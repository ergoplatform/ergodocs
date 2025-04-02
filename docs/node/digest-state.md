---
tags:
  - Digest State
  - Node
  - Pruning
  - UTXO
  - Storage
---

# Digest State

The "Digest State" feature in the Ergo protocol allows nodes to optimize the storage of blockchain data without compromising security and performance. By enabling the Digest State feature, nodes can prune or reduce the size of the UTXO (Unspent Transaction Output) set, blocks, and headers, resulting in more efficient storage utilization.

## How does it work?

In a traditional blockchain, each node stores the complete history of transactions, blocks, and headers, which can lead to significant storage requirements as the blockchain grows. However, with the Digest State feature, Ergo nodes can selectively retain only the essential data.

To enable the Digest State feature, set the [`ergo.node.stateType = "digest"`](conf-node.md#state-type) configuration parameter to "digest". Once enabled, the node supports UTXO set pruning, allowing it to reduce the storage footprint while still maintaining full-node security guarantees.

## Benefits of Digest State

- Efficient Storage: By pruning unnecessary data, Digest State reduces the storage requirements for nodes, making it feasible to run Ergo nodes on devices with limited storage capacity.

- Performance Optimization: With a smaller UTXO set, blocks, and headers, nodes can process transactions and blocks more efficiently, potentially improving overall network performance.

- Full-Node Security: Despite not storing the entire UTXO set, nodes with Digest State enabled can still validate transactions and blocks, ensuring compliance with the consensus rules of the network.

## Considerations

While Digest State provides storage and performance benefits, it's important to note that a healthy network requires a sufficient number of full (non-pruning) nodes. Full nodes maintain the complete history and state of the blockchain, serving as a reference for new nodes and ensuring the integrity of the entire blockchain's history.
