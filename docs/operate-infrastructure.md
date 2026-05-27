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
| Run an Ergo node | [Node Install](node/install.md) | [Manual Install](node/install/manual.md), [Configuration](node/conf.md) |
| Harden an operator setup | [Deployment Runbook](node/deploy-runbook.md) | [Hardening](node/operations/hardening.md), [Backups](node/operations/backups.md) |
| Expose or use node APIs | [Swagger Overview](node/swagger.md) | [OpenAPI Reference](node/swagger/openapi.md), [Reverse Proxy](node/operations/reverse-proxy.md) |
| Monitor services | [Monitoring](node/operations/monitoring.md) | [Incidents](node/operations/incidents.md), [Troubleshooting](node/install/troubleshooting.md) |
| Operate indexers or explorers | [Explorer Stack](node/explorer-stack.md) | [Scanner Operations](node/scanner-ops.md) |
| Run Rosen infrastructure | [Rosen Guard](eco/rosen/guard.md) | [Watcher Setup](eco/rosen/watcher.md), [Security Model](eco/rosen/security-model.md) |
| Run or bootstrap oracles | [Oracle Bootstrap](tutorials/oracle-bootstrap.md) | [Oracles](uses/oracles.md), [Oracle Pools V2](eco/oracles-v2.md) |
| Mine or operate a pool | [Securing the Network](securing-the-network-miners.md) | [Pool Operations](mining/pool-ops.md) |

## Operator Entry Points

- First install path: [Node Install](node/install.md).
- Production checklist: [Deployment Runbook](node/deploy-runbook.md).
- Ongoing operations: [Hardening](node/operations/hardening.md), [Monitoring](node/operations/monitoring.md), [Upgrades](node/operations/upgrades.md), [Backups](node/operations/backups.md).
- Data access: [Swagger Overview](node/swagger.md), [Indexed Node API](node/indexed-node.md), [Blockchain Indexing](dev/tutorials/blockchain-indexing.md).
- Lightweight relay tooling: [Ergo Proxy](node/ergo-proxy.md), [Ergo Relay](node/ergo-relay.md).

## Standard Operator Checks

- Keep secrets out of config files committed to Git.
- Back up wallets and service state before upgrades.
- Review release notes before node upgrades.
- Restrict API exposure.
- Monitor disk, memory, sync height, peer count, and service logs.
- Test recovery steps before relying on them.
