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
ia_status: directory
source_repos:
  - repo: Scottcjn/bottube
    branch: main
    paths:
      - README.md
      - ergo_bridge_blueprint.py
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
  - repo: GitCircles/GitCircles-Github
    branch: main
    paths:
      - README.md
  - repo: GitCircles/GitCircles-Roadmap
    branch: main
    paths:
      - README.md
  - repo: LEEKOHCHING/TabbyPOS-Introduction
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/Scottcjn/bottube
  - https://www.bottube.ai
  - https://github.com/a-shannon/ergo-agent-sdk
  - https://ergo-agent-sdk.readthedocs.io/
  - https://github.com/mwaddip/ergo-proxy
  - https://github.com/mwaddip/ergo-relay
  - https://github.com/cannonQ/nft-races
  - https://nft-races.vercel.app/
  - https://github.com/FlyingPig5/piggy-trade
  - https://github.com/GitCircles/GitCircles-Github
  - https://github.com/GitCircles/GitCircles-Roadmap
  - https://github.com/LEEKOHCHING/TabbyPOS-Introduction
  - https://github.com/moon-miner/SCypher-web
---

# Emerging Ecosystem Projects

These projects are recent ecosystem additions verified against public repositories or project sites. Each has a dedicated page; some are early, experimental, or developer-facing, so use the upstream repository or site for current status.

## How to Read This Page

| Status | Meaning |
| --- | --- |
| Active | Public project or repository has recent visible activity. |
| Emerging | Early project with enough public source material to document, but not necessarily mature. |
| Developer-facing | Useful mainly for builders, operators, or integrators. |
| Experimental | Research, prototype, or hackathon-stage work; do not assume production readiness. |

| Dedicated page | What it is | Status | Related surface |
| --- | --- | --- | --- |
| [BoTTube](bottube.md) | AI-native video platform with an Ergo bridge blueprint for deposit verification and P2PK address handling. | Emerging | Applications and utilities. |
| [Ergo Agent SDK](ergo-agent-sdk.md) | Python SDK for giving autonomous agents controlled access to Ergo and its DeFi ecosystem. | Developer-facing | Developer frameworks. |
| [Ergo Proxy](ergo-proxy.md) | Lightweight Ergo P2P relay proxy for forwarding peer messages without holding blockchain state. | Developer-facing | Node operations and P2P tooling. |
| [Ergo Relay](ergo-relay.md) | Minimal transaction signing and P2P relay service. | Developer-facing | Node operations and transaction broadcast tooling. |
| [NFT Races](nft-races.md) | CyberPets Racing, an Ergo NFT racing game. | Emerging | NFTs and gaming. |
| [PiggyTrade](piggytrade.md) | Trading app for Ergo. | Emerging | Finance and trading tools. |
| [GitCircles](gitcircles.md) | Contribution-reward framework for open-source communities. | Emerging | Funding and contribution tooling. |
| [TabbyPOS](tabbypos.md) | Web3 point-of-sale project for merchant crypto payments. | Emerging | Payments and merchant tooling. |
| [SCypher](scypher.md) | BIP39 seed-cypher tooling with ErgoHack context. | Experimental | Wallet-adjacent security tooling. |

## Covered Elsewhere

These related projects already have a page or a suitable umbrella page:

- [Ergo Rust Node](rust-node.md)
- [Ergo Knowledge Base and Transcripts](ergo-knowledge-base.md)
- [Degens.World](degens-world.md), including Ergo MCP, Ergo Node CLI, and Ergo block timestamps
- [Lithos](lithos.md), including current Lithos client work
- [Rosen Bridge](rosen.md), including guard, watcher, scanner, and health-check tooling
- [Dexy](dexy.md) and [Stablecoins](stablecoins.md)
- [Braid](braid.md), a Bitcoin and Ergo double merged-mined sidechain research project
- [CodeUtxo](codeutxo.md), Aletheia Protocol, FintelligenceAI, and the AI Project Starter Kit are covered in the [AI](ai.md) and [ErgoHack](ergohack.md) pages

## Not Added

Some leads were not included because they were generic infrastructure, duplicate services, non-Ergo-specific, or not verifiable enough from a public source:

- Discord CDN/image proxy links
- Generic repository components such as `scanner`, `health-check`, or `utils` when they are already part of Rosen infrastructure
- Bitcoin parser references and other external tooling without a clear Ergo-facing project page
- Temporary URLs, ngrok links, or private/test endpoints
