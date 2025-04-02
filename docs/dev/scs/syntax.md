---
tags:
  - Syntax
  - ErgoScript
---
# ErgoScript Syntax

ErgoScript is a strongly typed language designed specifically for the Ergo blockchain, enabling the creation of secure and efficient smart contracts. This guide provides an introduction to ErgoScript's syntax, its integration with Ergo's UTXO model, and essential concepts that will help you write robust contracts on the Ergo platform.

## Introduction to ErgoScript

ErgoScript, inspired by Scala, is the scripting language used to create smart contracts on the Ergo blockchain. It is designed to be both powerful and intuitive, allowing for the creation of complex financial contracts while maintaining readability and security. Understanding the syntax and structure of ErgoScript is crucial for developing contracts that are not only functional but also secure.

### ErgoScript and the UTXO Model

Ergo operates on the UTXO (Unspent Transaction Output) model and employs a Proof-of-Work consensus mechanism. However, Ergo enhances the traditional UTXO model with its *extended-UTXO model*, which supports the execution of intricate financial contracts, similar to those possible on Ethereum's account-based model.

Key concepts of ErgoScript related to the UTXO model include:

- **Box**: A `Box` is essentially a UTXO in Ergo and can store data across up to ten registers. Like Bitcoin, Ergo transactions consume one or more existing boxes (represented by the `INPUTS` array) and produce one or more new boxes (represented by the `OUTPUTS` array).
- **UTXO-Specific Constructs**: ErgoScript incorporates constructs like `Box`, `INPUTS`, and `OUTPUTS` that are specific to the UTXO model. The [LangSpec.md](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md) document provides a comprehensive list of these constructs.
- **Turing Completeness**: Although ErgoScript itself is not Turing complete, you can still build Turing-complete applications, as detailed in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).

### ErgoScript Syntax Overview

ErgoScript’s syntax is derived from Scala, but you don’t need to be a Scala expert to write ErgoScript. The language uses a minimal subset of Scala’s features, focusing on simplicity and functionality:

- **Immutable Values**: In ErgoScript, you define values using `val`, ensuring immutability (similar to constants in other languages). Unlike Scala, ErgoScript does not support the `var` keyword, meaning all defined values are immutable.
- **Array Access**: Both Scala and ErgoScript use round parentheses for array access. For example, `OUTPUTS(0)` refers to the first element of the `OUTPUTS` array.
- **Functional Programming**: ErgoScript supports functional programming constructs such as `foreach`, `exists`, and `fold`, making it easier to work with collections. More details on these can be found in the [ErgoScript Compiler Documentation](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/ergoscript-compiler.md).
- **Boolean Predicates**: ErgoScript programs, like ErgoTree, consist of sequences of boolean predicates connected using `&&` (AND) and `||` (OR).
- **Cryptographic Operations**: ErgoScript supports cryptographic operations with `BigInt` and `GroupElement` types, allowing for addition, multiplication, and exponentiation. Note that `BigInt` operations in ErgoScript are performed modulo `2^256`, so overflow management is crucial.

### Example: Basic ErgoScript Syntax

Here’s a simple ErgoScript example to help you get started:

```scala
val bool: Boolean = true
```

In this example:

- **`val`**: A keyword used to create an immutable value.
- **`bool`**: The name of the variable being created.
- **`: Boolean`**: The type of the variable (Boolean in this case). Specifying the type is optional but recommended for clarity.
- **`= true`**: Assigns the value `true` to `bool`.


### More ErgoScript Syntax Examples

Let's explore a more complex example that demonstrates control structures, data types, and basic operations:

```scala
if(bool == true){
    val x = 0
    val y = 1
    val z = ((x * y) + 5) - (3 / 2)
}else{
    val x = 2L
    val y: Coll[Long]  = Coll(0L, 1L, x) // Creating a collection of Long elements
    val z: (Long, Long) = (3, 4)
    val a: (Long, Coll[Long]) = (x, y) // Combining Long and collection types
    val b: Coll[((Long, Long), Boolean)] = Coll(((2L, 4L), true), ((7L, 2L), false))
}
```

In this code:

- **Control Structures**: The `if-else` statement directs the flow based on the `bool` value.
- **Data Types**:

      - `x` and `y` are integers.
      - `z` is calculated based on arithmetic operations.
      - `y` in the `else` block is a collection of `Long` values (`Coll[Long]`).
      - `a` is a tuple combining a `Long` and a collection.
      - `b` is a collection of tuples with pairs of `Long` values and Booleans.

### Def vs Val: Understanding Function Definitions

ErgoScript allows you to define functions using either `def` or `val`. Understanding the distinction is crucial for writing efficient and effective scripts:

#### Example Code

```scala
def computeAsDef(myInt: Int): Int = {
  myInt + 1
}

val computeAsVal: Int = {
  (myInt: Int) =>
    myInt + 1
}
```

Both functions accomplish the same task but differ in when the computation occurs:

- **`computeAsDef`**: Defined using `def`, this function is evaluated each time it is called, allowing for dynamic computation.
- **`computeAsVal`**: Defined using `val`, this is a function literal (lambda). The computation is defined at script initialization and only executed when the function is invoked.

### Advanced Functional Programming in ErgoScript

ErgoScript supports higher-order functions and advanced functional programming constructs, allowing for powerful data manipulation:

```scala
val myMap: Coll[(Int, Long)] = {      
  val intCollection = Coll(0, 1, 2)
  intCollection.map{
    (myInt: Int) =>                   
    (myInt, myInt.toLong)
  }                                      
}
```

In this example:

- **`Coll[(Int, Long)]`**: Defines a collection of tuples with `Int` and `Long` pairs.
- **`map` Function**: Applies a transformation to each element in the collection using a lambda expression, converting each `Int` to a `Long`.

For more details on collections and functional programming in ErgoScript, refer to the [Colls.scala](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/core/shared/src/main/scala/sigma/Colls.scala) file.

## Additional Resources

For further learning and a deeper dive into ErgoScript, explore the following resources:

- [Deco Education - ErgoScript Developer Course](https://github.com/DeCo-Education/ErgoScript-Developer-Course/blob/main/Class-Documents/Class-1/Materials/Class1.MD)
- [ErgoScript Specification](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/sigma-dsl.md): Detailed reference for Sigma Protocols and ErgoScript.
- [LangSpec.md](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md): Comprehensive language specification for ErgoScript.
- [ErgoScript Reference Guide](https://ergoplatform.org/en/blog/2021_07_26_ergo_script_guide/): A detailed guide on writing ErgoScript.
