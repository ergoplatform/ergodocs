---
tags:
  - Box
---

# Box Format

In Ergo's protocol, a 'box' is a fundamental entity that encapsulates various types of information. It is not just an unspent transaction output (UTXO) balance, but a versatile container that can hold value, tokens, custom data, and more. This flexibility allows for complex operations, such as running scripts or smart contracts, directly on the blockchain.

## Registers in a Box

A box is composed of **registers**. Each box can have up to 10 registers, denoted as $R_0, R_1, \dots, R_9$. Out of these, four registers are mandatory and contain specific values:

- **$R_0$**: Contains the monetary value of the box, stored as a VLQ-encoded unsigned long.
- **$R_1$**: Contains a serialized guard script (ErgoScript), which dictates the conditions under which the box can be spent.
- **$R_2$**: Contains tokens, represented as pairs of token identifiers (32 bytes) and their respective amounts (VLQ-encoded integers).
- **$R_3$**: Contains metadata including the declared creation height, the unique identifier of the transaction that created the box, and the index of the box in the transaction outputs.

Each register is an expression in the Sigma language, meaning every register contains a value of a specific type. These types are defined in [this document](types.md). The value in a register should be a concrete constant value, not a function of a known output type.

### Additional Registers

The registers $R_4$ to $R_9$ are optional and can be used to store additional data relevant to the transaction or smart contract. These registers follow the same serialization rules as the mandatory ones, but they are serialized without any delimiters, each as a Sigma expression.

## Box Serialization Format

Box bytes are critical for various functions like obtaining the box identifier, building authenticated trees for the blockchain state, and constructing transactions. The serialization of a box follows a specific structure:

- **Monetary Value**: Serialized as a VLQ-encoded unsigned long value.
- **Script Bytes**: The serialized script (from $R_1$) is wrapped in a constant array of constant bytes.
- **Creation Height**: Serialized as a VLQ-encoded unsigned integer.
- **Number of Tokens**: Represented as a one-byte unsigned integer. Each token in the box is a tuple $(token\_identifier, amount)$, where the identifier is 32 bytes and the amount is a VLQ-encoded integer.
- **Additional Registers**: Serialized without any delimiters. The number of non-empty registers is represented as a 1-byte unsigned integer.
- **Transaction Identifier**: A 32-byte identifier of the transaction that created the box.
- **Index of Transaction Output**: Serialized as a VLQ-encoded index of the box in the transaction outputs.

## Box Candidate

A **Box Candidate** is a preliminary version of a box used during transaction creation. It holds the same values in all registers as a fully formed box, except for $R_3$. In a Box Candidate, $R_3$ is initialized with a placeholder value $(creation\_height, 0^{34*8})$ where a 34-byte string of zeros replaces the actual transaction ID and output index. This indicates that the box candidate is not yet associated with a specific transaction or output index.

Once the transaction is confirmed on the blockchain, the placeholder in $R_3$ is replaced with the actual transaction ID and output index, finalizing the box.

## Transaction Format

An Ergo transaction consists of three parts:

1. **Inputs**: Links to boxes that will be removed from the state during transaction application. Each input consists of:
    - A box ID.
    - A proof for the final Sigma proposition of this box-protecting script.
    - A context extension used during script evaluation.

2. **Data Inputs**: Links to boxes that will not be removed from the state but will be available in the context of regular input scripts. This allows transactions to reference additional data without consuming the box.

3. **Outputs**: New boxes that will be included in the state during transaction application.

### Transaction Serialization

- **Inputs Number**: VLQ-encoded number of inputs.
- **Inputs**: Each input is serialized as a 32-byte ID of the box to be spent, the VLQ-encoded length of the signature, the signature itself, and the context extension (as key-value pairs).
- **Number of Data Inputs**: VLQ-encoded number of data inputs.
- **Data Inputs**: 32-byte length IDs of data boxes.
- **Distinct Tokens Number**: Number of distinct tokens in the transaction, represented as a 1-byte unsigned integer.
- **Token IDs**: 32-byte length IDs of tokens in the transaction.
- **Outputs Number**: VLQ-encoded number of transaction outputs.
- **Box Candidates**: Each Box Candidate is serialized similarly to box bytes, but without the transaction identifier and output index. Tokens are represented as index -> amount pairs, where the index is a 1-byte index of the token in the token IDs section.

### Signing a Transaction

Input signatures are created by signing the `bytesToSign(tx)` message, which is calculated as the transaction bytes with all signatures set to zero (VLQ-encoded length of zero). The transaction ID is calculated as a Blake2b256 hash of this message.
