# Buy Back Guarantees

In this example, we will explore a decentralized token sale scenario where the seller provides buyback guarantees.

The guarantee works as follows: the seller requires the buyer to create a buy order at a specific price for a certain amount of tokens. The remaining amount goes to the seller.

Each order can have unique buyback properties, such as forming a bonding curve.

We begin with a buyback contract. It has an expiration condition (`buyerPk && sigmaProp(HEIGHT > 100)`); otherwise, the box has been spent if the original seller requests the number of tokens sent back.

```scala
    {
        val defined = OUTPUTS(0).R2[Coll[(Coll[Byte], Long)]].isDefined &&  OUTPUTS(0).R4[Coll[Byte]].isDefined
        (buyerPk && sigmaProp(HEIGHT > 100)) || sigmaProp (if (defined) {
          allOf(Coll(
              OUTPUTS(0).tokens(0)._1 == tokenId, 
              OUTPUTS(0).tokens(0)._2 >= tokenAmount,
              OUTPUTS(0).propositionBytes == sellerPk.propBytes,
              OUTPUTS(0).R4[Coll[Byte]].get == SELF.id)
             )
        } else { false } )
    }
```

The sell contract is then defined as follows:

```scala
      {
        sigmaProp(allOf(Coll(
                    blake2b256(OUTPUTS(0).propositionBytes) == bbh,
                    OUTPUTS(0).value == buyBackAmount,
                    OUTPUTS(1).value >= toWithdraw,
                    OUTPUTS(1).propositionBytes == sellerPk.propBytes,
                    OUTPUTS(1).R4[Coll[Byte]].get == SELF.id
                  ))
                 )
      }
```
In this case, `bbh` represents the buyback script hash.

You can experiment with a playground version of this code [on scastie](https://scastie.scala-lang.org/oVlOW1GpTkWGLPLzDmJTxA)


Just like the buyback, we can enhance orders with various conditions, thereby achieving DEX functionality. This makes simple DEX orders composable with complex logic such as token-sale, liquidity providing, etc. This concept is referred to as *smart orders*. However, the challenge lies in developing front-end apps and user interfaces for smart order-based DEXes.
