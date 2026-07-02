---
title: Ergo Marketplace
description: Early-stage decentralized marketplace design for permissionless trade infrastructure on Ergo.
tags:
  - ecosystem
  - marketplace
  - design
  - prototype
owner: docs
last_reviewed: 2026-07-02
source_repos:
  - repo: decentbob/ergo-marketplace
    branch: main
    paths:
      - README.md
      - VISION.md
      - DESIGN.md
source_of_truth:
  - https://github.com/decentbob/ergo-marketplace
---

# Ergo Marketplace

[Ergo Marketplace](https://github.com/decentbob/ergo-marketplace) is an early-stage design for neutral, permissionless trade infrastructure on Ergo. The public repository is documentation-first: it is meant to attract builders and feedback, not to present a finished product.

## Scope

The repository points readers to two main documents:

- `VISION.md`: project motivation, target users, hard problems, economic model, and launch considerations.
- `DESIGN.md`: technical specification for contract families, escrow state machine, parameter and bond economics, mediator and reputation mechanisms, connective/application layers, risk register, and transaction examples.

## Status

Treat this as design/prototype material. The README explicitly says it is not a finished product, and that AI was used to consolidate notes and find gaps. Do not describe it as live marketplace infrastructure until public code, contracts, audits, or deployed services support that claim.

A June 2026 maintainer update said the design was adjusted toward Ergo development standards: client-library work, type standards instead of registries, escrow-hash enforcement by listing, a formalized state NFT, seller-side distribution enforcement, restructured verification, a moved trust table, and guard pseudocode in an appendix. These are design/spec improvements, not production deployment claims.

## Links

- [Repository](https://github.com/decentbob/ergo-marketplace)
- [P2P Trading](p2p-trading.md)
- [Ergo Auction House](ergo-auctions.md)
