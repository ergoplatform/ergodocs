
# Resources

## Finding Testnet Peers

Connecting to reliable peers is essential for synchronizing your testnet node. Here are some resources and tips:

*   **Peer Lists:**
    *   [api.tokenjay.app/peers/list](https://api.tokenjay.app/peers/list): This API endpoint lists known peers. **Important:** This list may contain both mainnet and testnet nodes. You will need to check if a listed peer is connectable on the testnet P2P port (default: 9022).
*   **Community Channels:** Finding reliable, up-to-date testnet peers can sometimes be challenging. Check Ergo community channels (e.g., Discord servers, Telegram groups, Ergo Forum) for pinned messages or recent discussions mentioning active testnet nodes. Asking in support channels is often helpful.
*   **Configuration:** Ensure your node configuration (`testnet.conf` or main config with `--testnet` flag) specifies the correct testnet P2P port (`scorex.network.bindAddress` and potentially `scorex.network.declaredAddress` if needed) - default is `9022`. You can also add known reliable peer addresses to the `scorex.network.knownPeers` list in your configuration.

## Other Resources

*   [Testnet Explorer](https://testnet.ergoplatform.com/)
*   [ergo-synced-node](https://github.com/mgpai22/ergo-synced-node#ergo-testnet-node-setup): A pre-synchronized testnet node setup provided by a community member (check repository for current status).

## Ports

|                | mainnet  | testnet   |
|----------------|----------|-----------|
| API Port       | 9053     | 9052      | 
| P2P Port       | 9030     | 9022      |
| address prefix | (0) 0x00 | (16) 0x10 |


## Development 

- [Nautilus Testnet build](https://github.com/capt-nemo429/nautilus-wallet#testnet)
