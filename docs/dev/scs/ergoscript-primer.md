---
tags:
  - ErgoScript
  - Beginner Guide
---

# ErgoScript: A Beginner's Guide

## What is ErgoScript?

ErgoScript is a powerful, developer-friendly programming language designed specifically for writing smart contracts on the Ergo blockchain. Think of it as a specialized language that allows you to create complex financial contracts and applications with unprecedented flexibility and security.

## Key Characteristics

### 1. UTXO-Based Model
Unlike account-based blockchains, ErgoScript uses the UTXO (Unspent Transaction Output) model. This means:

- Contracts define conditions for spending coins
- Transactions are immutable and more secure
- Improved scalability and parallel processing

### 2. Declarative Programming
ErgoScript is declarative, which means you specify **what** should happen, not **how** it happens. For example:

```scala
// A simple contract that allows spending only after a specific block height
if (HEIGHT > 100000) signerPubKey else fail()
```

This contract says: "Allow spending only if the current blockchain height is greater than 100,000, otherwise fail."

### 3. Sigma Protocols
ErgoScript leverages advanced cryptographic techniques called Sigma Protocols, enabling:

- Complex signature schemes
- Ring signatures
- Threshold signatures
- Advanced privacy features

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
- [ErgoScript P2S Playground](https://wallet.plutomonkey.com/p2s/): Experiment and generate Ergo addresses
- [Ergo AppKit](https://github.com/ergoplatform/ergo-appkit): Development framework for building Ergo applications

## Common Use Cases

1. **Multi-Signature Wallets**
   Create wallets requiring multiple parties to approve transactions

2. **Time-Locked Contracts**
   Define contracts that can only be executed after a specific time or block height

3. **Conditional Spending**
   Set complex conditions for spending funds based on various parameters

## Learning Paths

### Beginner
- [ErgoScript Overview](/dev/scs/ergoscript.md)
- [UTXO Model Explained](/dev/protocol/eutxo)

### Intermediate
- [Sigma Protocols](/dev/scs/sigma.md)
- [Advanced Contract Patterns](/dev/scs/contracts.md)

### Advanced
- [ErgoTree Compilation](/dev/scs/ergoscriptvergotree.md)
- [Cryptographic Protocols](/dev/crypto/)

## Best Practices

1. Keep contracts simple and readable
2. Use built-in cryptographic primitives
3. Always consider transaction validation overhead
4. Test contracts thoroughly in the playground

## Common Pitfalls to Avoid

- Overcomplicating contract logic
- Ignoring performance implications
- Neglecting error handling
- Not understanding UTXO model nuances

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
- [ErgoScript Technical Documentation](/dev/scs/)
