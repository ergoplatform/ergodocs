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
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
OPENROUTER_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
MAX_SOURCE_CHARS = 24000
MAX_PAGE_CHARS = 50000
DEFAULT_MODELS = {
    "github-models": "openai/gpt-4.1",
    "openai": "gpt-5.4-mini",
    "openrouter": "openrouter/free",
}
FORBIDDEN_PUBLIC_MARKERS = (
    re.compile(r"\bSource Watch\b", re.IGNORECASE),
    re.compile(r"\bDiscord scan\b", re.IGNORECASE),
    re.compile(r"\bchat export\b", re.IGNORECASE),
    re.compile(r"\bautomation found\b", re.IGNORECASE),
    re.compile(r"\bAI[- ]assisted draft\b", re.IGNORECASE),
    re.compile(r"\bAI[- ]generated\b", re.IGNORECASE),
)
AUTOMATION_AUTHOR_EMAILS = {"actions@github.com"}
AUTOMATION_AUTHOR_NAMES = {"ergodocs automation", "github-actions[bot]"}
VALID_ACTIONS = {"no-doc-change", "needs-human-review", "draft-pr-safe"}
VALID_CONFIDENCE = {"low", "medium", "high"}


def run(command: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=check)


def docs_path(page_path: str) -> Path:
    path = (ROOT / page_path).resolve()
    docs_root = (ROOT / "docs").resolve()
    if docs_root != path and docs_root not in path.parents:
        raise ValueError(f"Page path is outside docs/: {page_path}")
    return path


def safe_repo_path(repo_path: str) -> Path:
    path = (ROOT / repo_path).resolve()
    allowed_roots = [(ROOT / "docs").resolve()]
    if not any(root == path or root in path.parents for root in allowed_roots):
        raise ValueError(f"Path is outside allowed generated areas: {repo_path}")
    return path


def rel_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


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
    elif provider == "openai":
        endpoint = OPENAI_ENDPOINT
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
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
        "response_format": {"type": "json_object"},
    }
    if provider == "openai":
        payload["max_completion_tokens"] = 12000
    else:
        payload["max_tokens"] = 12000
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


