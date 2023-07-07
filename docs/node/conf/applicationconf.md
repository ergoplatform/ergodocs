# application.conf
Please refer to [conf](conf.md)

<!--[View code on GitHub](https://raw.githubusercontent.com/ergoplatform/ergo/master/src/main/resources/application.conf)

The code in this file is responsible for configuring various settings for the Ergo project. It covers settings related to the node, wallet, network, and caching. The node settings include options for state type, transaction verification, block storage, mining, and mempool management. The wallet settings cover secret storage, seed strength, mnemonic phrase language, and transaction fee management. The network settings handle connection management, peer discovery, and synchronization. The cache settings optimize memory usage for various components.

For example, in the node settings, `stateType` can be set to "utxo" or "digest" to determine how the node maintains its state. The `verifyTransactions` setting enables or disables transaction verification. The `blocksToKeep` setting determines how many blocks with transactions and ADproofs are stored.

In the wallet settings, `seedStrengthBits` determines the strength of the generated seed, and `mnemonicPhraseLanguage` sets the language for the mnemonic seed. The `defaultTransactionFee` sets the fee used when it's not specified in a transaction.

In the network settings, `knownPeers` is a list of well-known nodes to connect to, and `maxConnections` sets the maximum number of network connections. The `syncInterval` and `syncTimeout` settings control the synchronization process.

In the cache settings, various cache sizes are defined for different components, such as `blockSectionsCacheSize` for block sections and `headersCacheSize` for headers.

These configurations allow the Ergo project to be fine-tuned for different use cases and environments, ensuring optimal performance and resource usage.


## ergo

### node 

Settings for node view holder regime. See papers.yellow.ModifiersProcessing.md

#### stateType
```conf
stateType = "utxo"
```

State type.  Possible options are:

- "utxo" - keep full utxo set, that allows to validate arbitrary block and generate ADProofs
- "digest" - keep state root hash only and validate transactions via ADProofs


#### verifyTransactions
```conf
verifyTransactions = true
```

Download block transactions and verify them (requires BlocksToKeep == 0 if disabled)

#### blocksToKeep

```conf
blocksToKeep = -1
```

Number of last blocks to keep with transactions and ADproofs, for all other blocks only the header will be stored.

Keep all blocks from genesis if negative
Please do not set it more than 114,688 (default adProofsSuffixLength), otherwise, it could be hard to find proofs around the peers


### utxoBootstrap

```conf
# Download and apply UTXO set snapshot and full-blocks after that
utxoBootstrap = false
```

#### PoPoWBootstrap
```conf
PoPoWBootstrap = false
```

Download PoPoW proof on node bootstrap

#### minimalSuffix
```conf
minimalSuffix = 10
```

Minimal suffix size for PoPoW proof (may be pre-defined constant or settings parameter)

#### mining
```conf
mining = false
```

Is the node is doing mining


#### maxTransactionCost
```conf
maxTransactionCost = 1000000
```

maximum cost of transaction for it to be propagated
#### maxTransactionSize
```conf
maxTransactionSize = 98304 // 96 kb
```

Maximum size of transaction to be accepted into mempool

#### useExternalMiner
```conf
useExternalMiner = true
```

Use external miner, native miner is used if set to `false`

#### internalMinersCount
```conf
internalMinersCount = 1
```
How many internal miner threads to spawn (used mainly for testing)
#### internalMinerPollingInterval
```conf
internalMinerPollingInterval = 500ms
```

How frequently to ask for new block candidate
#### miningPubKeyHex

```conf
miningPubKeyHex = null
```

Public key mining rewards will be dedicated to (P2PK address is also accepted)



#### offlineGeneration
```conf
offlineGeneration = false
```

If true, a node generates blocks being offline. The only really useful case for it probably is to start a new blockchain

#### keepVersions
```conf
keepVersions = 200
```

Number of state snapshot diffs to keep. Defines maximum rollback depth

#### acceptableChainUpdateDelay
```conf
acceptableChainUpdateDelay = 30m
```
Acceptable difference between NOW and timestamp of the latest chain update or best block. This helps to discover syncing issues.

#### mempoolCapacity

Maximum number of unconfirmed transactions node can accept

```conf
mempoolCapacity = 1000
```
#### mempoolCleanupDuration
```conf
mempoolCleanupDuration = 30m
```

Interval for mempool transaction re-check. We check transaction when it is entering the mempool, and then re-check it every interval valie

#### mempoolSorting
```conf
mempoolSorting = "random"
```

Mempool transaction sorting scheme ("random", "bySize", or "byExecutionCost")

#### rebroadcastCount
```conf
rebroadcastCount = 3
```

Number of transactions from mempool to be re-broadcasted at each epoch

#### minimalFeeAmount
```conf
minimalFeeAmount = 1000000
```

Minimal fee amount of transactions mempool accepts

#### blacklistedTransactions

```conf
blacklistedTransactions = []
```

List with hex-encoded identifiers of transactions banned from getting into memory pool


#### headerChainDiff

```conf
# default value is 100 blocks ~= 200 minutes
headerChainDiff = 100
```
The node is downloading headers first and only then full blocks. Depending on settings, the node is downloading whether a suffix of the blockchain (if stateType = "digest" and "blocksToKeep" >= 0) or all the full blocks (otherwise).

The node is considering that the headers-chain is synced if it sees a header of a block generated closely to the current moment. The node considers that a header is close if its timestamp is no more than "headerChainDiff" blocks on average than node's clocks.


#### checkpoint


```conf
checkpoint = null
```

Optional and individual checkpoint. If you going to provide it , set height and corresponding block header id like

```
checkpoint = {
    height = 703848
    blockId = "ed64513030a0396f492385410ba643bb24ca69f0a72b83c9bae8f04d1fa9c5cd"
}
```
   
- Before the height given (including it) validation of scripts is missed.
- This improving perfomance and memory usage during initial bootstrapping.
- The node still applying transactions to UTXO set and so checks UTXO set digests for each block.
- Block at checkpoint height is to be checked against expected one.
    

#### adProofsSuffixLength

Dump `ADProofs` only for the suffix given during bootstrapping


```conf
adProofsSuffixLength = 114688 // 112k
```


### cache 

What to keep in memory

#### history
##### blockSectionsCacheSize
```conf
blockSectionsCacheSize = 12
```
Number of recently used block sections that will be kept in memory
##### headersCacheSize
```conf
headersCacheSize = 1000
```
Number of recently used headers that will be kept in memory
##### indexesCacheSize
```conf
indexesCacheSize = 10000
```
Number of recently used indexes that will be kept in memory
#### network
##### invalidModifiersBloomFilterCapacity
```conf
invalidModifiersBloomFilterCapacity = 10000000
```
Maximum number of invalid modifiers to keep in DeliveryTracker

##### invalidModifiersBloomFilterExpirationRate
```
invalidModifiersBloomFilterExpirationRate = 0.1
```
Non-zero fraction of 1 as a rate of element expiration when capacity is full, the lower the more gradual expiration.
example : 0.1 is represented as 10 bloom filters expiring one by one

##### invalidModifiersCacheSize
```
invalidModifiersCacheSize = 10000
```
Maximum number of invalid modifiers to keep in cache, following modifiers are kept in bloom filters

##### invalidModifiersCacheExpiration
```
invalidModifiersCacheExpiration = 6h
```

For how long to keep invalid modifiers in cache

#### mempool
##### invalidModifiersBloomFilterCapacity
```
invalidModifiersBloomFilterCapacity = 10000000
```
Maximum number of invalid modifiers to keep in DeliveryTracker

##### invalidModifiersBloomFilterExpirationRate
```
invalidModifiersBloomFilterExpirationRate = 0.1
```
Non-zero fraction of 1 as a rate of element expiration when capacity is full, the lower the more gradual expiration.
example : 0.1 is represented as 10 bloom filters expiring one by one

##### invalidModifiersCacheSize
```
invalidModifiersCacheSize = 10000
```
Maximum number of invalid modifiers to keep in cache, following modifiers are kept in bloom filters

##### invalidModifiersCacheExpiration
```
invalidModifiersCacheExpiration = 6h
```

For how long to keep invalid modifiers in cache

### chain 

Chain-specific settings. Change only if you are going to launch a new chain 

#### protocolVersion
```
protocolVersion = 3
```

Blockchain protocol version supported by the client.

Please do not increase this value manually, this should be done by client developers.

#### addressPrefix 
```
addressPrefix = 16
```
Network address prefix, currently reserved values are 0 (Ergo mainnet) and 16 (Ergo testnet)

#### monetary
##### fixedRatePeriod
```
fixedRatePeriod = 525600
```
The number of blocks reward won't change (2 years)

##### fixedRate
```
fixedRate = 75000000000
```
number of coins issued every block during fixedRatePeriod (75 Ergo)
##### foundersInitialReward
```
foundersInitialReward = 7500000000
```

Part of coins issued, that is going to the foundation during fixedRatePeriod (7.5 Ergo)


##### epochLength

```
epochLength = 64800
```
number of blocks between reward reduction (90 days)

##### oneEpochReduction

```
oneEpochReduction = 3000000000
```

The number of coins reward decreases every epochs (3 Ergo)


##### minerRewardDelay
```
minerRewardDelay = 720
```
The delay between when a block is mined and when the reward can be spent. (720 blocks == ~1 day).

#### reemission

##### checkReemissionRules

```
checkReemissionRules = false
```
##### emissionNftId
```
emissionNftId = ""
```
##### reemissionTokenId
```
reemissionTokenId = ""
```
##### reemissionNftId
```
reemissionNftId = ""
```
##### activationHeight
```
activationHeight = 777217
```

##### reemissionStartHeight
```
reemissionStartHeight = 2080800
```
##### injectionBoxBytesEncoded
```
injectionBoxBytesEncoded = ""
```
#### noPremineProof
```
noPremineProof = [
      "'Chaos reigns': what the papers say about the no-deal Brexit vote", # https://www.theguardian.com/politics/2019/mar/14/chaos-reigns-what-the-papers-say-about-the-no-deal-brexit-vote
      "习近平的两会时间|这里有份习近平两会日历，请查收！", # http://www.xinhuanet.com/politics/2019lh/2019-03/13/c_1124232018.htm
      "ТАСС сообщил об обнаружении нескольких майнинговых ферм на столичных рынках", # https://www.vedomosti.ru/politics/news/2019/03/14/796376-mainingovih-ferm
      "000000000000000000139a3e61bd5721827b51a5309a8bfeca0b8c4b5c060931", # https://www.blockchain.com/btc/block/000000000000000000139a3e61bd5721827b51a5309a8bfeca0b8c4b5c060931
      "0xef1d584d77e74e3c509de625dc17893b22b73d040b5d5302bbf832065f928d03" # https://etherscan.io/block/0xef1d584d77e74e3c509de625dc17893b22b73d040b5d5302bbf832065f928d03
    ]
```

Latest news from media (the Guardian, Xinhua, Vedomosti), existing cryptocurrency block ids (Bitcoin, Ethereum)


####  foundersPubkeys 
```
 foundersPubkeys = [
      "039bb5fe52359a64c99a60fd944fc5e388cbdc4d37ff091cc841c3ee79060b8647",
      "031fb52cf6e805f80d97cde289f4f757d49accf0c83fb864b27d2cf982c37f9a8b",
      "0352ac2a471339b0d23b3d2c5ce0db0e81c969f77891b9edf0bda7fd39a78184e7"
    ]
```

Public keys of founders, represented as just group elements
   

### wallet 
#### secretStorage
##### secretDir
```
secretDir = ${ergo.directory}"/wallet/keystore"
```
##### encryption
###### prf
```
prf = "HmacSHA256"
```

Pseudo-random function with output of length `dkLen` (PBKDF2 param)

###### c
```
c = 128000
```
Number of PBKDF2 iterations (PBKDF2 param)
###### dkLen
```
dkLen = 256
```

Desired bit-length of the derived key (PBKDF2 param)
#### seedStrengthBits
```
seedStrengthBits = 160
```

Generating seed length in bits
Options: 128, 160, 192, 224, 256


#### mnemonicPhraseLanguage
```
mnemonicPhraseLanguage = "english"
```

Language to be used in mnemonic seed

Options: "chinese_simplified", "chinese_traditional", "english", "french", "italian", "japanese", "korean", "spanish"


#### keepSpentBoxes
```
keepSpentBoxes = false
```
Save used boxes (may consume additional disk space) or delete them immediately
#### defaultTransactionFee

```
defaultTransactionFee = 1000000
```

Default fee wallet is using when the fee is not specified

#### usePreEip3Derivation
```
usePreEip3Derivation = false
```

Use pre-EIP3 key derivation scheme

#### dustLimit
```
dustLimit = null
```
#### maxInputs
```
maxInputs = 100
```

#### optimalInputs
```
optimalInputs = 3
```
#### testMnemonic
```
# testMnemonic = "ozone drill grab fiber curtain grace pudding thank cruise elder eight picnic"
```
Mnemonic seed used in wallet for tests. If set the wallet operates in test mode.

#### testKeysQty
```
# testKeysQty = 5
```
Number of keys to be generated for tests

#### tokensWhitelist
```
tokensWhitelist = null
```

Whitelisted tokens, if non-null, the wallet will automatically burn non-whitelisted tokens from inputs when doing transactions.

If tokensWhitelist = [], all the tokens will be burnt, tokensWhitelist = ["example"] means that all the tokens except of "example" will be burnt

tokensWhitelist = null means no tokens burnt automatically
#### checkEIP27
```
checkEIP27 = false
```
Enable this setting to handle re-emission tokens in the wallet properly,
e.g. doing transfers correctly in the presence of re-emission tokens
#### profile
```
profile = "user"
```

Wallet profile allows to say wallet what kind of load it should expect, and so spend memory on caches and Bloom filters accordingly.

There are three options: user, exchange, appServer

User profile is about ordinary planned usage.

Exchange consumes ~20 MB of RAM for high-load ready Bloom filters

AppServer is in between

### voting 
```
"rulesToDisable" = []
```

Example: storage fee factor id = 1, target value = 1000000
`1 = 1000000`


A vote for soft-fork. [protocolVersion](#protocolversion) must be one announced in a block header increased by one also, and then the node will automatically propose a soft-fork (in the beginning of an epoch),  or vote for it.

Put any non-zero value here to vote for soft-fork, or zero to vote against.

`120 = 0`

Put an array of rules to deactivate with the soft-fork

## bounded-mailbox 

### mailbox-type
```
mailbox-type = "akka.dispatch.NonBlockingBoundedMailbox"
```

### mailbox-capacity
```
mailbox-capacity = 5000
```

## akka 
### actor.mailbox.requirements
### http
```
http {
    server {
      request-timeout = 1 minute
      max-connections = 128
    }
    parsing {
      max-uri-length = 8192
    }
  }
```
#### server
##### request-timeout
```
request-timeout = 1 minute
```
##### max-connections
```
max-connections = 128
```
#### parsing
##### max-uri-length
```
max-uri-length = 8192
```



## dataDir & logDir

```
  # Node data directory
  dataDir = ${user.home}"/scorex"
  # Node logs directory
  logDir = ${scorex.dataDir}"/log"

  logging {
    level = "INFO"
  }
```

## scorex 

### executionContext

Execution context used in tests

```conf
executionContext {
    type = Dispatcher
    executor = "thread-pool-executor"
    thread-pool-executor {
      fixed-pool-size = 16
    }
    throughput = 1
  }
```

### restApi

Node's REST API settings

#### bindAddress
#### apiKeyHash
#### corsAllowedOrigin
#### timeout
#### publicUrl

```
# Node's REST API settings
  restApi {
    # Network address to bind to
    bindAddress = "0.0.0.0:9052"

    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
    # Below is the hash of "hello" string.
    # Change it!
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"

    # Enable/disable CORS support.
    # This is an optional param. It would allow cors in case if this setting is set.
    # If this setting will be omitted cors will be prohibited.
    corsAllowedOrigin = "*"

    # request processing timeout
    timeout = 5s

    # node which exposes restApi in firewall should define publicly accessible URL of it
    # publicUrl = "https://example.com:80"
  }
```

### network

P2P Network settings

##### nodeName
##### appVersion
##### agentName
##### bindAddress
##### magicBytes
##### declaredAddress
##### upnpEnabled
##### localOnly


##### upnp-gateway-timeout
```
upnp-gateway-timeout = 7s
```
##### upnp-discover-timeout 
```
upnp-discover-timeout = 3s
```
Add delay for sending message

##### addedMaxDelay
```
addedMaxDelay = 0ms
```
##### Peers Settings
###### handshakeTimeout
###### knownPeers
###### getPeersInterval
###### maxConnections
###### connectionTimeout
###### peerEvictionInterval

##### Delivery Settings Limits

###### deliveryTimeout
###### maxDeliveryChecks

##### Timeouts

###### inactiveConnectionDeadline
###### syncInterval
###### syncIntervalStable
   

   
###### syncTimeout 

###### syncStatusRefresh

###### syncStatusRefreshStable
###### syncIntervalStable

###### controllerTimeout 
    Network controller timeout

##### Size limits 

###### desiredInvObjects = 400
    # Desired number of inv objects. Our requests will have this size.

    # How many persistent modifiers to store in the cache.
    # The cache stores modifiers that are waiting to be applied.
    maxModifiersCacheSize = 1024

    # Maximum number of PeerSpec objects in one Peers message
    maxPeerSpecObjects = 64

    # Default ban duration, unless permanent penalty is applied
    temporalBanDuration = 60m

    # Misbehaving peer penalty score will not be increased withing this time interval,
    # unless permanent penalty is applied
    penaltySafeInterval = 2m

    # Max penalty score peer can accumulate before being banned
    penaltyScoreThreshold = 500

    # If set (and it is set by default), the node will try to discover peers in the network.
    # If set to false, the node will use only peers from database
    # (with fallback to knownPeers config section if no peers there)
    peerDiscovery = true

```
network {

    #####################################################
    # Node information to be declared during handshake  #
    #####################################################

    # Node name to send during handshake
    nodeName = "ergo-node"

    # Network protocol version to be sent in handshakes
    appVersion = 5.0.1

    # Network agent name. May contain information about client code
    # stack, starting from core code-base up to the end graphical interface.
    # Basic format is `/Name:Version(comments)/Name:Version/.../`,
    # e.g. `/Ergo-Scala-client:2.0.0(iPad; U; CPU OS 3_2_1)/AndroidBuild:0.8/`
    agentName = "ergoref"

    # Network address
    bindAddress = "0.0.0.0:9022"

    ########################
    # Connection settings  #
    ########################

    # Magic bytes, that will be added to every p2p message to allow
    # distinguish different networks (e.g. testnet/mainnet).
    magicBytes = [2, 2, 2, 2]

    # String with IP address and port to send as external address during handshake.
    # Could be set automatically if UPnP is enabled.
    #
    # If `declared-address` is set, which is the common scenario for nodes running in the cloud,
    # the node will just listen to incoming connections on `bindAddress:port` and
    # broadcast its `declaredAddress` to its peers.
    # UPnP is supposed to be disabled in this scenario.
    #
    # If declared address is not set and UPnP is not enabled, the node will not listen to incoming connections at all.
    #
    # If declared address is not set and UPnP is enabled, the node will attempt to connect to an IGD, retrieve its
    # external IP address and configure the gateway to allow traffic through. If the node succeeds, the IGD's external
    # IP address becomes the node's declared address.
    #
    # In some cases, you may both set `decalredAddress` and enable UPnP (e.g. when IGD can't reliably determine its
    # external IP address). In such cases the node will attempt to configure an IGD to pass traffic from external port
    # to `bind-address:port`. Please note, however, that this setup is not recommended.
    # declaredAddress = ""

    # Enable UPnP tunnel creation only if you router/gateway supports it. Useful if your node is running in home
    # network. Completely useless if you node is in cloud.
    upnpEnabled = no

    # Accept only local connections
    localOnly = false

    # UPnP timeouts
    # upnp-gateway-timeout = 7s
    # upnp-discover-timeout = 3s

    # Add delay for sending message
    # addedMaxDelay = 0ms

    ##################
    # Peers settings #
    ##################

    # Network handshake timeout
    handshakeTimeout = 30s

    # A list of `IP:port` pairs of well known nodes.
    knownPeers = []

    # Interval between GetPeers messages to be send by our node to a random one
    getPeersInterval = 2m

    # Number of network connections
    maxConnections = 30

    # Network connection timeout
    connectionTimeout = 1s

    # interval of evicting random peer to avoid eclipsing
    peerEvictionInterval = 1h

    ############################
    # Delivery settings limits #
    ############################

    # Network delivery timeout
    deliveryTimeout = 10s

    # Max number of delivery checks. Stop expecting modifier if it was not delivered after that
    # number of delivery attempts. The node tries to ask different peers on different attempts, and
    # not increasing the delivery counter if global loss of connectivity is possible
    maxDeliveryChecks = 100

    ############
    # Timeouts #
    ############

    # Timeout for dropping dead connections
    inactiveConnectionDeadline = 10m

    # Interval between `SyncInfo` messages when our node is not synchronized yet
    syncInterval = 5s

    # Interval between `SyncInfo` messages when our node is already synchronized
    syncIntervalStable = 15s

    # Synchronization timeout
    syncTimeout = 10s

    # Synchronization status update interval
    syncStatusRefresh = 60s

    syncStatusRefreshStable = 90s

    # Synchronization status update interval for stable regime
    syncIntervalStable = 30s

    # Network controller timeout
    controllerTimeout = 5s

    ###############
    # Size limits #
    ###############

    # Desired number of inv objects. Our requests will have this size.
    desiredInvObjects = 400

    # How many persistent modifiers to store in the cache.
    # The cache stores modifiers that are waiting to be applied.
    maxModifiersCacheSize = 1024

    # Maximum number of PeerSpec objects in one Peers message
    maxPeerSpecObjects = 64

    # Default ban duration, unless permanent penalty is applied
    temporalBanDuration = 60m

    # Misbehaving peer penalty score will not be increased withing this time interval,
    # unless permanent penalty is applied
    penaltySafeInterval = 2m

    # Max penalty score peer can accumulate before being banned
    penaltyScoreThreshold = 500

    # If set (and it is set by default), the node will try to discover peers in the network.
    # If set to false, the node will use only peers from database
    # (with fallback to knownPeers config section if no peers there)
    peerDiscovery = true
  }
```

## critical-dispatcher 
```
critical-dispatcher {
  type = Dispatcher
  executor = "thread-pool-executor"
  thread-pool-executor {
    fixed-pool-size = 2
  }
  throughput = 1
}
```
The dispatcher which is used for block candidate generator and `NodeViewHolder` actors only



-->