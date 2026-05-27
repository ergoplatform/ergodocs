# AGENTS.md

## Project Overview

- ErgoDocs is the MkDocs Material documentation site for Ergo.
- Docs live in `docs/`; site config and nav live in `mkdocs.yml`.
- Maintenance scripts live in `tools/`.

## Setup

- Install: `python -m pip install -r requirements.txt`
- Serve locally: `./run.sh`
- Build: `.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check`

## Repo Layout

- `docs/`: published docs and maintainer docs.
- `docs/start_here.md`: maintainer map for workflows, tools, and repo hygiene.
- `tools/source_watch.py`: source-linked docs scanner.
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
- Set `last_reviewed` only after the page was actually checked against source.
- Treat Discord chat as review leads only; verify against repositories, issues, releases, EIPs, or maintainer confirmation before changing docs.
- Do not put secrets, credentials, tokens, or private data in docs or project memory.

## Source Watch

- Use `docs/contribute/source-watch.md` for metadata rules.
- Use `docs/contribute/source-watch-playbook.md` for repeatable scan workflow.
- Source Watch baseline defaults to `tools/state/source-watch-baseline.json`.
- Use GitHub scans only with `GITHUB_TOKEN` available; `.env` may provide it locally.

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
