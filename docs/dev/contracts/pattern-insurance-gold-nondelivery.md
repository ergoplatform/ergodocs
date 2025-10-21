---
title: Insurance — Physical Gold Non-Delivery (Digital Twin)
---

# Insurance — Physical Gold Non-Delivery (Digital Twin)

## Summary

- Problem: Provide on-chain insurance that pays out if a seller fails to deliver a promised physical gold item within a defined time/condition set.
- When to use: Commerce where physical delivery risk exists; tokenized “digital twin” representations backed by off-chain assets and delivery SLAs.
- Category: Insurance
- Status: WIP

## Canonical Code & Tests

- Upstream  
  - PR: (to be collected) — Add canonical contract code or prototypes once publicly referenced by Kushti/ErgoHack threads.
- Commit(s)  
  - Add pinned SHAs once a reference implementation is merged and stable.

## Security & Correctness Notes

- Assumptions  
  - Existence of a digital twin token or registry linking on-chain identity to an off-chain gold item and delivery obligation.
  - A verifiable attestation/dispute process determines whether delivery occurred by the deadline.
- Known limitations  
  - Requires an external signal (oracle/attestor/arbitration) to determine non-delivery; trust and incentives must be clearly modeled.
  - Liveness assumptions: claim/dispute windows must be sufficient and enforceable with clear finality.
- Test coverage  
  - Positive payout on verified non-delivery; denied payout when delivery was attested; disputes and timeouts tested.

## Off-chain Integration

- Required flows  
  - Seller lists commitment to deliver, escrow/premium funding, and delivery deadline encoded in contract state.
  - Attestor/oracle submits delivery confirmation or non-delivery attestation within the dispute window.
  - Buyer can initiate claim; contract resolves based on attestation and deadlines.
- SDK/API calls  
  - Fleet/AppKit: build claim and resolution transactions; attach attestations as registers/context vars.
- Data requirements  
  - Registers encode delivery deadline, attestation keys, dispute window parameters, and payout amounts.

## UI Considerations

- Minimal UI  
  - Showcase delivery deadline countdown, claim eligibility, and current attestation status.
- Edge cases  
  - Clear state transitions for “claim filed”, “attested delivered”, “attested non-delivery”, “timeout lapsed”.

## MCP Usage

- Provide an “insurance claim” builder (stub)  
  - Inputs: claim evidence, attestation payloads/keys, current box state.  
  - Output: transaction selecting payout or denial path per policy.
- Admin helper  
  - Rotate/authorize attestor keys via governance if needed.

## References

- Forum threads: Add links to discussions and ErgoHack write-ups once collected.
- Talks/ErgoHack: Add materials when available.
- Related patterns: [Trustless Hashrate Oracle](pattern-hashrate-oracle.md), [Daily Withdrawal Limit](pattern-daily-withdrawal-limit.md)

## See also

- Category: [contracts-insurance.md](contracts-insurance.md)  
- [Library index](contracts-library.md)
- [Additional contracts index](contracts.md)

## Contributor Checklist

- [ ] Upstream code link(s) verified (pending references)
- [ ] Tests run/green locally (note version)
- [ ] Example(s) compile/run
- [ ] Off-chain section outlines attestation and dispute handling
- [ ] UI section identifies minimum viable UX
- [ ] MCP section stubbed
- [x] Cross-linked from category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Consider multi-attestor or staked-attestor designs with slashable behavior to reduce unilateral trust.
