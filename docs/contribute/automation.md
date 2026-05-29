---
title: Documentation Automation
description: How ErgoDocs uses automated checks, source monitoring, and deployment workflows to keep documentation accurate.
tags:
  - documentation
  - automation
  - workflow
owner: docs
last_reviewed: 2026-05-28
---

# Documentation Automation

ErgoDocs is maintained as a docs-as-code project. Documentation changes are reviewed like software changes: pages live in Git, navigation is validated, links are built by MkDocs, and source-linked pages can be checked against upstream repositories.

Automation does not replace human review. It narrows the review queue, catches structural mistakes, and points maintainers to pages that may need source-backed updates.

## Automation Map

| Area | What it checks | Where to read more |
| --- | --- | --- |
| Local quality checks | MkDocs build, nav coverage, source metadata, structure, whitespace | [Documentation Tools](tools.md) |
| Source tracking | Pages tied to upstream repositories, commits, releases, configs, APIs, contracts, or EIPs | [Source Watch](source-watch.md) |
| Source inventory | Generated overview of watched repositories, branches, paths, and covered pages | [Watched Repositories](source-watch-inventory.md) |
| Review workflow | Repeatable commands for source-backed docs review and weekly maintenance | [Source Watch Playbook](source-watch-playbook.md) |
| Content quality | Page structure, accuracy, verification, and review lifecycle | [Documentation Lifecycle](docs-lifecycle.md) |
| Information architecture | Navigation, orphan pages, duplicate pages, and section design | [Information Architecture](information-architecture.md) |

## Pull Request Checks

Pull requests that touch docs or tooling run the docs quality workflow. The workflow installs dependencies, builds the site, checks navigation, and validates Source Watch metadata.

Before opening a pull request, contributors should run the same checks locally:

```bash
.venv/bin/python tools/source_watch.py scan --strict
.venv/bin/python tools/nav_audit.py --strict
.venv/bin/python tools/structure_audit.py --strict
git diff --check
.venv/bin/mkdocs build --site-dir /tmp/ergodocs-site-check
```

If a page was checked against upstream source behavior, update its `last_reviewed` field. Do not update `last_reviewed` for cosmetic edits alone.

## Source-Linked Review

Some docs pages describe behavior that changes outside this repository, such as node configuration, wallet APIs, smart contract examples, SDKs, bridges, or ecosystem applications. Those pages can declare their upstream sources in frontmatter:

```yaml
owner: docs
last_reviewed: 2026-05-28
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/application.conf
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/application.conf
```

Source Watch uses that metadata to show which docs may need review after upstream changes. It checks commits touching watched paths, GitHub releases from watched repositories, and open pull requests touching watched paths in important repositories. By default, open PR checks are limited to watched repositories under the `ergoplatform` GitHub owner. The report is a triage aid: maintainers still verify each claim against repositories, issues, releases, EIPs, or maintainer sources before changing public docs.

The generated [Watched Repositories](source-watch-inventory.md) page is built from the same metadata. Run `tools/source_watch_inventory.py --write` after changing `source_repos`; CI checks that the page is current.

## Weekly Docs Review

The scheduled `Weekly Docs Review` workflow has two independent inputs:

- Discord discussion leads: it exports the recent general and development chat windows, then generates docs, ecosystem, and GitHub-links reports.
- Watched source changes: it scans every docs page with `source_repos` metadata for upstream GitHub commits, releases, and important open pull requests in the same time window, even if those repositories were not mentioned on Discord that week.

The workflow combines those reports into a weekly review package, then opens GitHub issues only when a docs page may need attention. These issues are leads, not automatic change requests.

Manual runs support three modes:

- `full`: export Discord leads and scan all watched source repos.
- `discord-only`: export Discord leads without running Source Watch.
- `source-only`: scan all watched source repos without exporting Discord.

Each run writes a GitHub Actions summary with candidate counts, skipped pages, created or updated issues, errors, and the tracking issue number. Reports and the per-page issue summary are uploaded as workflow artifacts.

Runs use the shared `docs-source-watch` concurrency group so weekly review and AI draft-PR scans do not run broad Source Watch queries at the same time. The job has a 20-minute timeout to avoid stalled API or export operations running indefinitely.

Maintainers should:

1. Read the linked source or workflow artifact.
2. Decide whether the docs are actually stale.
3. Update the page naturally if needed.
4. Close the issue with a short note if no public docs change is needed.

Discord and chat exports are treated as pointers only. Public documentation should be verified against durable sources before it is changed.

Tracking issues are labelled `docs`, `automated`, and `weekly-review`. Per-page source-review issues are labelled `docs`, `source-watch`, and `automated`, and their titles include the review window.

If every candidate page is already reviewed or low-signal, the workflow comments on the weekly tracking issue and closes it automatically. The tracking issue stays open only when there is an actionable page-review issue, a script error, or follow-up that needs maintainer attention. New weekly runs also close older open weekly tracking issues as superseded.

## AI-Assisted Draft PRs

The manual `AI Docs Draft PRs` workflow can turn Source Watch candidates into draft pull requests. It uses GitHub Models through GitHub Actions, reads the current docs page plus upstream commit context, and asks the model to choose one of three outcomes:

- `no-doc-change`: the existing page already covers the source change.
- `needs-human-review`: the evidence is unclear, sensitive, or too risky for an automated draft.
- `draft-pr-safe`: the source supports a small documentation update.

When a draft is safe enough to propose, the workflow creates a branch and opens a draft pull request. It never merges changes. Every PR is labelled `docs`, `automated`, and `needs-human-review`; protocol, node, contract, ErgoScript, and tutorial pages also receive `sensitive`.

For best results, configure a `DOCS_BOT_TOKEN` repository secret from a bot account or GitHub App with permission to push branches and open pull requests. The workflow falls back to `GITHUB_TOKEN`, but pull requests created with the default Actions token may not trigger follow-on pull request workflows.

Use this workflow as a drafting assistant, not as an authority. Reviewers must verify source links, technical claims, examples, parameters, and page tone before merging.

## Deployment Checks

The main-branch deploy workflow syncs the checked-out repository to the server and builds the site on Linux. This matters because the remote build sees only committed files and uses a case-sensitive filesystem.

If a remote build warns about missing files that build locally:

- Check whether the file is ignored by `.gitignore`.
- Check whether Git tracks the path with different casing.
- Confirm the new page was committed, not just present locally.

See [Source Watch Playbook](source-watch-playbook.md) for the exact diagnostic commands.

## Design Principle

Automation should make documentation safer and easier to maintain without making pages feel generated. Public pages should explain Ergo clearly. Internal tooling details belong in maintainer docs, pull requests, and review notes.
