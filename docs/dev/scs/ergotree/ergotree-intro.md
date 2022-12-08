# ErgoTree Introduction

This section describes a **typed abstract syntax** of the ErgoTree language, which is used to define logical propositions protecting [boxes](box.md) in the Ergo blockchain. 

Serialized ErgoTree expressions are written into *UTXO* boxes and then evaluated by the transaction verifier. 

> Most Ergo users do not use ErgoTree directly since they are developing contracts in a higher-level language, such as [ErgoScript](ergoscript.md), which is then compiled into ErgoTree.

The reference implementation of ErgoTree uses Scala; however, alternative implementations can use other languages. This documentation provides a language-neutral specification of ErgoTree for developers of alternative ErgoTree implementations.

The design space of programming languages is very broad, ranging from general-purpose languages like C, Java, and Python to specialized languages like SQL, HTML, CSS, etc. 

The language for writing contracts on the blockchain must have several properties to serve as a robust platform for contractual money.

1. First, **the language and the contract execution environment should be deterministic**. Once created and stored in the blockchain, a smart contract should always behave predictably and deterministically; it should only depend on well-defined data context and nothing else. 
      1. As long as the data context does not change, any execution of the contract should return the same value any time it is executed on any execution platform using any compliant language implementation. No general-purpose programming language is deterministic because they provide non-deterministic operations, and ErgoTree does not have non-deterministic operations.
2. Second, **the language should facilitate spam-resistance**, i.e. defending against attacks when malicious contracts can overload the network nodes and bring the blockchain down ([Ler17](https://bitslog.wordpress.com/2017/01/08/a-bitcoin-transaction-that-takes-5-hours-to-verify/)). 
      1. To fulfil this goal transaction model of ErgoTree supports predictable cost estimation and the fast calculation of contract execution costs to ensure the evaluation cost of the given transaction is always
within acceptable bounds. In a general (Turing-complete) case, such cost prediction is not possible and requires special mechanisms such as Gas ([Woo14](http://gavwood.com/Paper.pdf)). Gas limits on transactions indeed protect the network from spam attacks. Still, at the expense of the users, who need to be careful to specify the gas limit large enough for the transaction to complete; otherwise, the gas used for the failed transaction will be kept by the miners for their work, and the user will not get it back.
1. Third, **the contract's language should be simple yet expressive enough** to implement a wide range of practical applications efficiently. 
      1. For example, ErgoTree is not turing-complete, but it is co-designed with the capabilities of the Ergo blockchain platform itself, making the whole system Turing-complete as demonstrated in ([CKM18](https://arxiv.org/abs/1806.10116)). The simplicity of the language enables spam resistance.
2. Forth, **simplicity and expressivity are often the characteristics of domain-specific languages** ([Fow10](https://books.google.de/books?hl=en&lr=&id=ri1muolw_YwC&oi=fnd&pg=PT29&dq=Martin+Fowler.+Domain-Specific+Languages.+01+2010.&ots=7Y9bdX4mdj&sig=UGF-xHd6q5xpdnxjEuVshpuPiNo&redir_esc=y#v=onepage&q=Martin%20Fowler.%20Domain-Specific%20Languages.%2001%202010.&f=false), [Hud96](https://dl.acm.org/doi/10.1145/242224.242477)). 
      1. From this perspective, ErgoTree is an intermediate representation of a DSL for writing smart contracts. The language directly captures the [*ubiquitous language*](https://www.martinfowler.com/bliki/UbiquitousLanguage.html) of the Ergo blockchain directly manipulating with Boxes, Tokens, Zero-Knowledge Sigma-Propostions etc.

These are the novel first-class features of Ergo platform, which it provides for user applications.

- It has a complementary frontend language called [ErgoScript](ergoscript.md), whose syntax is inspired by Scala/Kotlin and shares a common subset with Java and C#; thus, if you are proficient in any of these languages, you will be right at home using ErgoScript as well.
- ErgoScript aims to address the large audience of programmers with minimum surprise and [WTF](https://www.itworld.com/article/2833252/the-most-wtf-y-programming-languages.html) ratio.
- And last but not least, ErgoTree, as a core language of Ergo platform, should be optimized for compact storage and fast execution.

