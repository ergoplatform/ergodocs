Ergo Platform has a research-based approach for long-term success and has a lot in its toolbox to tackle scaling as we grow. Which options we implement will depend on the needs of applications building on top of Ergo, as well as the success of the solutions in other protocols. 

**TPS (Transactions per second)**

To get the elephant out the room - *'What is the TPS (Transactions per second) '* It's important to keep in mind that **TPS is mostly a vanity metric.** It's not about how many transactions you can do but rather the weight of those transactions and the computational cost limit per block. This cost limit depends on the hardware miners have, the size of the network, and other dynamic factors but there is no concrete formula to calculate scalability. The best path forward is to log transaction profiles once DeFi on Ergo becomes more established and perform load testing in the testnet. With the release of v5, the raw TPS numbers should bring us to around 47.5tx/s - improvements on top of this are still possible. The focus is on raising TPS without compromising classic blockchain assumptions and guarantees. 

Thanks to the high flexibility of the ErgoScript programming model, large chunks of transactions can happen on layer two and be settled in Ergo using a single transaction. Many different protocols will be possible on layer2, each one solving scalability problems in a specific domain (like simple payment transactions, sped up with sub-block confirmation protocols). [We are already seeing the beginnings of the strengths of eUTXO take shape with anetaBTC airdropping 3,000 wallets in a single transaction](https://twitter.com/HazeyOneKenobi/status/1481775230297288706). 

**Ergo can be considered a common *settlement layer* for many Level-2 protocols and applications.**


## Layer 0 *(Network Layer)*

The network or *peer to peer* layer. The Ergo Node Client has improved a lot since v4.0.8 and still has room to grow. Quick bootstrapping using [NiPoPoWs](/docs/node/nipopow.md) proofs and UTXO set snapshots in development

**Stateless Clients:** Then light clients: You can have full-node guarantees in Ergo without storing the full *UTXO set*. Bringing improved bootstrapping and block validation times.  

**State Bloat:** One of Ergo's major strengths when scaling is to avoid bloat without compromising functionality. E.g. persistent updateable storage is possible, with updates to be checked by a blockchain contract. However, only the digest of the authenticated data structure (and some additional bytes, less than 40 bytes anyway) are stored in the UTXO set regardless of data set size. Ergo utilizes a [Storage Rent Fee](https://ergoplatform.org/en/blog/2021-07-09-cryptocurrency-fees-a-solution-to-unreasonable-state-growth/) to prevent spam and recirculate unused data bytes, known as dust. Storage Rent Fee helps clean the network pollution and encourages users to be more active.

**Block size:** Parameters like block size etc., are not set in stone; rather, miners can adjust them. So if a miner is experiencing low full block validation time (as hardware is getting better with time and software), he may propose or vote to increase the block size.

**Logarithmic space mining:**  allows for *light miners.* Similar to light clients, light miners can bootstrap with block headers without downloading the entire blockchain. Integrating logarithmic space mining in Ergo is possible via a velvet (soft) fork; see this video from Dionysis Zindros from The University of Athens for a [introduction and their progress so far](https://www.youtube.com/watch?v=s05ypkSC7gk).

## Layer 1 (Blockchain)

Ergo supports multiple on-chain scalability solutions such as Sharding.

**Sub-block confirmation protocols:** such as ([Bitcoin-NG](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf) or [Flux](https://www.usenix.org/system/files/atc20-li-chenxing.pdf) are an active topic for research in 2022. Ergo blocks have *extension sections* with **mandatory and arbitrary key-value data**; by putting certain anchors there, it is possible to do BitcoinNG-style micro blocks, Aspen-like service-chains or generic sidechains with just velvet or soft forks. Also see *[Flux: Revisiting Near Blocks for Proof-of-Work Blockchains](https://eprint.iacr.org/2018/415.pdf)*

**Sharding:** as per [On the Security and Performance of Blockchain Sharding](https://eprint.iacr.org/2021/1276)

## Layer 2 (Off-Chain)

Ergo can utilize multiple off-chain solutions, such as [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains to compress blockchain bloat and provide similar benefits as zk-rollups. Ergo can also be compatible with other UTXO Layer 2 solutions, such as Bitcoin's Lightning Network. The implementation here will depend on the applications being built on Ergo.

### Research & Development

**Plasma Chains:** This is a hybrid approach (applied by Polygon) that uses a proof-of-stake (PoS) consensus layer on top of Ethereum. This parallel sidechain, which is based on the [plasma chains](https://ethereum.org/en/developers/docs/scaling/plasma/) design, is a lower-cost chain that relies on stakeholders to secure the network. As the staking tokens interact with the main chain, the model uses some part of Ethereum's security and its own inside PoS consensus. When users stake their tokens, they delegate the consensus to a validating operator, known as trusted and secure server providers. An Ergo implementation is currently being researched.

> Plasma tutorials for Ergo have now been released. Please see [Bank](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/avltree/bank/Bank.md) & [AVLTrees](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/avltree/AvlTrees.md)

**NIPoPoWs:** [Non-interactive proofs of proof of work](http://docs.ergoplatform.org/dev/protocol/nipopow/) are essential for two reasons: Light Clients and Side Chains. Light clients, which consist of light nodes and light wallets, are efficient clients that do not need to hold the whole blockchain to verify transactions and enable efficient mobile wallets and faster miner bootstrapping. Clients can interact using only the block headers, thus reducing computational resources. Ergo has enabled NIPoPoW support since the genesis block. They can be applied to Ergo's blockchain with an easy to implement [velvet fork](https://www.coindesk.com/markets/2018/03/15/velvet-forks-crypto-updates-without-the-controversy/). NIPoPoWs can also be deployed to support PoW and PoS cross-chain communication. NIPoPoW implementations via *Velvet soft forks* enable **infinite scalability** via sidechains on top of Ergo. 

**State Channels (Hydra):** is a *peer-to-peer signing model*, and the design can works well for payment channels for simple purposes. The problem, however, is the state channels are pre-set contracts for which the participants are defined at the launch. Each time a new participant wants to use the channel, a new contract creation is needed. In return, there is higher privacy and security but little to no flexibility for an open system. IOHK have published a new model called [Hydra: Isomorphic State Channels](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) that introduces multi-party state channels by utilizing both on-chain and off-chain computations powered by the eUTXO design. Other novel state channel constructions should be possible as well. It would be good to apply off-chain techniques to applications like ErgoMixer. Ergo is mentioned in the [Hydra whitepaper](https://eprint.iacr.org/2020/299.pdf). Research and discussions are underway. 


### Other Possibilities

**Lightning Network:** Due to the shared UTXO architecture utilizing Bitcoins, the Lightning network is also possible. Basically, in a lightning channel, two participants send their funds to a specific type of joint multisig wallet that allows them to create and enforce off-chain agreements. The network itself is just a bunch of these channels connected. You can then structure an off-chain payment across many channels, where none of the funds leaves any individual channel but instead shuffles around like an abacus.

**Rainbow Network:** as described in [this paper](http://research.paradigm.xyz/RainbowNetwork.pdf)

**ZK-Rollups:** utilize [zkSNARKs](https://blog.ethereum.org/2016/12/05/zksnarks-in-a-nutshell/) (zero-knowledge succinct non-interactive arguments of knowledge), they can decrease network load by taking hundreds of transfers off-chain and combining or "rolling" them up into a single transaction. The security of the transactions relies directly on the main chain secured by adding mathematical proofs to validate transactions. However, it is relatively harder than hybrid approaches to implement all the functionalities of the mainnet with full security. Various projects are attempting to implement zkSNARKs.

**Optimistic Rollups:** compute the transactions on a parallel EVM compatible chain called Optimistic Virtual Machine (OVM) that communicates with the main chain. The model is optimistic because it relies on the *Fraud-Proof principle*, where the aggregators are not actively verifying layer two. Still, they interfere in the event of a fraud dispute.

**Zero-Knowledge Contingent Payments:** It's possible to make payments that are released if and only if the payee discloses some knowledge (in a trustless manner where neither the payer nor payee can cheat). This is achieved using the combination of a `hash-locked transaction` and an external protocol to ensure the correct data is revealed in the hash lock release.

**FairSwap/FastSwap protocols:** As described in [this paper](https://eprint.iacr.org/2019/1296)

**Coinpools:** Another L2 solution for the UTXO model to consider as described in [this paper](https://discrete-blog.github.io/coinpool/)


## Resources

- [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)
- [Network congestion on Jul, 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)
- [Long-term vision for Ergo](https://www.ergoforum.org/t/long-term-vision-for-ergo/2629)