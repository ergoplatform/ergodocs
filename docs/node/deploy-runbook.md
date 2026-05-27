---
tags:
  - Deploy
  - Operations
  - Node
  - Indexing
  - Watchers
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/application.conf
      - src/main/resources/api/openapi.yaml
  - repo: rosen-bridge/operation
    branch: dev
    paths:
      - docs/watcher/deploy-docker.md
  - repo: ergoplatform/oracle-core
    branch: develop
    paths:
      - docs/how_to_bootstrap.md
  - repo: ergoplatform/explorer-backend
    branch: master
    paths:
      - modules/chain-grabber/src/main/resources/application.conf
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/application.conf
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/api/openapi.yaml
  - https://github.com/rosen-bridge/operation/tree/dev/docs/watcher/deploy-docker.md
  - https://github.com/ergoplatform/oracle-core/tree/develop/docs/how_to_bootstrap.md
  - https://github.com/ergoplatform/explorer-backend/tree/master/modules/chain-grabber/src/main/resources/application.conf
---

# Deployment Runbook

Use this page to choose the right operational setup before following a specific install guide.

## Pick a Profile

| Goal | Profile | Key settings | Follow-up |
| --- | --- | --- | --- |
| Validate the chain with minimum operator work | Pruned full node | `stateType = "utxo"`, UTXO bootstrap or pruning flow | [Pruned full node](pruned-full-node.md) |
| Keep full block history | Archival node | `blocksToKeep = -1` | [Archival node](archival-node.md) |
| Serve dApp/indexer queries from node API | Indexed node | `ergo.node.extraIndex = true` | [Indexed Node API](indexed-node.md) |
| Run Rosen watchers | Watcher host plus Ergo data source | indexed Ergo node recommended for health checks | [Rosen watcher](watcher.md) |
| Run Rosen guards | Guard host plus keygen output | guard API, DB, signing toggles, secrets | [Rosen guard](guard.md) |
| Bootstrap oracle pools | Oracle operator node | funded wallet, API access, `oracle-core` config | [Oracle bootstrap](oracle-bootstrap.md) |
| Build a custom explorer/indexer | Explorer backend stack | node API, PostgreSQL, Redis, chain-grabber | [Blockchain indexing](blockchain-indexing.md) |
| Host a mining pool | Pool stack plus node | stratum/miningcore, payout ops, pool DB | [Mining pool operations](pool-ops.md) |

## Ports and Exposure

| Service | Default | Expose publicly? | Notes |
| --- | --- | --- | --- |
| Node P2P | `9020` | Yes, for reachable public nodes | Set `declaredAddress` or UPnP if peers must dial in. |
| Node REST API | `9052` in default config, commonly proxied as `9053` | No direct public exposure | Keep behind localhost, VPN, SSH tunnel, or HTTPS reverse proxy. |
| Rosen watcher UI/API | `3030` | Prefer private access | Use SSH forwarding for headless servers. |
| PostgreSQL / Redis | deployment-specific | No | Keep bound to private network/container network. |

The reference node config binds REST to `0.0.0.0:9052` in `application.conf`, but operators should override this to localhost unless a reverse proxy or firewall is in place. Protected routes use `api_key` header auth against `scorex.restApi.apiKeyHash`; the plain API key still crosses the connection, so use HTTPS or tunnels when remote.

## Node Configuration Checklist

- Set `ergo.directory` to a stable data volume before first sync.
- Keep `ergo.node.verifyTransactions = true` for normal mainnet operation.
- Use `ergo.node.extraIndex = true` only when you need `/blockchain/...` indexed routes or services that depend on them.
- Keep `scorex.network.maxConnections` sized for the host; default config uses `30`.
- If accepting inbound peers, configure `scorex.network.declaredAddress` or UPnP and open the P2P port.
- Treat `ergo.wallet.seed`, watcher mnemonics, PostgreSQL passwords, and API keys as secrets. Prefer env vars where supported.
- For API users, set `scorex.restApi.apiKeyHash` to a Blake2b256 hash of a new API key; do not leave the example hash.

## Indexed API Checklist

Enable `extraIndex` before relying on these routes:

- `/blockchain/indexedHeight`
- `/blockchain/transaction/byId/{txId}`
- `/blockchain/transaction/byAddress`
- `/blockchain/box/byTokenId/{tokenId}`
- `/blockchain/box/unspent/byAddress`
- `/blockchain/box/byTemplateHash/{hash}`
- `/blockchain/token/byId/{tokenId}`
- `/blockchain/balance`

Watch `indexedHeight` separately from node sync height. A node can be chain-synced while the extra index is still catching up.

## Rosen Watcher Checklist

The Docker deployment flow is:

```shell
git clone https://github.com/rosen-bridge/operation.git
cd operation/watcher
cp env.template .env
touch config/local.yaml
sudo chown -R 3000:3000 logs
docker compose pull
docker compose up -d
```

Minimum configuration pieces:

- `.env`: PostgreSQL password, user, database, and port.
- `local.yaml`: `network`, watcher API key hash, Ergo mnemonic, Ergo node/explorer source, initial height, and per-chain source config.
- `api.apiKeyHash`: generated with `npx @rosen-bridge/cli blake2b-hash YOUR_API_KEY`.
- `ergo.type`: `node` or `explorer`; if using a node, enable `extraIndex` for reliable watcher health fields.
- `initialHeight`: choose a recent height. Changing it after startup does not rewind an existing watcher database; remove volumes if you need a rescan.
- `observation.confirmation`: tune per watched chain. Source docs recommend `9` for Ergo, `1` for Bitcoin, `20` for Ethereum, `25` for Cardano, and `300` for Binance.

Keep mnemonic and API hash in env vars where possible, not directly in shared config snippets.

## Rosen Guard Checklist

- Complete key generation ceremony before running guard service.
- Keep `isManualTxRequestActive` and `isArbitraryOrderRequestActive` set to `false` except during explicit manual flows.
- Put `API_KEY_HASH`, `MNEMONIC`, `TSS_SECRET`, RPC credentials, and webhook URLs in `.env` where supported.
- Back up guard PostgreSQL before Docker image or schema migrations.
- Monitor guard DB, service health, and signing-request queues.

## Oracle Pool Checklist

Oracle pool bootstrap has two phases:

1. Generate and edit config:

```console
oracle-core generate-oracle-config
oracle-core bootstrap --generate-config-template bootstrap.yaml
```

2. Bootstrap and distribute operator material:

```console
oracle-core bootstrap bootstrap.yaml
oracle-core run
```

Plan pool size before minting tokens. For example, a 9-oracle pool with `min_data_points: 5` and `min_votes: 5` keeps consensus above half while leaving room for new operators. Operators need oracle, reward, and ballot tokens plus the generated pool config.

## Explorer / Chain-Grabber Checklist

Explorer backend `chain-grabber` expects:

- node API source under `network.master-nodes`
- PostgreSQL connection under `db.url`, `db.user`, `db.pass`
- Redis cache under `redis-cache.url`
- poll intervals such as `chain-poll-interval = 15s` and `epoch-poll-interval = 60s`
- optional indexes for box registers, script constants, block extensions, ADProofs, and block stats

Run this as an indexer workload, not as a replacement for the node's own validation.
