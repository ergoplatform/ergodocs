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

# ErgoTree as a Language

This section provides improved and clearer documentation for the ErgoTree language. ErgoTree is a typed, call-by-value, higher-order functional language without recursion. It supports various features such as single-assignment blocks, tuples, optional values, indexed collections with higher-order operations, short-circuiting logical operations, and ternary if-else expressions with lazy branches. It is important to note that all operations in ErgoTree are deterministic, without side effects, and all values are immutable.

The semantics of ErgoTree are specified by first translating it to a lower-level language called Core-λ and then providing its denotational evaluation semantics. The abstract syntax of ErgoTree is defined in Table 1, which represents the `Value` class hierarchy in the reference implementation. The values in the "Mnemonic" column correspond to specific classes in the reference implementation.

### Table 1: Abstract syntax of ErgoTree language

| Set Name | Syntax | Mnemonic | Description |
|----------|--------|----------|-------------|
| $\mathcal{T} \ni T$ | **P** | **SPredefType** | See [Types](types.md) |
| | $\tau$ | **STypeVar** | Type variable |
| | $(T_1, \ldots, T_n)$ | **STuple** | Tuple of $n$ elements (see [Tuple] type) |
| | $(T_1, \ldots, T_n) \to T$ | **SFunc** | Function of $n$ arguments (see [Func] type) |
| | ${{Coll}}[T]$ | **SCollection** | Collection of elements of type $T$ |
| | ${{Option}}[T]$ | **SOption** | Optional value of type $T$ |
| $Term \ni e$ | $C(v, T)$ | **Constant** | Typed constant |
| | $x$ | **ValUse** | Variable |
| | $\TyLam{x_i}{T_i}{e}$ | **FuncExpr** | Lambda expression |
| | $\Apply{e_f}{\Ov{e_i}}$ | **Apply** | Application of a functional expression |
| | $\Apply{e.m}{\Ov{e_i}}$ | **MethodCall** | Method invocation |
| | $\Apply{e_f}{\Ov{e_i}}$ | **Tuple** | Constructor of a tuple with $n$ items |
| | $\Apply{\delta}{\Ov{e_i}}$ | | Primitive application |
| | $\text{if}~(e_{\text{cond}})~e_1~\text{else}~e_2$ | **If** | If-then-else expression |
| | $\{{ \overline{{\text{val}}}~x_i = e_i;}~e\}$ | **BlockExpr** | Block expression |
| $cd$ | $\Trait{I}{\overline{ms_i}}$ | **STypeCompanion** | Interface declaration |
| $ms$ | $\MSig{m[\overline{\tau_i}]}{\overline{x_i : T_i}}{T}$ | **SMethod** | Method signature declaration |

The terms in ErgoTree are assigned types according to the typing rules specified in [Typing](typing.md).

- **Constants** contain both the type and the data value of that type. The type of a constant must correspond to its value for it to be well-formed.
- **Variables** are always typed and identified by a unique ID, which refers to either a lambda-bound variable or a val-bound variable.
- **Lambda expressions** can take a list of lambda-bound variables, which can be used in the body expression. The body expression itself can also be a **block expression**.
- **Function application** takes an expression of functional type (e.g., $(T_1, \ldots, T_n) \to T$) and a list of arguments. The notation $e_f(\Ov{e})$ is not used to represent function application because it suggests that $(\Ov{e})$ is a subterm, which it is not.
- **Method invocation** allows the application of functions defined as methods of types. If an expression $e$ has type $T$, and a method $m$ is declared in type $T$, the method invocation $e.m(args)$ is valid. For more information on types and their methods, refer to [Types](types.md).
- **Conditional expressions** in ErgoTree evaluate the condition strictly and the branches lazily. Each branch is an expression executed based on the result of the condition. This laziness is specified by lowering the expressions to Core-λ (see Figure 2).
- **Block expressions** contain a list of **val** definitions (bindings) of variables. Each subsequent definition in the block can only refer to previously defined variables. The result of the block's execution is the result of the final expression $e$, which can refer to any variable defined within the block.

Each **type** in ErgoTree can be associated with a list of method declarations, indicating that the type has methods. The semantics of these methods follow similar principles to those in object-oriented languages like Java or Scala. When an instance of a type with methods exists, it is possible to call methods on the instance with additional arguments.

Each **method** in ErgoTree can be parameterized by type variables, which are used in the method signature. Since ErgoTree only supports monomorphic values, each method call is monomorphic, and all type variables are assigned concrete types (see the MethodCall typing rule in [typing](typing.md)).

To specify the semantics of ErgoTree, its terms are translated to a lower-level language called Core-λ, which is a simplified language without lazy operations. The lowering rules are defined in Figure 2.

## Figure 2: Lowering to Core-λ

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

All $n$-ary lambdas where $n > 1$ are transformed into single-argument lambdas using tupled arguments.

It should be noted that the $\IfThenElse{e_{\text{cond}}}{e_1}{e_2}$ term in ErgoTree has lazy evaluation of its branches, while the right-hand-side $\lst{if}$ is a primitive operation with strict evaluation of the arguments. Laziness is achieved using lambda expressions of type $\lst{Unit} \to \lst{Boolean}$.

Logical operations ($\lst{||}$, `&&`) in ErgoTree, which are lazy (short-circuiting) on the second argument, are translated to $\lst{if}$ terms in ErgoTree, which are then recursively translated to the corresponding Core-λ terms.

Syntactic blocks in ErgoTree are eliminated and translated into nested lambda expressions, which unambiguously specify the evaluation semantics of blocks. The evaluation semantics of Core-λ are specified in [evaluation](evaluation.md).

Note that the lowering transformation is used solely to specify semantics. Implementations may optimize the evaluation of ErgoTree directly as long as the semantics are preserved.
