# Layer 0 - Network Layer

Layer 0, also known as the *Network* or *Peer-to-Peer* (P2P) layer, facilitates decentralized communication between [nodes](install.md) in a blockchain network.

This layer is crucial as it enables the transmission of data and information across the network, allowing nodes to share and verify transactions, blocks, and other data without the need for a central authority or intermediary.

## Clients

- [Light clients](nipopow_nodes.md): These clients provide full-node guarantees without storing the entire UTXO set, resulting in a superior bootstrapping experience and improved block validation times.
- Quick bootstrapping: This is achieved using [NIPoPoWs](nipopows.md) proofs and UTXO set snapshots, which are currently in development.

Ergo also supports **[Logarithmic space mining](logspace.md)**, which allows for *light miners*. Similar to light clients, light miners can bootstrap with block headers without downloading the entire blockchain. This feature can be integrated into Ergo via a velvet (soft) fork. For an introduction and progress update, watch this [video](https://www.youtube.com/watch?v=s05ypkSC7gk) by Dionysis Zindros from The University of Athens.

## State Bloat

Ergo effectively manages state bloat without compromising functionality:

- Persistent updatable storage: Ergo allows updates to be checked by a blockchain contract. However, only the digest of the authenticated data structure (and some additional bytes, less than 40) is stored in the UTXO set, regardless of the data set size.
- [Storage Rent](rent.md) Fee: Ergo uses a Storage Rent Fee to prevent spam and recirculate unused data bytes, known as dust. This fee helps clean network pollution and encourages users to be more active.

## Miner-Adjusted Parameters

Ergo allows miners to adjust certain parameters:

- **Block size:** This parameter is not fixed and can be adjusted by miners. If miners experience low full block validation time (as hardware and software improve over time), they may propose or vote to increase the block size, which is currently set to `8MB`.
- **Transaction size:** As of node `4.0.23`, there is a transaction size limit of `96kb` for the mempool. Larger transactions can only be included manually by miners.

For more information, see the [Governance](governance.md) section.