---
tags:
  - NIPoPoWs
  - Plasma
  - Sigma Protocols
---

# Scaling

Based on a decade of [research](documents.md), extensive testing pre-launch and ongoing development, the Ergo community has launched a blockchain with all the tools to scale globally. 

Scalability is a complex topic that covers many aspects, including:
- The Cryptoeconomic incentive model – making sure miners are compensated for the various increased costs of a scaled blockchain - including state-related costs
- The Consensus model and its impact on what solutions are possible (for example, Proof of Stake does not allow the use of NiPoPoWs)
- The Accounting model for transactions and operations - Bitcoin  uses the UTXO Model versus the Account Model used in Ethereum

When it comes to addressing scalability, Ergo’s solutions are innovative, diverse and complex. 

In the Account model (Ethereum), both storage changes and validity checks are performed on-chain during code execution. In contrast, Ergo transactions are created off-chain and validation checks are performed on-chain, reducing the number of operations performed by every node on the network. In addition, due to the immutability of the transaction graph, various optimisation strategies are possible to improve the throughput of transactions per second in the network. Light-verifying nodes are also possible, thus further facilitating scalability and accessibility of the network.

These sections explore all past and potential scaling across each layer. If you're a developer the [Plasma Library](plasma.md) is available to use in your application.  

- [Layer 0](layer0.md): The *Network* or *P2P* Layer
- [Layer 1](layer1.md): The Blockchain
- [Layer 2](layer2.md): Off-chain

## The next evolution of blockchain.

There are three generations of blockchain technology, each capable of handling more complex behaviours than the last.

- The first generation is the original use case of BTC, which was to maintain a public transaction ledger accurately and reliably.
- Second-generation blockchains were created with the implementation of smart contracts as a priority, and Ethereum (ETH) is the most popular example. One significant difference with ETH is the language used to code smart contracts. It uses a Turing-complete language (Solidity), making it computationally universal.
- The third generation of blockchain technology focuses on solving issues related to congestion and scalability. As the technology becomes more decentralised, there will be an exponential increase in the number of users interacting with the blockchain. Third-generation blockchains generally can process off-chain transactions, helping speed up transactions significantly. DOT, ADA, and ERG are third-generation blockchains with smart-contract capabilities while proposing solutions for scalability to a global audience.

The account model Ethereum uses performs both storage changes and validity checks on-chain during code execution. In contrast, Ergo transactions are created off-chain, and only validation checks are performed on-chain, reducing the number of operations performed by every node on the network. In addition, due to the immutability of the transaction graph, various optimisation strategies can improve the throughput of transactions per second in the network. 


