---
title: Emerging Ecosystem Projects
description: Recent Ergo ecosystem projects and where they fit in ErgoDocs.
tags:
  - ecosystem
  - projects
  - tooling
  - community
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: Scottcjn/bottube
    branch: main
    paths:
      - README.md
      - ergo_bridge_blueprint.py
  - repo: mwaddip/ergots
    branch: master
    paths:
      - README.md
      - packages/ergoscript
  - repo: a-shannon/ergo-agent-sdk
    branch: main
    paths:
      - README.md
  - repo: mwaddip/ergo-proxy
    branch: master
    paths:
      - README.md
      - docs/protocol/ergo-p2p-wire-format.md
  - repo: mwaddip/ergo-relay
    branch: master
    paths:
      - README.md
  - repo: cannonQ/nft-races
    branch: main
    paths:
      - README.md
  - repo: FlyingPig5/piggy-trade
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/Scottcjn/bottube
  - https://www.bottube.ai
  - https://github.com/mwaddip/ergots
  - https://github.com/a-shannon/ergo-agent-sdk
  - https://ergo-agent-sdk.readthedocs.io/
  - https://github.com/mwaddip/ergo-proxy
  - https://github.com/mwaddip/ergo-relay
  - https://github.com/cannonQ/nft-races
  - https://nft-races.vercel.app/
  - https://github.com/FlyingPig5/piggy-trade
---

# Emerging Ecosystem Projects

These projects are recent ecosystem additions verified against public repositories or project sites. Each has a dedicated page; some are early, experimental, or developer-facing, so use the upstream repository or site for current status.

| Dedicated page | What it is | Related surface |
| --- | --- | --- |
| [BoTTube](bottube.md) | AI-native video platform with an Ergo bridge blueprint for deposit verification and P2PK address handling. | Applications and utilities. |
| [ergots](../dev/lib/ergots.md) | Browser-compatible TypeScript tooling for Ergo, including NiPoPoW, AVL+, and ErgoScript work. | Developer libraries. |
| [Ergo Agent SDK](../dev/stack/ergo-agent-sdk.md) | Python SDK for giving autonomous agents controlled access to Ergo and its DeFi ecosystem. | Developer frameworks. |
| [Ergo Proxy](../node/ergo-proxy.md) | Lightweight Ergo P2P relay proxy for forwarding peer messages without holding blockchain state. | Node operations and P2P tooling. |
| [Ergo Relay](../node/ergo-relay.md) | Minimal transaction signing and P2P relay service. | Node operations and transaction broadcast tooling. |
| [NFT Races](nft-races.md) | CyberPets Racing, an Ergo NFT racing game. | NFTs and gaming. |
| [PiggyTrade](piggytrade.md) | Trading app for Ergo. | Finance and trading tools. |

## Covered Elsewhere

These related projects already have a page or a suitable umbrella page:

- [Ergo Rust Node](../node/rust-node.md)
- [Ergo Knowledge Base and Transcripts](ergo-knowledge-base.md)
- [Degens.World](degens-world.md), including Ergo MCP, Ergo Node CLI, and Ergo block timestamps
- [Lithos](lithos.md), including current Lithos client work
- [Rosen Bridge](rosen.md), including guard, watcher, scanner, and health-check tooling
- [Dexy](dexy.md) and [Stablecoins](../uses/stablecoins.md)
- [Braid](../uses/sidechains/braid.md), a Bitcoin and Ergo double merged-mined sidechain research project

## Not Added

Some leads were not included because they were generic infrastructure, duplicate services, non-Ergo-specific, or not verifiable enough from a public source:

- Discord CDN/image proxy links
- Generic repository components such as `scanner`, `health-check`, or `utils` when they are already part of Rosen infrastructure
- Bitcoin parser references and other external tooling without a clear Ergo-facing project page
- Temporary URLs, ngrok links, or private/test endpoints
