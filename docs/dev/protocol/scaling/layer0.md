
# Layer 0 *(Network Layer)*

The network or *peer to peer* layer. The Ergo Node Client has greatly improved since v4.0.8 and still has room to grow. Quick bootstrapping using [NIPoPoWs](nipopows.md) proofs and UTXO set snapshots in development

## Clients

**Stateless Clients:** [Light clients](nipopow_nodes.md): In Ergo, you can get full-node guarantees without storing the full _UTXO set_, enabling a superior bootstrapping experience and improved block validation times.  

## Bloat

**State Bloat:** One of Ergo's major strengths when scaling is to avoid bloat without compromising functionality. For E.g. persistent updateable storage is possible, with updates to be checked by a blockchain contract. However, only the digest of the authenticated data structure (and some additional bytes, less than 40) is stored in the UTXO set regardless of the data set size. Ergo utilizes a [Storage Rent Fee](rent.md) to prevent spam and recirculate unused data bytes, known as dust. Storage Rent Fee helps clean the network pollution and encourages users to be more active.

**[Logarithmic space mining](logspace.md)**  allows for *light miners.* Similar to light clients, light miners can bootstrap with block headers without downloading the entire blockchain. Integrating logarithmic space mining in Ergo is possible via a velvet (soft) fork; see this video from Dionysis Zindros from The University of Athens for a [introduction and their progress so far](https://www.youtube.com/watch?v=s05ypkSC7gk).

## Miner-adjusted parameters. 

**Block size:** Parameters like block size, etc., are not set in stone; miners can adjust them. So if a miner is experiencing low full block validation time (as hardware is getting better with time and software), he may propose or vote to increase the block size. Currently set to `8MB`.

**Transaction size:** As of node `4.0.23`, there is a transaction size limit of `96kb` for the mempool. Larger transactions can only be included manually by miners. 

