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

- *Description*: Converts this numeric value to **Byte**, throwing exception if overflow.
- *Signature*: **`def toByte: Byte`**
- *Serialized as:* Downcast

#### Byte.toShort (106.2)

- *Description*: Converts this numeric value to Short, throwing exception if overflow.
- *Signature*: **`def toShort: Short`**
- *Serialized as:* Upcast

#### Byte.toInt (106.3)

- *Description*: Converts this numeric value to Int, throwing exception if overflow.
- *Signature*: **`def toInt: Int`**
- *Serialized as:* Upcast

#### Byte.toLong (106.4)

- *Description*: Converts this numeric value to Long, throwing exception if overflow.
- *Signature*: **`def toLong: Long`**
- *Serialized as:* Upcast

#### Byte.toBigInt (106.5)

- *Description*: Converts this numeric value to BigInt
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Upcast


### Short 

#### Short.toByte (106.1)

- *Description*: Converts this numeric value to Byte, throwing exception if overflow.
- *Signature*: **`def toByte: Byte`**
- *Serialized as:* Downcast

#### Short.toShort (106.2)

- *Description*: Converts this numeric value to Short, throwing exception if overflow.
- *Signature*: **`def toShort: Short`**
- *Serialized as:* Downcast

#### Short.toInt (106.3)

- *Description*: Converts this numeric value to Int, throwing exception if overflow.
- *Signature*: **`def toInt: Int`**
- *Serialized as:* Downcast

#### Short.toLong (106.4)

- *Description*: Converts this numeric value to Long, throwing exception if overflow.
- *Signature*: **`def toLong: Long`**
- *Serialized as:* Upcast


#### Short.toBigInt (106.5)

- *Description*: Converts this numeric value to BigInt
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Upcast

### Int 

#### Int.toByte (106.1)

- *Description*: Converts this numeric value to Byte, throwing exception if overflow.
- *Signature*: **`def toByte: Byte`**
- *Serialized as:* Downcast


#### Int.toShort (106.2)

- *Description*: Converts this numeric value to Short, throwing exception if overflow.
- *Signature*: **`def toShort: Short`**
- *Serialized as:* Downcast

#### Int.toInt (106.3)

- *Description*: Converts this numeric value to Int, throwing exception if overflow.
- *Signature*: **`def toInt: Int`**
- *Serialized as:* Downcast

#### Int.toLong (106.4)

- *Description*: Converts this numeric value to Long, throwing exception if overflow.
- *Signature*: **`def toLong: Long`**
- *Serialized as:* Upcast

#### Int.toBigInt (106.5)

- *Description*: Converts this numeric value to BigInt.
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Upcast

### Long 

#### Long.toByte (106.1)

- *Description*: Converts this numeric value to Byte, throwing exception if overflow.
- *Signature*: **`def toByte: Byte`**
- *Serialized as:* Downcast

#### Long.toShort (106.2)

- *Description*: Converts this numeric value to Short, throwing exception if overflow.
- *Signature*: **`def toShort: Short`**
- *Serialized as:* Downcast

#### Long.toInt (106.3)

- *Description*: Converts this numeric value to Int, throwing exception if overflow.
- *Signature*: **`def toInt: Int`**
- *Serialized as:* Downcast

#### Long.toLong (106.4)

- *Description*: Converts this numeric value to Long, throwing exception if overflow.
- *Signature*: **`def toLong: Long`**
- *Serialized as:* Downcast

#### Long.toBigInt (106.5)

- *Description*: Converts this numeric value to BigInt
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Upcast


### BigInt 

#### BigInt.toBigInt (106.5)

- *Description*: Converts this numeric value to BigInt
- *Signature*: **`def toBigInt: BigInt`**
- *Serialized as:* Downcast


### GroupElement 

#### GroupElement.getEncoded (7.2)

- *Description*: Get an encoding of the point value.
- *Signature*: **`def getEncoded: Coll[Byte]`**
- *Serialized as:* PropertyCall

#### GroupElement.exp (7.3)

- *Description*: Exponentiate this GroupElement to the given number. Returns this to the power of k
- *Signature*: **`def exp(k: BigInt): GroupElement`**
- - *Parameters*: `k` The power
- *Serialized as:* Exponentiate

#### GroupElement.multiply (7.4)

- *Description*: Group operation.
- *Signature*: **`def multiply(other: GroupElement): GroupElement`**
- *Parameters*: `other` other element of the group
- *Serialized as:* MultiplyGroup

#### GroupElement.negate (76.5)

- *Description*: Inverse element of the group.
- *Signature*: **`def negate: GroupElement`**
- *Serialized as:* PropertyCall


### SigmaProp 

