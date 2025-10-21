---
title: Bulletproof Range Proof Verification
---

# Bulletproof Range Proof Verification

## Summary

- Problem: Verify that a committed value lies within a specified range without revealing the value, enabling confidential constraints.
- When to use: Ensuring non-negative balances, bounded bids/prices, or supply caps when values should remain hidden.
- Category: Proofs
- Status: WIP

## Canonical Code & Tests

- Upstream  
  - PR: https://github.com/ergoplatform/sigmastate-interpreter/pull/1079 — Adds Bulletproof range proof verification example and tests (work in progress).
- Commit(s)  
  - Add pinned SHAs once merged/stable.

## Security & Correctness Notes

- Assumptions  
  - Bulletproofs provide soundness and zero-knowledge under standard assumptions; verification must cover all generators and relation checks.
  - Generators and curve parameters match what the proof was created for (no mismatched domain parameters).
- Known limitations  
  - Proof size grows logarithmically with range; on-chain verification costs must be budgeted and benchmarked.
  - If proofs are aggregated off-chain, ensure the verification path matches the aggregation scheme.
- Test coverage  
  - Ensure positive verification over valid proofs and negative tests for malformed or boundary-violating proofs.

## Off-chain Integration

- Required flows  
  - Construct commitments and Bulletproofs off-chain; provide proof elements in registers or context variables for on-chain verification.
  - Define canonical encoding for multi-scalar and point vectors to avoid ambiguity.
- SDK/API calls  
  - Fleet/AppKit: serialize proof bytes and attach to transaction; simulate verification locally pre-broadcast if possible.
- Data requirements  
  - Registers carry commitment(s), proof vectors, and range bounds (if not hardcoded).

## UI Considerations

- Minimal UI  
  - Clearly indicate when confidential amounts are used and any bounds enforced.
- Edge cases  
  - Display verification failures with actionable guidance (wrong bound, corrupted encoding, or domain mismatch).

## MCP Usage

- Provide a “verify range proof” helper (stub)  
  - Inputs: commitment(s), proof bytes, bounds  
  - Output: boolean/guard for composition in contract builder
- Composition  
  - Combine with [Stealth Address](pattern-stealth-address.md) or [Whitelist-only Token](pattern-whitelist-token.md) for confidential compliance checks.

## References

- Zero-knowledge proofs (overview): [zkp.md](zkp.md)
- Non-interactive ZK (NIZK): [nizk.md](nizk.md)
- Sigma protocols (foundation): [sigma.md](sigma.md)
- Discrete logarithms (prereq): [dlog.md](dlog.md)
- Talks/ErgoHack: Add references when available.
- Related patterns: [pattern-stealth-address.md](pattern-stealth-address.md), [pattern-whitelist-token.md](pattern-whitelist-token.md)

## See also

- Category: [contracts-proofs.md](contracts-proofs.md)  
- Library index: [contracts-library.md](contracts-library.md)  
- Additional contracts index: [contracts.md](contracts.md)

## Contributor Checklist

- [x] Upstream code link(s) verified (PR 1079)
- [ ] Tests run/green locally (note version)
- [ ] Example(s) compile/run
- [ ] Off-chain section outlines encoding/proof generation
- [ ] UI section identifies minimum viable UX
- [ ] MCP section stubbed
- [x] Cross-linked from category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Include a canonical byte layout for proof elements and commitments to ensure cross-implementation compatibility.
