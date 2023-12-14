# ErgoTree Evaluation
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
\newcommand{\Denot}[1]{[\![#1]\!]}  
$$


Evaluation of $\langname$ is specified by its translation to $\corelang$, whose terms form a subset of $\langname$ terms. Thus, typing rules of $\corelang$ form a subset of typing rules of $\langname$.

Here we specify evaluation semantics of $\corelang$, which is based on call-by-value (CBV) lambda calculus. Evaluation of $\corelang$ is specified using denotational semantics. To do that, we first specify denotations of types, then typed terms and then equations of denotational semantics.


/// details | Definition 1
    {type: note, open: true}

**The following $\corelang$ terms are called values:**

$$V :== x \mid C(d, T) \mid \Lam{x}{M}$$

All $\corelang$ terms are called ***producers***. (This is because, when evaluated, they produce a value.)

///


We now describe and explain a denotational semantics for the $\corelang$ language. The key principle is that each type $A$ denotes a set $\Denot{A}$ whose elements are the denotations of values of the type $A$.

Thus the type [$\lst{Boolean}$](types.md#boolean) denotes the 2-element set $\{\lst{true},\lst{false}\}$, because there are two values of type $\lst{Boolean}$. Likewise the type $(T_1,\dots,T_n)$ denotes $(\Denot{T_1},\dots,\Denot{T_n})$ because a value of type $(T_1,\dots,T_n)$ must be of the form $(V_1,\dots,V_n)$, where each $V_i$ is value of type $T_i$.

Given a value $V$ of type $A$, we write $\Denot{V}$ for the element of $A$ that it denotes. Given a close term $M$ of type $A$, we recall that it produces a value $V$ of type $A$. So $M$ will denote an element $\Denot{M}$ of $\Denot{A}$.

A value of type $A \to B$ is of the form $\Lam{x}{M}$. This, when applied to a value of type $A$ gives a value of type $B$. So $A \to B$ denotes $\Denot{A} \to \Denot{B}$. It is true that the syntax appears to allow us to apply $\Lam{x}{M}$ to any term $N$ of type $A$. But $N$ will be evaluated before it interracts with $\Lam{x}{M}$, so $\Lam{x}{M}$ is really only applied to the value that $N$ produces.

/// details | Definition 2
    {type: note, open: true}
A **context** $\Gamma$ is a finite sequence of identifiers with valuetypes $x_1:A_1, \dots ,x_n:A_n$. Sometimes we omit the identifiers and write $\Gamma$ as a list of value types.
///



- Given a context $\Gamma = x_1:A_1,\dots,x_n:A_n$, an environment (list of bindings for identifiers) associates to each $x_i$ as value of type $A_i$. So the environment denotes an element of $(\Denot{A_1},\dots,\Denot{A_n})$, and we write $\Denot{\Gamma}$ for this set.
- Given a $\corelang$ term $\DerEnv{M: B}$, we see that $M$, together with environment, gives a closed term of type $B$. So $M$ denotes a function $\Denot{M}$ from $\Denot{\Gamma}$ to $\Denot{B}$.

In summary, the denotational semantics is organized as follows.

- A type $A$ denotes a set $\Denot{A}$
- A context $x_1:A_1,\dots,x_n:A_n$ denotes the set $(\Denot{A_1},\dots,\Denot{A_n})$
- A term $\DerEnv{M: B}$ denotes a function $\Denot{M}$: $\Denot{\Gamma} \to \Denot{B}$


The denotations of $\corelang$ **types**


$$\Denot{\lst{Boolean}}  =  \{ \lst{true}, \lst{false} \}$$  

$$\Denot{\lst{P}}  = \text{see set of values in Appendix A}$$

$$\Denot{(T_1,\dots,T_n)} =  (\Denot{T_1},\dots,\Denot{T_n}) $$

$$\Denot{A \to B}  =  \Denot{A} \to \Denot{B}$$

The denotations of $\corelang$ **terms** which together specify the function $\Denot{\_}: \Denot{\Gamma} \to \Denot{T}$


$$\Apply{ \Denot{\lst{x}}			}{(\rho,\lst{x}\mapsto x, \rho')} = x$$

$$\Apply{ \Denot{C(d, T)} 			}{\rho}  =  d$$

$$\Apply{ \Denot{(\Ov{M_i})} 		}{\rho}  =  (\Ov{ \Apply{\Denot{M_i}}{\rho} })$$
	

$$\Apply{ \Denot{\Apply{\delta}{N}} }{\rho}  = \Apply{ (\Apply{\Denot{\delta}}{\rho}) }{ v }~where~v = \Apply{\Denot{N}}{\rho}$$

$$\Apply{ \Denot{\Lam{\lst{x}}{M}}	}{\rho}  =  \Lam{x}{ \Apply{\Denot{M}}{(\rho, \lst{x}\mapsto x)} }$$	

$$\Apply{ \Denot{\Apply{M_f}{N}}	}{\rho}  =  \Apply{ (\Apply{\Denot{M_f}}{\rho}) }{ v }~where~v = \Apply{\Denot{N}}{\rho}$$

$$\Apply{ \Denot{\Apply{M_I.\lst{m}}{\Ov{N_i}} }	}{\rho}  =  \Apply{ (\Apply{\Denot{M_I}}{\rho}).m }{ \Ov{v_i} }~where~\Ov{v_i = \Apply{\Denot{N_i}}{\rho}}$$ 


