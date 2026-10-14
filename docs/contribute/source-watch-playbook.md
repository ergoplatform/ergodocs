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
- scan GitHub releases only for repository entries with `release_watch: true`
- optionally scan open pull requests that touch watched paths for explicit roadmap/latest-work reviews
- suggest `source_repos` from GitHub links
- mark pages reviewed
- maintain a baseline so later scans show only new source changes
- validate watched GitHub paths exist

Keep `source_repos` focused on upstreams whose ongoing changes can make the page stale. Reference-only standards or aggregator links can stay in `source_of_truth` without being scanned.

Use `branch: default` only on active `source_repos` entries where guessing `master` or `main` would create false path errors. Broad ecosystem inventory entries should stay out of active Source Watch metadata.

## Environment

Use repo virtualenv:

```bash
source .venv/bin/activate
```

The script loads `GITHUB_TOKEN` from `.env` if present. Use a token for GitHub scans; unauthenticated GitHub API limits are low.

Open pull request checks are disabled by default. Add `--open-prs` plus repeated `--open-pr-owner <owner>` only when intentionally reviewing in-flight work, such as a major version candidate tracked on a roadmap page.

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

Weekly hot-path equivalent, excluding broad inventory-only refs:

```bash
.venv/bin/python tools/source_watch.py scan --github --watch-mode narrow --release-owner ergoplatform --release-owner ScorexFoundation --new-only --no-fail-on-changes --format markdown --output /tmp/source-watch.md
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

Regenerate the watched-repository inventory after changing Source Watch metadata:

```bash
.venv/bin/python tools/source_watch_inventory.py --write
```

CI checks the generated page with:

```bash
.venv/bin/python tools/source_watch_inventory.py --check
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

Discord-only repositories are tracking-issue leads, not per-page issues. A new repo mentioned in chat will not be scanned by Source Watch until a relevant docs page adds that repo to `source_repos`.

Manual mode options:

- `full`: export Discord leads and scan all watched source repos.
- `discord-only`: export Discord leads only.
- `source-only`: scan all watched source repos only.

The workflow uploads reports, per-page issue results, and summaries as artifacts. It also writes a GitHub Actions run summary with the mode, window, skipped-page counts, created or updated issue counts, errors, and tracking issue number.

It opens or updates a dated GitHub tracking issue labelled `docs`, `automated`, and `weekly-review`. Before opening the current tracking issue, it closes older open weekly tracking issues as superseded.

The workflow uses the shared `docs-source-watch` concurrency group and a 20-minute timeout. If a weekly review or AI draft-PR scan is already active, another broad source-watch run waits instead of starting a duplicate review.

It also runs `tools/docs_update_candidates.py` through `tools/weekly_docs_prs.py`. The shared candidate layer is page-aware: it filters Source Watch changes against the page path and current page text before opening issues. It skips pages whose `last_reviewed` date is on or after the latest matching source change, skips pages where every matching source change is low severity, skips broad repository activity that does not map clearly to the page, and skips candidates that already appear to be covered in the page text. Release candidates are intentionally stricter than commit candidates: a release only opens a page issue when the page identity or `source_of_truth` release links show that the page is about that repository/release, not merely because the page watches that repository for source-path drift. Issue titles describe the likely missing feature or behavior, for example `Add info on optional minerPk override...`, rather than only naming the page.

The weekly issue step also closes stale open `source-watch` issues when the latest candidate pass no longer marks them actionable.

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
- `provider`: AI provider, defaulting to `openai`.
- `model`: optional AI model ID; defaults to `gpt-5.4-mini` for OpenAI, `openrouter/free` for OpenRouter, and `openai/gpt-4.1` for GitHub Models.
- `max_pages`: maximum number of candidate pages to attempt.
- `max_requests`: total model call cap, including retries; defaults to 9.
- `max_output_tokens`: output cap per model request; defaults to 12000.
- `run_timeout`: execution budget in seconds; defaults to 600.
- `resume_run_id`: optional prior Actions run ID; restores its checkpoint artifact and revalidates against a fresh scan.
- `repo`: optional `owner/name` watched source filter for focused tests.
- `page`: optional docs page or path fragment filter for focused tests.
- `max_queries`: optional Source Watch path-query cap.
- `dry_run`: generate AI decisions without external writes; defaults to `true`. Set `false` explicitly to publish review issues and draft PRs.
- `include_open_prs`: include open pull requests as evidence for explicit latest-work or roadmap tests.

The workflow uses the shared candidate layer and a narrow Source Watch scan. Each candidate's commit patches, release notes, or opt-in PR files are fetched as structured outcomes with source IDs, retrieval status, resolved snapshots, and SHA-256 content identities. Every required source must be available and fit the evidence limits before generation. Missing patches, failed fetches, changing PR snapshots, incomplete file lists, and omitted or oversized evidence produce `unavailable-evidence` and a review-required outcome; no automatic Markdown draft is generated. This conservative gate can require manual review even when some useful evidence exists.

The model still chooses `no-doc-change`, `needs-human-review`, or `draft-pr-safe`. Drafts must cite supplied `source_id` and `content_sha256` pairs in `evidence_refs`. Unknown IDs, wrong hashes, malformed responses, changed frontmatter, destructive edits, and public automation boilerplate are refused. Valid references establish provenance, not factual faithfulness: maintainers must verify each claim, example, and interpretation. The model cannot advance `last_reviewed`; human factual review owns that date.

