# The Ergo Protocol

## Powering the future of finance

Ergo is a next-generation smart contract platform that enables anyone to participate in the digital DeFi revolution now.

Ensuring economic freedom for ordinary people through decentralized, private and secure financial tools.

The overwhelming majority of successful public blockchain use‐cases are related to financial applications. Ergo extends Bitcoin's way of writing contracts by attaching a guard script (together with additional custom data) to every coin. In addition to regular protection by some m‐of‐n signature, Ergo allows specifying the possible recipients of these coins, which may be another contract with similar complex conditions. **This "chaining" approach allows the implementation of secure and efficient contracts of arbitrary complexity.**


[ErgoScript](ergoscript-primer.md) is the language used to specify the conditions under which currency can be spent. The language supports a type of non-interactive zero-knowledge proofs called Σ-protocols and is flexible enough to allow for ring-signatures, multi signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.

> Keeping all this in mind, we expect ErgoScript and Ergo's design to be uniquely useful as Contractual Money.


## [Culture - The Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)
                                                
> Cryptocurrency should provide tools to enrich ordinary people. Small businesses struggling to make ends meet, not big depersonalised financial capital.

Ergo had a fair launch with only a 4.37% of funds allocated to ecosystem development. No smart contract platform is fairer. 

## Core Components

### [Autolykos](autolykos.md)

*Autolykos* is the underlying Memory-hard ASIC-resistant **Proof of Work** (PoW) algorithm oriented towards GPUs. 

### [NIPoPoWs](nipopow.md)

Extended support of light nodes makes Ergo friendly for end-users, allowing them to run contracts on common devices such as mobile phones without centralised intermediaries. 

### [Storage Rent](rent.md)
Another unique feature of Ergo is the concept of storage-rent, which is the ability of miners to take out a small amount of Ergs from boxes that have remained unspent for four or more years (the box is spent, and a new box is created with the lower value). This feature also allows Ergo to avoid long-term bloat of the UTXO set. 

### [eUTXO](eutxo.md)

Ergo uses a so-called *extended-UTXO model*, which implies UTXOs with the ability to contain arbitrary data and sophisticated scripts. 



### [ErgoScript](ergoscript.md)


> Ergo provides **superior support for real-world financial agreements**. It does this through:

   
1. A simple high-level language, [ErgoScript](/dev/scs/ergoscript), enabling clear descriptions of contractual logic.
2. Support for formal verification of contracts, bringing improved security guarantees.
3. **Turing complete** smart contracts as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).
4. Easy Oracle creation
6. Ergo's Smart contracts have a unique [Data Inputs](/dev/scs/data-inputs) concept, enabling a radically different approach to provide robust, flexible cryptography using easy, safe scripting on privacy-centric **Sigma Protocols** (non-interactive zero-knowledge proofs). 
7. The cryptographic part of ErgoScript is based on [Sigma Protocols](/dev/scs/sigma) and naturally supports threshold `m-of-n` signatures, ring signatures, and more. 
8. Support for [Multi-Stage contracts](/dev/scs/multi) that operate on a stateful level. 

**Creating financial contracts on the blockchain isn't just about the functionality; it's about making that functionality safe, accessible, and powerful.**


## [Scaling](scaling.md)

Ergo Platform has a research-based approach for long-term success and has a lot in its toolbox to tackle scaling as we grow. Which options we implement will depend on the needs of applications building on top of Ergo, as well as the success of the solutions in other protocols. 

## [Audit](audit.md)

Ergo has successfully passed a security audit of certain (most critical) parts of the code. This time the audit was done by Jean-Philipee Aumasson (aka veorq, aumasson.jp/).
