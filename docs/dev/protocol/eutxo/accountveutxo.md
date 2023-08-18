---
tags:
  - UTXO
---

# UTXO vs Account: Understanding Ergo's Transaction Model

Ergo, similar to Bitcoin, employs the Unspent Transaction Outputs (UTXO) model instead of the Account model used in platforms like Ethereum. This documentation aims to provide a comprehensive understanding of the UTXO model, also known as the Box model, and highlight the advantages it brings.

## Account Balance and UTXO

In the Account model, a balance is represented as a simple numerical value that increases or decreases with transactions. This parallels real-world transactions where your bank balance changes when money is added or deducted. Transactions to and from an account directly affect the blockchain balance.

On the other hand, the UTXO model, introduced by Bitcoin, takes a different approach. It considers an individual's balance as a collection of unspent outputs, analogous to having multiple portions of bread dough. The total balance is the sum of these portions, or UTXOs. These UTXOs can be split or merged before being transferred to another address. Let's illustrate this with an example:

1. Alice has 100 units (100 ERG). She sends 75 units to Bob and keeps 25 units for herself.
2. Charlie has 250 units. He transfers 150 units to Bob and retains 100 units.
3. Bob splits 20 units from the 150 units received from Charlie and merges them with the 75 units received from Alice. He then sends a total of 205 units to Dave, keeping 20 units for himself.

Dave now owns 205 units previously owned by Charlie, Alice, and Bob. In the UTXO model, these units can be split and merged, but they retain their original identity, unlike bread dough. The transaction history of these units can be traced back to when they were initially created.

## Advantages of the eUTxO Model over Account-Based Blockchains

The UTXO (Unspent Transaction Output) model used in Ergo offers several advantages over account-based blockchains like Ethereum. Let's compare the UTXO model to the account model to highlight these benefits:

1. **Immutability and Security:**
      - Ergo's eUTxO model: Each UTXO is immutable and cannot be modified during a transaction. This enhances security and simplifies transaction verification.
      - Account Model: Account balances can be modified during a transaction, which introduces potential vulnerabilities and requires careful state management.

2. **Simplicity and Developer-Friendliness:**
      - Ergo's eUTxO model: ErgoScript contracts in the UTXO model use a declarative programming paradigm. This simplifies development and reduces the likelihood of mistakes.
      - Account Model: The account model uses an imperative programming paradigm, which can be more challenging for developers and increase the risk of errors.

3. **Support for Off-Chain Protocols:**
      - Ergo's eUTxO model: Ergo's UTXO model provides better support for off-chain protocols like sidechains and the Lightning Network. Off-chain transaction creation reduces on-chain operations, improving scalability and network efficiency.
      - Account Model: Account-based blockchains have limited support for off-chain protocols, making it more challenging to scale and utilize layer-2 solutions effectively.

4. **Scalability and Optimization:**
      - Ergo's eUTxO model: The UTXO model allows for efficient off-chain transaction creation and verification. On-chain operations primarily focus on validation checks, reducing computational load and enhancing scalability.
      - Account Model: In account-based blockchains, most operations occur on-chain, leading to increased computational requirements and potentially limiting scalability.

5. **Concurrent and Distributed Nature:**
      - Ergo's eUTxO model: Ergo's UTXO model aligns well with the concurrent and distributed nature of blockchains. The immutable transaction graph simplifies system design, reduces complexities, and enables light trustless clients.
      - Account Model: Account-based blockchains face challenges in handling concurrency and distributed environments due to mutable balances and more complex state management.

6. **Expressive Power with Turing Completeness:**
      - Ergo's eUTxO model: Ergo extends the UTXO model to achieve Turing completeness through transaction trees and [multi-stage protocols](multi.md). It provides expressive power while mitigating issues such as blockchain bloat, bugs, and gas costs.
      - Account Model: Ethereum's Turing-complete execution model faces challenges related to scalability, security, and gas costs due to the complexities of executing a complete language on-chain.

By leveraging the UTXO model, Ergo combines immutability, simplicity, scalability, and expressive power to address some of the limitations and challenges faced by account-based blockchains like Ethereum. It offers enhanced security, developer-friendliness, support for off-chain protocols, and improved scalability, making it a compelling choice for decentralized applications.