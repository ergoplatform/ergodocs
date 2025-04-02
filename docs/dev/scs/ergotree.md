---
tags:
  - ErgoTree
  - Reference Manual
---

# ErgoTree: Reference Manual

ErgoTree forms the backbone of Ergo's [smart contracts](contracts.md). It is the typed abstract syntax of the ErgoTree language used for defining logical propositions that protect [boxes](box.md) (coin abstractions) in Ergo. While ErgoTree is fundamental, most users interact with it indirectly, primarily developing contracts using a higher-level language called [ErgoScript](ergoscript.md), which later compiles into ErgoTree. 

## Understanding ErgoTree

ErgoTree serves as a specialized language, encapsulating the [*universal language*](https://www.martinfowler.com/bliki/UbiquitousLanguage.html) of the [Ergo blockchain](protocol-overview.md). It directly interacts with key components such as [Boxes](box.md), [Tokens](eip4.md), and [Zero-Knowledge Sigma-Propositions](sigma.md). ErgoTree is optimized for efficient storage and rapid execution.

A language intended for writing [blockchain contracts](contracts.md) must be deterministic to ensure spam-resistance. It also needs to be simple yet expressive enough to function as a solid platform for [contractual money](on-contractual-money.md). ErgoTree meets these requirements, making it an essential tool for creating, securing, and managing boxes on the [Ergo blockchain](protocol-overview.md).

Complementing ErgoTree is a frontend language named [ErgoScript](ergoscript.md). Drawing inspiration from Scala/Kotlin, ErgoScript shares common subsets with Java and C#, making it user-friendly for programmers acquainted with these languages. ErgoScript is designed to attract a broad spectrum of programmers with its intuitive approach.

## Structure, Authentication, and Application

ErgoTree, distinct from low-level languages like stack-based EVM assembly, is structured as a *typed abstract syntax tree*. In this regard, ErgoTree is a kind of authentication language aka *"smart signature"* used to validate transactions or actions by verifying specific conditions.

ErgoTree achieves this by combining:

- **Secret Data Predicates**: Conditions verifying confidential information such as [digital signatures](signing.md) or [secret keys](wallets.md).
- **[Blockchain Context](blockchain-context.md) Predicates**: Conditions dependent on the [transaction's specific context](blockchain-context.md) within the [blockchain](protocol-overview.md).

By evaluating these predicates, ErgoTree authenticates [transactions](transactions.md), ensuring their legitimacy and adherence to set rules. Its ability to validate and secure transactions while adapting to the transaction context makes ErgoTree a versatile tool, extending its applicability to various digital platforms, including other [cryptocurrencies](protocol-overview.md) and [Central Bank Digital Currencies (CBDCs)](cbdc.md), or even non-monetary digital objects where smart access could be needed. Off-chain applications often need to perform similar validations; see [Fleet SDK Recipes](fleet-sdk-recipes.md) for examples using JavaScript/TypeScript.

- Additional parties can be authorized
- Parties can delegate authorization
- AND/OR expressions
- Conditions can extend beyond signer identity.

## Key ErgoTree Concepts

- ErgoTree is written into [UTXO boxes](box.md) and is subsequently evaluated by the [transaction verifier](validation.md).
- The propositions are stored in the [blockchain](protocol-overview.md) in the [ErgoTree serialization format](https://ergoplatform.org/docs/ErgoTree.pdf). This format optimizes for compact storage, swift [script execution](sigmastate-interpreter.md), and efficient [transaction validation](validation.md).
- The reference implementation of ErgoTree is in Scala, but alternative implementations can utilize other languages.
- ErgoTree's binary format intentionally omits metadata, which might be necessary for various Ergo applications.


## Additional Resources

- ErgoTree serialization section [available here](https://ergoplatform.org/docs/ErgoTree.pdf).
- [Constant-less lambdas](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/264).
- [ErgoTree as an Authentication Language](https://www.ergoforum.org/t/ergotree-as-an-authentication-language/).
- [Human representation for ergo tree #812](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/812).
- [ErgoTree pseudo-code](https://github.com/ross-weir/ergo-script-re/tree/main/ergotree-pseudo-code): Generates pseudo code for compiled ErgoTrees on a best effort basis.
