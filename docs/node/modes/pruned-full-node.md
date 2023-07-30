---
tags:
  - Snapshots
  - nipopows
---

# Pruned Full-Node Mode using UTXO Set Snapshots

## Overview and Motivation

[Ergo Protocol Reference Client 5.0.13](https://github.com/ergoplatform/ergo/releases/tag/v5.0.13) introduces the possibility of booting with a *verified UTXO set snapshot* and [NiPoPoWS](nipopows.md). This enables full node security on a standard laptop within 30-60 minutes, avoiding the need to check about 95% of the blockchain. It addresses the growing requirements for downloading, storing, and processing the entire blockchain in evolving systems like [Ergo](https://www.ergoplatform.com/) and [Ethereum](https://ethereum.org/).

The UTXO set authentication uses an AVL+ tree, outlined in [this research paper](https://eprint.iacr.org/2016/994.pdf) and available in the [Scrypto framework](https://github.com/input-output-hk/scrypto) on GitHub. Snapshots are taken every 51,200 blocks (~72 days), specifically after a block where *h % 51200 == 51199*.

This mode is similar to Ethereum protocol clients' *fast-sync* in Geth or Grothendieck and *warp-mode* in Parity, but with more aggressive optimizations.

[This research paper](https://eprint.iacr.org/2018/129) indicates that this method can be as secure as processing all blocks under certain statistical assumptions. Downloading and applying a historical UTXO set snapshot, along with subsequent full blocks, significantly reduces resource strain, encouraging broader blockchain adoption.

## Enabling

Add the following `utxo` and `nipopow` sections to your node configuration to enable UTXO Set Snapshots. 

```conf
ergo {
    node {
        mining = false
    }
    utxo {
        utxoBootstrap = true
        storingUtxoSnapshots = 0
    }
    nipopow {
        nipopowBootstrap = true
        p2pNipopows = 2
    }
}

scorex {
    restApi {
        apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
    }
}

```
