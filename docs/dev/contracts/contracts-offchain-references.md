---
title: Off-chain & UI References — Contracts Library
---

# Off-chain & UI References — Contracts Library

## Purpose

Collect links to working off-chain code, SDK snippets, and UI implementations that integrate specific contract patterns. Keep entries concise and point directly to repos and paths.

## How to contribute

- Add links under the relevant pattern heading below.
- One line per link: repo/path — short description (what it demonstrates).
- Prefer stable branches/tags; include commit SHAs when helpful.

## Perpetual Token

- Add references here that show token conservation checks in transaction builders (Fleet/AppKit) and wallet/UX safeguards against burns.

## Whitelist-only Token Transfers

- Add examples for Merkle/whitelist membership proof construction and propagation via registers/context vars.
- Admin UI flows for publishing/updating whitelist roots.

## Daily Withdrawal Limit

- Off-chain state read/update (window marker, cumulative amount) before building spend.
- UX showing “remaining allowance” with height/time-based windows.

## Stealth Address

- One-time address derivation helpers (sender side), chain scanning/indexing (recipient side).
- Wallet integrations with view keys and background discovery.

## Trustless Hashrate Oracle (Hashrate Coin)

- Reporter submission tooling (commit–reveal if used), aggregator examples, and consumer contract reads.
- Visualization of window parameters and stale-data warnings.

## Bulletproof Range Proof Verification

- Proof generation/serialization tooling; canonical byte layouts; local pre-verification before broadcast.
- Minimal demo showing confidential-bound checks.

## Schnorr Signature Verification

- Proof construction and serialization; aggregated/multi-party flows; context binding to transactions.
- Example errors and diagnostics for invalid/replayed proofs.

## Insurance — Physical Gold Non-Delivery

- Attestation payload formats, attestor/oracle update flows, and claim/dispute transactions.
- Governance flows for attestor key rotation.

## Import Off-chain Bank (Amitabh)

- Batch polling/ingestion, statement hashing, idempotent imports, and reconciliation/corrections.
- UI for last imported batch and dispute workflows.

## Trustless Peg

- Proof production pipelines (deposit/withdrawal), header/accumulator management, and state updates.
- Handling reorgs and timeouts; UX for confirmation depth.

## Trustless Bitcoin Relay

- Header ingestion batching, Merkle proof verification, and deposit acceptance.
- Relay maintenance tasks; monitoring tooling.

## Randomness from ErgoRaffle

- Commit and reveal transaction builders; seed derivation and winner selection code paths.
- UI for phase timers and auditable randomness display.

## General SDK References

- Fleet SDK: [fleet.md](fleet.md) — JS/TS-based transaction building and utilities.
- AppKit: [appkit.md](appkit.md) — JVM tooling for building and signing transactions.
- Sigma-Rust: [sigma-rust.md](sigma-rust.md) — Rust bindings and constrained environments.

## Indexers & APIs

- Explorer API: [explorer.md](explorer.md) — Query chain data and indexes.
- Blockchain Indexing tutorials: dev/tutorials/blockchain-indexing.md — Patterns for custom data pipelines.

## See also

- Library index: [contracts-library.md](contracts-library.md)
- MCP examples: [contracts-mcp-examples.md](contracts-mcp-examples.md)

## Notes

- For large codebases, link to specific files/paths and optionally pin a commit SHA.
- Keep entries short; detailed explanations belong in the pattern page’s Off-chain Integration.
