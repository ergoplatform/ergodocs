---
tags:
  - Etcha
  - Options
  - P2P Trading
owner: docs
last_reviewed: 2026-05-29
ia_status: directory
source_repos:
  - repo: cannonQ/ergo-p2p-options-frontend
    branch: master
    paths:
      - README.md
      - packages/core
      - packages/web
source_of_truth:
  - https://github.com/cannonQ/ergo-p2p-options-frontend
  - https://ergo-p2p-options-frontend-web.vercel.app/app/wizard
  - https://ergoforum.aap.cornell.edu/t/decentralized-p2p-options-contracts-on-ergo/3763
---

# Etcha

[Etcha](https://ergo-p2p-options-frontend-web.vercel.app/app/wizard) is an Ergo P2P options interface. It lets users write and trade options on oracle-tracked assets, with on-chain settlement and no intermediary.

The frontend repository describes physical delivery for assets such as rsADA, rsBTC, rsETH, DexyGold, and ERG, plus cash settlement with USE or SigUSD. It uses Fleet SDK transaction builders, a Next.js frontend, and a permissionless bot that watches pending option boxes and handles mint, deliver, and close transactions.

The public app is experimental. Verify contract details, settlement terms, and wallet prompts before signing.

## Links

- [Etcha repository](https://github.com/cannonQ/ergo-p2p-options-frontend)
- [Etcha app](https://ergo-p2p-options-frontend-web.vercel.app/app/wizard)
- [P2P options discussion](https://ergoforum.aap.cornell.edu/t/decentralized-p2p-options-contracts-on-ergo/3763)
