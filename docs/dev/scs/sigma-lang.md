---
tags:
  - Sigma Language
---

# The ***'Sigma Language'***

The [sigmastate-interpreter](https://github.com/ScorexFoundation/sigmastate-interpreter#sigma-language-background.md) repository contains implementations of ErgoScript compiler and ErgoTree Interpreter for a family of Sigma-protocol based authentication languages (or simply ***Sigma language***).

## Sigma Language Background

Every coin in Bitcoin is protected by a program in the stack-based Script language. An interpreter for the language evaluates the program against a context (a few variables containing information about a spending transaction and the blockchain), producing a single boolean value. While Bitcoin Script allows some contracts to be programmed, its abilities are limited. Also, a hard fork would be required to add new cryptographic primitives, such as ring signatures.

Generalizing the Bitcoin Script, ErgoScript compiler and ErgoTree interpreter implement an **authentication language** which allows developers to specify coin spending conditions. The [ErgoScript Compiler](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sc/src/main/scala/sigmastate/lang/SigmaCompiler.scala#L48) compiles the source code into [ErgoTree](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/sigmastate/Values.scala#L990) byte code, which can be saved in UTXO coins to protect their spending (same as in Bitcoin).

ErgoTree, in turn, is a bytecode language and memory representation that can be deterministically interpreted in the given _blockchain context_.

/// admonition | Please note
ErgoTree defines guarding proposition for a coin as a logic formula which combines predicates over a context and cryptographic statements provable via [Σ-protocols](sigma.md) with AND, OR, k-out-of-n connectives.
///
