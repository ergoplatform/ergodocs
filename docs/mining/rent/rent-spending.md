# Spending an expired box

The following conditions must be met in order to spend a box:

1. The difference between the upcoming block's height (taken from the preheader) and the box's creation height must be greater than or equal to the storage fee period. In other words, the box must have been stored for at least the required storage fee period.
1. The *spending proof* for the expired box must be empty.


This line of code checks if the box has been stored for at least the required storage fee period. It calculates the difference between the upcoming block's height (`context.preHeader.height`) and the box's creation height (`context.self.creationHeight`). If this difference is greater than or equal to the constant value representing the storage fee period (`Constants.StoragePeriod`), the condition is satisfied.
   
```
context.preHeader.height - context.self.creationHeight >= Constants.StoragePeriod
```

- (Reference: [ErgoInterpreter.scala, line 73](https://github.com/ergoplatform/ergo/blob/49b9f0fe7d0eba1a5ff81e524353acdd9a3cc6dd/ergo-wallet/src/main/scala/org/ergoplatform/wallet/interpreter/ErgoInterpreter.scala#L73))

The "*spending proof*" for the expired box refers to a cryptographic proof that is typically required to authorize the spending of a box (or transaction output). In the case of an expired box, the condition "spending proof must be empty" means that no such cryptographic proof is needed to spend the box. This allows anyone to spend the expired box without providing any proof of ownership, as long as the other conditions are met (such as the box being stored for at least the required storage fee period).

If these conditions are met, anyone can spend the expired box by providing an index of a recreated box (or an index of any box if the expired box doesn't have enough funds to cover the storage fee) in context extension variable #127, which is stored in the input.