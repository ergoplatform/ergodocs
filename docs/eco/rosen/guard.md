---
tags:
  - Rosen Bridge
  - Guard
  - Deploy
  - Operations
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: rosen-bridge/operation
    branch: dev
    paths:
      - docs/guard/setup.md
      - docs/guard/env-references.md
      - docs/guard/migrate-database.md
  - repo: rosen-bridge/utils
    branch: dev
    paths:
      - packages/cli
source_of_truth:
  - https://github.com/rosen-bridge/operation/tree/dev/docs/guard/setup.md
  - https://github.com/rosen-bridge/operation/tree/dev/docs/guard/env-references.md
  - https://github.com/rosen-bridge/operation/tree/dev/docs/guard/migrate-database.md
  - https://github.com/rosen-bridge/utils/tree/dev/packages/cli
---

# Rosen Guard Operations

Guards verify watcher-triggered events and coordinate bridge signing. Guard operation is higher risk than watcher operation because guards participate in signing flows and hold more sensitive operational material.

## Docker Setup Shape

```shell
git clone https://github.com/rosen-bridge/operation.git
cd operation/guard/
cp env.template .env
touch config/thresholds.json
touch config/local.yaml
sudo chown -R 8080:8080 logs config
docker compose pull
docker compose create
```

Before running guard service, participate in Rosen key generation ceremony using the keygen service docs from Rosen.

## Required Environment

```shell
POSTGRES_PASSWORD=
POSTGRES_USER=
POSTGRES_DB=
POSTGRES_PORT=5432
```

Useful optional environment variables include:

- `API_KEY_HASH`
- `MNEMONIC`
- `TSS_SECRET`
- `KOIOS_AUTH_TOKEN`
- `BLOCKFROST_PROJECT_ID`
- `ETHEREUM_RPC_AUTH_TOKEN`
- `BINANCE_RPC_AUTH_TOKEN`
- `DOGE_RPC_USERNAME`, `DOGE_RPC_PASSWORD`, `DOGE_RPC_API_KEY`
- `BITCOIN_RUNES_RPC_USERNAME`, `BITCOIN_RUNES_RPC_PASSWORD`, `BITCOIN_RUNES_RPC_API_KEY`, `BITCOIN_RUNES_UNISAT_API_KEY`
- `DISCORD_WEBHOOK_URL`
- `GUARD_PORT`

Do not add spaces after `=` in `.env`.

## Guard API Safety

Keep these disabled except during explicit manual signing flows:

```yaml
api:
  isManualTxRequestActive: false
  isArbitraryOrderRequestActive: false
```

When manual transaction or arbitrary order requests are needed:

1. Enable the relevant flag.
2. Restart guard.
3. Submit request through guard app.
4. Disable the flag.
5. Restart guard again.

Leaving either flag enabled increases risk from unauthorized access.

## API Key Hash

Generate a salted Blake2b API key hash with Rosen CLI:

```shell
npx @rosen-bridge/cli blake2b-hash YOUR_API_KEY
```

Use `API_KEY_HASH` in `.env` where possible instead of storing `api.apiKeyHash` in `local.yaml`.

## Database Backup / Migration

Before DB image migration or destructive maintenance:

```shell
docker compose down service
docker compose exec -T db pg_dump -U POSTGRES_USER POSTGRES_DB > dump_guard_db.bak
```

After restore, verify expected tables:

```shell
docker compose exec -it db psql -U POSTGRES_USER -d POSTGRES_DB -c "\dt"
```

Expected table set includes `block_entity`, `collateral_entity`, `commitment_entity`, `event_trigger_entity`, `permit_entity`, `transaction_entity`, and `migrations`.

