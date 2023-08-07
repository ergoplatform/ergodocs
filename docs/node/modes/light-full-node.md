
# Light Full-Node Mode

## Overview 

A *light-fullnode* only holds the root digest of the dictionary and checks full blocks or a suffix of the blockchain, depending on the setting. It uses AD-transformations to get a new digest from an old one and checks all transactions, but only stores a single digest.

The configuration below will check only last 1440 blocks, and provides full-node security when validating them.

This system supports wallet functionalities and custom scans. However, it has a limitation: it can only accept and broadcast transactions initiated within its own network, not those coming from external peers.


## Getting Started


It's possible to run the node in this *light mode* by changing the the [`stateType`](conf-node.md#state-type) variable in your `ergo.conf` file

Here is an example configuration for **light node** 


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

- `statetype` sets the type of state the node maintains. Possible options are `utxo`, where the node keeps a full utxo set allowing it to validate arbitrary blocks and generate ADProofs, and `digest`, where the node only keeps the state root hash and validates transactions via ADProofs.
- The `blocksToKeep` variable allows you to specify how many of the previous blocks you want to store. In this case, checking and storing only last 1440 blocks. 
- The `nipopowBootstrap` tells the node to Download a PoPoW proof on node bootstrap, bringing the storage requirements after bootstrapping down to ~100 Mb


This mode uses a 2-party authenticated dynamic dictionary built on top of the UTXO set. 

See the [technical workflow](light-techworkflow.md) for more information