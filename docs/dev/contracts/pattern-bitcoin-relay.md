---
title: Trustless Bitcoin Relay
---

# Trustless Bitcoin Relay

## Summary

- Problem: Verify Bitcoin chain events (e.g., transactions/headers) on Ergo to enable cross-chain actions without centralized trust.
- When to use: Bridging BTC value, verifying BTC deposits for mints/redemptions, or reading BTC state in Ergo contracts.
- Category: Interoperability
- Status: Planned

## Canonical Code & Tests

- Upstream  
  - References to research/implementations to be collected (forum threads, prototypes, ErgoHack work).
- Commit(s)  
  - Add pinned SHAs when a reference implementation becomes public and stable.

## Security & Correctness Notes

- Assumptions  
  - Verification uses Bitcoin headers and Merkle proofs, or succinct/light-client proofs, with sufficient finality depth (k confirmations).
  - Reorg handling is explicit; proofs reference a stable checkpoint window.
- Known limitations  
  - Full light-client verification on-chain can be resource intensive; designs may rely on aggregated/verified header sets maintained by an on-chain relay.
- Test coverage  
  - Include positive/negative cases: invalid Merkle proofs, insufficient confirmation depth, stale headers.

## Off-chain Integration

- Required flows  
  - Header ingestion: maintain a rolling set of BTC headers on Ergo-chain (relay boxes), respecting PoW/difficulty rules.
  - Proof verification: given a BTC tx and Merkle path, verify inclusion under a sufficiently confirmed header.
- SDK/API calls  
  - Fleet/AppKit: submit batched header updates; verify tx inclusion and construct mint/redeem transactions.
- Data requirements  
  - Registers store header chain commitments (tips, work), Merkle roots, and confirmation depth parameters.

## UI Considerations

- Minimal UI  
  - Show BTC deposit status, confirmation count, and relay tip height.
- Edge cases  
  - Communicate reorg risk until finality threshold is passed; handle failed relay updates gracefully.

## MCP Usage

- Provide “verify BTC inclusion” and “update headers” builders (stubs)  
  - Inputs: header batch, txid, Merkle path, confirmation threshold  
  - Output: guard/transaction updating relay or accepting a deposit
- Compose with [Trustless Peg](pattern-trustless-peg.md) for BTC↔Ergo asset movement.

## References

- NIPoPoW overview: [nipopows.md](nipopows.md)
- Light clients (NIPoPoW nodes): [nipopow_nodes.md](nipopow_nodes.md)
- Block header structure: [block-header.md](block-header.md)
- Transaction Merkle trees: [tx-merkle.md](tx-merkle.md)
- Block overview: [block.md](block.md)
- Talks/ErgoHack: Add materials when available.
- Related patterns: [pattern-trustless-peg.md](pattern-trustless-peg.md)

## See also

- Category: [contracts-interoperability.md](contracts-interoperability.md)  
- Library index: [contracts-library.md](contracts-library.md)  
- Additional contracts index: [contracts.md](contracts.md)

## Contributor Checklist

- [ ] Upstream code/design links verified (pending)
- [ ] Tests planned/implemented
- [ ] Example flows described (header update, tx verification)
- [ ] Off-chain proof construction documented
- [ ] UI flow outlined
- [ ] MCP stubs added
- [x] Cross-linked from category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Consider checkpointing and fraud/dispute mechanisms for header updates to mitigate malicious batches; document economic incentives.
