---
tags:
  - NIPoPoWs
  - Plasma
  - Sigma Protocols
  - Scaling
---

# Scaling Ergo

Creating a scalable blockchain infrastructure is a complex task. Ergo, fortified by a decade of [research](documents.md), rigorous testing, and ongoing development, has risen to the challenge. This guide will walk you through Ergo's sophisticated scalability features.

Blockchain scalability is primarily influenced by three factors:

- **Cryptoeconomic incentive model**: This model ensures that miners receive suitable rewards for the various costs associated with scaling a blockchain, which may include an increase in state-related costs.
- **Consensus model**: The chosen model can determine the feasibility of certain scalability solutions. For example, the Proof of Stake consensus model does not support Non-interactive Proofs of Proof-of-Work (NiPoPoWs).
- **Accounting model**: This pertains to the management of transactions and operations within the blockchain. Bitcoin uses the UTXO Model, while Ethereum uses the Account Model.

Ergo's innovative approach to scalability, underpinned by these aspects, sets it apart from other blockchain technologies. Unlike Ethereum's Account model, which manages storage changes and validity checks on-chain during code execution, Ergo's [eUTXO](eutxo.md) employs a unique strategy: transactions are created off-chain, and validation checks are conducted on-chain. 

This approach reduces the operational load on each network node, thereby enhancing overall efficiency. The immutability of the transaction graph allows for further optimization of this process, increasing the number of transactions processed per second. Additionally, the use of light-verifying nodes boosts both the scalability and accessibility of the network.

To gain a comprehensive understanding of Ergo's scalability, delve into the role of each layer in this process:

- [Layer 0](layer0.md): The *Network* or *Peer-to-Peer* Layer
- [Layer 1](layer1.md): The Core Blockchain Layer
- [Layer 2](layer2.md): The Off-chain Layer

These layers work in harmony to enhance Ergo's scalability, making it a flexible and potent choice for both developers and users. This collaborative model enables Ergo to provide robust, scalable solutions that are prepared to meet the challenges of global expansion.
