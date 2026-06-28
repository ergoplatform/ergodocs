---
tags:
  - Node
  - Protocol
  - P2P
  - Validation
  - Processing
  - Modifiers
owner: docs
last_reviewed: 2026-06-27
source_repos:
  - repo: ergoplatform/ergo
    branch: v6.0.3
    paths:
      - src/main/scala/org/ergoplatform/nodeView/mempool/ErgoMemPool.scala
      - src/main/scala/org/ergoplatform/nodeView/mempool/OrderedTxPool.scala
      - src/main/scala/org/ergoplatform/network/ErgoNodeViewSynchronizer.scala
      - ergo-core/src/main/scala/org/ergoplatform/settings/ValidationRules.scala
source_of_truth:
  - https://github.com/ergoplatform/ergo/commit/bc7b948c19c7
  - https://github.com/ergoplatform/ergo/pull/2299
  - https://github.com/ergoplatform/ergo/pull/2302
  - https://github.com/ergoplatform/ergo/pull/2305
  - https://github.com/ergoplatform/ergo/pull/2310
---

# Ergo Node Protocol

## Overview

*(Back to: [Node Overview](install.md))*

The Node Protocol section provides a comprehensive overview of the core operational aspects of the Ergo network. It covers the following key areas:

- **Processing Algorithm**: This section explains the algorithm used for processing Ergo [modifiers](modifiers-processing.md). It is applicable across all [security modes](modes.md) within the Ergo network, ensuring consistent data processing. The reference client also applies consistency checks while removing or invalidating transactions from the mempool, including checks that prevent duplicate IDs, avoid stale state in double-spend detection, and keep invalidated transaction IDs even when a stale registry entry is missing.

- **Validation Rules**: This part outlines the consensus-critical [validation rules](modifiers-validation.md). These rules are mandatory for every [node](install.md) in the Ergo network to maintain network integrity and security. They ensure that all [transactions](transactions.md) and [blocks](block.md) adhere to the established network standards. Extension-section validation includes size, interlink encoding, key-length, and empty-extension checks.

- **P2P Protocol**: The [P2P Protocol](p2p-protocol-overview.md) section delves into the [peer-to-peer](p2p-protocol-overview.md) protocol used in the Ergo network. It provides insights into how nodes communicate and share information, facilitating efficient data exchange within the network. Header synchronization handles missing parent headers explicitly, allowing the node to request the missing parent again and try equal or older peers after repeated failed downloads.

- **SyncInfoV2 continuation headers**: when the node receives a full continuation header inside a sync message, the synchronizer can mark it as received directly instead of creating a synthetic requested state. Normal downloaded modifiers still use the request/delivery tracking path.

- **Peer Management**: The [peer management](peer-management.md) section discusses the strategies nodes in the Ergo network employ to manage their peers. It includes information about peer discovery, connection, and disconnection, providing a clear understanding of how nodes maintain network connectivity.

For transaction authors and indexers, note that the mempool can contain dependent unconfirmed transactions. A transaction may spend a token minted by another unconfirmed transaction, so tooling should not assume every input box already exists in the confirmed UTXO set. Indexers should also avoid assuming that a token's whole minted supply appears in a single output.

By understanding these aspects, you can gain a deeper insight into how the Ergo network operates, ensuring its security and efficiency.
