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
- `tools/discord_dev_digest/discord_dev_digest.py`: exports Discord development chat and generates source-verification leads.
- `tools/discord_dev_digest/state/`: ignored local Discord exports and digest reports.
- `tools/nav_audit.py`: navigation coverage check.
- `tools/structure_audit.py`: section structure check.
- `.github/workflows/docs-quality.yml`: PR build and docs audit workflow.
- `.github/workflows/source-watch.yml`: scheduled watched-source scan and issue creation.
- `.github/workflows/ci.yml`: main-branch deploy workflow.
- `overrides/`: MkDocs Material theme overrides; keep because `mkdocs.yml` uses `custom_dir: overrides`.
- `tools/state/`: ignored local/generated working state, not durable project guidance.

## Engineering Rules

- Keep changes small and focused.
- Do not introduce new dependencies without asking.
- Prefer existing docs structure, nav naming, and Markdown style.
- When source behavior changes, update docs naturally; do not add tool-review boilerplate.
- Do not paste date-stamped changelog bullets into conceptual docs unless the page is already a changelog or release note. Fold verified changes into the relevant explanation, caveat, or workflow section in the page's existing voice.
- Set `last_reviewed` only after the page was actually checked against source.
- Treat Discord chat as review leads only; verify against repositories, issues, releases, EIPs, or maintainer confirmation before changing docs.
- For broad ecosystem sweeps, run Discord Dev Digest with `--profile ecosystem` and `--profile github-links`; compare linked GitHub repos against docs before deciding what belongs.
- Do not put secrets, credentials, tokens, or private data in docs or project memory.

## Source Watch

- Use `docs/contribute/source-watch.md` for metadata rules.
- Use `docs/contribute/source-watch-playbook.md` for repeatable scan workflow.
- Source Watch baseline defaults to `tools/state/source-watch-baseline.json`.
- Use GitHub scans only with `GITHUB_TOKEN` available; `.env` may provide it locally.

## Discord Dev Digest Handoff

- Current report: `tools/discord_dev_digest/state/669989266478202917-after-2026-04-26-report.md`.
- Latest focused Source Watch output: `/tmp/source-watch-discord-guided.md`.
- Resume prompt: `$caveman Read AGENTS.md, docs/contribute/source-watch-playbook.md, and tools/discord_dev_digest/state/669989266478202917-after-2026-04-26-report.md. Treat Discord as leads only. Continue source-backed doc updates from the 2026-05 Discord dev digest, verify against GitHub PRs/repos before editing, skip unverified sidechain-prefix claims, then run source_watch --strict, nav_audit --strict, structure_audit --strict, git diff --check, and mkdocs build.`
- Verified PR leads already checked: `ergoplatform/ergo#2299`, `#2302`, `#2305`, `#2310` are merged into `v6.0.3`; `ergoplatform/sigmastate-interpreter#1136` is merged into `v6.0.4`; `ergoplatform/ergo#2306`, `#2307`, `#2312`, `ergoplatform/ergo-appkit#253`, and `ergoplatform/sigmastate-interpreter#1138` were open when checked on 2026-05-27.

## CI and Deployment

- Pull requests touching docs/tooling run `.github/workflows/docs-quality.yml`.
- Weekly/source-triggered review uses `.github/workflows/source-watch.yml`.
- Main branch deploy uses `.github/workflows/ci.yml`.
- `tools/deploy.sh` is a manual legacy deploy helper; prefer GitHub Actions unless explicitly asked.

## Verification

Before saying work is complete, run the narrowest relevant checks first. For docs/tooling changes, prefer:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/nav_audit.py --strict
.venv/bin/python tools/structure_audit.py --strict
git diff --check
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```

If a check is not run, say why.

## PR/Review Expectations

- Call out risky changes, broken links, nav movement, generated files, and any unchecked source claims.
- Keep generated build output, local caches, `.env`, and virtualenv files out of commits.