Validated Markdown can produce a human-reviewed draft PR for either draft action. Review decisions without usable Markdown, unavailable evidence, and rejected drafts can produce review issues. No-change decisions produce no external writes. The script retains existing branch ownership and duplicate checks, refuses to overwrite PRs that are no longer drafts, and checks whitespace, navigation, structure, and the MkDocs build before pushing. Publishing requires a clean checkout and a `--repo` matching GitHub `origin`. A failed repository operation stops the run; generated staged edits may remain for inspection rather than being discarded automatically.

### Checkpoints and resume

The output JSON is also the checkpoint. It is saved atomically after each page transition and model attempt, including the validated decision before publishing. A writer lock prevents concurrent updates. Completed pages remain available when a later page fails or the process is interrupted. Existing output requires `--resume` or a new output path.

In Actions, set `resume_run_id` to a prior run from the same repository and retain the desired provider/model and limits. The workflow downloads only that run's checkpoint, scans sources again, and passes `--resume`. Switching a dry-run checkpoint to explicit publishing reuses matching validated decisions without a new model call. A hard cancellation or runner loss can prevent artifact upload; recovery needs a retained checkpoint.

For example, resume a downloaded artifact locally in the same repository and execution configuration:

```bash
.venv/bin/python tools/ai_docs_draft_prs.py \
  --report /tmp/source-watch.json \
  --repo ergoplatform/ergodocs \
  --output tools/state/ai-docs-draft-prs.json \
  --dry-run --resume
```

Resume re-fetches sources and compares page text, source snapshots/content, candidate metadata, provider/model, limits, target repository/base branch, and implementation fingerprints. Changed inputs invalidate generation reuse. Matching decisions are revalidated through the current evidence and Markdown checks. Matching completed publications are retained; pending or failed publication retries use the existing branch/PR/issue checks without regenerating. In-flight model requests count toward the page attempt cap, even when their response or billing is unknown. An interrupted successful response is saved before normalization so it can be revalidated on resume. Permanent generation failures require changed configuration or a new output path to retry.

`provider`, `model`, `results`, and each result's `page`, `action`, and `url` remain available. Additional fields include `stage`, `outcome`, `decision_outcome`, `sources`, `fingerprints`, `decision`, and `generation`. Outcomes distinguish `unavailable-evidence`, `generation-failure`, `validation-refusal`, `review-required`, `no-change`, `draft-ready`, and `publishing-failure`. Historical rows retained from earlier reports have `current: false`. Exit status is nonzero for current generation, validation, publishing, or execution-limit failures, including dry runs; evidence gates record review-required results without failing the run.

### Execution limits and evaluation

CLI limits default to 3 attempts per page, 9 model requests per invocation, 12000 output tokens per request, 85000 prompt characters, 60 seconds per model request, 180 seconds per page, and 600 seconds per invocation. Use `--max-attempts` (at most 5), `--max-requests`, `--max-output-tokens`, `--max-prompt-chars`, `--request-timeout`, `--page-timeout`, and `--run-timeout` to lower them. Page attempt counts survive resume; request/time budgets restart for each explicit invocation.

Only transient transport failures receive bounded backoff retries. Authentication errors, malformed or truncated output, provider refusals, and validation failures receive no automatic generation retry. Publishing is a separate step and is never included in model retries. Provider/model, returned model identity, reported token usage, unreported usage attempts, elapsed generation time, attempt status, and classified errors are retained. Unknown usage is not reported as zero. These are request/output/time caps, not a dollar spending guarantee; provider billing for timed-out requests may be unavailable. HTTP requests also have wall-clock deadlines, including slow response reads. The CLI uses Unix locks and main-thread timers on macOS/Linux. Publication checks and subprocesses have their own bounded timeouts and can finish beyond the scheduling budget.

Run repeatable policy regression cases without credentials or model calls:

```bash
.venv/bin/python tools/evaluate_ai_docs.py
.venv/bin/python -m unittest discover -s tests
```

Live model comparisons are opt-in and never publish. Name each model explicitly and set a shared request, output-token, and time budget:

```bash
.venv/bin/python tools/evaluate_ai_docs.py --live \
  --provider openai --model MODEL_A --model MODEL_B \
  --max-cases 3 --max-requests 4 --max-output-tokens 1500 \
  --run-timeout 120 --output tools/state/ai-docs-live-evaluation.json
```

The fixture suite measures policy/outcome agreement, evidence/reference gates, and edit protections. Live runs use the same policy and generation helpers, compare named models on synthetic task cases, and record per-model pass counts, calls, and reported usage. They do not measure real-world factual accuracy or replace human review. Recovery, retry, and publishing safety regressions live in `tests/test_ai_docs_execution.py`; evaluation cases live in `tests/fixtures/ai_docs_evaluation.json`.

The manual workflow uploads incremental results even after failure. Dry runs make no issue, label, branch, or PR writes. The publishing job retains the write permissions needed for explicit publishing; source-only local dry runs can use a read-scoped GitHub token and a separate provider key. AI keys are exposed only to the generation step, and the model receives page/source text without credentials or repository tools.

Configure `DOCS_BOT_TOKEN` if you want draft PRs to trigger normal pull request workflows. Without that secret, the workflow uses `GITHUB_TOKEN`, which can push branches and open PRs but may not trigger follow-on PR checks.

Configure `OPENAI_API_KEY` for the default OpenAI provider. The default model is `gpt-5.4-mini`. OpenRouter can still be tested with `provider=openrouter`, and GitHub Models can still be tested with `provider=github-models`, but GitHub Models depends on repository or organization access.

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
