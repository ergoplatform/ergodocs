---
tags:
  - Data Model
  - Transactions
---
# Transactions

Each Ergo transaction is an **atomic state transition operation**. 

- It destroys a [box](../../data-model/box/) from the state and creates new ones. 
- If the transaction is spending boxes protected by some non-trivial scripts, its inputs should also contain proof of spending correctness - context extension (user-defined key-value map) and data inputs (links to existing boxes in the state) that may be used during script reduction to crypto, signatures that satisfies the remaining cryptographic protection of the script. 
- Transactions are not encrypted, so it is possible to browse and view every transaction ever collected into a block.


Each transaction executed on Ergo consists of **these three things**. 

- `One or more` **Input boxes** (source of funds). 
    -  These boxes must already exist and will be destroyed. 
    -  The guard script in each of these boxes will be evaluated and must return true for the transaction to be considered valid,
- `One or more` **Output boxes** (destination of funds). 
    -  These boxes will be created.
-  `Zero or more` **Data-Inputs** boxes. 
    -  These are additional boxes whose data can be referenced and used by smart contracts of the inputs. 
    -  The guard script in these boxes will not be evaluated.


**Data inputs** are unique to Ergo and not yet present in other extended-UTXO systems. Multiple transactions can share a data-input box, and it will store only a single reference to the box in the block. 

We can also spend a data-input box in the same transaction as long as it existed before the transaction was applied. As an example, the box with id 
```
d2b9b6536287b242f436436ce5a1e4a117d7b4843a13ce3abe3168bff99924a1
```

was used as both an input and a data input in [this transaction](). 

While the use of data-inputs may not be immediately apparent, they play a major role in making Ergo more friendly to DeFi applications where we want to refer to a box without needing (or having the ability) to spend it, such as in decentralized order-books (DEX). 

For instance, the above transaction used a "timestamping service" to timestamp a box provided as data input.

A script in Ergo can refer to other boxes in the transaction. For instance, the code snippet `INPUTS(0).value > 10000 && OUTPUTS(1).value > 20000` in any of the inputs boxes would enforce that the first input and the second output boxes must have a value greater than `10000` and `20000`, respectively.

For a comparison between the logic used in eUTXO and account-based models, please see [Off Chain Logic & eUTXO](https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/) and a [model transaction](/dev/protocol/model-tx)


### Box Format

A box is made of **registers** *(and nothing but registers!)*, we allow every box in the system to have up to 10 registers. We denote the registers as `R_0,R_1,...,R_9`. From these registers, four are filled with mandatory values: `R_0` contains monetary value of a box, `R_1` contains serialized guard script, `R_2` contains tokens, `R_3` contains declared creation height, unique identifier of transaction which created the coin and also an index of the box in the transaction.

Each register is an expression in sigma language. Thus the registers are typed: every register contains a value of some type. Types are defined in TODO. The value should be evaluated (i.e. it should be a concrete constant value, not a function of a known output type).

We introduce `extract({})` function, which is reading contents of a register, for example, `extract({c, R_0})` extracts monetary value from the box `c`.

Box bytes used to obtain the box identifier, build authenticated tree for the state, and build a transaction, are to be formed as follows:

-   *monetary value.* We use VLQ-encoded unsigned long value to store monetary value of the box
-   *bytes of a script.* To see how the script is serialized, see (TODO). The script is to be represented as register R1 by wrapping its bytes are constant array of constant bytes.
-   *creation height* VLQ-encoded unsigned integer value
-   *number of tokens* which box is carrying. Represented as a one-byte unsigned integer.
-   *tokens*. A box can carry multiple tokens. A single record in this field is represented as a tuple `token\_identifier -> amount`, where identifier is of 32 bytes and amount is VLQ-encoded integer.
-   *number of additional registers.* Extra registers should come in order (R4, \..., etc), so this number, represented as 1-byte unsigned value, defines how much non-empty registers are coming after mandatory ones. If the number is zero, next field is missed.
-   *additional registers.* Extra registers are serialized without any delimiters. Each register is serialized as a sigmaexpression.
-   *transaction identifier.* 32-bytes long identifier of a transaction which created the box 
-   *index of a transaction output.* VLQ-encoded index of the box in the transaction outputs.

### Box candidate

Here we describe difference between a box and a box candidate. A box has a unique identifier to be defined deterministically from its contents. Thus we need to have different identifiers for boxs of the same meaning, even if they are created by the same transaction. We also require a box to have an identifier which is derived solely from box contents, thus we can not use *(transaction\_id, output\_id)* pair as Bitcoin Core implementation is doing.

