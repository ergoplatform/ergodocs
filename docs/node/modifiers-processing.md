# Ergo Modifiers Processing

Ergo's modifiers processing algorithm functions across all security modes. In contrast to many blockchain systems, Ergo features several types of modifiers which can be categorized into two distinct categories: In-memory and Persistent.

## In-memory Modifiers

1. **Transaction**: This is an in-memory modifier.
2. **TransactionIdsForHeader**: These are the ids of transactions associated with a particular block.
3. **UTXOSnapshotManifest**: These are the ids of UTXO chunks.

## Persistent Modifiers

1. **BlockTransactions**: These are sequences of transactions, each corresponding to a single block.
2. **ADProofs**: These are proofs verifying transaction correctness relative to the corresponding UTXO.
3. **Header**: Contains data needed to verify PoW, provides a link to the previous block, and carries the state root hash and root hash to its payload (BlockTransactions, ADProofs, Interlinks, etc).
4. **UTXOSnapshotChunk**: Represents a portion of UTXO.
5. **PoPoWProof**

Ergo employs certain parameters that define a specific security regime:

1. **ADState**: A boolean value. If true, only the state roothash is kept.
2. **VerifyTransactions**: A boolean value. If true, block transactions are downloaded and verified. If disabled, `BlocksToKeep` must equal 0.
3. **PoPoWBootstrap**: A boolean value. If true, only the PoPoW proof is downloaded.
4. **BlocksToKeep**: An integer value specifying the number of the most recent blocks to retain with their transactions. For all other blocks, only the header is kept. If the value is negative, all blocks from genesis are retained.
5. **MinimalSuffix**: An integer value representing the minimal suffix size for the PoPoW proof. This could be a pre-defined constant.

The system enforces the following condition:

```java
if(VerifyTransactions == false) require(BlocksToKeep == 0)
```

The mode as defined in `multimode.md` can be identified as follows:

```java
mode = if(ADState == false && VerifyTransactions == true
&& PoPoWBootstrap == false && BlocksToKeep < 0) "full"
else if(ADState == false && VerifyTransactions == true
&& PoPoWBootstrap == false && BlocksToKeep >= 0) "pruned-full"
else if(ADState == true && VerifyTransactions == true
&& PoPoWBootstrap == false) "light-full"
else if(ADState == true && VerifyTransactions == false
&& PoPoWBootstrap == true && BlocksToKeep == 0) "light-spv"
else if(ADState == true && VerifyTransactions == true
&& PoPoWBootstrap == true && BlocksToKeep == 0) "light-full-PoPoW"
else //Other combinations are possible
```

## Modifiers Processing

This operation involves updating the headers chain to the best in the network. The process includes sending ErgoSyncInfo messages to connected peers, receiving responses with INV messages containing ids of blocks better than the current best block, requesting headers for all ids, and reacting based on the received header. 

During bootstrapping, headers are downloaded. If `PoPoW` is true, `GetPoPoWProof` is sent for all connections, and upon receipt, the PoPoWProof is applied to the History. Otherwise, the headers chain is updated to the best in the network.

Additionally, the initial state is downloaded to start processing transactions. If `ADState` is true, the state is initialized with the state roothash from the block header `BlocksToKeep` ago. If `BlocksToKeep` is less than 0 or greater than `History.headersHeight`, the state is initialized with the genesis state. Otherwise, a full state `BlocksToKeep` back in history is downloaded.

The state is then updated to the best headers height. If `State.bestHeader` equals `History.bestHeader`, no action is taken as the state is already updated. If `VerifyTransactions` is false, the state root hash is simply updated to the best header in history. If `VerifyTransactions` is true, transaction ids are requested from all headers without transactions and transaction processing continues as described in the original text.

In regular mode, two infinite loops run in different threads, each executing the following functions:

1. Updating the headers chain to the best in the network.
2. Downloading and updating full blocks as needed.

Transaction processing continues as described in the original text, with the system requesting transaction ids from all headers without transactions, receiving TransactionIdsForHeader, and performing actions based on whether transactions are successful or not.


```java
def updateHeadersChainToBestInNetwork() = {
  1.2.1. Send ErgoSyncInfo message to connected peers
  1.2.2. Get response with INV message,
  containing ids of blocks, better than our best block
  1.2.3. Request headers for all ids from 1.2.2.
  1.2.4. On receiving header
   if(History.apply(header).isSuccess) {
      if(!(localScore == networkScore)) GOTO 1.2.1
   } else {
      blacklist peer
      GOTO 1.2.1
   }
}
```

## Bootstraping

The bootstrap process involves two main steps: downloading headers and downloading the initial state to begin transaction processing.



