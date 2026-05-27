#!/usr/bin/env python3
"""Export Ergo Discord dev chat and prepare docs-review leads."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = ROOT / "tools" / "state" / "discord-dev-digest"
DEFAULT_CHANNEL = "669989266478202917"
DEFAULT_REPO = ROOT.parent / "discord_summariser_ai"
DEFAULT_EXPORTER = (
    DEFAULT_REPO
    / "DiscordChatExporter"
    / "DiscordChatExporter-linux"
    / "mac"
    / "DiscordChatExporter.Cli.osx-arm64"
    / "DiscordChatExporter.Cli"
)

MESSAGE_RE = re.compile(r"^\[(?P<date>\d{2}/\d{2}/\d{4}) (?P<time>\d{2}:\d{2})\] (?P<author>.+)$")
URL_RE = re.compile(r"https?://[^\s<>)\]}\"']+")

TOPIC_PATTERNS: dict[str, tuple[list[str], list[str]]] = {
    "sidechains": (
        ["sidechain", "braid", "merged mining", "frontier", "evm", "serg", "frost", "relayer"],
        ["docs/uses/sidechains.md", "docs/uses/sidechains/sigma-chains.md", "docs/dev/protocol/scaling/layer2.md"],
    ),
    "nipopows": (
        ["nipopow", "suffix proof", "light client", "pow proof"],
        ["docs/dev/protocol/nipopows.md", "docs/dev/protocol/nipopow/nipopow_nodes.md"],
    ),
    "node networking": (
        ["handshake", "magic bytes", "peer", "ban", "unban", "p2p", "vlq"],
        ["docs/dev/p2p/p2p-handshake.md", "docs/node/peer-management.md", "docs/node/install/troubleshooting.md"],
    ),
    "node operations": (
        ["indexed node", "api", "swagger", "reverse proxy", "rate limit", "monitoring", "incident"],
        ["docs/operate-infrastructure.md", "docs/node/indexed-node.md", "docs/node/swagger.md"],
    ),
    "mining": (
        ["autolykos", "lithos", "pool", "miner", "hash", "merged-mined", "ethash"],
        ["docs/mining/mining-overview.md", "docs/mining/pool-ops.md", "docs/dev/protocol/autolykos-protocol.md"],
    ),
    "smart contracts": (
        ["ergoscript", "jit", "context extension", "avl", "fraud proof", "optimistic", "contract"],
        ["docs/dev/scs/ergoscript.md", "docs/node/jitc.md", "docs/dev/protocol/avl.md"],
    ),
    "wallets and dapps": (
        ["wallet", "nautilus", "satergo", "ergopay", "connector", "fleet", "appkit"],
        ["docs/wallets-overview.md", "docs/dev/wallets.md", "docs/dev/stack/fleet.md", "docs/dev/stack/appkit.md"],
    ),
    "standards": (
        ["eip", "standard", "reserved key", "extension block", "metadata"],
        ["docs/dev/wallet/eip-standards.md", "docs/dev/data-model/extension-section.md", "docs/roadmap.md"],
    ),
}


@dataclass
class Message:
    timestamp: str
    author: str
    body: str


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = value


def after_date(days: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=days)).date().isoformat()


def safe_filename(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-")


def run_export(args: argparse.Namespace, output_path: Path) -> None:
    load_dotenv(ROOT / ".env")
    token = os.environ.get(args.token_env)
    if not token:
        raise SystemExit(f"Missing {args.token_env} in environment or .env")

    exporter = Path(args.exporter).expanduser()
    if not exporter.exists():
        raise SystemExit(f"DiscordChatExporter not found: {exporter}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        str(exporter),
        "export",
        "--channel",
        args.channel,
        "--token",
        token,
        "--after",
        args.after,
        "--format",
        "PlainText",
        "--output",
        str(output_path),
    ]
    if args.before:
        command.extend(["--before", args.before])

    if args.dry_run:
        print(f"Would export channel {args.channel} after {args.after} to {output_path}")
        return

    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        stderr = result.stderr.replace(token, "[REDACTED]")
        stdout = result.stdout.replace(token, "[REDACTED]")
        raise SystemExit(f"Discord export failed ({result.returncode})\n{stdout}\n{stderr}")


def parse_plaintext(path: Path) -> list[Message]:
    messages: list[Message] = []
    current_author = ""
    current_time = ""
    current_lines: list[str] = []

    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = MESSAGE_RE.match(line)
        if match:
            if current_time and current_lines:
                messages.append(Message(current_time, current_author, "\n".join(current_lines).strip()))
            current_time = f"{match.group('date')} {match.group('time')}"
            current_author = match.group("author")
            current_lines = []
            continue
        if current_time:
            current_lines.append(line)

    if current_time and current_lines:
        messages.append(Message(current_time, current_author, "\n".join(current_lines).strip()))

    return [msg for msg in messages if msg.body and not msg.body.startswith("{Embed}")]


def topic_scores(messages: Iterable[Message]) -> tuple[Counter[str], dict[str, list[Message]]]:
    scores: Counter[str] = Counter()
    evidence: dict[str, list[Message]] = defaultdict(list)
    for msg in messages:
        text = msg.body.lower()
        for topic, (terms, _) in TOPIC_PATTERNS.items():
            hits = sum(1 for term in terms if term in text)
            if hits:
                scores[topic] += hits
                if len(evidence[topic]) < 5 and len(msg.body) > 40:
                    evidence[topic].append(msg)
    return scores, evidence


def doc_candidates(scores: Counter[str]) -> Counter[str]:
    candidates: Counter[str] = Counter()
    for topic, score in scores.items():
        for doc in TOPIC_PATTERNS[topic][1]:
            candidates[doc] += score
    return candidates


def important_messages(messages: Iterable[Message]) -> list[Message]:
    terms = [
        "released",
        "merged",
        "implemented",
        "tested",
        "roadmap",
        "should document",
        "docs",
        "breaking",
        "deprecated",
        "changed",
        "question",
        "issue",
        "bug",
        "api",
        "eip",
    ]
    picked = []
    for msg in messages:
        text = msg.body.lower()
        if any(term in text for term in terms) and len(msg.body) > 60:
            picked.append(msg)
    return picked[:25]


def excerpt(text: str, limit: int = 420) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1].rstrip() + "..."


def write_report(messages: list[Message], args: argparse.Namespace, export_path: Path, report_path: Path) -> None:
    scores, evidence = topic_scores(messages)
    candidates = doc_candidates(scores)
    links = Counter(url.rstrip(".,") for msg in messages for url in URL_RE.findall(msg.body))
    high_signal = important_messages(messages)

    lines = [
        "# Discord Dev Digest",
        "",
        f"- Channel: `{args.channel}`",
        f"- After: `{args.after}`",
        f"- Before: `{args.before or 'now'}`",
        f"- Export: `{export_path}`",
        f"- Messages parsed: {len(messages)}",
        "",
        "## Use This Safely",
        "",
        "Discord chat is a lead source, not a source of truth. Verify claims against repos, issues, releases, EIPs, or maintainer confirmation before changing docs.",
        "",
        "## Topic Signals",
        "",
    ]

    if scores:
        for topic, count in scores.most_common():
            lines.append(f"- **{topic}**: {count}")
    else:
        lines.append("- No strong topic signals found.")

    lines.extend(["", "## Candidate Docs To Review", ""])
    if candidates:
        for doc, score in candidates.most_common(20):
            exists = "exists" if (ROOT / doc).exists() else "missing"
            lines.append(f"- `{doc}` ({exists}, score {score})")
    else:
        lines.append("- No candidates found.")

    lines.extend(["", "## Mentioned Links", ""])
    for url, count in links.most_common(25):
        lines.append(f"- {url} ({count})")
    if not links:
        lines.append("- No links found.")

    lines.extend(["", "## Evidence Snippets", ""])
    for topic, msgs in sorted(evidence.items()):
        lines.append(f"### {topic}")
        lines.append("")
        for msg in msgs:
            lines.append(f"- `{msg.timestamp}` {msg.author}: {excerpt(msg.body)}")
        lines.append("")

    lines.extend(["## High-Signal Messages", ""])
    for msg in high_signal:
        lines.append(f"- `{msg.timestamp}` {msg.author}: {excerpt(msg.body)}")
    if not high_signal:
        lines.append("- None found.")

    lines.extend(
        [
            "",
            "## Codex Prompt",
            "",
            "```text",
            f"$caveman Read {report_path}. Treat Discord as leads only. For each candidate doc, verify claims against source repos/issues/EIPs before editing. Update docs naturally, add source_repos metadata when source-backed, then run source_watch, nav_audit, structure_audit, git diff --check, and mkdocs build.",
            "```",
            "",
        ]
    )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export Discord dev chat and prepare ErgoDocs review leads.")
    parser.add_argument("command", nargs="?", choices=["scan", "export", "analyze"], default="scan")
    parser.add_argument("--channel", default=DEFAULT_CHANNEL, help="Discord channel ID to export.")
    parser.add_argument("--days", type=int, default=31, help="Days back to scan when --after is omitted.")
    parser.add_argument("--after", help="Start date, YYYY-MM-DD. Defaults to today minus --days.")
    parser.add_argument("--before", help="Optional end date, YYYY-MM-DD.")
    parser.add_argument("--token-env", default="DISCORD_TOKEN", help="Environment variable containing Discord token.")
    parser.add_argument("--exporter", default=DEFAULT_EXPORTER.as_posix(), help="Path to DiscordChatExporter.Cli.")
    parser.add_argument("--input", type=Path, help="Existing PlainText export to analyze.")
    parser.add_argument("--output-dir", type=Path, default=STATE_DIR, help="Directory for export and report output.")
    parser.add_argument("--dry-run", action="store_true", help="Print intended export without calling Discord.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    args.after = args.after or after_date(args.days)
    stamp = f"{safe_filename(args.channel)}-after-{safe_filename(args.after)}"
    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
    export_path = args.input or output_dir / f"{stamp}.txt"
    report_path = output_dir / f"{stamp}-report.md"

    if args.command in {"scan", "export"} and not args.input:
        run_export(args, export_path)
    if args.command == "export":
        print(export_path)
        return 0
    if args.dry_run and not export_path.exists():
        return 0
    if not export_path.exists():
        raise SystemExit(f"Export file not found: {export_path}")

    messages = parse_plaintext(export_path)
    write_report(messages, args, export_path, report_path)
    print(report_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
