# Full-Node Mode

## Overview

A full node stores all the blocks since the genesis block, and a full node checks the proofs of work, linking structure correctness (parent block id, interlink elements), and all the blocks' transactions. 

A full node stores every block forever and keeps a copy of the entire UTXO set in order to be able to validate arbitrary transactions. 

See this section to [setup a full node](install.md)



## Technical Workflow

For the full node regime, the modifiers processing workflow is as follows:

1.  Send **ErgoSyncInfo** message to connected peers.
2.  Get a response with an INV message containing the ids of blocks, better than our best block.
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

On receiving transaction ids from the Header:

```java
transactionIdsForHeader.filter(txId => !MemPool.contains(txId)).foreach { txId =>
    request transaction with txId
}
```

On receiving a transaction:

```java
if(Mempool.apply(transaction).isSuccess) {
    if(!isInitialBootstrapping) Broadcast INV for this transaction
        Mempool.getHeadersWithAllTransactions { BlockTransactions =>
            GOTO 7
    }
}
```

Now we have **BlockTransactions**: all transactions corresponding to some Header

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