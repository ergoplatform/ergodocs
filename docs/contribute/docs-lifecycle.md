---
tags:
  - contribute
  - documentation
  - workflow
  - docs-as-code
  - ai
owner: docs
last_reviewed: 2026-05-26
source_repos:
  - repo: glasgowm148/ergodocs
    branch: main
    paths:
      - tools/ai_docs_review_prompt.md
source_of_truth:
  - https://github.com/glasgowm148/ergodocs/tree/main/tools/ai_docs_review_prompt.md
---

# Documentation Lifecycle

Documentation should move with product and protocol changes. Use this workflow for new features, changed behavior, releases, and larger content updates.

## 1. Intake

Capture docs needs as soon as engineering work starts:

- What changed?
- Who is affected?
- What does the reader need to do differently?
- Which pages, examples, screenshots, or API references need updates?
- What source of truth verifies the change?

For engineering changes, link docs work to the issue, pull request, release note, EIP, or repository discussion.

## 2. Draft

Write from tested behavior. Prefer small, reviewable pull requests:

- Add or update the main task page.
- Add concept context only when needed.
- Update navigation and related links.
- Add troubleshooting notes for expected failure modes.
- Include verification steps.

## 3. Technical Review

Ask a subject matter expert to check:

- Technical accuracy.
- Missing edge cases.
- Version or network assumptions.
- Security, privacy, or funds-at-risk warnings.
- Whether examples work as written.

## 4. Content Review

Check the page against [Content Standards](content-standards.md):

- Reader goal is clear.
- Structure fits the page type.
- Terminology is consistent.
- Links and navigation help discovery.
- The page is concise enough to use during a task.

## 5. Publish

Before merge:

```bash
mkdocs build
python tools/nav_audit.py
```

If the page changes navigation, inspect the local site with:

```bash
mkdocs serve
```

## 6. Maintain

Docs need owners after launch:

- Review high-traffic and high-risk pages regularly.
- Update pages when linked repositories, APIs, wallets, or services change.
- Remove stale workarounds after fixes ship.
- Convert repeated support questions into troubleshooting entries.
- Use search and analytics signals to find pages readers cannot discover.
- Use [Source Watch](source-watch.md) metadata on pages tied to source repositories.

## AI-Assisted Drafting

AI can speed up docs work, but human review remains required.

Good uses:

- Summarizing source issues or pull requests into a draft outline.
- Finding stale terms across the docs.
- Suggesting missing prerequisites, warnings, or troubleshooting entries.
- Producing first-pass examples for review.

Use the [AI Docs Review Prompt](https://github.com/glasgowm148/ergodocs/blob/main/tools/ai_docs_review_prompt.md) for a structured first-pass review of pull request diffs.

Do not publish AI output without checking it against source code, command output, release notes, or subject matter review.

AI review checklist:

- Claims trace back to a source.
- Commands were tested or clearly marked as examples.
- No invented flags, endpoints, APIs, versions, or product names.
- No secrets, private data, or copied third-party text were introduced.
