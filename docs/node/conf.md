# Overview of Node Configuration Files 

Welcome to the node configuration files documentation. This section provides a comprehensive guide to various configuration files crucial for setting up and managing an Ergo node. These files include essential parameters for controlling and fine tuning different aspects of the Ergo protocol, ranging from node operation and blockchain management to wallet functionality and voting mechanisms. 

Included in this section is the [application.conf](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/application.conf) file, which is the main configuration file, and a host of others that each serve specific purposes in the overall functioning of the node.

- [application.conf](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/application.conf): The principal configuration file which contains the primary settings for the Ergo protocol. 

    - [node](conf-node.md): Configures node-specific parameters.
    - [cache](conf-cache.md): Handles cache-related settings.
    - [chain](conf-chain.md): Manages blockchain related settings.
    - [wallet](conf-wallet.md): Sets up wallet parameters.
    - [voting](conf-voting.md): Oversees voting-related configurations.

- [bounded-mailbox](conf-bounded.md): Controls mailbox settings.
- [akka](conf-akka.md): Manages Akka settings for the actor system.
- [scorex](conf-scorex.md): Handles settings related to Scorex framework.
- [critical-dispatcher](conf-crit.md): Manages settings for critical dispatchers.
- [api-dispatcher](conf-api.md): Sets up settings for API dispatchers.

This section also details the [testnet.conf](testnetconf.md) file, which is specifically designed for operating in the Ergo testnet environment.

Feel free to navigate through each file documentation for a deeper understanding of the node configuration process. Remember, properly managing these settings is crucial for the smooth operation of your Ergo node.