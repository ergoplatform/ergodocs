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

Source Watch uses that metadata to show which docs may need review after upstream changes. The report is a triage aid: maintainers still verify each claim against repositories, issues, releases, EIPs, or maintainer sources before changing public docs.

## Weekly Review Leads

The scheduled review workflow collects recent project discussion and watched-source changes, then opens GitHub issues when a docs page may need attention. These issues are leads, not automatic change requests.

Maintainers should:

1. Read the linked source or workflow artifact.
2. Decide whether the docs are actually stale.
3. Update the page naturally if needed.
4. Close the issue with a short note if no public docs change is needed.

Discord and chat exports are treated as pointers only. Public documentation should be verified against durable sources before it is changed.

## Deployment Checks

The main-branch deploy workflow syncs the checked-out repository to the server and builds the site on Linux. This matters because the remote build sees only committed files and uses a case-sensitive filesystem.

If a remote build warns about missing files that build locally:

- Check whether the file is ignored by `.gitignore`.
- Check whether Git tracks the path with different casing.
- Confirm the new page was committed, not just present locally.

See [Source Watch Playbook](source-watch-playbook.md) for the exact diagnostic commands.

## Design Principle

Automation should make documentation safer and easier to maintain without making pages feel generated. Public pages should explain Ergo clearly. Internal tooling details belong in maintainer docs, pull requests, and review notes.
