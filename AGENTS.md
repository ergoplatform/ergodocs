# AGENTS.md

## Project Overview

- ErgoDocs is the MkDocs Material documentation site for Ergo.
- Docs live in `docs/`; site config and nav live in `mkdocs.yml`.
- Maintenance scripts live in `tools/`.

## Codex Response Style

- Default to caveman-style brevity for all Codex responses in this project.
- Keep answers terse, direct, and low-filler.
- Prefer short bullets or compact paragraphs.
- Do not add long explanations unless explicitly asked.
- Preserve technical accuracy and call out uncertainty.
- Never compress or alter code, commands, file paths, identifiers, logs, stack traces, or error messages.
- When making changes, summarize only what changed and how to verify it.
- Ask at most one clarifying question when blocked; otherwise make a reasonable assumption and proceed.

## Setup

- Install: `python -m pip install -r requirements.txt`
- Serve locally: `./run.sh`
- Build: `.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check`
- Use the repo `.venv` only. Do not activate stale temporary envs such as `.tmp_mdtest`; if Codex auto-enters one, remove it from `~/.codex/history.jsonl`.

## Repo Layout

- `docs/`: published docs and maintainer docs.
- `docs/start_here.md`: maintainer map for workflows, tools, and repo hygiene.
- `tools/source_watch.py`: source-linked docs scanner.
- `tools/source_watch_inventory.py`: generates/checks `docs/contribute/source-watch-inventory.md` from page `source_repos`.
- `tools/discord_dev_digest/discord_dev_digest.py`: exports Discord development chat and generates source-verification leads.
- `tools/discord_dev_digest/state/`: ignored local Discord exports and digest reports.
- `tools/weekly_docs_prs.py`: opens/updates per-page source-review issues from Source Watch JSON.
- `tools/ai_docs_draft_prs.py`: optional GitHub Models-assisted draft PR creator from Source Watch JSON.
- `tools/nav_audit.py`: navigation coverage check.
- `tools/structure_audit.py`: section structure check.
- `.github/workflows/docs-quality.yml`: PR build and docs audit workflow.
- `.github/workflows/source-watch.yml`: scheduled watched-source scan and issue creation.
- `.github/workflows/weekly-discord-docs.yml`: Friday Discord lead scan, artifact upload, weekly tracking issue, and per-page source-review issues.
- `.github/workflows/ai-docs-draft-prs.yml`: manual AI-assisted draft PR workflow using GitHub Models; never auto-merges.
- `.github/workflows/ci.yml`: main-branch deploy workflow.
- `.github/codeql/codeql-config.yml`: CodeQL config; excludes legacy non-executable assets such as `docs/assets/mathjax2.js`.
- `overrides/`: MkDocs Material theme overrides; keep because `mkdocs.yml` uses `custom_dir: overrides`.
- `tools/state/`: ignored local/generated working state, not durable project guidance.

## Engineering Rules

- Keep changes small and focused.
- Do not introduce new dependencies without asking.
- Prefer existing docs structure, nav naming, and Markdown style.
- Linux deploy builds are case-sensitive. If MkDocs warns remotely but not locally, check for case-only path mismatches tracked by Git.
- `.gitignore` has broad Python ignores such as `lib/`; docs subdirectories named `lib` must be explicitly unignored or new files inside them will exist locally but not deploy.
- When source behavior changes, update docs naturally; do not add tool-review boilerplate.
- Do not paste date-stamped changelog bullets into conceptual docs unless the page is already a changelog or release note. Fold verified changes into the relevant explanation, caveat, or workflow section in the page's existing voice.
- Set `last_reviewed` only after the page was actually checked against source.
- Treat Discord chat as review leads only; verify against repositories, issues, releases, EIPs, or maintainer confirmation before changing docs.
- For broad ecosystem sweeps, run Discord Dev Digest with `--profile ecosystem` and `--profile github-links`; compare linked GitHub repos against docs before deciding what belongs.
- Do not put secrets, credentials, tokens, or private data in docs or project memory.

## Link Style

- For normal Markdown links between docs pages, prefer basename-only links: `[Label](page.md)`.
- Do not rewrite normal Markdown links to full relative paths such as `../eco/page.md` or `docs/eco/page.md` unless required by non-doc context.
- Exception: card blocks (`::cards::`) with JSON/YAML `url` fields must use a valid relative path from the current page to the target page. A basename is OK only when the target page is in the same directory.
- Root `README.md` is GitHub-facing, not a docs page; links from README should use repo-relative paths such as `docs/contribute/tools.md`.
- Do not re-add hook logic that rewrites card `url` basenames at render time. Card paths should be explicit in source.
- After broad link edits, scan card URLs and run MkDocs build; card links can fail differently than normal Markdown links.

## Source Watch

- Use `docs/contribute/source-watch.md` for metadata rules.
- Use `docs/contribute/source-watch-playbook.md` for repeatable scan workflow.
- Source Watch baseline defaults to `tools/state/source-watch-baseline.json`.
- Use GitHub scans only with `GITHUB_TOKEN` available; `.env` may provide it locally.
- Source Watch JSON includes `author_login` when GitHub exposes a linked user for a commit, open pull request, or release.
- Source Watch scans watched GitHub path commits, GitHub releases from watched repositories, and open pull requests touching watched paths only for important owners. Default open PR owner is `ergoplatform`; add owners with `--open-pr-owner`.
- Do not add broad external standards, analytics trackers, or one-off aggregator PRs to `source_repos` unless ongoing changes should trigger docs review; keep those as `source_of_truth` links only.

