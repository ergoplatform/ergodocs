---
tags:
  - ErgoScript
---

# ErgoTree: The Core of Ergo's Infrastructure

ErgoTree is a fundamental part of Ergo's infrastructure, serving as the backbone of its contract development process. However, most users interact with ErgoTree indirectly. They typically develop contracts using a higher-level language, such as ErgoScript, which is then compiled into ErgoTree.

**Key Concepts**

- [ErgoTree](https://ergoplatform.org/docs/ErgoTree.pdf) is a tool used to define logical propositions that safeguard boxes (an abstraction of coins) in Ergo.
- Serialized ErgoTree expressions are inscribed into UTXO boxes and subsequently evaluated by the transaction verifier.
- While the reference implementation of ErgoTree is in Scala, alternative implementations can utilize other languages.
- The propositions are stored in the blockchain following the ErgoTree serialization format, which is optimized for compact storage, swift script execution, and efficient transaction validation.
- However, the ErgoTree binary format intentionally excludes metadata, which might be necessary for various Ergo applications.

## Rationale

**Efficient Script Validation**

Consider a transaction that has an `INPUTS` collection of boxes to spend. Each input box can have a script (referred to as the `propositionBytes` property) that protects it. This script needs to be executed within the context of the current transaction. For a simple transaction with a single input box, we need to validate 1000 scripts per second at a minimum to maintain a steady block validation of `1000` transactions per second.

Additionally, to increase the probability of successful mining, the block validation time should be minimized, allowing a miner to start solving the PoW puzzle as soon as possible. For every script (of an input box), the following steps are performed to validate it:

1. A Context object is created with `SELF = box`.
2. ErgoTree is traversed to build a cost graph for cost estimation.
3. The cost estimation is computed by evaluating the cost graph with the current context.
4. If the cost is within the limit, the ErgoTree is evaluated using the context to obtain a sigma proposition (see `SigmaProp`).
5. The sigma protocol verification procedure is executed.

## Potential Script Processing Optimization

Before an ErgoScript contract can be stored in a blockchain, it must be compiled from its source code into ErgoTree and then serialized into a byte array. Due to ErgoTree's purely functional graph-based IR, the compiler can perform various optimizations to reduce the size of the tree. This results in normalization/unification, where different original scripts may compile into identical ErgoTrees and, consequently, identical serialized bytes. In many cases, two boxes will have the same ErgoTree, with only the substitution of constants. For example, all pay-to-public-key scripts have the same ErgoTree template, with only the public key (a constant of GroupElement type) replaced.

Due to normalization and script template reusability, the number of different script templates is much less than the number of actual ErgoTrees in the UTXO boxes. For example, we may have 1000s of different script templates in a blockchain with millions of UTXO boxes.

The average reusability ratio is 1000 in this case. And even those 1000 different scripts may have different usage frequencies. Having a high reusability ratio, we can optimize script evaluation by performing step 2 from section D.2.1 only once per unique script.

The compiled cost graph can be cached in Map[Array[Byte], Context => Int]. Every ErgoTree template extracted from an input box can be used as the key in this map to obtain the

graph which is ready to execute.

However, there is an obstacle to the optimization by caching, i.e., the constants embedded in contracts. In many cases, it is natural to embed constants in the ErgoTree body, with the most notable scenario being when public keys are embedded. As a result, two functionally identical scripts are serialized to different byte arrays because they have different embedded constants.

### Templatized ErgoTree

A solution to the problem with embedded constants is simple; we don’t need to embed constants. Each constant in the body of ErgoTree can be replaced with an indexed placeholder node (see 63 ConstantPlaceholder). Each placeholder has an index of the constant in the constants collection of ErgoTree. The transformation is part of the compilation and is performed ahead of time. Each ErgoTree has an array of all the constants extracted from its body. Each placeholder refers to the constant by the constant’s index in the array. The index of the placeholder can be assigned by breadth-first topological order of the graph traversal during the compilation of ErgoScript into ErgoTree. Whatever method is used, a placeholder should always refer to an existing constant.

Thus the format of serialized ErgoTree contains:

1. The bytes of a collection with segregated constants.
2. The bytes of script expression with placeholders.

The collection of constants contains the serialized constant data (using ConstantSerializer) one after another. The script expression is a serialized Value with placeholders. Using such script format, we can use the script expression bytes as a key in the cache. The observation is that after the constants are segregated, what remains is the template. Thus, instead of applying steps 1-2 from section D.2.1 to constant-full scripts, we can apply them to constant-less templates. Before applying steps 3 - 5, we need to bind placeholders with actual values taken from the constants collection and then evaluate both the cost graph and ErgoTree.

[EIP5 is based on this ErgoTree feature](https://github.com/ergoplatform/eips/blob/master/eip-0005.md)

## Resources

- There is an ErgoTree serialization section [available](https://ergoplatform.org/docs/ErgoTree.pdf).
- [Constant-less lambdas](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/264).
- [ErgoTree as an Authentication Language](https://www.ergoforum.org/t/ergotree-as-an-authentication-language/).
- [Human representation for ergo tree #812](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/812).

### [ergotree-pseudo-code](https://github.com/ross-weir/ergo-script-re/tree/main/ergotree-pseudo-code)

This is a pseudo code generator for compiled ergo trees. It attempts to create pseudo code that roughly represents the ergo script that produced the tree. In some cases, it can produce a script that is equivalent (pseudo code compiles to the same ergo tree), but this is on a best effort basis.