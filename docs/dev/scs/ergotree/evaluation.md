# ErgoTree Evaluation

> This page is a WIP. Please see [ErgoTree.pdf](https://storage.googleapis.com/ergo-cms-media/docs/ErgoTree.pdf) for full details.


In this section we describe evaluation semantics of the ErgoTree language and the corresponding
reference implementation of the interpreter

## Semantics

Evaluation of ErgoTree is specified by its translation to **Core-λ**, whose terms form a subset of ErgoTree terms. Thus, typing rules of **Core-λ** form a subset of typing rules of ErgoTree.

Here we specify evaluation semantics of **Core-λ**, which is based on call-by-value (CBV) lambda calculus. Evaluation of **Core-λ** is specified using denotational semantics. To do that, we first specify denotations of types, then typed terms and then equations of denotational semantics.

> Definition 1 (values, producers) The following **Core-λ** terms are called values:
> 
> - V :== x | C(d, T ) | λx.M
> 
> All **Core-λ** terms are called producers. (This is because, when evaluated, they produce a value.)

We now describe and explain a denotational semantics for the **Core-λ** language. The key principle is that each type A denotes a set JAK whose elements are the denotations of values of the type A.

Thus, the type Boolean denotes the 2-element set {true, false}, because there are two values of type Boolean. Likewise the type (T1, . . . , Tn) denotes (JT1K, . . . , JTnK) because a value of type (T1, . . . , Tn) must be of the form (V1, . . . , Vn), where each Vi is value of type Ti. 

Given a value V of type A, we write JV K for the element of A that it denotes. Given a close term M of type A, we recall that it produces a value V of type A. So M will denote an element JM K of JAK.

A value of type A → B is of the form λx.M . This, when applied to a value of type A gives a value of type B. So A → B denotes JAK → JBK. It is true that the syntax appears to allow us to apply λx.M to any term N of type A. But N will be evaluated before it interracts with λx.M , so λx.M is really only applied to the value that N produces (hence the semantics is call-by-value).

> **Definition 2** A context Γ is a finite sequence of identifiers with value types x1 : A1, . . . , xn : An.

Sometimes we omit the identifiers and write Γ as a list of value types.

Given a context Γ = x1 : A1, . . . , xn : An, an environment (list of bindings for identifiers) associates to each xi as value of type Ai. So the environment denotes an element of (JA1K, . . . , JAnK), and we write JΓK for this set.

Given a **Core-λ** term Γ  M : B, we see that M , together with environment, gives a closed term of type B. So M denotes a function JM K from JΓK to JBK.

In summary, the denotational semantics is organized as follows.
 A type A denotes the set JAK
7
 A context x1 : A1, . . . , xn : An denotes the set (JA1K, . . . , JAnK)
 A term Γ ` M : B denotes a function JM K : JΓK → JBK
The denotations of types and terms is given in Figure 4.
Figure 4: Denotational semantics of **Core-λ**
The denotations of **Core-λ** types
JBooleanK = {true, false}
JPK = see set of values in Appendix A
J(T1, . . . , Tn)K = (JT1K, . . . , JTnK)
JA → BK = JAK → JBK
The denotations of **Core-λ** terms which together specify the function J K : JΓK → JT K
JxK〈(ρ, x 7 → x, ρ′)〉 = x
JC(d, T )K〈ρ〉 = d
J(Mi)K〈ρ〉 = (JMiK〈ρ〉)
Jδ〈N 〉K〈ρ〉 = (JδK〈ρ〉)〈v〉 where v = JN K〈ρ〉
Jλx.M K〈ρ〉 = λx.JM K〈(ρ, x 7 → x)〉
JMf 〈N 〉K〈ρ〉 = (JMf K〈ρ〉)〈v〉 where v = JN K〈ρ〉
JMI .m〈Ni〉K〈ρ〉 = (JMI K〈ρ〉).m〈vi〉 where vi = JNiK〈ρ〉