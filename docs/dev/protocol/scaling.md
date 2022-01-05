Ergo Platform has a research-based approach for long-term success and has a lot in its toolbox to tackle scaling.

The general idea is that large chunks of transactions can happen on layer 2, and be settled in Ergo using a single transaction. Thanks to the high flexibility of the ErgoScript programming model, many different protocols will be possible on layer2, each one solving scalability problems in a specific domain (like simple payment transactions which could be sped up with sub-block confirmation protocols). 

**Thus, Ergo can be considered a common *settlement layer* for many Level-2 protocols and applications.**


## Layers

- Layer 0 **(Peer 2 Peer)**. The Ergo Node Client has improved a lot since v4.0.8 and still has room to grow. Quick bootstrapping using [NiPoPoWs](/docs/node/nipopow.md) proofs and UTXO set snapshots in development
- Layer 1, **(application layer)**, Ergo supports multiple on-chain scalability solutions such as Sharding.
- Layer 2 **(off-chain)**. Ergo can utilise multiple off-chain solutions, such as [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains to compress blockchain bloat and provide similar benefits as zk-rollups. Ergo can also be compatible with other UTXO Layer 2 solutions, such as Bitcoin's Lightning Network. The implementation here will depend on the needs of the applications being built on Ergo.



## Layer 1

With the release of v5 the raw TPS numbers should bring us to around 47.5tx/s - improvements on top of this are still possible.

**However, TPS is mostly a vanity metric.** It's not about how many transactions you can do but rather, the computational cost, or gas limit per block. The cost limit depends on the hardware miners have, size of the network, and other factors. But there is no concrete formula to calculate this. The best path forward is to log transaction profiles once DeFi on Ergo becomes more established and do load testing in the testnet.


### Stateless Clients

Stateless clients allow light wallets and light miners to run with full node security. NIPoPoW implementation via Velvet soft forks will enable infinite sidechains on top of Ergo. 

### State Bloat

About scaling, the main approach is to avoid bloat without compromising functionality. E.g. persistent updateable storage is possible, with updates to be checked by a blockchain contract, but only digest of authenticated data structure (and some additional bytes, less than 40 bytes anyway) are stored in the UTXO set dependless on data set size. Storage rent is helping to remove dust from the UTXO set. Then light clients: in Ergo you can have full-node guarantees without storing UTXO set, if you do not mine. That’s about much improved boostrapping and block validation times. With such improvements, it is possible to raise TPS without compromising classic blockchain assumptions and guarantees. 


Ergo utilises "[Storage Rent Fee](https://ergoplatform.org/en/blog/2021-07-09-cryptocurrency-fees-a-solution-to-unreasonable-state-growth/)" to prevent spam and recirculate unused data bytes, known as dust. Storage Rent Fee helps clean the network pollution and encourages users to be more active.

### Block size

Parameters like block size etc are not set in stone, rather, miners can adjust them. So if a miner is experiencing low full block validation time (as hardware is getting better with time, as well as software), he may propose or vote to increase block size.

### Sharding

- [On the Security and Performance of Blockchain Sharding](https://eprint.iacr.org/2021/1276)

## Layer 2

### Sub-block confirmation 

Sub-block confirmation protocols ([Bitcoin-NG](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf) or [Flux](https://www.usenix.org/system/files/atc20-li-chenxing.pdf), topic for research in 2022 )

### Plasma

Plasma is a layer-2 scaling solution that was originally proposed by Joseph Poon and Vitalik Buterin in their paper Plasma: Scalable Autonomous Smart Contracts. It is a framework for building scalable applications. Plasma uses a combination of smart contracts and cryptographic verification.

Ergo implementation is currently being researched.


### Lightning Network 

Due to the shared UTXO architecture utilising Bitcoins Lightning network is also a possibility.

### Hydra

Ergo is mentioned in the Hydra whitepaper.

### ZK-Rollups

Zero-Knowledge Rollups 

## Resources

- [Roadmap](https://ergonaut.space/en/roadmap)
- [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)
- [Network congestion on Jul, 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)
