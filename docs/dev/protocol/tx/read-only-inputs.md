# Data Inputs

This section provides an overview of data inputs in Ergo. It explains the concept of data inputs, their benefits, and their usage in transactions. 

## Understanding Data Inputs

In traditional UTXO-based blockchains, transactions typically require spending and destroying all inputs. However, Ergo introduces the concept of **data inputs** to allow transactions to reference existing UTXOs and read their data without consuming them. This innovation solves the limitations normally associated with eUTXO.

Data inputs enable multiple transactions within a block or slot to read the data from the same UTXO concurrently, as none of them actually spend or destroy the data. This parallel processing of data inputs reduces transaction fees, as smart contract execution is not required, and there is no need to create extra outputs. Additionally, data inputs address various other challenges, making them a valuable design choice for all UTXO-based blockchains.

## Benefits of Data Inputs

By incorporating data inputs, Ergo provides the following advantages:

1. **Reduced Transaction Fees**: Since data inputs do not trigger smart contract execution or require additional outputs, transaction fees are reduced.

2. **Concurrent Data Access**: Multiple transactions can read data from the same UTXO concurrently, improving efficiency and scalability.

3. **Enhanced DeFi Applications**: Data inputs are particularly beneficial for decentralized finance (DeFi) applications. They allow referencing a box without the need to spend it, making them suitable for use cases like decentralized order-books (DEX).

## Working with Data Inputs

In Ergo, data inputs are unique to the platform and not yet present in other extended-UTXO systems. Multiple transactions can share a data input box, which contains a single reference to the box within the block.

It is also possible to spend a data input box in the same transaction, provided that it existed before the transaction was applied. This allows for flexibility in transaction construction.

To illustrate the usage of data inputs, consider the example transaction where a box with the ID `d2b9b6536287b242f436436ce5a1e4a117d7b4843a13ce3abe3168bff99924a1` is both an input and a data input. This transaction demonstrates how data inputs can be utilized effectively.

When writing scripts in Ergo, you can refer to other boxes in the transaction. For instance, the code snippet `INPUTS(0).value > 10000 && OUTPUTS(1).value > 20000` enforces a condition on the first input and the second output boxes.

For a more detailed comparison between the logic used in eUTXO and account-based models, refer to the [Off Chain Logic & eUTXO](https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/) article. Additionally, you can explore the [model transaction](model-tx.md) to gain a better understanding of transaction structure.

## Additional Resources

To learn more about the potential of the UTXO model and its implementation in Ergo, we recommend reading the introductory article [Unlocking The Potential Of The UTXO Model](https://github.com/Emurgo/Emurgo-Research/blob/master/smart-contracts/Unlocking%20The%20Potential%20Of%20The%20UTXO%20Model.md). You can also find further information and discussions in the following forum posts:

- [Building A Portable And Reusable (PaR) UTXO dApp Standard](https://www.ergoforum.org/t/building-a-portable-and-reusable-par-utxo-dapp-standard/441)
- [Data Inputs Semantics](https://www.ergoforum.org/t/data-inputs-semantics/654)

