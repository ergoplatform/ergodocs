---
title: Ergo Proxy
description: Lightweight Ergo P2P relay proxy.
tags:
  - Node
  - P2P
  - Proxy
  - Rust
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: mwaddip/ergo-proxy
    branch: master
    paths:
      - README.md
      - docs/protocol/ergo-p2p-wire-format.md
source_of_truth:
  - https://github.com/mwaddip/ergo-proxy
---

# Ergo Proxy

[Ergo Proxy](https://github.com/mwaddip/ergo-proxy) is a lightweight P2P relay for the Ergo network. It speaks the Ergo P2P protocol, keeps outbound peer connections, accepts inbound connections, and forwards messages between peers.

It does not store chain state, validate consensus rules, mine, or replace a full node.

## What It Does

- Handles Ergo P2P handshakes, message framing, and peer exchange.
- Tracks `Inv`-based forwarding so requests can be routed to peers that announced the data.
- Supports IPv6 listeners, allowing IPv6-only hosts to bridge into the IPv4 Ergo network.
- Can run listeners in full or light mode.

## Modes

- **Full mode** forwards inventory, modifiers, sync info, and peer exchange. It advertises as a full archival node and can allow inbound peers to sync through the proxy.
- **Light mode** is gossip-oriented. It relays inventory, transaction broadcast, and peer exchange, while advertising as a NiPoPoW-bootstrapped node.

## Operator Notes

Use Ergo Proxy for relay and connectivity experiments, especially around IPv6 and testnet connectivity. Do not treat it as a validating node. Peers connected through it still depend on real nodes for valid chain data.

## Links

- [Ergo Proxy repository](https://github.com/mwaddip/ergo-proxy)
- [P2P wire-format notes](https://github.com/mwaddip/ergo-proxy/blob/master/docs/protocol/ergo-p2p-wire-format.md)
