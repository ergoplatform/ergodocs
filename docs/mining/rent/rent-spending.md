# How to Spend an Expired Ergo Box

Spending an expired Ergo box involves satisfying specific conditions that differ from spending a regular box. The following criteria must be met:

## Conditions for Spending an Expired Box

1. **Storage Fee Duration**: The box must have been retained for at least the designated storage fee period. This is validated by calculating the difference between the height of the upcoming block, as indicated in the preheader, and the creation height of the box. This difference should be greater than or equal to the storage fee period.
2. **Spending Proof**: For an expired box, the spending proof must be left empty, eliminating the need for cryptographic authorization for the box's spending.

### Code Snippet for Verifying Storage Fee Duration

The following line of code checks whether the box has been stored for the required minimum duration, comparing the height of the upcoming block (`context.preHeader.height`) with the box's creation height (`context.self.creationHeight`):

```scala
context.preHeader.height - context.self.creationHeight >= Constants.StoragePeriod
```

**Reference**: [ErgoInterpreter.scala, line 73](https://github.com/ergoplatform/ergo/blob/49b9f0fe7d0eba1a5ff81e524353acdd9a3cc6dd/ergo-wallet/src/main/scala/org/ergoplatform/wallet/interpreter/ErgoInterpreter.scala#L73)

### Spending Proof for Expired Boxes

The term "spending proof" typically refers to a cryptographic authorization required for spending a box. However, in the context of an expired box, this requirement is waived. The spending proof for the expired box must be empty, meaning that no cryptographic validation is needed to authorize its spending. This allows any participant to spend the expired box without needing to prove ownership, as long as the storage fee duration condition is fulfilled.

### Additional Details for Spending an Expired Box

If both the above conditions are met, the expired box can be spent by anyone. To do so, one needs to provide an index of a newly recreated box (or an index of any box, if the expired box lacks sufficient funds for the storage fee) in the context extension variable #127, which will be stored as part of the input.
