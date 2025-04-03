---
tags:
  - Node
  - Configuration
  - Overview
  - application.conf
  - testnet.conf
---

# Overview of Node Configuration Files 

Welcome to the node configuration files documentation. This section provides a comprehensive guide to the various configuration files crucial for setting up and managing an Ergo node. These files contain essential parameters for controlling and fine-tuning different aspects of the Ergo protocol, ranging from node operation and blockchain management to wallet functionality and voting mechanisms. 

Included in this section is the main configuration file, [application.conf](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/application.conf), along with several others that each serve specific purposes in the node's overall functioning.

- [application.conf](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/application.conf): The principal configuration file containing the primary settings for the Ergo protocol. 

    - [node](conf-node.md): Configures node-specific parameters.
    - [cache](conf-cache.md): Handles cache-related settings.
    - [chain](conf-chain.md): Manages blockchain-related settings.
    - [wallet](conf-wallet.md): Sets up wallet parameters.
    - [voting](conf-voting.md): Oversees voting-related configurations.

- [bounded-mailbox](conf-bounded.md): Controls mailbox settings.
- [akka](conf-akka.md): Manages Akka settings for the actor system.
- [scorex](conf-scorex.md): Handles settings related to the Scorex framework.
- [critical-dispatcher](conf-crit.md): Manages settings for critical dispatchers.
- [api-dispatcher](conf-api.md): Sets up settings for API dispatchers.

This section also details the [testnet.conf](testnetconf.md) file, which is specifically designed for operating an Ergo node on the testnet environment.

Feel free to navigate through each file's documentation for a deeper understanding of the node configuration process. Remember, properly managing these settings is crucial for the smooth operation of your Ergo node.

### Ergo Configuration Sections

