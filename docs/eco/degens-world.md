---
tags:
  - Degens.World
  - Agentic
  - Tooling
  - Wallet
  - dApp
owner: docs
last_reviewed: 2026-05-30
source_repos:
  - repo: Degens-World/Ergo-MCP
    branch: main
    paths:
      - README.md
  - repo: Degens-World/Ergo-Node-CLI
    branch: main
    paths:
      - README.md
  - repo: Degens-World/ergo-block-timestamps
    branch: main
    paths:
      - README.md
  - repo: Degens-World/ai-radio-mcp
    branch: main
    paths:
      - README.md
  - repo: Degens-World/rust-expert-mcp
    branch: main
    paths:
      - README.md
  - repo: Degens-World/agente
    branch: master
    paths:
      - README.md
  - repo: Degens-World/Ergo-Context
    branch: main
    paths:
      - README.md
  - repo: Degens-World/Xergon-Network
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://degens.world/
  - https://github.com/Degens-World/Ergo-MCP
  - https://github.com/Degens-World/Ergo-MCP/releases/tag/v0.2.0
  - https://github.com/Degens-World/Ergo-Node-CLI
  - https://github.com/Degens-World/ergo-block-timestamps
  - https://ergo-block-timestamps.vercel.app/
  - https://github.com/Degens-World/ai-radio-mcp
  - https://github.com/Degens-World/rust-expert-mcp
  - https://github.com/Degens-World/agente
  - https://github.com/Degens-World/Ergo-Context
  - https://github.com/Degens-World/Xergon-Network
  - https://github.com/Danny-Degens/degen-wallet-oracle
  - https://github.com/Danny-Degens/ergo-mempool-radar
---

# Degens.World

## Overview

