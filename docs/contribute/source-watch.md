---
tags:
  - contribute
  - documentation
  - workflow
  - source-watch
  - docs-as-code
owner: docs
last_reviewed: 2026-05-26
---

# Source Watch

Source Watch connects docs pages to product repositories. It helps maintainers find pages that may need review after source code, API, configuration, or release changes.

For repeatable maintainer/agent workflow, see the [Source Watch playbook](source-watch-playbook.md).

## Page Metadata

Add metadata to pages that depend on source repositories:

```yaml
---
owner: docs
last_reviewed: never
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/application.conf
      - src/main/scala/org/ergoplatform/nodeView/
source_of_truth:
  - https://github.com/ergoplatform/ergo
---
```

Fields:

- `owner`: person or team responsible for review.
- `last_reviewed`: date when page was last checked against source behavior, or `never` for mappings that have not been reviewed yet.
- `source_repos`: GitHub repositories and paths that can make page stale.
- `source_of_truth`: links reviewers should use to verify claims.

## Local Validation

Run metadata validation and print watched pages:

```bash
python tools/source_watch.py --strict
```

Equivalent subcommand form:

```bash
python tools/source_watch.py scan --strict
```

## GitHub Change Scan

Run commit scan for watched source paths:

```bash
GITHUB_TOKEN=... python tools/source_watch.py --github
```

The script returns a non-zero exit code when source changes are found. Use that behavior for scheduled maintenance jobs or manual review, not normal docs builds.

Useful scan controls:

```bash
python tools/source_watch.py --github --since 2026-01-01 --repo ergoplatform/sigma-rust --max-queries 50
python tools/source_watch.py --github --page docs/dev/stack/sigma-rust.md --max-queries 20
python tools/source_watch.py --github --format json --output source-watch.json
python tools/source_watch.py --github --new-only --update-baseline
python tools/source_watch.py --github --validate-paths
```

Use `GITHUB_TOKEN` for larger scans. Unauthenticated GitHub API requests hit rate limits quickly.
The tool also loads `GITHUB_TOKEN` from a local `.env` file when present.

## Ignoring Noise

Some watched repos produce metadata-only or formatting-only changes. Ignore those in page frontmatter:

```yaml
source_ignore:
  commits:
    - abc123
  messages:
    - "process:"
    - "prettierrc"
  paths:
    - "docs/**"
```

Ignore rules affect reports only. They do not remove source links.

## Severity

GitHub scans classify changes:

- `high`: APIs, config, contracts, EIPs, wallet, mining, or core source paths.
- `medium`: examples, tutorials, tests, scripts, or general docs.
- `low`: metadata, anchors, formatting, process, typo, or Prettier-style changes.

Severity is a triage hint, not an accuracy guarantee.

## Baseline

Use a baseline to show only new source changes since the last scan:

```bash
python tools/source_watch.py --github --new-only --update-baseline
```

Default baseline path:

```text
memory-bank/source-watch-baseline.json
```

## Suggestions And Review Completion

Suggest metadata from GitHub links in a page:

```bash
python tools/source_watch.py suggest docs/dev/stack/headless.md
```

After a page has been checked against source behavior:

```bash
python tools/source_watch.py mark-reviewed docs/dev/stack/headless.md
```

This updates `last_reviewed` to today's date. Use `--date YYYY-MM-DD` to set an explicit date.

## Issues And PR Comments

Write a PR-comment body:

```bash
python tools/source_watch.py --github --pr-comment-file /tmp/source-watch-pr.md
```

Create or update GitHub issues for changed pages:

```bash
GITHUB_REPOSITORY=owner/repo python tools/source_watch.py --github --create-issues
```

Use `--dry-run` to preview intended issue actions.
Use `--no-fail-on-changes` for scheduled workflows where changed source should create or update issues without failing the workflow.

## Review Workflow

1. Add Source Watch metadata to pages tied to product behavior.
2. Run `python tools/source_watch.py --github`.
3. For pages with source changes, inspect linked commits.
4. Use the [AI Docs Review Prompt](https://github.com/glasgowm148/ergodocs/blob/main/tools/ai_docs_review_prompt.md) for a first-pass review.
5. Update docs, then set `last_reviewed` to the review date.
