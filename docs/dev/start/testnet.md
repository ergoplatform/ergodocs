Currently there is one Ergo testnet available. 

Explorer is available at [testnet.ergoplatform.com](https://testnet.ergoplatform.com/)

To join the testnet, just download [latest Ergo protocol reference client](https://github.com/ergoplatform/ergo/releases) and launch using

```bash
java -jar -Xmx3G ergo-*.jar --testnet -c testnet.conf
```

where minimal testnet.conf would be:

```
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

Testnet Faucet
==============

You can  get 60 testERG by sending a request to `https://testnet.ergofaucet.org/payment/address/TESTNET_WALLET_ADDRESS` 