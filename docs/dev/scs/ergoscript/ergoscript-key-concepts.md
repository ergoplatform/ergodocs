# Core Concepts of ErgoScript

- Ergo is a blockchain platform that operates on the UTXO (Unspent Transaction Output) model and employs a Proof-of-Work consensus mechanism.
- Ergo introduces an *extended-UTXO model* that enables the execution of intricate financial contracts, akin to those supported by Ethereum's account-based model.
- ErgoScript, being aligned with Ergo's UTXO model, incorporates numerous UTXO-specific constructs such as `Box`, `INPUTS`, and `OUTPUTS`. A comprehensive list of these constructs can be found [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md).
- A [Box](box.md), essentially a UTXO, can accommodate up to ten [registers](registers.md) for data storage. Analogous to Bitcoin, an Ergo transaction consumes one or more existing boxes (represented by the `INPUTS` array) and produces one or more new boxes (represented by the `OUTPUTS` array).
- ErgoScript's syntax is a subset of Scala's. However, proficiency in Scala is not a prerequisite for learning ErgoScript. The Scala elements used in ErgoScript are minimal and straightforward, such as `val`.
- Unlike Java or Python, both Scala and ErgoScript access arrays using round parentheses. Hence, `OUTPUTS(0)` denotes the first element of the `OUTPUTS` array.
- In contrast to Scala, ErgoScript does not support the `var` keyword; all elements are immutable.
- ErgoScript is not Turing complete, but it is possible to build Turing complete applications, as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).

## Key Principles

1. Ergo's UTXO model is reflected in ErgoScript through various UTXO-specific constructs such as `Box`, `INPUTS`, `OUTPUTS`, and more. A detailed list is available [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md). A [Box](box.md) is essentially a UTXO that can hold up to ten [registers](registers.md) for data storage. Similar to Bitcoin, a transaction in Ergo consumes one or more existing boxes (represented by the `INPUTS` array) and generates one or more new boxes (represented by the `OUTPUTS` array).

2. While ErgoScript's syntax is a subset of Scala, familiarity with Scala is not a requirement for learning ErgoScript. The Scala elements necessary for writing ErgoScript are minimal. However, some experience with Scala could be beneficial in understanding ErgoScript. Additionally, Scala is a [valuable language to include in your resume](https://insights.dice.com/2020/06/04/24-programming-languages-pay-top-salaries-scala/).

3. ErgoScript, like Scala, supports functional programming, which simplifies interactions with collections using concepts such as `foreach`, `exists`, `fold`, etc.

4. An ErgoScript program, akin to ErgoTree, consists of a sequence of boolean predicates connected using `&&` and `||`.

5. ErgoScript provides cryptographic operations via `BigInt` and `GroupElement` (Elliptic curve point) types, along with associated operations like addition, multiplication, and exponentiation. It's important to note that `BigInt` operations in ErgoScript are performed modulo `2^256`, unlike Scala, hence overflow needs to be carefully managed.
