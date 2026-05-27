---
tags:
  - Deploy
  - Operations
  - Backups
owner: docs
last_reviewed: 2026-05-27
---

# Backups

## Back Up

- node config overrides
- `wallet.dat` and wallet mnemonic/seed material
- Docker `.env` files
- Rosen watcher and guard `local.yaml`
- PostgreSQL dumps for guard, watcher, explorer, and custom indexers
- indexer schema/migration state
- reverse-proxy config and TLS renewal config

## Do Not Treat As Enough

- synced blockchain data alone
- container images alone
- public explorer history
- screenshots of config

## Restore Drill

At least once, restore onto a non-production host:

1. Restore config and secrets.
2. Restore DB dump or volume.
3. Start service on private ports.
4. Check API health.
5. Confirm node/index/watcher heights.
6. Confirm wallet address matches expected operator address.

