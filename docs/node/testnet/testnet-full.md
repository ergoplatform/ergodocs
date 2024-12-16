# Synchronising a full node

To join the testnet, download [latest Ergo protocol reference client](https://github.com/ergoplatform/ergo/releases) and launch using

```bash
java -jar -Xmx4G ergo-*.jar --testnet -c testnet.conf
```


A minimal `testnet.conf` would be:

```conf
ergo {
  networkType = "testnet"
}
scorex {
 restApi {
    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
    # Below is hash corresponding to API_KEY = "hello" (with no quotes)
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
}
```

The node will be available at `localhost:9052/panel`

Once the node is synchronised, a user interface for [Swagger](swagger.md) is available at `localhost:9052/swagger`. 

/// details | Mining
    {type: info, open: true}
If you want to help mine the testnet, you can do so by following the steps outlined on [CPU Mining](cpu-mining.md).
///