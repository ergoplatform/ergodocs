---
tags:
  - Box
---

# Box Format

In Ergo's protocol, a 'box' is a fundamental entity that encapsulates various types of information. It is not just an unspent transaction output balance, but a container that can hold value, tokens, custom data, and more. This flexibility allows for complex operations, such as running scripts or smart contracts, directly on the blockchain.

## Registers in a Box

A box is composed of **registers**. Each box can have up to 10 registers, denoted as $R_0,R_1,...,R_9$. Out of these, four registers are mandatory and contain specific values:

- $R_0$: Contains the monetary value of a box.
- $R_1$: Contains a serialized guard script.
- $R_2$: Contains tokens.
- $R_3$: Contains the declared creation height, a unique identifier of the transaction that created the coin, and the index of the box in the transaction.

Each register is an expression in the sigma language, meaning every register contains a value of a specific type. These types are defined [here](types.md). The value in a register should be a concrete constant value, not a function of a known output type.

## Extract Function

The $extract({})$ function is introduced to read the contents of a register. For instance, $extract({c, R_0})$ extracts the monetary value from the box $c$.

## Box Bytes

Box bytes are used to obtain the box identifier, build an authenticated tree for the state, and build a transaction. They are formed as follows:

- *Monetary Value*: Stored as a VLQ-encoded unsigned long value.
- *Script Bytes*: See (TODO) for how the script is serialized. The script is represented as register R1 by wrapping its bytes in a constant array of constant bytes.
- *Creation Height*: Stored as a VLQ-encoded unsigned integer value.
- *Number of Tokens*: Represented as a one-byte unsigned integer. A box can carry multiple tokens, each represented as a tuple $token\_identifier -> amount$, where the identifier is 32 bytes, and the amount is a VLQ-encoded integer.
- *Additional Registers*: Extra registers should come in order (R4, \..., etc.). This number, represented as a 1-byte unsigned value, defines how many non-empty registers are coming after the mandatory ones. If the number is zero, the next field is missed. Extra registers are serialized without any delimiters, each as a sigma expression.
- *Transaction Identifier*: A 32-byte long identifier of the transaction that created the box.
- *Index of a Transaction Output*: VLQ-encoded index of the box in the transaction outputs.

## Box Candidate

A box candidate is a preliminary version of a box, holding the same values in all registers except for $R_3$. In a fully formed box, $R_3$ contains a tuple of 

$(creation\_height, transaction\_id || output\_index)$. 

However, in a box candidate, $R_3$ is set to $(creation\_height, 0^{34*8})$. Here, a 34-byte string of zeros replaces the actual transaction id and output index. This placeholder indicates that the box candidate is not yet associated with a specific transaction or output index.

## Transaction Format

An Ergo transaction consists of three parts:

- **Inputs**: Links to boxes that will be removed from the state during the transaction application. Each input consists of a box id, proof for the final sigma proposition of this box-protecting script, and a context extension to be used during script evaluation.
- **Data inputs**: Links to boxes that will not be removed from the state but will be available in the context of regular input scripts.
- **Outputs**: New boxes that will be included in the state during the transaction application.

Transaction bytes are formed as follows:

- **Inputs number**: VLQ-encoded number of inputs.
- **Inputs**: Each input is represented as a 32-byte id of a box to be spent, the VLQ-encoded length of the signature, the signature itself, VLQ-encoded number of key-value pairs of context extension, and context extension pairs, that are 1-byte key and values serialized as a sigma expression.
- **Number of data inputs**: VLQ-encoded number of data inputs.
- **Data inputs**: 32-byte length ids of data boxes.
- **Distinct tokens number**: Number of distinct tokens in the transaction, represented as a 1-byte unsigned integer.
- **Token ids**: 32-byte length ids of tokens in the transaction.
- **Outputs number**: VLQ-encoded number of transaction outputs.
- **Boxcandidates**: Each coin candidate is serialized in the same way as box bytes from the [Box Format](#box-format) section, but the transaction identifier and index of a transaction output are missed, and tokens are represented as pairs index -> amount, where the index is a 1-byte index of a token in the token ids section.

Input signatures should sign a bytesToSign(tx) message, which is calculated as transaction bytes as if all its signatures are empty (and thus, VLQ-encoded length of signature equals 0). The transaction id is calculated as a Blake2b256 hash from the message to sign.

