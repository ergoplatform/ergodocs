
# scorex 

## executionContext

Execution context used in tests

### type
```conf
type = Dispatcher
```

### executor
```conf
executor = "thread-pool-executor"
```
### thread-pool-executor
#### fixed-pool-size
```conf
fixed-pool-size = 16
```

### throughput
```conf
throughput = 1
```


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

## dataDir
```conf
dataDir = ${user.home}"/scorex"
```

## logDir
```conf
logDir = ${scorex.dataDir}"/log"

  logging {
    level = "INFO"
  }
```

## restApi

Node's REST API settings

### bindAddress
```conf
bindAddress = "0.0.0.0:9052"
```
The network address to bind to
### apiKeyHash
```conf
apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
```
Hex-encoded Blake2b256 hash of an API key. It should be a 64-char long Base16 string.
Below is the hash of the "hello" string.
Change it!
### corsAllowedOrigin
```conf
corsAllowedOrigin = "*"
```
Enable/disable CORS support.
This is an optional parameter and will allow cors in case this setting is set.
If this setting is omitted, cors will be prohibited.

### timeout
```conf
timeout = 5s
```
Request processing timeout

### publicUrl
```conf
publicUrl = "https://example.com:80"
```
A node that exposes restApi in the firewall should define a publicly accessible URL.


## network

P2P Network settings
### Node information to be declared during the handshake
#### nodeName
```conf
nodeName = "ergo-node"
```
Node name to send during the handshake
#### appVersion
```conf
appVersion = 5.0.1
```
Network protocol version to be sent in handshakes
#### agentName
```conf
agentName = "ergoref"
```

Network agent name. It may contain information about the client's code
stack, from the core code base to the end graphical interface.
Basic format is `/Name:Version(comments)/Name:Version/.../`,
e.g. `/Ergo-Scala-client:2.0.0(iPad; U; CPU OS 3_2_1)/AndroidBuild:0.8/`
    
#### bindAddress
```
bindAddress = "0.0.0.0:9020"
```

Network address

### Connection settings
#### magicBytes
```
magicBytes = [2, 2, 2, 2]
```
Magic bytes will be added to every p2p message to distinguish different networks (e.g. testnet/mainnet).
   
#### declaredAddress

```
# declaredAddress = ""
```

To broadcast on IPV6, you must enter your IPV6 address here as such;

```
declaredAddress = "[2345:0425:2CA1:0000:0000:0567:5673:23b5]:9030"
```

Similarly to sync a node using ipv6 only you need to place this line in your config. 

```
scorex.network.knownPeers = ["[2601:204:c003:57e3:95b6:6344:5577:3e9c]:9030"]
```


String with IP address and port to send as external address during the handshake.

It could be set automatically if UPnP is enabled.

If `declared-address` is set, which is the common scenario for nodes running in the cloud, the node will just listen to incoming connections on `bindAddress:port` and broadcast its `declaredAddress` to its peers.

UPnP is supposed to be disabled in this scenario.

If the declared address is not set and UPnP is not enabled, the node will not listen to incoming connections.

If the declared address is not set and UPnP is enabled, the node will attempt to connect to an IGD, retrieve its external IP address and configure the gateway to allow traffic through. If the node succeeds, the IGD's external IP address becomes the node's declared address.

In some cases, you may both set `decalredAddress` and enable UPnP (e.g. when IGD can't reliably determine its
external IP address). In such cases, the node will attempt to configure an IGD to pass traffic from the external port to the `bind-address:port`. Please note, however, that this setup is not recommended.

#### upnpEnabled
```
upnpEnabled = no
```
Enable UPnP tunnel creation only if your router/gateway supports it. It is useful if your node runs an in-home network and is completely useless in the cloud.

#### localOnly
```
localOnly = false
```

Accept only local connections.


### upnp-gateway-timeout
```
upnp-gateway-timeout = 7s
```
### upnp-discover-timeout 
```
upnp-discover-timeout = 3s
```
Add delay for sending a message.

### addedMaxDelay
```
addedMaxDelay = 0ms
```

Add delay for sending a message.

### Peers Settings
#### handshakeTimeout
```
handshakeTimeout = 30s
```

Network handshake timeout

#### knownPeers
```
knownPeers = []
```

A list of `IP:port` pairs of well-known nodes.
#### getPeersInterval
```
getPeersInterval = 2m
```

The interval between GetPeers messages to be sent by our node to a random one

#### maxConnections
```conf
maxConnections = 30
```
Number of network connections
#### connectionTimeout
```conf
connectionTimeout = 1s
```

Network connection timeout
#### peerEvictionInterval
```conf
peerEvictionInterval = 1h
```

the interval of evicting random peer to avoid eclipsing

### Delivery Settings Limits

#### deliveryTimeout
```conf
deliveryTimeout = 10s
```
Network delivery timeout
#### maxDeliveryChecks
```conf
maxDeliveryChecks = 100
```

Max number of delivery checks. Stop expecting a modifier if it was not delivered after that number of delivery attempts. The node tries to ask different peers on different attempts and not increasing the delivery counter if global loss of connectivity is possible.
    
### Timeouts


#### inactiveConnectionDeadline
```conf
inactiveConnectionDeadline = 10m
```

Timeout for dropping dead connections
#### syncInterval
```conf
syncInterval = 5s
```

The interval between `SyncInfo` messages when our node is not synchronized yet



#### syncIntervalStable
```conf
syncIntervalStable = 15s
```

The interval between `SyncInfo` messages when our node is already synchronized

   
#### syncTimeout 
```conf
syncTimeout = 10s
```

Synchronization timeout

#### syncStatusRefresh
```
syncStatusRefresh = 60s
```

Synchronization status update interval

#### syncStatusRefreshStable
```conf
syncStatusRefreshStable = 90s
```
#### syncIntervalStable
```conf
syncIntervalStable = 30s
```

Synchronization status update interval for a stable regime


#### controllerTimeout 
```conf
controllerTimeout = 5s
```

Network controller timeout

### Size limits 

#### desiredInvObjects
```conf
desiredInvObjects = 400
```

Desired number of inv objects. Our requests will have this size.

#### maxModifiersCacheSize
```conf
maxModifiersCacheSize = 1024
```

How many persistent modifiers to store in the cache.

The cache stores modifiers that are waiting to be applied.

#### maxPeerSpecObjects
```conf
maxPeerSpecObjects = 64
```

The maximum number of PeerSpec objects in one Peers message

#### temporalBanDuration
```conf
temporalBanDuration = 60m
```

Default ban duration unless the permanent penalty is applied.


#### penaltySafeInterval
```conf
penaltySafeInterval = 2m
```

Misbehaving peer penalty score will not increase within this interval unless a permanent penalty is applied.
    
#### penaltyScoreThreshold
```conf
penaltyScoreThreshold = 500
```

Max penalty score a peer can accumulate before being banned.

#### peerDiscovery
```conf
peerDiscovery = true
```

If set (and it is set by default), the node will try to discover peers in the network.

If set to false, the node will use only peers from the database (with a fallback to knownPeers config section if no peers are there)
    

## ntp

### server
```conf
server = "pool.ntp.org"
```

NTP server address

### updateEvery
```conf
updateEvery = 30m
```
update time rate
### timeout
```conf
timeout = 30s
```
server answer timeout