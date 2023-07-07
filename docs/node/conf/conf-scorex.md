# Scorex Configuration

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


Taken from [application.conf#L354](https://github.com/ergoplatform/ergo/blob/49b9f0fe7d0eba1a5ff81e524353acdd9a3cc6dd/src/main/resources/application.conf#L354)

## Execution Context

The `executionContext` configuration section is used for tests. It specifies settings for the execution context that Scorex uses.

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

The `type` is set to "Dispatcher", and the `executor` to "thread-pool-executor". The `fixed-pool-size` under `thread-pool-executor` is set to 16, indicating that a maximum of 16 threads will be used for execution. The `throughput` setting is set to 1.

## Data and Log Directory

```conf
dataDir = ${user.home}"/scorex"
logDir = ${scorex.dataDir}"/log"
```
The `dataDir` setting determines the directory where the Scorex data will be stored, in this case, it is set to a "scorex" directory in the user's home directory. The `logDir` setting sets the location of the log files, which is a "log" directory within the Scorex data directory.

## REST API

```conf
restApi {
    bindAddress = "0.0.0.0:9052"
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
    corsAllowedOrigin = "*"
    timeout = 5s
    publicUrl = "https://example.com:80"
}
```

The `bindAddress` sets the network address to which the REST API binds. `apiKeyHash` is the hex-encoded Blake2b256 hash of the API key, in this case, it is the hash of the string "hello". `corsAllowedOrigin` is set to "*" to enable CORS support from all origins. `timeout` is the request processing timeout, and `publicUrl` is a publicly accessible URL if a node that exposes REST API in the firewall.

## Network Configuration

```conf
network {
    nodeName = "ergo-node"
    appVersion = 5.0.1
    agentName = "ergoref"
    bindAddress = "0.0.0.0:9022"
    magicBytes = [2, 2, 2, 2]
    // declaredAddress details omitted for brevity...
    upnpEnabled = no
    localOnly = false
    upnp-gateway-timeout = 7s
    upnp-discover-timeout = 3s
    addedMaxDelay = 0ms
    handshakeTimeout = 30s
    knownPeers = []
    getPeersInterval = 2m
    maxConnections = 30
    connectionTimeout = 1s
    peerEvictionInterval = 1h
    // More settings omitted for brevity...
}
```

The `network` configuration section contains numerous settings related to the P2P network, such as node name (`nodeName`), application version (`appVersion`), agent name (`agentName`), network bind address (`bindAddress`), magic bytes (`magicBytes`), UPnP settings, and more.

## NTP Configuration

```conf
ntp {
    server = "pool.ntp.org"
    updateEvery = 30m
    timeout = 30s
}
```

The `ntp` configuration section specifies the Network Time Protocol (NTP) server to use for time synchronization (`server`), how frequently to update the time (`updateEvery`), and the timeout

 for server responses (`timeout`).