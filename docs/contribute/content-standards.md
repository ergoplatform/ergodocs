---
tags:
  - contribute
  - documentation
  - content-design
  - style-guide
---

# Content Standards

Use this guide when creating or reviewing Ergo documentation. Good docs should help readers complete a task, understand a concept, or make a decision without needing to search Discord, Telegram, or source code first.

## Reader First

- Start from the reader's goal, not the implementation detail.
- Name the audience when scope matters: user, wallet developer, node operator, miner, exchange, dApp developer, researcher.
- Put prerequisites before steps.
- Put decisions and trade-offs before reference detail.
- Link to deeper material instead of repeating it.

## Page Structure

Most task pages should use this shape:

1. Goal: what the reader will achieve.
2. Prerequisites: accounts, tools, versions, funds, keys, or environment.
3. Steps: ordered actions with expected output.
4. Verification: how to know it worked.
5. Troubleshooting: common failures and fixes.
6. Next steps: related docs.

Most concept pages should use this shape:

1. Summary: one short paragraph.
2. Why it matters.
3. How it works.
4. Examples or diagrams.
5. Limits, risks, and trade-offs.
6. Related docs and source references.

## Writing Style

- Use direct, plain language.
- Prefer active voice.
- Keep paragraphs short.
- Define Ergo-specific terms on first use.
- Use consistent names for products, protocols, wallets, and repositories.
- Avoid unsupported claims such as "fastest", "best", or "secure" without context.
- Avoid time-sensitive wording such as "currently" unless the page includes a version or date.

## Code And Commands

- Mark every code block with a language.
- Show commands as copyable blocks.
- Show expected output when it helps verification.
- Never publish private keys, real seeds, production secrets, or privileged tokens.
- Test commands locally before publishing when practical.

## Navigation And Discoverability

- Add new pages to `mkdocs.yml` unless intentionally archived or linked only from another page.
- Use descriptive titles that match search intent.
- Add tags when a page belongs to an existing topic cluster.
- Link from overview pages to deeper guides.
- Run `python tools/nav_audit.py` after changing navigation.

## Review Checklist

- Page has clear audience and purpose.
- Commands, links, and code examples were checked.
- Prerequisites and verification steps are present for tutorials.
- Related docs are linked.
- New page appears in navigation or has a clear reason to stay unlisted.
- Terminology matches nearby pages.
