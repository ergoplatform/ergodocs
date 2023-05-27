
# Node Config File

Please see [conf](conf.md)

<!-- !!!Note!!! This guide is outdated and should be actualized to current config format

### Actual for version 1.6.1

Below you can find a complete Ergo Node configuration file. This is the default configuration shipped with the application.
It is possible to overwrite any parameters by providing an additional configuration file. You can pass an additional configuration file
by providing the path to it as the first command line parameter when starting Ergo Node application.

```bash
ergo {
  # Directory to keep data
  directory = ${user.dir}"/ergo/data"

  # Settings for node view holder regime. See papers.yellow.ModifiersProcessing.md
  node {
    # State type.  Possible options are:
    # "utxo" - keep full utxo set, that allows to validate arbitrary block and generate ADProofs
    # "digest" - keep state root hash only and validate transactions via ADProofs
    stateType = "utxo"

    # Download block transactions and verify them (requires BlocksToKeep == 0 if disabled)
    verifyTransactions = true

    # Number of last blocks to keep with transactions and ADproofs, for all other blocks only header will be stored.
    # Keep all blocks from genesis if negative
    blocksToKeep = -1

    # Download PoPoW proof on node bootstrap
    PoPoWBootstrap = false

    # Minimal suffix size for PoPoW proof (may be pre-defined constant or settings parameter)
    minimalSuffix = 10

    # Is the node is doing mining
    mining = false

    # If true, a node generates blocks being offline. The only really useful case for it probably is to start a new
    # blockchain
    offlineGeneration = false

    # Delay for miner after succesful block creation
    miningDelay = 5s

    # Number of state snapshot diffs to keep. Defines maximum rollback depth
    keepVersions = 200
  }

  testing {
    # Whether to turn on transaction generator
    transactionGeneration = false

    # Max number of transactions generated per a new block received
    maxTransactionsPerBlock = 100
  }

  cache {
    # Number of recently used modifiers that will be kept in memory
    modifiersCacheSize = 1000

    # Number of recently used indexes that will be kept in memory
    indexesCacheSize = 10000
  }

  # Chain-specific settings. Change only if you are going to launch a new chain!
  chain {
    # Network address prefix, currently reserved values are 0x00 (money chain mainnet) and 0x20 (32 in decimal,
    # money chain testnet)
    addressPrefix = 16

    # Monetary config for chain
    monetary {
      # number of blocks reward won't change (525600 (2 years) for mainnet, 10080 (14 days) for testnet)
      fixedRatePeriod = 10080
      # number of coins issued every block during fixedRatePeriod (75 Ergo)
      fixedRate = 7500000000
      # number of blocks between reward reduction (64800 (90 days) for mainnet, 2160 (3 days) for testnet)
      epochLength = 2160
      # number of coins reward decrease every epochs (3 Ergo)
      oneEpochReduction = 300000000
      # Base16 representation of state roothash after genesis
      afterGenesisStateDigestHex = "a8f724cef6f8a247a63fba1b713def858d97258f7cd5d7ed71489a474790db5501"
    }

    # Desired time interval between blocks
    blockInterval = 2m

    # length of an epoch in difficulty recalculation. 1 means difficulty recalculation every block
    epochLength = 256

    # Number of last epochs that will  be used for difficulty recalculation
    useLastEpochs = 8

    # Proof-of-Work algorithm and its parameters. Possible options are "fake" and "equihash".
    powScheme {
      powType = "equihash"
      n = 96 # used by Equihash
      k = 5  # used by Equihash
    }

    # Defines an id of the genesis block. Other genesis blocks will be considered invalid.
    # genesisId = "ab19bb59871e86507defb9a7769841b1130aad4d8c1ea8b0e01e0dee9e97a27e"
  }

  wallet {
    # Seed the wallet private keys are derived from
    seed = "C3FAFMC27697FAF29E9887F977BB5994"

    # How many Schorr secret keys (w for the g^w public key) to generate
    dlogSecretsNumber = 4

    # Interval to re-scan uncertain boxes. When a block arrives, its transaction outputs are to be scanned, and if
    # certain bytes are found in the output script (e.g. public key bytes), the box is to be put to a queue of a boxes
    # which are potentially wallet's. But to be sure, script execution is needed, which could be costly to do in a bulk.
    # So we check from a queue only one box per "scanningInterval".
    scanningInterval = 1s
  }
}
scorex {
  network {
    bindAddress = "0.0.0.0:9006"
    maxInvObjects = 400
    nodeName = "ergo-testnet1"
    knownPeers = ["178.128.162.150:9006", "78.46.93.239:9006", "209.97.136.204:9006", "209.97.138.187:9006", "209.97.134.210:9006", "88.198.13.202:9006"]
    syncInterval = 15s
    syncStatusRefresh = 30s
    syncIntervalStable = 20s
    syncTimeout = 5s
    syncStatusRefreshStable = 1m
    deliveryTimeout = 8s
    maxDeliveryChecks = 2
    appVersion = 0.2.1
    agentName = "ergoref"
    maxModifiersCacheSize = 512
    maxPacketSize = 2048576
  }
  restApi {
    bindAddress = "0.0.0.0:9052"
  }
}
```

### Ergo configuration section

