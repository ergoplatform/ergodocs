
# Light Full-Node Mode

## Overview 

This mode uses a 2-party authenticated dynamic dictionary built on top of the UTXO set. A light-fullnode only holds the root digest of the dictionary and checks full blocks or a suffix of the blockchain, depending on the setting. It uses AD-transformations to get a new digest from an old one and checks all transactions, but only stores a single digest.

## Getting Started


It's possible to run the node in this *light mode* by changing the the `stateType` variable. 

- `digest`
- `utxo` (default)

Mainnet `ergo.conf` for a **light node** (no UTXO, checking and storing only last 2880 blocks) 

The `blocksToKeep` variable allows you to specify how many of the previous blocks you want to store. 

```
ergo {
  node {
    stateType = "digest"
    blocksToKeep = 2880
    mining = false
  }


}

scorex {

 restApi {
    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
    apiKeyHash = "6ed54addddaf10fe8fcda330bd443a57914fbce38a9fa27248b07e361cc76a41"
  }
}
```


## Technical Workflow

It checks all the full blocks, or some suffix of the full blockchain, depending on the setting, thus starting from a trusted pre-genesis digest or some digest in the blockchain.

A light-fullnode uses AD-transformations (authenticated dictionary transformations) block section containing batch-proof for UTXO transformations to get a new digest from an old one. It also checks all the transactions but does not store anything but a single digest. 

Details can be found in [this paper](https://eprint.iacr.org/2016/994).

**Additional settings:** 

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