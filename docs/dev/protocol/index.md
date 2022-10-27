# Powering the future of finance

Ergo is a [next-generation](scaling.md) smart contract platform that enables anyone to participate in the digital DeFi revolution now.

Ensuring economic freedom for ordinary people through decentralized, private and secure financial tools.

## Why Ergo?

Ergo is multi-asset Proof-of-Work cryptocurrency with powerful financial contracts in the extended UTXO model, unique flexible crypto-contracts based on sigma-protocols, storage rent, stateless and ultra-efficient SPV clients support and focus on long-term survivability. Based on a scientific approach, but also very practical in any aspect. Ergo is a DeFi and crypto contracts platform that takes a radically different approach to smart contracts than other networks, non-custodial and non-interactive approaches including off-the-peg use of ring and threshold signatures – great for new privacy applications

The overwhelming majority of successful public blockchain use‐cases are related to financial applications. Ergo extends Bitcoin's way of writing contracts by attaching a guard script (together with additional custom data) to every coin. 

In addition to regular protection by some `m‐of‐n` signature, Ergo allows specifying the possible recipients of these coins, which may be another contract with similar complex conditions. This "chaining" approach allows the implementation of secure and efficient contracts of arbitrary complexity.


[ErgoScript](ergoscript.md) is the language used to specify the conditions under which currency can be spent. The language supports a type of non-interactive zero-knowledge proofs called [Σ-protocols](sigma.md) which is flexible enough to allow for ring-signatures, multi signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.

**Keeping all this in mind, we expect ErgoScript and Ergo's design to be uniquely useful as Contractual Money**

## [Culture - The Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)
                                                
> *"Cryptocurrency should provide tools to enrich ordinary people. Small businesses struggling to make ends meet, not big depersonalised financial capital."*

Ergo had a fair launch with only a **4.37%** of funds allocated to ecosystem development. No smart contract platform is fairer. 

## Core Components

- *[Autolykos](autolykos.md)* is the underlying Memory-hard ASIC-resistant **Proof of Work** (PoW) algorithm oriented towards GPUs. 
- [NIPoPoWs](nipopow.md) enable extended support of light nodes which makes Ergo friendly for end-users, allowing them to run contracts on common devices such as mobile phones without centralised intermediaries. 
- Another unique feature of Ergo is the concept of [Storage Rent](rent.md), which is the ability of miners to take out a small amount of Ergs from boxes that have remained unspent for four or more years (the box is spent, and a new box is created with the lower value). This feature also allows Ergo to avoid long-term bloat of the UTXO set. 
- Ergo uses a so-called *extended-UTXO model* ([eUTXO](eutxo.md)), which implies UTXOs with the ability to contain arbitrary data and sophisticated scripts. 

*Creating financial contracts on the blockchain isn't just about the functionality; it's about making that functionality safe, accessible, and powerful.* 

Ergo provides **superior support for real-world financial agreements**. It does this through:

   
1. A simple high-level language, [ErgoScript](/dev/scs/ergoscript), enabling clear descriptions of contractual logic.
2. Support for formal verification of contracts, bringing improved security guarantees.
3. *Turing complete* smart contracts as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).
4. Easy Oracle creation
5. A unique [Data Inputs](/dev/scs/data-inputs) concept, enabling a radically different approach to provide robust, flexible cryptography using easy, safe scripting on privacy-centric **Sigma Protocols**. 
6. The cryptographic part of ErgoScript is based on [Sigma Protocols](/dev/scs/sigma) and naturally supports threshold `m-of-n` signatures, ring signatures, and more. 
7. Support for [Multi-Stage contracts](/dev/scs/multi) that operate on a stateful level. 



