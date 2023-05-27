# Ergo Node Devnet Configuration Documentation

This document describes the main sections and fields of the [Ergo node configuration file for the Development Network](https://raw.githubusercontent.com/ergoplatform/ergo/master/src/main/resources/devnet.conf). This configuration serves the need for protocol-breaking changes testing.

## Ergo Configuration Section

### Network Type
`ergo.networkType = "devnet"`
This setting defines the network type. For development purposes, it's set to "devnet".

### Chain Configuration
`ergo.chain`
This section includes parameters related to the blockchain.

- `protocolVersion` sets the protocol version.
- `addressPrefix` is the prefix for network addresses. Reserved values include 0 (for mainnet), 16 (for testnet), and 32 (for devnet).
- `initialDifficultyHex` sets the initial difficulty for the network.
- `epochLength` defines the length of an epoch in difficulty recalculation. A value of 1 means difficulty is recalculated every block.
- `blockInterval` is the desired time interval between blocks.
- `monetary.minerRewardDelay` sets the delay between when a block is mined and when the reward can be spent.
- `voting` contains parameters related to the voting mechanism, such as the length of a voting epoch, the number of epochs for soft-fork voting, and activation epochs for a soft-fork after acceptance.
- `genesisStateDigestHex` is the Base16 representation of the genesis state roothash.

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
`scorex.restApi.apiKeyHash`
This parameter represents the hash of your API key. In the devnet configuration, it is set to `null`. The API key protects the invocation of critical API methods.

**Note:** Even though it is set to `null` for development, you must ensure to secure the transmission of the API key in a real-world scenario, as it is transmitted as plain text in the HTTP header and can be intercepted during network transit!