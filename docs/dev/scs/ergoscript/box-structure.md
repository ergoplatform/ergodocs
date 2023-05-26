# Understanding the Structure of a Box in ErgoScript

Both `INPUTS` and `OUTPUTS` are arrays, comprising of objects of the `Box` type. A `Box` contains the following key fields:

1. `value`: The amount contained in the box, expressed in nanoErgs.
2. `propositionBytes`: This is the script serialized as an array of bytes.
3. `tokens`: This optional field is an array of tokens or assets.
4. `R4..R9`: These are the [registers](registers.md) of a box used to store any kind of data.

Each element within the `tokens` array is a pair, with the structure `(tokenId, amount)`. Here, `tokenId` is an array of 32 bytes, and `amount` is a `Long` value. 

An example of using tokens within a script is as follows:

```scala
{
   val out = OUTPUTS(0)
   val token = out.tokens(0)
   token._1 == fromBase64("nZdrGUBMAfIO6lmSRJq2zEUKGCOeYOYzAeIqbfYs8sg=")  &&
   token._2 == 1 
}
```

In this script, `out` is the first output box, and `token` is the first token in this box. The script checks if the `tokenId` of this token matches the given base64-encoded string and if the amount of the token is 1.