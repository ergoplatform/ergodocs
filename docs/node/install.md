# The Ergo Reference Client (Node)

The Ergo Node, a key part of Ergo's P2P network, hosts and syncs the entire blockchain. This page outlines Ergo Node's installation options and developer resources.


/// details | Alternatives
    {type: info, open: true}
If you're simply looking for a secure place to store your ERG, see the [wallets](wallets.md) page. [Satergo](https://satergo.com/) even offers the option to install a full node alongside their wallet.
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

The only hardware requirements are ~20GB of storage for the blockchain and ~8GB of RAM for handling the sync. Due to the intensive disk I/O, we recommend having 4-6GB of RAM with a fast SSD, running with the `-Xmx4G` flag on JVM9/11.
////
//// details | Modes of operation
    {type: notes, open: true}
Ergo node offers various security models for user flexibility. For quick sync and full node security, consider setting up a Pruned Full Node.
/// details | Full Archival Node
    {type: tip, open: false}
To install the Ergo Node from scratch, you can refer to the [manual install](manual.md) page for detailed instructions.
///
/// details | Pruned Full Node
    {type: tip, open: false}
Bootstrap a [pruned full node](pruned-full-node.md) using a verified UTXO set snapshot and NiPoPoWS. This feature allows you to achieve full node security on a standard laptop within minutes, eliminating the need to check approximately 95% of the blockchain.
///
/// details | Light Full Node
    {type: tip, open: false}
[This mode](light-full-node.md) only holds the root digest of the dictionary and checks full blocks or a suffix of the blockchain, depending on the setting.
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

/// details | Get setup on Testnet
    {type: tip, open: false}
Alternatively, if you want to get started on the testnet, there is a dedicated [testnet](testnet.md) setup guide available.
///
/// details | Use Docker
    {type: tip, open: false}
For more convenience, Docker provides a streamlined way to install and run the Ergo Node. Refer to the [Docker](docker.md) guide for instructions on setting up the node using Docker.
///
/// details | Toolkits
    {type: notes, open: false}
- [Explorer & Node Bundles](explorer.md#toolkits): Access pre-packaged bundles that include an Ergo Node and an explorer for easy setup.
- [Ergosphere](https://ergosphere.cloud/): Ergosphere is an Umbrel-like solution that simplifies the setup of self-hosted Ergo services. Please note that it is currently in the BETA stage.
- [Ergode](https://github.com/ross-weir/ergode) (ergo-node) is an Ergo node implementation in TypeScript, targeting web and native runtimes.
///
/// details | Resources
    {type: notes, open: false}
- To get an overview of live nodes on the Ergo network, you can visit [ergonodes.net](http://ergonodes.net).
- [Frequently Asked Questions](faq.md): Find answers to common questions about the Ergo Node.
- [Modes of Operation](modes.md): Learn about the different modes of operation available for the Ergo Node.
- [APIs](api.md): Explore the APIs provided by the Ergo Node for interacting with the blockchain.
///
////