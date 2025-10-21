---
title: Pattern Template
---

# Pattern Name (concise, capability-focused)

Use this template when adding a new contract pattern. Follow ErgoDocs linking rules: use direct filenames for internal links outside of ::cards:: blocks, and always include a blank line before bullet lists for proper mkdocs rendering.

## Summary

- Problem: What this pattern solves in one or two sentences.
- When to use: Typical scenarios; preconditions.
- Category: One of [Tokens | Access Control | Privacy | Oracles | Proofs | Interoperability | Randomness | Insurance].
- Status: Done | WIP | Planned

## Canonical Code & Tests

- Upstream
  - PR(s): link to sigmastate-interpreter PR(s) with one-line description per PR.
  - Commit(s): pinned SHA links (optional but preferred for stability).
- Local mirror (optional)
  - If vendoring snippets or test vectors locally, state why and how/when it is synced.

## Security & Correctness Notes

- Assumptions: Explicit trust model, invariants, and required on-chain/off-chain checks.
- Known limitations: Edge cases, liveness assumptions, economic risks.
- Test coverage: Brief summary and links to upstream tests; what is covered (positive/negative paths).

## Off-chain Integration

- Required flows: High-level outline of off-chain steps (indexing, state tracking, transaction building).
- SDK/API calls: Pseudocode or references (Fleet/AppKit/ergo-lib, etc.).
- Data requirements: Registers, context variables, additional boxes/inputs.

## UI Considerations

- Minimal UI required: What the end-user must see/do to avoid misuse.
- Edge cases in UX: Error messaging, disabled states, confirmations, admin-only panels if applicable.

## MCP Usage

- How to call/compose via ErgoScript MCP (stubs acceptable).
- Example: Inputs, parameters, and expected outputs.

## References

- Forum threads:
- Talks/ErgoHack:
- Related patterns: Link other pattern filenames directly, e.g., [pattern-whitelist-token.md](pattern-whitelist-token.md)

## See also

- Category page: link the relevant category, e.g., [contracts-tokens.md](contracts-tokens.md)
- [Library index](contracts-library.md)
- [Additional contracts index](contracts.md)

## Contributor Checklist

- [ ] Upstream code link(s) verified
- [ ] Tests run/green locally (note version)
- [ ] Example(s) compile/run
- [ ] Off-chain section at least outlines key flows
- [ ] UI section identifies minimum viable UX
- [ ] MCP section filled or explicitly marked N/A
- [ ] Cross-linked from relevant category page(s)
- [ ] Added to status matrix in [contracts-library.md](contracts-library.md)
- [ ] Blank line precedes every list (mkdocs formatting)

## Notes

- Keep examples minimal and focused on the core invariant(s).
- Prefer linking to upstream code/tests instead of copying large blocks into docs.
