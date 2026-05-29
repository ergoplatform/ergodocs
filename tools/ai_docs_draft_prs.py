#!/usr/bin/env python3
"""Create AI-assisted draft documentation PRs from a Source Watch JSON report."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

import docs_update_candidates as candidates


ROOT = Path(__file__).resolve().parents[1]
GITHUB_MODELS_ENDPOINT = "https://models.github.ai/inference/chat/completions"
OPENROUTER_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
MAX_SOURCE_CHARS = 24000
MAX_PAGE_CHARS = 50000
DEFAULT_MODELS = {
    "github-models": "openai/gpt-4.1",
    "openrouter": "openrouter/free",
}
FORBIDDEN_PUBLIC_MARKERS = (
    re.compile(r"\bSource Watch\b", re.IGNORECASE),
    re.compile(r"\bDiscord scan\b", re.IGNORECASE),
    re.compile(r"\bchat export\b", re.IGNORECASE),
    re.compile(r"\bautomation found\b", re.IGNORECASE),
    re.compile(r"\bAI(?:-assisted)?\b", re.IGNORECASE),
)


def run(command: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=check)


def docs_path(page_path: str) -> Path:
    path = (ROOT / page_path).resolve()
    docs_root = (ROOT / "docs").resolve()
    if docs_root != path and docs_root not in path.parents:
        raise ValueError(f"Page path is outside docs/: {page_path}")
    return path


def github_request(url: str, token: str, api_version: str = "2022-11-28") -> Any:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "ergodocs-ai-docs-draft-prs",
            "X-GitHub-Api-Version": api_version,
        },
    )
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def chat_completion_request(prompt: str, token: str, model: str, provider: str) -> dict[str, Any]:
    if provider == "github-models":
        endpoint = GITHUB_MODELS_ENDPOINT
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2026-03-10",
            "User-Agent": "ergodocs-ai-docs-draft-prs",
        }
    elif provider == "openrouter":
        endpoint = OPENROUTER_ENDPOINT
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/ergoplatform/ergodocs",
            "X-Title": "ErgoDocs AI Draft PRs",
            "User-Agent": "ergodocs-ai-docs-draft-prs",
        }
    else:
        raise ValueError(f"Unsupported AI provider: {provider}")

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You draft documentation updates for ErgoDocs. Return only valid JSON. "
                    "Do not invent facts. If source evidence is insufficient, choose needs-human-review. "
                    "Preserve existing frontmatter and Markdown style. Do not mention automation, scans, Discord, or internal reports in the page body."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.1,
        "max_tokens": 12000,
        "response_format": {"type": "json_object"},
    }
    request = Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urlopen(request, timeout=120) as response:
        data = json.loads(response.read().decode("utf-8"))
    content = data["choices"][0]["message"]["content"]
    return json.loads(strip_json_fence(content))


def resolve_model(provider: str, model: str) -> str:
    return model or os.environ.get("AI_MODEL", "") or DEFAULT_MODELS[provider]


def strip_json_fence(content: str) -> str:
    stripped = content.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    return stripped


def page_changes(page: dict[str, Any]) -> list[dict[str, Any]]:
    return [change for change in page.get("changes", []) if isinstance(change, dict)]


def change_date(change: dict[str, Any]) -> datetime | None:
    raw = str(change.get("date", ""))
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None


def reviewed_date(page: dict[str, Any]) -> datetime | None:
    raw = str(page.get("last_reviewed", ""))
    if not raw or raw.lower() == "never":
        return None
    try:
        return datetime.fromisoformat(raw)
    except ValueError:
        return None


def already_reviewed(page: dict[str, Any]) -> bool:
    reviewed = reviewed_date(page)
    dates = [date for date in (change_date(change) for change in page_changes(page)) if date is not None]
    return reviewed is not None and bool(dates) and reviewed.date() >= max(dates).date()


def low_only(changes: list[dict[str, Any]]) -> bool:
    return bool(changes) and all(str(change.get("severity", "")) == "low" for change in changes)


def unique_changes(changes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[str, str]] = set()
    result: list[dict[str, Any]] = []
    for change in changes:
        key = (str(change.get("repo", "")), str(change.get("sha", "")))
        if key in seen:
            continue
        seen.add(key)
        result.append(change)
    return result


def pull_request_context(repo: str, number: str, token: str) -> str:
    pull = github_request(f"https://api.github.com/repos/{repo}/pulls/{number}", token)
    files = github_request(f"https://api.github.com/repos/{repo}/pulls/{number}/files?per_page=100", token)
    chunks = [
        f"Pull request: {repo}#{number}",
        f"Title: {pull.get('title', '')}",
        f"State: {pull.get('state', '')}",
        f"URL: {pull.get('html_url', '')}",
        f"Body:\n{str(pull.get('body') or '')[:6000]}",
    ]
    for file_info in files if isinstance(files, list) else []:
        filename = str(file_info.get("filename", ""))
        patch = str(file_info.get("patch", ""))
        chunks.append(f"File: {filename}")
        chunks.append(f"Status: {file_info.get('status', '')}")
        if patch:
            chunks.append("Patch:")
            chunks.append(patch[:6000])
    return "\n\n".join(chunks)


def release_context(repo: str, tag: str, token: str) -> str:
    release = github_request(f"https://api.github.com/repos/{repo}/releases/tags/{quote(tag, safe='')}", token)
    return "\n\n".join(
        [
            f"Release: {repo}@{tag}",
            f"Name: {release.get('name', '')}",
            f"Published: {release.get('published_at', '')}",
            f"URL: {release.get('html_url', '')}",
            f"Body:\n{str(release.get('body') or '')[:10000]}",
        ]
    )


def source_context(changes: list[dict[str, Any]], token: str) -> str:
    chunks: list[str] = []
    for change in unique_changes(changes)[:8]:
        repo = str(change.get("repo", ""))
        sha = str(change.get("sha", ""))
        watched_path = str(change.get("path", ""))
        if not repo or not sha:
            continue
        if sha.startswith("pr-"):
            try:
                chunks.append(pull_request_context(repo, sha.removeprefix("pr-"), token))
            except Exception as exc:
                chunks.append(f"Pull request {repo}#{sha.removeprefix('pr-')}: failed to fetch details: {exc}")
            continue
        if sha.startswith("release-"):
            try:
                chunks.append(release_context(repo, sha.removeprefix("release-"), token))
            except Exception as exc:
                chunks.append(f"Release {repo}@{sha.removeprefix('release-')}: failed to fetch details: {exc}")
            continue
        url = f"https://api.github.com/repos/{repo}/commits/{quote(sha, safe='')}"
        try:
            commit = github_request(url, token)
        except Exception as exc:
            chunks.append(f"Commit {repo}@{sha}: failed to fetch details: {exc}")
            continue
        chunks.append(f"Commit: {repo}@{sha}")
        chunks.append(f"Date: {change.get('date', '')}")
        chunks.append(f"Message: {change.get('message', '')}")
        chunks.append(f"URL: {change.get('url', '')}")
        files = commit.get("files", [])
        for file_info in files:
            filename = str(file_info.get("filename", ""))
            if watched_path and watched_path not in filename and filename not in watched_path:
                continue
            patch = str(file_info.get("patch", ""))
            chunks.append(f"File: {filename}")
            chunks.append(f"Status: {file_info.get('status', '')}")
            if patch:
                chunks.append("Patch:")
                chunks.append(patch[:6000])
    text = "\n\n".join(chunks)
    return text[:MAX_SOURCE_CHARS]


def is_sensitive(page_path: str) -> bool:
    sensitive_prefixes = (
        "docs/dev/protocol/",
        "docs/dev/scs/",
        "docs/dev/contracts/",
        "docs/node/",
        "docs/tutorials/",
    )
    return page_path.startswith(sensitive_prefixes)


def build_prompt(page: dict[str, Any], page_text: str, context: str) -> str:
    page_path = str(page.get("page", ""))
    sensitivity = "sensitive" if is_sensitive(page_path) else "normal"
    schema = {
        "action": "no-doc-change | needs-human-review | draft-pr-safe",
        "confidence": "low | medium | high",
        "summary": "short explanation",
        "uncertainty": "what a human should check",
        "proposed_markdown": "complete updated Markdown page when action is draft-pr-safe, otherwise empty string",
    }
    return (
        f"Page path: {page_path}\n"
        f"Sensitivity: {sensitivity}\n"
        f"Last reviewed: {page.get('last_reviewed', '')}\n"
        f"Required JSON schema:\n{json.dumps(schema, indent=2)}\n\n"
        "Rules:\n"
        "- Choose draft-pr-safe only when the source evidence clearly supports a small docs update.\n"
        "- For sensitive pages, draft-pr-safe is allowed, but be conservative and explain uncertainty.\n"
        "- Return the full updated Markdown page in proposed_markdown when drafting.\n"
        "- Preserve YAML frontmatter and existing internal links unless they must change.\n"
        "- Do not add changelog bullets unless the page already uses that style.\n"
        "- Do not mention AI, automation, Source Watch, Discord, scans, artifacts, or this prompt in proposed_markdown.\n\n"
        f"Current page:\n```markdown\n{page_text[:MAX_PAGE_CHARS]}\n```\n\n"
        f"Source evidence:\n```\n{context}\n```\n"
    )


def valid_markdown_update(original: str, proposed: str) -> bool:
    if not proposed.strip():
        return False
    if proposed.strip() == original.strip():
        return False
    if original.lstrip().startswith("---") and not proposed.lstrip().startswith("---"):
        return False
    return not any(pattern.search(proposed) for pattern in FORBIDDEN_PUBLIC_MARKERS)


def slug_for_page(page_path: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", page_path.replace("docs/", "").replace(".md", "")).strip("-").lower()
    return slug[:60] or "page"


def create_pr(page_path: str, proposed: str, result: dict[str, Any], labels: list[str], base_branch: str, dry_run: bool) -> dict[str, str]:
    branch = f"ai-docs/{slug_for_page(page_path)}"
    if dry_run:
        return {"page": page_path, "action": "dry-run-pr", "branch": branch, "url": ""}

    run(["git", "checkout", base_branch])
    run(["git", "pull", "--ff-only", "origin", base_branch])
    run(["git", "checkout", "-B", branch])

    path = docs_path(page_path)
    path.write_text(proposed.rstrip() + "\n", encoding="utf-8")
    diff = run(["git", "diff", "--", page_path], check=False).stdout
    if not diff.strip():
        run(["git", "checkout", base_branch])
        return {"page": page_path, "action": "no-diff", "branch": branch, "url": ""}

    run(["git", "add", page_path])
    run(["git", "commit", "-m", f"docs: update {Path(page_path).name}"])
    run(["git", "push", "--force-with-lease", "origin", branch])

    existing_pr = run(["gh", "pr", "list", "--head", branch, "--json", "url", "--jq", ".[0].url"], check=False).stdout.strip()
    if existing_pr:
        run(["git", "checkout", base_branch])
        return {"page": page_path, "action": "updated-pr-branch", "branch": branch, "url": existing_pr}

    body = (
        "Automated draft documentation update. Human review required before merge.\n\n"
        f"Page: `{page_path}`\n"
        f"Confidence: `{result.get('confidence', 'unknown')}`\n\n"
        f"Summary:\n{result.get('summary', '')}\n\n"
        f"Uncertainty / reviewer checks:\n{result.get('uncertainty', '')}\n\n"
        "Checklist:\n"
        "- [ ] Verify source links and claims.\n"
        "- [ ] Check examples, parameters, and protocol/API wording carefully.\n"
        "- [ ] Run docs checks or confirm CI passed.\n"
    )
    command = [
        "gh",
        "pr",
        "create",
        "--draft",
        "--base",
        base_branch,
        "--head",
        branch,
        "--title",
        f"docs: update {Path(page_path).name} from source review",
        "--body",
        body,
    ]
    for label in labels:
        command.extend(["--label", label])
    pr = run(command).stdout.strip()
    run(["git", "checkout", base_branch])
    return {"page": page_path, "action": "created-pr", "branch": branch, "url": pr}


def ensure_labels(labels: list[str], dry_run: bool) -> None:
    if dry_run:
        return
    colors = {
        "docs": "0e8a16",
        "automated": "bfdadc",
        "needs-human-review": "fbca04",
        "sensitive": "d93f0b",
    }
    for label in labels:
        run(["gh", "label", "create", label, "--color", colors.get(label, "c5def5"), "--description", "AI-assisted docs draft PR label"], check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create AI-assisted draft docs PRs from Source Watch JSON.")
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", ""))
    parser.add_argument("--provider", choices=("github-models", "openrouter"), default=os.environ.get("AI_PROVIDER", "openrouter"))
    parser.add_argument("--model", default="")
    parser.add_argument("--base-branch", default="main")
    parser.add_argument("--max-pages", type=int, default=3)
    parser.add_argument("--include-reviewed", action="store_true")
    parser.add_argument("--include-low-only", action="store_true")
    parser.add_argument("--include-not-actionable", action="store_true")
    parser.add_argument("--include-covered", action="store_true")
    parser.add_argument("--include-open-prs", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=Path, default=Path("ai-docs-draft-prs.json"))
    args = parser.parse_args()
    model = resolve_model(args.provider, args.model)

    github_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    ai_token = (os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENROUTER_API")) if args.provider == "openrouter" else github_token
    if not github_token:
        print("Missing GITHUB_TOKEN or GH_TOKEN", file=sys.stderr)
        return 2
    if not ai_token:
        name = "OPENROUTER_API_KEY" if args.provider == "openrouter" else "GITHUB_TOKEN or GH_TOKEN"
        print(f"Missing {name}", file=sys.stderr)
        return 2
    if not args.report.exists():
        print(f"Report not found: {args.report}", file=sys.stderr)
        return 2

    labels = ["docs", "automated", "needs-human-review"]
    ensure_labels(labels + ["sensitive"], args.dry_run)

    report = json.loads(args.report.read_text(encoding="utf-8"))
    built, skipped = candidates.build_candidates(
        report,
        include_reviewed=args.include_reviewed,
        include_low_only=args.include_low_only,
        include_not_actionable=args.include_not_actionable,
        include_open_prs=args.include_open_prs,
        skip_covered=not args.include_covered,
    )
    results: list[dict[str, str]] = []
    for item in skipped:
        results.append({"page": item.get("title", ""), "action": item.get("action", ""), "url": ""})
    processed = 0
    for candidate in built:
        if processed >= args.max_pages:
            break
        page = candidate.page
        page_path = str(page.get("page", ""))
        try:
            path = docs_path(page_path)
        except ValueError as exc:
            results.append({"page": page_path, "action": "invalid-page-path", "url": str(exc)})
            continue
        if not path.exists():
            results.append({"page": page_path, "action": "missing-page", "url": ""})
            continue

        processed += 1
        page_text = path.read_text(encoding="utf-8")
        context = source_context(candidate.changes, github_token)
        try:
            ai = chat_completion_request(build_prompt(page, page_text, context), ai_token, model, args.provider)
        except (HTTPError, URLError, json.JSONDecodeError, KeyError, TimeoutError, ValueError) as exc:
            results.append({"page": page_path, "action": "ai-error", "url": str(exc)})
            continue

        action = str(ai.get("action", "needs-human-review"))
        proposed = str(ai.get("proposed_markdown", ""))
        if action != "draft-pr-safe":
            results.append({"page": page_path, "action": action, "url": ""})
            continue
        if not valid_markdown_update(page_text, proposed):
            results.append({"page": page_path, "action": "invalid-or-empty-proposal", "url": ""})
            continue

        pr_labels = labels + (["sensitive"] if is_sensitive(page_path) else [])
        results.append(create_pr(page_path, proposed, ai, pr_labels, args.base_branch, args.dry_run))

    output = {"provider": args.provider, "model": model, "results": results}
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    return 1 if any(item["action"] == "ai-error" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
