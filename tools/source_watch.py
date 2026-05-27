#!/usr/bin/env python3
"""
Track docs pages against source repositories.

Default command is `scan`. Use `--github` to query GitHub commits.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
import fnmatch
import json
import os
from pathlib import Path
import re
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

try:
    import yaml
except ModuleNotFoundError:
    print("Missing dependency: PyYAML. Install with `pip install -r requirements.txt`.")
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
DEFAULT_BASELINE = ROOT / "tools" / "state" / "source-watch-baseline.json"
GITHUB_URL_RE = re.compile(
    r"https://github\.com/([^/\s\)\]\"'<>]+)/([^/\s\)\]\"'<>]+)/(blob|tree)/([^/\s\)\]\"'<>]+)/([^\s\)\]\"'<>]+)"
)


@dataclass
class SourceRef:
    repo: str
    paths: list[str]
    branch: str
    since: str | None


@dataclass
class SourceIgnore:
    commits: list[str] = field(default_factory=list)
    messages: list[str] = field(default_factory=list)
    paths: list[str] = field(default_factory=list)


@dataclass
class PageWatch:
    path: Path
    owner: str | None
    last_reviewed: str | None
    source_repos: list[SourceRef]
    source_of_truth: list[str]
    source_ignore: SourceIgnore


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


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def split_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}, text
    return yaml.safe_load(parts[1]) or {}, parts[2]


def write_frontmatter(path: Path, meta: dict[str, Any], body: str) -> None:
    path.write_text("---\n" + yaml.safe_dump(meta, sort_keys=False).strip() + "\n---\n" + body, encoding="utf-8")


def normalize_since(value: Any) -> str | None:
    if value is None:
        return None
    if str(value).strip().lower() == "never":
        return None
    return str(value)


def load_ignore(meta: dict[str, Any]) -> SourceIgnore:
    raw = meta.get("source_ignore") or {}
    if not isinstance(raw, dict):
        raw = {}
    return SourceIgnore(
        commits=[str(v) for v in as_list(raw.get("commits"))],
        messages=[str(v) for v in as_list(raw.get("messages"))],
        paths=[str(v) for v in as_list(raw.get("paths"))],
    )


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
            since = normalize_since(raw.get("since") or meta.get("last_reviewed"))
            if repo and paths:
                source_repos.append(SourceRef(repo=repo, paths=paths, branch=branch, since=since))

        if source_repos:
            watches.append(
                PageWatch(
                    path=path,
                    owner=str(meta.get("owner")) if meta.get("owner") else None,
                    last_reviewed=str(meta.get("last_reviewed")) if meta.get("last_reviewed") else None,
                    source_repos=source_repos,
                    source_of_truth=[str(v) for v in as_list(meta.get("source_of_truth"))],
                    source_ignore=load_ignore(meta),
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
        elif watch.last_reviewed.lower() != "never":
            try:
                datetime.fromisoformat(watch.last_reviewed)
            except ValueError:
                errors.append(f"{rel}: last_reviewed must use YYYY-MM-DD or never")
        if not watch.source_of_truth:
            errors.append(f"{rel}: missing source_of_truth")
    return errors


def github_request(method: str, url: str, token: str | None, payload: dict[str, Any] | None = None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "ergodocs-source-watch",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = Request(url, data=data, headers=headers, method=method)
    with urlopen(request, timeout=20) as response:
        raw = response.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def github_json(url: str, token: str | None) -> Any:
    return github_request("GET", url, token)


def format_http_error(exc: HTTPError) -> str:
    try:
        body = json.loads(exc.read().decode("utf-8"))
    except Exception:
        body = {}
    message = body.get("message") if isinstance(body, dict) else None
    if message:
        return f"HTTP Error {exc.code}: {message}"
    return f"HTTP Error {exc.code}: {exc.reason}"


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


def github_path_exists(ref: SourceRef, path: str, token: str | None) -> tuple[bool, str | None]:
    url = f"https://api.github.com/repos/{quote(ref.repo)}/contents/{quote(path)}?ref={quote(ref.branch)}"
    try:
        github_json(url, token)
        return True, None
    except HTTPError as exc:
        return False, format_http_error(exc)
    except (URLError, TimeoutError) as exc:
        return False, str(exc)


def classify_change(path: str, message: str) -> str:
    msg = message.lower()
    low_terms = ("format", "prettier", "typo", "anchor", "metadata", "readme", "docs", "process:")
    if any(term in msg for term in low_terms):
        return "low"
    high_patterns = (
        "api",
        "openapi",
        "conf",
        "config",
        "contract",
        "contracts",
        "eip-",
        "src/main",
        "src/it",
        "ergo-core",
        "wallet",
        "mining",
    )
    if any(pattern in path.lower() for pattern in high_patterns):
        return "high"
    medium_patterns = ("example", "tutorial", "docs/", "README", "test", "scripts")
    if any(pattern.lower() in path.lower() for pattern in medium_patterns):
        return "medium"
    return "medium"


def ignored(watch: PageWatch, path: str, commit: dict[str, str], cli_messages: list[str]) -> bool:
    sha = commit.get("sha", "")
    message = commit.get("message", "")
    for ignored_sha in watch.source_ignore.commits:
        if sha.startswith(ignored_sha):
            return True
    for pattern in watch.source_ignore.paths:
        if fnmatch.fnmatch(path, pattern):
            return True
    for fragment in [*watch.source_ignore.messages, *cli_messages]:
        if fragment and fragment.lower() in message.lower():
            return True
    return False


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
        filtered = [watch for watch in filtered if any(page in watch.path.relative_to(ROOT).as_posix() for page in page_terms)]
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
                        source_ignore=watch.source_ignore,
                    )
                )
        filtered = next_watches
    return filtered


def load_baseline(path: Path) -> set[str]:
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    return {str(item) for item in data.get("seen", [])}


def write_baseline(path: Path, seen: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"seen": sorted(seen)}, indent=2) + "\n", encoding="utf-8")


def change_key(page: str, repo: str, path: str, commit: dict[str, str]) -> str:
    return f"{page}|{repo}|{path}|{commit['sha']}"


def run_scan(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    token = os.environ.get("GITHUB_TOKEN")
    watches = load_watches()
    apply_since_override(watches, args.since)
    watches = filter_watches(watches, args.repo, args.page)
    errors = validate(watches)

    baseline_path = Path(args.baseline)
    baseline = load_baseline(baseline_path) if args.new_only or args.update_baseline else set()
    current_seen = set(baseline)
    queries_used = 0
    report: dict[str, Any] = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "pages_watched": len(watches),
        "queries_used": 0,
        "metadata_errors": errors,
        "pages": [],
        "path_errors": [],
    }

    for watch in watches:
        page_rel = watch.path.relative_to(ROOT).as_posix()
        page_entry: dict[str, Any] = {
            "page": page_rel,
            "owner": watch.owner,
            "last_reviewed": watch.last_reviewed,
            "source_of_truth": watch.source_of_truth,
            "sources": [],
            "changes": [],
            "ignored_changes": [],
        }
        for ref in watch.source_repos:
            source_entry = {"repo": ref.repo, "branch": ref.branch, "since": ref.since, "paths": []}
            for source_path in ref.paths:
                path_entry: dict[str, Any] = {"path": source_path}
                if args.validate_paths:
                    exists, error = github_path_exists(ref, source_path, token)
                    path_entry["exists"] = exists
                    if error:
                        path_entry["error"] = error
                        report["path_errors"].append({"page": page_rel, "repo": ref.repo, "path": source_path, "error": error})
                if args.github:
                    if args.max_queries is not None and queries_used >= args.max_queries:
                        path_entry["skipped"] = "max query limit reached"
                    else:
                        queries_used += 1
                        try:
                            commits = github_commits(ref, source_path, token)
                        except HTTPError as exc:
                            path_entry["error"] = format_http_error(exc)
                        except (URLError, TimeoutError) as exc:
                            path_entry["error"] = str(exc)
                        else:
                            path_entry["commits"] = []
                            for commit in commits:
                                key = change_key(page_rel, ref.repo, source_path, commit)
                                current_seen.add(key)
                                if args.new_only and key in baseline:
                                    continue
                                change = {
                                    **commit,
                                    "page": page_rel,
                                    "repo": ref.repo,
                                    "path": source_path,
                                    "severity": classify_change(source_path, commit["message"]),
                                }
                                if ignored(watch, source_path, commit, args.ignore_message):
                                    page_entry["ignored_changes"].append(change)
                                else:
                                    page_entry["changes"].append(change)
                                    path_entry["commits"].append(change)
                source_entry["paths"].append(path_entry)
            page_entry["sources"].append(source_entry)
        report["pages"].append(page_entry)

    report["queries_used"] = queries_used
    if args.update_baseline:
        write_baseline(baseline_path, current_seen)
        report["baseline_updated"] = baseline_path.as_posix()
    return report, 1 if any(page["changes"] for page in report["pages"]) else 0


def print_markdown(report: dict[str, Any]) -> None:
    print("# Source Watch Report")
    print()
    print(f"Generated: {report['generated']}")
    print(f"Pages watched: {report['pages_watched']}")
    print()
    if report["metadata_errors"]:
        print("## Metadata issues")
        for error in report["metadata_errors"]:
            print(f"- {error}")
        print()
    for page in report["pages"]:
        print(f"## {page['page']}")
        print()
        print(f"- Owner: {page['owner'] or 'missing'}")
        print(f"- Last reviewed: {page['last_reviewed'] or 'missing'}")
        print("- Source of truth:")
        for source in page["source_of_truth"]:
            print(f"  - {source}")
        print("- Watched source:")
        for source in page["sources"]:
            print(f"  - {source['repo']}@{source['branch']} since {source['since'] or 'unset'}")
            for path in source["paths"]:
                print(f"    - `{path['path']}`")
                if "exists" in path:
                    print(f"      - Exists: {path['exists']}")
                if "error" in path:
                    print(f"      - GitHub query failed: {path['error']}")
                if path.get("skipped"):
                    print(f"      - GitHub query skipped: {path['skipped']}")
                for commit in path.get("commits", []):
                    print(f"      - {commit['date']} {commit['sha']} [{commit['severity']}] {commit['message']}")
                    print(f"        {commit['url']}")
        if page["ignored_changes"]:
            print("- Ignored changes:")
            for change in page["ignored_changes"]:
                print(f"  - {change['sha']} {change['message']}")
        print()
    if report.get("queries_used"):
        print(f"GitHub queries used: {report['queries_used']}")
    if any(page["changes"] for page in report["pages"]):
        print("Suggested next step: review changed source paths and update affected docs.")


def write_output(report: dict[str, Any], args: argparse.Namespace) -> None:
    text = json.dumps(report, indent=2) + "\n" if args.format == "json" else markdown_text(report)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


def markdown_text(report: dict[str, Any]) -> str:
    from io import StringIO
    import contextlib

    buf = StringIO()
    with contextlib.redirect_stdout(buf):
        print_markdown(report)
    return buf.getvalue()


def pr_comment(report: dict[str, Any]) -> str:
    changes = [change for page in report["pages"] for change in page["changes"]]
    if not changes:
        return "Source Watch: no watched source changes found."
    lines = ["## Source Watch", "", f"Found {len(changes)} watched source changes.", ""]
    for change in sorted(changes, key=lambda item: (item["severity"], item["page"])):
        lines.append(f"- `{change['page']}` watches `{change['repo']}/{change['path']}`: **{change['severity']}** {change['message']}")
    return "\n".join(lines) + "\n"


def create_or_update_issues(report: dict[str, Any], issue_repo: str, token: str | None, dry_run: bool) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for page in report["pages"]:
        if not page["changes"]:
            continue
        title = f"Docs source changed: {page['page']}"
        body = pr_comment({"pages": [page]})
        body += "\n\nSource Watch generated this issue from watched repository changes.\n"
        if dry_run:
            results.append({"title": title, "action": "dry-run"})
            continue
        query = urlencode({"state": "open", "per_page": 100})
        issues = github_json(f"https://api.github.com/repos/{quote(issue_repo)}/issues?{query}", token)
        existing = next((issue for issue in issues if issue.get("title") == title), None)
        if existing:
            github_request("PATCH", existing["url"], token, {"body": body})
            results.append({"title": title, "action": "updated", "url": existing.get("html_url")})
        else:
            issue = github_request(
                "POST",
                f"https://api.github.com/repos/{quote(issue_repo)}/issues",
                token,
                {"title": title, "body": body},
            )
            results.append({"title": title, "action": "created", "url": issue.get("html_url")})
    return results


def suggest_frontmatter(page: Path) -> int:
    path = page if page.is_absolute() else ROOT / page
    text = path.read_text(encoding="utf-8")
    grouped: dict[tuple[str, str, str], set[str]] = {}
    for match in GITHUB_URL_RE.finditer(text):
        owner, repo, _kind, branch, source_path = match.groups()
        source_path = source_path.split("#", 1)[0].rstrip("`.,;:")
        grouped.setdefault((owner, repo, branch), set()).add(source_path)
    print("owner: docs")
    print("last_reviewed: never")
    print("source_repos:")
    for (owner, repo, branch), paths in sorted(grouped.items()):
        print(f"  - repo: {owner}/{repo}")
        print(f"    branch: {branch}")
        print("    paths:")
        for source_path in sorted(paths):
            print(f"      - {source_path}")
    print("source_of_truth:")
    for (owner, repo, branch), paths in sorted(grouped.items()):
        for source_path in sorted(paths):
            print(f"  - https://github.com/{owner}/{repo}/tree/{branch}/{source_path}")
    return 0


def mark_reviewed(page: Path, reviewed_date: str | None) -> int:
    path = page if page.is_absolute() else ROOT / page
    if not path.exists():
        print(f"Missing page: {path}", file=sys.stderr)
        return 1
    meta, body = split_frontmatter(path)
    if not meta:
        print(f"Page has no frontmatter: {path}", file=sys.stderr)
        return 1
    meta["last_reviewed"] = reviewed_date or date.today().isoformat()
    write_frontmatter(path, meta, body)
    try:
        label = path.relative_to(ROOT).as_posix()
    except ValueError:
        label = path.as_posix()
    print(f"Marked reviewed: {label} -> {meta['last_reviewed']}")
    return 0


def add_scan_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--github", action="store_true", help="Query GitHub commits for watched paths.")
    parser.add_argument("--strict", action="store_true", help="Fail when metadata is invalid.")
    parser.add_argument("--since", help="Override source scan start date, YYYY-MM-DD.")
    parser.add_argument("--repo", action="append", default=[], help="Only scan this owner/repo. Repeatable.")
    parser.add_argument("--page", action="append", default=[], help="Only scan pages containing this path fragment. Repeatable.")
    parser.add_argument("--max-queries", type=int, help="Stop GitHub lookups after this many path queries.")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Report format.")
    parser.add_argument("--output", help="Write report to file.")
    parser.add_argument("--ignore-message", action="append", default=[], help="Ignore commits whose message contains this text.")
    parser.add_argument("--validate-paths", action="store_true", help="Verify watched source paths exist on GitHub.")
    parser.add_argument("--baseline", default=DEFAULT_BASELINE.as_posix(), help="Baseline JSON path.")
    parser.add_argument("--new-only", action="store_true", help="Only report commits missing from baseline.")
    parser.add_argument("--update-baseline", action="store_true", help="Write seen commits to baseline.")
    parser.add_argument("--pr-comment-file", help="Write GitHub PR comment markdown to file.")
    parser.add_argument("--create-issues", action="store_true", help="Create or update GitHub issues for changed pages.")
    parser.add_argument("--issue-repo", default=os.environ.get("GITHUB_REPOSITORY", ""), help="owner/repo for issue creation.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write issues; print intended actions in report.")
    parser.add_argument("--no-fail-on-changes", action="store_true", help="Return success when changed source is found.")


def scan_command(args: argparse.Namespace) -> int:
    report, code = run_scan(args)
    if args.strict and report["metadata_errors"]:
        code = 1
    if args.no_fail_on_changes and code == 1 and not report["metadata_errors"]:
        code = 0
    if args.pr_comment_file:
        Path(args.pr_comment_file).write_text(pr_comment(report), encoding="utf-8")
    if args.create_issues:
        if not args.issue_repo:
            report["issue_results"] = [{"error": "--issue-repo or GITHUB_REPOSITORY required"}]
            code = 1
        else:
            try:
                report["issue_results"] = create_or_update_issues(report, args.issue_repo, os.environ.get("GITHUB_TOKEN"), args.dry_run)
            except HTTPError as exc:
                report["issue_results"] = [{"error": format_http_error(exc)}]
                code = 1
    write_output(report, args)
    return code


def main() -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Track docs pages against source repositories.")
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="Scan watched source repositories.")
    add_scan_args(scan_parser)
    suggest_parser = subparsers.add_parser("suggest", help="Suggest source_repos metadata from GitHub links.")
    suggest_parser.add_argument("page", type=Path)
    reviewed_parser = subparsers.add_parser("mark-reviewed", help="Set last_reviewed on a page.")
    reviewed_parser.add_argument("page", type=Path)
    reviewed_parser.add_argument("--date", help="Review date, YYYY-MM-DD. Defaults to today.")

    add_scan_args(parser)
    args = parser.parse_args()

    if args.command == "suggest":
        return suggest_frontmatter(args.page)
    if args.command == "mark-reviewed":
        return mark_reviewed(args.page, args.date)
    return scan_command(args)


if __name__ == "__main__":
    sys.exit(main())
