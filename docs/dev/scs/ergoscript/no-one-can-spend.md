# Unspendable Scripts in ErgoScript

In contrast to the [previous examples](anyone-can-spend.md), ErgoScript can also create programs at the opposite end of the flexibility spectrum that always evaluate to `false`. 

Here's an example of such a script:

```scala
true && false  // Corresponds to address m3iBKr65o53izn
```

The script in the example above results in an address to which funds can be sent, but not spent. These scripts are referred to as **no-one-can-spend scripts** due to this characteristic. It's crucial to remember not to send funds to these addresses as they cannot be retrieved.

Ergo features a concept known as [*'garbage collection'* or storage rent](rent.md). This mechanism ensures that boxes, such as those produced by no-one-can-spend scripts, are eventually removed from the blockchain over time to maintain the efficiency of the system.