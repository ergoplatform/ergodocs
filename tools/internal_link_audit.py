#!/usr/bin/env python3
"""Check local links, images, and anchors in rendered MkDocs pages, including cards."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import sys
from urllib.parse import unquote, urlsplit

SITE_HOSTS = frozenset({"docs.ergoplatform.com", "docs.ergoplatform.org"})


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors: set[str] = set()
        self.links: set[str] = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.anchors.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.anchors.add(attrs["name"])
        key = "href" if tag == "a" else "src" if tag == "img" else None
        if key and attrs.get(key):
            self.links.add(attrs[key])


@dataclass(frozen=True, order=True)
class Issue:
    page: str
    link: str
    reason: str


def audit(
    site: Path, site_hosts: frozenset[str] = SITE_HOSTS
) -> tuple[int, list[Issue]]:
    # Match exact filename casing even when running on a case-insensitive filesystem.
    files = {p.relative_to(site).as_posix(): p for p in site.rglob("*") if p.is_file()}
    pages = {}
    for name, path in files.items():
        if path.suffix.lower() == ".html":
            parser = PageParser()
            parser.feed(path.read_text(encoding="utf-8"))
            pages[name] = parser
    issues = []
    for page, parsed in sorted(pages.items()):
        for link in sorted(parsed.links):
            try:
                url = urlsplit(link)
            except ValueError:
                issues.append(Issue(page, link, "invalid URL"))
                continue
            if url.scheme or url.netloc:
                if (
                    url.scheme not in {"", "http", "https"}
                    or url.hostname not in site_hosts
                ):
                    continue
            path = unquote(url.path)
            if url.netloc:
                path = path or "/"
            if not path:
                target = page
            elif path.startswith("/"):
                target = posixpath.normpath(path.lstrip("/"))
            else:
                target = posixpath.normpath(
                    posixpath.join(posixpath.dirname(page), path)
                )
            if target == ".." or target.startswith("../"):
                issues.append(Issue(page, link, "path escapes site"))
                continue
            if target not in files:
                target = posixpath.join(target, "index.html")
                if target.startswith("./"):
                    target = target[2:]
            if target not in files:
                issues.append(Issue(page, link, "missing file (case-sensitive)"))
                continue
            # Text fragments have no corresponding HTML id.
            fragment = unquote(url.fragment).split(":~:text=", 1)[0]
            if fragment and target in pages and fragment not in pages[target].anchors:
                issues.append(Issue(page, link, f"missing anchor #{fragment}"))
    return len(pages), sorted(issues)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--site-dir", type=Path, required=True, help="Output directory of mkdocs build."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return nonzero when a local target is broken.",
    )
    parser.add_argument(
        "--site-host",
        action="append",
        default=[],
        help="Additional hostname whose absolute URLs should resolve against this build.",
    )
    args = parser.parse_args()
    if not args.site_dir.is_dir():
        parser.error("Build the site first; --site-dir must be an existing directory.")
    count, issues = audit(args.site_dir, SITE_HOSTS | frozenset(args.site_host))
    if not count:
        print("No HTML pages found; build the site first.", file=sys.stderr)
        return 2
    print(f"Rendered HTML pages: {count}")
    print(f"Broken internal targets: {len(issues)}")
    for issue in issues:
        print(f"  {issue.page}: {issue.link} ({issue.reason})")
    return 1 if args.strict and issues else 0


if __name__ == "__main__":
    sys.exit(main())
