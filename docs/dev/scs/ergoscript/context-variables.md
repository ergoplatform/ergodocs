# Leveraging Context Variables in ErgoScript

ErgoScript provides the capability to create intricate programs with predicates that are context-dependent. Let's take a look at an example:

```scala
HEIGHT < 4000000            // address 2fp75qcgMrTNR2vuLhiJYQt
```

This script uses the context variable `HEIGHT`, which signifies the height of the block in which the transaction is mined. If the blockchain height is less than 4,000,000, the box associated with this address becomes ["anyone-can-spend"](anyone-can-spend.md). Conversely, if the blockchain height equals or exceeds 4,000,000, the box becomes ["no-one-can-spend"](no-one-can-spend.md).

Apart from `HEIGHT`, ErgoScript supports other context variables such as `OUTPUTS`, `INPUTS`, and `minerPubKey`. These variables offer additional tools for writing more specific and flexible scripts. For more details on context variables and their usage, please refer to the [ErgoScript language specification](lang-spec.md).

Context extension values attached to inputs can also carry reusable script or proof data. Since Sigma 6.0, a transaction can provide script bytes through one input's context extension and let other inputs read the same value, which can be cleaner than duplicating the same script/proof material on every input. Keep variable IDs explicit and document which input supplies each value; otherwise multi-input contracts become hard to audit.
