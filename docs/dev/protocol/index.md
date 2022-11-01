# Powering the future of finance

Ergo is a [next-generation](scaling.md) smart contract platform that enables anyone to participate in the digital DeFi revolution now.

Ensuring economic freedom for ordinary people through decentralized, private and secure financial tools.

::cards::

[
  {
    "title": "Why Ergo?",
    "content": "",
    "url": "why.md"
  },
  {
    "title": "Contributing",
    "content": "Participate in decentralised finance!",
    "url": "../../contribute"
  },
  {
    "title": "FAQ",
    "content": "Frequently Asked Questions",
    "url": "../../faq"
  },


]

::/cards::

## Core Components

::cards::

[
  {
    "title": "Autolykos",
    "content": "The underlying Memory-hard ASIC-resistant **Proof of Work** (PoW) algorithm oriented towards GPUs. ",
    "url": "../../mining/autolykos"
  },
  {
    "title": "eUTXO",
    "content": "Ergo uses a so-called *extended-UTXO model*, which implies UTXOs with the ability to contain arbitrary data and sophisticated scripts. ",
    "url": "eutxo"
  },
  {
    "title": "NIPoPoWs",
    "content": "Enable extended support of light nodes which makes Ergo friendly for end-users, allowing them to run contracts on common devices such as mobile phones without centralised intermediaries. ",
    "url": "nipopows"
  },
  {
    "title": "Privacy",
    "content": "Ergo provides **superior access to discrete log-based zero-knowledge proofs**",
    "url": "zkp"
  },
  {
    "title": "Scaling",
    "content": "Explore the various scaling solutions being explored on Ergo.",
    "url": "scaling"
  },
  {
    "title": "Storage Rent",
    "content": "Storage Rent is a nominal fee incurred by unmoved boxes after four years.",
    "url": "scaling"
  },
  {
    "title": "ErgoScript",
    "content": "A simple high-level language enabling clear descriptions of contractual logic.",
    "url": "../../dev/scs/ergoscript"
  },


]

::/cards::

> *Creating financial contracts on the blockchain isn't just about the functionality; it's about making that functionality safe, accessible, and powerful.* 


Ergo provides **superior support for real-world financial agreements**. It does this through:

   
1. A simple high-level language, [ErgoScript](/dev/scs/ergoscript), enabling clear descriptions of contractual logic.
2. Support for formal verification of contracts, bringing improved security guarantees.
3. *Turing complete* smart contracts as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).
4. Easy Oracle creation
5. A unique [Data Inputs](/dev/scs/data-inputs) concept, enabling a radically different approach to provide robust, flexible cryptography.
6. The cryptographic part of ErgoScript is based on [Sigma Protocols](/dev/scs/sigma) and naturally supports threshold `m-of-n` signatures, ring signatures, and more. 
7. Support for [Multi-Stage contracts](/dev/scs/multi) that operate on a stateful level. 



## Core Components

- *[Autolykos](autolykos.md)* is the underlying Memory-hard ASIC-resistant **Proof of Work** (PoW) algorithm oriented towards GPUs. 
- [NIPoPoWs](nipopows.md) enable extended support of light nodes which makes Ergo friendly for end-users, allowing them to run contracts on common devices such as mobile phones without centralised intermediaries. 
- Another unique feature of Ergo is the concept of [Storage Rent](rent.md), which is the ability of miners to take out a small amount of Ergs from boxes that have remained unspent for four or more years (the box is spent, and a new box is created with the lower value). This feature also allows Ergo to avoid long-term bloat of the UTXO set. 
- Ergo uses a so-called *extended-UTXO model* ([eUTXO](eutxo.md)), which implies UTXOs with the ability to contain arbitrary data and sophisticated scripts. 


