#!/usr/bin/env python3
"""Audit external links in a rendered MkDocs site and maintain one GitHub issue."""

from __future__ import annotations

import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import html
import ipaddress
import json
import os
from pathlib import Path
import sys
import threading
import time
from typing import Any, Callable
from urllib.error import HTTPError
from urllib.parse import urlencode, urldefrag, urlparse
from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup

ISSUE_TITLE = "External link audit: actionable failures"
ISSUE_LABELS = {
    "docs": ("0e8a16", "Documentation work"),
    "automated": ("bfdadc", "Created or updated by automation"),
    "link-check": ("d4c5f9", "External link audit"),
}
USER_AGENT = "ErgoDocs-Link-Audit/1.0 (+https://docs.ergoplatform.com)"
BROWSER_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140 Safari/537.36"
)
ACTIONABLE_ERRORS = {"dns", "ssl", "redirect", "invalid-url"}
THREAD_LOCAL = threading.local()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def request_session(browser_headers: bool = False) -> requests.Session:
    key = "browser_session" if browser_headers else "audit_session"
    value = getattr(THREAD_LOCAL, key, None)
    if value is None:
        value = requests.Session()
        value.headers.update(
            {
                "User-Agent": BROWSER_USER_AGENT if browser_headers else USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8",
                "Accept-Language": "en-GB,en;q=0.9",
            }
        )
        setattr(THREAD_LOCAL, key, value)
    return value


def parsed_host(url: str) -> str:
    try:
        parsed = urlparse(url)
        host = parsed.hostname or ""
        _ = parsed.port
    except ValueError:
        return ""
    if parsed.scheme not in {"http", "https"} or not host:
        return ""
    return host.rstrip(".").lower()


def exclusion_reason(url: str, *, preconnect: bool = False) -> str | None:
    if "{" in url or "}" in url:
        return "placeholder URL"

    host = parsed_host(url)
    if not host:
        return None
    if host == "localhost" or host.endswith(".localhost"):
        return "local example host"

    try:
        address = ipaddress.ip_address(host.strip("[]"))
    except ValueError:
        address = None
    if address and (
        address.is_private
        or address.is_loopback
        or address.is_link_local
        or address.is_reserved
        or address.is_unspecified
        or not address.is_global
    ):
        return "private or local example address"

    parsed = urlparse(url)
    if (
        preconnect
        and host == "fonts.gstatic.com"
        and parsed.path in {"", "/"}
        and not parsed.query
    ):
        return "font preconnect"
    return None


def collect_urls(site: Path) -> tuple[dict[str, list[str]], list[dict[str, Any]], int]:
    if not site.is_dir():
        raise ValueError(f"Site directory not found: {site}")

    found: dict[str, set[str]] = defaultdict(set)
    excluded: dict[tuple[str, str], set[str]] = defaultdict(set)
    pages = sorted(site.rglob("*.html"))
    if not pages:
        raise ValueError(f"No HTML files found under: {site}")

    attrs = (
        ("a", "href"),
        ("img", "src"),
        ("script", "src"),
        ("link", "href"),
        ("iframe", "src"),
    )
    for page in pages:
        soup = BeautifulSoup(
            page.read_text(encoding="utf-8", errors="ignore"), "html.parser"
        )
        source = page.relative_to(site).as_posix()
        for tag_name, attr in attrs:
            for tag in soup.find_all(tag_name):
                raw = tag.get(attr)
                if not raw:
                    continue
                url = html.unescape(str(raw).strip())
                # The published site uses HTTPS, including scheme-relative URLs.
                if url.startswith("//"):
                    url = "https:" + url
                if not url.lower().startswith(("http://", "https://")):
                    continue
                scheme, rest = url.split(":", 1)
                url = scheme.lower() + ":" + rest
                try:
                    url = urldefrag(url)[0]
                except ValueError:
                    url = url.split("#", 1)[0]
                rel = tag.get("rel") or []
                if isinstance(rel, str):
                    rel = rel.split()
                reason = exclusion_reason(
                    url,
                    preconnect=tag_name == "link"
                    and "preconnect" in {str(value).lower() for value in rel},
                )
                if reason:
                    excluded[(url, reason)].add(source)
                else:
                    found[url].add(source)

    excluded_rows = [
        {"url": url, "reason": reason, "pages": sorted(source_pages)}
        for (url, reason), source_pages in sorted(excluded.items())
    ]
    return (
        {url: sorted(source_pages) for url, source_pages in found.items()},
        excluded_rows,
        len(pages),
    )


def connection_error_kind(detail: str) -> str:
    lowered = detail.lower()
    dns_markers = (
        "name resolution",
        "failed to resolve",
        "nodename nor servname",
        "temporary failure in name resolution",
        "no address associated with hostname",
        "getaddrinfo failed",
    )
    return "dns" if any(marker in lowered for marker in dns_markers) else "connection"


