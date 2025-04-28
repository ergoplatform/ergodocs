---
tags:
  - Node
  - Reference Client
  - Installation
  - Setup
  - Guide
---

# The Ergo Reference Client (Node)

The Ergo Node is the core software that connects to the Ergo [P2P network](p2p-protocol-overview.md), validates [transactions](transactions.md) and [blocks](block.md), and maintains a copy of the entire [blockchain](protocol.md). Running a node is crucial for the network's decentralization and security. This page outlines the installation options and resources for the Ergo reference client.


/// details | Alternatives
    {type: info, open: true}
If you're simply looking for a secure place to store your ERG, see the [wallets](wallets.md) page. Some wallets like [Satergo](satergo.md) offer an integrated option to install and run a full node.
///

///// details | Installing the Ergo Reference Client
    {type: tip, open: true}
//// details | Minimum Requirements & Pre-requisites
    {type: warning, open: false}
**Java**

An Ergo node requires a **JDK/JRE version >= 9** installed on your system. We recommend using [Oracle Java SE](https://www.oracle.com/technetwork/java/javase/overview/index.html) or SDKMAN for Unix-based systems:

```bash
curl -s "https://get.sdkman.io" | bash
sdk install java 11.0.13.8.1-amzn
```

**Hardware**

The minimum hardware requirements are approximately ~20GB of storage for the blockchain and ~8GB of RAM for handling the initial sync. Due to potentially intensive disk I/O during sync, we recommend having at least 4-6GB of RAM available for the node process and using a fast SSD. Running with the `-Xmx4G` flag on the JVM is advised.
////
//// details | Modes of operation
    {type: notes, open: true}
Ergo node offers various [Modes of Operation](modes.md) for user flexibility. For quick sync and full node security, consider setting up a Pruned Full Node.
/// details | Full Archival Node
    {type: tip, open: false}
This mode stores the entire blockchain history. To install from scratch, refer to the [manual install](manual.md) page for detailed instructions.
///
/// details | Pruned Full Node
    {type: tip, open: false}
Bootstrap a [pruned full node](pruned-full-node.md) using a verified [UTXO set snapshot](eutxo.md) and [NiPoPoWs](nipopows.md). This feature allows you to achieve full node security on standard hardware within minutes, eliminating the need to download and validate most of the historical blockchain data.
///
/// details | Light Full Node
    {type: tip, open: false}
[This mode](light-full-node.md) only holds the root digest of the state dictionary and checks full blocks or a suffix of the blockchain, depending on the `blocksToKeep` setting ([History Pruning](history-pruning.md)).
///
////

//// details | Per device
    {type: notes, open: true}
/// details | Android
    {type: tip, open: false}
Sync the entire Ergo blockchain on your [mobile device](node-android.md)!
///
/// details | Raspberri Pi
    {type: tip, open: false}
Run a node on a [Raspberry Pi](pi.md)!
///
////


//// details | Developer Resources
    {type: notes, open: false}

/// details | DeepWiki Documentation
    {type: info, open: true}
For an alternative and potentially more detailed documentation source generated from the repository, explore the [Ergo Node on DeepWiki](https://deepwiki.com/ergoplatform/ergo/1-ergo-node-overview)
///


/// details | Get setup on Testnet
    {type: tip, open: false}
Alternatively, if you want to get started on the [testnet](testnet.md), there is a dedicated [testnet setup guide](testnet.md) available.
///
/// details | Use Docker
    {type: tip, open: false}
For more convenience, Docker provides a streamlined way to install and run the Ergo Node. Refer to the [Docker guide](docker.md) for instructions on setting up the node using Docker.
///
/// details | Toolkits
    {type: notes, open: false}
- [Explorer & Node Bundles](explorer.md#toolkits): Access pre-packaged bundles that include an Ergo Node and an [explorer](explorer.md) for easy setup.
- [Ergosphere](https://ergosphere.cloud/): Ergosphere is an Umbrel-like solution that simplifies the setup of self-hosted Ergo services. Please note that it is currently in the BETA stage.
- [Ergode](https://github.com/ross-weir/ergode) (ergo-node) is an Ergo node implementation in TypeScript, targeting web and native runtimes.
///
/// details | Resources
    {type: notes, open: false}
- To get an overview of live nodes on the Ergo network, you can visit [ergonodes.net](http://ergonodes.net).
- [Node Frequently Asked Questions](node-faq.md): Find answers to common questions about the Ergo Node.
- [Modes of Operation](modes.md): Learn about the different modes of operation available for the Ergo Node.
- [Node APIs](api.md): Explore the APIs provided by the Ergo Node for interacting with the blockchain.
- [Node Configuration](conf.md): Details on configuring the node via the `application.conf` file.
- [Node Protocol Details](protocol.md): Information on the underlying network protocol.
///
////
