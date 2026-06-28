---
title: ergo-use-x402
description: x402 and ACP payment examples for USE on Ergo using Babel fees.
tags:
  - ecosystem
  - payments
  - stablecoin
  - agentic-commerce
owner: docs
last_reviewed: 2026-06-27
source_repos:
  - repo: cannonQ/ergo-use-x402
    branch: master
    paths:
      - README.md
source_of_truth:
  - https://github.com/cannonQ/ergo-use-x402
  - https://github.com/x402-foundation/x402
  - https://github.com/agentic-commerce-protocol/agentic-commerce-protocol
---

# ergo-use-x402

[ergo-use-x402](https://github.com/cannonQ/ergo-use-x402) is an experimental implementation of x402 payments for Ergo's USE stablecoin. It demonstrates a payer spending USE while holding no ERG: the transaction uses a Babel-fee box so the miner fee is paid in USE and the facilitator verifies and broadcasts without holding a key.

## Scope

The repository includes:

- an x402 `exact` scheme for `ergo:mainnet` and `ergo:testnet`;
- a client package for building USE payments with a wallet/provider abstraction;
- a stateless facilitator with `/verify`, `/settle`, and `/supported` endpoints;
- an Agentic Commerce Protocol merchant package;
- a Hono test resource server;
- a storefront with Nautilus and ErgoPay paths;
- a self-hosted ErgoPay reducer example using AppKit.

The README reports seven confirmed mainnet payment paths across direct client broadcast, facilitator settlement, HTTP 402, ACP checkout, Nautilus storefront, and ErgoPay storefront flows.

## Caveats

- The project is an example implementation, not a ratified Ergo payment standard.
- `ergo:mainnet` is used as a convention between client and facilitator, not a finalized CAIP-2 namespace.
- Mempool acceptance is not finality. The repository recommends confirmed settlement for resources with economic value.
- Babel liquidity is an operational dependency; the USE Babel box needs enough ERG to cover backed payments.

## Links

- [Repository](https://github.com/cannonQ/ergo-use-x402)
- [USE stablecoin](use_stablecoin.md)
- [Babel Fees](babel-fees.md)
