# ErgoTree: Reference Manual

ErgoTree forms the backbone of Ergo's contract development process, playing a vital role in the infrastructure. It is the typed abstract syntax of the ErgoTree language used for defining logical propositions that protect boxes (coin abstractions) in Ergo. While ErgoTree is fundamental, most users interact with it indirectly, primarily developing contracts using a higher-level language called [ErgoScript](ergoscript.md), which later compiles into ErgoTree. 

## Understanding ErgoTree

ErgoTree is not only an integral part of Ergo's infrastructure but also serves as a domain-specific language. It encapsulates the [*ubiquitous language*](https://www.martinfowler.com/bliki/UbiquitousLanguage.html) of the Ergo blockchain, directly interacting with Boxes, Tokens, Zero-Knowledge Sigma-Propositions, among others. ErgoTree optimizes for compact storage and speedy execution, marking its prominence in the Ergo platform.

The language designed for writing blockchain contracts must be deterministic, fostering spam-resistance. It should also be simple yet expressive enough to act as a robust platform for contractual money. ErgoTree fulfills these criteria, emerging as a critical tool for creating, protecting, and managing boxes in the Ergo blockchain.

Supplementing ErgoTree is a frontend language named [ErgoScript](ergoscript.md). Inspired by Scala/Kotlin, ErgoScript shares common subsets with Java and C#, making it accessible for programmers familiar with these languages. ErgoScript aims to engage a large audience of programmers with minimal surprises.

## Key ErgoTree Concepts

- ErgoTree is written into UTXO boxes and is subsequently evaluated by the transaction verifier.
- The propositions are stored in the blockchain in the ErgoTree serialization format. This format optimizes for compact storage, swift script execution, and efficient transaction validation.
- The reference implementation of ErgoTree is in Scala, but alternative implementations can utilize other languages.
- ErgoTree's binary format intentionally omits metadata, which might be necessary for various Ergo applications.



## Additional Resources

- ErgoTree serialization section [available here](https://ergoplatform.org/docs/ErgoTree.pdf).
- [Constant-less lambdas](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/264).
- [ErgoTree as an Authentication Language](https://www.ergoforum.org/t/ergotree-as-an-authentication-language/).
- [Human representation for ergo tree #812](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/812).
- [ErgoTree pseudo-code](https://github.com/ross-weir/ergo-script-re/tree/main/ergotree-pseudo-code): Generates pseudo code for compiled ergo trees on a best effort basis.
