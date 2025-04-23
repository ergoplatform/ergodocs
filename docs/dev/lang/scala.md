---
tags:
  - Scala
  - Development
  - Ergo
---

# Scala Development with Ergo

Ergo's primary language is Scala. Similarly, the scripting language used by Ergo, [*ErgoScript*](ergoscript.md), is also based on Scala.

If you're new to Scala development with Ergo, the [Ergo Scala Skeleton App](https://github.com/dav009/ergo-scala-skeleton-app) is a great place to start.

## Why Scala? 

### Why Scala?

Ergo's primary language is Scala. Similarly, the scripting language used by Ergo, [ErgoScript](ergoscript.md), is also based on Scala, but the [off-chain code](off-chain-overview.md) can be written in any language. Developers have access to a growing selection of [tools](get-started.md) and [Software Development Kits (SDKs)](frameworks.md) for [JVM](jvm.md), [Rust](rust.md) and [JS/TS](js.md).


Scala has several features that set it apart from other [JVM](jvm.md) languages.

- Firstly, it is truly cross-platform, as the same code can run on [JVM](jvm.md) and [JavaScript](js.md) natively. This is a feature that is not found in many other languages.
- Additionally, key ecosystem libraries for Scala support all platforms, and the popularity of Scala.js and Scala-native is increasing.
- Another advantage of Scala is its conciseness, both in terms of [syntax](syntax.md) and conceptual level.
- Despite its high-level nature, Scala can also be more efficient than similar [Java](java.md) code due to its ability to use primitive unboxed types, and the ability of the Scala compiler to perform code specialization.
- Furthermore, Scala is multi-paradigm, allowing for the combination of OOP, FP, and LP, making it suitable for a wide range of domains.
- Lastly, Scala 3 brings even more powerful features such as metaprogramming and tools for zero-cost abstractions.

### Scala Versioning (Scala 3)

Ergo's core components, including the [reference node](install.md) and [`sigmastate-interpreter`](sigmastate-interpreter.md), have undergone migration to **Scala 3**. This migration leverages the newer language features, improved type system, and tooling enhancements offered by Scala 3.

*   **Rationale & Implications:** For a detailed understanding of the motivations behind the Scala 3 migration and its potential impact on the ecosystem (including Long-Term Support plans), refer to the official Scala blog post: [Next Steps for Scala 3 and Scala 2 Long-Term Support](https://www.scala-lang.org/blog/next-scala-lts.html).
*   **Developer Impact:** Developers contributing to or building upon these core libraries need to ensure their development environment and build tools (like SBT) are compatible with Scala 3. While Scala 3 offers significant improvements, developers should be aware of potential syntax changes or library compatibility adjustments compared to Scala 2.

## Learning Resources

Here are some tutorials, guides, and explanations to help you get started with Scala development on Ergo:

- [ErgoScript](ergoscript.md): Learn about ErgoScript, Ergo's scripting language.
- [AppKit](appkit.md): Discover how to use Ergo's AppKit to develop [applications](use-cases-overview.md).
- [Ergo Tutorials by Zackbalbin](https://github.com/zackbalbin/ErgoTutorials): A collection of tutorials for Ergo development.
- [Learning Ergo 101: Development Workflow](https://blog.cryptostars.is/learning-ergo-101-development-workflow-aa17dd63ef6): A guide to the [development workflow](get-started.md) for Ergo.

## Development Resources

Here are some resources that can assist you in your Scala development journey with Ergo:

- [sigmastate-interpreter](sigmastate-interpreter.md): This is an [ErgoScript compiler](compiler.md) and [ErgoTree Interpreter](ergotree.md) implementation for Ergo blockchain's [*Sigma Language*](sigma-lang.md). For the development of Ergo applications using [JVM](jvm.md) languages, consider using [Appkit](appkit.md).
- [ScoreX](https://github.com/scorexfoundation/scorex): An open-source, modular blockchain & cryptocurrency framework.
- [Scrypto](scrypto.md): An open-source cryptographic toolkit designed to make it easier and safer for developers to use [cryptography](crypto.md) in their applications. It's based on Scorex and used internally in [Ergo Node](install.md) and [ergo-wallet](wallet.md).
- [Ergo Scala Style Guide](https://github.com/ergoplatform/ergo-scala-style-guide): Follow this guide to maintain consistency and readability in your Scala code.

> Note: The public interfaces of these libraries are subject to change.