Values of **SigmaProp** type hold sigma propositions, which can be proved and verified using Sigma protocols. Each sigma proposition is represented as an expression where sigma protocol primitives such as **ProveDlog**, and **ProveDHTuple** are used as constants and special sigma protocol connectives like **&&**,**||** and **THRESHOLD** are used as operation.

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

- *Description*: Serialized bytes of this sigma proposition taken as ErgoTree.
- *Parameters*: 
- *Result*: `Coll[Byte]`
- *Serialized as:* SigmaPropBytes

#### SigmaProp.isProven (8.2)

- *Description*: Verify that sigma proposition is proven. (FRONTEND ONLY)
- *Parameters*: 
- *Result*: `Boolean`

For a full list of primitive operations on  $\lst{SigmaProp}$ type, see [Appendix B](https://raw.githubusercontent.com/ScorexFoundation/sigmastate-interpreter/fada073b82a16a928c457693b888da4c0310aca6/docs/spec/spec.pdf#appendix.B)

### Box 


#### Box.value (99.1)

- *Description*: Mandatory: Monetary value, in Ergo tokens (NanoErg unit of measure
- *Parameters*: 
- *Result*: $\lst{Long}$
- *Serialized as:* ExtractAmount

#### Box.propositionBytes (99.2)

- *Description*: Serialized bytes of guarding script, which should be evaluated to true in order
to open this box. (aka spend it in a transaction)
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* ExtractScriptBytes

#### Box.bytes (99.3)

- *Description*: Serialized bytes of this box’s content, including proposition bytes.
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* ExtractBytes

#### Box.bytesWithoutRef (99.4)

- *Description*: Serialized bytes of this box’s content, excluding transactionId and index of
output.
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* ExtractBytesWithNoRef

#### Box.value (99.5)

- *Description*: Blake2b256 hash of this box’s content, basically equals to blake2b256(bytes).
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* ExtractId

#### Box.creationInfo (99.6)

- *Description*: If tx is a transaction which generated this box, then $\lst{creationInfo._1}$ is a height of the tx’s block. The $\lst{creationInfo._2}$ is a serialized transaction identifier followed by box index in the transaction outputs.
- *Parameters*: 
- *Result*: $\lst{(Int,Coll[Byte])}$
- *Serialized as:* ExtractCreationInfo

#### Box.getReg (99.7)

- *Description*: Extracts register by id and type. Type param T expected type of the register. Returns Some(value) if the register is defined and has given type and None otherwise
- *Parameters*: $\lst{regId : Int}$ // zero-based identifier of the register.
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.tokens (99.8)

- *Description*: Secondary tokens.
- *Parameters*: 
- *Result*: $\lst{Coll[(Coll[Byte],Long)]}$
- *Serialized as:* PropertyCall

#### Box.R0 (99.9)

- *Description*: Monetary value, in Ergo tokens. 
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.value (99.10)

- *Description*: Guarding script
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.value (99.11)

- *Description*: Secondary tokens.
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R3 (99.12)

- *Description*: Reference to transaction and output id where the box was created
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R4 (99.13)

- *Description*: Non-mandatory register.
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R5 (99.14)

- *Description*: Non-mandatory register.
- *Parameters*: 
- *Result*: $\lst{Option[T]}$
- *Serialized as:* ExtractRegisterAs

#### Box.R6 (99.15)

- *Description*: Mandatory: Monetary value, in Ergo tokens (NanoErg unit of measure
- *Parameters*: 
- *Result*: $\lst{Long}$
- *Serialized as:* ExtractRegisterAs

#### Box.R7 (99.16)

- *Description*: Mandatory: Monetary value, in Ergo tokens (NanoErg unit of measure
- *Parameters*: 
- *Result*: $\lst{Long}$
- *Serialized as:* ExtractRegisterAs

#### Box.R8 (99.17)

- *Description*: Mandatory: Monetary value, in Ergo tokens (NanoErg unit of measure
- *Parameters*: 
- *Result*: $\lst{Long}$
- *Serialized as:* ExtractRegisterAs

#### Box.R9 (99.18)

- *Description*: Mandatory: Monetary value, in Ergo tokens (NanoErg unit of measure
- *Parameters*: 
- *Result*: $\lst{Long}$
- *Serialized as:* ExtractRegisterAs

### AvlTree 

#### AvlTree.digest (100.1)

- *Description*: Returns digest of the state represented by this tree. Authenticated tree $\lst{digest = root hash bytes ++ tree height}$
- *Parameters*: 
- *Result*: $\lst{Coll[Byte]}$
- *Serialized as:* PropertyCall

#### AvlTree.enabledOperations (100.2)

- *Description*: Flags of enabled operations packed in single byte.
- *Parameters*: 
- *Result*: $\lst{Byte}$
- *Serialized as:* PropertyCall

```
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
