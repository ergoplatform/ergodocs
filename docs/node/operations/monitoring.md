---
tags:
  - Deploy
  - Operations
  - Monitoring
  - Alerts
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/api/openapi.yaml
  - repo: rosen-bridge/operation
    branch: dev
    paths:
      - docs/watcher/deploy-docker.md
      - docs/guard/setup.md
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/api/openapi.yaml
  - https://github.com/rosen-bridge/operation/tree/dev/docs/watcher/deploy-docker.md
  - https://github.com/rosen-bridge/operation/tree/dev/docs/guard/setup.md
---

# Monitoring

Monitor sync, index lag, API health, and host resources separately.

## Node Checks

| Signal | Route / source | Alert when |
| --- | --- | --- |
| Node alive | `GET /info` | no response |
| Peer sync | `GET /peers/syncInfo` | stale or no peers |
| Connected peers | `GET /peers/connected` | unexpectedly low |
| Wallet status | `GET /wallet/status` | wallet locked when service expects unlocked |
| Indexed height | `GET /blockchain/indexedHeight` | lag grows while chain tip advances |
| Mempool pressure | `/transactions/poolHistogram`, `/transactions/unconfirmed/transactionIds` | high sustained pool size |

## Host Checks

- disk free on node data, DB, and log volumes
- JVM heap and restart count
- block/index database size growth
- file descriptor and network connection limits
- system clock drift

## Rosen Checks

- watcher UI/API reachable, usually through SSH tunnel or private network
- watcher/guard containers healthy
- PostgreSQL container healthy
- watcher initial heights correct for Ergo and target chain
- guard manual transaction toggles remain disabled except during explicit signing flows
- Discord webhook or external alert configured for production operators