To solve the issue we split concepts of a box and a box candidate. A box candidate is defining semantics of the corresponding box i.e. has the same values for all the registers except of the register `R_3` which is set to be `(creation\_height, transaction\_id || output\_index)` for a box and `(creation\_height, 0^{34*8})` (so instead of real transaction id and output index, a zero-bit string of 34 bytes is used) for a box candidate.

### Transaction Format

Ergo transaction consists of 3 parts:

-   `inputs` - links to boxs that will be removed from the state during the transaction application. Every inputs consists of box id, proof for final sigma proposition of this box protecting script and a context extension to be used during script evaluation.
-   `data inputs` - links to boxs that won't be removed from the state, but will be available in context of regular inputs scripts.
-   `outputs` - new boxs that will be included into the state during the transaction application.

Transaction bytes are to be formed as follows:

-   `inputs number` - VLQ-encoded number of inputs.
-   `inputs` - every input is represented as 32-byte id of a box to be spent, VLQ-encoded length of signature, signature itself, VLQ-encoded number of key-value pairs of context extension, and context extension pairs, that are 1-byte key and values serialized as a sigmaexpression
-   `number of data inputs` - VLQ-encoded number of data inputs.
-   `data inputs` - 32-byte length ids of data boxes
-   `distinct tokens number` - number of distinct tokens in the transaction, represented as 1 byte unsigned integer.
-   `token ids` - 32-byte length ids of tokens in the transaction
-   `outputs number` - VLQ-encoded number of transaction outputs
-   `boxcandidates` - every coin candidates are serialized in the same way, as box bytes from [4.1](#box-format) section, but transaction identifier and index of a transaction output are missed, and also tokens are represented as pairs `index -> amount`, where index is 1-byte index of token in token ids section

Inputs signatures should sign a `bytesToSign(tx)` message, that is calculated as transaction bytes, as if all it's signatures are empty (and thus VLQ-encoded length of signature equals to 0). Transaction id is calculated as a Blake2b256 hash from message to sign.

### Transaction Merkle Tree 

Like a miner in the Bitcoin protocol is building a Merkle tree of block transactions, as well as a Merkle tree of transaction witnesses (after the Segwit upgrade), in Ergo, a miner should build a Merkle tree (and include a correct root hash of the tree into a block header), which is in case of Ergo combines both transactions and their respective spending proofs.

This tree is to be constructed as follows. A data block under a leaf of the tree could be empty or 64 bytes in length. Data of 64 bytes contains identifier of the transaction (256-bits digest of transaction bytes without spending proofs) and 256 bits of a digest of all the spending proofs for the transaction combined. Data for `i-th` transaction in the block (starting from 0) is authenticated by the `i-th` leaf. A leaf is `hash(0 || pos || data)`, if the `data` is not empty  (we do add prefix for domain separation), or `null` otherwise. Here, `pos` is a position of the transaction in the block. For internal nodes, a node is `hash(1 || left\_child || right\_child)`, if either left child or right child of the node is not `null`, `null` othewise. If root hash is `null`, we are writing all zeros (of hash function output length) instead of it.

### Signing A Transaction

To spend a box a spending transaction `tx` has as an input, one needs to use `bytesToSign(tx)` (note that different inputs can be signed in parallel, however, the coins being spent are to be specified before signing), as well as the current state of the blockchain, or `context`. The signer also can extend the context by putting values there.

By having this data, a signer (or a prover) of an input first reduces the guarding proposition for the input box by evaluating, it using the context. Possible results of the reduction are:

-   abort if estimated upper-bound cost of evaluation (and verification) is too high.
-   true means that the box is spendable by anyone
-   false means that the box is not spendable at all (at least according to the current context)
-   expression still containing predicates over the context. That means context is not enough to evaluate some predicates over it. Prover can look into its own not revealed yet secrets in order to extend context. If the secrets are found, prover is reducing the expression further and doing the next step, if there is nothing more to evaluate. Otherwise the prover aborts.
-   expression containing only expressions over secret information provable via `\Sigma`-protocols. This is the most common case, and we will explain it in detail further.

We are having possible complex expression, like `dlog(x_1) \lor (dlog(x2) /\ dlog(x3))`, where `dlog(x)` means "prove me knowledge of a secret `w`, such as for a known group with generator `g`, `g^w = x`, via a non-interactive form of the Schnorr protocol". Internally, this exression is represented as a tree (TODO). This proof is to be proven and then serialized into a binary spending proof (which could be included into a transaction) as follows:

**Proving steps for a tree:**


1. bottom-up: mark every node real or simulated, according to the following rule. DLogNode -- if you know the secret, then real, else simulated. `\lor`: if at least one child real, then real; else simulated. `\land`: if at least one child simulated, then simulated; else real. 

> Note that all descendants of a simulated node will be later simulated, even if they were marked as real. This is what the next step will do.

Root should end up real according to this rule -- else you won't be able to carry out the proof in the end.

1. **top-down:** mark every child of a simulated node \"simulated.\" If two or more more children of a real `\lor` are real, mark all but one simulated.
2. **top-down:** compute a challenge for every simulated child of every `\lor` and `\land`, according to the following rules. If `\lor`, then every simulated child gets a fresh random challenge. If `\land` (which means `\land` itself is simulated, and all its children are), then every child gets the same challenge as the `\land`.
3. **bottom-up:** For every simulated leaf, simulate a response and a commitment (i.e., second and first prover message) according to the Schnorr simulator. For every real leaf, compute the commitment (i.e., first prover message) according to the Schnorr protocol. For every `\lor`/`\land` node, let the commitment be the union (as a set) of commitments below it.
4. Compute the Schnorr challenge as the hash of the commitment of the root (plus other inputs -- probably the tree being proven and the message).
5. **top-down:** compute the challenge for every real child of every real `\lor` and `\land`, as follows. If `\lor`, then the challenge for the one real child of `\lor` is equal to the XOR of the challenge of `\lor` and the challenges for all the simulated children of `\lor`. If `\land`, then the challenge for every real child of `\land` is equal to the the challenge of the `\land`.

> Note that simulated `\land` and `\lor` have only simulated descendants, so no need to recurse down from them.

Now, how to get a flat binary string containing `(e, z)` pairs (challenge and prover's response for a leafsub-protocol) from the tree:

### Transaction Validation Rules 


We split validation of a single transaction into two stages. There are `stateless checks` which could be done by the transaction only being presented. Stateful checks are requiring knowledge of the current state, in the form of the whole UTXO set or a part of it, namely concrete boxes a transaction is destroying along with proof of authenticity for them ( against a root hash included into a last block header).

**Stateless checks are:**

-   a transaction must spend at a least one input and create at least one output. A transaction spends no more than `32767` inputs and creates no more than `32767` outputs.
-   all the output amounts must be non-negative.
-   an output can not contain more than 4 assets. All the assets amounts must be positive.
-   transaction outputs collectively could not contain more than 16 assets.

> Notes

>- Should we allow 0-value iutputs?
- Check box and transaction sizes
- describe precisely during https://github.com/ergoplatform/ergo/issues/581


**Stateful checks are:**

-   all the input boxes are members of the UTXO set or where created by other transactions of this block.
-   all the data input boxes are members of the UTXO set or where created by other transactions of this block.
-   total input and output ergo amounts must be the same. Adding up should be done with overflow checks.
-   all the inputs have valid spending proofs.
-   total transaction cost which consists of cost of all spending proofs verification plus the cost of all tokens containing in transaction inputs and outputs validation (calculated as `(\sum_{i=1}^{n_{in}} m_{i} + m_{tx} + \sum_{i=1}^{n_{out}} k_{i} + k_{tx}) * e`, where `n_{in}` - number of inputs, `m_{i}` - number of tokens in `i`'th input, `m_{tx}` - number of tokens in all inputs in total, `n_{out}` - number of outputs, `k_{i}` - number of tokens in `i`'th output, `k_{tx}` - number of tokens in all outputs in total, `e` - cost of accessing a single token (adjustable via miners voting)) should not be greater than a limit per block (which is adjustable via miners voting as well).
-   for each kind of asset in the outputs, total output amount for the asset should be no more than the total input amount, if the asset identifier is not equals to identifier of the first input; otherwise, the total output amount must be positive. The latter case corresponds to issuance of a new asset, while the former sets asset preservation rule. 

> Please note that for total input amount of an asset we do not require for strict equality of the input and output amounts: the output amount could be less than input amount (or zero).

### Unified Transactions

- fee as boxes 
- absence of out-of-thin-air emission in the "coinbase" transaction.

### Full-Block Validation Rules

Below are rules for block validation when a node is verifying transactions (`VerifyTransactions = 1`)

-   every transaction in a block is referencing to inputs from the UTXO set or created by previous transactions in the block. 
    -   Please note that it is not possible for an input to refer to an output of some follow-up transaction of the block.
-   every transaction in a block is valid (see Section [4.6](#transaction-validation-rules) for transaction validation rules).
-   total cost of validation of all the inputs of all the transactions in the block is no more than allowed limit.
-   root hash of the authenticated UTXO set after application of the block transactions is the same as in the header.
-   for a node keeping UTXO, hash of the calcualted state transformations proof is the same as announced in the header of the block.
-   header is valid  (link to header validation rules)

(mention emission rules. extractEmissionBox is buggy probably. extension validation rules)