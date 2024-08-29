---
tags:
  - Data Inputs
---

# Data Inputs in ErgoScript

Data inputs are a unique and powerful feature in ErgoScript that extend the capabilities of traditional UTXO-based blockchains. This section provides an in-depth overview of data inputs, their benefits, and how they can be used in Ergo transactions.

## Understanding Data Inputs

In traditional UTXO-based blockchains, transactions typically involve spending and consuming inputs, which are then destroyed. However, Ergo introduces **data inputs**—a concept that allows transactions to reference existing UTXOs (unspent transaction outputs) and read their data without consuming them. This innovation addresses several limitations inherent in traditional UTXO models and brings enhanced flexibility and efficiency to the extended UTXO (eUTXO) model used by Ergo.

### Key Features of Data Inputs

- **Non-Destructive Access:** Data inputs enable transactions to access the contents of UTXOs without consuming or spending them. This means that the referenced UTXOs remain intact and can be used in future transactions.
- **Concurrent Data Access:** Multiple transactions within the same block can reference and read the data from a single UTXO simultaneously, as none of the transactions actually spend the UTXO. This capability supports parallel processing and reduces bottlenecks in transaction execution.

## Benefits of Data Inputs

Incorporating data inputs into ErgoScript provides several significant advantages:

1. **Reduced Transaction Fees:** Data inputs do not trigger the execution of scripts or the need to create additional outputs, leading to lower transaction fees. This makes them a cost-effective solution for complex transactions.
  
2. **Enhanced DeFi Applications:** Data inputs are particularly useful for decentralized finance (DeFi) applications, such as decentralized exchanges (DEXs) or order-book systems. They allow contracts to reference external data (e.g., oracle data or order book states) without consuming the data boxes, ensuring that multiple participants can interact with the same state concurrently.

3. **Improved Scalability and Efficiency:** By allowing multiple transactions to read from the same data input concurrently, data inputs help improve the scalability and efficiency of the network. This reduces the need for additional outputs and mitigates the risk of transaction conflicts.

## Working with Data Inputs

Data inputs are unique to Ergo and are not yet present in other eUTXO-based systems. When working with data inputs in ErgoScript, it’s important to understand how they function and how they can be utilized effectively in your smart contracts.

### Usage in Transactions

Data inputs in ErgoScript are essentially "read-only" boxes that provide necessary information for contract validation without being consumed by the transaction. For example, a DeFi contract might use a data input to check the current price of an asset from an oracle box, ensuring that the transaction adheres to certain conditions without altering the oracle box itself.

### Example Use Case

Consider a transaction where a box with the ID `d2b9b6536287b242f436436ce5a1e4a117d7b4843a13ce3abe3168bff99924a1` is referenced as both an input and a data input. This scenario demonstrates the flexibility of data inputs, allowing a transaction to read and possibly update a box’s state in a single operation, provided the box existed before the transaction was applied.

In ErgoScript, you can refer to other boxes in the transaction using constructs like:

```scala
INPUTS(0).value > 10000 && OUTPUTS(1).value > 20000
```

This script enforces conditions based on the values of the first input and the second output boxes, showcasing how data inputs can be used to influence the logic of a transaction without consuming the referenced boxes.

### Comparison with Traditional Models

Data inputs in ErgoScript provide a significant advancement over traditional UTXO models, particularly in how they facilitate more complex and interactive smart contracts. For a more detailed comparison between eUTXO and account-based models, refer to the [Off Chain Logic & eUTXO](https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/) article.

## Best Practices and Considerations

- **Selective Use:** Only include data inputs that are necessary for your contract logic to minimize transaction size and fees.
- **Reliable Sources:** Ensure that the data accessed through data inputs is reliable and comes from trusted sources, especially when using oracles or external data providers.
- **Validation Checks:** Always validate the data within data inputs to ensure it is in the expected format and state, reducing the risk of transaction failures.

## Additional Resources

For further reading and deeper understanding of the UTXO model and its implementation in Ergo, consider the following resources:

- [Unlocking The Potential Of The UTXO Model](https://github.com/Emurgo/Emurgo-Research/blob/master/smart-contracts/Unlocking%20The%20Potential%20Of%20The%20UTXO%20Model.md)
- [Building A Portable And Reusable (PaR) UTXO dApp Standard](https://www.ergoforum.org/t/building-a-portable-and-reusable-par-utxo-dapp-standard/441)
- [Data Inputs Semantics](https://www.ergoforum.org/t/data-inputs-semantics/654)
- [Model Transaction Example](model-tx.md)

### Conclusion

Data inputs are a powerful feature in ErgoScript that significantly enhance the flexibility, efficiency, and scalability of smart contracts. By allowing read-only access to UTXOs, data inputs enable more sophisticated interactions within the Ergo blockchain, making them an essential tool for developers building complex dApps and DeFi solutions.

