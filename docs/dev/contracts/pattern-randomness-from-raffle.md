---
title: Randomness from ErgoRaffle
---

# Randomness from ErgoRaffle

## Summary

- Problem: Source on-chain randomness for fair selections (e.g., raffle winners) with minimal bias and verifiable procedures.
- When to use: Lotteries, winner selection, randomized assignments where participants can verify the draw process.
- Category: Randomness
- Status: Planned

## Canonical Code & Tests

- Upstream  
  - References to ErgoRaffle implementations and randomness extraction write-ups to be collected (forum threads, repos, ErgoHack materials).
- Commit(s)  
  - Add pinned SHAs when a reference implementation and tests are public and stable.

## Security & Correctness Notes

- Assumptions  
  - Entropy may be derived from recent block data or commit–reveal contributions; analyze miner/manipulator incentives and feasible biases.
  - If participants contribute entropy, include slashing/timeout rules to prevent withholding attacks.
- Known limitations  
  - Pure block-derived randomness can be miner-influenced; mitigation includes delayed draws, multi-block mixing, or commit–reveal overlays.
- Test coverage  
  - Include tests for winner determinism given fixed entropy; negative tests for malformed commitments or late reveals.

## Off-chain Integration

- Required flows  
  - Commit–reveal: participants commit salt, later reveal; combine with block data for final seed.
  - Raffle: collect entries, lock funds, compute seed at end height, pick winner deterministically.
- SDK/API calls  
  - Fleet/AppKit: construct commit and reveal transactions; at finalization, construct winner-selection transaction with derived index.
- Data requirements  
  - Registers store commitments, reveal salts, draw height, and derived randomness seed or proof data.

## UI Considerations

- Minimal UI  
  - Display commit and reveal phases with timers; show derived randomness and winner visibly/auditably.
- Edge cases  
  - Handle missing reveals via timeouts; show fallback rules; prevent early winner leakage that could bias behavior.

## MCP Usage

- Provide “draw randomness” and “select winner” helpers (stubs)  
  - Inputs: commitments, reveals, block data reference  
  - Output: deterministic seed and selected index/recipient under contract rules

## References

- Forum threads: Add links discussing ErgoRaffle randomness and related draw mechanisms.
- Talks/ErgoHack: Add materials when available.
- Related patterns: [Bulletproof Range Proof](pattern-bulletproof-range-proof.md), [Stealth Address](pattern-stealth-address.md)

## See also

- Category: [contracts-randomness.md](contracts-randomness.md)  
  - Library index: [contracts-library.md](contracts-library.md)  
  - Additional contracts index: [contracts.md](contracts.md)

## Contributor Checklist

- [ ] Upstream code/design links verified (pending)
- [ ] Tests planned/implemented
- [ ] Example flows described (commit–reveal, raffle draw)
- [ ] Off-chain entropy handling documented
- [ ] UI flow outlined
- [ ] MCP stubs added
- [x] Cross-linked from category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Consider layered entropy: commit–reveal + multi-block mixing for stronger bias resistance; document parameters and trade-offs.
