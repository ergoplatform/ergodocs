# Rosen Watcher Prerequisites

This page lists the minimum/recommended requirements and pre-setup steps before deploying a Rosen Watcher. It complements the chain-specific guides and troubleshooting.

See also:
- Watcher setup and FAQ: [watcher.md](watcher.md)
- Bitcoin-specific notes: [bitcoin-watcher.md](bitcoin-watcher.md)
- Troubleshooting: [rosen-troubleshooting.md](rosen-troubleshooting.md)
- Security model: [security-model.md](security-model.md)

## Hardware and System Requirements

Minimum (single-network watcher):
- CPU: 2 cores
- RAM: 2 GB
- Storage: 20 GB+ (varies by logs, sqlite/postgres, and local node footprints if co-located)
- Network: Stable broadband; public Internet egress

Recommended (better headroom and multiple networks):
- CPU: 4 cores
- RAM: 4–8 GB
- Storage: 100 GB+ (or separate volumes per service)
- Network: Stable broadband with low packet loss

OS:
- Linux (x86_64) preferred for servers
- Windows 10/11 with WSL2 (Docker Desktop) or native Docker
- macOS (x86_64/ARM). Note: certain ARM environments have compatibility caveats; see [operation issue](https://github.com/rosen-bridge/operation/issues/6)

## Software Prerequisites

- Docker + Docker Compose
  - Docker Desktop (Windows/macOS) or Docker Engine + Compose plugin (Linux)
  - https://docs.docker.com/desktop/
- Git (to clone the operation repository)
- Optional: Node.js 18+ if you plan to use the npx CLI locally (alternatively, run it via Docker one-shot)

Verify versions:
```bash
docker --version
docker compose version
git --version
node --version # optional
```

## Ergo Node (if not using an external indexer)

If you aren't running an explorer, you will need to run an Ergo node with ExtraIndex enabled. This allows the node to store all transactions, boxes, and addresses in an index.

Example configuration:
```conf
ergo {
  node {
    mining = false
    extraIndex = true
    extraCacheSize = 500
  }
}

scorex {
  restApi {
    # IMPORTANT: Use your own apiKeyHash (blake2b of your API key)
    apiKeyHash = "REPLACE_ME_WITH_YOUR_BLAKE2B_HASH"
  }
}
```

Note: The `apiKeyHash` above must not be the placeholder. Generate your own blake2b hash (see below).

## Chain Node Requirements (by network)

- Bitcoin
  - Full node with `txindex=1` (not pruned).
  - If you synced as pruned, restart from scratch with txindex enabled.
  - Snapshot warnings: 3rd-party snapshots may not include txindex=1 indexes.
  - See [bitcoin-watcher.md](bitcoin-watcher.md)

- Cardano
  - A full node and Ogmios/Kupo (or compatible RPC/indexer endpoints) as required by your watcher configuration.
  - Keep components in sync; watcher errors can surface on rollbacks.

- EVM chains (Ethereum, BSC, etc.)
  - Reliable RPC endpoint (self-hosted or provider). Archive/trace not strictly required for all flows but improves robustness.
  - WebSocket support recommended where available.

- Ergo (source/target)
  - Local or remote Ergo node with `extraIndex=true` OR an explorer with required endpoints.

Confirm your `local.yaml`/environment points watchers to the correct endpoints for your chosen network.

## Secure API Key Hash (BLAKE2b)

Watchers use an API key hash to secure action-based APIs (lock/unlock). Generate a blake2b hash of your chosen API key:

Option A (local npx):
```bash
npx @rosen-bridge/cli blake2b-hash YOUR_API_KEY
```

Option B (one-shot Docker):
```bash
docker run -it --rm node:18.16 npx --yes @rosen-bridge/cli blake2b-hash YOUR_API_KEY
```

Use the resulting hash in your configuration (e.g., `apiKeyHash` in node config and watcher env).

## Networking

- Default watcher HTTP port: often `3030` (configurable). Avoid exposing publicly unless required; protect with firewall rules.
- Ensure local chain nodes are reachable from the watcher container network.
- If operating over SSH, you can forward the watcher UI:
```bash
ssh -L 3030:127.0.0.1:3030 user@watcher-server
```

## Environment Files and Minimal Config

Create a `.env` file alongside `docker-compose.yml` (example):
```env
CURRENT_NETWORK=BITCOIN
HTTP_PORT=3030
LOGGER_LEVEL=info

# Example endpoints (adapt for your chain)
BITCOIN_RPC_URL=http://127.0.0.1:8332
BITCOIN_RPC_USER=youruser
BITCOIN_RPC_PASS=yourpass
ERGO_NODE_URL=http://127.0.0.1:9053
ERGO_API_KEY_HASH=YOUR_BLAKE2B_HASH
```

Minimal `local.yaml` snippet (structure varies by version; refer to the `operation/watcher` docs):
```yaml
network: BITCOIN
http:
  port: 3030
ergo:
  nodeUrl: http://127.0.0.1:9053
  apiKeyHash: YOUR_BLAKE2B_HASH
bitcoin:
  rpc:
    url: http://127.0.0.1:8332
    user: youruser
    pass: yourpass
logging:
  level: info
```

## Quick Start

```bash
git clone https://github.com/rosen-bridge/operation.git
cd operation/watcher/

# Generate API key hash
npx @rosen-bridge/cli blake2b-hash YOUR_API_KEY
# or docker run -it --rm node:18.16 npx --yes @rosen-bridge/cli blake2b-hash YOUR_API_KEY

# Prepare .env and local.yaml as per your network
docker compose up -d
```

Then consult:
- Windows: video + guide linked in [watcher.md](watcher.md)
- macOS/Linux: tutorials and known-issues in [watcher.md](watcher.md)

## Security Best Practices

- Use unique API keys and keep hashes private.
- Restrict inbound access to watcher ports; prefer private networks/VPN/SSH tunnels.
- Keep Docker, OS, and node software patched.
- Do not reuse RPC credentials.
- Monitor logs for errors (see [watcher.md](watcher.md) for common docker commands).
- Consider process supervision and external monitoring (e.g., UptimeRobot, Healthchecks.io).

## Maintenance

- Updating:
```bash
docker compose pull
docker compose down
docker compose up -d
```

- Clearing volumes (resync):
```bash
docker compose down --volumes
```

- Database reset (example; adjust service/volume names to your compose):
```bash
docker compose down
docker volume rm watcher_postgres-data
docker compose up -d
```

Refer back to chain-specific pages and the [rosen-troubleshooting.md](rosen-troubleshooting.md) guide for operational incidents.
