# ErgoScript Key Concepts

- Ergo is a UTXO-based blockchain with Proof-of-Work consensus
- Ergo uses an *extended-UTXO model*, supporting advanced financial contracts comparable to those in Ethereum's account-based model. 
- Since Ergo is UTXO-based, ErgoScript has many UTXO-specific constructs such as: `Box`, `INPUTS`, and `OUTPUTS`. A complete list is available [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md)
- A [Box](box.md) is essentially a UTXO and consists of up to ten registers for storing data. Similar to Bitcoin, a transaction spends one or more existing boxes (denoted using the `INPUTS` array) and creates one or more new boxes (denoted using the `OUTPUTS` array)
- ErgoScript's syntax is a subset of Scala's. However, knowledge of Scala is not necessary to learn ErgoScript because the amount of Scala needed to write ErgoScript is small, e.g. `val`
- Note that arrays in Scala are accessed using round parentheses, not square brackets like in Java or Python. Thus, `OUTPUTS(0)` refers to the first element of the `OUTPUTS` array
- Unlike Scala, ErgoScript does not support the `var` keyword, and thus everything is immutable
- The scripting language is non-Turing complete, but applications can be made to be Turing complete, as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).


## Key Concepts

1. Since Ergo is UTXO based, ErgoScript has many UTXO-specific constructs such as `Box`, `INPUTS`, `OUTPUTS`, etc. 
A complete list is available [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md). A [Box](box.md) is essentially a UTXO and consists of up to ten [registers](registers.md) for storing data. Similar to Bitcoin, a transaction spends one or more existing boxes (denoted using the `INPUTS` array) and creates one or more new boxes (denoted using the `OUTPUTS` array).  

2. ErgoScript's syntax is a subset of Scala's. However, knowledge of Scala is not necessary to learn ErgoScript because the amount of Scala needed to write ErgoScript is tiny. That being said, some prior experience in Scala will be useful in picking up ErgoScript and Scala is a [good language to have on your resume](https://insights.dice.com/2020/06/04/24-programming-languages-pay-top-salaries-scala/) anyway.  

3. Like Scala, ErgoScript supports functional programming, which makes it easier to deal with collections using metaphors such as `foreach`, `exists`, `fold`, etc.  

4. Like ErgoTree, an ErgoScript program consists of a sequence of boolean predicates joined using `&&` and `||`. 

5. ErgoScript provides cryptographic operations via `BigInt` and `GroupElement` (Elliptic curve point) types along with relevant operations such as addition, multiplication and exponentiation. Note that, unlike Scala, `BigInt` operations in ErgoScript are performed modulo `2^256`, and thus, care must be taken about overflow. 