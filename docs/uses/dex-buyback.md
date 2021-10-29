In this example we will consider a decentralized token-sale, where seller is providing buyback guarantees. 

This guarantee is done in following way: a seller is requiring a buyer to create a buy order at some price and of some token amount also. Rest is going to the seller. 

Every order can have unique buyback properties (to e.g. form a bonding curve).

We start with buyback contract. It has expiration (`buyerPk && sigmaProp(HEIGHT > 100)` condition), otherwise, the box has been spent if asked amount of tokens sent back to the original seller.

```
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
Sell contract is then as follows:
```
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
where `bbh` is buyback script hash. 

Playground version you can experiment with is available: https://scastie.scala-lang.org/oVlOW1GpTkWGLPLzDmJTxA .


Similarly to buy-back, we can enhance orders with different conditions, getting DEX functionality (and simple DEX orders) composable with complex logic (token-sale, liquidity providing etc). I'm calling this *smart orders*. The big question, however, how to do front-end apps and UIs for smart order based DEXes.