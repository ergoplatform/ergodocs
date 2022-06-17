# Registers

[ErgoScript](/dev/scs/ergoscript) (as well as [ErgoTree](/dev/scs/ergotree)) is **typed**, so accessing a register is an operation that involves some expected type given in brackets. 

Thus, the `SELF.R4[Int]` expression should evaluate a valid value of the `Option[Int]` type.
    
For example, `val x = SELF.R4[Int]` expects the register - if it is present - to have type `Int`. 

There are three cases:

1. If the register does not exist. Then `val x = SELF.R4[Int]` succeeds and returns the None value, which conforms to any value of type `Option[T]` for any T. (In the example above, T is equal to `Int`). Calling `x.get` fails when x is equal to None, but `x.isDefined` succeeds and returns `false`.
2. If the register contains a value `v` of type `Int`. Then `val x = SELF.R4[Int]` succeeds and returns `Some(v)`, which is a valid value of type `Option[Int]`. In this case, calling `x.get` succeeds and returns the value `v` of type `Int`. Calling `x.isDefined` returns `true`.
3. If the register contains a value `v` of type T other than `Int`. Then `val x = SELF.R4[Int]` fails because there is no way to return a valid value of type `Option[Int]`. The register value is present, so returning it as None would break the typed semantics of registers collection.
    
Within some use cases, a register may have values of different types. To access such a register, we can use an additional register as a tag.

```scala
val tagOpt = SELF.R5[Int]
val res = if (tagOpt.isDefined) {
  val tag = tagOpt.get
  if (tag == 1) {
    val x = SELF.R4[Int].get
    // compute res using value x is of type Int
  } else if (tag == 2) {
    val x = SELF.R4[GroupElement].get
    // compute res using value x is of type GroupElement
  } else if (tag == 3) {
    val x = SELF.R4[ Array[Byte] ].get
    // compute res using value x of type Array[Byte]
  } else {
    // compute `res` when `tag` is not 1, 2 or 3
  }
} else {
  // compute value of res when register is not present
}
```

## Asset Issuance Standard and Oracles

Ergo supports custom tokens as first-class citizens. Namely, a special register (R2) of a box contains (tokenId -> amount) pairs. The hard limit for the number of tokens per box or transaction is pretty liberal; namely, there could be up to 255 secondary tokens in a transaction or a box; however, there are indirect limits (box could be no more than 4 kilobytes, and also tokens add to the estimated computational cost of the transaction).

Erg amount is written directly (with no identifier) as a number into register R0. There are more significant differences between Ergs and other tokens:

* Ergs can not be burnt: the total amount of ergs in transaction inputs should equal the total amount of the outputs. Unlike ergs, other tokens can be burnt: the total amount for a token in transaction inputs should be no less than the amount of the outputs.
* Storage rent (see Sec 5 of the whitepaper) could be paid only in Ergs.

Tokens can represent shares, complementary currency units etc. In the UTXO model, a token issued with an amount of exactly 1, which we call the singleton token, could also be used to imitate long-living accounts existing in Waves, Ethereum Classic etc. Namely, a transaction spends an old box with the singleton token and creates a new one, and the script of the old box can demand the new box to have specific properties (e.g. a particular script or a particular amount). Thus the smart account marked with the token can live and have its state changed as prescribed by the smart account contract through a transaction chain. 

A particular case for a singular token is an oracle. One can create a token, e.g. ERG/EUR exchange rates oracle. Then a box which contains the token has an exchange rate encoded in a specific register. As the oracle is a long-living account, contracts can know the oracle token identifier in advance and refer to it. 

How could new assets be created? There is a notable exception to the weak preservation rule (total amount in inputs is no less than the total amount in outputs),  namely, a transaction can create out-of-thin-air tokens in its outputs if the asset identifier is equal to the identifier of the first input box of the transaction. As the box identifier is cryptographically unique, there is no chance of having a second asset with the same identifier. At the same time, the hash function used is collision-resistant (and it indeed is). This rule also means that only one new asset per transaction can be created. 

Ergo reference implementation wallet is using specific registers in a certain way, though the protocol does not require this: 

  * R4 - verbose name
  * R5 - description
  * R6 - number of decimal places
  * additional registers (R7, R8, R9) could be used for asset-specific information 

Applications can use this convention; however, again, the protocol does not enforce it.
