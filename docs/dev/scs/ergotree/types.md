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
\newcommand{\Set}[1]{\{ #1 \}}
$$

# Predefined types


### Boolean

### Byte 

#### Byte.toByte (106.1)

- *Description*: Converts this numeric value to **Byte**, throwing an exception on overflow.
- *Signature*: **`def toByte: Byte`**
- *Serialized as:* Downcast

#### Byte.toShort (106.2)

- *Description*: Converts this numeric value to **Short**, throwing an exception on overflow.
- *Signature*: **`def toShort: Short`**
- *Serialized as:* Upcast

#### Byte.toInt (106.3)

- *Description*: Converts this numeric value to **Int**, throwing an exception on overflow.
- *Signature*: **`def toInt: Int`**
- *Serialized as:* Upcast

#### Byte.toLong (106.4)

- *Description*: Converts this numeric value to **Long**, throwing an exception on overflow.
- *Signature*: **`def toLong: Long`**
- *Serialized as:* Upcast

#### Byte.toBigInt (106.5)

- *Description*: Converts this numeric value to **BigInt**.
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Upcast


### Short 

#### Short.toByte (106.1)

- *Description*: Converts this numeric value to **Byte**, throwing an exception on overflow.
- *Signature*: **`def toByte: Byte`**
- *Serialized as:* Downcast

#### Short.toShort (106.2)

- *Description*: Converts this numeric value to **Short**, throwing an exception on overflow.
- *Signature*: **`def toShort: Short`**
- *Serialized as:* Downcast

#### Short.toInt (106.3)

- *Description*: Converts this numeric value to **Int**, throwing an exception on overflow.
- *Signature*: **`def toInt: Int`**
- *Serialized as:* Downcast

#### Short.toLong (106.4)

- *Description*: Converts this numeric value to **Long**, throwing an exception on overflow.
- *Signature*: **`def toLong: Long`**
- *Serialized as:* Upcast


#### Short.toBigInt (106.5)

- *Description*: Converts this numeric value to **BigInt**.
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Upcast

### Int 

#### Int.toByte (106.1)

- *Description*: Converts this numeric value to **Byte**, throwing an exception on overflow.
- *Signature*: **`def toByte: Byte`**
- *Serialized as:* Downcast


#### Int.toShort (106.2)

- *Description*: Converts this numeric value to **Short**, throwing an exception on overflow.
- *Signature*: **`def toShort: Short`**
- *Serialized as:* Downcast

#### Int.toInt (106.3)

- *Description*: Converts this numeric value to **Int**, throwing an exception on overflow.
- *Signature*: **`def toInt: Int`**
- *Serialized as:* Downcast

#### Int.toLong (106.4)

- *Description*: Converts this numeric value to **Long**, throwing an exception on overflow.
- *Signature*: **`def toLong: Long`**
- *Serialized as:* Upcast

#### Int.toBigInt (106.5)

- *Description*: Converts this numeric value to **BigInt**.
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Upcast

### Long 

#### Long.toByte (106.1)

- *Description*: Converts this numeric value to **Byte**, throwing an exception on overflow.
- *Signature*: **`def toByte: Byte`**
- *Serialized as:* Downcast

#### Long.toShort (106.2)

- *Description*: Converts this numeric value to **Short**, throwing an exception on overflow.
- *Signature*: **`def toShort: Short`**
- *Serialized as:* Downcast

#### Long.toInt (106.3)

- *Description*: Converts this numeric value to **Int**, throwing an exception on overflow.
- *Signature*: **`def toInt: Int`**
- *Serialized as:* Downcast

#### Long.toLong (106.4)

- *Description*: Converts this numeric value to **Long**, throwing an exception on overflow.
- *Signature*: **`def toLong: Long`**
- *Serialized as:* Downcast

#### Long.toBigInt (106.5)

- *Description*: Converts this numeric value to **BigInt**.
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Upcast


### BigInt 

#### BigInt.toBigInt (106.5)

- *Description*: Converts this numeric value to **BigInt**.
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Downcast


### GroupElement 

#### GroupElement.getEncoded (7.2)

- *Description*: Returns an encoding of the point value.
- *Signature*: **`def getEncoded: Coll[Byte]`**
- *Serialized as:* PropertyCall

#### GroupElement.exp (7.3)

- *Description*: Exponentiates this GroupElement to the given number. Returns this group element raised to the power of k.
- *Signature*: **`def exp(k: BigInt): GroupElement`**
- *Parameters*: `k` The power
- *Serialized as:* Exponentiate

#### GroupElement.multiply (7.4)

- *Description*: Performs the group operation (multiplication) with another element.
- *Signature*: **`def multiply(other: GroupElement): GroupElement`**
- *Parameters*: `other` The other element of the group.
- *Serialized as:* MultiplyGroup

#### GroupElement.negate (7.5)

- *Description*: Returns the inverse element in the group.
- *Signature*: **`def negate: GroupElement`**
- *Serialized as:* PropertyCall


### SigmaProp 

Values of **SigmaProp** type hold sigma propositions, which can be proved and verified using Sigma protocols. Each sigma proposition is represented as an expression where sigma protocol primitives such as **ProveDlog** and **ProveDHTuple** are used as constants, and special sigma protocol connectives like **AND**, **OR**, and **THRESHOLD** are used as operations.

The abstract syntax of sigma propositions is shown below.


| Set | | Syntax | Mnemonic | Description |
|--||--|--|----|
| $Tree \ni t$	| := 	| $\lst{Trivial(b)}$ 	| $\lst{TrivialProp}$	| boolean value $\lst{b}$ as sigma proposition  
|   | $\mid$	| $\lst{Dlog(ge)}$ 	| $\lst{ProveDLog}$	| knowledge of discrete logarithm of $\lst{ge}$
|   | $\mid$    | $\lst{DHTuple(g,h,u,v)}$ 	| $\lst{ProveDHTuple}$	| knowledge of Diffie-Hellman tuple 
|   | $\mid$    | $\lst{THRESHOLD}(k,t_1,\dots,t_n)$ 	| $\lst{THRESHOLD}$	| knowledge of $k$ out of $n$ secrets
|   | $\mid$    | $\lst{OR}(t_1,\dots,t_n)$	| $\lst{OR}$	| knowledge of any one of $n$ secrets
|   | $\mid$    | $\lst{AND}(t_1,\dots,t_n)$	| $\lst{AND}$	| knowledge of all $n$ secrets


Every well-formed tree of sigma proposition is a value of type $\lst{SigmaProp}$, thus following the notation of the [evaluation section](evaluation.md) we can define denotation of $\lst{SigmaProp}$

$$\Denot{\lst{SigmaProp}} = \Set{t \in Tree}$$


The following methods can be called on all instances of $\lst{SigmaProp}$ type.

#### SigmaProp.propBytes (8.1)

- *Description*: Returns the serialized bytes of this sigma proposition represented as ErgoTree.
- *Parameters*: 
- *Result*: `Coll[Byte]`
- *Serialized as:* SigmaPropBytes

#### SigmaProp.isProven (8.2)

- *Description*: Verifies that the sigma proposition is proven. (FRONTEND ONLY)
- *Parameters*: 
- *Result*: `Boolean`

For a full list of primitive operations on  $\lst{SigmaProp}$ type, see [Appendix B](https://raw.githubusercontent.com/ScorexFoundation/sigmastate-interpreter/fada073b82a16a928c457693b888da4c0310aca6/docs/spec/spec.pdf#appendix.B)

### Box 


#### Box.value (99.1)

- *Description*: Monetary value in nanoErgs.
- *Parameters*: 
- *Result*: $\lst{Long}$
- *Serialized as:* ExtractAmount

#### Box.propositionBytes (99.2)

- *Description*: Serialized bytes of the guarding script. This script must evaluate to true to spend the box.
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* ExtractScriptBytes

#### Box.bytes (99.3)

- *Description*: Returns the serialized bytes of this box's content, including proposition bytes.
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* ExtractBytes

#### Box.bytesWithoutRef (99.4)

- *Description*: Returns the serialized bytes of this box's content, excluding the transactionId and output index.
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* ExtractBytesWithNoRef

#### Box.id (99.5)

- *Description*: Returns the Blake2b256 hash of this box's content (`blake2b256(bytes)`).
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* ExtractId

#### Box.creationInfo (99.6)

- *Description*: Returns the height and transaction/output index where the box was created. `creationInfo._1` is the block height, and `creationInfo._2` is the transaction identifier concatenated with the box index.
- *Parameters*: 
- *Result*: $\lst{(Int,Coll[Byte])}$
- *Serialized as:* ExtractCreationInfo

#### Box.getReg (99.7)

- *Description*: Extracts register `regId` by ID and expected type `T`. Returns `Some(value)` if the register exists and has the specified type, `None` otherwise.
- *Parameters*: $\lst{regId : Int}$ // zero-based identifier of the register.
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.tokens (99.8)

- *Description*: Returns the collection of secondary tokens held in the box.
- *Parameters*: 
- *Result*: $\lst{Coll[(Coll[Byte],Long)]}$
- *Serialized as:* PropertyCall

#### Box.R0 (99.9)

- *Description*: Register R0: Monetary value in nanoErgs. Use `ExtractAmount` (value property).
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R1 (99.10)

- *Description*: Register R1: Guarding script bytes. Use `ExtractScriptBytes` (propositionBytes property).
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R2 (99.11)

- *Description*: Register R2: Secondary tokens [(TokenId, Amount)]. Use `ExtractTokens` (tokens property).
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R3 (99.12)

- *Description*: Register R3: Box creation information (height, txId, index). Use `ExtractCreationInfo` (creationInfo property).
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R4 (99.13)

- *Description*: Optional register R4 for arbitrary data storage. Use `ExtractRegisterAs`.
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R5 (99.14)

- *Description*: Optional register R5 for arbitrary data storage. Use `ExtractRegisterAs`.
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R6 (99.15)

- *Description*: Optional register R6 for arbitrary data storage. Use `ExtractRegisterAs`.
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R7 (99.16)

- *Description*: Optional register R7 for arbitrary data storage. Use `ExtractRegisterAs`.
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R8 (99.17)

- *Description*: Optional register R8 for arbitrary data storage. Use `ExtractRegisterAs`.
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R9 (99.18)

- *Description*: Optional register R9 for arbitrary data storage. Use `ExtractRegisterAs`.
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

### AvlTree 

#### AvlTree.digest (100.1)

- *Description*: Returns the digest of the state represented by this tree (root hash bytes ++ tree height).
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* PropertyCall

#### AvlTree.enabledOperations (100.2)

- *Description*: Returns the flags of enabled operations packed into a single byte.
- *Parameters*: 
- *Result*: $\lst{Byte}$
- *Serialized as:* PropertyCall

```scala
isInsertAllowed == (enabledOperations & 0x01) != 0
isUpdateAllowed == (enabledOperations & 0x02) != 0
isRemoveAllowed == (enabledOperations & 0x04) != 0
```

#### AvlTree.keyLength (100.3)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Int}$
- *Serialized as:* PropertyCall

#### AvlTree.valueLengthOpt (100.4)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* PropertyCall

#### AvlTree.isInsertAllowed (100.5)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* PropertyCall

#### AvlTree.isUpdateAllowed (100.6)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Boolean}$
- *Serialized as:* PropertyCall

#### AvlTree.isRemovedAllowed (100.7)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Boolean}$
- *Serialized as:* PropertyCall

#### AvlTree.updateOperations (100.8)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{AvlTree}$
- *Serialized as:* MethodCall

#### AvlTree.contains (100.9)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Boolean}$
- *Serialized as:* MethodCall

#### AvlTree.get (100.10)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Option[Coll[Byte]]}$
- *Serialized as:* MethodCall

#### AvlTree.getMeny (100.11)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Coll[Option[Coll[Byte]]]}$
- *Serialized as:* MethodCall

#### AvlTree.insert (100.12)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Option[AvlTree]}$
- *Serialized as:* MethodCall

#### AvlTree.update (100.13)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{Option[AvlTree]}$
- *Serialized as:* MethodCall

#### AvlTree.remove (100.14)

- *Description*:
- *Parameters*: 
- *Result*: $\lst{Option[AvlTree]}$
- *Serialized as:* MethodCall

#### AvlTree.updateDigest (100.15)

- *Description*: 
- *Parameters*: 
- *Result*: $\lst{AvlTree}$
- *Serialized as:* MethodCall

### Header 

### PreHeader 

### Context 

### Global 

### Coll 

### Option