def check_url(
    url: str,
    connect_timeout: float,
    read_timeout: float,
    browser_headers: bool = False,
) -> dict[str, Any]:
    if not parsed_host(url):
        return {
            "status": None,
            "final_url": None,
            "error": "invalid-url",
            "detail": "Invalid HTTP(S) URL",
        }

    try:
        with request_session(browser_headers).get(
            url,
            allow_redirects=True,
            stream=True,
            timeout=(connect_timeout, read_timeout),
        ) as response:
            return {
                "status": response.status_code,
                "final_url": response.url,
                "error": None,
            }
    except requests.exceptions.SSLError as exc:
        kind = "ssl"
        detail = str(exc)
    except requests.exceptions.TooManyRedirects as exc:
        kind = "redirect"
        detail = str(exc)
    except requests.exceptions.ConnectTimeout as exc:
        kind = "connect-timeout"
        detail = str(exc)
    except requests.exceptions.ReadTimeout as exc:
        kind = "read-timeout"
        detail = str(exc)
    except requests.exceptions.ConnectionError as exc:
        detail = str(exc)
        kind = connection_error_kind(detail)
    except requests.RequestException as exc:
        kind = "request"
        detail = str(exc)
    except Exception as exc:
        kind = "invalid-url"
        detail = str(exc)
    return {"status": None, "final_url": None, "error": kind, "detail": detail[:500]}


def needs_retry(attempt: dict[str, Any]) -> bool:
    if attempt.get("error") == "invalid-url":
        return False
    status = attempt.get("status")
    return (
        attempt.get("error") is not None
        or status in {404, 408, 410, 425}
        or (isinstance(status, int) and status >= 500)
    )


def classify_attempt(attempt: dict[str, Any]) -> tuple[str, str]:
    status = attempt.get("status")
    error = attempt.get("error")
    if isinstance(status, int) and status < 400:
        return "ok", f"HTTP {status}"
    if status in {404, 410}:
        return "actionable", f"HTTP {status} after retry"
    if error in ACTIONABLE_ERRORS:
        return "actionable", f"Persistent {error} failure"
    if isinstance(status, int):
        return "warning", f"HTTP {status}"
    return "warning", f"Persistent {error or 'request'} failure"


CheckFunction = Callable[[str, float, float, bool], dict[str, Any]]


def run_check_batch(
    urls: list[str],
    *,
    workers: int,
    connect_timeout: float,
    read_timeout: float,
    browser_headers: bool,
    check_fn: CheckFunction,
    progress_every: int,
) -> dict[str, dict[str, Any]]:
    checked: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(
                check_fn, url, connect_timeout, read_timeout, browser_headers
            ): url
            for url in urls
        }
        for index, future in enumerate(as_completed(futures), 1):
            url = futures[future]
            try:
                checked[url] = future.result()
            except Exception as exc:
                checked[url] = {
                    "status": None,
                    "final_url": None,
                    "error": "request",
                    "detail": str(exc)[:500],
                }
            if progress_every and index % progress_every == 0:
                print(f"checked {index}/{len(urls)}", file=sys.stderr, flush=True)
    return checked


def audit_site(
    site: Path,
    *,
    workers: int = 16,
    retry_workers: int = 6,
    connect_timeout: float = 8,
    read_timeout: float = 20,
    retry_connect_timeout: float = 12,
    retry_read_timeout: float = 35,
    retries: int = 2,
    retry_delay: float = 1,
    progress_every: int = 100,
    check_fn: CheckFunction = check_url,
) -> dict[str, Any]:
    sources, excluded, html_pages = collect_urls(site)
    urls = sorted(sources)
    attempts: dict[str, list[dict[str, Any]]] = {url: [] for url in urls}
    pending = urls

    for round_index in range(retries + 1):
        if not pending:
            break
        if round_index and retry_delay:
            time.sleep(retry_delay)
        batch = run_check_batch(
            pending,
            workers=workers if round_index == 0 else retry_workers,
            connect_timeout=(
                connect_timeout if round_index == 0 else retry_connect_timeout
            ),
            read_timeout=read_timeout if round_index == 0 else retry_read_timeout,
            browser_headers=round_index > 0,
            check_fn=check_fn,
            progress_every=progress_every,
        )
        for url, attempt in batch.items():
            attempts[url].append({"attempt": round_index + 1, **attempt})
        pending = [url for url in pending if needs_retry(attempts[url][-1])]

    results: list[dict[str, Any]] = []
    for url in urls:
        final = attempts[url][-1]
        outcome, reason = classify_attempt(final)
        results.append(
            {
                "url": url,
                "pages": sources[url],
                "outcome": outcome,
                "reason": reason,
                "status": final.get("status"),
                "final_url": final.get("final_url"),
                "error": final.get("error"),
                "detail": final.get("detail"),
                "attempts": attempts[url],
            }
        )

    counts = {
        name: sum(item["outcome"] == name for item in results)
        for name in ("ok", "warning", "actionable")
    }
    return {
        "generated": utc_now(),
        "site": str(site),
        "html_pages": html_pages,
        "unique_external_urls": len(
            set(urls) | {str(item["url"]) for item in excluded}
        ),
        "checked_urls": len(urls),
        "excluded_urls": len(excluded),
        "summary": counts,
        "results": results,
        "excluded": excluded,
    }


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def source_cell(pages: list[str], limit: int = 3) -> str:
    shown = [f"`{markdown_cell(page)}`" for page in pages[:limit]]
    if len(pages) > limit:
        shown.append(f"+{len(pages) - limit} more")
    return "<br>".join(shown)


