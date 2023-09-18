---
tags:
  - Flash Loans
---

# The Challenges and Risks of Implementing Flash Loans on Ergo

Flash loans, while gaining significant attention in the world of decentralized finance (DeFi), primarily on Ethereum's account-based blockchain, have also been the root cause of numerous attacks. These loans, which allow users to borrow funds without collateral and return them within the same transaction, have not only revolutionized but also destabilized DeFi on account-based blockchains due to their inherent risks. Implementing them on eUTXO (Extended Unspent Transaction Output) blockchains poses several challenges and potential concerns.

## Understanding UTXO and Its Distinctiveness

The [UTXO (Unspent Transaction Output)](eutxo.md) model, which was first introduced by Bitcoin, operates [differently from account-based models like Ethereum](accountveutxo.md). In the UTXO model, transactions utilize unspent transaction outputs (UTXOs) and generate new ones. This is a stark contrast to the account-based model, where smart contracts maintain a dynamic state that can be modified by other transactions within the same block. UTXO blockchains, on the other hand, necessitate that all computations be performed beforehand and incorporated into the transaction itself.

## Deterministic Nature of UTXO Blockchains

UTXO blockchains are deterministic, meaning all outcomes must be predictable before being added to the blockchain. This property conflicts with the inherently dynamic nature of flash loans, where one contract might depend on the outcome of another, all within the same transaction. You would need to predict the final state of all affected UTXOs beforehand, a near-impossible task given the real-time fluctuations in DeFi markets.

## Why Flash Loans Are Difficult on eUTXO 

### One Transaction, Many Steps

Flash loans usually involve multiple steps: borrowing funds, performing an action like arbitrage, and then repaying the loan, all within one transaction. In eUTXO blockchains, this would be highly impractical. Each 'step' would require its own transaction, which would have to be computed beforehand due to the deterministic nature of the model.

### Cross-Protocol Interactions Are Complex

Flash loans often require interacting with multiple DeFi protocols rapidly. In eUTXO systems, this would mean packaging multiple UTXOs, from various protocols, into a single transaction. Calculating all these in advance would be complex and computationally intensive.

### No Guarantees of Atomic Execution Within a Block

Flash loans are designed to be [atomic](atomic-composability.md)—either the whole chain of transactions is completed, or none are. This is straightforward in account-based blockchains where multiple interactions can occur within the same block. However, eUTXO blockchains do not offer such guarantees, making it risky if a multi-step flash loan transaction spans across multiple blocks.

## Potential Workarounds and Considerations

### Data Inputs

[Data inputs](read-only-inputs.md), a unique feature in Ergo's UTXO model, allow transactions to reference existing UTXOs and read their data without consuming them. This feature can be leveraged to address some of the limitations associated with flash loans in eUTXO systems by allowing multiple transactions within a block or slot to read the data from the same UTXO concurrently.

### Multi-Stage Contracts

[Multi-stage contracts](multi.md) offer a way to work around some of these limitations. These contracts allow a series of transactions to be 'chained' together, emulating more complex, multi-step processes. They can hold interim states and even facilitate parallelized actions.

1. **Interim State Management**: These contracts can 'remember' a partial state, enabling a more complex, sequenced series of transactions, somewhat simulating a flash loan's multi-step process.
   
2. **Complex Logic and Parallel Actions**: These contracts can also facilitate more complex transaction logic, and even actions in parallel, which is closer to how flash loans operate on account-based blockchains.

**Challenges of Multi-Stage Contracts**

1. **Still No Atomicity**: While these contracts can enable complex transactions, they can't guarantee that these will all be processed in the same block, a fundamental feature of flash loans.
  
2. **High Complexity, High Risk**: The more complex the system, the higher the likelihood of security risks, particularly in financial operations like flash loans.

## Hard Fork

Atomicity of chained transactions can be supported via hard-fork extension. If the community wanted such a hard fork, we could extend the transaction serialisation format adding special extensions section for each transaction. This section can be used to mark some transactions as belonging to a chain, which will force all miners to either accept the whole chain, or not.

## Conclusion

The eUTXO model inherently promotes transaction security and predictability at the cost of some functionalities that are easier to implement in account-based systems, such as flash loans. While weak blocks and multi-stage contracts offer interesting workarounds, they do not fully address the challenges and risks posed by implementing flash loans in eUTXO blockchains.
