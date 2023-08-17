
# Light Full Node Technical Workflow

The light full node operates by checking all the full blocks or a specified suffix of the full blockchain, depending on the settings. It starts from a trusted pre-genesis digest or a digest within the blockchain.

To obtain a new digest from an old one, the light full node utilizes AD-transformations (authenticated dictionary transformations) block sections that contain batch-proof for UTXO transformations. However, it only stores a single digest and does not retain any transaction data.

For more detailed information, refer to [this paper](https://eprint.iacr.org/2016/994).

**Additional settings:** 

The light full node supports the following additional settings:

- **depth** - from which block in the past to checktransactions (if 0, then go from genesis).
- **additional-checks** - light-full node trusts the previous digest and checks current digest validity by using the previous one as well as AD-transformations.
- **additional-depth** - depth to start additional checks from.

## Workflow Steps

1.  Send **ErgoSyncInfo** message to connected peers.
2.  Get a response with an **INV** message containing the IDs of blocks that are better than the current best block.
3.  Request headers for all the IDs received in step 2.
4.  Upon receiving a header, perform the following checks:

```java
if (History.apply(header).isSuccess) {
    if (localScore != networkScore) {
        GOTO 1
    } else {
        GOTO 5
    }
} else {
    blacklist peer
}
```

5.  Request BlockTransactions and ADProofs starting from the specified BlocksToKeep value in the history. This is done after the node bootstrapping process and involves requesting the last header:

```java
History.lastBestHeaders(BlocksToKeep).foreach { header =>
    send message(GetBlockTransactionsForHeader(header)) to Random full node
    send message(GetAdProofsHeader(header)) to Random full node
}
```

6.  Upon receiving a modifier (BlockTransactions or ADProofs), perform the following checks:

```java
if (History.apply(modifier) == Success(ProgressInfo)) {
    /* TODO if history now contains both ADProofs and BlockTransactions,
    it should return ProgressInfo with both of them. Otherwise,
    it should return an empty ProgressInfo */
    if (State().apply(ProgressInfo) == Success((newState, ADProofs))) {
        if ("mode" == "pruned-full") {
            drop BlockTransactions and ADProofs older than BlocksToKeep
        }
    } else {
        /*Drop Header from history because its transaction sequence is not valid*/
        History.drop(BlockTransactions.headerId)
    }
}
```