def result_table(items: list[dict[str, Any]], limit: int | None = None) -> list[str]:
    selected = items if limit is None else items[:limit]
    lines = ["| URL | Result | Source pages |", "| --- | --- | --- |"]
    for item in selected:
        lines.append(
            f"| `{markdown_cell(str(item['url']))}` | {markdown_cell(str(item['reason']))} | "
            f"{source_cell(item.get('pages', []))} |"
        )
    if limit is not None and len(items) > limit:
        lines.append(f"| _{len(items) - limit} more_ | See JSON artifact | |")
    return lines


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    actionable = [item for item in report["results"] if item["outcome"] == "actionable"]
    warnings = [item for item in report["results"] if item["outcome"] == "warning"]
    lines = [
        "# External Link Audit",
        "",
        f"Generated: `{report['generated']}`",
        "",
        f"- Rendered HTML pages: {report['html_pages']}",
        f"- Unique external URLs: {report['unique_external_urls']}",
        f"- Checked: {report['checked_urls']}",
        f"- Excluded local/example URLs: {report['excluded_urls']}",
        f"- Passed: {summary['ok']}",
        f"- Warnings: {summary['warning']}",
        f"- Actionable: {summary['actionable']}",
        "",
        "## Actionable Failures",
        "",
    ]
    lines.extend(
        result_table(actionable) if actionable else ["No actionable failures."]
    )
    lines.extend(["", "## Warnings", ""])
    lines.extend(result_table(warnings, limit=100) if warnings else ["No warnings."])
    lines.extend(
        [
            "",
            "Warnings include access controls, rate limits, server errors, ordinary connection failures, and timeouts. They do not create an issue automatically.",
            "",
        ]
    )
    return "\n".join(lines)


def issue_body(report: dict[str, Any], run_url: str) -> str:
    actionable = [item for item in report["results"] if item["outcome"] == "actionable"]
    lines = [
        "Automated external-link audit found failures that remained actionable after validation and applicable retries.",
        "",
        f"Generated: `{report['generated']}`",
        f"Actionable failures: {len(actionable)}",
        f"Warnings: {report['summary']['warning']}",
    ]
    if run_url:
        lines.extend([f"Workflow report: {run_url}"])
    lines.extend(["", *result_table(actionable, limit=25), ""])
    lines.extend(
        [
            "Fix or replace each URL in its listed source page. Warnings remain in the uploaded JSON and Markdown reports for later rechecks.",
            "",
            "This issue is updated in place and closes automatically when no actionable failures remain.",
        ]
    )
    return "\n".join(lines) + "\n"


def github_request(
    method: str, url: str, token: str, payload: dict[str, Any] | None = None
) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "ergodocs-external-link-audit",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = Request(url, data=data, headers=headers, method=method)
    with urlopen(request, timeout=20) as response:
        raw = response.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def ensure_labels(repo: str, token: str) -> None:
    endpoint = f"https://api.github.com/repos/{repo}/labels"
    for name, (color, description) in ISSUE_LABELS.items():
        try:
            github_request(
                "POST",
                endpoint,
                token,
                {"name": name, "color": color, "description": description},
            )
        except HTTPError as exc:
            if exc.code != 422:
                raise


def find_open_issues(repo: str, token: str) -> list[dict[str, Any]]:
    query = urlencode(
        {
            "q": f'repo:{repo} is:issue is:open in:title "{ISSUE_TITLE}"',
            "per_page": 100,
        }
    )
    result = github_request(
        "GET", f"https://api.github.com/search/issues?{query}", token
    )
    issues = result.get("items", [])
    return sorted(
        [
            issue
            for issue in issues
            if issue.get("title") == ISSUE_TITLE and "pull_request" not in issue
        ],
        key=lambda issue: int(issue.get("number", 0)),
    )


