#!/usr/bin/env python3
"""Open per-page documentation review issues from a Source Watch JSON report."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
from typing import Any
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


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


def page_changes(page: dict[str, Any]) -> list[dict[str, Any]]:
    return [change for change in page.get("changes", []) if isinstance(change, dict)]


def body_for_page(page: dict[str, Any], report: dict[str, Any], artifact_url: str) -> str:
    changes = page_changes(page)
    authors = sorted({safe_login(str(change.get("author_login", ""))) for change in changes})
    authors = [author for author in authors if author]

    lines = [
        "Automated documentation review lead.",
        "",
        "This page may need updates based on recent source changes and/or weekly Discord leads.",
        "Please highlight any errors, missing context, or incorrect assumptions.",
        "",
        "Discord is treated as leads only; docs changes must be verified against source repos, releases, issues, EIPs, or maintainer confirmation.",
        "",
        f"Page: `{page.get('page', '')}`",
        f"Generated: `{report.get('generated', '')}`",
        "",
    ]

    if authors:
        lines.extend(["Possible reviewers from source commits:", ", ".join(authors), ""])

    if artifact_url:
        lines.extend(["Weekly report artifact:", artifact_url, ""])

    lines.extend(["Source changes:", ""])
    for change in changes:
        author = safe_login(str(change.get("author_login", ""))) or str(change.get("author_login", "") or "unknown")
        lines.append(
            f"- `{change.get('repo', '')}/{change.get('path', '')}` "
            f"{change.get('date', '')} `{change.get('sha', '')}` "
            f"[{change.get('severity', 'unknown')}] {change.get('message', '')} "
            f"({author})"
        )
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
            "- Update docs naturally if needed.",
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


def create_or_update_issue(repo: str, title: str, body: str, token: str, dry_run: bool) -> dict[str, str]:
    if dry_run:
        return {"title": title, "action": "dry-run", "url": ""}

    existing = find_issue(repo, title, token)
    if existing:
        issue = github_request("PATCH", existing["url"], token, {"body": body})
        return {"title": title, "action": "updated", "url": issue.get("html_url", "")}

    issue = github_request("POST", f"https://api.github.com/repos/{repo}/issues", token, {"title": title, "body": body})
    return {"title": title, "action": "created", "url": issue.get("html_url", "")}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create per-page docs review issues from Source Watch JSON.")
    parser.add_argument("--report", required=True, type=Path, help="Source Watch JSON report.")
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", ""), help="GitHub repo, owner/name.")
    parser.add_argument("--artifact-url", default="", help="Workflow artifact or run URL to include.")
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
    results: list[dict[str, str]] = []
    for page in report.get("pages", []):
        if not page_changes(page):
            continue
        title = f"Docs review needed: {page.get('page', '')}"
        body = body_for_page(page, report, args.artifact_url)
        try:
            results.append(create_or_update_issue(args.repo, title, body, token or "", args.dry_run))
        except HTTPError as exc:
            results.append({"title": title, "action": "error", "url": format_http_error(exc)})

    print(json.dumps({"issues": results}, indent=2))
    return 1 if any(result["action"] == "error" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