[Degens.World](http://degens.world) is an umbrella for community-built Ergo apps, wallet experiments, agent tooling, and AI/agentic economy work. Public repositories are collected under [Degens-World on GitHub](https://github.com/Degens-World).

## Recent updates

- [Degen Wallet](https://swap.degens.world/download): public testing opened in March 2026. The wallet added dApp integration, direct LP swap, low-fee quick swap, USE mint merged with swap, an active dApps view, Android testing, and iOS TestFlight preparation.
- [Ergo MCP](https://github.com/Degens-World/Ergo-MCP): agentic MCP server with explorer functionality. [`v0.2.0`](https://github.com/Degens-World/Ergo-MCP/releases/tag/v0.2.0) was released in March 2026.
- [Ergo Skills](https://github.com/Degens-World/Ergo-Skills): skills repository intended to give agents project-specific Ergo context such as AppKit, Fleet, and wallet patterns.
- [Ergo Node CLI](https://github.com/Degens-World/Ergo-Node-CLI): command-line tooling for launching or maintaining nodes and for agent tool calls.
- [Agent Army](https://github.com/Degens-World/agent-army): local multi-agent orchestration for splitting tasks, passing memory, and coordinating long-running agent loops.
- [Agent Heartbeat](https://github.com/Degens-World/agent-heartbeat): experimental agent heartbeat/status tooling.
- [Agente](https://github.com/Degens-World/agente): autonomous Ergo trading-agent framework using Machina Finance plus Claude or local Ollama. It signs and submits through a local Ergo node wallet, sends Telegram notifications, and can open, close, or adjust grid and limit orders.
- [Sovereignty](https://sovereignty.degens.world): public testing of an Ergo-centric agent platform where agents create user-owned wallets and can trade ErgoDEX pairs, create LP positions, mint tokens/NFTs, and interact with Degens apps.
- [Etcha](https://ergo-p2p-options-frontend-web.vercel.app/app/wizard): decentralized P2P options alpha. It supports physical delivery options and cash-settled options using stablecoins such as USE or SigUSD; later contract work focused on cancel-anytime full refunds.
- [Ergo block timestamps](https://ergo-block-timestamps.vercel.app/): block timestamp app and API with source at [ergo-block-timestamps](https://github.com/Degens-World/ergo-block-timestamps). The public app provides block/range/week/month/year timestamp queries.
- [Ergo Emissions](https://ergoemissions.degens.world): mini-dApp for Ergo emission data.
- [Degen Wallet Oracle](https://github.com/Danny-Degens/degen-wallet-oracle) and [Ergo Mempool Radar](https://github.com/Danny-Degens/ergo-mempool-radar): small public JavaScript tools around wallet scoring and mempool visibility.
- [AgenticAiHome](https://AgenticAiHome.com): AI agent open economy project on Ergo.
- [AEther](https://github.com/Degens-World/AEther-Litepaper): litepaper released in April 2026. Current work covers Ergo/Cosmos/EVM bridge design, wrapping on Ergo mainnet/testnets, external P2P node sync, on-chain commitments, and multi-authority quorum ingestion.
- [AI Blockchain Radio](https://github.com/Degens-World/ai-blockchain-radio), [Ergo Fortune Teller](https://github.com/Degens-World/ergo-fortune-teller), and [Hackathon Judge](https://github.com/Degens-World/hackathon-judge): small experimental agent/media/demo repositories from the same public GitHub organization.
- [Ergo New Testnet snapshot](https://github.com/Degens-World/Ergo-New-Testnet-ergo-6.0.1-1-91aa8056-SNAPSHOT): archived-style testnet release artifact for a November 2025 `ergo-6.0.1` snapshot; do not treat it as an official current node release.
- Orbis: [orbis.degens.world](https://orbis.degens.world/) opened for testing, with NFT PlotWars and cross-chain work noted.
- Silentium: private AI proxy announced in the April 2026 weekly update.
- WaddleSwap: line-item swaps were made functional in the April 2026 weekly update.
- Incubate UI: UI work started in January 2026.
- SIGHUB: repository/browser-style work shipped in March 2026.
- [Xergon](https://github.com/Degens-World/Xergon-Network): decentralized Proof-of-Node-Work network for AI compute on Ergo; early work covers node scoring, local database persistence, and GPU-model testing while mining.

Some of these projects are experimental or in public testing. Treat project-specific UIs and repos as the source of truth for current availability.

## Agent and tooling details

The Degens.World agent work is aimed at giving LLM/agent tooling direct Ergo context rather than relying on generic blockchain knowledge. The MCP server exposes explorer functionality to agents inside development environments, while Ergo Skills is intended to collect project-specific recipes for AppKit, Fleet, wallet connector flows, and related Ergo patterns.

Related agent tooling includes an Ergo Q/A docs interface, [Ergo Context](https://github.com/Degens-World/Ergo-Context) for LLM/agent ErgoScript context, [AI Radio MCP](https://github.com/Degens-World/ai-radio-mcp), and [Rust Expert MCP](https://github.com/Degens-World/rust-expert-mcp). Rust Expert MCP is external Rust tooling with live access to Rust language references, compiler errors, RFCs, The Book, the Reference, the Nomicon, and crates.io.

Agente is the trading-agent component in this surface. Its loop fetches ERG price and wallet state, builds context, asks an LLM for a structured decision, executes through the Machina Finance SDK, signs through the configured Ergo node, and reports decisions through Telegram.

## Wallet and dApp flow

Degen Wallet testing focused on Android first, then iOS TestFlight preparation. The wallet work included:

- in-wallet swap flows;
- WebView/dApp browser support;
- ErgoPay-based dApp interactions;
- USE mint merged with swap;
- an active dApps view;
- debugging around CORS, headers, and mobile wallet signing.

## Experimental dApps

- Sovereignty was described as a public-test agent platform where agents can create user-owned wallets, trade ErgoDEX pairs, create LP positions, mint tokens/NFTs, and interact with Degens.World apps.
- Etcha started as P2P options, with pooled liquidity planned later. Contract updates focused on a cancel-anytime, full-refund UX.
- WaddleSwap line-item swaps were functional by the April weekly update.
- Silentium was announced as a private AI proxy.
- Xergon focuses on node/chat inference testing and Proof-of-Node-Work scoring for AI compute.
