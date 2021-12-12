Ergo Platform has a research-based approach for long-term success and has a lot in its toolbox to tackle scaling.


## Layers

- Layer 0 **(Peer 2 Peer)**. The Ergo Node Client has improved a lot since v4.0.8 and still has room to grow. Quick bootstrapping using [NiPoPoWs](/docs/node/nipopow.md) proofs and UTXO set snapshots in development
- Layer 1, **(application layer)**, Ergo supports multiple on-chain scalability solutions such as Sharding.
- Layer 2 **(off-chain)**. Ergo can utilise multiple off-chain solutions, such as [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains to compress blockchain bloat and provide similar benefits as zk-rollups. Ergo can also be compatible with other UTXO Layer 2 solutions, such as Bitcoin's Lightning Network. The implementation here will depend on the needs of the applications being built on Ergo.

## Settlement Layer

> The general idea is that large chunks of transactions can happen in layer 2, and the whole chunks will be settled in Ergo blockchain using a single transaction. Thanks to the high flexibility of the ErgoScript programming model, many different protocols will be possible on layer2, each one solving scalability problems in a specific domain (like simple payment transactions).

> Thus, the Ergo blockchain can be considered a common settlement layer for many level2 protocols and applications.

## TPS

TPS: v5 should be possible of 47.5tx/s - improvements on top of this are still possible.


## Stateless Clients

Stateless clients allow light wallets and light miners to run with full node security. NIPoPoW implementation via Velvet soft forks will enable infinite sidechains on top of Ergo. 


## State Bloat

Ergo utilises "[Storage Rent Fee](https://ergoplatform.org/en/blog/2021-07-09-cryptocurrency-fees-a-solution-to-unreasonable-state-growth/)" to prevent spam and recirculate unused data bytes, known as dust. Storage Rent Fee helps clean the network pollution and encourages users to be more active.




## Resources

- [Roadmap](https://ergonaut.space/en/roadmap)
- [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)
- [Network congestion on Jul, 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)
