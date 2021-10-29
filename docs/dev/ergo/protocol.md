# The Ergo Protocol

Ergo is a **Resilient Platform for Contractual Money**. Designed with the main focus to provide an efficient, secure, and easy way to implement financial contracts.

Ergo builds advanced cryptographic features and radically new DeFi functionality on the rock-solid foundations laid by a decade of blockchain theory and development. It complements tried and tested principles with the latest peer-reviewed academic research into cryptography, consensus models, and digital currencies.

With a research-driven but practical development model, Ergo has prioritized useful features without compromising on security. 

Extended support of light nodes makes Ergo friendly for end-users, allowing them to run contracts on common devices such as mobile phones without centralized intermediaries. To be useful in the long-term, we use widely-researched solutions with high-security guarantees while also preventing performance degradation over time with a new economic model.


**All cryptocurrencies rely on contributions from the scientific research community. Ergo brings it in its core!**


### [The Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)                                                      
> Cryptocurrency should provide tools to enrich ordinary people. The small businesses that are getting not much above making ends meet, not depersonalized big financial capital. This is what inspired me. This is my dream.

## [Proof-of-Work](../protocol/autolykos.md)

Ergo uses Autolykos as the underlying PoW algorithm. Autolykos v2 (the current version of PoW) is a memory-hard ASIC-resistant PoW algorithm oriented towards GPUs.


## [eUTXO](../data-model/box.md)

The platform's smart contracts are built on the extended **UTXO (eUTXO)** model with a unique data input concept, offering a radically different approach to provide robust, flexible cryptography and easy, safe scripting on privacy-centric **Sigma Protocols** (non-interactive zero-knowledge proofs). 

Ergo is a **UTXO** based blockchain with Proof-of-Work consensus. In this aspect, it is similar to Bitcoin. Ergo uses standard **Elliptic Curve** Cryptography with the same curve as Bitcoin (`Secp256k1`). Unlike Bitcoin and similar to Cardano, Ergo uses a so-called "extended-UTXO model," which implies UTXOs with the ability to contain arbitrary data and sophisticated scripts. 

Due to this, Ergo supports advanced financial contracts similar to those in Ethereum's account-based model.

## [ErgoScript](../scs/ergoscript.md)


Ergo provides advanced programming abilities for financial contracts using a high-level language called ErgoScript. 

The scripting language in itself is non-Turing complete, but applications run on the platform can be made to be Turing complete as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).

Ergo provides superior support for real-world financial agreements. It does this through:

1. Support for [multi-stage contracts](../scs/multi.md) 
2. A simple high-level language, ErgoScript, enabling clear descriptions of contractual logic
3. Support for formal verification of contracts for improved security guarantees (Ergo Platform deployed its [first formally verified p2p crowdfunding contract](https://twitter.com/chepurnoy/status/1239936086106935296) just three months after the network launched)
4. Easy Oracle creation
5. Native support for complex signature schemes

In short, creating financial contracts on the blockchain isn’t just about the functionality you provide. It’s about making that functionality safe and accessible, as well as powerful. Ergo achieves this and more.


## [Sigma Protocols](../scs/sigma.md)

The cryptographic part of ErgoScript is based on **Sigma Protocols** and naturally supports threshold `m-of-n` signatures, ring signatures, and more. Keeping all this in mind, we expect ErgoScript and Ergo's design to be uniquely useful as **Contractual Money** with countless possible applications. 

## [NIPoPoWs](../../node/nipopows.md)

**Non-Interactive Proofs of Proof of Work** ([NIPoPoWs](https://nipopows.com/)) are essential for two reasons: Light Clients and Side Chains. These two components are essential for clients and nodes to facilitate easier onboarding to the blockchain. A decentralized network is inherently inefficient because of the randomness mechanism in a synchronous network; that is to say, every time a transaction (TX) occurs on the network, a couple of random nodes must process the TX to prove and secure its reliability. When put into perspective, that is an enormous task on a global scale. There can be billions of transactions, and it is plausible that many of those are from contributors operating with low bandwidth.


## [Storage Rent](https://ergoplatform.org/en/blog/2020_04_21_ergo_positioning/)
Another unique feature of Ergo is the concept of storage-rent, which is the ability of miners to take out a small amount of Ergs from boxes that have remained unspent for four or more years (the box is spent, and a new box is created with the lower value). This allows Ergo to avoid long-term bloat of the UTXO set.


## Scaling

- [Roadmap](https://ergonaut.space/en/roadmap)
- [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)
- [Network congestion on Jul, 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)


## Long-Term Vision

- [Long-term vision for Ergo](https://www.ergoforum.org/t/long-term-vision-for-ergo/2629) ~ 26 Sept, 2021