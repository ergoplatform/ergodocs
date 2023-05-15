On the protocol level, we have the ability to prune the UTXO set, blocks, and headers. When setting `ergo.node.stateType = "digest"` in the node installation, UTXO set pruning is supported and enabled. This means that your node does not store the UTXO set but still maintains full-node security guarantees. It is also possible to prune blocks using the `ergo.node.blocksToKeep` parameter in this mode, allowing you to run a node with full-node security while minimizing storage (while still keeping all the headers).

Currently, we are working on bootstrapping with a UTXO set snapshot. This means that you can have a node with a pruned UTXO set and full blocks, and during bootstrapping with NiPoPoWs, headers can be pruned in any mode.

This approach enables obtaining a verified UTXO set snapshot without needing to check approximately 95% of the blockchain.

We are progressing towards bootstrapping with NiPoPoWs. Hopefully, by Q1 2023, a release will be available with UTXO set snapshots and NiPoPoWs bootstrapping, allowing for full-node security with bootstrapping taking approximately 30-60 minutes on a regular laptop.

Here are some relevant PRs on GitHub:

- [Bootstrapping with UTXO set - Part 1: Snapshot creation #1444](https://github.com/ergoplatform/ergo/pull/1444)
- [Preparation for bootstrapping with UTXO set snapshot, part 2 #1940](https://github.com/ergoplatform/ergo/pull/1940)
- [Utxo set bootstrapping code part 3 #1947](https://github.com/ergoplatform/ergo/pull/1947)
- [Utxo set bootstrapping preparation, part 5 #1985](https://github.com/ergoplatform/ergo/pull/1985) (recently merged)

Additionally, there is a PR related to P2P networking support for bootstrapping with UTXO set snapshot:

- [P2P networking support for bootstrapping with UTXO set snapshot #1444](https://github.com/ergoplatform/ergo/pull/1444) (recently merged)