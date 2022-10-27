## Data Inputs

**Data inputs** are unique to Ergo and not yet present in other extended-UTXO systems. Multiple transactions can share a data-input box, which will store only a single reference to the box in the block. 

We can also spend a data-input box in the same transaction as long as it existed before the transaction was applied. As an example, the box with the id. 
```
d2b9b6536287b242f436436ce5a1e4a117d7b4843a13ce3abe3168bff99924a1
```

It was used as both an input and a data input in [this transaction](). 

While the use of data inputs may not be immediately apparent, they play a major role in making Ergo more friendly to DeFi applications where we want to refer to a box without needing (or have the ability) to spend it, such as in decentralized order-books (DEX). 

For instance, the above transaction used a "timestamping service" to timestamp a box provided as data input.

A script in Ergo can refer to other boxes in the transaction. For instance, the code snippet `INPUTS(0).value > 10000 && OUTPUTS(1).value > 20000` in any of the inputs boxes would enforce that the first input and the second output boxes must have a value greater than `10000` and `20000`, respectively.

For a comparison between the logic used in eUTXO and account-based models, please see [Off Chain Logic & eUTXO](https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/) and a [model transaction](/dev/protocol/model-tx)
