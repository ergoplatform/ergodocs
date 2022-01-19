# The Ergo Protocol

Ergo is a Layer 1 proof of work blockchain that provides a platform for developers to build trustless financial contracts and enables true peer to peer, decentralised, grassroots finance.

Ergo has prioritised useful features without compromising security with a research-driven but practical development model. 

*Ergo*, **a resilient platform for contractual money**

Below you can dive deeper into some of the most important components of Ergo. 

## [The Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)                                                      
> Cryptocurrency should provide tools to enrich ordinary people. Small businesses struggling to make ends meet, not big depersonalised financial capital.

## [Autolykos](/dev/protocol/autolykos)

*Autolykos* is the underlying Memory-hard ASIC-resistant **Proof of Work** (PoW) algorithm oriented towards GPUs. 

## [eUTXO](eutxo.md)

Ergo is a **UTXO** based blockchain with Proof-of-Work consensus. In this aspect, it is similar to Bitcoin. Ergo uses standard **Elliptic Curve** Cryptography with the same curve as Bitcoin (`Secp256k1`). Unlike Bitcoin and similar to Cardano, Ergo uses a so-called "extended-UTXO model," which implies UTXOs with the ability to contain arbitrary data and sophisticated scripts. 

Ergo's Smart contracts have a unique **data input** concept, enabling a radically different approach to provide robust, flexible cryptography using easy, safe scripting on privacy-centric **Sigma Protocols** (non-interactive zero-knowledge proofs). 


## [ErgoScript](/dev/scs/ergoscript)


Smart contracts are written in a high-level language called [ErgoScript](/dev/scs/ergoscript) with the ability for **Turing complete** smart contracts as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).

Ergo provides **superior support for real-world financial agreements**. It does this through:

1. Support for [multi-stage contracts](/dev/scs/multi) 
2. A simple high-level language, ErgoScript, enabling clear descriptions of contractual logic
3. Support for formal verification of contracts, bringing improved security guarantees (Ergo Platform deployed its [first formally verified p2p crowdfunding contract](https://twitter.com/chepurnoy/status/1239936086106935296) just three months after the network launched)
4. Easy Oracle creation
5. Native support for complex signature schemes

Creating financial contracts on the blockchain isn't just about the functionality; it's about making that functionality safe, accessible, and powerful. 


### [Sigma Protocols](/dev/scs/sigma)

The cryptographic part of ErgoScript is based on **Sigma Protocols** and naturally supports threshold `m-of-n` signatures, ring signatures, and more. Keeping all this in mind, we expect ErgoScript and Ergo's design to be uniquely useful as **Contractual Money** with countless possible applications. 

## [NIPoPoWs](/dev/protocol/nipopow)

Extended support of light nodes makes Ergo friendly for end-users, allowing them to run contracts on common devices such as mobile phones without centralised intermediaries. 

**Non-Interactive Proofs of Proof of Work** ([NIPoPoWs](https://nipopows.com/)) are essential for two reasons: Light Clients and Side Chains. These two components are essential for clients and nodes to facilitate easier onboarding to the blockchain. A decentralised network is inherently inefficient because of the randomness mechanism in a synchronous network; that is to say, every time a transaction (TX) occurs on the network, a couple of random nodes must process the TX to prove and secure its reliability. That is an enormous task on a global scale when put into perspective. There can be billions of transactions, and it is plausible that many of those are from contributors operating with low bandwidth.



## [Storage Rent](/dev/protocol/rent)
Another unique feature of Ergo is the concept of storage-rent, which is the ability of miners to take out a small amount of Ergs from boxes that have remained unspent for four or more years (the box is spent, and a new box is created with the lower value). This feature also allows Ergo to avoid long-term bloat of the UTXO set. (Currently 50% of UTXOs in Bitcoin). 


## [Scaling](/dev/protocol/scaling)

Ergo Platform has a research-based approach for long-term success and has a lot in its toolbox to tackle scaling as we grow. Which options we implement will depend on the needs of applications building on top of Ergo, as well as the success of the solutions in other protocols. 



## Long-Term Vision

- [Long-term vision for Ergo](https://www.ergoforum.org/t/long-term-vision-for-ergo/2629) ~ 26 Sept, 2021

## Audit

- [Audit](../protocol/audit.md)