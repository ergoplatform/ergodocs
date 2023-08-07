# Node Configuration

The `node{}` configuration section specifies general settings for the node view holder regime. It includes parameters for state type, extra index, block and transaction verification, mining configuration, memory pool management, and more. 

## State Type
```conf
stateType = "utxo"
```
The `stateType` setting sets the type of state the node maintains. Possible options are `utxo`, where the node keeps a full utxo set allowing it to validate arbitrary blocks and generate ADProofs, and `digest`, where the node only keeps the state root hash and validates transactions via ADProofs.

## Extra Index
```conf
extraIndex = false
extraCacheSize = 500
```
The `extraIndex` setting, if set to true, allows the node to store all transactions, boxes, and addresses in an index. `extraCacheSize` sets the number of recently used extra indexes kept in memory.

## Verify Transactions
```conf
verifyTransactions = true
```
If `verifyTransactions` is set to true, the node will download block transactions and verify them. 

## Blocks to Keep
```conf
blocksToKeep = -1
```
The `blocksToKeep` setting defines the number of last blocks to keep with transactions and ADproofs. Only the header will be stored for other blocks.

## PoPoW Bootstrap
```conf
PoPoWBootstrap = false
```
If `PoPoWBootstrap` is set to true, the node will download the Proof of Proof of Work (PoPoW) on node bootstrap.

## Mining
```conf
mining = false
maxTransactionCost = 1000000
maxTransactionSize = 98304 // 96 kb
useExternalMiner = true
internalMinersCount = 1
internalMinerPollingInterval = 500ms
miningPubKeyHex = null
```
These settings determine if you are mining through the node, the maximum transaction cost and size to propagate, whether to use an external miner, the number of internal miner threads to spawn, how frequently to ask for new block candidates, and a dedicated public key for mining rewards.

## Offline Generation
```conf
offlineGeneration = false
```
If `offlineGeneration` is set to true, the node will generate blocks while disconnected from the mainnet.

## Keep Versions
```conf
keepVersions = 200
```
The `keepVersions` setting specifies the number of state snapshots diffs to keep, which defines the maximum rollback depth.

## Acceptable Chain Update Delay
```conf
acceptableChainUpdateDelay = 30m
```
The `acceptableChainUpdateDelay` setting is the acceptable difference between the current time and the timestamp of the latest chain update or best block. It helps to discover syncing issues.

## Memory Pool Configuration
The mempool settings define the maximum number of unconfirmed transactions the node will accept, the interval for re-checking a transaction in the memory pool, the mempool transaction sorting scheme, the number of transactions to rebroadcast at each epoch, and the minimum fee amount for transactions.

## Blacklisted Transactions
```conf
blacklistedTransactions = []
```
The `blacklistedTransactions` setting is a list of hex-encoded identifiers of transactions banned from the memory pool.

## Header Chain Diff
```conf
headerChainDiff = 100
```
The `headerChainDiff` setting defines the number of blocks the node considers to be "close" in time when syncing the header chain.

## Checkpoint
```conf
checkpoint = null
```
The `checkpoint` setting allows you to specify an optional individual checkpoint to skip script validation for performance and memory usage improvements during initial bootstrapping.

## ADProofs

 Suffix Length
```conf
adProofsSuffixLength = 114688 // 112k
```
The `adProofsSuffixLength` setting specifies the length of the `ADProofs` suffix dumped during bootstrapping.

## UTXO Bootstrap
```conf
utxoBootstrap = false
storingUtxoSnapshots = 2
p2pUtxoSnapshots = 2
```
The `utxoBootstrap` setting, if set to true, allows the node to download and apply UTXO set snapshot and full-blocks after that. `storingUtxoSnapshots` sets the number of UTXO set snapshots to store, 0 means that they are not stored at all. `p2pUtxoSnapshots` sets the number of UTXO set snapshots for a height with the same id we need to find in the p2p network in order to start downloading it.

## NiPoPoW Bootstrap
```conf
nipopowBootstrap = false
p2pNipopows = 2
nipopowSuffix = 10
```
The `nipopowBootstrap` setting, if set to true, allows the node to download the Proof of Proof of Work (NiPoPoW) on node bootstrap. `p2pNipopows` sets the number of different proofs we are downloading from other peers and comparing with each other, before choosing the best one. `nipopowSuffix` sets the minimal suffix size for NiPoPoW proof.