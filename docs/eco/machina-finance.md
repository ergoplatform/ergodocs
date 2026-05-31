---
tags:
  - Machina Finance
  - DEX
  - Grid Trading
  - dApp
  - dApp-InDev
owner: docs
last_reviewed: '2026-05-30'
ia_status: directory
source_repos:
  - repo: nautls/machina-finance
    branch: main
    paths:
      - packages/contracts/SPEC.md
      - packages/contracts/src
source_of_truth:
  - https://github.com/nautls/machina-finance
---

# Machina Finance

## Overview

Machina Finance is a decentralized exchange (DEX) design under development on Ergo. The public repository currently focuses on contract specifications and source for order execution rather than a production user interface. Its distinctive feature is **[grid order contracts](grid_trading.md)**, which are intended to let liquidity providers create configurable trading grids while traders can combine grid, limit, and market-style orders.

## Recent updates

- `Jan 21`: the `GridOrder` SDK / Fleet plugin module was complete with 100% test coverage, while `LimitOrder` work was still progressing.
- `Jan 28`: a critical input-aggregation bug was fixed and the `E2T` limit contract was finished and ready for review.
- `Mar 4`: all SDK actions were implemented and the contracts moved into audit.

## Goal

The primary objective of Machina Finance is to promote decentralization and facilitate P2P trade. By leveraging the power of blockchain technology and smart contracts, Machina Finance aims to create a DEX that is secure, transparent, and user-friendly.

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
