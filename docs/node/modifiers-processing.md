---
tags:
  - Modifiers
  - Processing
  - Node
  - Technical
  - Architecture
---

# Ergo Modifiers Processing

Ergo's modifiers processing algorithm is a universal mechanism that operates consistently across all security modes. Unlike many blockchain systems, Ergo introduces several types of modifiers, which can be broadly classified into two categories: In-memory and Persistent.

## In-memory Modifiers

In-memory modifiers are temporary and do not persist across sessions. They include:

1. **Transaction**: A single transaction represents an in-memory modifier.
2. **TransactionIdsForHeader**: These are identifiers associated with transactions for a specific block.
3. **UTXOSnapshotManifest**: These are identifiers for chunks of the Unspent Transaction Output (UTXO) set.

## Persistent Modifiers

Persistent modifiers are data elements that are stored and persist across sessions. They play a crucial role in maintaining the continuity and integrity of the Ergo network. The following are the types of persistent modifiers:

1. **BlockTransactions**: These are sequences of transactions, each corresponding to a single block. They provide a detailed record of all transactions within a block.

2. **ADProofs**: These are proofs that validate the correctness of transactions relative to the corresponding Unspent Transaction Output (UTXO). They ensure that all transactions are valid and consistent with the UTXO.

3. **Header**: This contains essential data needed to verify Proof of Work (PoW), provides a link to the previous block, and carries the state root hash and root hash to its payload (BlockTransactions, ADProofs, Interlinks, etc). It serves as the backbone of the blockchain, linking all blocks together.

4. **UTXOSnapshotChunk**: This represents a portion of the UTXO set. It allows the UTXO set to be managed in manageable chunks, improving efficiency.

5. **PoPoWProof**: This is a proof of Proof of Work (PoPoW) that provides evidence of the computational work done to add a new block to the blockchain.

In addition to these modifiers, Ergo employs certain parameters that define a specific security regime. 

These parameters include:

1. **ADState**: A boolean value. If true, only the state root hash is kept. This parameter helps in reducing the storage requirements by only keeping the state root hash.

2. **VerifyTransactions**: A boolean value. If true, block transactions are downloaded and verified. This parameter ensures the integrity of the transactions within the blocks. If disabled, `BlocksToKeep` must equal 0.

3. **PoPoWBootstrap**: A boolean value. If true, only the PoPoW proof is downloaded. This parameter allows for a lighter bootstrap process by only downloading the PoPoW proof.

4. **BlocksToKeep**: An integer value specifying the number of the most recent blocks to retain with their transactions. For all other blocks, only the header is kept. If the value is negative, all blocks from genesis are retained. This parameter helps in managing the storage requirements by specifying the number of blocks to keep.

5. **MinimalSuffix**: An integer value representing the minimal suffix size for the PoPoW proof. This could be a pre-defined constant. This parameter helps in managing the size of the PoPoW proof.


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

Additionally, the initial state is downloaded to start processing transactions. If `ADState` is true, the state is initialized with the state root hash from the header of the block `BlocksToKeep` blocks ago. If `BlocksToKeep` is less than 0 or greater than `History.headersHeight`, the state is initialized with the genesis state. Otherwise, the full state from `BlocksToKeep` blocks back in history is downloaded.

The state is then updated to the best headers height. If `State.bestHeader` equals `History.bestHeader`, no action is taken as the state is already updated. If `VerifyTransactions` is false, the state root hash is simply updated to the best header in history. If `VerifyTransactions` is true, transaction ids are requested from all headers without transactions, and transaction processing continues as described in the original text.

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

## Bootstrapping

Bootstrapping is the initial setup process that prepares the node for transaction processing. It involves two main steps: 

1. **Downloading Headers**: The process depends on the `PoPoWBootstrap` parameter. If *true*, the node sends a `GetPoPoWProof` request to peers. Upon receiving the `PoPoWProof`, it applies it to the History component. If *false*, the node updates the headers chain to the best known chain in the network using the standard synchronization process.

2. **Downloading Initial State**: The system checks the `ADState` and `BlocksToKeep` settings to determine how to initialize the state. 
    - If `ADState` is *true*, the state is initialized with the state root hash from the header of the block `BlocksToKeep` blocks ago. 
    - If `BlocksToKeep` is less than 0 (meaning keep all blocks) or greater than the current known header height (`History.headersHeight`), the state is initialized with the genesis state. 
    - Otherwise (for pruned modes with `ADState = false`), the system requests a historical `UTXOSnapshotManifest` corresponding to the state `BlocksToKeep` blocks back. Upon receiving the manifest, it requests each required `UTXOSnapshotChunk` from peers. Received chunks are applied to the State component until the full state snapshot is reconstructed.

After the initial state is downloaded or initialized, it is updated to match the best known header height. Depending on whether `VerifyTransactions` is enabled, this involves either just updating the state root hash or requesting and processing the necessary block transactions and AD proofs to reach the target height, as described previously.

Once the bootstrapping process is complete, the system transitions to regular mode.

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

In regular mode, the system operates two infinite loops in separate threads, each performing a distinct function:

1. **Updating the Headers Chain**: This loop continuously updates the headers chain to match the best in the network.

2. **Downloading and Updating Full Blocks**: This loop is responsible for downloading and updating full blocks as needed.

The specific actions taken within these loops depend on the values of `State.bestHeader`, `History.bestHeader`, and `VerifyTransactions`.

```java
if(State.bestHeader == History.bestHeader) {
    // No action is taken as the state is already updated
} else if(VerifyTransactions == false) {
    // The state root hash is updated to the best header in history
    State.setBestHeader(History.bestHeader)
} else {
    // If the headers chain is better than the full block
    // Request transaction ids from all headers without transactions
    assert(history contains header chain from State.bestHeader to History.bestHeaders)
    History.continuation(from = State.bestHeader, size = ???).get.foreach { header =>
        sendToRandomFullNode(GetTransactionIdsForHeader(header))
        if(ADState == true) sendToRandomFullNode(GetADProofsForHeader(header))
    }
    // On receiving TransactionIdsForHeader
    Mempool.apply(TransactionIdsForHeader)
    TransactionIdsForHeader.filter(txId => !MemPool.contains(txId)).foreach { txId =>
        request transaction with txId
    }
    // On receiving a transaction
    if(Mempool.apply(transaction).isSuccess) {
        // Broadcast INV for this transaction
        Mempool.getHeadersWithAllTransactions { BlockTransactions =>
            // Now we have BlockTransactions
            // Continue with the next step
        }
    }
    // Continue with the process as described in the bootstrap section
}
```

In this mode, the system is continuously updating its state and transactions, ensuring it stays in sync with the network.
