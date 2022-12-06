# Serialization

> This page is a WIP. Please see [ErgoTree.pdf](https://storage.googleapis.com/ergo-cms-media/docs/ErgoTree.pdf) for full details.

> This section defines a binary format used to store ErgoTree contracts in persistent stores, transfer them over the wire, and enable cross-platform interoperation.

The terms of the language described in [Section 2] can be serialized to an array of bytes to be stored in the Ergo blockchain (e.g., **Box.propositionBytes**).

When the guarding script of an input box of a transaction is validated, the **propositionBytes** array is deserialized to an ErgoTree IR (represented by the ErgoTree class), which can be evaluated as it is specified in [Section 4].

Here we specify the serialization procedure in general. The serialization format of ErgoTree types (**SType** class) and nodes (**Value** class) is correspondingly specified in [section 5.1] and [Appendix C].

The table below shows size limits checked during contract deserialization, which is important to resist malicious script attacks.

## Table 1: Serialization limits

| Constant | Value | Description |
|---|---|---|
| VLQ <sub> max </sub> | 10 | Maximum size of VLQ encoded byte sequence (See VLQ formats E.1) |
| T <sub> max </sub> | 100 | Maximum size of serialized type term (see Type format 5.1) |
| D <sub> max </sub> | 4Kb | Maximum size of serialized data instance (see Data format 5.2) |
| C <sub> max </sub> | = T <sub> max </sub> + D <sub> max </sub> | Maximum size of serialized data instance (see Const format 5.3) |
| Expr <sub> max </sub> | 4Kb | Maximum size of serialized ErgoTree term (see Expr format 5.4) |
| ErgoTree <sub> max </sub> | 4Kb | Maximum size of serialized ErgoTree contract (see ErgoTree format 5.5) |


All the serialization formats used and defined throughout this section are listed in Table 2, which introduces a name for each format and shows the number of bytes each format may occupy in the byte stream.

## Table 2: Serialization formats

The serialization format of ErgoTree is optimized for compact storage and rapid deserialization.

We use the `[1..n]` notation when serialization may produce from **1 to n bytes** (depending on the actual data).

In many cases, the serialization procedure is *data dependent* and thus has branching logic. 

We use a pseudo-language with operators like **for**, **match**, **if**, and **optional ** to express this complex serialization logic in the specification. 

The language allows us to specify a structure out of simple *serialization slots*. 

Each slot specifies a fragment of the serialized stream of bytes, whereas operators specify how the slots are combined to form the resulting stream of bytes. 

The notation is summarized in Table 3.

## Table 3: Serialization Notation

In the next section, we describe how types (**Int**, **Coll[Byte]**, etc.) are serialized; then, we define the serialization of typed data. 

This will give us a basis to describe the serialization of Constant nodes of ErgoTree. After that, we will proceed to the serialization of arbitrary ErgoTree trees.

## Type Serialization

For the motivation behind this type of encoding, please see [Appendix D.1].

### Distribution of type codes

The whole space of 256 one-byte codes is divided, as shown in [Figure 4].

#### Table 4: Distribution of type codes between Data and Function types



### Encoding of Data Types

There are eight different values for *embeddable* types, and three more are reserved for future extensions. Each embeddable type has a type code in the range `1,...,11` as shown in [Figure 5].



#### Table 5: Embeddable Types

| Code | Type |
|-|-|
| 1 | Boolean |
| 2 | Byte |
| 3 | Short (16-bit) |
| 4 | Int (32 bit) |
| 5 | Long (64-bit) |
| 6 | BigInt (represented by java.math.BigInteger) |
| 7 | GroupElement (represented by org.bouncycastle.math.ec.ECPoint) |
| 8 | SigmaProp |
| 9 | reserved for Char |
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
| 0x48(72) | (_,_,_) | Triple of types 
| 0x49(73) - 0x53(83) | (Int, _) | Pair of types where second is embeddable ((Int, _)) |
| 0x54(84) | (_,_,_,_) | Quadruple of types |
| 0x55(85) - 0x5F(95) | (_, _) | Symmetric pair of embeddable types ((Int, Int), (Byte,Byte), etc.) |
| 0x60(96) | (_,...,_) | Tuple type with more than 4 items (Int, Byte, Box, Boolean, Int) |
| 0x61(97) |  Any | Any type 
| 0x62(98) |  Unit | Unit type |
| 0x63(99) |  Box | Box type |
| 0x64(100) |  AvlTree | AvlTree type 
| 0x65(101) |  Context | Context type 
| 0x66(102) | | reserved for String 
| 0x67(103) | | reserved for TypeVar 
| 0x68(104) |  Header | Header type 
| 0x69(105) |  PreHeader | PreHeader type 
| 0x6A(106) |  Global | Global type 
| 0x6B(107)-0x6E(110) | | reserved for future use 
| 0x6F(111) | | Reserved for future Class type (e.g. user-defined types) 

We use the encoding schema defined below for each type of constructor, like **Coll** or **Option**.

- Type constructor has an associated base code which is a multiple of 12 
    - (e.g. 12 for **Coll[_]**, 24 for **Coll[Coll[_]]**, etc.). 
- The base code can be added to the embeddable type code to produce the code of the constructed type. 
    - For example `12 + 1 = 13` is a code of **Coll[Byte]**. 
    - The code of the type constructor (e.g. 12 in this example) is used when the type parameter is non-embeddable type (e.g. **Coll[(Byte, Int)]**).
    - In this case, the code of the type constructor is read first, and then recursive descent is performed to read bytes of the parameter type (in this case *(Byte, Int)*). 

This encoding allows very simple and fast decoding using **div** and **mod** operations.

Following the above encoding schema, the interval of codes for data types is divided, as shown in Table 6

### Encoding of Function Types

We use 12 different values for both domain and range types of functions. 

> **This gives us 144 (12∗12) function types in total and allows us to represent 121 (11∗11) functions over primitive types using just a single byte.**

Each code **F** in a range of the function types (i.e. **F ∈ {112, . . . , 255}**) can be represented as **F = D∗12+R+112**, where **D, R ∈ {0, . . . , 11}** - indices of domain and range types correspondingly, 112 - is the first code in an interval of function types.

- If **D = 0**, the domain type is not embeddable, and the recursive descent is necessary to write/read the domain type.
- If **R = 0**, then the range type is not embeddable, and the recursive descent is necessary to write/read the range type.
 
#### Recursive Descent

When an argument of a type constructor is not a primitive type, we fall back to the simple encoding schema, in which case we emit the separate code for the type constructor according to the table above and descend recursively to every child node of the type tree.

We do this descend only for those children whose code cannot be embedded in the parent code.

For example, serialization of **Coll[(Int,Boolean)]** proceeds as the following:

1. Emit **0x0C** because the elements type of the collection is not embeddable
2. Recursively serialize **(Int, Boolean)**
3. Emit **0x41(=0x3D+4)** because the first type of the pair is embeddable, and its code is **4**
4. Recursively serialize **Boolean**
5. Emit **0x02** - the code for embeddable type **Boolean**

More examples of type serialization are shown in Table 7

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
| (Int,Box)=>Boolean |0 |1 |    0*12+1+112, 60+4, 99 | 3 func with embedded range, then Int embedded, then Box |
    

### Data Serialization

In ErgoTree, all runtime data values have an associated type also available at runtime (this is called [*type reification*](https://en.wikipedia.org/wiki/Reification_(computer_science))). 

However, the serialization format separates data values from their type descriptors. This saves space when for example, a collection of items is serialized. It is done so that a type tree can fully describe the contents of a typed data structure. 

For example, having a typed data object **d: (Int, Coll[Byte], Boolean)**, we can tell, by examining the structure of the type, that **d** is a tuple with three items; the first item contains a *32-bit integer*, the second - a collection of *bytes*, and the third - logical *true/false* value.

To serialize/deserialize typed data, we need to know its type descriptor (type tree). The data serialization procedure is recursive over a type tree and the corresponding sub-components of the data object. For primitive types (the leaves of the type tree), the format is fixed. The data values of ErgoTree types are serialized according to the predefined recursive function shown in Figure 5
which uses the notation from Table 3.

Figure 5: Data serialization format

#### GroupElement serialization

A value of the GroupElement type is represented in reference implementation using **SecP256K1Point** class of the `org.bouncycastle.math.ec.custom.sec` package and serialized into **ASN.1** encoding. 

The different encodings are considered during deserialization, including point compression for Fp (see X9.62 sec. 4.2.1 pg. 17).

Figure 6: GroupElement serialization format

#### SigmaProp serialization

In reference implementation values of the **SigmaProp** type are serialized using **SigmaBoolean. serializer**.

#### AvlTree serialization

In reference, implementation values of the **AvlTree** type are serialized using **AvlTreeData. serializer**.

Figure 8: AvlTree serialization format

### Constant Serialization

The **Constant** format is simple and self-sufficient to represent any data value. Serialized bytes of the Constant format contain both the **type bytes** and the **data bytes**; thus, they can be stored or wire transferred and then later unambiguously interpreted. The format is shown in Figure 9

Figure 9: Constant serialization format

To parse the **Constant** format, first, use the type serializer from section [5.1] and read the type. Then use the parsed type as an argument of the data serializer given in section [5.2]

### Expression Serialization

Expressions of ErgoTree are serialized as tree data structures using the recursive procedure described in [Figure 10]. Expression nodes are represented in the reference implementation using the **Value** class.

### ErgoTree serialization

The ErgoTree propositions stored in UTXO boxes are represented in the reference implementation using ErgoTree class. The class is serialized using the ErgoTree serialization format shown in [Figure 11].

Figure 11: ErgoTree serialization format

Serialized instances of ErgoTree class are self-sufficient and can be stored and passed around.

ErgoTree format defines the top-level serialization format of ErgoTree scripts. The interpretation of the byte array depends on the first header bytes, which use VLQ encoding up to 30 bits. We define meaning for only the first byte, which may be extended in future versions. The meaning of the bits is shown in [Figure 12].

Figure 12: ErgoTree header bits

Currently, we don’t specify interpretation for the second and other bytes of the header. We reserve the possibility to extend the header by using **Bit 7 == 1** and chain additional bytes as in **VLQ**.

Once the new bytes are required, a new language version should be created and implemented via soft-forkability. That new language will give an interpretation for the new bytes.

The default behavior of ErgoTreeSerializer is to preserve the original structure of ErgoTree and check the consistency. In case of any inconsistency, the serializer throws an exception.

If constant segregation Bit4 is set to 1, then the constants collection contains the constants for which there may be ConstantPlaceholder nodes in the tree. However, if the constant segregation bit is 0, then the constants collection should be empty, and any placeholder in the tree will lead to an exception.