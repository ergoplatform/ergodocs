---
title: eBiome
description: Ergo ecosystem analytics, explorer, and forensics dashboard.
tags:
  - ecosystem
  - analytics
  - explorer
  - dashboard
owner: docs
last_reviewed: 2026-07-02
source_of_truth:
  - https://ebiome.cc
  - https://ebiome.cc/explorer
  - https://ebiome.cc/forensics
---

# eBiome

[eBiome](https://ebiome.cc) is an Ergo ecosystem analytics dashboard. The live site describes itself as real-time analytics for the Ergo ecosystem, covering SigmaUSD, Spectrum DEX, Rosen Bridge, mining stats, and related network data.

## What It Covers

The public site includes sections for:

- ecosystem overview;
- explorer search for transactions, addresses, tokens, and blocks;
- global ledger / address views;
- DeFi, lending, and stablecoin dashboards;
- smart-money, rich-list, and forensics views;
- mining and Rosen Bridge dashboards.

The forensics section is heuristic analysis, not deterministic attribution. Treat grouped-address results as probability-based investigative signals rather than facts about ownership or control.

A June 2026 project update described Forensics V2 as a daily-updated view over wallets above `0.5 ERG`, with all historical Ergo transactions analysed, address profiles, bot detection, round-trip transfer checks, cryptographically linked-wallet signals, and common deposit/spend/source/sink clustering. These remain heuristic signals, not proof of real-world identity.

## Status

Treat eBiome as a live external dashboard. No public source repository was verified during this review, so docs should link to the live site rather than describe internal implementation details.

## Links

- [eBiome](https://ebiome.cc)
- [Explorer](https://ebiome.cc/explorer)
- [Forensics](https://ebiome.cc/forensics)
