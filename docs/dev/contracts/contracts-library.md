---
title: Ergo Contracts & Patterns Library
---

# Ergo Contracts & Patterns Library

A centralized index of canonical ErgoScript contract patterns with upstream code, tests, off-chain notes, UI considerations, and MCP usage.

## Why this exists

Many contract ideas and implementations are scattered across forums, hackathon repos, and PRs. Builders need pattern-level entry points with code-first references and minimal glue to integrate.

## How to use this library

- Pick a category, open a pattern page, review the assumptions and security notes, then follow links to upstream code/tests.
- Off-chain and UI references will be collected progressively; contributions welcome.

## Categories

- [Tokens](contracts-tokens.md)
- [Access Control](contracts-access-control.md)
- [Privacy](contracts-privacy.md)
- [Oracles](contracts-oracles.md)
- [Proofs](contracts-proofs.md)
- [Interoperability](contracts-interoperability.md)
- [Randomness](contracts-randomness.md)
- [Insurance](contracts-insurance.md)

## Status Matrix

| Pattern | Category | Upstream | Status |
| --- | --- | --- | --- |
| [Perpetual Token](pattern-perpetual-token.md) | Tokens | [PR 1082](https://github.com/ergoplatform/sigmastate-interpreter/pull/1082) | Done |
| [Whitelist-only Token](pattern-whitelist-token.md) | Tokens | [PR 1080](https://github.com/ergoplatform/sigmastate-interpreter/pull/1080) | Done |
| [Daily Withdrawal Limit](pattern-daily-withdrawal-limit.md) | Access Control | [PR 1083](https://github.com/ergoplatform/sigmastate-interpreter/pull/1083) | Done |
| [Stealth Address](pattern-stealth-address.md) | Privacy | [PR 1084](https://github.com/ergoplatform/sigmastate-interpreter/pull/1084) | Done |
| [Trustless Hashrate Oracle](pattern-hashrate-oracle.md) | Oracles | [PR 1085](https://github.com/ergoplatform/sigmastate-interpreter/pull/1085) | WIP |
| [Bulletproof Range Proof Verification](pattern-bulletproof-range-proof.md) | Proofs | [PR 1079](https://github.com/ergoplatform/sigmastate-interpreter/pull/1079) | WIP |
| [Schnorr Signature Verification](pattern-schnorr-verification.md) | Proofs | (to be published) | WIP |
| [Insurance: Physical Gold Non-delivery](pattern-insurance-gold-nondelivery.md) | Insurance | (refs pending) | WIP |
| [Import Off-chain Bank (Amitabh)](pattern-import-offchain-bank.md) | Interoperability | (refs pending) | Planned |
| [Trustless Peg](pattern-trustless-peg.md) | Interoperability | (refs pending) | Planned |
| [Trustless Bitcoin Relay](pattern-bitcoin-relay.md) | Interoperability | (refs pending) | Planned |
| [Randomness from ErgoRaffle](pattern-randomness-from-raffle.md) | Randomness | (refs pending) | Planned |

## Quick Links

- [Contributing Guide](contracts-contributing.md)
- [Off-chain & UI References](contracts-offchain-references.md)
- [MCP Examples](contracts-mcp-examples.md)
- [Other contracts index and examples](contracts.md)

## Contributor Guide

- How to add/edit patterns: contracts-contributing.md
- Pattern template: pattern-template.md
- Off-chain/UI reference collection: contracts-offchain-references.md
- MCP usage examples: contracts-mcp-examples.md

## Linking rules (ErgoDocs)

- Use direct filenames for internal links outside of ::cards:: blocks (e.g., contracts-tokens.md).
- Ensure globally unique filenames to avoid ambiguity.
- Within ::cards:: blocks, use relative paths.

## Roadmap (docs sync)

- Create category pages with brief explanations and links to pattern pages.
- Add minimal stubs for each pattern with upstream PR/commit links and placeholders for Off-chain, UI, MCP.
- Backfill references from forum threads and ErgoHack write-ups.
- Add cross-links from tutorials and language pages.
- Add a monthly sync check to update statuses and links.

## Call for contributors

- If you’ve implemented off-chain flows or UI for any pattern, please add links via PR.
- If you have forum threads or research notes, link them in the References section of the relevant pattern page.
- Labels to use in issues: contracts:pattern, contracts:offchain, contracts:UI, contracts:sync-upstream
