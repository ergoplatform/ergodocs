# Context Enrichment


In Bitcoin and other existing UTXO systems, the *context* is just the UTXO being processed. 

In order for a UTXO-based system to support transaction trees, the context must be rich enough to contain at least the entire spending transaction.

More formally, for any UTXO based blockchain, we can define the following levels of context, each extending the previous:

- **Level 1**: current UTXO, height and timestamp
- **Level 2**: current transaction (inputs and outputs)
- **Level 3**: current block header and block solution
- **Level 4**: current block (other sibling transactions)
 
Any platform at Level 2 and above is suitable for transaction trees. In this regard, Bitcoin operates at Level 1 and Ergo at Level 3. 

Note that in Level 4 we cannot check validity of transactions independently of other transactions in the block. Hence it is more complex to implement Level 4.


In this work we show via examples how to create efficient Ethereum-like contracts in the UTXO model using transaction trees. The examples include a Rock-Paper-Scissors game, an Initial Coin Offering (ICO) campaign and a new primitive called reversible addresses for securely storing funds. 



### Enriched Context Levels

- Script code can have predicates on objects in context. 
    - Example `OUTPUT(0).value >= 1000`
- It is known that Level 2 can emulate Turing complete (hence Ethereum)
However, the proof uses Rule 110 cellular automation. Reduction is not efficient
- We need something more efficient than Rule 110. This is our contribution.


## How to ensure that each stage follows protocol?

Code in context Level 2 and higher allows multistage protocols

Spending transactions must create another UTXO with the required properties. 

```scala
out.propositionBytes == state_n_code && 
out.R4[Int].get == SELF.R4[Int].get // ensure data is propagated
```

This code is checking two conditions:

- Whether the propositionBytes of the out box is equal to state_n_code.
- Whether the R4 register of the out box is equal to the R4 register of the current SELF box.

The first condition checks if the script of the output box matches the expected script (as represented by state_n_code). If this condition is not satisfied, the script will reject the transaction.

The second condition ensures that a certain data value stored in the R4 register is propagated from the current box to the output box. If this condition is not satisfied, the script will reject the transaction.