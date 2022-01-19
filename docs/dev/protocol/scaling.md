Ergo Platform has a research-based approach for long-term success and has a lot in its toolbox to tackle scaling.

The node has seen great improvements recently (starting from 4.0.8), significant improvements are still possible by just optimizing the node code.

Implementations for bootstrapping with NiPoPoW proofs and UTXO set snapshots are in development. Then we can think about sub-block confirmation protocols and L2.

## Layers

- **Layer 0** *(Network Layer)*. The Ergo Node Client has improved a lot since v4.0.8 and still has room to grow. Quick bootstrapping using [NiPoPoWs](/docs/node/nipopow.md) proofs and UTXO set snapshots in development
- **Layer 1** *(Application Layer)*, Ergo supports multiple on-chain scalability solutions such as Sharding.
- **Layer 2** *(off-chain)*. Ergo can utilise multiple off-chain solutions, such as [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains to compress blockchain bloat and provide similar benefits as zk-rollups. Ergo can also be compatible with other UTXO Layer 2 solutions, such as Bitcoin's Lightning Network. The implementation here will depend on the needs of the applications being built on Ergo.

Large chunks of transactions can happen on layer 2, and be settled in Ergo using a single transaction. Thanks to the high flexibility of the ErgoScript programming model, many different protocols will be possible on layer2, each one solving scalability problems in a specific domain (like simple payment transactions which could be sped up with sub-block confirmation protocols). 

**Thus, Ergo can be considered a common *settlement layer* for many Level-2 protocols and applications.**

## Layer 0

### Stateless Clients

Stateless clients allow light wallets and light miners to run with full node security. NIPoPoW implementation via Velvet soft forks will enable infinite sidechains on top of Ergo. 

### State Bloat

About scaling, the main approach is to avoid bloat without compromising functionality. E.g. persistent updateable storage is possible, with updates to be checked by a blockchain contract, but only digest of authenticated data structure (and some additional bytes, less than 40 bytes anyway) are stored in the UTXO set regardless of data set size. Storage rent is helping to remove dust from the UTXO set. Then light clients: in Ergo you can have full-node guarantees - without storing the full **UTXO set** (assuming you do not mine). This should bring a much-improved bootstrapping and block validation times. With such improvements, it is possible to raise TPS without compromising classic blockchain assumptions and guarantees. 


Ergo utilises "[Storage Rent Fee](https://ergoplatform.org/en/blog/2021-07-09-cryptocurrency-fees-a-solution-to-unreasonable-state-growth/)" to prevent spam and recirculate unused data bytes, known as dust. Storage Rent Fee helps clean the network pollution and encourages users to be more active.

### Block size

Parameters like block size etc are not set in stone, rather, miners can adjust them. So if a miner is experiencing low full block validation time (as hardware is getting better with time, as well as software), he may propose or vote to increase the block size.

## Layer 1

### Sharding

- [On the Security and Performance of Blockchain Sharding](https://eprint.iacr.org/2021/1276)

### Sub-block confirmation 

Sub-block confirmation protocols such as ([Bitcoin-NG](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf) or [Flux](https://www.usenix.org/system/files/atc20-li-chenxing.pdf) are an active topic for research in 2022.

An Ergo block has *extension section* with **mandatory and arbitrary key-value data**, By putting certain anchors there it is possible to do BitcoinNG-style microblocks, Aspen-like service-chains or generic sidechains with just velvet or soft forks. 

## Layer 2 (Off-chain Protocols)


**Lightning Network:** Due to the shared UTXO architecture utilising Bitcoins Lightning network is also a possibility. Layer 2 solutions also have validator nodes, so their security is not always tied solely to the main chain. For example, [Lightning Network](http://lightning.network/how-it-works/) is a Bitcoin scaling solution and it also has its own nodes that validate transactions. There are no mining rewards for hosting a Lightning Network node so the node operator income relies solely on transaction fees.

**Rainbow Network** as described in [this paper](http://research.paradigm.xyz/RainbowNetwork.pdf)

**Plasma Chains:** This is a hybrid approach (which is applied by Polygon) that uses a proof-of-stake (PoS) consensus layer on top of Ethereum. This parallel side-chain, which is based on the [plasma chains](https://ethereum.org/en/developers/docs/scaling/plasma/) design, is a lower-cost chain that relies on stakeholders to secure the network. As the staking tokens interact with the main chain, the model uses some part of Ethereum’s security and some part of its own inside PoS consensus. When users stake their tokens, they delegate the consensus to a validating operator, known as trusted and secure server providers. An Ergo implementation is currently being researched.

**ZK-Rollups:** utilise [zkSNARK](https://blog.ethereum.org/2016/12/05/zksnarks-in-a-nutshell/)s (zero-knowledge succinct non-interactive arguments of knowledge), they can decrease network load by taking hundreds of transfers off-chain and combining or "rolling" them up into a single transaction. The security of the transactions relies directly on the main chain secured by adding mathematical proofs to validate transactions. However, it is relatively harder than hybrid approaches to implement all the functionalities of the mainnet with full security. Various projects are developing their approach for implementing zkSNARKs.

**Optimistic Rollups:** [Optimistic Rollups](https://docs.ethhub.io/ethereum-roadmap/layer-2-scaling/optimistic_rollups/) work a little bit differently than plasma and zkSNARK in terms of securing the layer. Optimistic rollups compute the transactions on a parallel EVM compatible chain called Optimistic Virtual Machine (OVM) and communicate with the main chain. The model is called optimistic because it relies on the Fraud-Proof principle, where the aggregators are not actively verifying layer 2 but they interfere in the event of a fraud dispute. 

**State Channels:** Lastly, a model called state channel is a type of peer-to-peer signing model and the design can also be used as payment channels for simple purposes. The problem, however, is the state channels are pre-set contracts for which the participants are defined at the launch. Each time a new participant wants to use the channel, a new contract creation is needed. In return, there is higher privacy and security but little to no flexibility for an open system. IOHK research members published a new model called [Hydra: Isomorphic State Channels](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) that introduces multi-party state channels by utilizing both on-chain and off-chain computations powered by the eUTXO design. Other novel state channel constructions should be possible possible as well. It would be good to apply offchain techniques to certain applications, such as ErgoMixer.

**NIPoPoWs:** [Non-interactive proofs of proof of work](http://docs.ergoplatform.org/dev/protocol/nipopow/) is a generalized term that refers to light clients and side-chains. Light clients, which consist of light nodes and light wallets, are efficient clients that do not need to hold the whole blockchain to verify transactions and enable efficient mobile wallets and faster miner bootstrapping. Clients can interact with each other using only the block headers, thus reducing computational resources. Ergo has enabled NIPoPoW support since the genesis block and they can be applied to Ergo’s blockchain with an easy to implement [velvet fork](https://www.coindesk.com/markets/2018/03/15/velvet-forks-crypto-updates-without-the-controversy/). NIPoPoWs can also be deployed to support PoW and PoS cross-chain communication.

**Zero-Knowledge Contingent Payments**

**FairSwap/FastSwap protocols**

As described in [this paper](https://eprint.iacr.org/2019/1296)

**Coinpools**

Another L2 solution for the UTXO model to consider as described in [this paper](https://discrete-blog.github.io/coinpool/)



### Hydra

Ergo is mentioned in the [Hydra whitepaper](https://eprint.iacr.org/2020/299.pdf). Research and discussions are underway. 



## TPS

With the release of v5 the raw TPS numbers should bring us to around 47.5tx/s - improvements on top of this are still possible.

**However, TPS is mostly a vanity metric.** It's not about how many transactions you can do but rather, the computational cost, or gas limit per block. The cost limit depends on the hardware miners have, size of the network, and other factors. But there is no concrete formula to calculate this. The best path forward is to log transaction profiles once DeFi on Ergo becomes more established and do load testing in the testnet.


## Resources

- [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)
- [Network congestion on Jul, 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)


