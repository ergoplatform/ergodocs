---
tags:
  - Deploy
  - Operations
  - Upgrades
  - Rollback
owner: docs
last_reviewed: 2026-05-27
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

