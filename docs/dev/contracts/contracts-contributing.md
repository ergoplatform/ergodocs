---
title: Contributing — Contracts & Patterns Library
---

# Contributing — Contracts & Patterns Library

## Goal

Standardize how new contract patterns are added so developers can rely on consistent pages, links, and examples.

## What counts as a “pattern”

- A reusable on-chain capability (e.g., rate limit, whitelist transfer, perpetual token).
- Includes canonical code link(s) and tests (preferably upstream to sigmastate-interpreter).
- Optional off-chain/UI references and MCP usage notes.

## Before you start

- Check existing categories in the library: [contracts-library.md](contracts-library.md).
- Pick the right category page (e.g., [contracts-tokens.md](contracts-tokens.md), [contracts-access-control.md](contracts-access-control.md)).
- Use the template: [pattern-template.md](pattern-template.md).
- Filenames must be globally unique (project rule). Use the prefix `pattern-` for pattern pages.

## How to add a new pattern

1) Create the page

- Copy [pattern-template.md](pattern-template.md) → `pattern-your-pattern-name.md`.
- Fill all sections (Status may be WIP if code not merged yet).
- Link upstream PR(s) and/or specific commit SHAs when possible.

2) Update category page

- Add a bullet under the correct category, linking to your new page by filename only.
  - Example: “- My Pattern: [pattern-my-pattern.md](pattern-my-pattern.md)”.

3) Update the library index

- Add your pattern to the Status Matrix section of [contracts-library.md](contracts-library.md) (keep it concise).
- Make sure Category and Status are aligned.

4) Cross-link

- If relevant, add “Related patterns” links within your page (use direct filenames).
- If a tutorial demonstrates the pattern, add a “This tutorial uses: pattern-...” line to the tutorial.
  - Keep changes minimal: just a single sentence near the top or bottom.

5) Tests and examples

- Prefer linking to upstream tests in sigmastate-interpreter.
- If you provide example snippets, keep them short (10–20 lines) and focused on the invariant.
- Avoid pasting large code blocks from upstream; link instead.

6) Off-chain and UI references (optional but appreciated)

- If you know working examples (SDK snippets, dApp code), add them to:
  - [contracts-offchain-references.md](contracts-offchain-references.md) — off-chain repos/snippets.
  - The pattern page’s Off-chain Integration and UI Considerations sections.
- Use concise bullets and direct links to repos/paths.

7) MCP usage (optional)

- If your pattern has a clear MCP composition path, add a stub section describing inputs/outputs.
- If not ready, mark MCP section as N/A with a short note.

## Linking rules (ErgoDocs)

- Use direct filenames for internal links outside of ::cards:: blocks (e.g., [pattern-whitelist-token.md](pattern-whitelist-token.md)).
- Do not use relative paths like ../folder/file.md outside ::cards:: blocks.
- Ensure filenames are globally unique.
- Always include a blank line before bullet lists for proper mkdocs rendering.

## Acceptance checklist (include in your PR description)

- [ ] New pattern page created from [pattern-template.md](pattern-template.md) and fully populated.
- [ ] Category page updated with a bullet link.
- [ ] Status Matrix updated in [contracts-library.md](contracts-library.md) (row added/edited).
- [ ] Upstream PRs/SHAs linked and verified.
- [ ] Off-chain/UI references added when available (optional).
- [ ] MCP section completed or explicitly N/A.
- [ ] Related patterns cross-linked (at least 1 where applicable).
- [ ] Spelling/formatting pass, headings follow template.
- [ ] All links resolve in local mkdocs build (no 404s).

## Maintainers’ review checklist

- [ ] Pattern is scoped and clearly named (capability-oriented).
- [ ] Links are stable (PRs, commits) and minimally sufficient.
- [ ] No large upstream code dumps copied into docs.
- [ ] Page follows template and uses library taxonomy.
- [ ] Category and library index updated.
- [ ] Internal linking rules followed.
- [ ] Blank line precedes every list (mkdocs formatting).

## Sync & maintenance

- Aim for monthly passes to:
  - Update statuses (WIP → Done) once PRs merge.
  - Add pinned SHAs to Canonical Code sections.
  - Backfill off-chain/UI/MCP references contributed by the community.

## Questions / Help wanted

- Open issues with labels:
  - `contracts:pattern` — new/changes to patterns.
  - `contracts:offchain` — off-chain flows/examples needed.
  - `contracts:UI` — UI examples/design notes needed.
  - `contracts:sync-upstream` — status/links sync tasks.

## See also

- Library index: [contracts-library.md](contracts-library.md)
- Off-chain references: [contracts-offchain-references.md](contracts-offchain-references.md)
- MCP examples: [contracts-mcp-examples.md](contracts-mcp-examples.md)
- Legacy index of contracts/examples: [contracts.md](contracts.md)
