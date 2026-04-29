---
tags:
  - Degens.World
  - Agentic
  - Tooling
  - Wallet
  - dApp
---

# Degens.World

## Overview

[Degens.World](http://degens.world) is an umbrella for community-built Ergo apps, wallet experiments, agent tooling, and AI/agentic economy work. Public repositories are collected under [Degens-World on GitHub](https://github.com/Degens-World).

## Recent updates

- [Degen Wallet](https://swap.degens.world/download): public testing opened in March 2026. The wallet added dApp integration, direct LP swap, low-fee quick swap, USE mint merged with swap, an active dApps view, Android testing, and iOS TestFlight preparation.
- [Ergo MCP](https://github.com/Degens-World/Ergo-MCP): agentic MCP server with explorer functionality. `v0.2.0` was released in March 2026.
- [Ergo Skills](https://github.com/Degens-World/Ergo-Skills): skills repository intended to give agents project-specific Ergo context such as AppKit, Fleet, and wallet patterns.
- [Ergo Node CLI](https://github.com/Degens-World/Ergo-Node-CLI): command-line tooling for launching or maintaining nodes and for agent tool calls.
- [Agent Army](https://github.com/Degens-World/agent-army): local multi-agent orchestration for splitting tasks, passing memory, and coordinating long-running agent loops.
- [Sovereignty](https://sovereignty.degens.world): public testing of an Ergo-centric agent platform where agents create user-owned wallets and can trade ErgoDEX pairs, create LP positions, mint tokens/NFTs, and interact with Degens apps.
- [Etcha](https://ergo-p2p-options-frontend-web.vercel.app/app/wizard): decentralized P2P options alpha. It supports physical delivery options and cash-settled options using stablecoins such as USE or SigUSD; later contract work focused on cancel-anytime full refunds.
- [Ergo block timestamps](https://ergo-block-timestamps.vercel.app/): block timestamp app and API with hourly polling, GitHub Actions updates, and block/range/week/month/year queries. Source: [ergo-block-timestamps](https://github.com/Degens-World/ergo-block-timestamps).
- [Ergo Emissions](https://ergoemissions.degens.world): mini-dApp for Ergo emission data.
- [AgenticAiHome](https://AgenticAiHome.com): AI agent open economy project on Ergo.
- [AEther](https://github.com/Degens-World/AEther-Litepaper): litepaper released in April 2026. The log also records Ergo/Cosmos/EVM bridge work, wrapping on Ergo mainnet/testnets, external P2P node sync, on-chain commitments, and multi-authority quorum ingestion work.
- Orbis: [orbis.degens.world](https://orbis.degens.world/) opened for testing, with NFT PlotWars and cross-chain work noted.
- Silentium: private AI proxy announced in the April 2026 weekly update.
- WaddleSwap: line-item swaps were made functional in the April 2026 weekly update.
- Incubate UI: UI work started in January 2026; no public URL was provided in the log.
- SIGHUB: repository/browser-style work was reported as shipped in March 2026; no public URL was provided in the log.
- Xergon: private repo work and early node/chat inference testing were reported; no public project URL was provided in the log.

Some of these projects are experimental or in public testing. Treat project-specific UIs and repos as the source of truth for current availability.

## Agent and tooling details

The Degens.World agent work is aimed at giving LLM/agent tooling direct Ergo context rather than relying on generic blockchain knowledge. The MCP server exposes explorer functionality to agents inside development environments, while Ergo Skills is intended to collect project-specific recipes for AppKit, Fleet, wallet connector flows, and related Ergo patterns.

The log also mentions an Ergo Q/A docs interface and a Rust Expert MCP. The Rust Expert MCP was described as a server with live access to Rust language references, compiler errors, RFCs, The Book, the Reference, the Nomicon, and crates.io. No public Ergo Docs integration was provided in the log.

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
- Xergon remained private during the log period, with early inference and node/chat testing mentioned but no public URL.
