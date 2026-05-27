---
title: NFT Races
description: CyberPets Racing, an Ergo NFT racing game.
tags:
  - gaming
  - NFTs
  - ecosystem
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: cannonQ/nft-races
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/cannonQ/nft-races
  - https://nft-races.vercel.app/
---

# NFT Races

[NFT Races](https://nft-races.vercel.app/) is the public CyberPets Racing app, a provably fair asynchronous NFT racing game on Ergo.

Players connect a Nautilus wallet, discover CyberPets in their wallet, train creatures, enter races, and compete for leaderboard points and rewards. Race resolution uses deterministic randomness seeded from Ergo block hashes.

## Current Architecture

The repository describes Phase 1 as an alpha where game logic runs server-side and NFT ownership is verified on-chain. Phase 2 is planned to move state and logic on-chain through ErgoScript smart contracts and AVL trees.

The current stack uses:

- Vite and React for the frontend;
- Vercel serverless functions for API routes;
- Supabase/PostgreSQL for storage;
- Ergo Explorer APIs for ownership checks;
- Nautilus through the EIP-12 dApp connector.

## Links

- [NFT Races app](https://nft-races.vercel.app/)
- [NFT Races repository](https://github.com/cannonQ/nft-races)
- [Gaming overview](../uses/gaming.md)
