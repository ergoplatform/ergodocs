#!/usr/bin/env python3
"""
Report docs pages linked to source repositories.

Default mode is offline and validates metadata only.
Use --github to query GitHub commits for watched paths.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

try:
    import yaml
except ModuleNotFoundError:
    print("Missing dependency: PyYAML. Install with `pip install -r requirements.txt`.")
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"


def load_dotenv() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = value


@dataclass
class SourceRef:
    repo: str
    paths: list[str]
    branch: str
    since: str | None


@dataclass
class PageWatch:
    path: Path
    owner: str | None
    last_reviewed: str | None
    source_repos: list[SourceRef]
    source_of_truth: list[str]


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def load_watches() -> list[PageWatch]:
    watches: list[PageWatch] = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        meta = parse_frontmatter(path)
        raw_repos = as_list(meta.get("source_repos"))
        if not raw_repos:
            continue

        source_repos: list[SourceRef] = []
        for raw in raw_repos:
            if not isinstance(raw, dict):
                continue
            repo = str(raw.get("repo", "")).strip()
            paths = [str(p).strip() for p in as_list(raw.get("paths")) if str(p).strip()]
            branch = str(raw.get("branch", "master")).strip() or "master"
            since = raw.get("since") or meta.get("last_reviewed")
            if repo and paths:
                source_repos.append(SourceRef(repo=repo, paths=paths, branch=branch, since=str(since) if since else None))

        if source_repos:
            watches.append(
                PageWatch(
                    path=path,
                    owner=str(meta.get("owner")) if meta.get("owner") else None,
                    last_reviewed=str(meta.get("last_reviewed")) if meta.get("last_reviewed") else None,
                    source_repos=source_repos,
                    source_of_truth=[str(v) for v in as_list(meta.get("source_of_truth"))],
                )
            )
    return watches


def validate(watches: list[PageWatch]) -> list[str]:
    errors: list[str] = []
    for watch in watches:
        rel = watch.path.relative_to(ROOT).as_posix()
        if not watch.owner:
            errors.append(f"{rel}: missing owner")
        if not watch.last_reviewed:
            errors.append(f"{rel}: missing last_reviewed")
        else:
            try:
                datetime.fromisoformat(watch.last_reviewed)
            except ValueError:
                errors.append(f"{rel}: last_reviewed must use YYYY-MM-DD")
        if not watch.source_of_truth:
            errors.append(f"{rel}: missing source_of_truth")
    return errors


def github_json(url: str, token: str | None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "ergodocs-source-watch",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    with urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def github_commits(ref: SourceRef, path: str, token: str | None) -> list[dict[str, str]]:
    base = f"https://api.github.com/repos/{quote(ref.repo)}/commits"
    query = f"?sha={quote(ref.branch)}&path={quote(path)}&per_page=5"
    if ref.since:
        query += f"&since={quote(ref.since)}T00:00:00Z"
    data = github_json(base + query, token)
    commits: list[dict[str, str]] = []
    for item in data:
        commit = item.get("commit", {})
        commits.append(
            {
                "sha": str(item.get("sha", ""))[:12],
                "date": str(commit.get("committer", {}).get("date", "")),
                "message": str(commit.get("message", "")).splitlines()[0],
                "url": str(item.get("html_url", "")),
            }
        )
    return commits


def format_http_error(exc: HTTPError) -> str:
    try:
        body = json.loads(exc.read().decode("utf-8"))
    except Exception:
        body = {}
    message = body.get("message") if isinstance(body, dict) else None
    if message:
        return f"HTTP Error {exc.code}: {message}"
    return f"HTTP Error {exc.code}: {exc.reason}"


def apply_since_override(watches: list[PageWatch], since: str | None) -> None:
    if not since:
        return
    datetime.fromisoformat(since)
    for watch in watches:
        for ref in watch.source_repos:
            ref.since = since


def filter_watches(watches: list[PageWatch], repos: list[str], pages: list[str]) -> list[PageWatch]:
    filtered = watches
    if pages:
        page_terms = [page.strip() for page in pages if page.strip()]
        filtered = [
            watch
            for watch in filtered
            if any(page in watch.path.relative_to(ROOT).as_posix() for page in page_terms)
        ]

    if repos:
        repo_terms = {repo.strip() for repo in repos if repo.strip()}
        next_watches: list[PageWatch] = []
        for watch in filtered:
            source_repos = [ref for ref in watch.source_repos if ref.repo in repo_terms]
            if source_repos:
                next_watches.append(
                    PageWatch(
                        path=watch.path,
                        owner=watch.owner,
                        last_reviewed=watch.last_reviewed,
                        source_repos=source_repos,
                        source_of_truth=watch.source_of_truth,
                    )
                )
        filtered = next_watches

    return filtered


def print_report(watches: list[PageWatch], use_github: bool, max_queries: int | None) -> int:
    token = os.environ.get("GITHUB_TOKEN")
    queries_used = 0
    print("# Source Watch Report")
    print()
    print(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    print(f"Pages watched: {len(watches)}")
    print()

    changes_found = False
    for watch in watches:
        rel = watch.path.relative_to(ROOT).as_posix()
        print(f"## {rel}")
        print()
        print(f"- Owner: {watch.owner or 'missing'}")
        print(f"- Last reviewed: {watch.last_reviewed or 'missing'}")
        print("- Source of truth:")
        for source in watch.source_of_truth:
            print(f"  - {source}")
        print("- Watched source:")

        for ref in watch.source_repos:
            print(f"  - {ref.repo}@{ref.branch} since {ref.since or 'unset'}")
            for path in ref.paths:
                print(f"    - `{path}`")
                if not use_github:
                    continue
                if max_queries is not None and queries_used >= max_queries:
                    print("      - GitHub query skipped: max query limit reached")
                    continue
                queries_used += 1
                try:
                    commits = github_commits(ref, path, token)
                except HTTPError as exc:
                    print(f"      - GitHub query failed: {format_http_error(exc)}")
                    continue
                except (URLError, TimeoutError) as exc:
                    print(f"      - GitHub query failed: {exc}")
                    continue
                if commits:
                    changes_found = True
                    for commit in commits:
                        print(f"      - {commit['date']} {commit['sha']} {commit['message']}")
                        print(f"        {commit['url']}")
                else:
                    print("      - No commits found")
        print()

    if use_github and changes_found:
        print("Suggested next step: run AI docs review prompt with changed commits and affected pages.")
    if use_github:
        print(f"GitHub queries used: {queries_used}")
    if use_github and changes_found:
        return 1
    return 0


def main() -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Track docs pages against source repositories.")
    parser.add_argument("--github", action="store_true", help="Query GitHub commits for watched paths.")
    parser.add_argument("--strict", action="store_true", help="Fail when metadata is invalid.")
    parser.add_argument("--since", help="Override source scan start date, YYYY-MM-DD.")
    parser.add_argument("--repo", action="append", default=[], help="Only scan this owner/repo. Repeatable.")
    parser.add_argument("--page", action="append", default=[], help="Only scan pages containing this path fragment. Repeatable.")
    parser.add_argument("--max-queries", type=int, help="Stop GitHub lookups after this many path queries.")
    args = parser.parse_args()

    watches = load_watches()
    apply_since_override(watches, args.since)
    watches = filter_watches(watches, args.repo, args.page)
    errors = validate(watches)
    if errors:
        print("Metadata issues:")
        for error in errors:
            print(f"- {error}")
        if args.strict:
            return 1
        print()

    return print_report(watches, args.github, args.max_queries)


if __name__ == "__main__":
    sys.exit(main())
