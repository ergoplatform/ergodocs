---
tags:
  - NIPoPoWs
  - Plasma
  - Sigma Protocols
---

# Expanding Ergo's Blockchain Technology

Building a scalable blockchain infrastructure is no small feat. Ergo, backed by a decade's worth of [research](documents.md), meticulous testing, and continuous development, has proven up to the challenge. This document will guide you through Ergo's advanced scalability features

Three primary factors are integral to blockchain scalability:

- **Cryptoeconomic incentive model**: This framework ensures that miners are appropriately rewarded for the various costs that come with scaling a blockchain, which can include an increase in state-related costs.
- **Consensus model**: Depending on the chosen model, certain scalability solutions may or may not be feasible. For instance, the Proof of Stake consensus model does not support Non-interactive Proofs of Proof-of-Work (NiPoPoWs).
- **Accounting model**: This refers to how transactions and operations are managed within the blockchain. While Bitcoin employs the UTXO Model, Ethereum operates on the Account Model.

These aspects underpin Ergo's innovative approach to scalability, distinguishing it from other blockchain technologies. Unlike Ethereum's Account model which handles storage changes and validity checks on-chain during code execution, Ergo's [eUTXO](eutxo.md) adopts a different strategy: transactions are created off-chain and validation checks are performed on-chain. 

This system minimizes the operational demand on each node in the network, thereby improving overall efficiency. With the transaction graph's immutability, we can further optimize this process to enhance the number of transactions processed per second. Moreover, the incorporation of light-verifying nodes augments both the scalability and accessibility of the network.

For a deeper understanding of Ergo's scalability, explore each layer's role in this process:

- [Layer 0](layer0.md): The *Network* or *Peer-to-Peer* Layer
- [Layer 1](layer1.md): The Core Blockchain Layer
- [Layer 2](layer2.md): The Off-chain Layer

Each layer works synergistically to bolster Ergo's scalability, making it a versatile and powerful choice for developers and users alike. This cooperative model allows Ergo to offer robust, scalable solutions ready to meet the demands of global expansion.