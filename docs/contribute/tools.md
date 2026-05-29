---
title: Documentation Tools
description: Maintainer guide to ErgoDocs tooling in the tools directory.
tags:
  - documentation
  - maintainer
  - tooling
owner: docs
last_reviewed: 2026-05-27
---

# Documentation Tools

This page explains the scripts and prompt files in `tools/`.

Run Python tools from the repository root, preferably through the local virtualenv:

```bash
.venv/bin/python tools/source_watch.py scan --strict
```

## Core Checks

### `tools/source_watch.py`

Tracks docs pages against upstream GitHub repositories using `source_repos` metadata.

Use it to:

- validate Source Watch frontmatter
- scan watched GitHub paths for changes
- suggest `source_repos` metadata from GitHub links
- mark pages reviewed after source verification
- write/update the baseline at `tools/state/source-watch-baseline.json`

Common commands:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/source_watch.py scan --github --new-only --repo ergoplatform/ergo --max-queries 120 --no-fail-on-changes --format markdown --output /tmp/source-watch-ergo.md
.venv/bin/python tools/source_watch.py suggest docs/dev/stack/headless.md
.venv/bin/python tools/source_watch.py mark-reviewed docs/dev/stack/headless.md
```

Use a `GITHUB_TOKEN` in `.env` for GitHub scans.

### `tools/nav_audit.py`

Checks MkDocs navigation health.

It reports:

- missing nav targets
- duplicate nav targets
- active docs not reachable from nav

Run after nav edits:

```bash
.venv/bin/python tools/nav_audit.py --strict
```

If remote MkDocs warns about a missing nav target that does not fail locally, check Git's tracked paths, not only the local filesystem. Case-only directory differences can be hidden on macOS and fail on Linux:

```bash
git ls-files docs/dev/Integration/guide.md docs/dev/integration/guide.md
```

### `tools/structure_audit.py`

Checks information architecture health across the docs set.

It reports:

- active docs count
- nav coverage
- duplicates and cross-surface duplicates
- orphan pages
- source-watched coverage by area
- max nav depth

Run after section moves or large docs reshuffles:

```bash
.venv/bin/python tools/structure_audit.py --strict
```

Use Markdown output for review notes:

```bash
.venv/bin/python tools/structure_audit.py --markdown
```

### `tools/discord_dev_digest/discord_dev_digest.py`

Exports the Ergo Discord development channel with DiscordChatExporter and turns the chat log into docs-review leads.

Use it to:

- export recent development chat from Discord
- parse topics, URLs, and high-signal messages
- map discussion topics to likely docs pages
- switch analysis profiles for different review tasks
- write a Codex-ready review prompt

Default channel is Ergo's development channel. The tool reads `DISCORD_TOKEN` from `.env`, but never writes the token to reports.

Run a past-month scan:

```bash
.venv/bin/python tools/discord_dev_digest/discord_dev_digest.py scan --days 31
```

Analyze an existing PlainText export:

```bash
.venv/bin/python tools/discord_dev_digest/discord_dev_digest.py analyze --input /path/to/export.txt
```

Dry-run exporter path/date setup without calling Discord:

```bash
.venv/bin/python tools/discord_dev_digest/discord_dev_digest.py scan --days 31 --dry-run
```

Find ecosystem project leads from the past few months:

```bash
.venv/bin/python tools/discord_dev_digest/discord_dev_digest.py scan --days 120 --profile ecosystem
```

Audit all GitHub repositories linked in a Discord export and compare them with docs text:

```bash
.venv/bin/python tools/discord_dev_digest/discord_dev_digest.py analyze --profile github-links --input tools/discord_dev_digest/state/669989266478202917-after-2026-01-27.txt
```

Reports are written under `tools/discord_dev_digest/state/`.

Treat Discord output as leads only. Verify claims against source repositories, issues, releases, EIPs, or maintainer confirmation before changing docs.

### `tools/ai_docs_draft_prs.py`

Creates AI-assisted draft pull requests from a Source Watch JSON report.

The script uses GitHub Models to compare a candidate docs page with upstream commit context and choose:

- `no-doc-change`
- `needs-human-review`
- `draft-pr-safe`

It only opens draft PRs for `draft-pr-safe` results. Draft PRs still require human review and must not be auto-merged.

Common dry run:

```bash
.venv/bin/python tools/ai_docs_draft_prs.py \
  --report /tmp/source-watch.json \
  --repo ergoplatform/ergodocs \
  --dry-run
