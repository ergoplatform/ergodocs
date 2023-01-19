---
tags:
  - NIPoPoWs
---

# Pruned Full-Node Mode

## Overview 

[NiPoPoWS](nipopows.md) make it possible to boot a full node using a verified UTXO set snapshot without checking ~95% of the blockchain.

This provides full node security on an ordinary laptop in ~30-60 mins.

Hopefully, in Q1 2023, we will see a release with UTXO set snapshots + NiPoPoWs bootstrapping, you can follow along on GitHub here, [Bootstrapping with UTXO set](https://github.com/ergoplatform/ergo/pull/1444)

This mode is similar to fast-sync in Geth or Grothendieck, warp-mode in Parity (all three are Ethereum protocol clients), but makes more aggressive optimisations. In particular, a pruned-full node does not download and store full blocks that are not residing in a target blockchain suffix while also removing full blocks from the suffix. 


## Technical Workflow

In detail, a pruned client downloads all the headers, then, by using them, it checks proofs-of-work and linking structure(or parent id only?). Then it downloads a UTXO snapshot for some height from its peers. Finally, full blocks after the snapshot will be downloaded and applied to get a current UTXO set. A pruned full node also skips the AD-transformation block part, like a full node. Additional setting: \"suffix\" - how many full blocks to store(w. some minimum set?). Its regular modifiers processing is the same as for the full node regime, while its bootstrap process is different:

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