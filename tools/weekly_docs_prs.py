#!/usr/bin/env python3
"""Open page-specific documentation update issues from Source Watch candidates."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import docs_update_candidates as candidates


def github_request(method: str, url: str, token: str, payload: dict[str, Any] | None = None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "ergodocs-weekly-docs-prs",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = Request(url, data=data, headers=headers, method=method)
    with urlopen(request, timeout=20) as response:
        raw = response.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def github_get(url: str, token: str) -> Any:
    return github_request("GET", url, token)


def format_http_error(exc: HTTPError) -> str:
    try:
        body = json.loads(exc.read().decode("utf-8"))
    except Exception:
        body = {}
    if isinstance(body, dict) and body.get("message"):
        return f"HTTP {exc.code}: {body['message']}"
    return f"HTTP {exc.code}: {exc.reason}"


def safe_login(login: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9-]{1,39}", login):
        return ""
    if login.endswith("[bot]") or login.lower().endswith("-bot"):
        return ""
    return login


def watched_sources(page: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    for source in page.get("sources", []):
        repo = source.get("repo", "")
        branch = source.get("branch", "")
        for path in source.get("paths", []):
            source_path = path.get("path", "")
            if repo and source_path:
                lines.append(f"{repo}@{branch}/{source_path}")
    return lines


def body_for_candidate(candidate: candidates.Candidate, report: dict[str, Any], artifact_url: str, window: str) -> str:
    changes = candidates.unique_changes(candidate.changes)
    authors = sorted({safe_login(str(change.get("author_login", ""))) for change in changes})
    authors = [author for author in authors if author]
    page = candidate.page

    lines = [
        "Automated documentation update lead.",
        "",
        f"Likely update: add or adjust documentation for **{candidate.subject}**.",
        "Please verify the source links, then update the page if the feature or behavior is not already covered.",
        "",
        "Discord is treated as leads only; docs changes must be verified against source repos, releases, issues, EIPs, or maintainer confirmation.",
        "",
        f"Page: `{candidate.page_path}`",
        f"Review window: `{window}`",
        f"Last reviewed: `{page.get('last_reviewed') or 'missing'}`",
        f"Generated: `{report.get('generated', '')}`",
        "",
        "Why this issue exists:",
        candidate.reason,
        "",
    ]

    sources = watched_sources(page)
    if sources:
        lines.extend(["Watched paths for this page:"])
        for source in sources:
            lines.append(f"- `{source}`")
        lines.append("")

    if authors:
        lines.extend(["Possible reviewers from source changes:", ", ".join(authors), ""])

    if artifact_url:
        lines.extend(["Weekly report artifact:", artifact_url, ""])

    lines.extend(["Likely relevant source changes:", ""])
    for change in changes:
        author = safe_login(str(change.get("author_login", ""))) or str(change.get("author_login", "") or "unknown")
        paths = ", ".join(f"`{path}`" for path in change.get("paths", [])) or f"`{change.get('path', '')}`"
        lines.append(
            f"- `{change.get('repo', '')}` {change.get('date', '')} `{change.get('sha', '')}` "
            f"[{change.get('severity', 'unknown')}] {change.get('message', '')} ({author})"
        )
        lines.append(f"  Paths: {paths}")
        if change.get("url"):
            lines.append(f"  {change['url']}")

    source_of_truth = page.get("source_of_truth") or []
    if source_of_truth:
        lines.extend(["", "Source of truth:"])
        for source in source_of_truth:
            lines.append(f"- {source}")

    lines.extend(
        [
            "",
            "Before closing:",
            "- Verify source changes against durable upstream sources.",
            "- Add the missing feature, behavior, option, endpoint, or caveat naturally if it is not already covered.",
            "- If the page already covers the change, comment briefly and close as already covered.",
            "- Do not mention Discord scans or internal reports in public docs.",
            "- Run `source_watch.py scan --strict`, `nav_audit.py --strict`, `structure_audit.py --strict`, `git diff --check`, and `mkdocs build`.",
        ]
    )
    return "\n".join(lines) + "\n"


def find_issue(repo: str, title: str, token: str) -> dict[str, Any] | None:
    query = urlencode({"state": "open", "per_page": 100})
    issues = github_get(f"https://api.github.com/repos/{repo}/issues?{query}", token)
    for issue in issues:
        if issue.get("title") == title and "pull_request" not in issue:
            return issue
    return None


def source_watch_issues(repo: str, token: str) -> list[dict[str, Any]]:
    query = urlencode({"state": "open", "labels": "source-watch", "per_page": 100})
    issues = github_get(f"https://api.github.com/repos/{repo}/issues?{query}", token)
    return [issue for issue in issues if "pull_request" not in issue]


def create_or_update_issue(repo: str, title: str, body: str, labels: list[str], token: str, dry_run: bool) -> dict[str, str]:
    if dry_run:
        return {"title": title, "action": "dry-run", "url": ""}

    existing = find_issue(repo, title, token)
    if existing:
        issue = github_request("PATCH", existing["url"], token, {"body": body, "labels": labels})
        return {"title": title, "action": "updated", "url": issue.get("html_url", "")}

    issue = github_request("POST", f"https://api.github.com/repos/{repo}/issues", token, {"title": title, "body": body, "labels": labels})
    return {"title": title, "action": "created", "url": issue.get("html_url", "")}


def close_stale_issues(repo: str, active_titles: set[str], token: str, dry_run: bool) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for issue in source_watch_issues(repo, token):
        title = str(issue.get("title", ""))
        if title in active_titles:
            continue
        if not (title.startswith("Docs review needed") or title.startswith("Add info on ")):
            continue
        if dry_run:
            results.append({"title": title, "action": "dry-run-close-stale", "url": str(issue.get("html_url", ""))})
            continue
        comment_url = str(issue.get("comments_url", ""))
        issue_url = str(issue.get("url", ""))
        if comment_url:
            github_request(
                "POST",
                comment_url,
                token,
                {"body": "Closing because the latest Source Watch candidate pass no longer marks this page change as actionable."},
            )
        github_request("PATCH", issue_url, token, {"state": "closed"})
        results.append({"title": title, "action": "closed-stale", "url": str(issue.get("html_url", ""))})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Create per-page docs update issues from Source Watch JSON.")
    parser.add_argument("--report", required=True, type=Path, help="Source Watch JSON report.")
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", ""), help="GitHub repo, owner/name.")
    parser.add_argument("--artifact-url", default="", help="Workflow artifact or run URL to include.")
    parser.add_argument("--window", default="", help="Review window label to include in issue bodies.")
    parser.add_argument("--include-reviewed", action="store_true", help="Open issues even when last_reviewed is on/after latest source change.")
    parser.add_argument("--include-low-only", action="store_true", help="Open issues when all matching source changes are low severity.")
    parser.add_argument("--include-not-actionable", action="store_true", help="Open issues even when no doc-relevant signal is found.")
    parser.add_argument("--include-covered", action="store_true", help="Open issues even when the page text already appears to mention the subject.")
    parser.add_argument("--close-stale", action="store_true", help="Close old source-watch issues not present in the current candidate set.")
    parser.add_argument("--output", type=Path, help="Write JSON issue action summary to this path.")
    parser.add_argument("--label", action="append", help="Label to apply to created or updated issues. Repeatable.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned issue actions without writing.")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token and not args.dry_run:
        print("Missing GITHUB_TOKEN or GH_TOKEN", file=sys.stderr)
        return 2
    if not args.repo:
        print("Missing --repo or GITHUB_REPOSITORY", file=sys.stderr)
        return 2
    if not args.report.exists():
        print(f"Report not found: {args.report}", file=sys.stderr)
        return 2

    report = json.loads(args.report.read_text(encoding="utf-8"))
    labels = args.label or ["docs", "source-watch", "automated"]
    window = args.window or "unspecified"
    built, skipped = candidates.build_candidates(
        report,
        include_reviewed=args.include_reviewed,
        include_low_only=args.include_low_only,
        include_not_actionable=args.include_not_actionable,
        skip_covered=not args.include_covered,
    )

    results: list[dict[str, str]] = [*skipped]
    active_titles = {candidate.title for candidate in built}
    for candidate in built:
        body = body_for_candidate(candidate, report, args.artifact_url, window)
        try:
            results.append(create_or_update_issue(args.repo, candidate.title, body, labels, token or "", args.dry_run))
        except HTTPError as exc:
            results.append({"title": candidate.title, "action": "error", "url": format_http_error(exc)})

    if args.close_stale and (token or args.dry_run):
        try:
            results.extend(close_stale_issues(args.repo, active_titles, token or "", args.dry_run))
        except (HTTPError, URLError, TimeoutError) as exc:
            action = "skipped-stale-check" if args.dry_run else "error"
            message = format_http_error(exc) if isinstance(exc, HTTPError) else str(exc)
            results.append({"title": "close stale source-watch issues", "action": action, "url": message})

    output = json.dumps({"issues": results, "candidates": [candidate.as_dict() for candidate in built]}, indent=2)
    if args.output:
        args.output.write_text(output + "\n", encoding="utf-8")
    print(output)
    return 1 if any(result["action"] == "error" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
