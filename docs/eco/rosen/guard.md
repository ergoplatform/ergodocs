---
tags:
  - Rosen Bridge
  - Guard
  - Deploy
  - Operations
owner: docs
last_reviewed: 2026-11-26
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
  - https://github.com/rosen-bridge/guard-service/releases/tag/12.0.0
  - https://github.com/rosen-bridge/guard-service/releases/tag/11.0.2
---

# Rosen Guard Operations

Guards verify watcher-triggered events and coordinate bridge signing. Guard operation is higher risk than watcher operation because guards participate in signing flows and hold more sensitive operational material.

[Guard service 12.0.0](https://github.com/rosen-bridge/guard-service/releases/tag/12.0.0) integrates Handshake, adds commitment initial synchronization and block-cleanup controls, and hardens event synchronization and cross-network response checks. [11.0.2](https://github.com/rosen-bridge/guard-service/releases/tag/11.0.2) fixes nonce reuse in the Ergo multisig package and removes `maxPriorityFeePerGas` verification from EVM transaction-fee validation. These releases establish component support; they do not by themselves prove that a Handshake route is enabled in the public bridge application.

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

If you enable the optional Alloy or Prometheus Agent containers, make their configuration trees and entrypoint executable before startup:

```shell
chmod -R ao+rX ./alloy ./prometheus-agent
chmod o+x ./prometheus-agent/entrypoint.sh
```

Current Rosen deployment docs use symbolic permissions so these commands still work under restrictive operator umasks such as `007`.

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
- `HANDSHAKE_RPC_USERNAME`, `HANDSHAKE_RPC_PASSWORD`, `HANDSHAKE_RPC_API_KEY`
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

## Public Event Status

To publish guard event and transaction status changes to the Rosen application, add:

```yaml
publicStatus:
  baseUrl: https://app.rosen.tech
```

This sends each status change to the configured Rosen application for display on its event details page.

## Firo

Current guard source supports Firo through ElectrumX. The guard configuration needs the generated ECDSA public key, TSS chain code, and derivation path from the key-generation ceremony:

```yaml
firo:
  chainNetwork: electrumx
  electrumx:
    host: YOUR_ELECTRUMX_HOST
    port: 50002
    reconnectDelay: 5
  bankPublicKey: GENERATED_PUBLIC_KEY
  tssChainCode: ''
  derivationPath:
    -
```

`reconnectDelay` is optional. Confirm production key and derivation values with current Rosen ceremony and deployment documentation.

## Handshake

Current guard source supports Handshake through JSON-RPC. Configure the node URL and, when required by the endpoint, username, password, or API key. The corresponding environment variables are `HANDSHAKE_RPC_USERNAME`, `HANDSHAKE_RPC_PASSWORD`, and `HANDSHAKE_RPC_API_KEY`.

```yaml
handshake:
  chainNetwork: rpc
  rpc:
    url: YOUR_HANDSHAKE_NODE_URL
    username: YOUR_RPC_USERNAME
    password: YOUR_RPC_PASSWORD
    apiKey: YOUR_API_KEY
  bankPublicKey: GENERATED_PUBLIC_KEY
  tssChainCode: ''
  derivationPath:
    -
```

See the upstream [Guard setup](https://github.com/rosen-bridge/operation/blob/dev/docs/guard/setup.md#handshake) and [environment references](https://github.com/rosen-bridge/operation/blob/dev/docs/guard/env-references.md).

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
