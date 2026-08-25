---
tags:
  - Deploy
  - Operations
  - Monitoring
  - Alerts
owner: docs
last_reviewed: 2026-08-25
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

### Rosen Monitoring Stack

Current Rosen watcher deployment supports separate `logger` and `monitoring` Compose profiles. The logger path uses Alloy and Loki; the metrics path uses Prometheus Agent, Node Exporter, and cAdvisor, with Grafana and Alertmanager in the observability stack.

Use `COMPOSE_PROFILES=logger`, `monitoring`, or `logger,monitoring`. Set `IS_SAME_HOST=true` only when the observability stack shares the watcher host and its external networks already exist. For a remote stack, use `IS_SAME_HOST=false` and set remote-write URLs and basic-auth credentials in the monitoring environment files. Keep those credentials out of source control.

Before starting the optional agents, make the configuration trees readable/traversable and the Prometheus Agent entrypoint executable:

```shell
chmod -R ao+rX ./alloy ./prometheus-agent
chmod o+x ./prometheus-agent/entrypoint.sh
```

Use these symbolic modes rather than fixed numeric permissions; they remain effective under restrictive umasks such as `007`.

cAdvisor filesystem and disk-I/O panels may show no data on cgroup v2 hosts; Rosen's source guide calls out full `container_fs_*` coverage as a cgroup v1 limitation.
