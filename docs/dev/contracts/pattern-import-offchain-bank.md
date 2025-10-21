---
title: Import Off-chain Bank (Amitabh)
---

# Import Off-chain Bank (Amitabh)

## Summary

- Problem: Represent balances or events from a traditional/off-chain banking system on Ergo with auditable synchronization and minimized trust.
- When to use: Bridging fiat account states or payment confirmations into on-chain logic for settlement, escrow, or accounting.
- Category: Interoperability
- Status: Planned

## Canonical Code & Tests

- Upstream  
  - References to Amitabh’s work to be collected (designs/prototypes, repos, or forum threads).
- Commit(s)  
  - Add pinned SHAs when a reference implementation is public and stable.

## Security & Correctness Notes

- Assumptions  
  - A trustworthy mechanism exists to attest off-chain bank events (e.g., signed statements, API proofs, or audited batch reports).
  - Clear reconciliation rules exist for conflicts, reversals, and settlement windows.
- Known limitations  
  - Inherent dependency on off-chain attestations and potential reversibility of banking operations.
  - Finality and chargeback windows must be explicitly modeled.
- Test coverage  
  - Include scenarios for normal sync, missing updates, conflicting statements, and dispute resolution.

## Off-chain Integration

- Required flows  
  - Poll or subscribe to bank event source; translate to canonical “import events”.
  - Build transactions that encode imported state (e.g., balances, batch proofs) under a governance/attestation policy.
  - Handle corrections (reversals) via compensating entries with on-chain traceability.
- SDK/API calls  
  - Fleet/AppKit: construct “import” updates; ensure idempotency (same statement not applied twice).
- Data requirements  
  - Registers for batch ids, statement hashes, attestor keys, and reconciliation metadata.

## UI Considerations

- Minimal UI  
  - Show last imported batch, statement hash, and reconciliation status.
- Edge cases  
  - Present dispute workflows; indicate when imported entries are pending finality.

## MCP Usage

- Provide “import bank batch” builder (stub)  
  - Inputs: batch id, statement hash/data, attestation  
  - Output: transaction applying or rejecting the import per policy
- Provide “reconcile/correct” builder  
  - Inputs: reversal/correction entries with references  
  - Output: correction tx with audit trail.

## References

- Forum threads: Add links covering off-chain bank import discussions and Amitabh’s prior work.
- Talks/ErgoHack: Add relevant materials when available.
- Related patterns: [Trustless Bitcoin Relay](pattern-bitcoin-relay.md), [Trustless Peg](pattern-trustless-peg.md)

## See also

- Category: [contracts-interoperability.md](contracts-interoperability.md)  
- [Library index](contracts-library.md)
- [Additional contracts index](contracts.md)

## Contributor Checklist

- [ ] Upstream code link(s)/designs verified (pending)
- [ ] Tests run/green locally (note version) once code exists
- [ ] Example(s) compile/run
- [ ] Off-chain section outlines polling/batch and reconciliation flows
- [ ] UI section identifies minimum viable UX
- [ ] MCP section stubbed
- [x] Cross-linked from category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Consider multi-attestor or auditor models with stakes and slashing for incorrect imports; document economic incentives and dispute timelines.
