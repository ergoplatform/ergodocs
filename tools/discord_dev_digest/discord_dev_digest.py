#!/usr/bin/env python3
"""Export Ergo Discord chat and prepare task-specific review leads."""

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


ROOT = Path(__file__).resolve().parents[2]
STATE_DIR = ROOT / "tools" / "discord_dev_digest" / "state"
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
GITHUB_RE = re.compile(r"https?://(?:www\.)?github\.com/([^/\s#?]+)/([^/\s#?]+)")

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

ECOSYSTEM_TERMS = [
    "app",
    "bridge",
    "dapp",
    "dex",
    "explorer",
    "indexer",
    "launch",
    "mining pool",
    "project",
    "protocol",
    "released",
    "sdk",
    "service",
    "sidechain",
    "tool",
    "wallet",
]

PROJECT_STOPWORDS = {
    "also",
    "api",
    "app",
    "arxiv",
    "bitcoin",
    "cdn",
    "contextextension",
    "discord",
    "drive",
    "eips",
    "ergo",
    "ergoscript",
    "ergoforum",
    "ergoplatform",
    "eprint",
    "explorer",
    "github",
    "http",
    "https",
    "images",
    "images-ext-1",
    "mainnet",
    "matrix",
    "node",
    "pr",
    "scanner",
    "sdk",
    "scala",
    "sigma",
    "telegram",
    "tenor",
    "tests",
    "testnet",
    "there",
    "this",
    "utils",
    "what",
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


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def readable_name(value: str) -> str:
    value = re.sub(r"[-_]+", " ", value).strip()
    words = []
    for word in value.split():
        if word.isupper() or any(ch.isdigit() for ch in word):
            words.append(word)
        else:
            words.append(word[:1].upper() + word[1:])
    return " ".join(words)


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


def docs_index() -> tuple[set[str], str]:
    slugs = {path.stem.lower() for path in (ROOT / "docs").rglob("*.md")}
    slugs |= {slugify(path.stem) for path in (ROOT / "docs").rglob("*.md")}
    corpus = "\n".join(path.read_text(encoding="utf-8", errors="ignore").lower() for path in (ROOT / "docs").rglob("*.md"))
    return slugs, corpus


def normalize_github_repo(url: str) -> str | None:
    match = GITHUB_RE.match(url.rstrip(".,;:)]}"))
    if not match:
        return None
    owner = match.group(1).strip()
    repo = match.group(2).strip().removesuffix(".git")
    if not owner or not repo or repo.lower() in {"issues", "pull", "pulls", "tree", "blob"}:
        return None
    return f"{owner}/{repo}"


def github_category(repo: str) -> str:
    owner, name = repo.lower().split("/", 1)
    if owner in {"ergoplatform", "scorexfoundation", "input-output-hk"}:
        return "core/reference"
    if owner == "rosen-bridge":
        return "Rosen tooling"
    if owner in {"bettermoneylabs"}:
        return "Ergo adjacent protocol"
    if any(term in name for term in ("oracle", "dex", "stable", "piggy", "lithos", "nft", "wallet")):
        return "ecosystem project"
    if any(term in name for term in ("node", "sdk", "mcp", "proxy", "relay", "ergots", "transcripts")):
        return "developer tooling"
    if any(term in name for term in ("miden", "bitcoin", "btc", "wdk")):
        return "external/context"
    return "needs triage"


def github_repos(messages: Iterable[Message]) -> list[dict[str, object]]:
    _, docs_text = docs_index()
    repos: dict[str, dict[str, object]] = {}
    for msg in messages:
        for url in URL_RE.findall(msg.body):
            repo = normalize_github_repo(url)
            if not repo:
                continue
            owner, name = repo.lower().split("/", 1)
            slug = slugify(name)
            documented = (
                repo.lower() in docs_text
                or f"github.com/{repo.lower()}" in docs_text
                or name in docs_text
                or slug in docs_text
            )
            record = repos.setdefault(
                repo,
                {
                    "repo": repo,
                    "count": 0,
                    "links": Counter(),
                    "evidence": [],
                    "documented": documented,
                    "category": github_category(repo),
                    "owner": owner,
                    "name": name,
                    "slug": slug,
                },
            )
            record["count"] = int(record["count"]) + 1
            record["links"][url.rstrip(".,;:)]}")] += 1
            evidence = record["evidence"]
            if isinstance(evidence, list) and len(evidence) < 3:
                evidence.append(msg)
    return sorted(repos.values(), key=lambda item: (bool(item["documented"]), str(item["category"]), -int(item["count"]), str(item["repo"]).lower()))


def project_name_from_url(url: str) -> str | None:
    cleaned = url.rstrip(".,")
    match = re.match(r"https?://(?:www\.)?github\.com/([^/\s]+)/([^/\s#?]+)", cleaned)
    if match:
        owner = match.group(1).lower()
        repo = match.group(2)
        if owner not in {"ergoplatform", "scorexfoundation"} and repo.lower() not in {"issues", "pull", "pulls"}:
            return readable_name(repo)
        if owner in {"ergoplatform", "rosen-bridge"} and any(term in repo.lower() for term in ("wallet", "node", "app", "sdk", "stable")):
            return readable_name(repo)
        return None
    match = re.match(r"https?://(?:www\.)?([^/\s#?]+)", cleaned)
    if not match:
        return None
    domain = match.group(1).lower()
    if any(skip in domain for skip in ("cdn.", "discord.", "github.", "google.", "images-ext-", "twitter.", "x.com", "youtube.", "youtu.be")):
        return None
    root = domain.split(".")[0]
    if root in PROJECT_STOPWORDS or len(root) < 3:
        return None
    return readable_name(root)


def project_names_from_text(text: str) -> set[str]:
    names: set[str] = set()
    for url in URL_RE.findall(text):
        name = project_name_from_url(url)
        if name:
            names.add(name)

    patterns = [
        r"\b(?:called|named|project|protocol|tool|wallet|dapp|app|sidechain|bridge|pool|service)\s+([A-Z][A-Za-z0-9][A-Za-z0-9 ._-]{1,42})",
        r"\b([A-Z][A-Za-z0-9]+(?:[ -][A-Z][A-Za-z0-9]+){0,3})\s+(?:is|has|launched|released|ships|supports|integrates|works|uses)\b",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            raw = match.group(1).strip(" .,:;()[]{}")
            raw = re.sub(r"\s+(?:and|or|with|for|to|on|in)$", "", raw, flags=re.I)
            slug = slugify(raw)
            if len(slug) >= 3 and slug not in PROJECT_STOPWORDS and not slug.isdigit():
                names.add(readable_name(raw))
    return names


def ecosystem_projects(messages: Iterable[Message]) -> list[dict[str, object]]:
    page_slugs, docs_text = docs_index()
    projects: dict[str, dict[str, object]] = {}
    for msg in messages:
        body_lower = msg.body.lower()
        if not any(term in body_lower for term in ECOSYSTEM_TERMS):
            continue
        for name in project_names_from_text(msg.body):
            slug = slugify(name)
            if slug in PROJECT_STOPWORDS or len(slug) < 3 or slug.isdigit():
                continue
            record = projects.setdefault(
                slug,
                {
                    "name": name,
                    "count": 0,
                    "links": Counter(),
                    "evidence": [],
                    "has_page": slug in page_slugs,
                    "mentioned_in_docs": name.lower() in docs_text or slug in docs_text,
                },
            )
            record["count"] = int(record["count"]) + 1
            for url in URL_RE.findall(msg.body):
                record["links"][url.rstrip(".,")] += 1
            evidence = record["evidence"]
            if isinstance(evidence, list) and len(evidence) < 3:
                evidence.append(msg)
    return sorted(projects.values(), key=lambda item: (bool(item["has_page"]), -int(item["count"]), str(item["name"])))


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


def write_docs_report(messages: list[Message], args: argparse.Namespace, export_path: Path, report_path: Path) -> None:
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


def write_ecosystem_report(messages: list[Message], args: argparse.Namespace, export_path: Path, report_path: Path) -> None:
    projects = ecosystem_projects(messages)
    missing = [item for item in projects if not item["has_page"]]
    present = [item for item in projects if item["has_page"]]

    lines = [
        "# Discord Ecosystem Project Leads",
        "",
        f"- Channel: `{args.channel}`",
        f"- After: `{args.after}`",
        f"- Before: `{args.before or 'now'}`",
        f"- Export: `{export_path}`",
        f"- Messages parsed: {len(messages)}",
        "",
        "## Use This Safely",
        "",
        "Discord chat is a lead source, not a source of truth. Verify each project against its website, repository, release, or maintainer confirmation before adding docs.",
        "",
        "## Likely Missing Project Pages",
        "",
    ]

    if missing:
        for item in missing[:50]:
            links = item["links"]
            top_links = ", ".join(url for url, _ in links.most_common(3)) if isinstance(links, Counter) else ""
            note = "mentioned elsewhere in docs" if item["mentioned_in_docs"] else "not found in docs text"
            lines.append(f"- **{item['name']}** ({item['count']} mentions; {note})")
            if top_links:
                lines.append(f"  - Links: {top_links}")
    else:
        lines.append("- No likely missing project pages found.")

    lines.extend(["", "## Already Has A Likely Page", ""])
    for item in present[:50]:
        lines.append(f"- **{item['name']}** ({item['count']} mentions)")

    lines.extend(["", "## Evidence", ""])
    for item in missing[:25]:
        lines.append(f"### {item['name']}")
        lines.append("")
        evidence = item["evidence"]
        if isinstance(evidence, list):
            for msg in evidence:
                lines.append(f"- `{msg.timestamp}` {msg.author}: {excerpt(msg.body)}")
        lines.append("")

    lines.extend(
        [
            "## Codex Prompt",
            "",
            "```text",
            f"$caveman Read {report_path}. Treat Discord as leads only. Verify likely missing ecosystem projects against official sources, then add or update docs naturally where warranted. Do not create pages from Discord alone. Run nav_audit, structure_audit, source_watch --strict, git diff --check, and mkdocs build.",
            "```",
            "",
        ]
    )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def write_github_links_report(messages: list[Message], args: argparse.Namespace, export_path: Path, report_path: Path) -> None:
    repos = github_repos(messages)
    missing = [item for item in repos if not item["documented"]]
    present = [item for item in repos if item["documented"]]

    lines = [
        "# Discord GitHub Link Audit",
        "",
        f"- Channel: `{args.channel}`",
        f"- After: `{args.after}`",
        f"- Before: `{args.before or 'now'}`",
        f"- Export: `{export_path}`",
        f"- Messages parsed: {len(messages)}",
        f"- Unique GitHub repositories: {len(repos)}",
        "",
        "## Use This Safely",
        "",
        "Discord links are leads. Verify each missing repository against its README, releases, issues, or maintainer source before changing docs.",
        "",
        "## Not Mentioned In Docs",
        "",
    ]

    if missing:
        for item in missing:
            links = item["links"]
            top_links = ", ".join(url for url, _ in links.most_common(3)) if isinstance(links, Counter) else ""
            lines.append(f"- **{item['repo']}** ({item['count']} links; {item['category']})")
            if top_links:
                lines.append(f"  - Links: {top_links}")
    else:
        lines.append("- Every linked GitHub repository appears to be mentioned in docs text.")

    lines.extend(["", "## Already Mentioned In Docs", ""])
    if present:
        for item in sorted(present, key=lambda item: (-int(item["count"]), str(item["repo"]).lower())):
            lines.append(f"- **{item['repo']}** ({item['count']} links; {item['category']})")
    else:
        lines.append("- None.")

    lines.extend(["", "## Evidence For Missing Repositories", ""])
    for item in missing:
        lines.append(f"### {item['repo']}")
        lines.append("")
        evidence = item["evidence"]
        if isinstance(evidence, list):
            for msg in evidence:
                lines.append(f"- `{msg.timestamp}` {msg.author}: {excerpt(msg.body)}")
        lines.append("")

    lines.extend(
        [
            "## Codex Prompt",
            "",
            "```text",
            f"$caveman Read {report_path}. For every GitHub repo under Not Mentioned In Docs, verify whether it is Ergo-relevant or useful external dev context. Add or update docs naturally only where warranted, with source links. Leave context-only repos in this report if they do not belong in docs.",
            "```",
            "",
        ]
    )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def write_report(messages: list[Message], args: argparse.Namespace, export_path: Path, report_path: Path) -> None:
    if args.profile == "ecosystem":
        write_ecosystem_report(messages, args, export_path, report_path)
    elif args.profile == "github-links":
        write_github_links_report(messages, args, export_path, report_path)
    else:
        write_docs_report(messages, args, export_path, report_path)


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
    parser.add_argument(
        "--profile",
        choices=["docs", "ecosystem", "github-links"],
        default="docs",
        help="Analysis profile: docs review leads, ecosystem project discovery, or GitHub link audit.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print intended export without calling Discord.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    args.after = args.after or after_date(args.days)
    stamp = f"{safe_filename(args.channel)}-after-{safe_filename(args.after)}"
    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
    export_path = args.input or output_dir / f"{stamp}.txt"
    suffix = "report" if args.profile == "docs" else f"{args.profile}-report"
    report_path = output_dir / f"{stamp}-{suffix}.md"

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
