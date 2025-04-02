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
\newcommand{\MaxVlqSize}{VLQ_{max}}
\newcommand{\MaxBits}{Bits_{max}}
\newcommand{\MaxBytes}{Bytes_{max}}
\newcommand{\MaxTypeSize}{T_{max}}
\newcommand{\MaxDataSize}{D_{max}}
\newcommand{\MaxBox}{Box_{max}}
\newcommand{\MaxSigmaProp}{SigmaProp_{max}}
\newcommand{\MaxAvlTree}{AvlTree_{max}}
\newcommand{\MaxConstSize}{C_{max}}
\newcommand{\MaxExprSize}{Expr_{max}}
\newcommand{\MaxErgoTreeSize}{ErgoTree_{max}}
\newcommand{\Denot}[1]{[\![#1]\!]}
\newcommand{\ASDag}{ErgoTree}
$$

# Serialization

This page defines the binary format used to store ErgoTree contracts in persistent stores, transfer them over the wire, and enable cross-platform interoperation.

## Overview

The terms of the [ErgoTree language](ergotree-lang.md) can be serialized into an array of bytes for storage in the Ergo blockchain (e.g., in the `propositionBytes` field of a `Box`).

When the guarding script of a transaction's input box is validated, the `propositionBytes` array is deserialized into an **ErgoTree Intermediate Representation (IR)** (represented by the `ErgoTree` class in the reference implementation), which can then be [evaluated](evaluation.md).

The serialization procedure is specified in general terms. The serialization format for ErgoTree types (specified by the `SType` class hierarchy) and expression nodes (specified by the `Value` class hierarchy) is defined in [section 5.1](#table-1-serialization-limits) and [Appendix C](#table-2-serialization-formats), respectively.

Table 1 shows the size limits checked during contract deserialization, which are important for resisting malicious script attacks.

### Table 1: Serialization limits

| Constant | Value | Description |
|---|---|---|
| VLQ <sub> max </sub> | 10 | Maximum size of VLQ encoded byte sequence (See VLQ formats E.1) |
| T <sub> max </sub> | 100 | Maximum size of serialized type term (see Type format 5.1) |
| D <sub> max </sub> | 4Kb | Maximum size of serialized data instance (see Data format 5.2) |
| C <sub> max </sub> | = T <sub> max </sub> + D <sub> max </sub> | Maximum size of serialized data instance (see Const format 5.3) |
| Expr <sub> max </sub> | 4Kb | Maximum size of serialized ErgoTree term (see Expr format 5.4) |
| ErgoTree <sub> max </sub> | 4Kb | Maximum size of serialized ErgoTree contract (see ErgoTree format 5.5) |


All the serialization formats used and defined throughout this section are listed in Table 2, which introduces a name for each format and shows the number of bytes each format may occupy in the byte stream.

### Table 2: Serialization formats

|   Format          | #bytes          | Description |
|---|---|---|
|   $\lst{Byte}$    | $1$            | 8-bit signed two's-complement integer |
|   $\lst{Short}$ | $2$ | 16-bit signed two's-complement integer (big-endian) |
|   $\lst{Int}$ | $4$ | 32-bit signed two's-complement integer (big-endian) |
|   $\lst{Long}$ | $8$ | 64-bit signed two's-complement integer (big-endian) |
|   $\lst{UByte}$ | $1$ | 8-bit unsigned integer |
|   $\lst{UShort}$ | $2$ | 16-bit unsigned integer (big-endian) |
|   $\lst{UInt}$ | $4$ | 32-bit unsigned integer (big-endian) |
|   $\lst{ULong}$ | $8$ | 64-bit unsigned integer (big-endian) |
|   $\lst{VLQ(UShort)}$ | $[1..3]$ | Encoded unsigned $\lst{Short}$ value using VLQ. |
|   $\lst{VLQ(UInt)}$ | $[1..5]$ | Encoded unsigned 32-bit integer using VLQ. |
|   $\lst{VLQ(ULong)}$ | $[1..\MaxVlqSize]$ | Encoded unsigned 64-bit integer using VLQ. |
|$\lst{Bits}$ | $[1..\MaxBits]$ | A collection of bits packed in a sequence of bytes. |
|$\lst{Bytes}$ | $[1..\MaxBytes]$ | A sequence of bytes, whose size is stored elsewhere or well-known. |
|$\lst{Type}$ | $[1..\MaxTypeSize]$ | Serialized type terms of $\langname$. |
|$\lst{Data}$ | $[1..\MaxDataSize]$ | Serialized data values of $\langname$. |
|$\lst{GroupElement}$ | $33$ | Serialized elements of elliptic curve group. |
|$\lst{SigmaProp}$ | $[1..\MaxSigmaProp]$ | Serialized sigma propositions. |
|$\lst{AvlTree}$ | $44$ | Serialized dynamic dictionary digest. |
|$\lst{Constant}$ | $[1..\MaxConstSize]$ | Serialized $\langname$ constants (values with types). |
|$\lst{Expr}$ | $[1..\MaxExprSize]$ | Serialized expression terms of $\langname$. |
|$\lst{ErgoTree}$ | $[1..\MaxErgoTreeSize]$ | Serialized instances of $\langname$ contracts. |
    
We use the `[1..n]` notation when serialization may produce from **1 to n bytes** (depending on the actual data).

The serialization format of ErgoTree is optimized for compact storage and rapid deserialization.

In many cases, the serialization procedure is *data dependent* and thus has branching logic. 

We use a pseudo-language with operators like `for`, `match`, `if`, and `optional` to express this complex serialization logic in the specification. 

The language allows us to specify a structure composed of simple *serialization slots*. 

Each slot specifies a fragment of the serialized stream of bytes, while operators specify how the slots are combined to form the resulting stream of bytes. 

The notation is summarized in Table 3.

### Table 3: Serialization Notation

|   Notation   | Description |
|---|---|
$\Denot{T}$ where $T$ - type | Denotes a set of values of type $T$  |
$v \in \Denot{T}$ | The value $v$ belongs to the set $\Denot{T}$ |
$v : T$ | Same as $v \in \Denot{T}$ |
$\lst{match}$ $(t, v)$ | Pattern match on pair $(t, v)$ where $t, v$ - values |
$\lst{with}$ $(Unit, v \in \Denot{Unit})$ | Pattern case |
$\lst{for}$ i=1 $\lst{to}$ len \ $~\lst{serialize(}$v_i$\lst{)}$ \\ $\lst{end for}$ | Call the given $\lst{serialize}$ function repeatedly. The output bytes of all invocations are concatenated and become the output of the $\lst{for}$ statement. |
$$\lst{if}~$condition$~$\lst{then}$ | Serialize one of the branches depending on the *condition*. The output bytes of the executed branch become the output of the $\lst{if}$ statement. |
$\lst{serialize1(}$v_1$\lst{)} |  \lst{else} | ~~\lst{serialize2(}$v_2$\lst{)} | \lst{end if}$$ | 

<!--TODO: broken lst-->

In the next section, we describe how types (**Int**, **Coll[Byte]**, etc.) are serialized; then, we define the serialization of typed data. 

This will give us a basis to describe the serialization of Constant nodes of ErgoTree. After that, we will proceed to the serialization of arbitrary ErgoTree trees.

## Type Serialization

For the motivation behind this type of encoding, please see [Appendix D.1](https://raw.githubusercontent.com/ScorexFoundation/sigmastate-interpreter/4daec63275fd4e1364cf7a1132f3e7be6157bb5c/docs/spec/ergotree.pdf).


### Distribution of type codes

The whole space of 256 one-byte codes is divided, as shown in Table 4.

#### Table 4: Distribution of type codes between Data and Function types
|   Value/Interval   | Distribution |
|---|---|
$\lst{0x00}$ | special value to represent undefined type ($\lst{NoType}$ in $\ASDag$) |
$\lst{0x01 - 0x6F(111)}$ | **data types** including primitive types, arrays, options aka nullable types, classes (in future), 111 = 255 - 144 different codes |
$\lst{0x70(112) - 0xFF(255)}$ | **function types** $\lst{T1 => T2}$, 144 = 12 x 12 different codes~\footnote{Note that the function types are never serialized in version 1 of the Ergo protocol, this encoding is reserved for future development of the protocol.} |



### Encoding of Data Types

There are eight different values for *embeddable* types, and three more are reserved for future extensions. Each embeddable type has a type code in the range `1,...,11` as shown in Table 5.



#### Table 5: Embeddable Types

| Code | Type |
|-|-|
| 1 | **Boolean** |
| 2 | **Byte** |
| 3 | **Short** (16-bit) |
| 4 | **Int** (32 bit) |
| 5 | **Long** (64-bit) |
| 6 | **BigInt** (represented by java.math.BigInteger) |
| 7 | **GroupElement** (represented by org.bouncycastle.math.ec.ECPoint) |
| 8 | **SigmaProp** |
| 9 | reserved for **Char** |
| 10 | reserved |
| 11 | reserved |

#### Table 6: Code Ranges of Data Types

| Interval | Constructor | Description |
|---|---|---|
| 0x01 - 0x0B(11) | | embeddable types (including 3 reserved) |
| 0x0C(12) | Coll[_] | | Collection of non-embeddable types (Coll[(Int,Boolean)]) |
| 0x0D(13) - 0x17(23) | Coll[_] | Collection of embeddable types (Coll[Byte], Coll[Int], etc.) |
| 0x18(24) | Coll[Coll[_]] | Nested collection of non-embeddable types (Coll[Coll[(Int,Boolean)]]) |
| 0x19(25) - 0x23(35) | Coll[Coll[_]] | Nested collection of embeddable types (Coll[Coll[Byte]], Coll[Coll[Int]]) |
| 0x24(36) | Option[_] | Option of non-embeddable type (Option[(Int, Byte)]) |
| 0x25(37) - 0x2F(47) | Option[_] | Option of embeddable type (Option[Int]) |
| 0x30(48) | Option[Coll[_]] | Option of Coll of non-embeddable type (Option[Coll[(Int, Boolean)]]) |
| 0x31(49) - 0x3B(59) | Option[Coll[_]] | Option of Coll of embeddable type (Option[Coll[Int]]) |
| 0x3C(60) | (_,_) | Pair of non-embeddable types (((Int, Byte), (Boolean,Box)), etc.) |
| 0x3D(61) - 0x47(71) | (_, Int) | Pair of types where first is embeddable ((_, Int)) |
| 0x48(72) | (_,_,_) | Triple of types |
| 0x49(73) - 0x53(83) | (Int, _) | Pair of types where second is embeddable ((Int, _)) |
| 0x54(84) | (_,_,_,_) | Quadruple of types |
| 0x55(85) - 0x5F(95) | (_, _) | Symmetric pair of embeddable types ((Int, Int), (Byte,Byte), etc.) |
| 0x60(96) | (_,...,_) | Tuple type with more than 4 items (Int, Byte, Box, Boolean, Int) |
| 0x61(97) |  Any | Any type |
| 0x62(98) |  Unit | Unit type |
| 0x63(99) |  Box | Box type |
| 0x64(100) |  AvlTree | AvlTree type |
| 0x65(101) |  Context | Context type |
| 0x66(102) | | reserved for String |
| 0x67(103) | | reserved for TypeVar |
| 0x68(104) |  Header | Header type |
| 0x69(105) |  PreHeader | PreHeader type |
| 0x6A(106) |  Global | Global type |
| 0x6B(107)-0x6E(110) | | reserved for future use |
| 0x6F(111) | | Reserved for future Class type (e.g. user-defined types) |

We use the encoding schema defined below for each type constructor, like **Coll** or **Option**.

- A type constructor has an associated base code which is a multiple of 12 
    - (e.g., 12 for **Coll[_]**, 24 for **Coll[Coll[_]]**, etc.). 
- The base code can be added to the embeddable type code to produce the code of the constructed type. 
    - For example, `12 + 1 = 13` is the code for **Coll[Byte]**. 
    - The code of the type constructor (e.g., 12 in this example) is used when the type parameter is a non-embeddable type (e.g., **Coll[(Byte, Int)]**).
    - In this case, the code of the type constructor is read first, and then recursive descent is performed to read the bytes of the parameter type (in this case, *(Byte, Int)*). 

This encoding allows very simple and fast decoding using **div** and **mod** operations.

Following the above encoding schema, the interval of codes for data types is divided, as shown in Table 6.

### Encoding of Function Types

We use 12 different values for both domain and range types of functions. 

> **This gives us 144 (12∗12) function types in total and allows us to represent 121 (11∗11) functions over primitive types using just a single byte.**

Each code **F** in the range of function types (i.e., **F ∈ {112, . . . , 255}**) can be represented as **F = D∗12+R+112**, where **D, R ∈ {0, . . . , 11}** are the indices of domain and range types correspondingly, and 112 is the first code in the interval of function types.

- If **D = 0**, the domain type is not embeddable, and recursive descent is necessary to write/read the domain type.
- If **R = 0**, then the range type is not embeddable, and recursive descent is necessary to write/read the range type.
 
#### Recursive Descent

When an argument of a type constructor is not a primitive type, we fall back to the simple encoding schema. In this case, we emit the separate code for the type constructor according to the table above and descend recursively to every child node of the type tree.

We perform this descent only for those children whose code cannot be embedded in the parent code.

For example, serialization of **Coll[(Int,Boolean)]** proceeds as follows:

1. Emit **0x0C** because the element type of the collection is not embeddable.
2. Recursively serialize **(Int, Boolean)**.
3. Emit **0x41(=0x3D+4)** because the first type of the pair is embeddable, and its code is **4**.
4. Recursively serialize **Boolean**.
5. Emit **0x02** - the code for the embeddable type **Boolean**.

More examples of type serialization are shown in Table 7.

| Type | D | R | Serialized Bytes | #Bytes | Comments |
|---|-|-|---|--|---|
| Byte | | | 2 | 1 | simple embeddable type |
| Coll[Byte] | | |  12 + 2 = 14 | 1 | embeddable type in Coll |
| Coll[Coll[Byte]] | | |  24 + 2 = 26 | 1 | embeddable type in nested Coll |
| Option[Byte] | | |  36 + 2 = 38 | 1 | embeddable type in Option |
| Option[Coll[Byte]] | | |  48 + 2 = 50 | 1 | embeddable type in Coll nested in Option |
| (Int,Int) | | |  84 + 4 = 88 | 1 | symmetric pair of embeddable type |
| Int=>Boolean | 4 |1 |    161 = 4*12+1+112 | 1 | embeddable domain and range |
| (Int,Int)=>Int | 0 |4|    115=0*12+4+112, 88 | 2 | embeddable range, then symmetric pair |
| (Int,Boolean) | | |  60 + 4, 1 | 2 | Int embedded in pair, then Boolean |
| (Int,Box)=>Boolean |0 |1 |    0*12+1+112, 60+4, 99 | 3 | func with embedded range, then Int embedded, then Box |
    

### Data Serialization

In ErgoTree, all runtime data values have an associated type also available at runtime (this is called [*type reification*](https://en.wikipedia.org/wiki/Reification_(computer_science))). 

However, the serialization format separates data values from their type descriptors. This saves space when, for example, a collection of items is serialized. This is done so that a type tree can fully describe the contents of a typed data structure. 

For example, having a typed data object **d: (Int, Coll[Byte], Boolean)**, we can tell, by examining the structure of the type, that **d** is a tuple with three items; the first item contains a *32-bit integer*, the second a collection of *bytes*, and the third a logical *true/false* value.

To serialize/deserialize typed data, we need to know its type descriptor (type tree). The data serialization procedure is recursive over the type tree and the corresponding sub-components of the data object. For primitive types (the leaves of the type tree), the format is fixed. The data values of ErgoTree types are serialized according to the predefined recursive function shown in Figure 5, which uses the notation from Table 3.

<!--TODO-->
Figure 5: Data serialization format

#### GroupElement serialization

A value of the GroupElement type is represented in the reference implementation using the `SecP256K1Point` class of the `org.bouncycastle.math.ec.custom.sec` package and serialized using **ASN.1** encoding. 

Different encodings are considered during deserialization, including point compression for Fp (see X9.62 sec. 4.2.1 pg. 17).

<!--TODO-->
Figure 6: GroupElement serialization format

#### SigmaProp serialization

In the reference implementation, values of the **SigmaProp** type are serialized using `SigmaBoolean.serializer`.

#### AvlTree serialization

In the reference implementation, values of the **AvlTree** type are serialized using `AvlTreeData.serializer`.

<!--TODO-->
Figure 8: AvlTree serialization format

### Constant Serialization

The **Constant** format is simple and self-sufficient to represent any data value. Serialized bytes in the Constant format contain both the **type bytes** and the **data bytes**; thus, they can be stored or transferred over the wire and then later unambiguously interpreted. The format is shown in Figure 9.

Figure 9: Constant serialization format

To parse the **Constant** format, first, use the type serializer from section 5.1 and read the type. Then use the parsed type as an argument of the data serializer given in section 5.2.

### Expression Serialization

Expressions of ErgoTree are serialized as tree data structures using the recursive procedure described in Figure 10. Expression nodes are represented in the reference implementation using the `Value` class hierarchy.

### ErgoTree serialization

The ErgoTree propositions stored in UTXO boxes are represented in the reference implementation using the `ErgoTree` class. The class is serialized using the ErgoTree serialization format shown in Figure 11.

Figure 11: ErgoTree serialization format

Serialized instances of the `ErgoTree` class are self-sufficient and can be stored and passed around.

The ErgoTree format defines the top-level serialization format of ErgoTree scripts. The interpretation of the byte array depends on the first header byte(s), which use VLQ encoding (up to 30 bits are reserved). We currently define meaning only for the first byte, which may be extended in future versions. The meaning of the bits is shown in Figure 12.

Figure 12: ErgoTree header bits

Currently, we don’t specify interpretation for the second and other bytes of the header. We reserve the possibility to extend the header by using **Bit 7 == 1** and chaining additional bytes as in **VLQ**.

Once new bytes are required, a new language version should be created and implemented via soft-forkability. That new language will give an interpretation for the new bytes.

The default behavior of ErgoTreeSerializer is to preserve the original structure of ErgoTree and check consistency. In case of any inconsistency, the serializer throws an exception.

If the constant segregation bit (Bit 4) is set to 1, then the constants collection contains the constants for which there may be `ConstantPlaceholder` nodes in the tree. However, if the constant segregation bit is 0, then the constants collection should be empty, and any placeholder in the tree will lead to an exception.
