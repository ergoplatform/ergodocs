---
tags:
  - Machina Finance
  - DEX
  - Grid Trading
  - dApp
  - dApp-InDev
owner: docs
last_reviewed: 2026-10-21
ia_status: directory
source_repos:
  - repo: nautls/machina-finance
    branch: main
    paths:
      - packages/contracts/SPEC.md
      - packages/contracts/src
  - repo: machinafi/sdk
    branch: master
    release_watch: true
    paths:
      - README.md
      - src
source_of_truth:
  - https://github.com/nautls/machina-finance
  - https://github.com/machinafi/sdk
  - https://github.com/machinafi/sdk/releases/tag/0.1.0-alpha.0
---

# Machina Finance

## Overview

Machina Finance is a decentralized exchange (DEX) design under development on Ergo. Its contract source and first public orders SDK are now open source, with the SDK published as a Fleet SDK plugin layer for building grid and limit order transactions. Its distinctive feature is **[grid order contracts](grid_trading.md)**, which are intended to let liquidity providers create configurable trading grids while traders can combine grid, limit, and market-style orders.

## Recent updates

- `May 9`: the public [Machina Finance orders SDK](https://github.com/machinafi/sdk) released [`0.1.0-alpha.0`](https://github.com/machinafi/sdk/releases/tag/0.1.0-alpha.0), adding token-to-token grid-order and ERG-to-token limit-order support.
- The SDK README reports 100% test coverage and lists the supported contract wrappers for token-to-token grid orders, ERG-to-token grid orders, and ERG-to-token limit orders.
- `Jul 2`: dev updates said final grid-contract optimizations had been added and limit-order contracts were in progress.
- `Jan 21`: the `GridOrder` SDK / Fleet plugin module was complete with 100% test coverage, while `LimitOrder` work was still progressing.
- `Jan 28`: a critical input-aggregation bug was fixed and the `E2T` limit contract was finished and ready for review.
- `Mar 4`: all SDK actions were implemented and the contracts moved into audit.

## Goal

The primary objective of Machina Finance is to promote decentralization and facilitate P2P trade. By leveraging the power of blockchain technology and smart contracts, Machina Finance aims to create a DEX that is secure, transparent, and user-friendly.

## Developer Surface

- [Contracts](https://github.com/nautls/machina-finance) are public in the original Machina Finance repository.
- [Orders SDK](https://github.com/machinafi/sdk) provides `GridOrder` and `LimitOrder` helpers for Fleet SDK transaction builders.
- SDK actions cover order creation, fills, and closing order boxes.

## SDK Price and Fill Semantics

Current [SDK source](https://github.com/machinafi/sdk/blob/master/src/grid-order.ts) uses `prices: { bid, ask }` from the owner's perspective: the owner buys at the bid and sells at the ask. Contract R5 stores the taker's buy/sell prices as `[ask, bid]`. Both prices must be positive and `bid <= ask`; do not carry older buy/sell argument conventions into this API without checking the pinned version.

Grid orders reject equal base/quote IDs, negative amounts and ERG as the quote asset. Token-to-token grids require base liquidity so the token positions remain valid. Limit orders currently support ERG/token pairs; token-to-token creation throws. Fill construction validates the remaining owner-box minimum and distinguishes a continuing partial fill from a final payout. The source manifest is `0.1.0-alpha.1`; confirm the package actually installed rather than assuming an older alpha artifact has these changes.

## Features

### Grid Order Contracts

Grid order contracts are a novel feature in the world of DEXs. They allow for a more efficient and effective trading experience by replacing the need for liquidity pools. This feature is currently under development and is expected to bring significant changes to the way DEXs operate.

### Contract Model

The current contract specification defines:

- **Origin Attestation Tokens (OATs)** to identify boxes issued by the MachinaFi protocol.
- **Pair Identifier Tokens (PITs)** to link a pair's settings and execution boxes.
- **Execution boxes** that check trade execution, protocol fees, executor fees, and miner-fee limits.
- **Settings boxes** that hold base/quote asset IDs, maker/taker fee percentages, and per-order fee parameters.
- **Order contracts** for grid, limit, and market-style orders with creator refunds, partial fills where applicable, and context-variable checks for safer batched execution.

## Resources

- [Twitter](https://twitter.com/MachinaFinance)
- [GitHub](https://github.com/nautls/machina-finance)
- [Orders SDK](https://github.com/machinafi/sdk)
