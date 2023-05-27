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

### Ergo Configuration Sections

The root configuration section `ergo` encompasses essential application parameters and various other configuration subsections. There's also another root section `scorex` that contains parameters inherited from the [Scorex project](https://github.com/ScorexFoundation/Scorex).

The parameter `directory` allows you to define a path to the base application directory. You can use environment variables to override configuration parameters. For instance, the base directory is built relative to the user's `HOME` environment variable by default. Refrain from enclosing references to environment variables in quotation marks, as they'll be treated as strings and not resolved.

### Network Settings

The `scorex.network` section allows you to configure settings related to the P2P network.

By using the `declaredAddress` parameter, you can establish the external IP address and port number of the node. This is necessary for operating behind NAT in most cloud hosting scenarios where the machine doesn't directly interface with the external address. If left unspecified, your node will connect to the P2P network but won't accept incoming connections, meaning other nodes can't connect. Other nodes connect to your node using these settings. The format for this parameter is "[ip-address]:[port]".

You can use the `bindAddress` parameter to set the IP address of the local network interface where the Ergo Node will accept incoming connections. By default, the node binds to "0.0.0.0", indicating it will listen on all available network adapters.

**About Internet Address Settings**

Internet Address settings follow the "<ip-address>:<port>" format. Note that the "<port>" component after the colon is crucial.

For the `bindAddress` setting, the port component is used to establish the network port number to which other Ergo nodes will connect. Please ensure that this port is externally accessible; otherwise, your node will only establish outgoing connections to the P2P network. If the specified port is already occupied by another application, your node won't start.

You can use the `nodeName` parameter to assign a visible name to your node for other participants of the P2P network. This name is transmitted during the initial handshake. In the default configuration, this parameter is commented out, resulting in a randomly generated name.

The `knownPeers` parameter stores a list of bootstrap nodes that your node will connect to upon initialization.

**About Time Settings**

All time span parameters are set in milliseconds. However, you can use duration units to shorten their values. The supported units include:
* s, second, seconds
* m, minute, minutes
* h, hour, hours
* d, day, days

For examples of usage, refer to the default configuration file above.

Use the `maxConnections` parameter to define the maximum number of concurrent connections that the node can handle.

The `connectionTimeout` parameter allows you to adjust the network communication timeout.

The `handshakeTimeout` parameter can be used to set the time period to wait for a response during a handshake. If no response is received, the peer will be blacklisted.

You can configure the UPnP settings using parameters that begin with `upnp`. These settings are typically useful only if you're running your Ergo node on a home network where the node can request your router to establish a tunnel. By default, this functionality is disabled. Use the `upnpEnabled` parameter to enable it.

**Wallet Settings**

In the `wallet` section, you can configure the built-in wallet of the Ergo node.

Use the `dlogSecretsNumber` parameter to specify the number of Schorr secret keys (w for the g^w public key) to generate.

The `scanningInterval` parameter allows you to set a re-sc

anning interval for uncertain boxes.

You can use the `seed` parameter to recreate an existing wallet on a new node. If you don't have an existing wallet, comment out this parameter and start the node. During the first run, the application will generate a new wallet with a random seed for you. In this case, the seed will be displayed in the application log.

**Warning!**

The wallet is a crucial part of your node. Ensure to store the wallet's file in a safe and protected location, and remember to back it up. 

It's advised to remove the seed from the configuration file as soon as the node starts. If an attacker obtains access to this seed string, they can access all your funds across all your addresses!

**Blockchain Settings**

In the `ergo.chain` section, you can select or customize the blockchain parameters.

Use the `blockInterval` parameter to set the desired time interval between blocks.

The `epochLength` parameter is used to set the length of an epoch in difficulty recalculation. A value of 1 means difficulty recalculation every block.

The `useLastEpochs` parameter stores the number of most recent epochs that will be used for difficulty recalculation.

You can modify the PoW algorithm or related parameters using the `powScheme` section.

**Node Settings**

In the `ergo.node` section, you can configure parameters related to the node regime.

Use the `enable` parameter to enable or disable block generation on the node. By default, it's disabled.

A node with the `offlineGeneration` parameter disabled will begin mining as soon as it connects to the first peer in the P2P network. Setting this parameter to `true` enables off-line generation.

You can adjust your node's mining delay after discovering a new block using the `miningDelay` parameter.

**REST API Settings**

In the `scorex.rest-api` section, you can set the node's REST API parameters.

You can use the `bindAddress` parameter to select the network interface where the REST API will accept incoming connections. The `:<port>` component can be used to change the port number that the REST API will listen to for connections.

> **Warning!** For increased security, refrain from changing `bindAddress` from "127.0.0.1" unless you're sure of what you're doing! For external access, you should use [Nginx's proxy_pass module](http://nginx.org/ru/docs/http/ngx_http_proxy_module.html) or [SSH port-forwarding](http://blog.trackets.com/2014/05/17/ssh-tunnel-local-and-remote-port-forwarding-explained-with-examples.html) instead.

Use the `api-key-hash` parameter to set the hash of your API key. The API key is used to protect the invocation of critical API methods. Note that you should provide the hash of the API key in this parameter, but during REST calls, you should provide the API key itself. You can use blake2b to generate the hash of your API key.

> **Warning!** The API key is transmitted as plain text in the HTTP header and can be intercepted by an attacker during network transit! This could allow the attacker to transfer your funds to any address! Hence, protect the transmission using HTTPS or SSH port forwarding.

The `corsAllowedOrigin` parameter can be used to enable or disable CORS support in the REST API. CORS enables the safe resolution of queries to other domains outside the one running the node. It's necessary for Swagger and the Lite client. You can read more about it [here](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing).
