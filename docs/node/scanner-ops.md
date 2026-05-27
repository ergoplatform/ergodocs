---
tags:
  - Deploy
  - Scanner
  - Indexing
  - Node API
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/api/openapi.yaml
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/api/openapi.yaml
---

# Scanner Operations

Node scans are useful for lightweight event tracking when you do not need a full custom indexer.

## When Scans Fit

- track boxes created after scan registration
- monitor one contract template or address pattern
- avoid separate database/indexer for small services
- use wallet/scanner API as operational glue

## When Scans Do Not Fit

- historical backfill before scan registration
- complex joins across addresses, tokens, and registers
- analytics workloads
- high-volume public queries

Use [Indexed Node API](indexed-node.md), [Explorer Stack](explorer-stack.md), or [Custom Indexer](../dev/tutorials/blockchain-indexing/custom-indexer.md) for those cases.

## Core Routes

- `POST /scan/register`
- `POST /scan/deregister`
- `GET /scan/listAll`
- `GET /scan/unspentBoxes/{scanId}`
- `GET /scan/spentBoxes/{scanId}`
- `POST /scan/stopTracking`
- `POST /scan/p2sRule`
- `POST /scan/addBox`
- `GET /wallet/transactionsByScanId/{scanId}`

## Operator Notes

- Register scans before expected events occur.
- Store scan IDs in service config.
- Back up node wallet/scanner state if service depends on it.
- Monitor scan results after node upgrades or rescans.
- Do not expose scan-management routes publicly.