The root configuration section `ergo` encompasses essential application parameters and various other configuration subsections. There is also another root section, `scorex`, which contains parameters inherited from the [Scorex project](https://github.com/ScorexFoundation/Scorex).

The `directory` parameter allows you to define a path to the base application directory. You can use environment variables to override configuration parameters. For instance, the base directory path is constructed relative to the user's `HOME` environment variable by default. Refrain from enclosing references to environment variables in quotation marks, as they will be treated as literal strings and not resolved.

### Network Settings

The `scorex.network` section allows you to configure settings related to the P2P network.

Using the `declaredAddress` parameter, you can establish the external IP address and port number that your node advertises to peers. This is necessary for operating behind NAT, common in cloud hosting scenarios where the machine doesn't directly interface with the external IP address. If left unspecified, your node will connect to the P2P network but won't accept incoming connections, meaning other nodes cannot connect to it. Other nodes use these settings to connect to your node. The format for this parameter is `"<ip-address>:<port>"`.

You can use the `bindAddress` parameter to set the IP address of the local network interface where the Ergo Node will listen for incoming P2P connections. By default, the node binds to `"0.0.0.0"`, indicating it will listen on all available network adapters.

**About Internet Address Settings**

Internet Address settings follow the `"<ip-address>:<port>"` format. Note that the `:<port>` component is crucial.

For the `bindAddress` setting, the port component establishes the network port number on which your node listens for incoming connections from other Ergo nodes. Please ensure this port is externally accessible (e.g., through firewall rules and port forwarding); otherwise, your node will only establish outgoing connections. If the specified port is already occupied by another application, your node will fail to start.

You can use the `nodeName` parameter to assign a visible name to your node for other participants in the P2P network. This name is transmitted during the initial handshake. In the default configuration, this parameter is commented out, resulting in a randomly generated node name.

The `knownPeers` parameter stores a list of bootstrap node addresses that your node will attempt to connect to upon initialization.

**About Time Settings**

All time span parameters are specified in milliseconds by default. However, you can use duration units for convenience. Supported units include:
* s, second, seconds
* m, minute, minutes
* h, hour, hours
* d, day, days

For usage examples, refer to the default configuration file linked above.

Use the `maxConnections` parameter to define the maximum number of concurrent P2P connections the node can handle.

The `connectionTimeout` parameter allows you to adjust the network communication timeout for P2P connections.

The `handshakeTimeout` parameter sets the maximum time to wait for a response during the P2P handshake process. If no response is received within this period, the peer will be blacklisted.

You can configure UPnP (Universal Plug and Play) settings using parameters starting with `upnp`. These settings are typically useful only if you're running your Ergo node on a home network where the node can automatically request your router to establish port forwarding. By default, UPnP is disabled. Use the `upnpEnabled` parameter to enable it.

**Wallet Settings**

In the `ergo.wallet` section, you can configure the node's built-in wallet.

Use the `dlogSecretsNumber` parameter to specify the number of Schnorr secret keys (private keys corresponding to `ProveDlog` public keys) to generate or manage within the wallet.

The `scanningInterval` parameter allows you to set the rescanning interval for uncertain boxes (boxes whose spending status might be temporarily unknown during chain reorganizations).

You can use the `seed` parameter (a Base64 encoded string) to restore an existing wallet on a new node. If you don't have an existing wallet seed, comment out this parameter. When the node starts for the first time, it will generate a new wallet with a random seed, which will be displayed in the application log.

**Warning!**

The wallet file (`wallet.dat` by default) is crucial. Ensure you store it in a safe, protected location and back it up regularly. 

It is strongly advised to remove the `seed` parameter from the configuration file after the wallet has been successfully initialized or restored. If an attacker gains access to your seed phrase, they can access all funds associated with that wallet across all derived addresses!

**Blockchain Settings**

In the `ergo.chain` section, you can select or customize blockchain parameters (primarily relevant for custom networks or testnets).

Use the `blockInterval` parameter to set the target time interval between blocks (in seconds).

The `epochLength` parameter defines the length of an epoch (in blocks) used for difficulty recalculation and storage rent adjustments.

The `useLastEpochs` parameter specifies the number of most recent epochs used for difficulty recalculation.

You can modify the Proof-of-Work algorithm or related parameters using the `powScheme` section.

**Node Settings**

In the `ergo.node` section, you can configure parameters related to the node's operational mode.

Use the `mining` parameter (previously `enable`) to enable or disable block generation (mining) on the node. By default, it's disabled (`mining = false`).

A node with `offlineGeneration = false` (default) will only attempt mining once it is fully synchronized and connected to the network. Setting `offlineGeneration = true` allows the node to mine blocks even when offline or not fully synced (useful for testing or private networks).

You can adjust your node's mining delay after discovering a new block using the `miningDelay` parameter (in milliseconds).

### REST API Settings

In the `scorex.rest-api` section, you can configure the node's REST API parameters.

Use the `bindAddress` parameter to select the network interface and port where the REST API will accept incoming connections (e.g., `"127.0.0.1:9053"`).

> **Warning!** For security reasons, avoid changing `bindAddress` from `"127.0.0.1"` (localhost) unless you fully understand the implications. Exposing the API directly to the internet is highly discouraged. For external access, use secure methods like [Nginx's `proxy_pass` module](http://nginx.org/en/docs/http/ngx_http_proxy_module.html) with HTTPS or [SSH port forwarding](http://blog.trackets.com/2014/05/17/ssh-tunnel-local-and-remote-port-forwarding-explained-with-examples.html).

Use the `apiKeyHash` parameter to set the Blake2b hash of your chosen API key (password). This key protects access to sensitive API endpoints (like wallet operations). Note that you provide the *hash* in the configuration, but you must provide the *plain text API key* itself in the `api_key` HTTP header when making REST calls. You can use tools like `blake2b-cli` or online calculators to generate the hash of your chosen API key.

> **Warning!** The API key is transmitted as plain text in the HTTP header and can be intercepted if the connection is not secured (e.g., using HTTPS or SSH tunneling). An attacker intercepting the key could potentially access wallet functions and transfer your funds! Always protect API access.

The `corsAllowedOrigin` parameter configures Cross-Origin Resource Sharing (CORS) support for the REST API. Setting it to `"*"` allows requests from any origin, which is necessary for tools like the Swagger UI and web-based wallets interacting directly with the node API. You can restrict it to specific origins for enhanced security if needed. Read more about CORS [here](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing).

### API Performance, Timeouts, and Limits

Several configuration parameters can influence the performance and behavior of the node's REST API, especially under heavy load:

*   **Request Timeout:** The `scorex.restApi.timeout` setting (see [Scorex Config](conf-scorex.md)) defines the maximum time the node will spend processing a single API request before timing out (default is often 5 seconds). If you experience timeouts during complex queries or high load, you might consider increasing this value, but be aware of the potential resource implications.
*   **Concurrency Handling:** The processing of API requests is managed by Akka dispatchers. The `api-dispatcher` settings (see [API Dispatcher Config](conf-api.md)) control the number of threads (`parallelism-min`, `parallelism-factor`, `parallelism-max`) and the processing throughput (`throughput`) for handling concurrent API requests. Tuning these values might improve responsiveness under load but requires understanding Akka dispatcher configuration.
*   **Rate Limiting:** The Ergo node software does **not** include built-in application-level rate limiting for its API endpoints. If you need to protect your node from excessive API requests, you should implement rate limiting externally, for example, using a reverse proxy server like Nginx or HAProxy placed in front of the node.
*   **JVM Memory:** Overall node performance, including API responsiveness, can be affected by the allocated Java Virtual Machine (JVM) memory. Ensure the node has sufficient heap space allocated via the `-Xmx` flag (e.g., `-Xmx4G`) when starting the node, as described in the [Manual Installation Guide](install/manual.md). Insufficient memory can lead to increased garbage collection pauses and slower response times, potentially contributing to timeouts under load.
