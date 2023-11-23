---
tags:
  - Plasma
  - NIPoPoWs
  - Lightning
  - Rollups
  - Hydra
---


# Layer 2: Off-Chain

Layer 2 solutions are secondary frameworks or protocols constructed on top of a [Layer 1](layer1.md) blockchain protocol. Their purpose is to enhance the efficiency, scalability, and capabilities of the underlying blockchain by facilitating *off-chain* transactions or computations.

Ergo is compatible with a broad range of Layer 2 solutions derived from other UTXO blockchains, such as Bitcoin's Lightning Network. Ergo can also implement various off-chain solutions like [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains, which help alleviate blockchain congestion and offer benefits akin to ZK-rollups.

The integration of specific Layer 2 solutions into Ergo is determined by the requirements of the applications being developed.

> Join the Layer 2 discussion on [Telegram](https://t.me/ErgoLayer2) or [Discord]().

## ErgoScript: Powering Layer 2 Transactions

[ErgoScript](ergoscript.md)'s flexible design allows large parts of transactions to be executed on Layer 2, which are then settled on the Ergo blockchain in a single transaction. For instance, a developer successfully used the eUTXO model to airdrop native tokens to [10,000 addresses simultaneously](https://explorer.ergoplatform.com/en/transactions/e2c4954665ccf87791f42983ae4f7031205c2e719709907cbf2ff09e5489d4b8). 

ErgoScript features several advancements like time-weighted data, Turing completeness, read-only data inputs, multi-stage contracts, sigma protocols, NIPoPoWs, and more. These enhancements enable a variety of Layer 2 protocols, each addressing scalability issues in their unique way.

> **Ergo can thus be considered a shared *settlement layer* for multiple Level-2 protocols and applications.**

## Plasma: Enhancing Data Structures

Ergo inherently supports [AVL trees](avl.md), an efficient authenticated data structure that allows for proving different properties of the data without accessing the entire dataset.

The ledger is maintained as an AVL tree using **[Plasma](plasma.md)**. Users conduct off-chain transactions with the bank, resulting in changes in the ledger. The bank periodically publishes a compact snapshot of the ledger on the blockchain.

The [Plasma Library](plasma.md) can be used to build *Plasma chains*, leading to a comprehensive L2 solution. Currently, it's mainly used for data compression and contract simplification, but the development of Plasma chains is a promising future prospect.

## NIPoPoWs: Facilitating Scalability

[NiPoPoWs](nipopows.md) offer scalability potential by enabling the interoperability of various blockchain networks. This capability can alleviate the load on individual chains by distributing it across multiple networks.

One practical application could involve smaller, less secure blockchains leveraging the security of larger, more established chains. For example, a minor blockchain could periodically submit proofs of work to a larger chain, anchoring their blockchain to the larger network. This approach would not only enhance the security of the smaller chain but also enable the transfer of assets between chains without a centralized intermediary.

NIPoPoWs could further improve the scalability of Layer 2 solutions like sidechains or state channels. By enabling these solutions to communicate more securely and efficiently, NIPoPoWs could reduce the load on the main blockchain network and increase transaction throughput.

## Emerging Layer 2 Solutions

There are several Layer 2 solutions currently under development that show great promise:

### **Lightning Network** 

The Lightning Network is a Layer 2 protocol that operates by allowing two participants to pool their funds into a specific type of joint multi-signature wallet. This wallet facilitates the creation and enforcement of off-chain agreements. The network is composed of these interconnected channels, enabling off-chain payments to be routed across multiple channels, akin to an abacus.

### **Rainbow Network** 

The Rainbow Network is an off-chain, non-custodial exchange and payment network that supports any assets for which two parties can agree on a price oracle. It enables users to trade, borrow, lend, and make payments in synthetic assets entirely off-chain, even though they only have one on-chain payment channel collateralized by a single asset. For more details, refer to [this paper](http://research.paradigm.xyz/RainbowNetwork.pdf).

### **Rollups**

Rollups are a Layer 2 solution that could be implemented on Ergo using [AVL trees](avl.md). They involve bundling groups of transactions together, with the primary focus being on data posting on-chain, rather than verification. 

There are two primary types of *Rollups* used for scaling: 

- **Optimistic Rollups** operate by handling transactions on a parallel chain that is compatible with the main chain. This model is termed 'optimistic' because it relies on the *Fraud-Proof principle*, where aggregators do not actively verify Layer 2, but intervene in case of fraud disputes. For more information, refer to this [ergoforum](https://www.ergoforum.org/t/optimistic-rollups-and-fraud-proofs-in-ergo/3819) post.
- **ZK-Rollups** utilize [zkSNARKs](https://blog.ethereum.org/2016/12/05/zksnarks-in-a-nutshell/) (zero-knowledge succinct non-interactive arguments of knowledge) to reduce network load by bundling hundreds of transfers off-chain into a single transaction. While their implementation is more complex than hybrid approaches, many projects are exploring this direction.

### **Hydra**

Hydra, a form of **State Channels**, employs a *peer-to-peer signing model* that is particularly effective for simple applications such as payment channels. One of its limitations is that it requires the participants to be predefined at the time of channel creation, necessitating a new contract for each new participant. While this model provides high levels of privacy and security, it lacks flexibility for open systems. To address this, IOHK introduced [Hydra: Isomorphic State Channels](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/), a solution that leverages both on-chain and off-chain computations, powered by the eUTXO design, to facilitate multi-party state channels. This approach opens up possibilities for other innovative state channel constructions, which could be utilized in tools like ErgoMixer.

### **Zero-Knowledge Contingent Payments** 

Zero-Knowledge Contingent Payments are designed to be released only when the payee discloses specific knowledge in a trustless manner, ensuring that neither the payer nor the payee can cheat. This is achieved through a combination of a `hash-locked transaction` and an external protocol that verifies the correct data is revealed when the hash lock is released.

### **FairSwap/FastSwap protocols** 

The FairSwap and FastSwap protocols are Layer 2 solutions that provide secure and efficient transaction methods. Detailed information about these protocols can be found in [this paper](https://eprint.iacr.org/2019/1296).

### **Coinpools** 

Coinpools represent another potential Layer 2 solution for the UTXO model. They offer a method for grouping transactions to improve efficiency and scalability. More information about Coinpools can be found in [this paper](https://discrete-blog.github.io/coinpool/).
