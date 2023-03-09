---
tags:
  - ErgoScript
---

# A Quick Primer on ErgoScript

The Ergo node does not understand ErgoScript. Instead, it uses a low-level language called [**ErgoTree**](https://ergoplatform.org/docs/ErgoTree.pdf), which is a "tree" based language (somewhat like XML). 

However, writing code in ErgoTree is *difficult*.  

- ErgoTree is similar to Bitcoin's Script in some aspects. 
- An ErgoTree program is deterministic and consists of a sequence of boolean predicates joined using `AND` and `OR`.
- Ergo nodes execute the ErgoTree program contained in a transaction and consider it valid if it evaluates to `true`.

An example of such an ErgoTree program would be 

```scala
AND(OR(condition_1, condition_2), condition_3)
```

which implies that the transaction is valid if `condition_3` and at least one of `condition_1` or `condition_2` hold.    

[ErgoScript](ergoscript.md) is a high-level developer-friendly language for writing smart contracts that are then compiled to ErgoTree before being written to the blockchain.

The equivalent of the above program in ErgoScript would be 

```scala
(condition_1 || condition_2) && condition_3
```



## ErgoScript Examples

> **Tip:** For beginners, we highly recommend the [ErgoScript P2S playground](https://wallet.plutomonkey.com/p2s/), which can be used to get the Ergo address corresponding to some arbitrary ErgoScript program. Please use the P2S playground only for experiments.


- [Anyone Can Spend Scripts](anyone-can-spend.md)
- [No-one-Can Spend Scripts](no-one-can-spend.md)
- [Context Variables](context-variables.md)
- [Code-blocks](code-blocks.md)
- [Public-keys](public-keys.md)
- [Functional Programming](functional-programming.md)
- [Box Structure](box-structure.md)
- [Storing Data](storing-data.md)
