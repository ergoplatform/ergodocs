# Running your Node over Tor

[Tor](https://www.torproject.org/download/tor/) is a network that helps you anonymize your internet traffic by routing it through a series of volunteer-operated servers. We'll guide you through the process of setting up Tor on your node.


If you have Tor installed, simply edit your configuration template to bind your node's services to the Tor-enabled addresses. 

```bash
scorex.network.bindAddress = "127.0.0.1:9030"
scorex.restApi.bindAddress = "127.0.0.1:9053"
```

Assuming you have Tor installed and running with the above confirmation, all you need to do is run with the `DsocksProxyHost` and `DsocksProxyPort` parameters that ensure that your node's traffic is routed through the Tor network.

```
java -jar -Xmx4G ergo-*.jar --mainnet -c ergo.conf -DsocksProxyHost=localhost -DsocksProxyPort=9050
```
