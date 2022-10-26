# Smart Contracts

[ErgoScript](https://ergoplatform.org/docs/ErgoScript.pdf) is the smart contract language used by the Ergo blockchain. While it has concise syntax adopted from Scala/Kotlin, it may seem not very clear at first because, conceptually, ErgoScript is quite different from conventional languages, which we all know and love. Ergo is a UTXO-based blockchain, whereas smart contracts are traditionally associated with account-based systems like Ethereum. However, Ergo's transaction model has many advantages over the account-based model. With the right approach, developing Ergo contracts can be significantly easier than writing and debugging Solidity code.

The [ErgoScript](ergoscript.md) page provides an overview of all resources related to smart contract development, or dive straight into the [ErgoScript Primer](ergoscript-primer.md).

**Below, we will cover the key aspects of the Ergo contract model which makes it different:**

##### Paradigm   

The account model of Ethereum is imperative. This means that the typical task of sending coins from Alice to Bob requires changing the balances in storage as a series of operations. Ergo's UTXO-based programming model, on the other hand, is declarative. ErgoScript contracts specify conditions for a transaction to be accepted by the blockchain (not changes to be made in the storage state due to the contract execution).

##### Scalability

In the account model of Ethereum, both storage changes and validity checks are performed _on-chain_ during code execution. In contrast, Ergo transactions are created _off-chain_, and only validation checks are performed on-chain, thus reducing the number of operations performed by every node on the network. In addition, due to the immutability of the transaction graph, various optimization strategies can improve the throughput of transactions per second in the network. [Light verifying nodes](nipopow_nodes.md) are also possible, thus further facilitating scalability and accessibility of the network.

##### Shared state

The account-based model relies on the shared mutable state, which is known to lead to complex semantics (and subtle million-dollar bugs) in the context of concurrent/ distributed computation. Ergo's model is based on an immutable graph of transactions. This approach, inherited from Bitcoin, plays well with blockchains' concurrent and distributed nature and facilitates light trustless clients.

##### Expressive Power

Ethereum advocated the execution of a Turing-complete language on the blockchain. It theoretically promised unlimited potential; however, severe limitations came to light from excessive blockchain bloat, subtle multi-million dollar bugs, gas costs that limit contract complexity, and other such problems. Ergo on the flip side, extends UTXO to enable Turing completeness while limiting the complexity of the ErgoScript language itself. The same expressive power is achieved differently and more semantically soundly.

