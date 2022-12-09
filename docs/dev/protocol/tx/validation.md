

### Transaction Validation Rules 


We split the validation of a single transaction into two stages. There are $stateless checks$ which could be done by the transaction only being presented. Stateful checks require knowledge of the current state, in the form of the whole UTXO set or a part of it, namely concrete boxes a transaction is destroying, along with proof of authenticity for them ( against a root hash included in the last block header).

**Stateless checks are:**

-   a transaction must spend at least one input and create at least one output. A transaction spends no more than $32767$ inputs and creates no more than $32767$ outputs.
-   all the output amounts must be non-negative.
-   an output can not contain more than four assets, and all the assets' amounts must be positive.
-   transaction outputs collectively could not contain more than 16 assets.

> Notes

>- Should we allow a 0-value?
- Check box and transaction sizes
- describe precisely during https://github.com/ergoplatform/ergo/issues/581


**Stateful checks are:**

-   all the input boxes are members of the UTXO set or were created by other transactions within the same block. 
-   all the data input boxes are members of the UTXO set or were created by other transactions within the same block. 
-   total input and output ERG amounts must be the same, and adding up should be done with overflow checks.
-   all the inputs have valid spending proofs.
-   total transaction cost which consists of cost of all spending proofs verification plus the cost of all tokens containing in transaction inputs and outputs validation (calculated as $(\sum_{i=1}^{n_{in}} m_{i} + m_{tx} + \sum_{i=1}^{n_{out}} k_{i} + k_{tx}) * e$, where $n_{in}$ - number of inputs, $m_{i}$ - number of tokens in $i$'th input, $m_{tx}$ - number of tokens in all inputs in total, $n_{out}$ - number of outputs, $k_{i}$ - number of tokens in $i$'th output, $k_{tx}$ - number of tokens in all outputs in total, $e$ - cost of accessing a single token (adjustable via miners voting)) should not be greater than a limit per block (which is adjustable via miners voting as well).
-   for each kind of asset in the outputs, the total output amount for the asset should be no more than the total input amount if the asset identifier is not equal to the identifier of the first input; otherwise, the total output amount must be positive. The latter case corresponds to issuing a new asset, while the former sets the asset preservation rule. 

> Please note that for the total input amount of an asset, we do not require strict equality of the input and output amounts: the output amount could be less than the input amount (or zero).


### Full-Block Validation Rules

Below are rules for block validation when a node is verifying transactions

($VerifyTransactions = 1$)

-   Every transaction in a block references inputs from the UTXO set or created by previous transactions in the block. 
-   Please note that it is impossible for an input to refer to an output of some follow-up block transaction.
-   Every transaction in a block is valid (see Section [4.6](#transaction-validation-rules) for transaction validation rules).
-   Total cost of validation of all the inputs of all the transactions in the block is no more than the allowed limit.
-   Root hash of the authenticated UTXO set after the application of the block transactions is the same as in the header.
-   For a node keeping UTXO, the hash of the calculated state transformations proof is the same as announced in the block's header.
-   Header is valid  (link to header validation rules)

> TODO: (mention emission rules. extractEmissionBox is buggy, probably. Extension validation rules)
