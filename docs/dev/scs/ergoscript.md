---
tags:
  - ErgoScript
  - Smart Contracts
  - Sigma Protocols
---

# ErgoScript

## Overview

**ErgoScript** is a simple yet powerful scripting language for [smart contracts](contracts.md) on the Ergo blockchain, designed as a subset of Scala. It allows developers to define complex conditions for spending funds. ErgoScript code is translated into a lower-level representation called [**ErgoTree**](ergotree.md) before being stored on the blockchain. During transaction validation, ErgoTree is interpreted using cryptographic protocols based on [Sigma Protocols](sigma.md). This unique architecture enables Ergo to support advanced cryptographic functionalities like [ring signatures](ring.md) and [threshold signatures](threshold.md) directly within the scripting language, without needing special core protocol changes.

/// admonition | Sigma Protocols
    type: tip

Ergo's support for [**Sigma Protocols**](sigma.md) (aka generalized Schnorr proofs) is a key feature, providing efficient and composable building blocks for zero-knowledge proofs. [Schnorr proofs](sigma/schnorr.md) and [proofs of Diffie-Hellman tuples](sigma/diffie.md) are supported by default, with the potential for the community to add more via [soft forks](soft-fork.md).
///

ErgoScript builds upon the security principles of Bitcoin while enabling much more complex financial contracts. Unlike Bitcoin Script, ErgoScript supports features necessary for advanced applications, including the ability to reference blockchain state and implement complex logic, effectively enabling Turing-Complete computations through [multi-stage contract interactions](multi.md).

//// details | Background Reading
    {type: info, open: false}
/// details | Contract Model Comparison: Ergo (eUTXO) vs. Ethereum (Account)
    {type: info, open: false}

### Paradigm

The account model (used by Ethereum) is imperative: sending coins involves changing balances in a global storage state. Ergo's [eUTXO-based](eutxo.md) programming model is declarative: ErgoScript contracts specify *conditions* under which funds ([UTXOs](eutxo.md)) can be spent, rather than dictating state changes.

### Scalability

In the account model, both storage changes and validity checks happen **on-chain** during contract execution. In Ergo, [transactions](transactions.md) are typically created **off-chain**, and only the validation checks occur on-chain. This significantly reduces the computational load on validating [nodes](modes.md). The immutable nature of the transaction graph also allows for various optimizations to improve throughput. Furthermore, Ergo's design facilitates [**light verifying nodes**](nipopow_nodes.md) (via [NIPoPoWs](nipopows.md)), enhancing network [scalability](scaling.md) and accessibility.

### Shared State

The account-based model relies on a shared mutable state, which can lead to complex interactions and subtle bugs in concurrent systems. Ergo's model, based on Bitcoin's UTXO concept, uses an immutable graph of transactions, which is inherently more suitable for distributed environments and simplifies the development of [light clients](light-spv-node.md).

### Expressive Power

While Ethereum's Turing-complete language offers theoretical flexibility, it has practical limitations like blockchain bloat, complex bugs, unpredictable gas costs, and limits on contract complexity. Ergo achieves similar expressive power through its [eUTXO model](eutxo.md) and [multi-stage contracts](multi.md), but intentionally keeps the core ErgoScript language non-Turing-complete to enhance security and predictability.

///
/// admonition | Simple Example
    type: info

```scala
// This script locks funds in a box.
// It allows Alice to spend the funds before block 100,000,
// OR Bob to spend them at or after block 100,000.
{
  (HEIGHT < 100000 && alicePubKey) ||
  (HEIGHT >= 100000 && bobPubKey)
}
```
*(`HEIGHT` is a context variable representing the current block height. `alicePubKey` and `bobPubKey` represent proof of knowledge of their respective secret keys, typically via a signature check).*

///
/// admonition | Key Concepts
    type: info

Explore the [Core Concepts of ErgoScript](ergoscript/ergoscript-key-concepts.md).
///

/// admonition | Data Inputs
    type: note

Ergo offers a unique approach to smart contracts by allowing them to access data from other [boxes](box.md) on the blockchain without spending them, using **[data inputs](read-only-inputs.md)**. This enables efficient access to shared information like [oracle price feeds](oracles.md) or [DAO](dao.md) parameters.

///
/// admonition | ErgoScript vs ErgoTree
    type: note

ErgoScript is the high-level, developer-friendly language. It gets compiled into **[ErgoTree](ergotree.md)**, a lower-level, serialized representation stored on the blockchain and interpreted by nodes. Explore the distinction [here](ergotree.md).
///
////

/// admonition | Getting Started
    type: note

Please see this [Quick Primer on ErgoScript](ergoscript-primer.md) for an overview of key concepts and some basic examples.
///

## Related Technical Resources
- [ErgoTree Documentation](ergotree.md)
- [Sigma Protocols Overview](sigma.md)
- [Schnorr Signatures](sigma/schnorr.md)
- [Light Verifying Nodes](nipopow_nodes.md)
- [eUTXO Model Explanation](eutxo.md)

## Comparative Analysis
ErgoScript stands out by:

- Enabling complex logic via the [eUTXO model](eutxo.md) without full on-chain Turing-completeness risks.
- Natively supporting advanced cryptographic protocols ([Sigma Protocols](sigma.md)).
- Allowing complex financial contracts with predictable execution costs.
- Maintaining a declarative, secure programming model based on UTXOs.

## Performance Considerations
- Off-chain transaction creation minimizes on-chain computation.
- On-chain validation focuses only on script conditions.
- Immutable transaction graph allows for optimizations.
- Native support for light verifying nodes enhances accessibility.
- Non-Turing complete base language prevents infinite loops and simplifies cost analysis.
