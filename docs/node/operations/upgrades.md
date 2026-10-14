---
tags:
  - Deploy
  - Operations
  - Upgrades
  - Rollback
owner: docs
last_reviewed: 2026-10-14
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/application.conf
  - repo: rosen-bridge/operation
    branch: dev
    paths:
      - docs/guard/migrate-database.md
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/application.conf
  - https://github.com/rosen-bridge/operation/tree/dev/docs/guard/migrate-database.md
---

# Upgrades and Rollback

## Before Upgrade

- Read release notes and config changes.
- Back up config, wallet data, and service `.env` files.
- Stop services cleanly before replacing binaries, jars, or Docker images.
- Record current node height, indexed height, app version, and DB image tags.
- For Docker services, pull images before maintenance window where possible.
- When comparing `application.conf` defaults with local overrides, check for renamed network flags such as `allowLocal` in current upstream configs; older notes may still refer to `localOnly`.

## Node Upgrade

1. Stop node cleanly.
2. Back up config and wallet.
3. Replace jar/image/package.
4. Compare `application.conf` defaults with local overrides.
5. Start node and watch `/info`, peer sync, logs, and JVM memory.
6. If `extraIndex = true`, track `/blockchain/indexedHeight`.

## Rollback

- Prefer config rollback first when failure is config-only.
- For binary rollback, stop node cleanly and restore previous binary/image.
- Do not delete data directories unless corruption is confirmed and backups exist.
- If database schema changed, follow service-specific migration/restore instructions rather than downgrading blindly.

## Rosen Guard Database Migration Pattern

Rosen guard source docs include a Docker DB image migration flow:

```shell
docker compose down service
docker compose exec -T db pg_dump -U POSTGRES_USER POSTGRES_DB > dump_guard_db.bak
docker compose down
docker volume rm guard_postgres-data
git pull
docker compose pull
docker compose up -d db
docker compose exec -T db psql -U POSTGRES_USER -d POSTGRES_DB < dump_guard_db.bak
docker compose up -d
```

Verify restore with `\dt` and confirm expected tables such as `block_entity`, `collateral_entity`, `event_trigger_entity`, and `transaction_entity`.

## Reference Client 6.0.8

[v6.0.8](https://github.com/ergoplatform/ergo/releases/tag/v6.0.8) includes durable extra-index recovery and optional mining-time storage-rent collection. After upgrade, watch indexed height and any temporary `503` responses from indexed reads; do not delete the index merely because recovery is pending. Collection stays off unless `ergo.node.storageRentCollection = true`, and also needs `mining = true` and `extraIndex = true`.

Mainnet's `rejectStorageRentTxs = true` is a mempool policy; it does not ban rent claims from blocks. Check inherited network defaults before copying overrides between mainnet and testnet. Keep LevelDB 6.0.x data separate from the RocksDB 6.1.x line; the published v6.1.7 prerelease belongs to the earlier 6.0.7 implementation line.
