# ErgoTree Introduction

This section describes the **typed abstract syntax** of the ErgoTree language, which is used to define logical propositions protecting [boxes](box.md) in the Ergo blockchain. 

Serialized ErgoTree expressions are written into *UTXO* boxes and then evaluated by the transaction verifier. 

> Most Ergo users do not use ErgoTree directly, as they typically develop contracts in a higher-level language, such as [ErgoScript](ergoscript.md), which is then compiled into ErgoTree.

The reference implementation of ErgoTree uses Scala; however, alternative implementations can be written in other languages. This documentation provides a language-neutral specification of ErgoTree for developers creating alternative ErgoTree implementations.

The design space of programming languages is very broad, ranging from general-purpose languages like C, Java, and Python to specialized languages like SQL, HTML, CSS, etc. 

The language for writing contracts on the blockchain must have several properties to serve as a robust platform for contractual money:

1. First, **the language and the contract execution environment must be deterministic**. Once created and stored in the blockchain, a smart contract should always behave predictably and deterministically; it should depend only on a well-defined data context. 
      1. As long as the data context does not change, any execution of the contract should return the same value every time it is executed on any compliant execution platform or language implementation. General-purpose programming languages are typically not deterministic because they provide non-deterministic operations; ErgoTree avoids these.
2. Second, **the language should facilitate spam-resistance**, i.e., defending against attacks where malicious contracts could overload network nodes and bring down the blockchain ([Ler17](https://bitslog.wordpress.com/2017/01/08/a-bitcoin-transaction-that-takes-5-hours-to-verify/)). 
      1. To fulfill this goal, the ErgoTree transaction model supports predictable cost estimation and the fast calculation of contract execution costs, ensuring the evaluation cost of any given transaction remains within acceptable bounds. In a general (Turing-complete) case, such cost prediction is not possible and requires special mechanisms such as Gas ([Woo14](http://gavwood.com/Paper.pdf)). Gas limits on transactions indeed protect the network from spam attacks, but at the expense of users, who need to be careful to specify a gas limit large enough for the transaction to complete; otherwise, the gas used for the failed transaction will be kept by the miners for their work, and the user will not get it back.
1. Third, **the contract's language should be simple yet expressive enough** to implement a wide range of practical applications efficiently. 
      1. For example, ErgoTree is not Turing-complete, but it is co-designed with the capabilities of the Ergo blockchain platform itself, making the whole system Turing-complete as demonstrated in ([CKM18](https://arxiv.org/abs/1806.10116)). The simplicity of the language enables spam resistance.
2. Fourth, **simplicity and expressivity are often characteristics of domain-specific languages** ([Fow10](https://books.google.de/books?hl=en&lr=&id=ri1muolw_YwC&oi=fnd&pg=PT29&dq=Martin+Fowler.+Domain-Specific+Languages.+01+2010.&ots=7Y9bdX4mdj&sig=UGF-xHd6q5xpdnxjEuVshpuPiNo&redir_esc=y#v=onepage&q=Martin%20Fowler.%20Domain-Specific%20Languages.%2001%202010.&f=false), [Hud96](https://dl.acm.org/doi/10.1145/242224.242477)). 
      1. From this perspective, ErgoTree is an intermediate representation of a DSL for writing smart contracts. The language directly captures the [*ubiquitous language*](https://www.martinfowler.com/bliki/UbiquitousLanguage.html) of the Ergo blockchain, directly manipulating Boxes, Tokens, Zero-Knowledge Sigma-Propositions, etc.

These are the novel first-class features of the Ergo platform, which it provides for user applications.

- It has a complementary frontend language called [ErgoScript](ergoscript.md), whose syntax is inspired by Scala/Kotlin and shares a common subset with Java and C#; thus, if you are proficient in any of these languages, you will likely feel comfortable using ErgoScript as well.
- ErgoScript aims to address a large audience of programmers with minimum surprise and a low [WTF](https://www.itworld.com/article/2833252/the-most-wtf-y-programming-languages.html) ratio.
- Last but not least, ErgoTree, as a core language of the Ergo platform, should be optimized for compact storage and fast execution.
