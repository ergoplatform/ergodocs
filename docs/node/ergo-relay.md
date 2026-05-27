---
title: Ergo Relay
description: Minimal Ergo transaction signing and P2P broadcast service.
tags:
  - Node
  - P2P
  - Transactions
  - Rust
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: mwaddip/ergo-relay
    branch: master
    paths:
      - README.md
source_of_truth:
  - https://github.com/mwaddip/ergo-relay
---

# Ergo Relay

[Ergo Relay](https://github.com/mwaddip/ergo-relay) is a small Rust service for signing transactions and broadcasting them directly to the Ergo P2P network. It is designed as a lightweight component for Ergo-based infrastructure that needs signing and broadcast without running a full Ergo node.

## Components

The project ships two binaries:

- `ergo-relay`: HTTP service for transaction signing and P2P broadcast.
- `ergo-peers`: peer discovery helper that writes a peer list for broadcast use.

## API Shape

`ergo-relay` exposes node-compatible endpoints for common transaction flows:

- `POST /wallet/transaction/sign`: signs an unsigned transaction.
- `POST /transactions`: broadcasts a signed transaction.
- `GET /info`: health check.

The signing request follows the Ergo node's `/wallet/transaction/sign` shape, including an unsigned transaction and DLog secrets.

## Safety Notes

Do not expose `ergo-relay` directly to the public internet. It accepts signing material by design, so deploy it behind local-only networking or a narrow trusted service boundary.

## Links

- [Ergo Relay repository](https://github.com/mwaddip/ergo-relay)
