# Transaction Tree

A *transaction tree* is a structure that represents a sequence of related transactions in a hierarchical manner, with each transaction in the tree having one or more child transactions that are dependent on its successful execution.

A transaction tree can be thought of as a more complex version of a [transaction chain](tx-chains.md), in which each transaction in the chain may have multiple child transactions, each of which may in turn have their own child transactions. This creates a branching structure that resembles a tree, with the original transaction at the root and subsequent transactions branching off from it.

Transaction trees can be useful for representing more complex transaction sequences and dependencies, particularly in the context of smart contracts and other advanced blockchain applications. They can help to ensure that transactions are executed in the correct order and with appropriate dependencies, while also providing a more detailed and flexible view of the overall transaction sequence.


## Process

A transaction tree is an extension of transaction chains where the code can contain `if` statements and simple loops, i.e., where some start and end nodes are the same. The following figure illustrates a transaction tree.

![](../../../assets/img/scs/tx-tree.png)

An `if` statement is handled using the following pseudocode.

```
if (condition) { out.propositionBytes == state_3_code }
else { out.propositionBytes == state_4_code }
```

A simple loop is a special case of the `if` statement:

```
if (condition) { out.propositionBytes == state_2_code }
else { out.propositionBytes == SELF.propositionBytes }
```

Most useful contracts can be represented using branches and simple loops but no cycles (as shown by examples in the paper). Ergo can be used to create such contracts using UTXOs.


Next, we'll look at [Transaction Graphs](tx-graphs.md)