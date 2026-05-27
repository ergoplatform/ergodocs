---
title: Operate Infrastructure
description: Start page for node operators, API providers, indexer operators, Rosen operators, oracle operators, and pool operators.
tags:
  - start
  - deploy
  - operations
owner: docs
last_reviewed: 2026-05-27
---

# Operate Infrastructure

Use this page if you run Ergo services rather than only using wallets or dApps.

## Choose Your Operating Path

| I need to... | Start here | Then go deeper |
| --- | --- | --- |
| Run an Ergo node | [Node Install](install.md) | [Manual Install](manual.md), [Configuration](conf.md) |
| Harden an operator setup | [Deployment Runbook](deploy-runbook.md) | [Hardening](hardening.md), [Backups](backups.md) |
| Expose or use node APIs | [Swagger Overview](swagger.md) | [OpenAPI Reference](openapi.md), [Reverse Proxy](reverse-proxy.md) |
| Monitor services | [Monitoring](monitoring.md) | [Incidents](incidents.md), [Troubleshooting](troubleshooting.md) |
| Operate indexers or explorers | [Explorer Stack](explorer-stack.md) | [Scanner Operations](scanner-ops.md) |
| Run Rosen infrastructure | [Rosen Guard](guard.md) | [Watcher Setup](watcher.md), [Security Model](security-model.md) |
| Run or bootstrap oracles | [Oracle Bootstrap](oracle-bootstrap.md) | [Oracles](oracles.md), [Oracle Pools V2](oracles-v2.md) |
| Mine or operate a pool | [Securing the Network](securing-the-network-miners.md) | [Pool Operations](pool-ops.md) |

## Operator Entry Points

- First install path: [Node Install](install.md).
- Production checklist: [Deployment Runbook](deploy-runbook.md).
- Ongoing operations: [Hardening](hardening.md), [Monitoring](monitoring.md), [Upgrades](upgrades.md), [Backups](backups.md).
- Data access: [Swagger Overview](swagger.md), [Indexed Node API](indexed-node.md), [Blockchain Indexing](blockchain-indexing.md).
- Lightweight relay tooling: [Ergo Proxy](ergo-proxy.md), [Ergo Relay](ergo-relay.md).

## Related Operator References

- Node modes: [Full Node](full-node.md), [Pruned Full Node](pruned-full-node.md), [Light Full Node](light-full-node.md), [Light SPV](light-spv-node.md).
- Configuration: [Configuration Overview](conf.md), [Node Settings](conf-node.md), [Wallet Settings](conf-wallet.md), [API Settings](conf-api.md).
- Network behavior: [Peer Management](peer-management.md), [Synchronisation](synchronisation.md), [Modifiers](modifiers.md).
- Test networks: [Testnet](testnet.md), [CPU Mining on Testnet](cpu-mining.md), [Fork Your Own Chain](mine-your-own-chain.md).

## Standard Operator Checks

- Keep secrets out of config files committed to Git.
- Back up wallets and service state before upgrades.
- Review release notes before node upgrades.
- Restrict API exposure.
- Monitor disk, memory, sync height, peer count, and service logs.
- Test recovery steps before relying on them.
