
# Box Structure

Both the `INPUTS` and `OUTPUTS` arrays are a collection of `Box` type, which has the following important fields:

1. The amount (in nanoErgs) contained in the box: `value`
2. The serialized script as an array of bytes: `propositionBytes`
3. An array of tokens (optional assets): `tokens`
4. The registers of a box `R4..R9` used to store arbitrary data

Each element of `tokens` is a pair of type `(tokenId, amount)`, where `tokenId` is an array of 32 bytes and the amount is `Long`. 
An example of using tokens is the script:

    {
       val out = OUTPUTS(0)
       val token = out.tokens(0)
       token._1 == fromBase64("nZdrGUBMAfIO6lmSRJq2zEUKGCOeYOYzAeIqbfYs8sg=")  &&
       token._2 == 1 
    }