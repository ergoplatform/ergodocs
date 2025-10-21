---
title: Stealth Address
---

# Stealth Address

## Summary

- Problem: Enable recipients to receive funds to unlinkable, one-time addresses derived from a public identifier, improving on-chain privacy.
- When to use: Privacy-preserving payments, donations, merchant receipts where recipient identity should not be trivially linkable across payments.
- Category: Privacy
- Status: Done

## Canonical Code & Tests

- Upstream  
  - PR: https://github.com/ergoplatform/sigmastate-interpreter/pull/1084 — Adds a stealth address contract example with tests.
- Commit(s)  
  - Prefer pinned SHAs once available; add here once merged and stable.

## Security & Correctness Notes

- Assumptions  
  - Sender uses recipient’s public view data to derive an unlinkable one-time address (e.g., Diffie-Hellman-style derivation).
  - Recipient can scan the chain to discover outputs addressed to them and reconstruct the spending key.
- Known limitations  
  - Off-chain scanning/indexing is required for recipients to detect incoming payments.
  - Side-channel leakage (timing, value patterns) may still reveal correlations; consider mixing/delayed spends.
- Test coverage  
  - Upstream tests demonstrate correct address derivation and spend authorization.

## Off-chain Integration

- Required flows  
  - Sender: derive one-time address using recipient’s published parameters; construct output to that address.
  - Recipient: background wallet task scans for derivable outputs and indexes spendable boxes.
- SDK/API calls  
  - Fleet/AppKit: helper functions to derive per-payment addresses and to scan/recognize eligible outputs.
- Data requirements  
  - Recipient publishes public parameters (e.g., in a profile or on-chain registry) necessary for derivation.
  - Optionally include “view tags” or lightweight hints to accelerate scanning.

## UI Considerations

- Minimal UI  
  - Recipient settings page to publish/view public stealth parameters.
  - Incoming payments tab that updates as the wallet discovers new outputs.
- Edge cases  
  - Backup/recovery must include stealth scanning keys; warn users about incomplete backups that miss stealth funds.

## MCP Usage

- Expose helpers to:  
  - Derive one-time addresses from recipient parameters and a sender nonce.  
  - Scan chain or indexer results for matches given a recipient’s stealth keys.
- Example (stub)  
  - Inputs: recipient public params, sender randomness  
  - Output: derived ErgoTree/address and metadata for transaction building

## References

- Forum threads: Add historical discussions on stealth payments if available.
- Talks/ErgoHack: Add materials when collected.
- Related patterns: [Bulletproof Range Proof](pattern-bulletproof-range-proof.md), [Whitelist-only Token](pattern-whitelist-token.md)

## See also

- Library index: contracts-library.md  
- Additional contracts index: contracts.md

## Contributor Checklist

- [x] Upstream code link(s) verified
- [ ] Tests run/green locally (note version)
- [ ] Example(s) compile/run
- [ ] Off-chain section at least outlines key flows
- [ ] UI section identifies minimum viable UX
- [ ] MCP section filled or explicitly marked N/A
- [x] Cross-linked from relevant category page(s)
- [x] Added to status matrix in [contracts-library.md](contracts-library.md)

## Notes

- Consider integrating with mixers or delayed-spend policies for stronger privacy; document residual metadata leakage and user guidance.
