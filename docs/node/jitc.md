---
tags:
  - JITC
  - Just-In-Time Costing
  - AOTC
  - Node
  - Performance
  - Scalability
  - EIP-39
---

# Just-In-Time Costing

Whether you are an investor or developer, if you have been involved in the world of cryptocurrencies, you have probably encountered discussions about transaction efficiency, scalability, and costing on forums or Twitter threads. For a blockchain technology to achieve long-term viability and widespread adoption, it needs to be adaptable and scalable. With Ergo's latest Protocol Reference Client 5.0.0, the network takes significant leaps forward, introducing new features that offer substantial benefits to miners, developers, and users at all levels of the ecosystem.

If you are new to blockchain, terms like scalability and costing might seem perplexing. Scalability refers to a blockchain's ability to handle a growing number of transactions. As a platform expands, it is expected that the number of users executing transactions will significantly increase. Without proper scaling mechanisms, the network can become congested, resulting in longer transaction execution times. When discussing costing, we are referring to the expenses associated with a transaction. In the blockchain realm, every transaction incurs a fee, including fees for validating smart contracts. In Proof of Work blockchains, costing has traditionally been determined using either Ahead-of-Time (AOT) or Just-In-Time (JIT) costing. Until now, Ergo has employed AOT costing, which calculates cost estimates before executing any script, ensuring exclusion of excessively expensive scripts.

## Ergo Protocol Reference Client 5.0.0

The release of the Reference Client 5.0.0 introduces several network improvements. In simple terms, the network's user experience (UX) will be significantly enhanced due to increased transaction processing within a block, benefiting both miners and developers. Moreover, the network will offer more efficient costing capabilities.

As previously mentioned, Ergo has primarily utilized AOT costing for scripting. However, with Reference Client 5.0.0, Ergo takes a significant step forward by introducing a hybrid costing model that combines AOT and JIT costing. For a detailed explanation of Ergo's new hybrid costing approach, you can refer to a previous Ergo blog post titled "[Ergo's Hybrid Method for Counting Costs](https://ergoplatform.org/en/blog/2022-02-09-ergos-hybrid-method-for-counting-costs/)".

The hybrid costing model operates in two stages. In the first stage, transaction inputs pass through a verifier, with each input's script reduced to a sigma proposition—a type of spending condition that can be cryptographically verified. JIT costing is applied during this reduction stage. Once each input in the transaction has a sigma proposition, AOT costing, which is simple and fast, is employed to calculate the costs of all cryptographic operations within the transaction. The individual costs are then aggregated to determine the final cost of the transaction itself. Subsequently, the final cost of the transaction is added to the block cost, which must remain within the block budget before it can be added to the blockchain.

However, it's worth noting that these cryptographic operations are significantly more resource-intensive than reduction operations and typically consume 80% of the verification time. AOT costing ensures that a costing attack utilizing cryptographic operations is not feasible, while reduction operations are divided by a factor of 5, making them less vulnerable to attacks.

The same process is repeated for each transaction in the block, with the total cost of the block gradually accumulated. Before a block can be added to the blockchain, its cost must be below the allowed cost per block. The deployment of this new two-part costing method enables more efficient and accurate cost estimation with reduced expenses compared to using AOT costing alone.

As a result of these improvements in Reference Client 5.0.0, users and developers will experience faster script executions, and the available space within blocks will be utilized more efficiently. Faster script execution enables even

 higher transaction rates on the network, while improved costing allows blocks to accommodate more transactions, thereby increasing throughput.

For further details on the new Reference Client 5.0.0, please visit the [Github release](https://github.com/ergoplatform/ergo/releases/tag/v5.0.0) page. You will find comprehensive information about Sigma Interpreter 5.0.0, PaiNet testnet settings, as well as the EIP39 implementation.
