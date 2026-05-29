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

For the broader automation map, see [Documentation Automation](automation.md). For repeatable review commands, see the [Source Watch playbook](source-watch-playbook.md).

For a generated overview of everything currently watched, see [Watched Repositories](source-watch-inventory.md).

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

Only add repositories to `source_repos` when ongoing upstream changes should trigger docs review. Stable external standards, one-off reference links, analytics trackers, and aggregator pull requests usually belong in `source_of_truth` only, not active scans.

## Local Validation

Run metadata validation and print watched pages:

```bash
.venv/bin/python tools/source_watch.py scan --strict
```

## GitHub Change Scan

Run a GitHub scan for watched source paths, open pull requests, and releases:

```bash
GITHUB_TOKEN=... .venv/bin/python tools/source_watch.py scan --github
```

The script returns a non-zero exit code when source changes are found. A source change can be a commit touching a watched path, an open pull request touching a watched path in an important watched repository, or a GitHub release from a watched repository. By default, open pull request checks are limited to watched repositories under the `ergoplatform` GitHub owner. Use that behavior for scheduled maintenance jobs or manual review, not normal docs builds.

Useful scan controls:

```bash
.venv/bin/python tools/source_watch.py scan --github --since 2026-01-01 --repo ergoplatform/sigma-rust --max-queries 50
.venv/bin/python tools/source_watch.py scan --github --page docs/dev/stack/sigma-rust.md --max-queries 20
.venv/bin/python tools/source_watch.py scan --github --format json --output source-watch.json
.venv/bin/python tools/source_watch.py scan --github --new-only --update-baseline
.venv/bin/python tools/source_watch.py scan --github --validate-paths
.venv/bin/python tools/source_watch.py scan --github --open-pr-owner ergoplatform --open-pr-owner rosen-bridge
.venv/bin/python tools/source_watch.py scan --github --no-open-prs
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
.venv/bin/python tools/source_watch.py scan --github --new-only --update-baseline
```

Default baseline path:

```text
tools/state/source-watch-baseline.json
```

## Suggestions And Review Completion

Suggest metadata from GitHub links in a page:

```bash
.venv/bin/python tools/source_watch.py suggest docs/dev/stack/headless.md
```

After a page has been checked against source behavior:

```bash
.venv/bin/python tools/source_watch.py mark-reviewed docs/dev/stack/headless.md
```

This updates `last_reviewed` to today's date. Use `--date YYYY-MM-DD` to set an explicit date.

## Inventory

Regenerate the watched-repository inventory after changing `source_repos` metadata:

```bash
.venv/bin/python tools/source_watch_inventory.py --write
```

CI runs `tools/source_watch_inventory.py --check` so the published inventory stays aligned with page frontmatter.

## Issues And PR Comments

Write a PR-comment body:

```bash
.venv/bin/python tools/source_watch.py scan --github --pr-comment-file /tmp/source-watch-pr.md
```

Create or update GitHub issues for changed pages:

```bash
GITHUB_REPOSITORY=owner/repo .venv/bin/python tools/source_watch.py scan --github --create-issues
```

Use `--dry-run` to preview intended issue actions.
Use `--no-fail-on-changes` for scheduled workflows where changed source should create or update issues without failing the workflow.

## Review Workflow

1. Add Source Watch metadata to pages tied to product behavior.
2. Run `.venv/bin/python tools/source_watch.py scan --github`.
3. For pages with source changes, inspect linked commits.
4. Use the [AI Docs Review Prompt](https://github.com/glasgowm148/ergodocs/blob/main/tools/ai_docs_review_prompt.md) for a first-pass review.
5. Update docs, then set `last_reviewed` to the review date.

## Weekly Automation

The weekly docs workflow combines recent source changes with discussion-derived leads. It can create review issues for pages that may need attention, but those issues are not proof that a public docs change is required.

When reviewing an automated issue:

1. Open the upstream source link.
2. Check whether the published page is stale or incomplete.
3. Update the docs only when the source confirms a reader-visible change.
4. Close the issue with a short note if no docs change is needed.
