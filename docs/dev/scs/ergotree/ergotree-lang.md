# ErgoTree as a language

> This page is a WIP. Please see [ErgoTree.pdf](https://storage.googleapis.com/ergo-cms-media/docs/ErgoTree.pdf) for full details.


In this section we define an abstract syntax for the ErgoTree language. It is a typed call-by-value, higher-order functional language without recursion. It supports single-assignment blocks, tuples, optional values, indexed collections with higher-order operations, short-cutting logicals, ternary ’if’ with lazy branches. All operations are deterministic, without side effects and all values are
immutable.

The semantics of ErgoTree is specified by first translating it to a core calculus (Core-λ) and then by giving its denotational evaluation semantics. Typing rules are given in section 3 and the evaluation semantics is given in section 4. In section 5 we describe serialization format of ErgoTree.

Guidance on compliant interpreter implementation is provided in section 6.

ErgoTree is defined below using abstract syntax notation as shown in Figure 1. This corresponds to Value class of the reference implementation, which can be serialized to an array of bytes using **ValueSerializer**. The mnemonic names shown in the figure correspond to classes of the reference implementation.

Figure 1: Abstract syntax of ErgoScript language

We assign types to the terms in a standard way following typing rules shown in Figure 3.

Constants keep both the type and the data value of that type. To be well-formed the type of the constant should correspond to its value.
Variables are always typed and identified by unique id, which refers to either lambda bound variable or a val bound variable.

Lambda expressions can take a list of lambda-bound variables which can be used in the body expression, which can be a block expression.

Function application takes an expression of functional type (e.g. T1 → Tn) and a list of arguments. The reason we do not write it e<sub>f</sub>(e<sup>-</sup>) is that this notation suggests that (e) is a subterm, which it is not.

Method invocation allows to apply functions defined as methods of types. If expression e has type T and and method m is declared in the type T then method invocation e.m(args) is defined for the appropriate args. See section A for the specification of types and their methods.

Conditional expressions of ErgoTree are strict in the condition and lazy in both of the branches.

Each branch is an expression which is executed depending on the result of condition. This laziness of branches specified by lowering to Core-λ (see Figure 2).

Block expression contains a list of val definitions of variables. To be wellformed each subsequent definition can only refer to the previously defined variables. Result of block execution is the result of the resulting expression e, which can refer to any variable of the block.

Each type may be associated with a list of method declarations, in which case we say that the type has methods. The semantics of the methods is the same as in Java. Having an instance of some type with methods it is possible to call methods on the instance with some additional arguments. 

Each method can be parameterized by type variables, which can be used in method signature. Because ErgoTree supports only monomorphic values each method call is monomorphic and all type variables are assigned to concrete types (see MethodCall typing rule in Figure 3).

The semantics of ErgoTree is specified by translating all its terms to a somewhat lower and simplified language, which we call Core-λ and which doesn’t have lazy operations. This lowering translation is shown in Figure 2.

Figure 2: Lowering to Core-λ

Note that if (econd) e1 else e2 term of ErgoTree has lazy evaluation of its branches whereas right-hand-side if is a primitive operation and have strict evaluation of the arguments. The laziness is achieved by using lambda expressions of Unit ⇒ Boolean type.
We translate logical operations (||, &&) of ErgoTree, which are lazy on second argument to if term of ErgoTree, which is recursively translated to the corresponding Core-λ term.

Syntactic blocks of ErgoTree are completely eliminated and translated to nested lambda expressions, which unambiguously specify evaluation semantics of blocks. The semantics of Core-λ is specified in Section 4.

Note, that we use lowering transformation only to specify semantics. Implementations can optimize by evaluating ErgoTree directly as long as the semantics is preserved.