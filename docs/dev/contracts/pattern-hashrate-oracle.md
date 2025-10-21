---
title: Trustless Hashrate Oracle (Hashrate Coin)
---

# Trustless Hashrate Oracle (Hashrate Coin)

## Summary

- Problem: Bring PoW hashrate data on-chain in a trust-minimized way for use in contracts (e.g., hashrate-pegged assets).
- When to use: Tokenizing hashrate exposure, protocol parameters tied to external hashrate, or products referencing mining difficulty.
- Category: Oracles
- Status: WIP

## Canonical Code & Tests

- Upstream  
  - PR: <https://github.com/ergoplatform/sigmastate-interpreter/pull/1085> — Trustless Hashrate Oracle (Hashrate Coin) pattern and tests (work in progress).
- Commit(s)  
  - Add pinned SHAs once merged and stabilized.

## Security & Correctness Notes

- Assumptions  
  - Data is derived from publicly verifiable chain state (e.g., difficulty/headers) or from a verifiable aggregation scheme.
  - Adversaries cannot profitably forge the reported hashrate under the adopted derivation/verification model.
- Known limitations  
  - Windowing/averaging choices affect responsiveness vs. noise resilience.
  - If using off-chain aggregation, must define slashing/penalties for incorrect submissions.
- Test coverage  
  - WIP upstream tests; ensure negative cases (malformed submissions, stale data) are covered before marking stable.

## Off-chain Integration

- Required flows  
  - If pure on-chain derivation: specify extraction from headers/difficulty and validation window.
  - If reporter-based: define commit–reveal/aggregation and dispute windows; index and track reporter sets.
- SDK/API calls  
  - Fleet/AppKit: build submissions with required registers; verify aggregation across inputs before signing.
- Data requirements  
  - Registers for epoch/window metadata, aggregated value, reporter commitments/proofs where applicable.

## UI Considerations

- Minimal UI  
  - Display current hashrate value and window parameters.
  - For reporter flows: show participation status, stake (if any), and submission deadlines.
- Edge cases  
  - Show warnings for stale windows; surface disputes or inconsistent submissions.

## MCP Usage

- Provide an oracle “submit/aggregate” builder (stub)  
  - Inputs: window parameters, reporter data, commitments/reveals.  
  - Output: transaction enforcing acceptance criteria or aggregating a new round.
- Consumer helper  
  - Read latest finalized value and validate within policy bounds.

## References

- [Oracle overview](oracles.md)
- [Oracle Core (operators)](oracle.md)
- [Oracle Pools v2 (EIP-23)](oracles-v2.md)
- Talks/ErgoHack: Add references when collected.
- Related patterns: [pattern-bulletproof-range-proof.md](pattern-bulletproof-range-proof.md)

## See also

- Category: [contracts-oracles.md](contracts-oracles.md)  
- [Library index](contracts-library.md)
- [Additional contracts index](contracts.md)

## Contributor Checklist

- [x] Upstream code link(s) verified (PR 1085)
- [ ] Tests run/green locally (note version)
- [ ] Example(s) compile/run
- [ ] Off-chain section outlines commit–reveal or derivation flows
- [ ] UI section identifies minimum viable UX
- [ ] MCP section stubbed
- [x] Cross-linked from category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Carefully document data derivation assumptions; consider including a brief derivation formula and windowing approach once finalized.
