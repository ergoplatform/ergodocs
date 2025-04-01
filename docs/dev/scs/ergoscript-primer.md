---
tags:
  - ErgoScript
  - Beginner Guide
---

# ErgoScript: A Beginner's Guide

## What is ErgoScript?

ErgoScript is a powerful, developer-friendly programming language designed specifically for writing [smart contracts](contracts.md) on the [Ergo blockchain](protocol-overview.md). Think of it as a specialized language that allows you to create complex [financial contracts](contracts.md) and applications with unprecedented flexibility and [security](security.md).

## Key Characteristics

### 1. UTXO-Based Model
Unlike [account-based blockchains](accountveutxo.md), ErgoScript uses the [UTXO (Unspent Transaction Output) model](eutxo.md). This means:

- Contracts define conditions for spending coins
- [Transactions](transactions.md) are immutable and more secure
- Improved [scalability](scaling.md) and parallel processing

### 2. Declarative Programming
ErgoScript is declarative, which means you specify **what** should happen, not **how** it happens. For example:

```scala
// A simple contract that allows spending only after a specific block height
if (HEIGHT > 100000) signerPubKey else fail()
```

This contract says: "Allow spending only if the current [blockchain height](block-header.md) is greater than 100,000, otherwise fail."

### 3. Sigma Protocols
ErgoScript leverages advanced cryptographic techniques called [Sigma Protocols](sigma.md), enabling:

- Complex signature schemes
- [Ring signatures](ring.md)
- [Threshold signatures](threshold.md)
- Advanced [privacy features](privacy-guide.md)

## Getting Started

### Basic Syntax
ErgoScript is a subset of Scala, so if you're familiar with functional programming, you'll feel right at home. Here's a simple example:

```scala
// A contract that requires two of three signatures to spend
val pubKey1 = ...
val pubKey2 = ...
val pubKey3 = ...

sigmaProp(pubKey1 && pubKey2 || pubKey1 && pubKey3 || pubKey2 && pubKey3)
```

### Development Tools
- [ErgoScript P2S Playground](https://wallet.plutomonkey.com/p2s/): Experiment and generate [Ergo addresses](address.md)
- [Ergo AppKit](appkit.md): Development framework for building Ergo applications

## Common Use Cases

1. **[Multi-Signature Wallets](threshold.md)**
   Create wallets requiring multiple parties to approve [transactions](transactions.md)

2. **Time-Locked Contracts**
   Define contracts that can only be executed after a specific time or [block height](block-header.md)

3. **Conditional Spending**
   Set complex conditions for spending funds based on various parameters

## Learning Paths

### Beginner
- [ErgoScript Overview](ergoscript.md)
- [UTXO Model Explained](eutxo.md)

### Intermediate
- [Sigma Protocols](sigma.md)
- [Advanced Contract Patterns](contracts.md)

### Advanced
- [ErgoTree Compilation](ergoscriptvergotree.md)
- [Cryptographic Protocols](crypto.md)

## Best Practices

1. Keep contracts simple and readable
2. Use built-in [cryptographic primitives](crypto.md)
3. Always consider [transaction validation](validation.md) overhead
4. Test contracts thoroughly in the playground

## Common Pitfalls to Avoid

- Overcomplicating contract logic
- Ignoring performance implications
- Neglecting error handling
- Not understanding [UTXO model](eutxo.md) nuances

## Community and Support

- [Ergo Developer Forum](https://www.ergoforum.org/)
- [Ergo GitHub Discussions](https://github.com/ergoplatform/ergo/discussions)
- [Ergo Developer Telegram](https://t.me/ergo_dev)

## Next Steps

1. Experiment with the P2S Playground
2. Study example contracts
3. Join community discussions
4. Start building your first dApp!

## Recommended Reading

- [Ergo Whitepaper](https://ergoplatform.org/en/whitepaper/)
- [ErgoScript Technical Documentation](ergoscript.md)
