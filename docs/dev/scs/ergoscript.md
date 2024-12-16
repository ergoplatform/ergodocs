---
tags:
  - ErgoScript
---

# ErgoScript

## Quick Navigation
- [Overview](#overview)
- [Sigma Protocols](#sigma-protocols)
- [Contract Model](#contract-model)
- [Key Aspects](#key-aspects)
- [Examples](#examples)

## Overview

**ErgoScript is a super-simple subset of Scala.** It is a top-level language translated into a low-level language called [ErgoTree](ergotree.md), which is translated during execution into cryptographic protocol. That's how Ergo supports ring and threshold signatures and much more crypto protocols with no special cases made in the core!

/// admonition | Sigma Protocols
    type: tip

Ergo's support for [sigma-protocols](sigma.md) (aka generalized Schnorr proofs) are truly unique as building blocks for composable statements. [Schnorr protocols](schnorr.md) and [proof-of-Diffie-Hellman-tuples](diffie.md) are supported by default, with more options available that the community can add via soft forks.
///

ErgoScript is built considering Bitcoin's security and privacy to make all kinds of complex financial contracts accessible. In comparison, Bitcoin's design doesn't allow loops or building any complex smart contracts on top of it. ErgoScript allows for self-replication; therefore, we can use it to create Turing-Complete processes in a blockchain.

//// details | Background Reading
    {type: info, open: false}
/// details | **What are the key aspects of the Ergo contract model that make it different?**
    {type: info, open: false}

### Paradigm

The account model of Ethereum is imperative. This means that the typical task of sending coins from Alice to Bob requires changing the balances in storage as a series of operations. Ergo's UTXO-based programming model, on the other hand, is declarative. ErgoScript contracts specify conditions for a transaction to be accepted by the blockchain (not changes to be made in the storage state due to the contract execution).

### Scalability

In the account model of Ethereum, both storage changes and validity checks are performed _on-chain_ during code execution. In contrast, Ergo transactions are created _off-chain_, and only validation checks are performed on-chain, thus reducing the number of operations performed by every node on the network. In addition, due to the immutability of the transaction graph, various optimization strategies can improve the throughput of transactions per second in the network. [Light verifying nodes](nipopow_nodes.md) are also possible, thus further facilitating scalability and accessibility of the network.

### Shared state

The account-based model relies on the shared mutable state, which is known to lead to complex semantics (and subtle million-dollar bugs) in the context of concurrent/ distributed computation. Ergo's model is based on an immutable graph of transactions. This approach, inherited from Bitcoin, plays well with blockchains' concurrent and distributed nature and facilitates light trustless clients.

### Expressive Power

Ethereum advocated the execution of a Turing-complete language on the blockchain. It theoretically promised unlimited potential; however, severe limitations came to light from excessive blockchain bloat, subtle multi-million dollar bugs, gas costs that limit contract complexity, and other such problems. Ergo on the flip side, extends UTXO to enable Turing completeness while limiting the complexity of the ErgoScript language itself. The same expressive power is achieved differently and more semantically soundly.

///
/// admonition | Simple Example
    type: info

```scala
if (HEIGHT < 100000) alicePubKey else bobPubKey
```

1. Allows Only Alice to spend a box before a certain height 
2. Allows Only Bob to spend the box after that.

///
/// admonition | Key Concepts
    type: info

Explore the [Core Concepts of ErgoScript](ergoscript-key-concepts.md).
///

/// admonition | Context Claims
    type: note

Ergo offers a unique approach to smart contract-enabled blockchains, providing efficient global context claims through the concept of data inputs.

///
/// admonition | ErgoScript vs ErgoTree
    type: note

ErgoScript is a high-level developer-friendly language for writing smart contracts that are then compiled to ErgoTree before being written to the blockchain. Explore the distinction [here](ergoscriptvergotree.md)
///
////

/// admonition | Getting Started
    type: note

Please see this [Quick Primer on ErgoScript](/dev/scs/ergoscript-primer) for an overview of key concepts and some basic examples.
///

## Related Technical Resources
- [ErgoTree Documentation](ergotree.md)
- [Sigma Protocols Overview](sigma.md)
- [Schnorr Signatures](schnorr.md)
- [Light Verifying Nodes](nipopow_nodes.md)
- [UTXO Model Explanation](/dev/protocol/eutxo)

## Comparative Analysis
ErgoScript stands out by:

- Providing Turing-completeness without compromising blockchain efficiency
- Supporting advanced cryptographic protocols
- Enabling complex financial contracts with minimal overhead
- Maintaining a declarative, secure programming model

## Performance Considerations
- Off-chain transaction creation
- On-chain validation only
- Immutable transaction graph
- Supports light verifying nodes
- Controlled Turing-completeness
