# Testnet Resources

This page provides resources for interacting with the Ergo Testnet.

## Finding & Connecting to Testnet Peers

Synchronizing a testnet node requires connecting to active testnet peers. Finding reliable peers can sometimes be challenging.

### Peer Lists

* **Public Peer Lists:**
  * For mainnet peers: `https://api.tokenjay.app/peers/list?unreachable=false&closedApi=false&limit=50`
  * For testnet peers: Use the same list but swap the port numbers (mainnet uses 9053, testnet uses 9052)

### Node Configuration

Below is an example configuration for a testnet node:

```
ergo {
  networkType = "testnet"
  directory = "/ergo/.ergo"
  node {
    useExternalMiner = true
    offlineGeneration = true
    mining = true
    mempoolCapacity = 10000
    extraIndex = true
    maxTransactionSize = 1000000
    maxTransactionCost = 2000000
  }
  wallet.secretStorage.secretDir = ${ergo.directory}"/wallet/keystore"
  chain {
    genesisStateDigestHex = "cb63aa99a3060f341781d8662b58bf18b9ad258db4fe88d09f8f71cb668cad4502"
    reemission {
      checkReemissionRules = true
    }
  }
}

scorex {
  restApi {
    apiKeyHash = ""
    bindAddress = "0.0.0.0:9052"
  }
  network {
    bindAddress = "0.0.0.0:9022"
    knownPeers = [
      "213.239.193.208:9022",
      "51.158.54.129:9022",
      "51.89.40.122:9022"
    ]
    maxConnections = 100
  }
}
```

### Important Configuration Options

* **`knownPeers`**: Manually specify testnet peers to connect to
* **`maxConnections`**: Default is around 30, can be increased for better network connectivity (may require more resources)
* **`bindAddress`**: For REST API, use port 9052 for testnet (compared to 9053 for mainnet)
* **`networkType`**: Must be set to "testnet"

## Port Reference

| Service | Mainnet | Testnet |
|---------|---------|---------|
| REST API | 9053 | 9052 |
| P2P Network | 9030 | 9022 |
| Address Prefix | (0) 0x00 | (16) 0x10 |

## Testnet Resources

* [Testnet Explorer](https://testnet.ergoplatform.com/)
* [Testnet Faucet](https://testnet.ergofaucet.org/) - Get test ERG for development
* [Nautilus Testnet Build](https://github.com/capt-nemo429/nautilus-wallet#testnet)

## Development Tools

When configuring dApps for testnet, update these settings:
```
node.url = "http://213.239.193.208:9052/"
node.networkType = "TESTNET"
explorer.url = "https://testnet.ergoplatform.com/"
```

For detailed documentation on node setup and development, refer to the [official Ergo documentation](https://docs.ergoplatform.com/documents/).