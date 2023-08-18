# Transaction Validation Rules 

The validation of a single transaction is divided into two stages: stateless checks and stateful checks. Stateless checks are performed solely based on the transaction itself, while stateful checks require knowledge of the current state, including the UTXO set or a part of it, and the specific boxes a transaction is destroying, along with their proof of authenticity (against a root hash included in the last block header).

**Stateless Checks:**

-   A transaction must spend at least one input and create at least one output. A transaction can spend up to $32767$ inputs and create up to $32767$ outputs.
-   All output amounts must be non-negative.
-   An output cannot contain more than four assets, and all the assets' amounts must be positive.
-   The transaction outputs collectively cannot contain more than 16 assets.

> Notes

> - Consideration: Should we allow a 0-value?
> - Check box and transaction sizes
> - Precise description to be provided during https://github.com/ergoplatform/ergo/issues/581


**Stateful Checks:**

-   All the input boxes must be members of the UTXO set or created by other transactions within the same block. 
-   All the data input boxes must be members of the UTXO set or created by other transactions within the same block. 
-   The total input and output ERG amounts must be the same, with overflow checks.
-   All the inputs must have valid spending proofs.
-   The total transaction cost, which includes the cost of all spending proofs verification and the cost of all tokens in transaction inputs and outputs validation, should not exceed a limit per block (adjustable via miners voting).
-   For each kind of asset in the outputs, the total output amount for the asset should not exceed the total input amount unless the asset identifier is the identifier of the first input; in this case, the total output amount must be positive. This rule ensures asset preservation and allows for new asset issuance. 

> Note: For the total input amount of an asset, we do not require strict equality of the input and output amounts: the output amount could be less than the input amount (or zero).


### Full-Block Validation Rules

The following rules apply for block validation when a node is verifying transactions ($VerifyTransactions = 1$):

-   Every transaction in a block must reference inputs from the UTXO set or created by previous transactions in the block. 
-   Note: An input cannot refer to an output of a subsequent block transaction.
-   Every transaction in a block must be valid (refer to the transaction validation rules above).
-   The total cost of validation of all the inputs of all the transactions in the block must not exceed the allowed limit.
-   The root hash of the authenticated UTXO set after applying the block transactions must match the one in the header.
-   For a node maintaining UTXO, the hash of the calculated state transformations proof must match the one announced in the block's header.
-   The header must be valid (refer to header validation rules).

> TODO: (Mention emission rules. The extractEmissionBox function may have bugs. Extension validation rules need to be added.)

