---
tags:
  - P2P
---

# P2P Protocol Overview

The Ergo network protocol uses full nodes (peers) to maintain a collaborative peer-to-peer network for block and transaction exchange.

## Introduction

The [**Full Node**](install.md) downloads and verifies every block (and transaction) before it relays them to other nodes.


## [Handshake](/dev/p2p/p2p-handshake)

Nodes perform send each other `handshake messages.` to establish connections with other peers. 

## [Network Messages](/dev/p2p/network)

## [Modifier Exchange](/dev/p2p/modifiers)

## Syncing


## Misc

- On mainnet P2P uses port `9030` (`9053` for the API)
- For crawling [https://libp2p.io/](https://libp2p.io/)