### Download headers

Depending on the **PoPoW** value, the process varies.

If **PoPoW** is *true*:

```
1.1.1. Send GetPoPoWProof(suffix = Max(MinimalSuffix ,BlocksToKeep)) for all connections
1.1.2. On receive PoPoWProof, apply it to History
```

If PoPoW is false, update the headers chain to the best in the network.



### Download initial State to start processing transactions

The system checks for the ADState and BlocksToKeep values to decide how to initialize the state.



```java
if(ADState == true) {
  Initialize state with state roothash from block header BlocksToKeep ago
} else if(BlocksToKeep < 0 || BlocksToKeep > History.headersHeight) {
  Initialize state with genesis State
} else {
/*
We need to download full state BlocksToKeep back in history
TODO what if we can download state only "BlocksToKeep - N"
or "BlocksToKeep + N" blocks back?
*/
  2.1. Request historical UTXOSnapshotManifest for at least BlocksToKeep back
  2.2. On receiving UTXOSnapshotManifest:
    UTXOSnapshotManifest.chunks.foreach ( chunk => request chunk from sender()
/*Or from random fullnode*/
  2.3. On receiving UTXOSnapshotChunk
  State.applyChunk(UTXOSnapshotChunk) match {
     case Success(Some(newMinimalState)) => GOTO 3
     case Success(None) => stay at 2.3
     /*we need more chunks to construct state. TODO periodicaly request missed chunks*/
     case Failure(e) => ???
     /*UTXOSnapshotChunk or constcucted state roothash is invalid*/
  }
}
```
### Update State to best headers height

Depending on the values of State.bestHeader, History.bestHeader, and VerifyTransactions, the state is updated accordingly.

```java
 if(State.bestHeader == History.bestHeader) {
    //Do nothing, State is already updated
  } else if(VerifyTransactions == false) {
/*Just update State rootshash to best header in history*/
    State.setBestHeader(History.bestHeader)
  } else {
/*we have headers chain better than full block */
    3.1.
      assert(history contains header chain from State.bestHeader to History.bestHeaders)
      History.continuation(from = State.bestHeader, size = ???).get.foreach { header =>
        sendToRandomFullNode(GetBlockTransactionsForHeader(header))
        if(ADState == true) sendToRandomFullNode(GetADProofsForHeader(header))
      }
    3.2. On receiving modifiers ADProofs or BlockTransactions
      /*TODO History should return non-empty ProgressInfo
      only if it contains both ADProofs and BlockTransactions,
      or it contains BlockTransactions and ADState==false*/
      if(History.apply(modifier) == Success(ProgressInfo)) {
        if(State().apply(ProgressInfo) == Success((newState, ADProofs))) {
          if(ADState==false) ADProofs.foreach ( ADProof => History.apply(ADProof))
          if(BlocksToKeep>=0)
          /*remove BlockTransactions and ADProofs older than BlocksToKeep from history*/
        } else {
      /*Drop Header from history,
      because it's transaction sequence is not valid*/
          History.drop(modifier.headerId)
        }
      } else {
        blacklistPeer
      }
      GOTO 3
    }
```
### GOTO regular mode.



## Regular Mode

In the regular mode, two infinite loops run in different threads, each performing a different function:

- Updating the headers chain to the best in the network.
- Downloading and updating full blocks when needed.

Depending on the values of `State.bestHeader`, `History.bestHeader`, and `VerifyTransactions`, specific actions are taken.


```java
 if(State.bestHeader == History.bestHeader) {
    //Do nothing, State is already updated
  } else if(VerifyTransactions == false) {
    //Just update State rootshash to best header in history
    State.setBestHeader(History.bestHeader)
  } else {
    //we have headers chain better then full block
    3.1. Request transaction ids from all headers without transactions
      assert(history contains header chain from State.bestHeader to History.bestHeaders)
      History.continuation(from = State.bestHeader, size = ???).get.foreach { header =>
        sendToRandomFullNode(GetTransactionIdsForHeader(header))
        if(ADState == true) sendToRandomFullNode(GetADProofsForHeader(header))
      }
    3.2. On receiving TransactionIdsForHeader:
      Mempool.apply(TransactionIdsForHeader)
      TransactionIdsForHeader.filter(txId => !MemPool.contains(txId)).foreach { txId =>
        request transaction with txId
      }
    3.3. On receiving a transaction:
      if(Mempool.apply(transaction).isSuccess) {
         Broadcast INV for this transaction
         Mempool.getHeadersWithAllTransactions { BlockTransactions =>
            GOTO 3.4 //now we have BlockTransactions
         }
      }
    3.4. (same as 3.2. from bootstrap)
  }
```
