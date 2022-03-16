# Modes of Operation


Ergo (since the very first testing network `Testnet0`) supports multiple security models. 

In addition to running in "full node mode", which is similar to Bitcoin fullnode, Ergo reference implementation supports `Light-SPV`, `Light-Fullnode` and `Pruned-Fullnode` modes.

## Full-Node Mode

Like in Bitcoin, a full node is storing all the full blocks since genesis block. Full node checks proofs of work, linking structure correctness (parent block id, interlink elements), and all the transactions in all the blocks. A fullnode is storing all the full blocks forever. It is also holding full UTXO set to be able to validate an arbitrary transaction. The only optimization a fullnode is doing is that is skipping downloading and checking AD-transformation block part (see below in the "Light-Fullnode" section). For the full node regime, modifiers processing workflow is as follows:

1.  Send ErgoSyncInfo message to connected peers.
2.  Get response with INV message, containing ids of blocks, better than our best block.
3.  Request headers for all ids from 2.
4.  On receiving header:

```java
if(history.apply(header).isSuccess) {
    if(!isInitialBootstrapping) Broadcast INV for this header
    Request transaction ids from this block
    } else {
    blacklist peer
    }
```

1.  On receiving transaction ids from header:

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
    /*We should notify our neighbours, that now we have all the transactions
    State apply modifiers (may be empty for block in a fork chain)
    and generate ADProofs for them.
    TODO requires different interface from scorex-core,
    because it should return ADProofs
    TODO when minimal state apply Progress info,
    it may also create UTXOSnapshot
    (e.g. every 30000 blocks like in Ethereum).
    This UTXOSnapshot should be required for mining by Rollerchain*/
    if(State().apply(ProgressInfo) == Success((newState, ADProofs))) {
    if("mode"="full" || "mode"=="pruned-full") ADProofs.foreach ( ADProof => History.apply(ADProof))
    if("mode"=="pruned-full" || "mode"=="light-full") drop BlockTransactions and ADProofs older than BlocksToKeep
    } else {
    //Drop Header from history, because it's transaction sequence is not valid
    History.drop(BlockTransactions.headerId)
    }
} else {
blacklist peer who sent header
}
```

### Pruned Full-Node Mode

This mode is similar to fast-sync in Geth or Grothendieck, warp-mode in Parity (all the three are Ethereum protocol clients), but makes more aggressive optimizations. In particular, a pruned-fullnode is not down- loading and storing full blocks not residing in a target blockchain suffix, and also removing full blocks going out of the suffix. In detail, a pruned client is downloading all the headers, then, by using them, it checks proofs-of-work and linking structure(or parent id only?). Then it downloads a UTXO snapshot for some height from its peers. Finally, full blocks after the snapshot are to be downloaded and applied to get a current UTXO set. A pruned fullnode is also skipping AD-transformation block part, like a fullnode. Additional setting: \"suffix\" - how much full blocks to store(w. some minimum set?). Its regular modifiers processing is the same as for fullnode regime, while its bootstrap process is different:

1.  Send `ErgoSyncInfo` message to connected peers.
2.  Get response with `INV` message, containing ids of blocks, better than
    our best block.
3.  Request headers for all ids from 2.
4.  On receiving header:

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
    request chunk from sender() //Or from random fullnode
    }
```

7.  On receiving `UTXOSnapshotChunk`:

    ```java
    State.applyChunk(UTXOSnapshotChunk) match {
         case Success(Some(newMinimalState)) => GOTO 8
         case Success(None) => stay at 7
         /*we need more chunks to construct state.
         TODO periodicaly request missed chunks*/
         case Failure(e) => ???
         //UTXOSnapshotChunk or constcucted state roothash is invalid
      }
    ```

8.  Request `BlockTransactions` starting from State we have

    ```java
    History.headersStartingFromId(State.headerId).foreach { header =>
        send message(GetBlockTransactionsForHeader(header)) to Random fullnode
      }
    ```

9.  On receiving `BlockTransactions`: same as in Fullnode.7.
10. Operate as Fullnode.

