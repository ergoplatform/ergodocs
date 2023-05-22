# Digest State

In the Ergo protocol, there's a feature called the "Digest State". This feature allows nodes to prune or reduce the UTXO (Unspent Transaction Output) set, blocks, and headers, meaning that these data elements can be minimized for efficiency without compromising the network's security and performance. 

In a typical blockchain, each node stores the entire history of transactions, blocks, and headers. This can lead to significant storage requirements as the blockchain grows. However, with the Digest State feature, Ergo allows nodes to keep only the essential data. 

Setting [`ergo.node.stateType = "digest"`](conf-node.md#statetype) in the configuration of a node enables this feature. Once enabled, the node supports and enables UTXO set pruning. 

Although the node does not store the entire UTXO set when this feature is enabled, it still maintains full-node security guarantees. In the context of blockchain, a full node is a node that verifies all the rules of the blockchain. In Ergo's case, even if a node is not storing the entire UTXO set (due to the Digest State feature being enabled), it can still validate transactions and blocks, enforcing the consensus rules of the network.

This feature allows a trade-off between storage requirements and performance, making it possible to run Ergo nodes on devices with lower storage capacity. The ability to prune the UTXO set makes the protocol more scalable and potentially faster, as there is less data to process.

However, it is important to note that a network needs a sufficient number of full (non-pruning) nodes to function correctly and securely. These full nodes maintain the complete history and state of the blockchain, providing the essential data required to bootstrap new nodes and verify the entirety of the blockchain's history. While Digest State nodes maintain the security guarantees of a full node, they do not maintain the full transaction history. Therefore, a balance between full nodes and Digest State nodes is necessary for a healthy, functioning network.