
### node 

`node{}` specifies general settings for the node view holder regime. 

See papers.yellow.ModifiersProcessing.md

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

Maximum size of a transaction to be accepted into the memory pool.

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

How frequently to ask for new block candidates.

#### miningPubKeyHex

```
miningPubKeyHex = null
```

This variable will dedicate public key mining rewards (P2PK address is also accepted)



#### offlineGeneration
```
offlineGeneration = false
```

If true, the node will generate blocks while disconnected from the ergo mainnet. The only useful case for this is when you want to launch your own blockchain. See the [testnet](testnet.md) page for more information.

#### keepVersions
```
keepVersions = 200
```

The number of state snapshots diffs to keep, which defines the maximum rollback depth.

#### acceptableChainUpdateDelay
```
acceptableChainUpdateDelay = 30m
```
The acceptable difference between NOW and the timestamp of the latest chain update or best block. (Helps to discover syncing issues.)

> TODO: The 'acceptable difference' between the current time and the timestamp of the latest chain update (or best block). This helps to discover syncing issues. 

#### mempoolCapacity
```
mempoolCapacity = 1000
```

`mempoolCapacity` specifies the maximum number of unconfirmed transactions the node will accept.

#### mempoolCleanupDuration
```
mempoolCleanupDuration = 30m
```

The interval for the *re-check* of a transaction in the memory pool. The transaction is initially checked when it enters the memory pool and then again at the specified interval.

#### mempoolSorting
```
mempoolSorting = "random"
```

Specify the mempool transaction sorting scheme. The three options available are; 

- `random`
- `bySize`
- `byExecutionCost`


#### rebroadcastCount
```
rebroadcastCount = 3
```

The number of transactions currently in the mempool that are to be re-broadcasted at each epoch.

#### minimalFeeAmount
```
minimalFeeAmount = 1000000
```

The minimal fee amount for transactions that the memory pool will accept.

#### blacklistedTransactions

```
blacklistedTransactions = []
```

List with hex-encoded identifiers of transactions banned from the memory pool.


#### headerChainDiff

```conf
# default value is 100 blocks ~= 200 minutes
headerChainDiff = 100
```

The node downloads the headers first before moving on to full blocks. Depending on the settings specified by the user, the node downloads a *suffix* of the blockchain (if [stateType](#statetype) = "digest" and ["blocksToKeep"](#blockstokeep) >= 0) or all the full blocks (otherwise).

The node considers the headers-chain synced if it sees a block's header generated closer to the current moment. The node considers that a header is "close" if its timestamp is no more than `headerChainDiff` blocks on average ahead of the node's clocks.


#### checkpoint


```conf
checkpoint = null
```

You can specify an optional and individual checkpoint. If you want to use this, set the `height` and corresponding block header id as such;

```
checkpoint = {
    height = 703848
    blockId = "ed64513030a0396f492385410ba643bb24ca69f0a72b83c9bae8f04d1fa9c5cd"
}
```
   
- Before (and including) the height given, validation of scripts is missed.
- This improves performance and memory usage during initial bootstrapping.
- The node still applies transactions to the UTXO set and checks UTXO set digests for each block.
- Block at checkpoint height are checked against the expected height.
    

#### adProofsSuffixLength

Only dump the `ADProofs` for this suffix length given during bootstrapping.


```
adProofsSuffixLength = 114688 // 112k
```

