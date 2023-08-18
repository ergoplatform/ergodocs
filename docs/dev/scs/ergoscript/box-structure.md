---
tags:
  - Box
---

# Deep Dive into ErgoScript's Box Structure

In Ergo's ecosystem, the term ['box'](box.md) is more than just an unspent transaction output balance. It's a versatile container that holds various types of information (value, tokens, custom data, etc.), making Ergo's boxes highly flexible and functional. This functionality allows for complex operations, such as executing scripts or smart contracts, directly on the blockchain.

The `INPUTS` and `OUTPUTS` in ErgoScript are arrays, each consisting of `Box` type objects. A `Box` encapsulates the following key fields:

1. `value`: The amount held in the box, denoted in nanoErgs.
2. `propositionBytes`: The script, serialized into a byte array.
3. `tokens`: An optional field that holds an array of tokens or assets.
4. `R4..R9`: These are the [registers](registers.md) of a box, capable of storing any type of data.

Each element in the `tokens` array is a pair, structured as `(tokenId, amount)`. Here, `tokenId` is a 32-byte array, and `amount` is a `Long` value. 

```scala
{
   val out = OUTPUTS(0)
   val token = out.tokens(0)
   token._1 == fromBase64("nZdrGUBMAfIO6lmSRJq2zEUKGCOeYOYzAeIqbfYs8sg=")  &&
   token._2 == 1 
}
```

In this script, `out` is the first output box, and `token` is the first token in this box. The script checks if the `tokenId` of this token matches the given base64-encoded string and if the amount of the token is 1.
