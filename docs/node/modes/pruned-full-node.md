# Pruned Full-Node Mode and UTXO Set Snapshots

## Overview 

[NiPoPoWS](nipopows.md) make it possible to boot a full node using a *verified UTXO set snapshot*. This provides full node security on an ordinary laptop in ~30-60 mins, without having to check ~95% of the blockchain. 

> Hopefully, in Q1 2023, we will see a release with UTXO set snapshots + NiPoPoWs bootstrapping; you can follow along on GitHub here, [Bootstrapping with UTXO set](https://github.com/ergoplatform/ergo/pull/1444)

This mode is similar to [*fast-sync*](https://ethereum.stackexchange.com/questions/1161/what-is-geths-fast-sync-and-why-is-it-faster) in Geth or Grothendieck, or [*warp-mode*](https://ethereum.stackexchange.com/questions/9991/what-is-paritys-warp-sync-and-why-is-it-faster-than-geth-fast) in Parity (all are Ethereum protocol clients), but makes more aggressive optimisations. 

Specifically, a pruned-full node does not download and store full blocks that do not reside in a target blockchain suffix while also removing full blocks from the suffix. 

## Technical Workflow (WIP)

In detail, a pruned client downloads all the headers, then, by using them, it checks proofs-of-work and linking structure(or parent id only?). Then it downloads a UTXO snapshot for some height from its peers. Finally, full blocks after the snapshot will be downloaded and applied to get a current UTXO set. A pruned full node also skips the AD-transformation block part, like a full node. Additional setting: "suffix" - how many full blocks to store(w. some minimum set?). Its regular modifiers processing is the same as for the full node regime, while its bootstrap process is different:

1.  Send an **ErgoSyncInfo** message to connected peers.
2.  Get a response with an `INV` message containing the ids of blocks, better than our best block.
3.  Request headers for all ids from 2.
4.  On receiving Header:
    ```java
    if(History.apply(header).isSuccess) {
        if(!(localScore == networkScore)) GOTO 1
        else GOTO 5
    } else {
        blacklist peer
    }
    ```
5.  Request historical `UTXOManifest` for at least `BlocksToKeep` back.
6.  On receiving `UTXOSnapshotManifest`:
    ```java
    UTXOSnapshotManifest.chunks.foreach { chunk =>
        request chunk from sender() //Or from random full node
    }
    ```
7.  On receiving `UTXOSnapshotChunk`:
    ```java
    State.applyChunk(UTXOSnapshotChunk) match {
         case Success(Some(newMinimalState)) => GOTO 8
         case Success(None) => stay at 7
         /*we need more chunks to construct the state.
         TODO periodically request missed chunks*/
         case Failure(e) => ???
         //UTXOSnapshotChunk or constructed state root hash is invalid
    }
    ```
8.  Request `BlockTransactions` starting from State we have
    ```java
    History.headersStartingFromId(State.headerId).foreach { header =>
        send message(GetBlockTransactionsForHeader(header)) to Random full node
    }
    ```
9.  On receiving `BlockTransactions`: same as in Fullnode.7.
10. Operate as Fullnode.

## UTXO Set Snapshots

At present, efforts are being focused on bootstrapping with a UTXO set snapshot. This allows for the operation of a node with a pruned UTXO set and full blocks, while concurrently facilitating bootstrapping with NiPoPoWs, and pruning headers in any mode.

This strategy ensures the acquisition of a verified UTXO set snapshot without the necessity of inspecting about 95% of the blockchain.

### Motivation

As the blockchain evolves, the requirements for downloading, storing, and processing the entire blockchain, including all full blocks, escalate. In blockchains like [Ergo](https://www.ergoplatform.com/) or [Ethereum](https://ethereum.org/), where the UTXO set snapshot is authenticated, this resource strain can be mitigated. This can be achieved by downloading and applying a historical UTXO set snapshot (or accounts snapshot in the case of Ethereum) along with the full blocks succeeding it. 

According to [this research paper](https://eprint.iacr.org/2018/129), this method can be as secure as processing all blocks, assuming an overwhelming probability function of the full-blocks suffix length.

[This specification](https://github.com/ergoplatform/ergo/blob/master/papers/utxo.md) explains how bootstrapping with a UTXO set snapshot is implemented in the Ergo protocol reference client. It will be beneficial in understanding the implementation and in developing alternative clients compatible with the reference client.

### Implementation Details

The UTXO set is authenticated using an AVL+ tree. The design principles for constructing this tree can be found in [this research paper](https://eprint.iacr.org/2016/994.pdf), and the tree implementation is available in the [Scrypto framework](https://github.com/input-output-hk/scrypto) on GitHub.

Time is divided into epochs, with each epoch comprising 51,200 blocks (~72 days). A snapshot is taken after the last block of an epoch, specifically, after processing a block with a height where *h % 51200 == 51199*.

#### Chunk Format

*To be provided*

#### Manifest Format

*To be provided*

#### Networking Layer

*To be provided*

#### Bootstrapping

*To be provided*

#### Node Configuration

The node uses bootstrapping with a UTXO set snapshot if *ergo.node.utxoBootstrap = true* is set in the [configuration](conf-node.md).

#### Sync Info V3

*To be provided*

## Resources

Here are some relevant PRs on GitHub:

- [Bootstrapping with UTXO set - Part 1: Snapshot creation #1444](https://github.com/ergoplatform/ergo/pull/1444)
- [Preparation for bootstrapping with UTXO set snapshot, part 2 #1940](https://github.com/ergoplatform/ergo/pull/1940)
- [Utxo set bootstrapping code part 3 #1947](https://github.com/ergoplatform/ergo/pull/1947)
- [Utxo set bootstrapping preparation, part 5 #1985](https://github.com/ergoplatform/ergo/pull/1985) (recently merged)

Additionally, there is a PR related to P2P networking support for bootstrapping with UTXO set snapshot:

- [P2P networking support for bootstrapping with UTXO set snapshot #1444](https://github.com/ergoplatform/ergo/pull/1444) (recently merged)
