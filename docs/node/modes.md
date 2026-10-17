---
tags:
  - Node
  - Modes
  - Full Node
  - Pruned Node
  - Light Node
  - Digest Node
  - Stateless Node
  - SPV
  - Configuration
  - Comparison
---

# Node Modes of Operation

*(Back to: [Node Installation](install.md))*

The [Ergo node](install.md) offers several modes of operation, allowing users to balance resource requirements (disk space, memory, bandwidth) with security assumptions and desired functionality. Choosing the right mode depends on your specific use case, such as running a backend for a dApp, securing personal funds, or simply verifying transactions.

The primary modes are configured using settings in your `ergo.conf` file, mainly `ergo.node.stateType` and `ergo.node.blocksToKeep`. Bootstrapping options like `ergo.node.utxo.utxoBootstrap` and `ergo.node.nipopow.nipopowBootstrap` can significantly speed up the initial synchronization for compatible modes but do not define the mode itself.

Here's a comparison of the main operational modes:

## Mode Comparison

| Feature / Mode        | [Archival Full Node](archival-node.md) | [Pruned Full Node](pruned-full-node.md) | [Digest (Stateless) Node](light-full-node.md)¹ | [Light SPV Client](light-spv-node.md) |
| :-------------------- | :------------------------------------------- | :-------------------------------------------- | :-------------------------------------------------- | :------------------------------------------ |
| **Primary Goal**      | Max Security, Full History                   | Full Security, Reduced Storage                | Full Security, Minimal Storage                      | Tx Verification, Minimal Resources          |
| **Key Config**        | `stateType="utxo"`<br>`blocksToKeep=-1`      | `stateType="utxo"`<br>`blocksToKeep > 0`      | `stateType="digest"`<br>`blocksToKeep > 0`         | N/A (Client Software)                       |
| **Bootstrapping**     | Full Sync from Genesis | Full Sync / UTXO Snapshot (`utxoBootstrap=true`) / NiPoPoW (`nipopowBootstrap=true`) | Full Sync / NiPoPoW (`nipopowBootstrap=true`)¹ | NiPoPoW Sync |
| **Storage (Initial)** | Very High (100s GB+) | Medium (Snapshot: ~1-2GB + Recent Blocks) | Low (Headers + State: ~1-3GB + Recent Blocks) | Very Low (MBs) |
| **Storage (Ongoing)** | High (Grows with chain) | Medium (Grows slowly with `blocksToKeep`) | Low (Grows slowly with `blocksToKeep`) | Very Low |
| **Resource Needs**    | High (CPU/RAM/Disk IO) | Moderate | Moderate-Low | Very Low |
| **Sync Time**         | Very Long          | Fast (with bootstrap) | Fast (with bootstrap) | Very Fast |
| **Full Tx Validation**| Yes                | Yes (for kept blocks) | Yes (for kept blocks, via ADProofs) | No (Header validation only) |
| **API Support**       | Full               | Full (for available data) | Limited (May lack endpoints requiring full UTXO set) | N/A (Relies on Full Node API) |
| **Wallet Compatibility**| Full (incl. restore) | New Wallets OK; **No Restore** | New Wallets OK; **No Restore**; Potential issues with standard P2P tx submission reported² | Verification only; Relies on Full Node for tx submission/balance |
| **Use Cases**         | Mining, Archiving, Max Trust Backend | dApp Backend, Personal Wallet Backend (New Wallet) | Mobile Node Backend ([Android Guide](node-android.md)), dApp Backend (Specific Needs), Personal Wallet Backend (New Wallet, check compatibility) | Light Wallets, Quick Verification Tools |

**Detailed Explanations & Notes:**

1. **Bootstrapping (`utxoBootstrap`, `nipopowBootstrap`):**
    * UTXO snapshot bootstrap downloads the UTXO set at a checkpoint and then applies later blocks. It requires `stateType="utxo"`.
    * NiPoPoW bootstrap obtains the header chain through a proof and can be used with either UTXO or Digest state. It requires UTXO snapshot bootstrap or a nonnegative `blocksToKeep` value.
    * For a UTXO node, `ergo.node.utxo.utxoBootstrap=true` can be combined with `ergo.node.nipopow.nipopowBootstrap=true` to bootstrap both the state and the headers.
    * Note ¹: For a Digest node, keep `ergo.node.utxo.utxoBootstrap=false`. The Digest + UTXO snapshot combination is unsupported; enabling it does not provide a working snapshot sync. To bootstrap a pruned Digest node, use `stateType="digest"`, a positive `blocksToKeep` value, and `ergo.node.nipopow.nipopowBootstrap=true`.
    * **Progress Indication:** Be aware that the initial download phase when using bootstrapping (especially `utxoBootstrap`) can take a significant amount of time depending on network speed and peer availability. The node logs may not show detailed progress during large snapshot downloads. It's often helpful to monitor your system's network activity or the increasing size of the node's data directory (`.ergo/snapshots` or similar) to gauge progress during this phase.

2. **Digest Mode (`stateType="digest"`) Limitations:**
    * This mode keeps only an authenticated digest (root hash) of the UTXO set, verifying state transitions using [ADProofs](block-adproofs.md) contained in blocks.
    * **Wallet Compatibility:** While functional for creating new wallets and basic operations, users have reported issues submitting standard P2P transactions from wallets connected *only* to a digest-mode node. Compatibility with specific wallets or dApps requiring full UTXO set access may vary. **Verification is recommended.**
    * **API Limitations:** Some API endpoints that rely on scanning the full UTXO set might not be available or may return limited data.
    * **Peer Relaying:** Digest nodes typically cannot relay transactions received from peers, as they don't validate them against the full UTXO set.

3. **Wallet Restoration (Pruned & Digest Modes):**
    * Nodes running with `blocksToKeep` set to a positive value (Pruned and Digest modes) **cannot** be used to restore wallets from seed phrases if those wallets were used *before* the oldest block kept by the node. They lack the historical transaction data needed for the scan.
    * You **must** use an Archival Full Node (`blocksToKeep = -1`) or a trusted explorer service for restoring older wallets. For new wallets created and used *only* while the pruned/digest node is running, restoration might work, but using an archival node is the safest approach.

4. **Resource Usage:**
    * The storage figures are estimates and depend heavily on the `blocksToKeep` setting and chain activity. A typical light/mobile setup using digest mode with bootstrapping might initially consume around 3GB.
    * Memory requirements (`-Xmx` flag) also vary. While an archival node might need 8GB+, pruned/digest nodes can often run with 2-4GB, though more may be needed during intense activity or bootstrapping.

## Further Reading

* [Configuration File](conf.md)
* [Pruned Full Node Details](pruned-full-node.md)
* [Light Full (Digest) Node Details](light-full-node.md) (Covers `stateType="digest"`)
* [Light SPV Clients / NiPoPoWs](nipopow_nodes.md)
* [History Pruning (`blocksToKeep`)](history-pruning.md)
