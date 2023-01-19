
# Resources

To find public testnet nodes, you can use [api.tokenjay.app/peers/list](https://api.tokenjay.app/peers/list) and swap ports until you find one that's running testnet.

- [Testnet Explorer](https://testnet.ergoplatform.com/)
- [ergo-synced-node](https://github.com/mgpai22/ergo-synced-node#ergo-testnet-node-setup)


## Development 

- [Nautilus Testnet build](https://github.com/capt-nemo429/nautilus-wallet#testnet)


> Please note that the [Headless dApp framework](/dev/stack/headless/#headless-dapp-framework) [does not work with testnet addresses](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/src/encoding.rs#L104)



## Ports

|                | mainnet  | testnet   |
|----------------|----------|-----------|
| API Port       | 9053     | 9052      | 
| P2P Port       | 9030     | 9021      |
| address prefix | (0) 0x00 | (16) 0x10 |



