# UTXO Snapshots

We can prune the UTXO set, blocks and headers on a protocol level. In the [node](node.md), UTXO set pruning is supported and enabled when `ergo.node.stateType = "digest"`, then your node does not store UTXO set but retains full-node security guarantees. It is also possible to prune blocks in this mode (ergo.node.blocksToKeep parameter). Then you can run a node with full node security and min storage (it still keeps all the headers).

Currently, we are working on bootstrapping with a UTXO set snapshot. This enables you to have a node with a UTXO set and full-blocks pruned, and then on bootstrapping with NiPoPoWs (then headers can be pruned in any mode)