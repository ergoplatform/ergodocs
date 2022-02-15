# Testnet

Currently, there are two Ergo testnet available. 

Explorer is available at [testnet.ergoplatform.com](https://testnet.ergoplatform.com/)

To join the testnet, just download [latest Ergo protocol reference client](https://github.com/ergoplatform/ergo/releases) and launch using

```bash
java -jar -Xmx3G ergo-*.jar --testnet -c testnet.conf
```

A minimal `testnet.conf` would be:

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

**Faucet**

You can  get 60 testERG by sending a request to `https://testnet.ergofaucet.org/payment/address/TESTNET_WALLET_ADDRESS` 


## GetBlok 

This should help out any devs who need to do work on testnet but don't know how to run a solo mining node. It should also give an give an alternative way to start up testnet in case the usual miner is down. 

```
ergo-testnet.getblok.io:3056
```

Payouts are frozen for right now, if any of you need testnet ERG then you can tag @CheeseEnthusiast on Discord and he can start them up again.


## Notes

### IDs


```
# Network address prefix, currently reserved values are 0 (mainnet) and 16 (testnet)
addressPrefix = 16
```

### Ports

API is `9052` on testnet, `9053` on mainnet. P2P port is `9020` on testnet, `9030` on mainnet
 
### HDF

Headless framework does not work with testnet addresses.[ref](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/src/encoding.rs#L104)

so 0x10 for the testnet, 0x00 for the mainnet

