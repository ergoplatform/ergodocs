---
tags:
  - Plasma
  - NIPoPoWs
  - Lightning
  - Rollups
  - Hydra
---

# Layer 2 Solutions (Off-Chain)

Layer 2 refers to a supplementary protocol or framework constructed over a [Layer 1](layer1.md) blockchain protocol. The primary objective of Layer 2 solutions is to augment the underlying blockchain's efficiency, scalability, and capabilities by enabling *off-chain* transactions or computations.

Ergo displays a broad range of compatibility with various Layer 2 solutions derived from other UTXO blockchains, including the likes of Bitcoin's Lightning Network. Additionally, Ergo can employ numerous off-chain solutions, such as [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains. These tools aid in reducing blockchain congestion while providing similar benefits to ZK-rollups.

The incorporation of specific Layer 2 solutions into Ergo is driven by the demands of the applications under construction.

> Participate in the Layer 2 conversation on [Telegram](https://t.me/ErgoLayer2) or [Discord]().

## The Power of ErgoScript

The flexible design of [ErgoScript](ergoscript.md) enables large parts of transactions to be executed on Layer 2, which are then settled on the Ergo blockchain in a single transaction. For instance, a developer effectively utilized the eUTXO model to airdrop native tokens to [10,000 addresses simultaneously](https://explorer.ergoplatform.com/en/transactions/e2c4954665ccf87791f42983ae4f7031205c2e719709907cbf2ff09e5489d4b8). 

ErgoScript boasts several advancements like time-weighted data, Turing completeness, read-only data inputs, multi-stage contracts, sigma protocols, NIPoPoWs, and more. These enhancements pave the way for a myriad of protocols on Layer 2, each addressing scalability issues in their own unique way.

> **As such, Ergo can be viewed as a shared *settlement layer* for multiple Level-2 protocols and applications.**

## Embracing Plasma

Ergo inherently supports [AVL trees](avl.md), an effective authenticated data structure that allows for proving different properties of the data without accessing the entire dataset.

The ledger is maintained as an AVL tree using **[Plasma](plasma.md)**. Users carry out off-chain transactions with the bank, leading to changes in the ledger. Periodically, the bank publishes a compact snapshot of the ledger on the blockchain.

The [Plasma Library](plasma.md) can be utilized to construct *Plasma chains*, leading to a comprehensive L2 solution. Currently, it's primarily used for data compression and simplifying contracts, though the development of Plasma chains is a promising future prospect.

## Harnessing NIPoPoWs

[NiPoPoWs](nipopows.md) hold the potential for scalability by facilitating the interoperability of diverse blockchain networks. This capability can ease the load on individual chains by distributing it across multiple networks.

One practical application could involve smaller, less secure blockchains leveraging the security of larger, more established chains. For instance, a minor blockchain could periodically submit proofs of work to a larger chain, anchoring their blockchain to the larger network. This approach would not only boost the security of the smaller chain but also enable the transfer of assets between chains without a centralized intermediary.

NiPoPoWs could further improve the scalability of Layer 2 solutions like sidechains or state channels. By enabling these solutions to communicate more securely and efficiently, NiPoPoWs could decrease the load on the main blockchain network and enhance transaction throughput.

## Exploring Other Possibilities

Several promising Layer 2 solutions are on the horizon:

### **Lightning Network** 

The Lightning Network operates through a system where two participants pool their funds into a particular type of joint multi-sig wallet. This wallet enables them to create and enforce off-chain agreements. The network itself consists of these interconnected channels, allowing off-chain payments to be structured across multiple channels, akin to an abacus.

### **Rainbow Network** 

The Rainbow Network, an off-chain non-custodial exchange and payment network, supports any assets where two parties can agree on a price oracle. The Rainbow Network empowers users to trade, borrow, lend, and make payments in synthetic assets entirely off-chain, despite only having one on-chain payment channel collateralized by a single asset. More details can be found in [this paper](http://research.paradigm.xyz/RainbowNetwork.pdf).

### **Rollups**

Rollups are feasible via AVL trees. A roll-up involves bundling up groups of transactions, with the primary concern being data posting on-chain, not verification. 

There are two main types of *Rollups* employed for scaling. 

- **Optimistic Rollups** handle transactions on a parallel chain compatible with the main chain. This model is optimistic because it relies on the *Fraud-Proof principle*, where aggregators do not actively verify Layer 2, but intervene in case of fraud disputes. More information can be found in this [ergoforum](https://www.ergoforum.org/t/optimistic-rollups-and-fraud-proofs-in-ergo/3819) post.
- **ZK-Rollups** leverage [zkSNARKs](https://blog.ethereum.org/2016/12/05/zksnarks-in-a-nutshell/) (zero-knowledge succinct non-interactive arguments of knowledge) to decrease network load by bundling hundreds of transfers off-chain into a single transaction. Although their implementation is more challenging than hybrid approaches, numerous projects are making attempts in this direction.

### **Hydra**

**State Channels (Hydra)** is a *peer-to-peer signing model* that works well for payment channels for simple applications. A potential limitation, however, is that state channels predefine the participants at launch, which necessitates a new contract each time a new participant wishes to use the channel. Despite offering high privacy and security, it has limited flexibility for an open system. IOHK introduced [Hydra: Isomorphic State Channels](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) that uses both on-chain and off-chain computations, powered by the eUTXO design, to facilitate multi-party state channels. Other novel state channel constructions are also possible and could find applications in tools like ErgoMixer.

### **Zero-Knowledge Contingent Payments** 

Payments can be designed such that they are released only if the payee discloses some knowledge in a trustless manner where neither the payer nor payee can cheat. This is achieved using a combination of a `hash-locked transaction` and an external protocol to ensure the correct data is revealed in the hash lock release.

### **FairSwap/FastSwap protocols** 

These protocols are detailed in [this paper](https://eprint.iacr.org/2019/1296).

### **Coinpools** 

Another potential Layer 2 solution for the UTXO model is described in [this paper](https://discrete-blog.github.io/coinpool/).