## Discord Dev Digest Handoff

- Current report: `tools/discord_dev_digest/state/669989266478202917-after-2026-04-26-report.md`.
- Latest focused Source Watch output: `/tmp/source-watch-discord-guided.md`.
- Resume prompt: `$caveman Read AGENTS.md, docs/contribute/source-watch-playbook.md, and tools/discord_dev_digest/state/669989266478202917-after-2026-04-26-report.md. Treat Discord as leads only. Continue source-backed doc updates from the 2026-05 Discord dev digest, verify against GitHub PRs/repos before editing, skip unverified sidechain-prefix claims, then run source_watch --strict, nav_audit --strict, structure_audit --strict, git diff --check, and mkdocs build.`
- Verified PR leads already checked: `ergoplatform/ergo#2299`, `#2302`, `#2305`, `#2310` are merged into `v6.0.3`; `ergoplatform/sigmastate-interpreter#1136` is merged into `v6.0.4`; `ergoplatform/ergo#2306`, `#2307`, `#2312`, `ergoplatform/ergo-appkit#253`, and `ergoplatform/sigmastate-interpreter#1138` were open when checked on 2026-05-27.

## Weekly Docs Review

- `DISCORD_TOKEN` is configured as a GitHub Actions repository secret; do not commit `.env`.
- `.github/workflows/weekly-discord-docs.yml` is named `Weekly Docs Review`; it runs Fridays at 09:00 UTC and supports manual runs with `days`, `after`, and `mode`.
- Manual `mode` values: `full`, `discord-only`, `source-only`.
- In `full` and `discord-only`, it exports the previous week from general (`668903786902847502`) and development (`669989266478202917`), then generates `docs`, `ecosystem`, and `github-links` reports.
- The workflow separately runs Source Watch across every page with `source_repos` for the same date window. This scan is not limited to repositories mentioned on Discord that week.
- It then calls `tools/weekly_docs_prs.py` to open/update per-page source-review issues.
- `tools/weekly_docs_prs.py` labels per-page issues `docs`, `source-watch`, and `automated`; titles include the review window.
- `tools/weekly_docs_prs.py` skips pages whose `last_reviewed` date is on or after the latest matching source commit, and skips low-severity-only pages by default.
- If every per-page candidate is skipped, the weekly workflow comments on the tracking issue and closes it as up to date. Keep the tracking issue open only when actionable page-review issues or errors remain.
- The workflow closes older open weekly tracking issues as superseded, labels the current tracking issue `docs`, `automated`, and `weekly-review`, writes a GitHub Actions summary, and uploads the per-page issue summary as an artifact.
- Weekly review and AI draft PR workflows share `concurrency.group: docs-source-watch` so broad Source Watch scans do not run concurrently. Weekly review has `timeout-minutes: 20`.
- Per-page review issues list source commit authors as plain usernames only; do not add `@` mentions until the automation has proven low-noise.
- Keep Discord exports/reports as artifacts or ignored local state. Do not commit raw Discord logs or generated reports with chat content.
- These issues are review leads, not proof that docs changes are required. Verify source before editing public docs.

## AI Draft PRs

- `.github/workflows/ai-docs-draft-prs.yml` is manual only.
- It runs Source Watch for the requested window, asks GitHub Models to assess candidate pages, and may open one draft PR per page.
- Draft PRs are labelled `docs`, `automated`, and `needs-human-review`; sensitive pages also get `sensitive`.
- It uses optional `DOCS_BOT_TOKEN` for checkout, branch pushes, and PR creation; otherwise falls back to `GITHUB_TOKEN`. Prefer `DOCS_BOT_TOKEN` if generated PRs should trigger normal PR workflows.
- AI output must remain draft-only. Never auto-merge AI docs PRs.
- The script should choose `needs-human-review` or `no-doc-change` when source evidence is weak; humans still verify every source claim before merge.

## CI and Deployment

- Pull requests touching docs/tooling run `.github/workflows/docs-quality.yml`.
- Weekly/source-triggered review uses `.github/workflows/source-watch.yml`.
- Weekly Discord lead review uses `.github/workflows/weekly-discord-docs.yml`.
- Main branch deploy uses `.github/workflows/ci.yml`.
- Deploy syncs the checked-out repo to the server, then builds on Linux from `PROJECT_DIR/src`; only committed/tracked files are present remotely.
- Remote deploy now skips `apt-get update` when `python3-venv`, `python3-pip`, and `rsync` are already installed. If installation is needed and the Caddy apt source is configured, the workflow refreshes the Caddy Cloudsmith key before updating package indexes.
- `tools/deploy.sh` is a manual legacy deploy helper; prefer GitHub Actions unless explicitly asked.

## Verification

Before saying work is complete, run the narrowest relevant checks first. For docs/tooling changes, prefer:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/source_watch_inventory.py --check
.venv/bin/python tools/nav_audit.py --strict
.venv/bin/python tools/structure_audit.py --strict
git diff --check
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```

If a check is not run, say why.

## PR/Review Expectations

- Call out risky changes, broken links, nav movement, generated files, and any unchecked source claims.
- Keep generated build output, local caches, `.env`, and virtualenv files out of commits.
