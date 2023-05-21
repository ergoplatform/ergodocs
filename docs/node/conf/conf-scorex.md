# Scorex Configuration

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
    bindAddress = "0.0.0.0:9020"
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