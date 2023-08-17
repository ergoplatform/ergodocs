
# Light Full-Node Mode

The light full-node mode in Ergo allows for a more resource-efficient way of running a node while still maintaining full-node security. In this mode, the node only holds the root digest of the dictionary and checks full blocks or a suffix of the blockchain, depending on the setting. It uses AD-transformations to get a new digest from an old one and checks all transactions, but only stores a single digest.

## Features and Limitations

The light full-node mode supports wallet functionalities and custom scans, making it suitable for various use cases. However, it has a limitation: it can only accept and broadcast transactions initiated within its own network, not those coming from external peers.

## Getting Started

To run the node in light mode, you need to make changes to the `ergo.conf` file. Specifically, you need to modify the [`stateType`](conf-node.md#state-type) variable to "digest" and set the `blocksToKeep` variable to specify how many of the previous blocks you want to store. For example, setting `blocksToKeep` to 1440 will check and store only the last 1440 blocks.

Here is an example configuration for running a light full-node:



```
ergo {
  node {
    stateType = "digest"
    blocksToKeep = 1440
    mining = false
    nipopowBootstrap = true
  }


}

scorex {

 restApi {
    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
    apiKeyHash = "6ed54addddaf10fe8fcda330bd443a57914fbce38a9fa27248b07e361cc76a41"
  }
}
```

In this configuration, the `stateType` is set to "digest" to maintain only the state root hash and validate transactions via ADProofs. The `blocksToKeep` variable is set to 1440 to store and validate the last 1440 blocks. The `nipopowBootstrap` option tells the node to download a PoPoW proof on node bootstrap, reducing the storage requirements after bootstrapping to approximately 100 Mb.

## Technical Details

The light full-node mode uses a 2-party authenticated dynamic dictionary built on top of the UTXO set. For more information on the technical workflow and implementation details, you can refer to the [light-techworkflow.md](light-techworkflow.md) document.



