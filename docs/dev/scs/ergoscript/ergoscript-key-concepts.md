# Core Concepts of ErgoScript

- Ergo is a blockchain based on the UTXO (Unspent Transaction Output) model and uses a Proof-of-Work consensus mechanism.
- Ergo incorporates an *extended-UTXO model* which allows the execution of complex financial contracts similar to those facilitated by Ethereum's account-based model.
- Given Ergo's UTXO orientation, ErgoScript incorporates numerous UTXO-specific constructs such as `Box`, `INPUTS`, and `OUTPUTS`. You can find a comprehensive list [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md).
- A [Box](box.md), effectively a UTXO, can hold up to ten [registers](registers.md) used for data storage. Similar to Bitcoin, a transaction in Ergo consumes one or more existing boxes (represented by the `INPUTS` array) and generates one or more new boxes (represented by the `OUTPUTS` array).
- The syntax of ErgoScript is a subset of Scala's. However, you don't need to be proficient in Scala to learn ErgoScript. The overlap of Scala used in writing ErgoScript is minimal, with simple elements like `val`.
- Unlike in Java or Python, arrays in Scala and ErgoScript are accessed using round parentheses. Therefore, `OUTPUTS(0)` refers to the first element of the `OUTPUTS` array.
- Contrasting with Scala, ErgoScript doesn't support the `var` keyword; every element is immutable.
- ErgoScript is not Turing complete, but you can construct Turing complete applications as illustrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).

## Key Principles

1. Ergo's UTXO orientation is reflected in many UTXO-specific constructs within ErgoScript, such as `Box`, `INPUTS`, `OUTPUTS`, and more. A complete catalog is available [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md). A [Box](box.md) is essentially a UTXO containing up to ten [registers](registers.md) for data storage. Like Bitcoin, a transaction spends one or more existing boxes (represented with the `INPUTS` array) and creates one or more new boxes (depicted using the `OUTPUTS` array).

2. ErgoScript's syntax is a Scala subset, but knowledge of Scala isn't mandatory for learning ErgoScript. The portion of Scala required to write ErgoScript is minuscule. However, having some Scala experience could aid in understanding ErgoScript. Moreover, Scala is a [valuable language to include in your resume](https://insights.dice.com/2020/06/04/24-programming-languages-pay-top-salaries-scala/).

3. Like Scala, ErgoScript supports functional programming, simplifying interactions with collections using concepts such as `foreach`, `exists`, `fold`, etc.

4. An ErgoScript program, similar to ErgoTree, comprises a sequence of boolean predicates connected using `&&` and `||`.

5. ErgoScript offers cryptographic operations via `BigInt` and `GroupElement` (Elliptic curve point) types along with associated operations such as addition, multiplication, and exponentiation. Note that `BigInt` operations in ErgoScript are performed modulo `2^256`, unlike Scala, and thus overflow must be carefully managed.