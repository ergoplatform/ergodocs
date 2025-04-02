---
tags:
  - Snapshots
  - nipopows
---

# Pruned Full-Node Mode

The [Ergo Protocol Reference Client 5.0.13](https://github.com/ergoplatform/ergo/releases/tag/v5.0.13) introduced a new feature: bootstrapping using a *verified UTXO set snapshot* and [NiPoPoWS](nipopows.md). This feature allows you to achieve full node security on a standard laptop within minutes, eliminating the need to check approximately 95% of the blockchain. This addresses the increasing demands for downloading, storing, and processing the entire blockchain.

This mode is akin to the *fast-sync* in Geth or Grothendieck and *warp-mode* in Parity, used by Ethereum protocol clients, but with more aggressive optimizations.

## Getting Started

> Important: You cannot restore an old wallet with a pruned node. The recommended approach is to create a new wallet and transfer funds to it.

Add the following `utxo` and `nipopow` sections to your node configuration to enable UTXO Set Snapshots. 

```conf
ergo {
    node {
        mining = false

        utxo {
           utxoBootstrap = true
           storingUtxoSnapshots = 0
        }
        nipopow {
           nipopowBootstrap = true
           p2pNipopows = 2
        }
    }
    
}

scorex {
    restApi {
        apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
    }
}
```

**Note on Progress Reporting:** Currently, the node may not provide detailed progress updates specifically during the *download phase* of the UTXO snapshot itself when `utxoBootstrap = true`. Synchronization progress for headers and subsequent blocks is typically visible via the node panel (`/panel`) or logs, but the snapshot download phase might appear as a period of inactivity before regular block processing resumes.

## Technical Details

The UTXO set authentication uses an AVL+ tree, outlined in [this research paper](https://eprint.iacr.org/2016/994.pdf) and available in the [Scrypto framework](https://github.com/input-output-hk/scrypto). [This research paper](https://eprint.iacr.org/2018/129) indicates that this method can be as secure as processing all blocks under certain statistical assumptions. 

For more information see the [Technical Details](pruned-impl.md).
