$$
\newcommand{\lst}[1]{#1}
\newcommand{\Tup}[1]{(#1)}
\newcommand{\Apply}[2]{#1\langle#2\rangle}
\newcommand{\MSig}[3]{\text{def}~#1(#2): #3}
\newcommand{\Ov}[1]{\overline{#1}}
\newcommand{\TyLam}[3]{\lambda(\Ov{#1:#2}).#3}
\newcommand{\Trait}[2]{\text{trait}~#1~\{ #2 \}}
\newcommand{\To}{\mapsto}
\newcommand{\Low}[1]{\mathcal{L}{[\![#1]\!]}}
\newcommand{\Lam}[2]{\lambda#1.#2}
\newcommand{\IfThenElse}[3]{\text{if}~(#1)~#2~\text{else}~#3}
\newcommand{\False}{\text{false}}
\newcommand{\True}{\text{true}}
\newcommand{\langname}{ErgoTree}
\newcommand{\corelang}{Core-\lambda}
$$



# ErgoTree as a language

In this section, we define an abstract syntax for the ErgoTree language. It is a typed **call-by-value, higher-order functional language without recursion**.

It supports single-assignment blocks, tuples, optional values, indexed collections with higher-order operations, short-cutting logicals, and ternary ’if’ with lazy branches. 

**All operations are deterministic, without side effects and all values are *immutable*.**

The semantics of ErgoTree is specified by first translating it to core calculus (***Core-λ***) and then giving its denotational evaluation semantics. 

In Table 1, ErgoTree is defined below using abstract syntax notation. This corresponds to the **Value** class of the reference implementation, which can be serialized to an array of bytes using **ValueSerializer**. 

The values in the *'mnemonic'* column correspond to reference implementation classes.

### **Table 1: Abstract syntax of ErgoScript language**

| Set Name | | Syntax | Mnemonic | Description |
|--||--|--|----|
$\mathcal{T} \ni T$ | ::=   |    **P**  | **SPredefType**   | See [Types](types.md)
|   | $\mid$    | $\tau$    | **STypeVar** | type variable 
|   | $\mid$    | $(T_1, ... ,T_n)$ | **STuple** | tuple of $n$ elements (see [Tuple] type)
|   | $\mid$    | $(T_1,...,T_n) \to T$ | **SFunc** | function of $n$ arguments (see [Func] type) 
|   | $\mid$    | ${{Coll}}[T]$         | **SCollection** | collection of elements of type $T$   
|   | $\mid$    | ${{Option}}[T]$       | **SOption** | optional value of type $T$  
$Term\ni e$ | ::=       |   $C(v, T)$               | **Constant** | typed constants  
|   | $\mid$    |   $x$                     | **ValUse** | variables  
|   | $\mid$    |   $\TyLam{x_i}{T_i}{e}$       | **FuncExpr** | lambda expression 
|   | $\mid$    |   $\Apply{e_f}{\Ov{e_i}}$     | **Apply** | application of functional expression 
|   | $\mid$    |   $\Apply{e.m}{\Ov{e_i}}$     | **MethodCall** | method invocation  
|   | $\mid$    |   $\Apply{e_f}{\Ov{e_i}}$     | **Tuple** | constructor of tuple with $n$ items 
|   | $\mid$    |   $\Apply{\delta}{\Ov{e_i}}$  | | primitive application
|   | $\mid$    |   if $(e_{cond})$ $e_1$ **else} $e_2$ | **If** | if-then-else expression 
|   | $\mid$    |   $\{{{ \overline{{val}}}~x_i = e_i;}~e\}$  | **BlockExpr** | block expression 
$cd$    |   ::= |   $\Trait{I}{\overline{ms_i}}$    | **STypeCompanion** | interface declaration    
$ms$    |   ::= | $\MSig{m[\overline{\tau_i}]}{\overline{x_i : T_i}}{T}$    | **SMethod** | method signature declaration   


We assign types to the terms in a standard way following the typing rules shown in [Typing](typing.md).

- **Constants** keep both the type and the data value of that type. To be well-formed, the type of the constant should correspond to its value.
- **Variables** are always typed and identified by a unique id, which refers to either lambda bound variable or a val bound variable.
- **Lambda expressions** can take a list of lambda-bound variables which can be used in the body expression, which can be a **block expression**.
- **Function application** takes an expression of functional type (e.g. $T_1 \to T_n$) and a list of arguments. The reason we do not write it $e_f(\Ov{e})$ is that this notation suggests that $(\Ov{e})$ is a subterm, which it is not.
- **Method invocation** allows us to apply functions that are defined as methods of types. If expression e has type T and method m is declared in the type T, method invocation e.m(args) is defined for the appropriate args. See section A for the specification of types and their methods.
- **Conditional expressions** of ErgoTree are strict in the condition and lazy in both of the branches.
    - Each branch is an expression executed depending on the result of the condition—this laziness of branches is specified by lowering to Core-λ (see Figure 2).
- **Block expression** contains a list of **val** definitions of variables. To be wellformed, each subsequent definition can only refer to the previously defined variables. The result of block execution is the result of the expression e, which can refer to any block variable.

Each **type** may be associated with a list of method declarations, in which case we say the type has methods. The semantics of the methods is the same as in Java. Having an instance of some type with methods, it is possible to call methods on the instance with additional arguments. 

Each **method** can be parameterized by type variables, which can be used in the method signature. Because ErgoTree supports only monomorphic values, each method call is monomorphic, and all type variables are assigned to concrete types (see MethodCall typing rule in [typing](typing.md)).

The semantics of ErgoTree is specified by translating all its terms to a somewhat lower and simplified language, which we call Core-λ and does not have lazy operations.

## **Figure 2: Lowering to Core-λ**


| $Term_{ErgoTree}$ | | $Term_{Core}$  | 
|---||---|
$\Low{ \TyLam{x_i}{T_i}{e}      }$ | $\To$ | $\Lam{   x:(T_0,\dots,T_n)}{ \Low{ \{ \Ov{\lst{val}~x_i: T_i = x.\_i;}~e\} } }$    
$\Low{ \Apply{e_f}{\Ov{e_i}}    }$ | $\To$ | $\Apply{ \Low{e_f} }{ \Low{(\Ov{e_i})} }$  
$\Low{ \Apply{e.m}{\Ov{e_i}}    }$ | $\To$ | $\Apply{ \Low{e}.m}{\Ov{ \Low{e_i} }}$ 
$\Low{ \Tup{e_1, \dots ,e_n}    }$ | $\To$ | $\Tup{   \Low{e_1}, \dots ,\Low{e_n}}$ 
$\Low{ e_1~\text{\|\|}~e_2        }$ | $\To$ | $\Low{   \IfThenElse{ e_1 }{ \True }{ e_2 }}$    
$\Low{ e_1~\text{&&}~e_2      }$ | $\To$ | $\Low{   \IfThenElse{ e_1 }{ e_2 }{ \False } }$  
$\Low{ \IfThenElse{e_{cond}}{e_1}{e_2} }$ | $\To$ | $\Apply{(if(\Low{e_{cond}} ,~\Lam{(\_:Unit)}{\Low{e_1}} ,~\Lam{(\_:Unit)}{\Low{e_2}} ))}{}$ 
$\Low{ \{ \Ov{\text{val}~x_i: T_i = e_i;}~e\} }$ | $\To$ | $\Apply{ (\Lam{(x_1:T_1)}{( \dots \Apply{(\Lam{(x_n:T_n)}{\Low{e}})}{\Low{e_n}} \dots )}) }{\Low{e_1}}$\\
$\Low{ \Apply{\delta}{\Ov{e_i}} }$ | $\To$ | $\Apply{\delta}{\Ov{ \Low{e_i} }}$ 
$\Low{ e }$     | $\To$ |  $e$  

All $n$-ary lambdas when $n>1$ are transformed to single arguments lambdas using tupled arguments.

> Note that $\IfThenElse{e_{cond}}{e_1}{e_2}$ term of $\langname$ has a lazy evaluation of its branches whereas right-hand-side $\lst{if}$ is a primitive operation and has a strict evaluation of the arguments. The laziness is achieved using lambda expressions of $\lst{Unit}$ $\to$ $\lst{Boolean}$ type.

We translate logical operations ($\lst{||}$, &&) of $\langname$, which are lazy on second argument to $\lst{if}$ term of $\langname$, which is recursively translated to the corresponding $\corelang$ term.

Syntactic blocks of $\langname$ are eliminated and translated to nested lambda expressions, which unambiguously specify the evaluation semantics of blocks. The $\corelang$ is specified in [evaluation](evaluation.md).

Note that we use lowering transformation only to specify semantics. 

Implementations can optimize by evaluating ErgoTree directly as long as the semantics is preserved.

