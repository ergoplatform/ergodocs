# Layer 2 (Off-Chain)

Layer 2 refers to the secondary protocol or system built on top of a [Layer 1](layer1.md) blockchain protocol. 

Layer 2 solutions aim to enhance the underlying blockchain's functionality, scalability, and efficiency by enabling *off-chain* transactions or computations.

Ergo is compatible with many Layer 2 solutions from other UTXO blockchains, such as Bitcoin's Lightning Network, and can utilise multiple off-chain solutions, such as [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains, to compress blockchain bloat and provide similar benefits as ZK-rollups. 

The specific Layer 2 solutions that are implemented on Ergo will depend on the needs of the applications being built.

> Join the Layer 2 chat on [Telegram](https://t.me/ErgoLayer2) or [Discord]()

## ErgoScript

The [ErgoScript](ergoscript.md) programming model is highly flexible, allowing for large portions of transactions to occur on Layer 2 and then be settled on the Ergo blockchain using a single transaction. For example, here you can see a developer harnessing the power of eUTXO to airdrop native tokens to [10,000 addresses at once](https://explorer.ergoplatform.com/en/transactions/e2c4954665ccf87791f42983ae4f7031205c2e719709907cbf2ff09e5489d4b8). 

ErgoScript includes several improvements, such as time-weighted data, Turing completeness, read-only data inputs, multi-stage contracts, sigma protocols, NIPoPoWs, and more. These improvements enable many different protocols on Layer 2, each solving scalability problems in a specific domain.

> **Therefor, Ergo can be considered a common *settlement layer* for many Level-2 protocols and applications.**


## Plasma

Ergo has native support for [AVL trees](avl.md), an efficient authenticated data structure that allows for proving the data's various properties without knowing the entire set.

The ledger is stored as an AVL tree using **[Plasma](plasma.md)**. Users perform off-chain transactions with the bank, and the ledger keeps changing. Occasionally, the bank publishes a compact snapshot of the ledger on the blockchain.

You can use the [Plasma Library](plasma.md) to create *Plasma chains* and make a full L2 solution. Right now, it is mostly used for data compression and simplifying contracts, though Plasma chains are possible in future.

## NIPoPoWs

[NiPoPoWs](nipopows.md) can potentially be used for scaling by enabling the interoperability of different blockchain networks, which can help reduce the burden on individual chains and distribute the load across multiple networks.

One way this could work is by allowing smaller, less-secure blockchains to leverage the security of larger, more-established chains. For example, a smaller blockchain could periodically submit proofs of work to a larger chain to anchor their own blockchain to the larger network. This would provide the smaller chain with additional security, as well as the ability to transfer assets between chains without the need for a centralized intermediary.

NiPoPoWs could also potentially be used to improve the scalability of layer 2 solutions, such as sidechains or state channels. By enabling these solutions to communicate with each other more efficiently and securely, NiPoPoW could help reduce the load on the main blockchain network and improve transaction throughput.



## Other Possibilities

### **Lightning Network** 

In a lightning channel, two participants send their funds to a specific type of joint multi-sig wallet that allows them to create and enforce off-chain agreements. The network itself is just a bunch of these channels connected. You can then structure an off-chain payment across many channels, where none of the funds leaves any individual channel but shuffles around like an abacus.

### **Rainbow Network** 

The Rainbow Network is an off-chain non-custodial exchange and payment network supporting any assets for which two parties can agree on a price oracle. The Rainbow Network allows users to trade, borrow, lend, and make payments in synthetic assets entirely off-chain while having only one on-chain payment channel collateralised by a single asset.

As described in [this paper](http://research.paradigm.xyz/RainbowNetwork.pdf)

### **Rollups**

Rollups are also possible via AVL trees. A roll-up involves rolling up collections of transactions, and the only concern is posting the data on-chain, not verification. 

There are two main types of *Rollups* used for scaling. 

- **Optimistic Rollups** compute the transactions on a parallel compatible chain that communicates with the main chain. The model is optimistic because it relies on the *Fraud-Proof principle*, where aggregators do not actively verify layer two. Still, they interfere in the event of a fraud dispute. Disputes in optimistic rollups when computations are done only on data whose validity is disputed
    - See this [ergoforum](https://www.ergoforum.org/t/optimistic-rollups-and-fraud-proofs-in-ergo/3819) post for more information.
- **ZK-Rollups** utilise [zkSNARKs](https://blog.ethereum.org/2016/12/05/zksnarks-in-a-nutshell/) (zero-knowledge succinct non-interactive arguments of knowledge), they can decrease network load by taking hundreds of transfers off-chain and combining or "rolling" them up into a single transaction. The security of the transactions relies directly on the main chain secured by adding mathematical proofs to validate transactions. However, it is relatively harder than hybrid approaches to implement all the functionalities of the mainnet with full security. Various projects are attempting to implement zkSNARKs.
    - Zk rollups have many issues in practice, and pairing compatible curves support in the core protocol is likely required.


### Hydra

**State Channels (Hydra)** is a *peer-to-peer signing model*, and the design can work well for payment channels for simple purposes. The problem, however, is that the state channels are pre-set contracts for which the participants are defined at the launch. New contract creation is needed each time a new participant wants to use the channel. In return, there is higher privacy and security but little flexibility for an open system. IOHK has published a new model called [Hydra: Isomorphic State Channels](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) that introduces multi-party state channels by utilising both on-chain and off-chain-computations-powered-by-the-eUTXO-design. Other novel state channel constructions should be possible as well. It would be good to apply off-chain techniques to applications like ErgoMixer. 



### **Zero-Knowledge Contingent Payments** 

It is possible to make payments that are released if and only if the payee discloses some knowledge (in a trustless manner where neither the payer nor payee can cheat). Achieved using a combination of a `hash-locked transaction` and an external protocol to ensure the correct data is revealed in the hash lock release.

### **FairSwap/FastSwap protocols** 

As described in [this paper](https://eprint.iacr.org/2019/1296)

### **Coinpools** 

Another L2 solution for the UTXO model to consider is described in [this paper](https://discrete-blog.github.io/coinpool/)