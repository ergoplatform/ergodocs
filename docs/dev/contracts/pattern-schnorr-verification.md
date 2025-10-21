---
title: Schnorr Signature Verification
---

# Schnorr Signature Verification

## Summary

- Problem: Verify Schnorr signatures or embed Schnorr-style sigma relations within contracts for flexible authorization and cryptographic policies.
- When to use: Custom signature schemes, aggregated signatures, or composing AND/OR conditions around Schnorr proofs within Ergo contracts.
- Category: Proofs
- Status: WIP

## Canonical Code & Tests

- Upstream  
  - PR: (to be published) — Add the canonical link once available.
- Commit(s)  
  - Add pinned SHAs once the upstream PR is merged/stable.

## Security & Correctness Notes

- Assumptions  
  - Sigma protocol soundness under discrete logarithm assumptions; careful handling of challenges and transcripts.
  - Domain separation for challenges if mixing proof systems or contexts.
- Known limitations  
  - Composability: ensure predicates are combined using proper Sigma conjunctions/disjunctions to avoid unintended shortcuts.
  - Replay resistance requires binding proofs to context (e.g., transaction-specific challenges).
- Test coverage  
  - Include positive/negative tests: valid proofs, altered messages, altered public keys, and boundary cases for transcript/challenge derivation.

## Off-chain Integration

- Required flows  
  - Construct Schnorr proofs off-chain using the intended message/context; serialize proof bytes for on-chain verification.
  - For multi-party or aggregated flows, define the aggregation scheme and participant ordering.
- SDK/API calls  
  - Fleet/AppKit: produce proof bytes and attach to input registers or context variables; pre-verify locally before signing/broadcast.
- Data requirements  
  - Registers carry the message digest (if not implicit), public key(s), and Schnorr proof elements.

## UI Considerations

- Minimal UI  
  - If user-facing, label when a non-standard/aggregated signature is in use; provide a verification summary.
- Edge cases  
  - Clear error states for “wrong message/tx binding” vs “invalid proof” to aid debugging.

## MCP Usage

- Provide a “verify Schnorr proof” helper (stub)  
  - Inputs: public key(s), message or context digest, proof bytes  
  - Output: boolean/guard for contract composition
- Composition  
  - Combine with multisig policies or access-control patterns for flexible authorization.

## References

- Forum threads: Add links for Schnorr-focused discussions and designs when collected.
- Talks/ErgoHack: Add references once available.
- Related patterns: [Bulletproof Range Proof](pattern-bulletproof-range-proof.md)

## See also

- Category: [contracts-proofs.md](contracts-proofs.md)  
- Library index: [contracts-library.md](contracts-library.md)  
- Additional contracts index: [contracts.md](contracts.md)

## Contributor Checklist

- [ ] Upstream code link(s) verified (pending PR)
- [ ] Tests run/green locally (note version)
- [ ] Example(s) compile/run
- [ ] Off-chain section outlines serialization and context binding
- [ ] UI section identifies minimum viable UX
- [ ] MCP section stubbed
- [x] Cross-linked from category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Be explicit about how the challenge is derived (e.g., Fiat–Shamir transform over specific domain-tagged transcripts) to avoid cross-protocol confusion.
