# Testnet

The testnet is an alternative Ergo block chain you can use for testing and experimentation, without having to use real ERG or worrying about breaking the main chain. The testnet runs on different ports than the mainnet and can be accessed by changing your `.conf` and running with the `--testnet` flag. 


|                | mainnet  | testnet   |
|----------------|----------|-----------|
| API Port       | 9053     | 9052      | 
| P2P Port       | 9030     | 9020      |
| address prefix | (0) 0x00 | (16) 0x10 |

- [Testnet Explorer](https://testnet.ergoplatform.com/)

To join the testnet, just download [latest Ergo protocol reference client](https://github.com/ergoplatform/ergo/releases) and launch using

```bash
java -jar -Xmx4G ergo-*.jar --testnet -c testnet.conf
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

> Please note that the [Headless dApp framework](/dev/stack/headless/#headless-dapp-framework) does not work with testnet addresses. [ref](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/src/encoding.rs#L104)



**GetBlok**

Alternatively, GetBlok run a public testnet that should help out any devs who need to do work on testnet but don't know how to run a solo mining node. It should also give an give an alternative way to start up testnet in case the usual miner is down. 

```
ergo-testnet.getblok.io:3056
```

Payouts are frozen for right now, if any of you need testnet ERG then you can tag @CheeseEnthusiast on Discord and he can start them up again.



