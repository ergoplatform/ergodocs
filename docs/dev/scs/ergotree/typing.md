# ErgoTree Typing
> This page is a WIP. Please see [ErgoTree.pdf](https://storage.googleapis.com/ergo-cms-media/docs/ErgoTree.pdf) for full details.


Figure 3: Typing rules of ErgoTree

Note that each well-typed term has exactly one type hence we assume there exists a funcion **term Type : T erm → T** which relates each well-typed term with the corresponding type.

Primitive operations can be parameterized with type variables, for example addition (B.0.19) has the signature def **+[T](left: T, right: T)**: T where T is one of the numeric types (Table 8).

Function ptype returns the type of a primitive operation specialized for the concrete types of its arguments, for example **ptype(+, Int, Int) = (Int, Int) → Int**.

Similarily, the function **mtype** returns a type of method specialized for concrete types of the arguments of the **MethodCall** term.

**lockValue** rule defines a type of well-formed block expression. It assumes a total ordering on val definitions. If a block expression is not well-formed than it cannot be typed and evaluated.

The rest of the rules are standard for typed lambda calculus