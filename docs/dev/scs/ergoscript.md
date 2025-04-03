---
tags:
  - ErgoScript
  - Smart Contracts
  - Sigma Protocols
---

# ErgoScript

## Overview

**ErgoScript** is a powerful, developer-friendly programming language designed specifically for writing [smart contracts](contracts.md) on the [Ergo blockchain](protocol-overview.md). Think of it as a specialized language that allows you to create complex [financial contracts](contracts.md) and applications with unprecedented flexibility and [security](security.md). Designed as a subset of Scala, it allows developers to define complex conditions for spending funds.

ErgoScript code is translated into a lower-level representation called [**ErgoTree**](ergotree.md) before being stored on the [blockchain](protocol-overview.md). During [transaction validation](validation.md), ErgoTree is interpreted using cryptographic protocols based on [Sigma Protocols](sigma.md). This unique architecture enables Ergo to support advanced cryptographic functionalities like [ring signatures](ring.md) and [threshold signatures](threshold.md) directly within the scripting language, without requiring special core protocol changes.

/// admonition | Sigma Protocols
    type: tip

Ergo's support for [**Sigma Protocols**](sigma.md) (aka generalized Schnorr proofs) is a key feature, providing efficient and composable building blocks for [zero-knowledge proofs](zkp.md). [Schnorr proofs](schnorr.md) and [proofs of Diffie-Hellman tuples](diffie.md) are supported by default, with the potential for the community to add more through [soft forks](soft-fork.md).
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

The account-based model relies on a shared mutable state, which can lead to complex interactions and subtle bugs in concurrent systems. Ergo's model, based on Bitcoin's UTXO concept, uses an immutable [graph of transactions](transactions.md), which is inherently more suitable for distributed environments and simplifies the development of [light clients](light-spv-node.md).

### Expressive Power

While Ethereum's Turing-complete language offers theoretical flexibility, it has practical limitations like blockchain bloat, complex bugs, unpredictable gas costs, and limits on contract complexity. Ergo achieves similar expressive power through its [eUTXO model](eutxo.md) and [multi-stage contracts](multi-stage-txs.md), but intentionally keeps the core ErgoScript language itself non-Turing-complete to enhance security and predictability.

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
*(`HEIGHT` is a context variable representing the current [block height](block-header.md). `alicePubKey` and `bobPubKey` represent proof of knowledge of their respective secret keys, typically via a [signature check](signing.md)).*

///
/// admonition | Key Concepts
    type: info

Explore the [Core Concepts of ErgoScript](ergoscript-key-concepts.md).
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


## Experimenting & Tooling

While ErgoScript aims for simplicity and security, debugging complex contracts can still be challenging. Currently, developers often rely on manual inspection and testing using the tools below. Tools are emerging to improve this process:

