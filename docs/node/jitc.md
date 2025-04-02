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

Discussions about transaction efficiency, scalability, and costing are common in the cryptocurrency space. For a blockchain technology to achieve long-term viability and widespread adoption, adaptability and scalability are crucial. Ergo's Protocol Reference Client 5.0.0 introduced significant advancements, offering substantial benefits to miners, developers, and users across the ecosystem, particularly regarding script execution costing.

If you are new to blockchain, terms like scalability and costing might seem complex. **Scalability** refers to a blockchain's capacity to handle an increasing number of transactions. As a platform grows, transaction volume typically increases. Without effective scaling mechanisms, the network can become congested, leading to longer confirmation times. **Costing** refers to the computational expense associated with validating transactions and smart contracts. In Proof-of-Work blockchains like Ergo, every transaction incurs a fee, partly determined by its computational cost. Historically, this cost has been estimated using either Ahead-of-Time (AOT) or Just-In-Time (JIT) methods. Until version 5.0.0, Ergo primarily used AOT costing, which estimates costs *before* script execution to prevent excessively resource-intensive scripts from overwhelming the network.

## Ergo Protocol Reference Client 5.0.0 and Hybrid Costing

The release of Reference Client 5.0.0 introduced several network improvements, including a more efficient hybrid costing model ([EIP-39](https://github.com/ergoplatform/eips/pull/79)). This enhances the network's user experience (UX) by allowing more efficient transaction processing within blocks, benefiting miners, developers, and users.

As mentioned, Ergo previously relied mainly on AOT costing. Reference Client 5.0.0 introduced a hybrid model combining AOT and JIT costing. For a detailed explanation, refer to the blog post: "[Ergo's Hybrid Method for Counting Costs](https://ergoplatform.org/en/blog/2022-02-09-ergos-hybrid-method-for-counting-costs/)".

The hybrid costing model operates in two stages during transaction validation:

1.  **Reduction Stage (JIT Costing)**: Each input's guarding script (ErgoTree) is reduced to its final sigma proposition (a cryptographic condition like `proveDlog(pk)` or `atLeast(2, Coll(pk1, pk2, pk3))`). The cost of this reduction phase is calculated using **Just-In-Time (JIT)** costing, meaning the cost is determined based on the actual operations performed during reduction.
2.  **Cryptographic Verification Stage (AOT Costing)**: Once all input scripts are reduced to sigma propositions, the cost of verifying the required cryptographic proofs (e.g., signature checks) is calculated using **Ahead-of-Time (AOT)** costing. AOT costing for crypto operations is simple, fast, and predictable.

The costs from both stages are aggregated to determine the final cost of the transaction. This transaction cost is then added to the cumulative cost of the block being validated. A block is only valid if its total accumulated cost remains within the maximum allowed block budget.

Cryptographic operations are significantly more resource-intensive than reduction operations, typically consuming around 80% of the verification time. Using AOT costing for the cryptographic stage ensures that denial-of-service attacks based on expensive crypto operations remain infeasible. The JIT costing applied during the reduction stage provides a more accurate measure of the actual computational work performed during script execution.

This two-part costing method enables more efficient and accurate cost estimation compared to relying solely on AOT costing.

As a result of these improvements in Reference Client 5.0.0, users and developers benefit from potentially faster script execution times (as costs more accurately reflect actual work) and more efficient utilization of block space. This allows blocks to potentially accommodate more transactions, thereby increasing network throughput.

For further details on Reference Client 5.0.0, please visit the [GitHub release page](https://github.com/ergoplatform/ergo/releases/tag/v5.0.0). You will find comprehensive information about Sigma Interpreter 5.0.0, testnet settings, and the EIP-39 implementation.
