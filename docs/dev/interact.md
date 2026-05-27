---
tags:
  - Interaction
  - RPC
  - Node
  - Explorer
  - API
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
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/application.conf
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/api/openapi.yaml
  - https://github.com/rosen-bridge/operation/tree/dev/docs/watcher/deploy-docker.md
  - https://github.com/ergoplatform/oracle-core/tree/develop/docs/how_to_bootstrap.md
---

# Deploy Ergo Infrastructure

Deploy pages are for operators running infrastructure: nodes, APIs, wallets, indexers, Rosen watchers, oracle pools, and blockchain-indexing services.

Start with the [Deployment Runbook](../node/deploy-runbook.md) if you are choosing a topology or hardening an existing host.

## Operator Paths

| Need | Start here | Why |
| --- | --- | --- |
| Run a validating node | [Node install overview](../node/install.md) | Choose manual, Docker, Raspberry Pi, Android, or source build. |
| Choose archival, pruned, digest, or light mode | [Modes of operation](../node/modes.md) | Pick storage and validation trade-offs before syncing. |
| Harden config and API access | [Node configuration](../node/conf.md) | Set data directory, REST API, P2P, wallet, and network config. |
| Serve indexed API queries | [Indexed Node API](../node/indexed-node.md) | Requires `ergo.node.extraIndex = true`. |
| Use Swagger / OpenAPI | [Swagger overview](../node/swagger.md) | Explore REST endpoints and protected wallet routes. |
| Run Rosen watchers | [Rosen watcher deployment](../eco/rosen/watcher.md) | Docker deployment, `local.yaml`, chain sources, and health checks. |
| Operate oracle pools | [Oracle Core](../dev/oc/oracle.md) and [Oracle bootstrap](../tutorials/oracle-bootstrap.md) | Bootstrap pools, distribute tokens/config, run oracle operators. |
| Build a custom indexer | [Blockchain indexing](../dev/tutorials/blockchain-indexing.md) | Compare explorer API, node API, and custom chain-grabber setups. |

## Public Services vs Owned Infrastructure

Public nodes and explorers are useful for experiments, but production services should run their own node or indexer where possible.

- Public node APIs can disappear, lag, rate-limit, or expose only a subset of routes.
- Wallet, watcher, oracle, and transaction-submission workflows depend on API availability and correct network view.
- Indexed routes under `/blockchain/...` require a node with `extraIndex = true`; not every public node enables this.
- Services that hold secrets should not send wallet API keys, mnemonics, or private operational data to third-party hosts.

Useful public entry points:

- Ergo Explorer: [explorer.ergoplatform.com](https://explorer.ergoplatform.com/)
- Ergo Explorer alternatives: [ergexplorer.com](https://ergexplorer.com/), [sigmaspace.io](https://sigmaspace.io/)
- Public peer list: [api.tokenjay.app/peers/list](http://api.tokenjay.app/peers/list)

## Baseline Hardening

- Keep node REST API private by default. Use localhost, SSH tunnels, VPN, firewall rules, or HTTPS reverse proxy.
- Change the example `apiKeyHash`; it is the hash of `hello` in the default config.
- Put node data, wallet files, PostgreSQL data, and watcher volumes on durable storage.
- Track node sync height and indexed height separately.
- Back up wallet files and mnemonics offline. Do not keep seed phrases in shared config files.
- For Rosen watchers, prefer environment variables for `MNEMONIC`, `API_KEY_HASH`, RPC credentials, and API tokens.
