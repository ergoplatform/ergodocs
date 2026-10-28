---
tags:
  - Machina Finance
  - DEX
  - Grid Trading
  - dApp
  - dApp-InDev
owner: docs
last_reviewed: 2026-10-28
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
  - https://github.com/machinafi/sdk/releases/tag/v0.1.0
---

# Machina Finance

## Overview

Machina Finance is a decentralized exchange (DEX) design under development on Ergo. Its contract source and first public orders SDK are now open source, with the SDK published as a Fleet SDK plugin layer for building grid and limit order transactions. Its distinctive feature is **[grid order contracts](grid_trading.md)**, which are intended to let liquidity providers create configurable trading grids while traders can combine grid, limit, and market-style orders.

## Recent updates

- [SDK `v0.1.0`](https://github.com/machinafi/sdk/releases/tag/v0.1.0) replaces the alpha creation API with owner-side bid/ask prices, recompiles the bundled contracts to ErgoTree v1, and adds grid-order performance getters and custom-contract support. An SDK release does not establish that a production DEX or operator service is live.
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

The [`v0.1.0` SDK](https://github.com/machinafi/sdk/blob/v0.1.0/src/grid-order.ts) uses `prices: { bid, ask }` from the owner's perspective: the owner buys at the bid and sells at the ask. `order.price`, `buy()` and `sell()` retain taker-side semantics: an order created with `{ bid: 5n, ask: 10n }` exposes `{ buy: 10n, sell: 5n }`. Both prices must be positive and `bid <= ask`; replace the older creation arguments rather than copying their field names.

Grid orders reject equal base/quote IDs, negative amounts and ERG as the quote asset. Token-to-token grids require base liquidity so the token positions remain valid. Limit orders currently support ERG/token pairs; token-to-token creation throws. Fill construction validates the remaining owner-box minimum and distinguishes a continuing partial fill from a final payout. Pin the installed package version when building integrations.

## SDK Compatibility and Metrics

In `v0.1.0`, all bundled contracts were recompiled from ErgoTree v2 to v1. Their header changes from `1a` to `19`, changing every contract address. The default `GridOrder` and `LimitOrder` wrappers reject boxes using the old v2 trees; upgrading the SDK does not move existing orders. Keep the matching contract/version available when handling older boxes.

New grid orders store `[ask, bid, initialBase, initialQuote]` in R5. The contract preserves this collection when recreating the order but does not validate the declared initial balances. The SDK exposes `initialAmounts`, `delta` (current minus initial), taker-side `volume`, and `realizedProfit` in base units. These are derived from creator-declared data, not independently verified trading history. All four getters return `undefined` when initial balances are absent. With equal bid and ask, `volume` is `undefined` and `realizedProfit` is `0n` when initial balances are present.

`new GridOrder(box, contract?)` and `GridOrder.create(params, contract?)` accept a custom `OrderContract`. The constructor checks that the box matches the supplied contract; creation checks that its E2T/T2T type matches the base asset.

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