```

The GitHub Actions workflow `.github/workflows/ai-docs-draft-prs.yml` is the normal way to run it with GitHub Models permissions.

External repositories that are useful for maintainer context but do not currently need user-facing Ergo project pages:

- [Backlog.md](https://github.com/MrLesk/Backlog.md), [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills), [claude-dbc](https://github.com/mwaddip/claude-dbc), and [nanoclaw](https://github.com/qwibitai/nanoclaw): external AI-agent and project-workflow tools useful only as maintainer workflow references.
- [cmttk](https://github.com/mwaddip/cmttk), [otzi](https://github.com/mwaddip/otzi), and [n64llm-legend-of-Elya](https://github.com/sophiaeagent-beep/n64llm-legend-of-Elya): adjacent Cardano, Bitcoin, and AI-demo repositories.
- [PocketFlow Tutorial Codebase Knowledge](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge): external codebase-to-tutorial tool that can help maintainers understand unfamiliar repositories before writing docs.

## Build Hooks

### `tools/hooks.py`

MkDocs imports this through `mkdocs.yml`:

```yaml
on_page_markdown: "tools.hooks:fix_lists"
```

The hook normalizes over-indented nested list markers before Markdown rendering.

Do not run it directly. Validate hook changes with:

```bash
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-hooks-check
```

## Prompt Files

### `tools/ai_docs_review_prompt.md`

Prompt template for source-backed docs review.

Use it when reviewing a PR, source diff, release note, EIP, or upstream code change. It asks the reviewer to check reader goal, technical accuracy, verification, safety, IA, style, and freshness risk.

### `tools/markdown_prompt.md`

Compact Markdown formatting prompt for docs cleanup.

Use it when asking an AI assistant to normalize headings, details blocks, bullets, code blocks, and links for MkDocs.

## Utility Scripts

### `tools/links.sh`

Extracts HTTP links from the repository into `links.txt`, then writes GitHub links into `GitHub.txt`.

Run:

```bash
bash tools/links.sh
```

Generated files are ignored by Git unless deliberately added.

### `tools/zip_files.py`

Creates `md_files.zip` containing Markdown files from the current working tree.

Run:

```bash
.venv/bin/python tools/zip_files.py
```

Generated `md_files.zip` is ignored by Git.

### `tools/deploy.sh`

Legacy manual deploy helper that SSHes into the old server and rebuilds the site there.

Normal publishing should use GitHub Actions instead:

- `.github/workflows/docs-quality.yml` for PR checks
- `.github/workflows/source-watch.yml` for scheduled source scans
- `.github/workflows/ci.yml` for main-branch deploy

Only run `tools/deploy.sh` when explicitly asked and when server access is intended.

## Local State

`tools/state/` stores ignored local/generated tool state.

Current uses:

- `tools/state/source-watch-baseline.json`: Source Watch baseline when `--update-baseline` is used.
- `tools/state/memory-bank/`: legacy local notes moved out of the repository root.
- `tools/discord_dev_digest/state/`: local Discord exports and generated reports.

Do not put durable project rules in `tools/state/`. Use `AGENTS.md` and maintainer docs instead.

## Tracked Files And Ignore Rules

Some docs directories can match broad development ignore rules. For example, Python templates often ignore `lib/`, which also matches `docs/dev/lib/`.

Before relying on a new page that builds locally, confirm Git can see it:

```bash
git status --short --untracked-files=all
git check-ignore -v docs/dev/lib/ergots.md
```

If a docs directory is wrongly ignored, add a narrow exception for that docs path rather than weakening the general ignore rule.

## Standard Verification Set

For most docs/tooling changes, run:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/nav_audit.py --strict
.venv/bin/python tools/structure_audit.py --strict
git diff --check
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```
