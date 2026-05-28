---
title: Maintainer Start Here
description: Internal guide to the documentation repository, maintenance tools, source-watch workflow, and repo hygiene.
tags:
  - documentation
  - maintainer
  - workflow
owner: docs
last_reviewed: 2026-05-27
---

# Maintainer Start Here

This page is the quick map for people or agents maintaining ErgoDocs.

## Main Docs Workflows

- [Source Watch](source-watch.md): connect pages to upstream repositories, scan for source changes, and mark pages reviewed only after checking the source.
- [Source Watch Playbook](source-watch-playbook.md): repeatable command list for future source-backed review sessions.
- [Documentation Automation](automation.md): public overview of checks, source-linked review, weekly leads, and deploy behavior.
- [Documentation Tools](tools.md): maintainer guide to scripts, prompts, hooks, and local tool state.
- [Information Architecture](information-architecture.md): how sections should be structured and how pages should link together.
- [Documentation Lifecycle](docs-lifecycle.md): page ownership, review expectations, and freshness rules.
- [Content Standards](content-standards.md): writing style, structure, and review standards.
- [Contribute to the Docs](docs.md): general contribution path for docs changes.

## Core Files

- `AGENTS.md`: repo-level instructions for Codex and other coding agents.
- `mkdocs.yml`: site configuration, navigation, theme setup, plugins, and hooks.
- `requirements.txt`: Python dependencies for local builds and docs tooling.
- `run.sh`: activates the repo virtualenv and starts `mkdocs serve`.
- `refs.bib`: bibliography/reference data.

## Tools

- `tools/source_watch.py`: validates `source_repos` metadata and scans watched GitHub paths for commits.
- `tools/discord_dev_digest/discord_dev_digest.py`: exports Discord development chat and prepares source-verification leads for docs updates.
- `tools/nav_audit.py`: checks navigation coverage and obvious nav problems.
- `tools/structure_audit.py`: checks section structure, orphan pages, and duplicate labels.
- `tools/hooks.py`: MkDocs hook code used during rendering.
- `tools/ai_docs_review_prompt.md`: prompt template for source-backed docs review.
- `tools/markdown_prompt.md`: compact Markdown formatting prompt for docs authors or AI-assisted cleanup.
- `tools/zip_files.py`: manual helper that creates `md_files.zip` from Markdown files.
- `tools/links.sh`: extracts HTTP links into `links.txt` and GitHub links into `GitHub.txt`; generated output should not be committed unless deliberately needed.
- `tools/deploy.sh`: manual legacy deploy helper; prefer GitHub Actions deploy workflow for normal publishing.

Use the repo virtualenv for Python tools:

```bash
source .venv/bin/activate
```

or call tools directly:

```bash
.venv/bin/python tools/source_watch.py scan --strict
```

## Tool Workflows

Use `tools/nav_audit.py --strict` after nav edits. It fails on missing nav targets, duplicate nav entries, and unlisted active docs.

Use `tools/structure_audit.py --strict` after large section moves. It reports active docs, nav coverage, duplicate targets, source-watched page counts, area counts, and orphan pages.

Use `tools/source_watch.py scan --strict` after adding or changing `source_repos`. It validates required metadata without calling GitHub.

Use GitHub-backed Source Watch scans when checking whether upstream repos changed:

```bash
.venv/bin/python tools/source_watch.py scan --github --new-only --repo ergoplatform/ergo --max-queries 120 --no-fail-on-changes --format markdown --output /tmp/source-watch-ergo.md
```

Use `tools/source_watch.py suggest docs/path/page.md` to draft frontmatter from GitHub links already in a page.

Use `tools/source_watch.py mark-reviewed docs/path/page.md` only after checking the page against upstream source.

## GitHub Workflows

- `.github/workflows/docs-quality.yml`: PR workflow for docs/tooling changes. It installs dependencies, builds MkDocs, runs nav audit, and validates Source Watch metadata.
- `.github/workflows/source-watch.yml`: weekly/manual workflow that runs GitHub Source Watch, uploads reports, and can create/update GitHub issues for changed watched source.
- `.github/workflows/ci.yml`: main-branch deploy workflow. It syncs the checked-out repo to the server, builds there on Linux, publishes live site, and runs non-blocking sanity checks. Remote warnings that do not appear locally usually mean a Git-tracked path case mismatch or a locally present file ignored by `.gitignore`.
- `.github/workflows/ci-debug.yml`: manual/push diagnostic workflow for checking GitHub Actions trigger context.

Issue and PR templates:

- `.github/ISSUE_TEMPLATE/docs-request.yml`: asks for source of truth, audience, impact, pages, and verification source.
- `.github/pull_request_template.md`: asks for summary, change type, verification, source of truth, affected pages, and follow-up docs.

## Repo Directories

- `docs/`: published Markdown docs and internal maintainer docs.
- `tools/`: maintenance scripts and review prompts.
- `tools/state/`: ignored local/generated shared tool state. Source Watch uses `tools/state/source-watch-baseline.json` as its default baseline when scans are updated. Legacy local memory-bank files may live under `tools/state/memory-bank/`.
- `tools/discord_dev_digest/state/`: ignored local Discord exports and digest reports.
- `overrides/`: MkDocs Material theme overrides. Keep this; `mkdocs.yml` uses it through `custom_dir: overrides`.
- `site/`: generated MkDocs build output. Do not edit by hand.
- `.venv/`: local Python virtualenv. Do not commit.

## Agent Context

Read `AGENTS.md` first. Use this page for repository map, then use [Source Watch Playbook](source-watch-playbook.md) for source-backed review sessions.

Do not add a large manual memory bank by default. Put durable shared rules in `AGENTS.md`, published maintainer workflow in `docs/`, and local/generated scan state in `tools/state/`.

## Cleanup Rules

Safe to remove when they appear:

- `.tmp_*`
- `__pycache__/`
- `.DS_Store`
- `.cache/`
- `.metals/`
- generated `site/` output

Do not remove `overrides/` unless `mkdocs.yml` no longer uses a custom theme directory.

Keep generated local state under `tools/state/`; do not put it back in the repo root.

## Remote Build Gotchas

Linux deploys are stricter than local macOS builds:

- Check case-sensitive paths with `git ls-files` when remote MkDocs says a nav target is missing.
- Check ignored pages with `git check-ignore -v docs/path/file.md` when a page exists locally but not remotely.
- New docs files must be tracked and committed; the deploy workflow does not see ignored or untracked local files.
- Broad Python ignore rules such as `lib/` can accidentally hide docs directories named `lib`; use narrow unignore rules for docs paths that must be published.

## Before Finishing Changes

Run:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/nav_audit.py --strict
.venv/bin/python tools/structure_audit.py --strict
git diff --check
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```
