---
tags:
  - Deploy
  - Testnet
  - Devnet
  - Operations
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/testnet.conf
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/testnet.conf
---

# Testnet and Devnet Operations

Use testnet for public compatibility testing. Use devnet/private fork when you need controlled mining, custom parameters, or repeatable contract scenarios.

## Choose

| Need | Use |
| --- | --- |
| Test wallet or API integration against public non-mainnet chain | [Testnet](testnet.md) |
| Sync full testnet history | [Testnet full sync](testnet-full.md) |
| Mine blocks for local tests | [CPU mining](cpu-mining.md) |
| Run isolated custom chain | [Fork your own chain](mine-your-own-chain.md) |
| Check config shape | [testnet.conf](testnetconf.md), [devnet.conf](devnetconf.md) |

## Operator Notes

- Keep testnet/devnet data directories separate from mainnet.
- Never reuse production wallet seeds.
- Pin config files in version control for repeatable devnet tests.
- For private chains, document genesis/config changes next to deployment scripts.