*   **[Debugging Guide](debugging.md):** Covers current best practices, tools, and techniques for debugging ErgoScript.
*   **[Ergoscript Simulator](https://github.com/spectrum-finance/ergoscript-simulator):** A community-developed tool that allows simulating ErgoScript execution.
*   **[ErgoScript P2S Playground](https://wallet.plutomonkey.com/p2s/):** Experiment and generate [Ergo addresses](address.md).
*   **[escript.online](https://escript.online/):** Online editor and compiler.
*   **[Scastie](scastie.md):** Online Scala compiler suitable for ErgoScript snippets.
*   **[Kiosk](stack/kiosk.md):** Web-based UI to explore ErgoScript.
*   **[Ergo-Puppet](puppet.md):** Advanced tool for off-chain experimentation and testing.

## Advanced Patterns & Tutorials

ErgoScript's features enable the implementation of complex contract patterns:

*   **[Finite State Machines (FSMs)](fsm-example.md):** Learn how to model multi-stage contracts where behavior depends on the current state encoded within a box.
*   **[Merkleized Abstract Syntax Trees (MAST)](mast-example.md):** Explore techniques to improve privacy and efficiency for contracts with many spending conditions by revealing only the executed script branch.

## Common Use Cases

ErgoScript's flexibility enables various applications:

*   **[Multi-Signature Wallets](threshold.md):** Create wallets requiring multiple parties to approve [transactions](transactions.md).
*   **Time-Locked Contracts:** Define contracts that can only be executed after a specific time or [block height](block-header.md).
*   **Conditional Spending:** Set complex conditions for spending funds based on various parameters (e.g., oracle data, specific inputs).
*   **Atomic Swaps:** Facilitate trustless peer-to-peer exchange of different assets across blockchains or within Ergo.
*   **Crowdfunding:** Implement secure and transparent crowdfunding campaigns.
*   **Complex Financial Derivatives:** Build sophisticated financial instruments on the blockchain.

## Best Practices

1.  Keep contracts simple and readable.
2.  Use built-in [cryptographic primitives](crypto.md) where possible.
3.  Always consider [transaction validation](validation.md) overhead and potential costs.
4.  Test contracts thoroughly using playgrounds and SDK testing frameworks.
5.  Reason carefully about all possible execution paths and potential economic exploits.
6.  Leverage [data inputs](read-only-inputs.md) for accessing shared state efficiently.

## Common Pitfalls to Avoid

*   Overcomplicating contract logic unnecessarily.
*   Ignoring performance implications and transaction costs.
*   Neglecting comprehensive error handling and edge cases in off-chain code interacting with contracts.
*   Not fully understanding the nuances of the [eUTXO model](eutxo.md) (e.g., box lifecycle, state transitions).
*   Insecure handling of secrets or assumptions about context in off-chain components.

## Learning Paths & Next Steps

1.  **Beginner:**
    *   Understand the [Core Concepts](ergoscript-key-concepts.md).
    *   Experiment with the [P2S Playground](https://wallet.plutomonkey.com/p2s/).
    *   Study simple [example contracts](contracts.md).
2.  **Intermediate:**
    *   Learn about [Sigma Protocols](sigma.md).
    *   Explore [Multi-Stage Contract patterns](multi.md).
    *   Work through SDK tutorials ([AppKit](appkit.md), [Fleet](fleet.md), [SigmaRust](sigma-rust.md)).
3.  **Advanced:**
    *   Understand [ErgoTree Compilation & Serialization](ergotree.md).
    *   Explore advanced [cryptographic protocols](crypto.md).
    *   Contribute to open-source projects or build your own dApp.

Join community discussions on [Discord](https://discord.gg/ergo-platform-668903786361651200) (`#ergoscript`, `#sigma-rust`, `#appkit`, `#fleet`), [Telegram](https://t.me/ergo_dev), or the [Ergo Forum](https://www.ergoforum.org/) to ask questions and collaborate.

## Advanced Cryptography & Structures

ErgoScript's foundation on Sigma Protocols allows for powerful cryptographic primitives. However, some advanced structures have specific considerations:

*   **Merkle Trees:** While [Merkle Trees](../data-model/structures/merkle/merkle-tree.md) are fundamental to Ergo's data integrity (e.g., for transactions and extension data), direct verification of arbitrary Merkle proofs *within* an ErgoScript contract is not natively supported by a single built-in function. Verification typically happens off-chain or relies on specific protocol designs where roots are checked. The [MAST pattern](tx/mast-example.md) leverages Merkle trees conceptually, often using `executeFromVar` for on-chain execution of proven branches rather than full proof verification within the script. Developers interested in the general concept and off-chain usage should consult the main [Merkle Tree documentation](../data-model/structures/merkle/merkle-tree.md).

## Related Technical Resources
- [ErgoTree Documentation](ergotree.md)
- [Sigma Protocols Overview](sigma.md)
- [Schnorr Signatures](schnorr.md)
- [Light Verifying Nodes](nipopow_nodes.md)
- [eUTXO Model Explanation](eutxo.md)
- [Ergo Whitepaper](https://ergoplatform.org/en/whitepaper/)
- [ErgoScript Language Specification](lang-spec.md) (Detailed reference)
- [Advanced ErgoScript Tutorial](https://ergoplatform.org/docs/AdvancedErgoScriptTutorial.pdf)

## Comparative Analysis
ErgoScript stands out by:

- Enabling complex logic via the [eUTXO model](eutxo.md) without full on-chain Turing-completeness risks.
- Natively supporting advanced cryptographic protocols ([Sigma Protocols](sigma.md)).
- Allowing complex [financial contracts](contracts.md) with predictable [execution costs](min-fee.md).
- Maintaining a declarative, secure programming model based on [UTXOs](eutxo.md).

## Performance Considerations
- Off-chain [transaction creation](transactions.md) minimizes [on-chain computation](ergoscript.md).
- [On-chain validation](validation.md) focuses only on script conditions.
- Immutable [transaction graph](transactions.md) allows for optimizations.
- Native support for [light verifying nodes](light-spv-node.md) enhances accessibility.
- [Non-Turing complete](multi-stage-txs.md) base language prevents infinite loops and simplifies cost analysis.
- See the [Interpreter Performance Style Guide](https://github.com/ergoplatform/sigmastate-interpreter/blob/develop/docs/perf-style-guide.md) for tips on writing efficient scripts.