Root configuration section `ergo` holds essential application parameters and other configuration subsections.
There is also another one root section `scorex` that holds the parameters inherited from the [Scorex project](https://github.com/ScorexFoundation/Scorex).

Using parameter `directory` it is possible to set a path to the base application directory.
It is also possible to use environment variables to override configuration parameters.
For example, by default the base directory is being constructed relatively to the user's `HOME` environment variable.
Please do not enclose references to environment variables into quotation marks, otherwise they will be handled as strings and won't be resolved.




### Network settings

In `scorex.network` section P2P network related settings could be set.

Using `declaredAddress` parameter you can set the external IP address and port number of the node. It's necessary to work behind NAT in most cloud hosting, where the machine does not interface directly with the external address. If you do not specify it, then your node connects to the P2P network, but it won't listen to incoming connections so other nodes will not be able to connect. Other nodes are connected to your node using these data. The format of this parameter is "[ip-address]:[port]".

Using parameter `bindAddress` you can set the IP address of local network interface on which Ergo Node will accept incoming connections.
By default, node binds to "0.0.0.0" that means that it will listen on all available network adapters.


**Note about Internet Address settings**

Internet Address settings have `<ip-adderss>:<port>` format.
Note the `<port>` part at the very end of the address after the colon.

For the `bindAddress` setting port part is used to set the network port number to which other Ergo nodes will connect.
Please ensure that the port is reachable from outside, otherwise your node will have only outgoing connections to P2P network.
If the given port is taken by other application, your node won't start.

Parameter `nodeName` could be used to set the name of your node visible to other participants of the P2P network. The name transmitted during initial handshake. In the default configuration, this parameter is commented out, which leads to random name generation.

The `knownPeers` parameter stores the list of bootstrap nodes to which your node will establish outgoing connections while initializing.

**Note about time settings**

All time span parameters are set in milliseconds. You can also use duration units to shorten their values. Supported units are:
* s, second, seconds
* m, minute, minutes
* h, hour, hours
* d, day, days

For usage examples see the default configuration file above.

Use `maxConnections` parameter to set the maximum number of simultaneous connections handled by the node.

Parameter `connectionTimeout` could be used to change the network communication timeout.

Using `handshakeTimeout` parameter it is possible to set time period to wait for reply during handshake. In case of no reply the peer will be blacklisted.

Using parameters that starts with `upnp` you can configure the UPnP settings. Actually, those settings are useful only if you ran your Ergo node on the home network where the node could ask your router to establish a tunnel. By default, this functionality is disabled. Use `upnpEnabled` parameter to enable this functionality.

**Wallet settings**

In `wallet` section you can configure the wallet built in Ergo node.

Use `dlogSecretsNumber` parameter to specify how many Schorr secret keys (w for the g^w public key) to generate.

Use `scanningInterval` parameter to set an interval of re-scaning uncertain boxes.

Using `seed` parameter you could recreate an existing walled on a new node. If you don't have any existing wallet comment out this parameter and start the node. During the first run, the application will create a new wallet with a random seed for you. In this case, the seed will be displayed in the application log.

**Attention!**

The wallet is a critical part of your node. You should better store wallet's file in a safe and protected location. Don't forget to backup your wallet's file.

It's recommended to remove the seed from the configuration file immediately after the start of the node. If an attacker gains access to this seed string, he has access to all your funds on all your addresses!

**Blockchain settings**

At `ergo.chain` you can select or custom the blockchain parameters.

Use `blockInterval` parameter to set desired time interval between blocks.

Parameter `epochLength` used to set the length of an epoch in difficulty recalculation. 1 means difficulty recalculation every block

`useLastEpochs` parameter stores a number of last epochs that will be used for difficulty recalculation.

You can change the PoW algo or related parameters using `powScheme` section.

**Node settings**

In section `ergo.node` it is possible to configure parameters of the node regime.

Use `enable` parameter to enable or disable block generation on the node. By default, it's disabled.

Node with disabled `offlineGeneration` parameter will start mining as soon as it connects to the first peer in the P2P network. Setting this parameter to `true` will enable off-line generation.

Using `miningDelay` parameter you can tune your node's mining delay after finding a new block.


**REST API settings**

In section `scorex.rest-api` you can set the node's REST API parameters.

Parameter `bindAddress` could be used to select network interface on which REST API will accept incoming connections.
The `:<port>` part could be used to change the port number, which REST API will listen for connections.


> **Attention!** For the better security, do not change `bindAddress` from "127.0.0.1" if you do not know what you're doing!
For the external access you should use [Nginx's proxy_pass module](http://nginx.org/ru/docs/http/ngx_http_proxy_module.html) or [SSH port-forwarding](http://blog.trackets.com/2014/05/17/ssh-tunnel-local-and-remote-port-forwarding-explained-with-examples.html) instead.


Use `api-key-hash` parameter to set the hash of your API key. The API key is used to protect calls of critical API methods. Remember, that in this parameter you should provide the hash of API key, but during REST calls you should provide API key itself. You can use blake2b to produce the hash of your API key.



> **Attention!** API key is transmitted in the HTTP header as unprotected plain text! An attacker could intercept it in network transit and use it to transfer your money to any address! So you have to protect the transmission using HTTPS or use SSH port forwarding.


Parameter `corsAllowedOrigin` could be used to enable or disable CORS support in REST API.
CORS allows to safely resolve queries to other domains outside the one running the node.
It's necessary for Swagger and Lite client. You can read about it [here](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing).

# Wallets

## Linux
## Mac
## Windows

`HOME` environment variable is not often set in Windows. Please replace `${HOME}` with `${HOMEPATH}` or `${APPDATA}` in your configuration file.
You should also remember that environment variables names are case sensitive in Windows.

## Pi

- [How to setup an Ergo node on a Raspberry Pi](https://youtu.be/yDqhlgz0244)

-->