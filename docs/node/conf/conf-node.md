
### node 

Settings for node view holder regime. See papers.yellow.ModifiersProcessing.md

#### stateType
```
stateType = "utxo"
```

Sets the *state type*. The possible options are:

- `utxo` - keep full utxo set, which allows you to validate arbitrary blocks and generate ADProofs
- `digest` - keep state root hash only and validate transactions via ADProofs


#### verifyTransactions
```
verifyTransactions = true
```

Download block transactions and verify them (requires `BlocksToKeep == 0` if disabled)

#### blocksToKeep
```
blocksToKeep = -1
```

The number of last blocks to keep with transactions and ADproofs; only the header will be stored for all other blocks.

- Keep all blocks from genesis if negative.
- Please do not set above `114,688` (which corresponds to the default [`adProofsSuffixLength`](#adproofssuffixlength); otherwise, finding proofs around the peers could be hard.

#### PoPoWBootstrap
```
PoPoWBootstrap = false
```

Download the *PoPoW proof* (Proof of Proof of Work) on node bootstrap

#### minimalSuffix
```
minimalSuffix = 10
```

Minimal suffix size for PoPoW proof (maybe pre-defined constant or settings parameter)

#### mining
```
mining = false
```

If you are mining through the node. 


#### maxTransactionCost
```
maxTransactionCost = 1000000
```

The maximum a transaction can cost for it to be propagated. 

#### maxTransactionSize
```
maxTransactionSize = 98304 // 96 kb
```

Maximum size of a transaction to be accepted into mempool.

#### useExternalMiner
```
useExternalMiner = true
```

Use external miner; native miner is used if set to `false.`

#### internalMinersCount
```
internalMinersCount = 1
```
How many internal miner threads to spawn (used mainly for testing)

#### internalMinerPollingInterval
```
internalMinerPollingInterval = 500ms
```

How frequently to ask for new block candidate.

#### miningPubKeyHex

```
miningPubKeyHex = null
```

Public key mining rewards will be dedicated to (P2PK address is also accepted)



#### offlineGeneration
```
offlineGeneration = false
```

If true, a node generates blocks being offline. The only really useful case for it is to start a new blockchain.

#### keepVersions
```
keepVersions = 200
```

The number of state snapshots diffs to keep. Defines maximum rollback depth

#### acceptableChainUpdateDelay
```
acceptableChainUpdateDelay = 30m
```
The acceptable difference between NOW and the timestamp of the latest chain update or best block. This helps to discover syncing issues.

#### mempoolCapacity
```
mempoolCapacity = 1000
```

`mempoolCapacity` specifies the maximum number of unconfirmed transactions the node will accept.

#### mempoolCleanupDuration
```
mempoolCleanupDuration = 30m
```

Interval for mempool transaction re-check. We check the transaction when it enters the mempool and then re-check it for every interval value.

#### mempoolSorting
```
mempoolSorting = "random"
```

Mempool transaction sorting scheme ("random", "bySize", or "byExecutionCost")

#### rebroadcastCount
```
rebroadcastCount = 3
```

Number of transactions from mempool to be re-broadcasted at each epoch

#### minimalFeeAmount
```
minimalFeeAmount = 1000000
```

Minimal fee amount of transactions mempool accepts.

#### blacklistedTransactions

```
blacklistedTransactions = []
```

List with hex-encoded identifiers of transactions banned from getting into the memory pool.


#### headerChainDiff

```conf
# default value is 100 blocks ~= 200 minutes
headerChainDiff = 100
```
The node is downloading headers first and only then full blocks. Depending on the settings, the node is downloading whether a suffix of the blockchain (if stateType = "digest" and "blocksToKeep" >= 0) or all the full blocks (otherwise).

The node considers that the headers-chain is synced if it sees a block's header generated closely to the current moment. The node considers that a header is close if its timestamp is no more than "headerChainDiff" blocks on average than the node's clocks.


#### checkpoint


```conf
checkpoint = null
```

Optional and individual checkpoint. If you are going to provide it, set the height and corresponding block header id like

```
checkpoint = {
    height = 703848
    blockId = "ed64513030a0396f492385410ba643bb24ca69f0a72b83c9bae8f04d1fa9c5cd"
}
```
   
- Before the height given (including it), validation of scripts is missed.
- This improves performance and memory usage during initial bootstrapping.
- The node still applies transactions to the UTXO set and checks UTXO set digests for each block.
- Block at checkpoint height is to be checked against the expected one.
    

#### adProofsSuffixLength

Dump `ADProofs` only for the suffix given during bootstrapping


```
adProofsSuffixLength = 114688 // 112k
```

