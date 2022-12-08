$$
\newcommand{\TEnv}{\Gamma}
\newcommand{\Der}[2]{#1~\vdash~#2}
\newcommand{\DerV}[2]{#1~\vdash^{\text{\lst{v}}}~#2}
\newcommand{\DerC}[2]{#1~\vdash^{\text{\lst{c}}}~#2}
\newcommand{\DerEnv}[1]{\Der{\TEnv}{#1}}
\newcommand{\DerEnvV}[1]{\DerV{\TEnv}{#1}}
\newcommand{\DerEnvC}[1]{\DerC{\TEnv}{#1}}
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


# ErgoTree Typing

$\langname$ is a strictly typed language, in which every term should have a type in order to be wellformed and evaluated. Typing judgement of the form $\Der{\Gamma}{e : T}$ say that $e$ is a term of type $T$ in the typing context $\Gamma$.


### **Figure 3: Typing rules of ErgoTree**



$$\frac{}{\Der{\Gamma}{C(\_, T)~:~T}}~(Const)$$

$$\frac{}{\Der{\Gamma,x~:~T}{x~:~T}}~(Var)$$

$$\frac{\Ov{\DerEnv{e_i:~T_i}}~~ptype(\delta, \Ov{T_i}) :~(T_1,\dots,T_n) \to T}{\Apply{\delta}{\Ov{e_i}}:~T}~(Prim)$$

$$\frac{\DerEnv{e_1 :~T_1}~~\dots~~\DerEnv{e_n :~T_n}}      {\DerEnv{(e_1,\dots,e_n)~:~(T_1,\dots,T_n)}}~(Tuple)$$

$$\frac{\DerEnv{e~:~I,~e_i:~T_i}~~mtype(m, I, \Ov{T_i})~:~(I, T_1,\dots,T_n) \to T}{ \Apply{e.m}{\Ov{e_i}}:~T }~(MethodCall)$$ 


$$\frac{\Der{\TEnv,\Ov{x_i:~T_i}}{e~:~T}}{\Der{\Gamma}{\TyLam{x_i}{T_i}{e}~:~(T_0,\dots,T_n) \to T}}~(FuncExpr)$$

$$\frac{\Der{\TEnv}{e_f:~(T_1,\dots,T_n) \to T}~~~\Ov{\Der{\TEnv}{e_i:~T_i}} }{ \Der{\Gamma}{\Apply{e_f}{\Ov{e_i}}~:~T} }~(Apply)$$


$$\frac{\DerEnv{e_{cond}:~\lst{Boolean}}~~\DerEnv{e_1:~T}~~\DerEnv{e_2 :~T} }{\DerEnv{\IfThenElse{e_{cond}}{e_1}{e_2}~:~T} }~\lst{(If)}$$

$\frac{\DerEnv{e_1 :~T_1}~\wedge~\forall k\in\{2,\dots,n\}~\Der{\Gamma,x_1:~T_1,\dots,x_{k-1}:~T_{k-1}}{e_k:~T_k}~\wedge~\Der{\Gamma,x_1:~T_1,\dots,x_n:~T_n}{e:~T}}{ \DerEnv{\{ \Ov{\text{val}}~x_i = e_i;}~e\}~:~T} ~(BlockExpr)$






> Note that each well-typed term has exactly one type; hence we assume there exists a function $termType: Term \to \mathcal{T}$ which relates each well-typed term with the corresponding type.

**Primitive operations** can be parameterized with type variables; for example,[addition](https://raw.githubusercontent.com/ScorexFoundation/sigmastate-interpreter/4daec63275fd4e1364cf7a1132f3e7be6157bb5c/docs/spec/ergotree.pdf) has the signature $+~:~ (T,T) \to T$ where $T$ is a [numeric type](types.md). Function $ptype$, defined in [primops](), returns a type of primitive operation specialized for concrete types of its arguments, for example, $ptype(+,Int, Int) = (Int, Int) \to Int$.

Similarly, the function $mtype$ returns a type of method specialized for concrete types of the arguments of the MethodCall term.

**BlockExpr** rule defines a type of well-formed block expression. It assumes a total ordering on **val** definitions. If a block expression is not well-formed, than is cannot be typed and evaluated.

The rest of the rules are standard for typed lambda calculus.