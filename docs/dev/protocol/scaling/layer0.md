
# Layer 0 *(Network Layer)*

Layer 0 is known as the *'network'* or *peer-to-peer* (P2P) layer that allows [nodes](install.md) to communicate with each other in a decentralised manner.

The P2P layer facilitates the transmission of data and information across the blockchain network, enabling nodes to share and verify transactions, blocks, and other data. This layer is a critical component because it enables network participants to interact with each other directly without relying on a central authority or intermediary.


## Clients

- [Light clients](nipopow_nodes.md): In Ergo, you can get full-node guarantees without storing the full _UTXO set_, enabling a superior bootstrapping experience and improved block validation times.  
- Quick bootstrapping using [NIPoPoWs](nipopows.md) proofs and UTXO set snapshots in development
- **[Logarithmic space mining](logspace.md)**  allows for *light miners.* Similar to light clients, light miners can bootstrap with block headers without downloading the entire blockchain. Integrating logarithmic space mining in Ergo is possible via a velvet (soft) fork; see this video from Dionysis Zindros from The University of Athens for a [introduction and their progress so far](https://www.youtube.com/watch?v=s05ypkSC7gk).


## Bloat

**State Bloat:** One of Ergo's major strengths when scaling is to avoid bloat without compromising functionality. 

- Persistent updateable storage is possible, with updates to be checked by a blockchain contract. However, only the digest of the authenticated data structure (and some additional bytes, less than 40) is stored in the UTXO set regardless of the data set size. 
- Ergo utilises a [Storage Rent](rent.md) Fee to prevent spam and recirculate unused data bytes, known as dust. Storage Rent Fee helps clean the network pollution and encourages users to be more active.


## Miner-adjusted parameters. 

**Block size:** Parameters like block size are not set in stone and can be adjusted by miners. So miners experiencing low full block validation time (as hardware improves with time and software) they may propose or vote to increase the block size. Currently set to `8MB`.

**Transaction size:** As of node `4.0.23`, there is a transaction size limit of `96kb` for the mempool. Larger transactions can only be included manually by miners. 

