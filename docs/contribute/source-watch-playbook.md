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

Use this page for repeatable source-backed documentation review. For the public overview of the automation system, start with [Documentation Automation](automation.md).

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

## Remote Build Warning Triage

GitHub deploy builds run on Linux from the synced Git checkout, so they can expose problems hidden on macOS:

- Case-only path mismatches: `docs/dev/Integration/guide.md` and `docs/dev/integration/guide.md` are the same path on common macOS volumes but different paths on Linux. If remote MkDocs reports a nav target missing while local builds pass, compare `mkdocs.yml` against `git ls-files`.
- Ignored docs paths: broad Python ignores such as `lib/` can hide docs files under directories named `lib`. A page can exist locally and build locally but be absent from the remote checkout if Git ignores it. Use `git status --short --untracked-files=all` and `git check-ignore -v docs/path/file.md`.
- Commit coverage: the deploy workflow rsyncs the checked-out repository, not arbitrary local files. New pages must be tracked and committed before remote builds can see them.

Useful checks:

```bash
git ls-files docs/dev/Integration/guide.md docs/dev/integration/guide.md docs/dev/lib/ergots.md
git check-ignore -v docs/dev/lib/ergots.md
git status --short --untracked-files=all
```

If a file has the wrong case in Git, use `git mv` so the index records the rename:

```bash
git mv docs/dev/Integration/guide.md docs/dev/integration/guide.md
```

If a docs directory is ignored by a broad rule, add a narrow unignore rule instead of removing the broad Python ignore:

```gitignore
lib/
!docs/dev/lib/
!docs/dev/lib/**
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

## Weekly Docs Review

`.github/workflows/weekly-discord-docs.yml` is named `Weekly Docs Review` in GitHub Actions. It runs every Friday at 09:00 UTC and can also be started manually.

The workflow performs two separate weekly checks:

- It exports the previous week of Discord messages from the general and development channels, then generates docs, ecosystem, and GitHub-links lead reports.
- It runs Source Watch across every page with `source_repos` metadata for the same date window. This full watched-repo scan is not limited to repositories mentioned on Discord that week.

Manual mode options:

- `full`: export Discord leads and scan all watched source repos.
- `discord-only`: export Discord leads only.
- `source-only`: scan all watched source repos only.

The workflow uploads reports, per-page issue results, and summaries as artifacts. It also writes a GitHub Actions run summary with the mode, window, skipped-page counts, created or updated issue counts, errors, and tracking issue number.

It opens or updates a dated GitHub tracking issue labelled `docs`, `automated`, and `weekly-review`. Before opening the current tracking issue, it closes older open weekly tracking issues as superseded.

The workflow uses the shared `docs-source-watch` concurrency group and a 20-minute timeout. If a weekly review or AI draft-PR scan is already active, another broad source-watch run waits instead of starting a duplicate review.

It also runs `tools/weekly_docs_prs.py` against the Source Watch JSON report. That script opens or updates one source-review issue per affected docs page, labels it `docs`, `source-watch`, and `automated`, includes the review window in the title, and lists GitHub commit authors as plain usernames where the GitHub API exposes them. It skips pages whose `last_reviewed` date is on or after the latest matching source commit, and it skips pages where every matching source change is low severity. These are review issues, not proof that a docs update is required.

If all per-page candidates are skipped, the workflow comments on the weekly tracking issue and closes it as up to date. If at least one per-page issue is created, updated, or errors, the tracking issue remains open so maintainers can follow up.

Use those reports as leads only:

1. Read the workflow artifact reports.
2. Verify each candidate update against repositories, releases, issues, EIPs, or maintainer sources.
3. Update docs naturally without mentioning Discord, scans, or internal reports.
4. Run the normal validation commands.
5. Open a PR with source links and verification notes.

The workflow requires the `DISCORD_TOKEN` repository secret. It downloads DiscordChatExporter during the run and uses GitHub's built-in `GITHUB_TOKEN` to create the tracking issue.

## GitHub Deploy Notes

`.github/workflows/ci.yml` deploys the main branch by syncing the checked-out repository to the server and building MkDocs there. It does not rely on a server-side Git checkout.

The remote build runs on Linux. It sees:

- committed files from the GitHub checkout
- case-sensitive paths
- no untracked local files
- no files hidden by `.gitignore`

The workflow only installs `python3-venv`, `python3-pip`, and `rsync` when they are missing. This avoids unrelated apt repository warnings during normal deploys. If package installation is needed and the server has the Caddy apt source configured, the workflow refreshes the Caddy Cloudsmith signing key before running `apt-get update`.

## AI Draft PR Workflow

`.github/workflows/ai-docs-draft-prs.yml` is a manual workflow for creating human-reviewed draft PRs from Source Watch results.

Inputs:

- `since`: explicit Source Watch start date.
- `days`: fallback lookback window when `since` is empty.
- `model`: GitHub Models model ID, defaulting to `openai/gpt-4o-mini`.
- `max_pages`: maximum number of candidate pages to attempt.
- `dry_run`: generate AI decisions without pushing branches or opening PRs.

The workflow:

1. Runs a full Source Watch scan for the requested window.
2. Sends each actionable candidate page and upstream commit context to GitHub Models.
3. Expects one of `no-doc-change`, `needs-human-review`, or `draft-pr-safe`.
4. Creates one draft PR per `draft-pr-safe` page.
5. Labels draft PRs `docs`, `automated`, and `needs-human-review`; sensitive pages also get `sensitive`.
6. Uploads the AI decision JSON as an artifact and writes it to the run summary.

Configure `DOCS_BOT_TOKEN` if you want draft PRs to trigger normal pull request workflows. Without that secret, the workflow uses `GITHUB_TOKEN`, which can push branches and open PRs but may not trigger follow-on PR checks.

Do not auto-merge these PRs. Treat them as AI-authored drafts that require normal maintainer review and CI.

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
