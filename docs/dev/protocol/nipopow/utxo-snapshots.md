# UTXO Snapshots

We can prune the UTXO set, blocks and headers on a protocol level. In the [node](install.md), UTXO set pruning is supported and enabled when `ergo.node.stateType = "digest"`, then your node does not store UTXO set but retains full-node security guarantees. It is also possible to prune blocks in this mode (ergo.node.blocksToKeep parameter). Then you can run a node with full node security and min storage (it still keeps all the headers).

Currently, we are working on bootstrapping with a UTXO set snapshot. This enables you to have a node with a UTXO set and full-blocks pruned, and then on bootstrapping with NiPoPoWs (then headers can be pruned in any mode)

This makes it possible to get a verified UTXO set snapshot without checking ~95% of the blockchain.

Then bootstrapping with NiPoPoWs will be done. Hopefully, in Q1 2023, we will see a release with UTXO set snapshots + NiPoPoWs bootstrapping, giving full node security with bootstrapping in ~30-60 mins on an ordinary laptop.

-  [Bootstrapping with UTXO set - Part 1: Snapshot creation #1444](https://github.com/ergoplatform/ergo/pull/1444)

Most full nodes will provide snapshots. Security is theoretically the same as for a full node.