def close_issue(issue: dict[str, Any], token: str, comment: str) -> None:
    comments_url = str(issue.get("comments_url", ""))
    if comments_url:
        github_request("POST", comments_url, token, {"body": comment})
    github_request("PATCH", str(issue["url"]), token, {"state": "closed"})


def sync_issue(
    report: dict[str, Any], repo: str, token: str, run_url: str, dry_run: bool = False
) -> dict[str, Any]:
    actionable = int(report.get("summary", {}).get("actionable", 0))
    if dry_run:
        return {
            "title": ISSUE_TITLE,
            "action": "dry-run-update" if actionable else "dry-run-close",
            "url": "",
        }

    existing = find_open_issues(repo, token)
    if not actionable:
        for issue in existing:
            close_issue(
                issue,
                token,
                "Closing automatically because the latest audit found no actionable external-link failures. Warnings, if any, remain in the workflow report.",
            )
        return {
            "title": ISSUE_TITLE,
            "action": "closed" if existing else "clean",
            "url": str(existing[0].get("html_url", "")) if existing else "",
            "closed_duplicates": max(0, len(existing) - 1),
        }

    ensure_labels(repo, token)
    body = issue_body(report, run_url)
    labels = list(ISSUE_LABELS)
    if existing:
        issue = github_request(
            "PATCH", str(existing[0]["url"]), token, {"body": body, "labels": labels}
        )
        action = "updated"
    else:
        issue = github_request(
            "POST",
            f"https://api.github.com/repos/{repo}/issues",
            token,
            {"title": ISSUE_TITLE, "body": body, "labels": labels},
        )
        action = "created"

    for duplicate in existing[1:]:
        close_issue(
            duplicate,
            token,
            f"Closing duplicate; tracking continues in {issue.get('html_url', ISSUE_TITLE)}.",
        )
    return {
        "title": ISSUE_TITLE,
        "action": action,
        "url": str(issue.get("html_url", "")),
        "closed_duplicates": max(0, len(existing) - 1),
    }


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return parsed


def nonnegative_int(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be at least 0")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan = subparsers.add_parser(
        "scan", help="Check external URLs found in rendered HTML."
    )
    scan.add_argument("site", type=Path, help="Rendered MkDocs site directory.")
    scan.add_argument("--json-report", required=True, type=Path)
    scan.add_argument("--markdown-report", required=True, type=Path)
    scan.add_argument("--workers", type=positive_int, default=16)
    scan.add_argument("--retry-workers", type=positive_int, default=6)
    scan.add_argument("--connect-timeout", type=float, default=8)
    scan.add_argument("--read-timeout", type=float, default=20)
    scan.add_argument("--retry-connect-timeout", type=float, default=12)
    scan.add_argument("--retry-read-timeout", type=float, default=35)
    scan.add_argument("--retries", type=nonnegative_int, default=2)
    scan.add_argument("--retry-delay", type=float, default=1)
    scan.add_argument("--progress-every", type=nonnegative_int, default=100)

    issue = subparsers.add_parser(
        "sync-issue", help="Create, update, deduplicate, or close the audit issue."
    )
    issue.add_argument("--report", required=True, type=Path)
    issue.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", ""))
    issue.add_argument("--run-url", default="")
    issue.add_argument("--output", type=Path)
    issue.add_argument("--dry-run", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "scan":
        try:
            report = audit_site(
                args.site,
                workers=args.workers,
                retry_workers=args.retry_workers,
                connect_timeout=args.connect_timeout,
                read_timeout=args.read_timeout,
                retry_connect_timeout=args.retry_connect_timeout,
                retry_read_timeout=args.retry_read_timeout,
                retries=args.retries,
                retry_delay=args.retry_delay,
                progress_every=args.progress_every,
            )
        except (OSError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 2
        args.json_report.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_report.parent.mkdir(parents=True, exist_ok=True)
        args.json_report.write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8"
        )
        args.markdown_report.write_text(render_markdown(report), encoding="utf-8")
        print(
            json.dumps(
                {
                    "summary": report["summary"],
                    "checked_urls": report["checked_urls"],
                    "excluded_urls": report["excluded_urls"],
                }
            )
        )
        return 0

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
    if not args.repo:
        print("Missing --repo or GITHUB_REPOSITORY", file=sys.stderr)
        return 2
    if not token and not args.dry_run:
        print("Missing GITHUB_TOKEN or GH_TOKEN", file=sys.stderr)
        return 2
    if not args.report.is_file():
        print(f"Report not found: {args.report}", file=sys.stderr)
        return 2
    try:
        report = json.loads(args.report.read_text(encoding="utf-8"))
        result = sync_issue(report, args.repo, token, args.run_url, args.dry_run)
    except (HTTPError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Issue sync failed: {exc}", file=sys.stderr)
        return 1
    output = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
