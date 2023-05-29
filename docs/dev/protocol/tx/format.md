---
tags:
  - Box
---

# Box Format

A box is made of **registers** *(and nothing but registers!)*; we allow every box in the system to have up to 10 registers. We denote the [registers](registers.md) as $R_0,R_1,...,R_9$. From these registers, four are filled with mandatory values: $R_0$ contains the monetary value of a box, $R_1$ contains serialized guard script, $R_2$ contains tokens, $R_3$ contains declared creation height, unique identifier of transaction which created the coin and also an index of the box in the transaction.

The term 'box' in Ergo's context captures the idea that these entities are like containers holding various types of information (value, tokens, custom data, etc.), beyond just the unspent transaction output balance. This makes the boxes in Ergo significantly more flexible and functional, enabling more complex operations, such as running scripts or smart contracts, directly on the blockchain.

Each register is an expression in the sigma language. Thus the registers are typed: every register contains a value of some type. Types are defined [here](types.md). The value should be evaluated (i.e. it should be a concrete constant value, not a function of a known output type).

We introduce the $extract({})$ function, which reads the contents of a register, for example, $extract({c, R_0})$ extracts monetary value from the box $c$.

Box bytes used to obtain the box identifier, build authenticated tree for the state, and build a transaction, are to be formed as follows:

-   *monetary value.* We use VLQ-encoded unsigned long value to store the monetary value of the box
-   *bytes of a script.* To see how the script is serialized, see (TODO). The script is to be represented as register R1 by wrapping its bytes in a constant array of constant bytes.
-   *creation height* VLQ-encoded unsigned integer value
-   *number of tokens* which box is carrying. Represented as a one-byte unsigned integer.
-   *tokens*. A box can carry multiple tokens. A single record in this field is represented as a tuple $token\_identifier -> amount$, where the identifier is 32 bytes, and the amount is a VLQ-encoded integer.
-   *number of additional registers.* Extra registers should come in order (R4, \..., etc.), so this number, represented as a 1-byte unsigned value, defines how much longer non-empty registers are coming after mandatory ones. If the number is zero, the next field is missed.
-   *additional registers.* Extra registers are serialized without any delimiters. Each register is serialized as a sigma expression.
-   *transaction identifier.* 32-byte long identifier of a transaction which created the box 
-   *index of a transaction output.* VLQ-encoded index of the box in the transaction outputs.

### Box candidate

Here we describe the difference between a box and a box candidate. A box has a unique identifier to be defined deterministically from its contents. Thus we need to have different identifiers for boxes of the same meaning, even if the same transaction creates them. We also require a box to have an identifier derived solely from box contents; thus, we can not use the *(transaction\_id, output\_id)* pair as Bitcoin Core implementation is doing.

To solve the issue, we split the concepts of a box and a box candidate. A box candidate is defining the semantics of the corresponding box, i.e. has the same values for all the registers except $R_3$, which is set to be $(creation\_height, transaction\_id || output\_index)$ for a box and $(creation\_height, 0^{34*8})$ (so instead of real transaction id and output index, a zero-bit string of 34 bytes is used) for a box candidate.

### Transaction Format

Ergo transaction consists of 3 parts:

- $inputs$ - links to boxes that will be removed from the state during the transaction application. Every input consists of box id, proof for the final sigma proposition of this box-protecting script, and a context extension to be used during script evaluation.
- $data inputs$ - links to boxes that will not be removed from the state but will be available in the context of regular input scripts.
- $outputs$ - new boxes will be included in the state during the transaction application.

Transaction bytes are to be formed as follows:

-   $inputs number$ - VLQ-encoded number of inputs.
-   $inputs$ - every input is represented as a 32-byte id of a box to be spent, the VLQ-encoded length of the signature, the signature itself, VLQ-encoded number of key-value pairs of context extension, and context extension pairs, that are 1-byte key and values serialized as a sigma expression
-   $number of data inputs$ - VLQ-encoded number of data inputs.
-   $data inputs$ - 32-byte length ids of data boxes
-   $distinct tokens number$ - number of distinct tokens in the transaction, represented as 1 byte unsigned integer.
-   $token ids$ - 32-byte length ids of tokens in the transaction
-   $outputs number$ - VLQ-encoded number of transaction outputs
-   $boxcandidates$ - every coin candidate is serialized in the same way, as box bytes from [4.1](#box-format) section, but the transaction identifier and index of a transaction output are missed, and also tokens are represented as pairs $index -> amount$, where the index is 1-byte index of token in token ids section

Input signatures should sign a $bytesToSign(tx)$ message, which is calculated as transaction bytes as if all its signatures are empty (and thus, VLQ-encoded length of signature equals 0). The transaction id is calculated as a Blake2b256 hash from message to sign.