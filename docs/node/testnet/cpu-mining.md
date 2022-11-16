# CPU Mining

If you want to mine your own blocks on the testnet, you'll need to enable `mining` and disable `useExternalMiner` in your configuration file. 

```
ergo {
  networkType = "testnet"

  node {
    mining = true
    useExternalMiner = false
  }

 
}

scorex {

 network {
    bindAddress = "0.0.0.0:9020"
    nodeName = "ergo-testnet"
    #knownPeers = []
  }

 restApi {
    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
    # Below is hash corresponding to API_KEY = "hello" (with no quotes)
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
}

```