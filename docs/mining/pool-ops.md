---
tags:
  - Deploy
  - Mining
  - Pool Operations
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: oliverw/miningcore
    branch: master
    paths:
      - README.md
source_of_truth:
  - https://github.com/oliverw/miningcore/tree/master/README.md
---

# Mining Pool Operations

Mining pool pages live under `Mine`, but pool hosting is operational infrastructure. Use this page as the Deploy entry point.

## Pool Stack

| Layer | Docs |
| --- | --- |
| Node for block candidates | [Solo node configuration](setup/solo-node.md) |
| Pool overview | [Host a pool](setup/pool.md) |
| Stratum server | [Stratum](setup/stratum.md) |
| Miningcore | [MiningCore](setup/miningcore.md) |
| Windows MiningCore | [MiningCore Windows](setup/pool_win.md) |
| Storage rent mining behavior | [Storage rent spending](rent/rent-spending.md) |

## Operator Checklist

- Run and monitor an Ergo node before pool software.
- Keep pool DB backed up.
- Monitor miners, stale shares, block candidate freshness, and payout queues.
- Understand EIP-27 / storage rent behavior if pool constructs payout or rent-related transactions.
- Keep public stratum ports separate from node API and wallet API.

