# Testnet

The testnet is an alternative Ergo blockchain you can use for testing and experimentation without having to use real ERG or worrying about breaking the main chain. The testnet runs on different ports than the mainnet and can be accessed by changing your `.conf` and running with the `--testnet` flag. 


## Synchronising a full node

To join the testnet, download [latest Ergo protocol reference client](https://github.com/ergoplatform/ergo/releases/tag/5.0-RC2) and launch using

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
  
network {
   knownPeers = [
      "213.239.193.208:9020",
      "37.156.20.158:9020"
    ]
   peerDiscovery = false
  }

}
```

The node will be available at `localhost:9052/panel`

Once the node is syncronised, a user interface for [Swagger](/node/swagger/) is available at `localhost:9052/swagger`. 

You can get some testERG from [testnet.ergofaucet.org](https://testnet.ergofaucet.org/)


## Resources


- [Testnet Explorer](https://testnet.ergoplatform.com/)
- [ergo-synced-node](https://github.com/mgpai22/ergo-synced-node#ergo-testnet-node-setup)
- [Nautilus Testnet build](https://github.com/capt-nemo429/nautilus-wallet#testnet)




> Please note that the [Headless dApp framework](/dev/stack/headless/#headless-dapp-framework) [does not work with testnet addresses](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/src/encoding.rs#L104)

### Ports

|                | mainnet  | testnet   |
|----------------|----------|-----------|
| API Port       | 9053     | 9052      | 
| P2P Port       | 9030     | 9021      |
| address prefix | (0) 0x00 | (16) 0x10 |

To find public testnet nodes, you can use [api.tokenjay.app/peers/list](https://api.tokenjay.app/peers/list) and swap the port till you find one that's running testnet.



### GetBlok testnet

Alternatively, GetBlok runs a public testnet that should help devs who need to work on the testnet but don't know how to run a solo mining node. It should also give an alternative way to start a testnet in case the usual miner is down. 

```
ergo-testnet.getblok.io:3056
```
