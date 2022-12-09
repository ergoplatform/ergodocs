# Transaction Fees

You can specify any fee as long as it is not less then the minimal amount required by the protocol. This minimum depend on the serialized size of the box which you create (i.e. fee box). 

The network will accept a box if it has at least **360 nanoerg per byte**, However in practice **0.001 ERG** (or 1000000 NanoErg) is usually used in apps as a minimum per box to simplify things. 

Miners sort transactions in the mempool based on fee per byte. Somewhere around 0.001 erg/ kilobyte is a good min fee to set to be accepted in 1 block.

Knowing what fee to suggest to your user depends on your application, but you need to satisfy the protocol. When transaction is validated the [following check is perfomed](https://github.com/ergoplatform/ergo/blob/e784a70b8fabf7ae41f2ac9aa593a647f488100c/src/main/scala/org/ergoplatform/modifiers/mempool/ErgoTransaction.scala#L163). Which uses the [following function](https://github.com/ergoplatform/ergo/blob/74e715dead5b73d7c6ee723594fd8d4e88f22a94/src/main/scala/org/ergoplatform/utils/BoxUtils.scala#L43)

This is how the minimum fee is calculated in [sigma-rust](https://github.com/ergoplatform/sigma-rust/blob/95e533beb41ce3667766a1a869e11cc6ff3e1850/ergotree-ir/src/chain/ergo_box/box_value.rs#L32-L48)

