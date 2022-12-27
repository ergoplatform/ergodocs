# Modes of Operation


The Ergo node supports multiple security models. (since `Testnet0`!, the very first testing network)

In addition to running in "full node mode," similar to a full Bitcoin node, Ergo reference implementation supports [Light-SPV](#light-spv-mode), [Light-Fullnode](#light-full-node-mode), and [Pruned-Fullnode](#pruned-full-node-mode) modes.

## Full-Node Mode

Like in Bitcoin, a full node stores all the blocks since the genesis block, and a full node checks proofs of work, linking structure correctness (parent block id, interlink elements), and all the blocks' transactions. A full node stores all the full blocks forever, and it is also holding a full UTXO set to be able to validate an arbitrary transaction. A full node's only optimisation is skipping downloading and checking the AD-transformation block part (see below in the "Light-Fullnode" section). For the full node regime, the modifiers processing workflow is as follows:

1.  Send ErgoSyncInfo message to connected peers.
Get a response with an INV message containing the ids of blocks, better than our best block.
3.  Request headers for all ids from 2.
4.  On receiving Header:

```java
if(history.apply(header).isSuccess) {
    if(!isInitialBootstrapping) Broadcast INV for this Header
    Request transaction ids from this block
    } else {
    blacklist peer
    }
```

1.  On receiving transaction ids from the Header:

```java
transactionIdsForHeader.filter(txId => !MemPool.contains(txId)).foreach { txId =>
    request transaction with txId
}
```

2.  On receiving a transaction:

```java
if(Mempool.apply(transaction).isSuccess) {
    if(!isInitialBootstrapping) Broadcast INV for this transaction
        Mempool.getHeadersWithAllTransactions { BlockTransactions =>
            GOTO 7
    }
}
```

3.  Now we have `BlockTransactions`: all transactions corresponding to some Header

```java
if(History.apply(BlockTransactions) == Success(ProgressInfo)) {
    if(!isInitialBootstrapping) Broadcast INV for BlockTransactions
    /*We should notify our neighbours that now we have all the transactions
    State apply modifiers (may be empty for a block in a forked chain)
    and generate ADProofs for them.
    TODO requires a different interface from scorex-core,
    because it should return ADProofs
    TODO when minimal state apply Progress info,
    it may also create UTXOSnapshot
    (e.g. every 30000 blocks like in Ethereum).
    This UTXOSnapshot should be required for mining by Rollerchain*/
    if(State().apply(ProgressInfo) == Success((newState, ADProofs))) {
        if("mode"="full" || "mode"=="pruned-full") ADProofs.foreach ( ADProof => History.apply(ADProof))
        if("mode"=="pruned-full" || "mode"=="light-full") drop BlockTransactions and ADProofs older than BlocksToKeep
    } else {
        //Drop Header from history because its transaction sequence is not valid
        History.drop(BlockTransactions.headerId)
    }
} else {
blacklist peer who sent Header
}
```

### Pruned Full-Node Mode

This mode is similar to fast-sync in Geth or Grothendieck, warp-mode in Parity (all three are Ethereum protocol clients), but makes more aggressive optimizations. In particular, a pruned-full node is not downloading and storing full blocks not residing in a target blockchain suffix and removing full blocks from the suffix. In detail, a pruned client downloads all the headers, then, by using them, it checks proofs-of-work and linking structure(or parent id only?). Then it downloads a UTXO snapshot for some height from its peers. Finally, full blocks after the snapshot will be downloaded and applied to get a current UTXO set. A pruned full node also skips the AD-transformation block part, like a full node. Additional setting: \"suffix\" - how many full blocks to store(w. some minimum set?). Its regular modifiers processing is the same as for the full node regime, while its bootstrap process is different:

1.  Send an `ErgoSyncInfo` message to connected peers.
2.  Get a response with an `INV` message containing the ids of blocks, better than
    our best block.
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

## Light Full-Node Mode

This mode is based on an idea to use a 2-party authenticated dynamic dictionary built on top of the UTXO set. A light-fullnode holds only a root digest of a dictionary. It checks all the full blocks, or some suffix of the full blockchain, depending on the setting, thus starting from a trusted pre-genesis digest or some digest in the blockchain. A light-fullnode uses AD-transformations (authenticated dictionary transformations) block section containing batch-proof for UTXO transformations to get a new digest from an old one. It also checks all the transactions but does not store anything but a single digest. Details can be found in [this paper](https://eprint.iacr.org/2016/994).

Additional settings: 

- **depth** - from which block in the past to checktransactions (if 0, then go from genesis).
- **additional-checks** - light-full node trusts the previous digest and checks current digest validity by using the previous one as well as AD-transformations.
- **additional-depth** - depth to start additional checks from.

Steps:

1.  Send **ErgoSyncInfo** message to connected peers.
2.  Get a response with an **INV** message containing the ids of blocks, better than our best block.
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

5.  Request BlockTransactions and ADProofs starting from BlocksToKeep
    back in History (just one last header after node bootstrapping):

```java
History.lastBestHeaders(BlocksToKeep).foreach { header =>
    send message(GetBlockTransactionsForHeader(header)) to Random full node
    send message(GetAdProofsHeader(header)) to Random full node
    }
```

6.  On receiving modifier BlockTransactions or ADProofs:

```java
if(History.apply(modifier) == Success(ProgressInfo)) {
    /* TODO if history now contains both ADProofs and BlockTransactions,
    it should return ProgressInfo with both of them. Otherwise,
    it should return an empty ProgressInfo */
if(State().apply(ProgressInfo) == Success((newState, ADProofs)))
{
if("mode"=="pruned-full") drop BlockTransactions and ADProofs older than BlocksToKeep
}
else {
            /*Drop Header from history because its transaction sequence is not valid*/
            History.drop(BlockTransactions.headerId)
        }
    }
```

## Light-SPV Mode

A Light SPV node does not check full blocks and is useful for mobile phones and low-end hardware. An SPV node downloads the block headers only (and checks proofs of work and links). Unlike Bitcoin's SPV, Ergo's Light-SPV downloads and checks not every Header but a sublinear number (in blockchain length). In benchmarks, this results in tens of kilobytes compared to tens or hundreds of megabytes in Bitcoin/Ethereum. 

### Bootstrap

1.  Send **`GetPoPoWProof`** for all connections.
2.  On receiving **`PoPoWProof`**, apply it to History (History should determine whether this PoPoWProof is better than its current best header chain).
3.  **`GOTO`** regular regime.

### Regular

1.  Send ErgoSyncInfo message to connected peers
2.  Get a response with an INV message containing the ids of blocks, better than
    our best block.
3.  Request headers for all ids from 2.
4.  On receiving Header:

```java
    if(History.apply(header).isSuccess) {
        State.apply(header) // just change state roothash
    if(!isInitialBootstrapping) Broadcast INV for this header
    } else {
        blacklist peer
    }
```

## Mode-Related Settings

Ergo has the following settings which determine a mode:

-   **`ADState: Boolean`** - keeps state roothash only.
-   **`VerifyTransactions: Boolean`** - download block transactions and verify them (requires BlocksToKeep == 0 if disabled).
-   **`PoPoWBootstrap: Boolean`** - download PoPoW proof only
-   **`BlocksToKeep: Int`** - number of last blocks to keep with transactions; for all other blocks, it keeps Header only. Keep all blocks from
    genesis if negative
-   **`MinimalSuffix: Int`** - minimal suffix size for PoPoW proof (maybe
    pre-defined constant).

`if(VerifyTransactions == false) require(BlocksToKeep == 0)` Mode from "multimode.md" can be determined as follows:
