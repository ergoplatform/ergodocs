---
title: PiggyTrade
description: Trading application for the Ergo blockchain.
tags:
  - trading
  - DEX
  - ecosystem
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: FlyingPig5/piggy-trade
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/FlyingPig5/piggy-trade
---

# PiggyTrade

[PiggyTrade](https://github.com/FlyingPig5/piggy-trade) is a trading app for the Ergo blockchain.

PiggyTrade is moving from Python toward a Kotlin implementation with sigma-rust JNI bindings, faster loading and caching, and on-chain DEX pool data access. Treat upstream repository state as the source of truth before relying on a specific build, API, or mobile package.

## Position In The Ecosystem

PiggyTrade fits with Ergo's DEX and trading-tool surface rather than as a base protocol component. It may be useful to users looking for trading interfaces and to developers tracking app-level use of sigma-rust bindings.

## Links

- [PiggyTrade repository](https://github.com/FlyingPig5/piggy-trade)
- [DEX overview](../uses/dex.md)
- [P2P trading](p2p-trading.md)
