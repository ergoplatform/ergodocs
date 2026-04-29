#!/usr/bin/env python3
"""
Audit mkdocs navigation quality.

Checks:
- nav targets that don't exist under docs/
- duplicate nav targets (same page appears multiple times)
- orphan markdown pages that aren't reachable from nav
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
import sys
from typing import Dict, Iterable, List, Sequence, Tuple

try:
    import yaml
except ModuleNotFoundError:
    print("Missing dependency: PyYAML. Install with `pip install -r requirements.txt`.")
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
MKDOCS_YML = ROOT / "mkdocs.yml"
DOCS_DIR = ROOT / "docs"

# Intentionally excluded from nav.
ORPHAN_EXCLUDE_PREFIXES = (
    "archive/",
    "events/pdf/",
)
ORPHAN_EXCLUDE_FILES = {
    "archive.md",
    "awesome-ergo.md",
    "categories/index.md",
    "prompt.md",
    "README.md",
    "todo.md",
    "tags.md",
}


class Loader(yaml.SafeLoader):
    """Safe YAML loader with support for !!python/name tags used by mkdocs."""


def _python_name_tag(loader: Loader, suffix: str, node: yaml.Node) -> str:
    return f"python_name:{suffix}"


Loader.add_multi_constructor("tag:yaml.org,2002:python/name:", _python_name_tag)


NavEntry = Tuple[Tuple[str, ...], str | None, str]


def walk_nav(node, section_path: Sequence[str] | None = None) -> Iterable[NavEntry]:
    if section_path is None:
        section_path = []

    if isinstance(node, str):
        yield (tuple(section_path), None, node)
        return

    if isinstance(node, list):
        for item in node:
            yield from walk_nav(item, section_path)
        return

    if isinstance(node, dict):
        for key, value in node.items():
            if isinstance(value, str):
                yield (tuple(section_path), key, value)
            else:
                yield from walk_nav(value, [*section_path, key])
        return


def should_exclude_orphan(path: str) -> bool:
    if path in ORPHAN_EXCLUDE_FILES:
        return True
    return any(path.startswith(prefix) for prefix in ORPHAN_EXCLUDE_PREFIXES)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit mkdocs nav and docs coverage.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero exit code when issues are found.",
    )
    args = parser.parse_args()

    config = yaml.load(MKDOCS_YML.read_text(encoding="utf-8"), Loader=Loader)
    nav = config.get("nav", [])

    entries: List[NavEntry] = []
    for item in nav:
        entries.extend(walk_nav(item))

    paths = [path for _, _, path in entries]
    path_counts = Counter(paths)

    missing: List[NavEntry] = []
    for entry in entries:
        _, _, rel = entry
        if not (DOCS_DIR / rel).exists():
            missing.append(entry)

    locations: Dict[str, List[Tuple[Tuple[str, ...], str | None]]] = defaultdict(list)
    for section_path, title, rel in entries:
        locations[rel].append((section_path, title))

    duplicates = {rel: locs for rel, locs in locations.items() if len(locs) > 1}

    all_docs = sorted(p.relative_to(DOCS_DIR).as_posix() for p in DOCS_DIR.rglob("*.md"))
    nav_set = set(paths)
    orphans = [p for p in all_docs if p not in nav_set and not should_exclude_orphan(p)]

    print(f"Nav entries: {len(entries)}")
    print(f"Unique nav targets: {len(nav_set)}")
    print(f"Missing nav targets: {len(missing)}")
    if missing:
        for section_path, title, rel in missing:
            section = " / ".join(section_path) if section_path else "(root)"
            print(f"  MISSING {rel}  [{section}] title={title!r}")

    print(f"Duplicate nav targets: {len(duplicates)}")
    if duplicates:
        for rel, locs in sorted(duplicates.items()):
            print(f"  DUP {rel} ({len(locs)}x)")
            for section_path, title in locs:
                section = " / ".join(section_path) if section_path else "(root)"
                print(f"    - [{section}] title={title!r}")

    print(f"Orphan docs (excluding archive/pdf/system pages): {len(orphans)}")
    if orphans:
        for rel in orphans:
            print(f"  ORPHAN {rel}")

    has_issues = bool(missing or duplicates or orphans)
    return 1 if args.strict and has_issues else 0


if __name__ == "__main__":
    sys.exit(main())
