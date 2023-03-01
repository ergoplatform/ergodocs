# Transaction Graphs

A transaction graph is a structure that represents a set of related transactions in a more flexible and dynamic manner than a transaction tree. While a transaction tree is a hierarchical structure representing a sequence of transactions with specific dependencies between them, a transaction graph is a more general representation of the relationships between transactions with more complex and flexible dependencies.

In a transaction graph, each transaction is represented as a node, with edges connecting the nodes to represent dependencies between transactions. Unlike a transaction tree, which has a defined hierarchy and fixed relationships between transactions, a transaction graph allows for more complex and flexible relationships between transactions, including multiple dependencies and more complex branching.

Transaction graphs can be useful for representing complex transactions and dependencies, particularly in the context of smart contracts and other advanced blockchain applications. They allow for a more flexible and nuanced view of the transaction sequence, with the ability to represent more complex relationships and dependencies between transactions.

Transaction graphs are a powerful tool for representing complex blockchain transactions. They can help to improve the efficiency, scalability, and security of blockchain-based systems and applications, particularly in the context of advanced smart contracts and other decentralised applications.

As shown below, Ergo supports a more advanced technique called transaction graphs, where cycles are allowed in contract references.

![](../../../assets/img/scs/tx-graph.png)

Please see the [Advanced ErgoScript Tutorial](https://storage.googleapis.com/ergo-cms-media/docs/AdvancedErgoScriptTutorial.pdf) Section 3.3.3.