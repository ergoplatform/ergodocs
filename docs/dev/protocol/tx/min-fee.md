# Transaction Fees

Transaction fees in Ergo are flexible, but they must meet a minimum threshold as defined by the protocol. This minimum fee is dependent on the serialized size of the box you create, also known as the fee box.

The network will accept a fee box if it carries at least **360 nanoerg per byte**. However, to simplify calculations, applications typically use a minimum of **0.001 ERG** (or 1000000 NanoErg) per box.

Miners prioritize transactions in the mempool based on the fee per byte. To ensure your transaction is accepted in the next block, it is recommended to set a minimum fee of around 0.001 erg/kilobyte.

The appropriate fee for your transaction largely depends on the requirements of your application, but it must comply with the protocol. During transaction validation, a [specific check](https://github.com/ergoplatform/ergo/blob/e784a70b8fabf7ae41f2ac9aa593a647f488100c/src/main/scala/org/ergoplatform/modifiers/mempool/ErgoTransaction.scala#L163) is performed, which utilizes a [particular function](https://github.com/ergoplatform/ergo/blob/74e715dead5b73d7c6ee723594fd8d4e88f22a94/src/main/scala/org/ergoplatform/utils/BoxUtils.scala#L43) to calculate the minimum fee.

For a practical example of how the minimum fee is computed, refer to the implementation in [sigma-rust](https://github.com/ergoplatform/sigma-rust/blob/95e533beb41ce3667766a1a869e11cc6ff3e1850/ergotree-ir/src/chain/ergo_box/box_value.rs#L32-L48).