## Light Full-Node Mode

This mode is based on an idea to use a 2-party authenticated dynamic dictionary built on top of UTXO set. A light-fullnode holds only a root digest of a dictionary. It checks all the full blocks, or some suffix of the full blockchain, depending on setting, thus starting from a trusted pre-genesis digest or some digest in the blockchain. A light-fullnode is using AD-transformations (authenticated dictionary transformations) block section containing batch-proof for UTXO transformations to get a new digest from an old one. It also checks all the transactions, but doesn't store anything but a single digest for that. Details can be found in [this paper](https://eprint.iacr.org/2016/994).

Additional settings: 

- **depth** - from which block in the past to checktransactions (if 0, then go from genesis).
- **additional-checks** - light-fullnode trusts previous digest and checks
current digest validity by using the previous one as well as
AD-transformations.
- **additional-depth** - depth to start additional checks from.

1.  Send ErgoSyncInfo message to connected peers.
2.  Get response with INV message, containing ids of blocks, better than our best block.
3.  Request headers for all ids from 2.
4.  On receiving header:

```java
if(History.apply(header).isSuccess) {
    if(!(localScore == networkScore)) GOTO 1
    else GOTO 5
    } else {
    blacklist peer
    }
```

5.  Request BlockTransactions and ADProofs starting from BlocksToKeep
    back in History (just 1 last header after node botstrapping):

```java
History.lastBestHeaders(BlocksToKeep).foreach { header =>
    send message(GetBlockTransactionsForHeader(header)) to Random fullnode
    send message(GetAdProofsHeader(header)) to Random fullnode
    }
```

6.  On receiving modifier BlockTransactions or ADProofs:

```java
if(History.apply(modifier) == Success(ProgressInfo)) {
    /* TODO if history now contains both ADProofs and BlockTransactions,
    it should return ProgressInfo with both of them, otherwise
    it should return empty ProgressInfo */
if(State().apply(ProgressInfo) == Success((newState, ADProofs)))
{
if("mode"=="pruned-full") drop BlockTransactions and ADProofs older than BlocksToKeep
}
else {
            /*Drop Header from history, because it's transaction sequence is not valid*/
            History.drop(BlockTransactions.headerId)
        }
    }
```

## Light-SPV Mode

This mode is not about checking any full blocks. Like in Bitcoin, an SPV
node is downloading block headers only, and so checks only proofs of
work and links. Unlike Bitcoin's SPV, the Light-SPV is downloading and
checking not all the headers but a sublinear(in blockchain length)
number of them(in benchmarks, this is about just tens of kilobytes
instead of tens or hundreds of megabytes for Bitcoin/Ethereum).
Light-SPV mode is intended to be useful for mobile phones and low-end
hardware.

### Bootstrap

1.  Send GetPoPoWProof for all connections.

2.  On receive PoPoWProof apply it to History (History should be able to
    determine, whether this PoPoWProof is better than it's current best
    header chain).

3.  GOTO regular regime.

### Regular

1.  Send ErgoSyncInfo message to connected peers
2.  Get response with INV message, containing ids of blocks, better than
    our best block.
3.  Request headers for all ids from 2.
4.  On receiving header:

```java
    if(History.apply(header).isSuccess) {
    State.apply(header) // just change state roothash
    if(!isInitialBootstrapping) Broadcast INV for this header
    } else {
    blacklist peer
    }
```

## Mode-Related Settings

Ergo has the following settings determines a mode:

-   ADState: Boolean - keeps state roothash only.
-   VerifyTransactions: Boolean - download block transactions and verify them (requires BlocksToKeep == 0 if disabled).
-   PoPoWBootstrap: Boolean - download PoPoW proof only
-   BlocksToKeep: Int - number of last blocks to keep with transactions,
    for all other blocks it keep header only. Keep all blocks from
    genesis if negative
-   MinimalSuffix: Int - minimal suffix size for PoPoW proof (may be
    pre-defined constant).

`if(VerifyTransactions == false) require(BlocksToKeep == 0)` Mode from "multimode.md" can be determined as follows: