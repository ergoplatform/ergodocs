#!/usr/bin/env python3
"""Generate a markdown inventory of Source Watch repository coverage."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
import sys

import source_watch


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "contribute" / "source-watch-inventory.md"


@dataclass
class RepoCoverage:
    repo: str
    branches: set[str] = field(default_factory=set)
    pages: set[str] = field(default_factory=set)
    paths: set[str] = field(default_factory=set)


@dataclass
class OwnerCoverage:
    owner: str
    repos: set[str] = field(default_factory=set)
    pages: set[str] = field(default_factory=set)
    paths: set[str] = field(default_factory=set)


CORE_OWNERS = {
    "ergoplatform",
    "rosen-bridge",
    "fleet-sdk",
    "scalahub",
    "ScorexFoundation",
}

ECOSYSTEM_OWNERS = {
    "BetterMoneyLabs",
    "ChainCashLabs",
    "Degens-World",
    "duckpools",
    "ergopad",
    "ergonames",
    "GitCircles",
    "Lithos-Protocol",
    "SavonarolaLabs",
    "Spectrum-Finance",
    "spectrum-finance",
}


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def repo_link(repo: str) -> str:
    return f"[`{repo}`](https://github.com/{repo})"


def page_link(page: str) -> str:
    label = page.removeprefix("docs/")
    return f"[`{escape_cell(label)}`]({Path(label).name})"


def owner_type(owner: str) -> str:
    if owner in CORE_OWNERS:
        return "Core / infrastructure"
    if owner in ECOSYSTEM_OWNERS:
        return "Ecosystem org"
    if owner.lower() in {"bitcoin", "defillama", "satoshilabs", "emurgo", "input-output-hk", "keystonehq"}:
        return "External standard/vendor"
    return "Developer / project"


def format_list(values: list[str], limit: int = 8) -> str:
    if not values:
        return ""
    shown = values[:limit]
    text = "<br>".join(f"`{escape_cell(value)}`" for value in shown)
    remaining = len(values) - len(shown)
    if remaining > 0:
        text += f"<br>+{remaining} more"
    return text


def build_inventory() -> str:
    watches = source_watch.load_watches()
    by_repo: dict[str, RepoCoverage] = {}
    by_repo_branch: dict[tuple[str, str], RepoCoverage] = {}
    by_owner: dict[str, OwnerCoverage] = {}
    by_type: dict[str, OwnerCoverage] = {}

    for watch in watches:
        page = watch.path.relative_to(ROOT).as_posix()
        for ref in watch.source_repos:
            owner = ref.repo.split("/", 1)[0]
            owner_entry = by_owner.setdefault(owner, OwnerCoverage(owner=owner))
            owner_entry.repos.add(ref.repo)
            owner_entry.pages.add(page)
            owner_entry.paths.update(ref.paths)

            type_name = owner_type(owner)
            type_entry = by_type.setdefault(type_name, OwnerCoverage(owner=type_name))
            type_entry.repos.add(ref.repo)
            type_entry.pages.add(page)
            type_entry.paths.update(ref.paths)

            repo_entry = by_repo.setdefault(ref.repo, RepoCoverage(repo=ref.repo))
            repo_entry.branches.add(ref.branch)
            repo_entry.pages.add(page)
            repo_entry.paths.update(ref.paths)

            key = (ref.repo, ref.branch)
            branch_entry = by_repo_branch.setdefault(key, RepoCoverage(repo=ref.repo))
            branch_entry.branches.add(ref.branch)
            branch_entry.pages.add(page)
            branch_entry.paths.update(ref.paths)

    area_counts: dict[str, int] = defaultdict(int)
    for watch in watches:
        rel = watch.path.relative_to(ROOT).as_posix()
        parts = rel.split("/")
        area = parts[1] if parts[0] == "docs" and len(parts) > 2 else parts[0].removeprefix("docs/")
        area_counts[area or "root"] += 1

    lines = [
        "---",
        "title: Source Watch Inventory",
        "description: Generated inventory of upstream repositories watched by ErgoDocs pages.",
        "tags:",
        "  - documentation",
        "  - automation",
        "  - source-watch",
        "owner: docs",
        "last_reviewed: never",
        "---",
        "",
        "# Source Watch Inventory",
        "",
        "This page is generated from `source_repos` frontmatter across the docs. Do not edit the tables by hand; run `tools/source_watch_inventory.py --write` after changing Source Watch metadata.",
        "",
        "Source Watch checks watched repositories for commits touching declared paths and GitHub releases. Open pull request checks are opt-in for explicit latest-work or roadmap reviews.",
        "",
        "## Summary",
        "",
        f"- Source-watched pages: `{len(watches)}`",
        f"- Watched repositories: `{len(by_repo)}`",
        f"- Watched GitHub owners: `{len(by_owner)}`",
        f"- Watched repo/branch pairs: `{len(by_repo_branch)}`",
        f"- Watched paths: `{sum(len(entry.paths) for entry in by_repo_branch.values())}`",
        "",
        "## Coverage Groups",
        "",
        "| Group | Owners | Repositories | Pages | Paths |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]

    for type_name in ["Core / infrastructure", "Ecosystem org", "Developer / project", "External standard/vendor"]:
        entry = by_type.get(type_name, OwnerCoverage(owner=type_name))
        owners = {repo.split("/", 1)[0] for repo in entry.repos}
        lines.append(f"| {escape_cell(type_name)} | {len(owners)} | {len(entry.repos)} | {len(entry.pages)} | {len(entry.paths)} |")

    lines.extend(
        [
            "",
        "## Coverage By Area",
        "",
        "| Area | Source-watched pages |",
        "| --- | ---: |",
        ]
    )

    for area, count in sorted(area_counts.items()):
        lines.append(f"| `{escape_cell(area)}` | {count} |")

    lines.extend(
        [
            "",
            "## Coverage By GitHub Owner",
            "",
            "| Owner | Group | Repositories | Pages | Paths |",
            "| --- | --- | ---: | ---: | ---: |",
        ]
    )

    for owner in sorted(by_owner, key=lambda item: (-len(by_owner[item].pages), item.lower())):
        entry = by_owner[owner]
        lines.append(f"| [`{escape_cell(owner)}`](https://github.com/{owner}) | {escape_cell(owner_type(owner))} | {len(entry.repos)} | {len(entry.pages)} | {len(entry.paths)} |")

    lines.extend(
        [
            "",
            "## Watched Repositories",
            "",
            "| Repository | Owner group | Branches | Pages | Paths |",
            "| --- | --- | --- | ---: | ---: |",
        ]
    )

    for repo in sorted(by_repo, key=lambda item: (-len(by_repo[item].pages), item.lower())):
        entry = by_repo[repo]
        owner = repo.split("/", 1)[0]
        branches = ", ".join(f"`{escape_cell(branch)}`" for branch in sorted(entry.branches))
        lines.append(f"| {repo_link(repo)} | {escape_cell(owner_type(owner))} | {branches} | {len(entry.pages)} | {len(entry.paths)} |")

    lines.extend(
        [
            "",
            "## Pages With Broad Coverage",
            "",
            "| Page | Repositories | Paths |",
            "| --- | ---: | ---: |",
        ]
    )

    page_repos: dict[str, set[str]] = defaultdict(set)
    page_paths: dict[str, set[str]] = defaultdict(set)
    for watch in watches:
        page = watch.path.relative_to(ROOT).as_posix()
        for ref in watch.source_repos:
            page_repos[page].add(ref.repo)
            page_paths[page].update(f"{ref.repo}/{path}" for path in ref.paths)

    broad_pages = sorted(page_repos, key=lambda item: (-len(page_repos[item]), item))
    for page in broad_pages[:25]:
        lines.append(f"| {page_link(page)} | {len(page_repos[page])} | {len(page_paths[page])} |")

    lines.extend(
        [
            "",
            "## Repo And Path Coverage",
            "",
            "| Repository | Branch | Watched paths | Pages |",
            "| --- | --- | --- | --- |",
        ]
    )

    for repo, branch in sorted(by_repo_branch, key=lambda item: (item[0].lower(), item[1].lower())):
        entry = by_repo_branch[(repo, branch)]
        paths = format_list(sorted(entry.paths))
        pages = format_list(sorted(entry.pages), limit=6)
        lines.append(f"| {repo_link(repo)} | `{escape_cell(branch)}` | {paths} | {pages} |")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Source Watch repository inventory markdown.")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--write", action="store_true", help="Write the generated inventory.")
    parser.add_argument("--check", action="store_true", help="Fail if the generated inventory is stale.")
    args = parser.parse_args()

    text = build_inventory()
    output = args.output if args.output.is_absolute() else ROOT / args.output

    if args.check:
        if not output.exists():
            print(f"Missing generated inventory: {output}", file=sys.stderr)
            return 1
        existing = output.read_text(encoding="utf-8")
        if existing != text:
            print(f"Generated inventory is stale: {output}", file=sys.stderr)
            print("Run: .venv/bin/python tools/source_watch_inventory.py --write", file=sys.stderr)
            return 1
        return 0

    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        print(f"Wrote {output.relative_to(ROOT)}")
        return 0

    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
