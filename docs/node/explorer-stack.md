---
tags:
  - Deploy
  - Explorer
  - Indexing
  - PostgreSQL
  - Redis
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ergoplatform/explorer-backend
    branch: master
    paths:
      - modules/chain-grabber/src/main/resources/application.conf
source_of_truth:
  - https://github.com/ergoplatform/explorer-backend/tree/master/modules/chain-grabber/src/main/resources/application.conf
---

# Explorer Stack

Explorer-style deployments are indexer stacks, not node replacements. Run a validating node first, then add indexer services, PostgreSQL, Redis, and frontend/API layers as needed.

## Components

| Component | Role |
| --- | --- |
| Ergo node | chain source and validation |
| chain-grabber | polls node, handles chain data, writes DB |
| PostgreSQL | persistent indexed data |
| Redis | cache layer |
| Explorer API / GraphQL | query layer |
| Frontend | user interface |

## Chain-Grabber Config Shape

```conf
chain-poll-interval = 15s
epoch-poll-interval = 60s
write-orphans = true

network {
  master-nodes = ["http://node.example:9053"]
}

indexes {
  box-registers = true
  script-constants = true
  block-extensions = true
  ad-proofs = true
  block-stats = true
}

db.url = "jdbc:postgresql://localhost:5432/explorer"
redis-cache.url = "redis://localhost:6380"
```

## Operator Notes

- Monitor node height, chain-grabber progress, PostgreSQL disk, and Redis availability.
- Plan DB backups before image or schema changes.
- Keep public Explorer API separate from wallet-holding node API.
- For smaller services, consider [Indexed Node API](indexed-node.md) before full explorer stack.
- For custom app-specific indexes, use [Custom Indexer](../dev/tutorials/blockchain-indexing/custom-indexer.md).

## Existing Docs

- [Explorer overview](../dev/stack/explorer.md)
- [Local explorer setup](../dev/stack/explorer/explorer_local.md)
- [GraphQL](../dev/stack/explorer/graphql.md)
- [Blockchain indexing](../dev/tutorials/blockchain-indexing.md)

