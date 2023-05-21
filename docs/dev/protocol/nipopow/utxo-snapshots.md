# UTXO Set Snapshots

At present, efforts are being focused on bootstrapping with a UTXO set snapshot. This allows for the operation of a node with a pruned UTXO set and full blocks, while concurrently facilitating bootstrapping with NiPoPoWs, and pruning headers in any mode.

This strategy ensures the acquisition of a verified UTXO set snapshot without the necessity of inspecting about 95% of the blockchain.

## Motivation

As the blockchain evolves, the requirements for downloading, storing, and processing the entire blockchain, including all full blocks, escalate. In blockchains like [Ergo](https://www.ergoplatform.com/) or [Ethereum](https://ethereum.org/), where the UTXO set snapshot is authenticated, this resource strain can be mitigated. This can be achieved by downloading and applying a historical UTXO set snapshot (or accounts snapshot in the case of Ethereum) along with the full blocks succeeding it. 

According to [this research paper](https://eprint.iacr.org/2018/129), this method can be as secure as processing all blocks, assuming an overwhelming probability function of the full-blocks suffix length.

[This specification](https://github.com/ergoplatform/ergo/blob/master/papers/utxo.md) explains how bootstrapping with a UTXO set snapshot is implemented in the Ergo protocol reference client. It will be beneficial in understanding the implementation and in developing alternative clients compatible with the reference client.

## Implementation Details

The UTXO set is authenticated using an AVL+ tree. The design principles for constructing this tree can be found in [this research paper](https://eprint.iacr.org/2016/994.pdf), and the tree implementation is available in the [Scrypto framework](https://github.com/input-output-hk/scrypto) on GitHub.

Time is divided into epochs, with each epoch comprising 51,200 blocks (~72 days). A snapshot is taken after the last block of an epoch, specifically, after processing a block with a height where *h % 51200 == 51199*.

## Chunk Format

*To be provided*

## Manifest Format

*To be provided*

## Networking Layer

*To be provided*

## Bootstrapping

*To be provided*

## Node Configuration

The node uses bootstrapping with a UTXO set snapshot if *ergo.node.utxoBootstrap = true* is set in the [configuration](conf-node.md).

## Sync Info V3

*To be provided*


## UTXO Set, Blocks, and Headers Pruning Capabilities

On the protocol level, the capability to prune the UTXO set, blocks, and headers is available. By setting `ergo.node.stateType = "digest"` in the node installation, support and enablement for UTXO set pruning are achieved. This means that while the node does not store the UTXO set, it still upholds full-node security guarantees. Additionally, block pruning is possible by using the `ergo.node.blocksToKeep` parameter in this mode, enabling the operation of a node with full-node security while minimizing storage (but retaining all the headers).

## Resources

Here are some relevant PRs on GitHub:

- [Bootstrapping with UTXO set - Part 1: Snapshot creation #1444](https://github.com/ergoplatform/ergo/pull/1444)
- [Preparation for bootstrapping with UTXO set snapshot, part 2 #1940](https://github.com/ergoplatform/ergo/pull/1940)
- [Utxo set bootstrapping code part 3 #1947](https://github.com/ergoplatform/ergo/pull/1947)
- [Utxo set bootstrapping preparation, part 5 #1985](https://github.com/ergoplatform/ergo/pull/1985) (recently merged)

Additionally, there is a PR related to P2P networking support for bootstrapping with UTXO set snapshot:

- [P2P networking support for bootstrapping with UTXO set snapshot #1444](https://github.com/ergoplatform/ergo/pull/1444) (recently merged)