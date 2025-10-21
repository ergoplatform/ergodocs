---
title: Perpetual Token
---

# Perpetual Token

## Summary

- Problem: Create a token that cannot be burned, ensuring perpetual total supply once issued.
- When to use: Asset classes where destruction is disallowed (e.g., perpetual identity tokens, licenses, governance shares).
- Category: Tokens
- Status: Done

## Canonical Code & Tests

- Upstream  
  - PR: https://github.com/ergoplatform/sigmastate-interpreter/pull/1082 — Adds a perpetual token contract example with tests.
- Commit(s)  
  - Prefer pinned SHAs when available; add here once merged and stable.

## Security & Correctness Notes

- Assumptions  
  - Token-burning paths are excluded by contract logic; spending conditions preserve token amount across state transitions.
  - Issuer and holders cannot accidentally or maliciously reduce supply.
- Known limitations  
  - Contract must be composed with transfer logic carefully (e.g., whitelist or free-transfer patterns) without introducing burn leak paths.
  - Off-chain composition must not construct transactions that implicitly burn via fee or dust handling.
- Test coverage  
  - Upstream tests validate invariants on token amount conservation across spends.

## Off-chain Integration

- Required flows  
  - Construct outputs preserving token amounts across spends; validate sum(inputs.tokens) == sum(outputs.tokens) for the given token id.
  - Index and track the token id and box lineage to ensure conservation across updates.
- SDK/API calls  
  - Fleet/AppKit: build transaction with token preservation checks before signing; assert output aggregates.
- Data requirements  
  - Track token id in registers or metadata if needed for UI labeling; ensure output boxes contain expected token balances.

## UI Considerations

- Minimal UI  
  - Display token as non-burnable; disable burn buttons or warn explicitly.
- Edge cases  
  - Prevent partial-send flows that might inadvertently route tokens into fee-only boxes (token loss); guard with transaction simulation.

## MCP Usage

- MCP composition: Expose a builder that enforces token conservation for the target token id and rejects transactions that reduce total supply.
- Example (stub)  
  - Inputs: tokenId, outputs schema  
  - Output: transaction template guaranteeing conservation

## References

- Forum threads: Add links if referenced historically.
- Talks/ErgoHack: Add materials if available.
- Related patterns: pattern-whitelist-token.md

## Contributor Checklist

- [x] Upstream code link(s) verified
- [ ] Tests run/green locally (note version)
- [ ] Example(s) compile/run
- [ ] Off-chain section at least outlines key flows
- [ ] UI section identifies minimum viable UX
- [ ] MCP section filled or explicitly marked N/A
- [x] Cross-linked from relevant category page(s) (pending category creation)
- [x] Added to status matrix in contracts-library.md (already listed)

## Notes

- This pattern is a conservation invariant; when composing with transfer controls or vaults, ensure no branch allows burn via “missing token output”.
