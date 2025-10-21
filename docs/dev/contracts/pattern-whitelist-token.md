---
title: Whitelist-only Token Transfers
---

# Whitelist-only Token Transfers

## Summary

- Problem: Restrict token transfers so only addresses on a whitelist can receive or spend the token.
- When to use: Permissioned assets, gated communities, compliance-limited instruments, or staged rollouts with controlled distribution.
- Category: Tokens
- Status: Done

## Canonical Code & Tests

- Upstream  
  - PR: <https://github.com/ergoplatform/sigmastate-interpreter/pull/1080> — Token with whitelisted-only transfers, including tests.
- Commit(s)  
  - Prefer pinned SHAs once merged and stable.

## Security & Correctness Notes

- Assumptions  
  - The whitelist root or set is authoritative and managed by governance or an admin flow.
  - Contract verifies recipient/spender membership against a whitelist commitment (e.g., Merkle root or on-chain set).
- Known limitations  
  - Whitelist updates require on-chain state updates or a governance-controlled box.
  - Off-chain logic must prevent constructing transactions that bypass membership checks (e.g., via intermediary boxes not satisfying constraints).
- Test coverage  
  - Upstream tests validate acceptance for whitelisted recipients and rejection otherwise.

## Off-chain Integration

- Required flows  
  - Keep an index of whitelisted public keys or addresses.
  - When building transactions, prove membership (e.g., Merkle proof) and attach required data (registers or context vars).
- SDK/API calls  
  - Fleet/AppKit: include proof/materials for whitelist membership in transaction building; ensure scripts select correct branch.
- Data requirements  
  - Store whitelist root/parameters in a governance/admin box; propagate root into the contract box for verification.

## UI Considerations

- Minimal UI  
  - Admin view to add/remove addresses and publish updated whitelist commitments.
  - Transfer form should validate recipient membership before allowing submit.
- Edge cases  
  - Handle race between whitelist change and spend attempt; show clear errors on mismatch.
  - Provide visibility into current whitelist version/root.

## MCP Usage

- Expose a “whitelist transfer” builder that:  
  - Inputs: tokenId, recipient, membership proof (if required), current whitelist root.  
  - Output: transaction template enforcing recipient membership.
- Composition  
  - Combine with [Perpetual Token](pattern-perpetual-token.md) to prevent burning while still gating transfer.

## References

- Forum threads: Add specific discussions on permissioned tokens if available.
- Talks/ErgoHack: Add references when collected.
- Related patterns: [Perpetual Token](pattern-perpetual-token.md)

## Contributor Checklist

- [x] Upstream code link(s) verified
- [ ] Tests run/green locally (note version)
- [ ] Example(s) compile/run
- [ ] Off-chain section at least outlines key flows
- [ ] UI section identifies minimum viable UX
- [ ] MCP section filled or explicitly marked N/A
- [x] Cross-linked from relevant category page(s) (pending category creation)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Consider a dual-mode design: admin-controlled whitelist plus emergency pause. Document governance upgrade paths and audit trail for whitelist changes.
