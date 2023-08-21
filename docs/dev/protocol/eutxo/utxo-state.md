# UTXO State

## Introduction

The UTXO (Unspent Transaction Output) state is a fundamental concept in blockchain technology, particularly in platforms that use the UTXO model, such as Ergo and Cardano. This model differs from the account-based model used by other platforms like Ethereum. The account-based model requires nodes to check all accounts to validate the system, whereas in the UTXO model, nodes primarily verify transactions.

## UTXO and Transaction Validation

This section will delve into the intricacies of the UTXO state, its role in transaction validation, and how it influences the design and execution of smart contracts on platforms like Ergo and Cardano. By leveraging the advantages of UTXO and extending its capabilities with eUTXO, Ergo provides a powerful and efficient platform for building and executing smart contracts. In the eUTXO model, Ergo allows smart contracts to utilize UTXOs as data inputs without modifying them, enabling parallel computation and facilitating non-custodial atomic swaps. This makes it easier to perform complex operations securely and efficiently.

## UTXO Model and Transactions

In the UTXO model, a transaction consumes unspent outputs from previous transactions and creates new output(s) that can be used as inputs for future transactions. These transactions are atomic state transition operations, which means they destroy a box from the state and create new ones. Each transaction consists of one or more input boxes, which are the source of funds for the transaction and will be destroyed by the transaction, and one or more output boxes, which are the destination of funds and will be created by the transaction.

## UTXO State and Boxes

The UTXO state, therefore, is a database of all unspent transaction outputs, or boxes. Each box is an immutable unit, which can be created or removed, but never altered. The box is not just a simple coin; it houses data, code, and registers, with all of its contents exclusively stored in the registers. Four pre-defined registers contain the box's monetary value, its protection script, and the ID of the transaction that created the box. Each box has a unique ID, derived from the unique contents of the box, including the data of the transaction that created it.

## UTXO and Cryptocurrency

Each UTXO represents a certain amount of cryptocurrency and can only be spent once by the owner of the private key associated with it. When a UTXO is spent, it is removed from the UTXO state. When a transaction creates new outputs, they are added to the UTXO state.

## Advantages of UTXO Model

The UTXO model has several advantages, including parallelizability of transactions, improved privacy, and a clear ownership structure. The inherent design of UTXO supports parallel transaction processing, making it simpler to scale the network. Additionally, UTXOs are more compatible with stateless client solutions and are well-suited for off-chain and sidechain protocols, enabling seamless integration with various solutions beyond the main chain.

## Challenges in UTXO Model

However, the UTXO model also presents unique challenges for developers, such as handling UTXO fragmentation and understanding the concept of "change" outputs. For instance, if the transaction is spending boxes protected by a non-trivial script, its inputs should also contain proof of spending correctness - context extension (user-defined key-value map) and data inputs (links to existing boxes in the state) that you may use during script reduction to crypto, signatures that satisfy the remaining cryptographic protection of the script.

## Conclusion

The UTXO model, despite its challenges, offers a robust and efficient method for transaction validation and execution of smart contracts. For more information on related topics, refer to [Ergo vs Cardano](ergo_vs_cardano.md) and [Sigma Protocols](sigma.md).

