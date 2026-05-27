---
tags:
  - Deploy
  - Operations
  - Security
  - Node
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/application.conf
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/application.conf
---

# Node Hardening

Use this checklist for public or semi-public node hosts.

## Network Exposure

- Keep REST API private unless a reverse proxy, VPN, or SSH tunnel protects it.
- Expose P2P only if you want inbound peers. Configure `scorex.network.declaredAddress` or UPnP.
- Do not expose PostgreSQL, Redis, wallet files, or watcher/guard databases.
- Separate public API nodes from wallet-holding nodes when possible.

## Secrets

- Replace default `scorex.restApi.apiKeyHash`; default config uses Blake2b256 hash of `hello`.
- Store wallet seeds, watcher mnemonics, guard mnemonics, DB passwords, and RPC tokens outside shared config snippets.
- Prefer environment variables where Rosen and other Docker deployments support them.
- Back up `wallet.dat`, mnemonics, `.env`, and local config files offline.

## Host Layout

- Put node data under a stable `ergo.directory` on durable storage.
- Keep logs on a partition with rotation.
- Keep DB volumes separate from application code.
- Do not run node, indexer, watcher, and guard as root unless the deployment requires it.

## API Safety

- Use HTTPS for remote API access.
- Add reverse-proxy rate limits before exposing transaction, mempool, wallet, or indexed query routes.
- For browser apps, set CORS narrowly when you know the origin. `corsAllowedOrigin = "*"` is convenient but broad.
- Treat the plain `api_key` header as a secret; TLS or tunnels matter because config stores only the hash.

