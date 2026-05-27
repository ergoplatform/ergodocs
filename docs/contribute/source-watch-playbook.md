---
tags:
  - contribute
  - documentation
  - workflow
  - source-watch
  - maintainer
owner: docs
last_reviewed: 2026-05-27
---

# Source Watch Playbook

Use this page when continuing source-backed docs review.

## What Source Watch Does

`tools/source_watch.py` maps docs pages to upstream GitHub repositories using page frontmatter:

```yaml
owner: docs
last_reviewed: never
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/application.conf
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/application.conf
```

It can:

- validate metadata
- scan GitHub commits for watched paths
- suggest `source_repos` from GitHub links
- mark pages reviewed
- maintain a baseline so later scans show only new commits
- validate watched GitHub paths exist

## Environment

Use repo virtualenv:

```bash
source .venv/bin/activate
```

The script loads `GITHUB_TOKEN` from `.env` if present. Use a token for GitHub scans; unauthenticated GitHub API limits are low.

## Fast Local Checks

Run these before and after edits:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/nav_audit.py --strict
.venv/bin/python tools/structure_audit.py --strict
git diff --check
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```

## Scan For Source Changes

All watched pages:

```bash
.venv/bin/python tools/source_watch.py scan --github --new-only --no-fail-on-changes --format markdown --output /tmp/source-watch.md
```

Focus one repo:

```bash
.venv/bin/python tools/source_watch.py scan --github --new-only --repo ergoplatform/ergo --max-queries 120 --no-fail-on-changes --format markdown --output /tmp/source-watch-ergo.md
```

Focus page family:

```bash
.venv/bin/python tools/source_watch.py scan --github --new-only --page docs/node --page docs/dev/scs --max-queries 120 --no-fail-on-changes --format markdown --output /tmp/source-watch-focused.md
```

Validate watched paths exist on GitHub:

```bash
.venv/bin/python tools/source_watch.py scan --strict --validate-paths --page docs/node/deploy-runbook.md
```

Update baseline after a scan you have triaged:

```bash
.venv/bin/python tools/source_watch.py scan --github --new-only --update-baseline --no-fail-on-changes
```

Default baseline:

```text
tools/state/source-watch-baseline.json
```

## Review Workflow

1. Run a focused scan.
2. Read `/tmp/source-watch*.md`.
3. For each changed page, inspect upstream commits/files.
4. Update docs naturally. Do not add text like "reviewed by Source Watch".
5. If page was actually checked against source, update `last_reviewed`:

```bash
.venv/bin/python tools/source_watch.py mark-reviewed docs/path/page.md
```

6. Run validation/build commands.

## Good Future Prompt

Paste this in a future agent session:

```text
$caveman Read docs/contribute/source-watch-playbook.md first. Then run a focused source-watch scan for <area/repo>, inspect upstream changes, update docs naturally, mark genuinely reviewed pages, and validate with nav_audit, structure_audit, source_watch --strict, git diff --check, and mkdocs build.
```

Examples:

```text
$caveman Read docs/contribute/source-watch-playbook.md first. Focus ergoplatform/ergo node docs.
```

```text
$caveman Read docs/contribute/source-watch-playbook.md first. Focus Rosen watcher/guard docs.
```

```text
$caveman Read docs/contribute/source-watch-playbook.md first. Focus sigma-rust and ErgoScript docs.
```

## Related Docs

- [Source Watch contributor docs](source-watch.md)
- [Documentation lifecycle](docs-lifecycle.md)
- [Information architecture](information-architecture.md)
