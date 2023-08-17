---
tags:
  - Snapshots
  - nipopows
---

# Pruned Full-Node Mode

[Ergo Protocol Reference Client 5.0.13](https://github.com/ergoplatform/ergo/releases/tag/v5.0.13) introduced bootstrapping using a combination of a *verified UTXO set snapshot* and [NiPoPoWS](nipopows.md). This enables full node security on a standard laptop within minutes, avoiding the need to check about 95% of the blockchain. Addressing the growing requirements for downloading, storing, and processing the entire blockchain.

This mode is similar to Ethereum protocol clients' *fast-sync* in Geth or Grothendieck and *warp-mode* in Parity, but with more aggressive optimizations.

## Getting Started

> Please note, that you cannot restore an old wallet with a pruned node, your best option is to create a new wallet and transfer funds across.

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


## Technical Details

The UTXO set authentication uses an AVL+ tree, outlined in [this research paper](https://eprint.iacr.org/2016/994.pdf) and available in the [Scrypto framework](https://github.com/input-output-hk/scrypto). [This research paper](https://eprint.iacr.org/2018/129) indicates that this method can be as secure as processing all blocks under certain statistical assumptions. 

For more information see the [Technical Details](pruned-impl.md).