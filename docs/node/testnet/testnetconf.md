# Testnet Configuration

This document describes the main sections and fields of the [Ergo node configuration file for the Test Network](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/testnet.conf). This configuration serves the need for non-breaking changes testing.

## Ergo Configuration Section

### Network Type
`ergo.networkType = "testnet"`
This setting defines the network type. For testing purposes, it's set to "testnet".

### Node Configuration
`ergo.node`
This section contains parameters related to the node settings.

- `headerChainDiff` defines the maximum allowed number of blocks difference between the current local chain and the network. If the difference exceeds this value, the node is considered unsynchronized.
- `internalMinersCount` sets the number of internal miner threads. This helps reproduce real-world scenarios like having multiple GPU miners.
- `internalMinerPollingInterval` is the polling interval for GPU miners.
- `maxTransactionCost` sets the maximum cost for a transaction to be propagated across the network.
- `adProofsSuffixLength` determines the size of the suffix for dumping ADProofs during bootstrapping.
- `checkpoint` is a mandatory checkpoint introduced due to some violations in the PaiNet.

### Chain Configuration
`ergo.chain`
This section includes parameters related to the blockchain.

- `protocolVersion` sets the protocol version.
- `addressPrefix` is the prefix for network addresses. Reserved values include 0 (for mainnet) and 16 (for testnet).
- `initialDifficultyHex` sets the initial difficulty for the network.
- `epochLength` defines the length of an epoch in difficulty recalculation. A value of 1 means difficulty is recalculated every block.
- `blockInterval` is the desired time interval between blocks.
- `monetary.minerRewardDelay` sets the delay between when a block is mined and when the reward can be spent.
- `voting` contains parameters related to the voting mechanism, such as the length of a voting epoch, the number of epochs for soft-fork voting, and activation epochs for a soft-fork after acceptance.
- `reemission` includes parameters related to the emission process. 
- `genesisStateDigestHex` is the Base16 representation of the genesis state roothash.

### Voting Configuration
`ergo.voting`
This section allows configuration of voting parameters.

### Wallet Configuration
`ergo.wallet.secretStorage.secretDir`
Sets the directory for the wallet's secret storage.

## Scorex Configuration Section

### Network Configuration
`scorex.network`
This section includes parameters related to the network settings.

- `magicBytes` is a unique identifier for the network protocol. 
- `bindAddress` sets the IP address and port number where the node will accept incoming connections. By default, it listens on all available network adapters.
- `nodeName` assigns a visible name to your node for other participants in the P2P network.
- `knownPeers` is a list of bootstrap nodes that your node will connect to upon initialization.

### REST API Configuration
`scorex.restApi`
This section allows the setting of the node's REST API parameters.

- `apiKeyHash` is the hash of your API key. The API key protects the invocation of critical API methods.

**Note:** Ensure to secure the transmission of the API key as it is transmitted as plain text in the HTTP header and can be intercepted during network transit!