---
tags:
  - P2P
---

# P2P Protocol Overview

The Ergo network protocol uses full nodes (peers) to maintain a collaborative peer-to-peer network for block and transaction exchange.

## Introduction

The [**Full Node**](install.md) downloads and verifies every block (and transactions) before it relays them to other nodes. 

[Significant improvements](https://github.com/ergoplatform/ergo/pull/1290) have recently been made to the P2P layer under [Layer 0 scaling](layer0.md) efforts. See all open [P2P issues](https://github.com/ergoplatform/ergo/issues?q=p2p+is%3Aopen).



## [Handshake](/dev/p2p/p2p-handshake)

Nodes perform send each other `handshake messages.` to establish connections with other peers. 

## [Network Messages](/dev/p2p/network)

## [Modifier Exchange](/dev/p2p/modifiers)

## Syncing


## Misc

- On mainnet P2P uses port `9030` (`9053` for the API)
- For crawling [https://libp2p.io/](https://libp2p.io/)