def normalize_model_response(raw: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError("model response is not an object")
    action = raw.get("action")
    confidence = raw.get("confidence")
    if action not in VALID_ACTIONS:
        raise ValueError(f"invalid model action: {action!r}")
    if confidence not in VALID_CONFIDENCE:
        raise ValueError(f"invalid model confidence: {confidence!r}")
    normalized = {
        "action": action,
        "confidence": confidence,
        "summary": raw.get("summary", ""),
        "uncertainty": raw.get("uncertainty", ""),
        "proposed_markdown": raw.get("proposed_markdown", ""),
    }
    for key in ("summary", "uncertainty", "proposed_markdown"):
        if not isinstance(normalized[key], str):
            raise ValueError(f"model field {key!r} is not a string")
    return normalized


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---\n", 4)
    if end == -1:
        return ""
    return text[4:end]


def frontmatter_has_key(text: str, key: str) -> bool:
    return bool(re.search(rf"^{re.escape(key)}\s*:", frontmatter(text), re.MULTILINE))


def frontmatter_value(text: str, key: str) -> str:
    lines = frontmatter(text).splitlines()
    result: list[str] = []
    collecting = False
    for line in lines:
        if re.match(rf"^{re.escape(key)}\s*:", line):
            collecting = True
            result.append(line.rstrip())
            continue
        if collecting:
            if line.startswith(" ") or not line.strip():
                result.append(line.rstrip())
                continue
            break
    return "\n".join(result).strip()


def first_h1(text: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def heading_count(text: str) -> int:
    return len(re.findall(r"^#{1,6}\s+", text, re.MULTILINE))


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


def evidence_links(changes: list[dict[str, Any]], limit: int = 8) -> list[str]:
    links: list[str] = []
    for change in unique_changes(changes):
        repo = str(change.get("repo", ""))
        sha = str(change.get("sha", ""))
        url = str(change.get("url", ""))
        if not url and repo and sha.startswith("release-"):
            url = f"https://github.com/{repo}/releases/tag/{sha.removeprefix('release-')}"
        elif not url and repo and sha.startswith("pr-"):
            url = f"https://github.com/{repo}/pull/{sha.removeprefix('pr-')}"
        elif not url and repo and sha:
            url = f"https://github.com/{repo}/commit/{sha}"
        if url and url not in links:
            links.append(url)
        if len(links) >= limit:
            break
    return links


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
        "proposed_markdown": "complete updated Markdown page when a plausible update can be drafted, otherwise empty string",
    }
    return (
        f"Page path: {page_path}\n"
        f"Sensitivity: {sensitivity}\n"
        f"Last reviewed: {page.get('last_reviewed', '')}\n"
        f"Required JSON schema:\n{json.dumps(schema, indent=2)}\n\n"
        "Rules:\n"
        "- Choose draft-pr-safe only when the source evidence clearly supports a small docs update.\n"
        "- Choose needs-human-review when the source evidence suggests a docs change but a human must verify sensitive wording.\n"
        "- For needs-human-review, still return the best complete updated Markdown page when possible.\n"
        "- For sensitive pages, draft-pr-safe is allowed, but be conservative and explain uncertainty.\n"
        "- Return the full updated Markdown page in proposed_markdown when any draft is useful for review.\n"
        "- Preserve YAML frontmatter and existing internal links unless they must change.\n"
        f"- If the page is updated and has last_reviewed frontmatter, set last_reviewed to {datetime.utcnow().date().isoformat()}.\n"
        "- Do not add changelog bullets unless the page already uses that style.\n"
        "- Do not mention AI, automation, Source Watch, Discord, scans, artifacts, or this prompt in proposed_markdown.\n\n"
        f"Current page:\n```markdown\n{page_text[:MAX_PAGE_CHARS]}\n```\n\n"
        f"Source evidence:\n```\n{context}\n```\n"
    )


def valid_markdown_update(original: str, proposed: str) -> bool:
    original_stripped = original.strip()
    proposed_stripped = proposed.strip()
    if not proposed_stripped:
        return False
    if proposed_stripped == original_stripped:
        return False
    if original.lstrip().startswith("---") and not proposed.lstrip().startswith("---"):
        return False
    for key in ("source_repos", "source_of_truth"):
        if frontmatter_has_key(original, key) and frontmatter_value(original, key) != frontmatter_value(proposed, key):
            return False
    original_h1 = first_h1(original)
    if original_h1 and first_h1(proposed) != original_h1:
        return False
    if len(proposed_stripped) < int(len(original_stripped) * 0.7):
        return False
    original_headings = heading_count(original)
    if original_headings and heading_count(proposed) < max(1, int(original_headings * 0.75)):
        return False
    return not any(pattern.search(proposed) for pattern in FORBIDDEN_PUBLIC_MARKERS)


def slug_for_page(page_path: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", page_path.replace("docs/", "").replace(".md", "")).strip("-").lower()
    return slug[:60] or "page"


def pr_body(page_path: str, result: dict[str, Any]) -> str:
    links = result.get("_evidence_links", [])
    evidence = "\n".join(f"- {link}" for link in links) if isinstance(links, list) and links else "- No direct source links captured."
    return (
        "Automated documentation addition, please highlight any errors.\n\n"
        "Human review required before merge.\n\n"
        f"Page: `{page_path}`\n"
        f"Model: `{result.get('_model', 'unknown')}`\n"
        f"Action: `{result.get('action', 'unknown')}`\n"
        f"Confidence: `{result.get('confidence', 'unknown')}`\n\n"
        f"Summary:\n{result.get('summary', '')}\n\n"
        f"Uncertainty / reviewer checks:\n{result.get('uncertainty', '')}\n\n"
        f"Source evidence:\n{evidence}\n\n"
        "Checklist:\n"
        "- [ ] Verify source links and claims.\n"
        "- [ ] Check examples, parameters, and protocol/API wording carefully.\n"
        "- [ ] Confirm `last_reviewed` is appropriate.\n"
        "- [ ] Run docs checks or confirm CI passed.\n"
    )


def issue_body(page_path: str, result: dict[str, Any]) -> str:
    return pr_body(page_path, result) + "\nNo safe Markdown draft was produced, so no branch was pushed.\n"


def edit_existing_pr(pr_url: str, body: str, labels: list[str]) -> None:
    command = ["gh", "pr", "edit", pr_url, "--body", body]
    for label in labels:
        command.extend(["--add-label", label])
    run(command)


def existing_issue_url(title: str) -> str:
    output = run(["gh", "issue", "list", "--state", "open", "--search", title, "--json", "url,title"], check=False).stdout
    try:
        issues = json.loads(output)
    except json.JSONDecodeError:
        return ""
    return next((str(issue.get("url", "")) for issue in issues if issue.get("title") == title), "")


def create_or_update_issue(page_path: str, result: dict[str, Any], labels: list[str], dry_run: bool) -> dict[str, str]:
    title = f"Docs review needed: {Path(page_path).name}"
    if dry_run:
        return {"page": page_path, "action": "dry-run-issue", "url": ""}
    body = issue_body(page_path, result)
    issue = existing_issue_url(title)
    if issue:
        command = ["gh", "issue", "edit", issue, "--body", body]
        for label in labels:
            command.extend(["--add-label", label])
        run(command)
        return {"page": page_path, "action": "updated-issue", "url": issue}
    command = ["gh", "issue", "create", "--title", title, "--body", body]
    for label in labels:
        command.extend(["--label", label])
    url = run(command).stdout.strip()
    return {"page": page_path, "action": "created-issue", "url": url}


def existing_pr_url(branch: str) -> str:
    return run(["gh", "pr", "list", "--head", branch, "--json", "url", "--jq", ".[0].url"], check=False).stdout.strip()


def branch_exists(branch: str) -> bool:
    output = run(["git", "ls-remote", "--heads", "origin", branch], check=False).stdout.strip()
    return bool(output)


def branch_owned_by_automation(branch: str) -> bool:
    if not branch_exists(branch):
        return True
    run(["git", "fetch", "origin", f"{branch}:refs/remotes/origin/{branch}"])
    email = run(["git", "log", "-1", "--format=%ae", f"origin/{branch}"]).stdout.strip()
    name = run(["git", "log", "-1", "--format=%an", f"origin/{branch}"]).stdout.strip()
    return email in AUTOMATION_AUTHOR_EMAILS or name in AUTOMATION_AUTHOR_NAMES


def pre_push_checks() -> None:
    run(["git", "diff", "--check"])
    run(["git", "diff", "--cached", "--check"])
    run([sys.executable, "tools/nav_audit.py", "--strict"])
    run([sys.executable, "tools/structure_audit.py", "--strict"])
    run([sys.executable, "-m", "mkdocs", "build", "--site-dir", "/tmp/ergodocs-ai-pr-check"])


def create_pr(
    page_path: str,
    proposed: str,
    result: dict[str, Any],
    labels: list[str],
    base_branch: str,
    dry_run: bool,
    target_path: str | None = None,
) -> dict[str, str]:
    branch = f"ai-docs/{slug_for_page(page_path)}"
    if dry_run:
        return {"page": page_path, "action": "dry-run-pr", "branch": branch, "url": ""}
    if not branch_owned_by_automation(branch):
        pr_url = existing_pr_url(branch)
        return {"page": page_path, "action": "protected-existing-branch", "branch": branch, "url": pr_url}

    try:
        run(["git", "checkout", base_branch])
        run(["git", "pull", "--ff-only", "origin", base_branch])
        run(["git", "checkout", "-B", branch])

        write_path = target_path or page_path
        path = safe_repo_path(write_path)
        write_path = rel_path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(proposed.rstrip() + "\n", encoding="utf-8")
        body = pr_body(page_path, result)
        existing_pr = existing_pr_url(branch)
        diff = run(["git", "diff", "--", write_path], check=False).stdout
        if not diff.strip():
            if existing_pr:
                edit_existing_pr(existing_pr, body, labels)
                return {"page": page_path, "action": "updated-pr-body", "branch": branch, "url": existing_pr}
            return {"page": page_path, "action": "no-diff", "branch": branch, "url": ""}

        run(["git", "add", write_path])
        pre_push_checks()
        run(["git", "commit", "-m", f"docs: update {Path(page_path).name}"])
        run(["git", "push", "--force-with-lease", "origin", branch])

        existing_pr = existing_pr_url(branch)
        if existing_pr:
            edit_existing_pr(existing_pr, body, labels)
            return {"page": page_path, "action": "updated-pr-branch", "branch": branch, "url": existing_pr}

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
        return {"page": page_path, "action": "created-pr", "branch": branch, "url": pr}
    finally:
        run(["git", "checkout", base_branch], check=False)


def create_review_pr(page_path: str, page_text: str, result: dict[str, Any], labels: list[str], base_branch: str, dry_run: bool) -> dict[str, str]:
    proposed = str(result.get("proposed_markdown", ""))
    if not valid_markdown_update(page_text, proposed):
        return create_or_update_issue(page_path, result, labels, dry_run)
    return create_pr(page_path, proposed, result, labels, base_branch, dry_run)


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
    parser.add_argument("--provider", choices=("github-models", "openai", "openrouter"), default=os.environ.get("AI_PROVIDER", "openai"))
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
    ai_token = {
        "github-models": github_token,
        "openai": os.environ.get("OPENAI_API_KEY"),
        "openrouter": os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENROUTER_API"),
    }[args.provider]
    if not github_token:
        print("Missing GITHUB_TOKEN or GH_TOKEN", file=sys.stderr)
        return 2
    if not ai_token:
        name = {
            "github-models": "GITHUB_TOKEN or GH_TOKEN",
            "openai": "OPENAI_API_KEY",
            "openrouter": "OPENROUTER_API_KEY",
        }[args.provider]
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
            ai = normalize_model_response(chat_completion_request(build_prompt(page, page_text, context), ai_token, model, args.provider))
        except (HTTPError, URLError, json.JSONDecodeError, KeyError, TimeoutError, ValueError) as exc:
            results.append({"page": page_path, "action": "ai-error", "url": str(exc)})
            continue
        ai["_model"] = model
        ai["_evidence_links"] = evidence_links(candidate.changes)

        action = str(ai.get("action", "needs-human-review"))
        proposed = str(ai.get("proposed_markdown", ""))
        if action == "no-doc-change":
            results.append({"page": page_path, "action": action, "url": ""})
            continue
        pr_labels = labels + (["sensitive"] if is_sensitive(page_path) else [])
        if action == "needs-human-review":
            results.append(create_review_pr(page_path, page_text, ai, pr_labels, args.base_branch, args.dry_run))
            continue
        if action != "draft-pr-safe":
            ai["uncertainty"] = f"Unexpected model action: {action}. Human review required."
            results.append(create_review_pr(page_path, page_text, ai, pr_labels, args.base_branch, args.dry_run))
            continue
        if not valid_markdown_update(page_text, proposed):
            ai["uncertainty"] = "Model marked draft-pr-safe, but Markdown failed safety validation. Human review required."
            results.append(create_or_update_issue(page_path, ai, pr_labels, args.dry_run))
            continue

        results.append(create_pr(page_path, proposed, ai, pr_labels, args.base_branch, args.dry_run))

    output = {"provider": args.provider, "model": model, "results": results}
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    if args.dry_run:
        return 0
    return 1 if any(item["action"] == "ai-error" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
