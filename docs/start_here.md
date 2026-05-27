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

- [Source Watch](contribute/source-watch.md): connect pages to upstream repositories, scan for source changes, and mark pages reviewed only after checking the source.
- [Source Watch Playbook](contribute/source-watch-playbook.md): repeatable command list for future source-backed review sessions.
- [Information Architecture](contribute/information-architecture.md): how sections should be structured and how pages should link together.
- [Documentation Lifecycle](contribute/docs-lifecycle.md): page ownership, review expectations, and freshness rules.
- [Content Standards](contribute/content-standards.md): writing style, structure, and review standards.
- [Contribute to the Docs](contribute/docs.md): general contribution path for docs changes.

## Core Files

- `AGENTS.md`: repo-level instructions for Codex and other coding agents.
- `mkdocs.yml`: site configuration, navigation, theme setup, plugins, and hooks.
- `requirements.txt`: Python dependencies for local builds and docs tooling.
- `run.sh`: activates the repo virtualenv and starts `mkdocs serve`.
- `hooks.py`: MkDocs hook code used during rendering.
- `refs.bib`: bibliography/reference data.

## Tools

- `tools/source_watch.py`: validates `source_repos` metadata and scans watched GitHub paths for commits.
- `tools/nav_audit.py`: checks navigation coverage and obvious nav problems.
- `tools/structure_audit.py`: checks section structure, orphan pages, and duplicate labels.
- `tools/ai_docs_review_prompt.md`: prompt template for source-backed docs review.
- `tools/links.sh`: link checking helper.
- `tools/deploy.sh`: deploy helper.

Use the repo virtualenv for Python tools:

```bash
source .venv/bin/activate
```

or call tools directly:

```bash
.venv/bin/python tools/source_watch.py scan --strict
```

## Repo Directories

- `docs/`: published Markdown docs and internal maintainer docs.
- `tools/`: maintenance scripts and review prompts.
- `overrides/`: MkDocs Material theme overrides. Keep this; `mkdocs.yml` uses it through `custom_dir: overrides`.
- `memory-bank/`: ignored local/generated working memory, not durable project guidance. Source Watch uses `memory-bank/source-watch-baseline.json` as its default baseline when scans are updated.
- `site/`: generated MkDocs build output. Do not edit by hand.
- `.venv/`: local Python virtualenv. Do not commit.

## Agent Context

Read `AGENTS.md` first. Use this page for repository map, then use [Source Watch Playbook](contribute/source-watch-playbook.md) for source-backed review sessions.

Do not add a large manual memory bank by default. Put durable shared rules in `AGENTS.md`, published maintainer workflow in `docs/`, and local/generated scan state in `memory-bank/`.

## Cleanup Rules

Safe to remove when they appear:

- `.tmp_*`
- `__pycache__/`
- `.DS_Store`
- `.cache/`
- `.metals/`
- generated `site/` output

Do not remove `overrides/` unless `mkdocs.yml` no longer uses a custom theme directory.

Keep `memory-bank/` unless Source Watch baseline storage is moved and `tools/source_watch.py` is updated.

## Before Finishing Changes

Run:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/nav_audit.py --strict
.venv/bin/python tools/structure_audit.py --strict
git diff --check
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```
