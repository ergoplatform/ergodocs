---
tags:
  - Deploy
  - Testnet
  - Devnet
  - Operations
owner: docs
last_reviewed: 2026-10-14
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
| Run several nodes on one private chain (Scala and Rust) | [Fixed-difficulty devnet](devnet60.md) |
| Check config shape | [testnet.conf](testnetconf.md), [devnet.conf](devnetconf.md) |

## Operator Notes

- Keep testnet/devnet data directories separate from mainnet.
- Never reuse production wallet seeds.
- Pin config files in version control for repeatable devnet tests.
- For private chains, document genesis/config changes next to deployment scripts.
- Current `testnet.conf` sets `version2ActivationHeight = 2147483647` and `version2ActivationDifficultyHex = "20"`, effectively disabling the historical protocol-v2/client-4.0 hard fork on public testnet. Do not assume public testnet reproduces that mainnet activation boundary; use a controlled devnet when testing activation behavior.

## Mempool Policy Differences

Current mainnet defaults reject empty-proof storage-rent claims from the mempool (`ergo.node.rejectStorageRentTxs = true`), while public testnet defaults to `false`. Both can still validate rent claims inside blocks. Set this flag explicitly when reproducing admission or relay behavior on a controlled network; network consensus parameters alone do not reproduce mainnet mempool policy.

## Network Regression Testing

[Peeryard](https://github.com/cafebedouin/peeryard) is an experimental Linux network test bench for several real Ergo nodes in separate namespaces. It can inject delay, loss, partitions and crashes, then compare behavior across pinned versions or implementations. Its paired-run measurements cover declared scenarios rather than proving protocol correctness. Keep the topology, seeds, exact node revisions and executed-case evidence with a result. Host namespace setup needs elevated permissions; normal test runs use the prepared unprivileged environment.
