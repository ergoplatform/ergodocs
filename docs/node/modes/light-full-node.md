
# Light Full-Node Mode

The light full-node mode in Ergo allows for a more resource-efficient way of running a node while still maintaining full-node security. In this mode, the node only holds the root digest of the dictionary and checks full blocks or a suffix of the blockchain, depending on the setting. It uses AD-transformations to get a new digest from an old one and checks all transactions, but only stores a single digest.

## Features and Limitations

The light full-node mode supports wallet functionalities and custom scans, making it suitable for various use cases. However, it has a limitation: it can only accept and broadcast transactions initiated within its own network, not those coming from external peers.

## Getting Started

To run the node in light mode, you need to adjust specific settings in your `ergo.conf` file.

**Core Settings:**

*   **`ergo.node.stateType = "digest"`**: This is the key setting that enables light-fullnode mode. Instead of storing the full UTXO set, the node only maintains the authenticated root hash of the state and validates state transitions using ADProofs contained in the blocks. See [`stateType`](conf-node.md#state-type) for details.
*   **`ergo.node.blocksToKeep = 1440`** (Example): This setting controls how many of the most recent blocks are stored with full transaction data. Older blocks will only have their headers stored. Setting it to `-1` keeps all blocks (similar to an archive node but still in digest state). A common value is `1440` (roughly one day). See [`blocksToKeep`](conf-node.md#blocks-to-keep) for details.

**Bootstrapping Options:**

Bootstrapping is the initial synchronization process. Light nodes have options to speed this up and reduce initial storage requirements:

*   **`ergo.node.nipopow.nipopowBootstrap = true`**: Instructs the node to download a NiPoPoW proof during startup. This significantly reduces the data needed for initial sync compared to downloading all headers from genesis.
*   **`ergo.node.utxoBootstrap = true`**: (Alternative to NiPoPoW bootstrap) Instructs the node to download a UTXO set snapshot to initialize its state. This can be faster but might require more initial bandwidth. *Note: These two bootstrap options might be mutually exclusive depending on the node version; check current node documentation or configuration comments.*

**Example Configuration:**



```conf
ergo {
  node {
    stateType = "digest"
    blocksToKeep = 1440 // Keep ~1 day of full blocks
    mining = false      // Usually false for light nodes

    # Choose one bootstrapping method (check compatibility):
    nipopow.nipopowBootstrap = true 
    # utxoBootstrap = true 

    # Optional: Adjust NiPoPoW parameters if using nipopowBootstrap
    nipopow.p2pNipopows = 2 
  }
}

scorex {
  restApi {
    # Set your API key hash for security
    apiKeyHash = "YOUR_API_KEY_HASH_HERE" 
  }
  # Optional: Adjust network settings if needed
  # network { ... } 
}
```

In this example configuration:
*   `stateType = "digest"` enables the core light-fullnode mode.
*   `blocksToKeep = 1440` keeps roughly the last day's worth of full blocks.
*   `nipopowBootstrap = true` is enabled for faster initial sync using NiPoPoW proofs.

## Resource Considerations

*   **Memory (RAM):** While lighter than archive mode, digest nodes still require sufficient RAM, especially during bootstrapping. Users have reported needing to increase the JVM heap space using the `-Xmx` flag (e.g., `java -Xmx1G -jar ...` or higher) particularly when bootstrapping on resource-constrained devices like mobile phones. Monitor your node's memory usage.
*   **Disk Space:** Significantly lower than archive mode. With `nipopowBootstrap` and a reasonable `blocksToKeep` value (like 1440), the storage footprint after sync can be relatively small (potentially under 1GB, but this can vary). Using `utxoBootstrap` might require more temporary space during the snapshot download.
*   **CPU:** Validation still requires CPU power, but generally less than an archive node maintaining the full UTXO set database.

## Wallet Compatibility

*   **General Support:** Light-fullnodes running in digest mode *can* support wallet functionalities, including managing keys and creating transactions.
*   **Potential Issues:** Some wallet implementations or specific wallet features might have compatibility issues with digest mode. This is because the node doesn't have the full UTXO set readily available locally, and certain queries might rely on that. Developers have reported issues in community channels, particularly concerning wallets needing to scan the full UTXO set or perform complex balance calculations.
*   **Recommendation:** If you intend to use a specific wallet with a digest-mode node, verify its compatibility with the wallet developers or community resources. Standard transaction sending/receiving is generally expected to work.

## Technical Details

The light full-node mode uses a 2-party authenticated dynamic dictionary built on top of the UTXO set. For more information on the technical workflow and implementation details, you can refer to the [light-techworkflow.md](light-techworkflow.md) document.
