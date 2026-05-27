#!/usr/bin/env python3
"""Audit documentation information architecture."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import argparse
import sys

try:
    import yaml
except ModuleNotFoundError:
    print("Missing dependency: PyYAML. Install with `pip install -r requirements.txt`.")
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"

EXCLUDE_PREFIXES = ("archive/", "events/pdf/")
EXCLUDE_FILES = {
    "README.md",
    "archive.md",
    "awesome-ergo.md",
    "categories/index.md",
    "prompt.md",
    "tags.md",
    "todo.md",
}
UNLISTED_STATUSES = {"legacy", "alias", "draft"}


class Loader(yaml.SafeLoader):
    """YAML loader that tolerates MkDocs python-name tags."""


def _python_name(loader: Loader, suffix: str, node: yaml.Node) -> str:
    return f"python_name:{suffix}"


Loader.add_multi_constructor("tag:yaml.org,2002:python/name:", _python_name)


def walk_nav(node, section_path=()):
    if isinstance(node, str):
        yield section_path, None, node
    elif isinstance(node, list):
        for item in node:
            yield from walk_nav(item, section_path)
    elif isinstance(node, dict):
        for title, value in node.items():
            if isinstance(value, str):
                yield section_path, title, value
            else:
                yield from walk_nav(value, (*section_path, title))


def include_doc(path: str) -> bool:
    if path in EXCLUDE_FILES:
        return False
    return not any(path.startswith(prefix) for prefix in EXCLUDE_PREFIXES)


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def top_area(path: str) -> str:
    first = path.split("/", 1)[0]
    if first in {"dev", "node", "mining"}:
        return "develop/deploy"
    if first in {"eco", "uses", "tutorials"}:
        return "use"
    if first in {"contribute", "ef", "events"}:
        return "participate"
    if first in {"doc", "start-here"} or path in {
        "crypto.md",
        "documents.md",
        "learn.md",
        "roadmap.md",
        "sig-scheme.md",
    }:
        return "learn"
    return "start/reference"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit docs IA health.")
    parser.add_argument("--markdown", action="store_true", help="Emit markdown report.")
    parser.add_argument("--strict", action="store_true", help="Fail on IA issues.")
    args = parser.parse_args()

    config = yaml.load(MKDOCS.read_text(encoding="utf-8"), Loader=Loader)
    entries = [entry for item in config.get("nav", []) for entry in walk_nav(item)]
    paths = [path for _, _, path in entries]
    nav_set = set(paths)
    locations = defaultdict(list)
    for section_path, title, path in entries:
        locations[path].append((section_path, title))

    docs = sorted(p.relative_to(DOCS).as_posix() for p in DOCS.rglob("*.md"))
    doc_meta = {p: frontmatter(DOCS / p) for p in docs}
    intentional_unlisted = [
        p for p in docs if include_doc(p) and doc_meta[p].get("ia_status") in UNLISTED_STATUSES
    ]
    active_docs = [
        p
        for p in docs
        if include_doc(p) and doc_meta[p].get("ia_status") not in UNLISTED_STATUSES
    ]
    duplicates = {path: locs for path, locs in locations.items() if len(locs) > 1}
    orphans = [p for p in active_docs if p not in nav_set]
    missing = [entry for entry in entries if not (DOCS / entry[2]).exists()]
    depths = [len(section_path) + 1 for section_path, _, _ in entries]
    area_counts = Counter(top_area(p) for p in active_docs)

    owner_count = 0
    source_count = 0
    source_by_area = Counter()
    for rel in active_docs:
        meta = doc_meta[rel]
        if meta.get("owner"):
            owner_count += 1
        if meta.get("source_repos"):
            source_count += 1
            source_by_area[top_area(rel)] += 1

    cross_surface = []
    for path, locs in duplicates.items():
        surfaces = sorted({loc[0][0] if loc[0] else "(root)" for loc in locs})
        if len(surfaces) > 1:
            cross_surface.append((path, surfaces, locs))

    lines = []
    if args.markdown:
        lines.append("# Information Architecture Audit")
        lines.append("")
        lines.append("## Summary")
        bullet = "- "
    else:
        bullet = ""

    summary = [
        ("active_docs", len(active_docs)),
        ("nav_entries", len(entries)),
        ("unique_nav_targets", len(nav_set)),
        ("missing_nav_targets", len(missing)),
        ("duplicate_nav_targets", len(duplicates)),
        ("cross_surface_duplicates", len(cross_surface)),
        ("orphans", len(orphans)),
        ("intentional_unlisted", len(intentional_unlisted)),
        ("max_nav_depth", max(depths) if depths else 0),
        ("docs_with_owner", owner_count),
        ("docs_with_source_repos", source_count),
    ]
    for key, value in summary:
        lines.append(f"{bullet}{key}: {value}")

    lines.append("")
    lines.append("## Areas" if args.markdown else "Areas")
    for area, count in sorted(area_counts.items()):
        sources = source_by_area[area]
        lines.append(f"{bullet}{area}: {count} pages, {sources} source-watched")

    lines.append("")
    lines.append("## Cross-Surface Duplicates" if args.markdown else "Cross-Surface Duplicates")
    for path, surfaces, locs in sorted(cross_surface)[:40]:
        where = "; ".join(" / ".join(loc[0]) for loc in locs)
        lines.append(f"{bullet}{path}: {', '.join(surfaces)} ({where})")

    lines.append("")
    lines.append("## Orphans" if args.markdown else "Orphans")
    for path in orphans[:80]:
        lines.append(f"{bullet}{path}")

    print("\n".join(lines))
    has_issues = bool(missing or duplicates or orphans)
    return 1 if args.strict and has_issues else 0


if __name__ == "__main__":
    sys.exit(main())
