
# scorex 

## executionContext

Execution context used in tests

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

## restApi

Node's REST API settings

### bindAddress
### apiKeyHash
### corsAllowedOrigin
### timeout
### publicUrl

```
# Node's REST API settings
  restApi {
    # Network address to bind to
    bindAddress = "0.0.0.0:9052"

    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
    # Below is the hash of "hello" string.
    # Change it!
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"

    # Enable/disable CORS support.
    # This is an optional param. It would allow cors in case if this setting is set.
    # If this setting will be omitted cors will be prohibited.
    corsAllowedOrigin = "*"

    # request processing timeout
    timeout = 5s

    # node which exposes restApi in firewall should define publicly accessible URL of it
    # publicUrl = "https://example.com:80"
  }
```

## network

P2P Network settings

### nodeName
### appVersion
### agentName
### bindAddress
### magicBytes
### declaredAddress
### upnpEnabled
### localOnly


### upnp-gateway-timeout
```
upnp-gateway-timeout = 7s
```
### upnp-discover-timeout 
```
upnp-discover-timeout = 3s
```
Add delay for sending message

### addedMaxDelay
```
addedMaxDelay = 0ms
```
### Peers Settings
#### handshakeTimeout
#### knownPeers
#### getPeersInterval
#### maxConnections
#### connectionTimeout
#### peerEvictionInterval

### Delivery Settings Limits

#### deliveryTimeout
#### maxDeliveryChecks

### Timeouts

#### inactiveConnectionDeadline
#### syncInterval
#### syncIntervalStable
   

   
#### syncTimeout 

#### syncStatusRefresh

#### syncStatusRefreshStable
#### syncIntervalStable

#### controllerTimeout 
    Network controller timeout

### Size limits 

#### desiredInvObjects = 400

