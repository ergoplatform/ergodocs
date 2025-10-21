---
title: Trustless Peg (Cross-Chain)
---

# Trustless Peg (Cross-Chain)

## Summary

- Problem: Enable movement or representation of assets across chains with minimized trust using verifiable proofs and incentive-compatible designs.
- When to use: Bridging assets/value between Ergo and another chain where users need permissionless entry/exit with cryptographic assurances.
- Category: Interoperability
- Status: Planned

## Canonical Code & Tests

- Upstream  
  - References to prior research and prototypes to be collected (forum threads, repos, ErgoHack materials).
- Commit(s)  
  - Add pinned SHAs when a reference implementation is public and stable.

## Security & Correctness Notes

- Assumptions  
  - Verification of the remote chain state is possible (via light-client proofs, NIPoPoW-like constructions, or succinct proofs).
  - Economic incentives and timeouts prevent griefing and encourage correct relaying/finality recognition.
- Known limitations  
  - Full trustlessness may require heavy verification or proof systems; interim federated/threshold variants might be used with clear trade-offs.
- Test coverage  
  - Include deposit, withdrawal, timeout, and dispute paths; test reorg/resubmission behavior where applicable.

## Off-chain Integration

- Required flows  
  - Deposit: lock/mint on origin chain → produce proof → verify and mint/release on destination chain.
  - Withdrawal: burn/lock on destination → produce proof → verify and release on origin.
- SDK/API calls  
  - Fleet/AppKit: assemble transactions that verify incoming proofs and update peg state boxes.
- Data requirements  
  - Registers carry proof bytes, block headers/accumulators, and peg state (supply, pending claims, timeouts).

## UI Considerations

- Minimal UI  
  - Clear status for deposits/withdrawals, confirmation depth, and dispute windows.
- Edge cases  
  - Reorg handling and proof replay; display risk until finality threshold is reached.

## MCP Usage

- Provide peg “verify proof” and “mint/release” builders (stubs)  
  - Inputs: proof bytes, asset mapping, current state  
  - Output: transaction that enforces verification and updates peg state

## References

- [NIPoPoW overview](nipopows.md)
- [Light clients (NIPoPoW nodes)](nipopow_nodes.md)
- [Sidechains overview](sidechains.md)
- [Sigma Chains](sigma-chains.md)
- Talks/ErgoHack: Add materials when available.
- Related patterns: [pattern-bitcoin-relay.md](pattern-bitcoin-relay.md), [pattern-import-offchain-bank.md](pattern-import-offchain-bank.md)

## See also

- Category: [contracts-interoperability.md](contracts-interoperability.md)  
- [Library index](contracts-library.md)
- [Additional contracts index](contracts.md)

## Contributor Checklist

- [ ] Upstream code/design links verified (pending)
- [ ] Tests planned/implemented
- [ ] Example flows described (deposit/withdrawal)
- [ ] Off-chain proof production documented
- [ ] UI flow outlined
- [ ] MCP stubs added
- [x] Cross-linked from category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Prefer proof-based verification over signers; if signers are used, document threshold/federation and slashing economics.
