# Full Archival Node Technical Workflow

This document outlines the technical workflow for the full archival node mode in Ergo. The process is as follows:

1. Send an **ErgoSyncInfo** message to connected peers.
2. Receive a response with an INV message containing the IDs of blocks that are better than our best block.
3. Request headers for all the block IDs received in step 2.

Upon receiving a header, the following operations are performed:


```java
if(history.apply(header).isSuccess) {
    if(!isInitialBootstrapping) Broadcast INV for this Header
    Request transaction ids from this block
    } else {
    blacklist peer
    }
```


When transaction IDs from the Header are received, the following operations are performed:

```java
transactionIdsForHeader.filter(txId => !MemPool.contains(txId)).foreach { txId =>
    request transaction with txId
}
```

Upon receiving a transaction, the following operations are performed:

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
For more information, please refer to the [Bootstrapping section of modifiers processing](modifiers-processing.md#bootstrapping).
