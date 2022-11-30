# Transaction Tree

A **transaction tree** is an extension of [transaction chains](tx-chains.md) where the code can contain `if` statements and simple loops, i.e., where some start and end nodes are the same. The following figure illustrates a transaction tree.

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

Next we'll look at [Transaction Graphs](tx-graphs.md)