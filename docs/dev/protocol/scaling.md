Ergo Platform has a research-based approach for long-term success and has a lot in its toolbox to tackle the scaling.


## Layers

- Layer 0 **(Peer 2 Peer)**. The Ergo Node Client has improved a lot since v4.0.8 and still has room to grow. Quick bootstrapping using [NiPoPoWs](/docs/node/nipopow.md) proofs and UTXO set snapshots in development
- Layer 1, **(application layer)**, Ergo supports multiple on-chain scalability solutions such as Sharding.
- Layer 2 **(off-chain)**. There are multiple off-chain solutions Ergo can utilise such as [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains to compress blockchain bloat and provide similar benefits as zk-rollups. Ergo can also be compatible with other UTXO Layer 2 solutions such as Bitcoin’s Lightning Network. The implementation here will depend on the needs of the applications being built on Ergo.

## Settlement Layer

> The general idea, roughtly, is that large chunks of transactions can happen in layer 2 and the whole chunks will be settled in Ergo blockchain using single transaction. Thanks to the high flexibility of ErgoScript programming model, many different protocols will be possible on layer2, each one solving scalability problem in a specific domain (like simple payment transactions).

> Thus, Ergo blockchain can be thought as common settlement layer for many level2 protocol and applications.

## TPS

TPS: v5 should be possible of 47.5tx/s - improvements ontop of this still possible.


## Stateless Clients

Stateless clients allow for both light wallets and light miners to run with full node security. NIPoPoW implementation via Velvet soft forks will enable infinite sidechains on top of Ergo. 


## State Bloat

Ergo utilizes "[Storage Rent Fee](https://ergoplatform.org/en/blog/2021-07-09-cryptocurrency-fees-a-solution-to-unreasonable-state-growth/)" to prevent spam and recirculate unused data bytes, known as dust. Storage Rent Fee helps to clean the network pollution and encourages users to be more active.




## Resources

- [Roadmap](https://ergonaut.space/en/roadmap)
- [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)
- [Network congestion on Jul, 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)
