---
tags:
  - Indexing
  - Node API
  - REST API
  - Off-Chain
---

# Indexing Strategy: Querying Node API Directly

Another approach to accessing blockchain data is to run your own Ergo node and query its [REST API](swagger.md) directly from your application.

## Concept

Instead of relying on a third-party explorer, your application communicates directly with an Ergo node instance that you control. This node maintains a copy of the blockchain (either full or pruned) and exposes endpoints to retrieve block, transaction, and state information.

## How It Works

1.  **Run an Ergo Node:** Set up and synchronize an Ergo node. You'll need to decide on the appropriate [mode](modes.md) (Archival Full, Pruned Full) based on whether you need full historical data or just recent state.
2.  **Configure API:** Ensure the node's API is enabled and accessible to your application (configure `scorex.restApi.bindAddress` and potentially `apiKeyHash` for security in `ergo.conf`).
3.  **Make API Requests:** Your application sends HTTP requests to your node's API endpoints (e.g., `/blocks/{headerId}`, `/transactions/unconfirmed`, `/blockchain/box/byId/{boxId}`).
4.  **Process Response:** Your application parses the raw JSON data returned by the node and extracts the necessary information.

## Pros

*   **Control & Trust:** You control the data source and don't rely on third parties.
*   **No Rate Limits:** You are only limited by the performance capabilities of your node and server hardware.
*   **Direct Access:** Provides access to raw, unfiltered block and transaction data as seen by the node.
*   **Real-time (Near):** Access to data is typically limited only by block propagation time.

## Cons

*   **Infrastructure Overhead:** Requires setting up, synchronizing, and maintaining an Ergo node, which consumes significant disk space, bandwidth, and computational resources.
*   **Query Performance:** The node API is designed for retrieving specific blocks or transactions, not for complex, application-level queries across the entire chain history (e.g., "find all boxes ever created by address X"). Such queries can be very slow or impractical via the direct API.
*   **Application Logic Complexity:** Your application needs significant logic to parse the raw API responses, track UTXOs, calculate balances, and manage application-specific state.
*   **Node Sync Requirement:** The node must be fully synchronized to provide complete and current data.

## When to Use

*   Applications that primarily need access to the latest chain state or specific recent blocks/transactions.
*   Simpler queries that don't require scanning large portions of the blockchain history.
*   When running a node is already necessary for other functions (like transaction submission).
*   Often used as the *data source* for a [custom indexer](./custom-indexer.md), rather than the primary query interface for the dApp frontend.

Querying the node API directly offers more control than public explorers but often lacks the performance and query flexibility needed for complex dApps, leading many to build [custom indexers](./custom-indexer.md).
