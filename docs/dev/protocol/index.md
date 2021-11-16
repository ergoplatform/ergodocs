# The Ergo Protocol

Ergo is a **Resilient Platform for Contractual Money**. Designed with the main focus to provide an efficient, secure, and easy way to implement robust financial contracts.

Ergo brings advanced cryptographic features and radically new DeFi functionality, complimenting tried and tested principles with the latest peer-reviewed academic research into cryptography, consensus models, and digital currencies.

With a research-driven but practical development model, Ergo has prioritized useful features without compromising on security. 

**All cryptocurrencies rely on contributions from the scientific research community. Ergo brings it in its core!**


## [The Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)                                                      
> Cryptocurrency should provide tools to enrich ordinary people. Small businesses that are struggling to make ends meet, not big depersonalized financial capital.

## [Autolykos](/dev/protocol/autolykos)

Ergo uses Autolykos as the underlying Proof of Work (PoW) algorithm. Autolykos v2 (the current version of PoW) is a memory-hard ASIC-resistant PoW algorithm oriented towards GPUs.

## [NIPoPoWs](/dev/protocol/nipopow)

Extended support of light nodes makes Ergo friendly for end-users, allowing them to run contracts on common devices such as mobile phones without centralized intermediaries. 


## [eUTXO](/dev/data-model/box)

The platform's smart contracts are built on the extended **UTXO (eUTXO)** model with a unique data input concept, offering a radically different approach to provide robust, flexible cryptography and easy, safe scripting on privacy-centric **Sigma Protocols** (non-interactive zero-knowledge proofs). 

Ergo is a **UTXO** based blockchain with Proof-of-Work consensus. In this aspect, it is similar to Bitcoin. Ergo uses standard **Elliptic Curve** Cryptography with the same curve as Bitcoin (`Secp256k1`). Unlike Bitcoin and similar to Cardano, Ergo uses a so-called "extended-UTXO model," which implies UTXOs with the ability to contain arbitrary data and sophisticated scripts. 

Due to this, Ergo supports advanced financial contracts similar to those in Ethereum's account-based model.

## [ErgoScript](/dev/scs/ergoscript)


Ergo provides advanced programming abilities for financial contracts using a high-level language called ErgoScript. 

The scripting language in itself is non-Turing complete, but applications run on the platform can be made to be Turing complete as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).

Ergo provides superior support for real-world financial agreements. It does this through:

1. Support for [multi-stage contracts](/dev/scs/multi) 
2. A simple high-level language, ErgoScript, enabling clear descriptions of contractual logic
3. Support for formal verification of contracts for improved security guarantees (Ergo Platform deployed its [first formally verified p2p crowdfunding contract](https://twitter.com/chepurnoy/status/1239936086106935296) just three months after the network launched)
4. Easy Oracle creation
5. Native support for complex signature schemes

In short, creating financial contracts on the blockchain isn’t just about the functionality you provide. It’s about making that functionality safe and accessible, as well as powerful. Ergo achieves this and more.


## [Sigma Protocols](/site/dev/scs/sigma/index.html)

The cryptographic part of ErgoScript is based on **Sigma Protocols** and naturally supports threshold `m-of-n` signatures, ring signatures, and more. Keeping all this in mind, we expect ErgoScript and Ergo's design to be uniquely useful as **Contractual Money** with countless possible applications. 

## [NIPoPoWs](/node/nipopow)

**Non-Interactive Proofs of Proof of Work** ([NIPoPoWs](https://nipopows.com/)) are essential for two reasons: Light Clients and Side Chains. These two components are essential for clients and nodes to facilitate easier onboarding to the blockchain. A decentralized network is inherently inefficient because of the randomness mechanism in a synchronous network; that is to say, every time a transaction (TX) occurs on the network, a couple of random nodes must process the TX to prove and secure its reliability. When put into perspective, that is an enormous task on a global scale. There can be billions of transactions, and it is plausible that many of those are from contributors operating with low bandwidth.


## [Storage Rent](https://ergoplatform.org/en/blog/2020_04_21_ergo_positioning/)
Another unique feature of Ergo is the concept of storage-rent, which is the ability of miners to take out a small amount of Ergs from boxes that have remained unspent for four or more years (the box is spent, and a new box is created with the lower value). This allows Ergo to avoid long-term bloat of the UTXO set.


## Scaling

The scaling aspect in Ergo Platform's design has been a high priority since the mainnet launch. In order to gain mass adoption, a blockchain should be able to scale. Scalability refers to the efficient use of computational resources and high throughput. Ergo incorporates various elements to achieve near-infinite scalability. The design is built on the extended UTXO model with its novel language, ErgoScript, relying on peer-reviewed academic research. With years of research, Ergo developed various features such as stateless clients, NIPoPoWs and UTXO based smart contracts.



Initially, Layer 0 is the reference layer where nodes are connected. This is the peer-to-peer infrastructure layer. The Ergo Node Client has improved a lot since v4.0.8 and still has 20 times more room to develop. [Light bootstrapping](https://ergoplatform.org/en/blog/2021-07-19-mining-in-logarithmic-space-nipopow-power-and-ergo/) using NIPoPoWs are also planned to be integrated via a Velvet soft fork.



On Layer 1, the application layer, Ergo supports on-chain scalability solutions such as Sharding. Aside from Sharding, the extended UTXO model allows most of the transactions to be executed off-chain and reduces on-chain network load.



In the end, there are Layer 2 scaling solutions that refer to off-chain layer scaling solutions. There are multiple off-chain solutions such as [Hydra](https://iohk.io/en/research/library/papers/hydrafast-isomorphic-state-channels/) and sidechains to compress blockchain bloat and provide similar benefits like zk-rollups. Ergo can also be compatible with other UTXO Layer 2 solutions such as Bitcoin’s Lightning Network.



Stateless clients allow for both light wallets and light miners to run with full node security. NIPoPoW implementation via Velvet soft forks will enable infinite sidechains on top of Ergo. 



Ergo utilizes "[Storage Rent Fee](https://ergoplatform.org/en/blog/2021-07-09-cryptocurrency-fees-a-solution-to-unreasonable-state-growth/)" to prevent spam and recirculate unused data bytes, known as dust. Storage Rent Fee helps to clean the network pollution and encourages users to be more active.



Ergo Platform has a research-based approach for long-term success and it has a lot in the toolbox to tackle the scaling problems that will come in the future. 



- [Roadmap](https://ergonaut.space/en/roadmap)
- [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)
- [Network congestion on Jul, 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)


## Long-Term Vision

- [Long-term vision for Ergo](https://www.ergoforum.org/t/long-term-vision-for-ergo/2629) ~ 26 Sept, 2021

## Audit

- [Audit](../protocol/audit.md)