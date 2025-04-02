---
tags:
  - Tor
  - Node
  - Privacy
  - Anonymity
  - Configuration
---

# Running your Node over Tor

[Tor](https://www.torproject.org/download/tor/) is a network that helps anonymize your internet traffic by routing it through a series of volunteer-operated servers (relays). This guide explains how to configure your Ergo node to route its P2P network traffic through Tor.


If you have Tor installed and running (typically listening on `127.0.0.1:9050` for SOCKS proxy connections), you first need to ensure your node's P2P and API interfaces are bound to localhost in your `ergo.conf` file:

```conf
scorex.network.bindAddress = "127.0.0.1:9030"
scorex.restApi.bindAddress = "127.0.0.1:9053"
```

With Tor installed and running, and the configuration above set, you then launch the Ergo node using specific Java system properties (`-D`) to direct its outgoing network traffic through the Tor SOCKS proxy:

```bash
java -DsocksProxyHost=localhost -DsocksProxyPort=9050 -Xmx4G -jar ergo-*.jar --mainnet -c ergo.conf 
```

# Example Configuration File

```conf
ergo {
    node {
        mining = false

        utxo {
           utxoBootstrap = true
           storingUtxoSnapshots = 0
        }
        nipopow {
           nipopowBootstrap = true
           p2pNipopows = 2
        }
    }

}

scorex {
    restApi {
        apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
        bindAddress = "127.0.0.1:9053"
    }
    network {
        bindAddress = "127.0.0.1:9030"
        # Use this if you want to bind it to a public address
        #declaredAddress = ""
    }
}
```
