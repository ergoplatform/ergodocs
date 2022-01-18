# A Quick Primer on ErgoScript

Ergo platform is getting a lot of attention these days. Several queries relate to ErgoScript, the underlying smart contract language of Ergo.
This article gives a short introduction to ErgoScript.

## What is ErgoScript?

The Ergo node does not understand ErgoScript. It only understands a low-level language called
 [**ErgoTree**](https://ergoplatform.org/docs/ErgoTree.pdf), which is a "tree" based language (somewhat like XML). 
 However, writing code in ErgoTree is difficult.  

ErgoTree is similar to Bitcoin's Script in some aspects. An ErgoTree program is deterministic and consists of a sequence of boolean predicates joined using `AND` and `OR`.
Ergo nodes execute the ErgoTree program contained in a transaction and consider it valid if it evaluates to `true`.
An example of such a program can be `AND(OR(condition_1, condition_2), condition_3)`, which implies that the transaction is valid if 
`condition_3` and at least one of `condition_1` or `condition_2` hold.    

ErgoScript is a high-level developer-friendly language for writing smart contracts that are then compiled to ErgoTree before being written to the blockchain.
The equivalent of the above program in ErgoScript will be `(condition_1 || condition_2) && condition_3`. 

## Key Concepts

1. Since Ergo is UTXO based, therefore ErgoScript has many UTXO-specific constructs such as `Box`, `INPUTS`, `OUTPUTS`, etc. 
A complete list is available [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md). A `Box` is essentially a UTXO and consists of up to ten registers for storing data. Similar to Bitcoin, a transaction spends one or more existing boxes (denoted using the `INPUTS` array) and creates one or more new boxes (denoted using the `OUTPUTS` array).  

2. ErgoScript's syntax is a subset of Scala's. However, knowledge of Scala is not necessary to learn ErgoScript because 
the amount of Scala needed to write ErgoScript is tiny. That being said, some prior experience in Scala will  
be useful in picking up ErgoScript and Scala is a [good language to have on your resume](https://insights.dice.com/2020/06/04/24-programming-languages-pay-top-salaries-scala/) anyway.  

3. Like Scala, ErgoScript supports functional programming, which makes it easier
to deal with collections using metaphors such as `foreach`, `exists`, `fold`, etc.  

4. Like ErgoTree, an ErgoScript program consists of a sequence of boolean predicates joined using `&&` and `||`. 

5. ErgoScript provides cryptographic operations via `BigInt` and `GroupElement` (Elliptic curve point) types along with relevant
operations such as addition, multiplication and exponentiation. Note that, unlike Scala, `BigInt` operations in ErgoScript are performed modulo `2^256`, and thus, care must be taken about overflow. 

## ErgoScript Examples

**Tip:** For beginners, we highly recommend Jason Davies' [ErgoScript P2S playground](https://wallet.plutomonkey.com/p2s/), 
which can be used to get the Ergo address
corresponding to some arbitrary ErgoScript program. Please use the P2S playground only for experiments and not for storing any large amounts.

### Anyone-Can-Spend Scripts

The simplest ErgoScript program is a single boolean predicate such as:

    true

This corresponds to the [address](https://wallet.plutomonkey.com/p2s/?source=dHJ1ZQ==) `4MQyML64GnzMxZgm`.

**Notes:**    
1. Any funds sent to this address can be spent by anyone because the script always evaluates to `true`.
2. Scripts that always evaluate to `true` (and the corresponding boxes) are called **anyone-can-spend**. 

A slightly more complex "anyone-can-spend" script is: 

    true && (false || true)     // address NwAyzZpF2KcXAGBJvPrAH 

### No-one-Can-Spend Scripts

At the other end of the spectrum are ErgoScript programs that always evaluate to `false`, such as 

    true && false               // address m3iBKr65o53izn

**Notes:**    
1. Funds sent to such addresses cannot be spent by anyone and consequently such scripts are called **no-one-can-spend**.
Please don't send funds to such addresses.  
2. Ergo has the concept of [*garbage collection* / storage rent](https://ergoplatform.org/en/blog/2020_04_21_ergo_positioning/), so such boxes will eventually be removed from the blockchain over a long period.
 
### Context Variables

More interesting ErgoScript programs contain predicates defined on context, such as:

    HEIGHT < 4000000            // address 2fp75qcgMrTNR2vuLhiJYQt
    
This uses the context variable `HEIGHT`, representing the height of the block in which the transaction gets mined. 
A box with this address is "anyone-can-spend" if the blockchain height is less than 4000000 and "no-one-can-spend" otherwise. 
There are other context variables such as `OUTPUTS, INPUTS, minerPubKey`. See the [documentation](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md) for details.

### Code-blocks

Multiple lines must be put inside a code-block enclosed in braces as in:

    {
       val out = OUTPUTS(0)
       val in = INPUTS(0)
       in.value == out.value
    }  

Note that arrays in Scala are accessed using round parentheses, not square brackets like in Java or Python. 
Thus, `OUTPUTS(0)` refers to the first element of the `OUTPUTS` array. As in Scala, the last line of a block is the returned value of that block. In the above example, the value returned is the boolean predicate
`in.value == out.value`.  

The above script, [corresponding to the address](https://wallet.plutomonkey.com/p2s/?source=eyAgCiAgdmFsIG91dCA9IE9VVFBVVFMoMCkKICB2YWwgaW4gPSBJTlBVVFMoMCkKICBpbi52YWx1ZSA9PSBvdXQudmFsdWUKfQ==)  `2EUTBShk4TbLWJNwGpkVYh8dAPqbrfvb3p`, 
allows anyone to spend the corresponding box provided that the first input and first output of the transaction have the same value. 

Observe that we used the `val` keyword to define intermediate variables. As in Scala, a `val` defines an immutable object. Therefore, the following snippet is invalid:

     ...
     val out = OUTPUTS(0)        // define an immutable value and set it to the first output.  
     out = OUTPUTS(1)            // cannot reassign a val (will give error)
     ...

Unlike Scala, ErgoScript does not support the `var` keyword, and thus everything is immutable. 
See below how to use lambda syntax to emulate mutable variables.

Multiple blocks can be joined as in: 

    {
      INPUTS(0).id == SELF.id
    } || {
      INPUTS(0).value == 100000 
    }  

### Public-keys

The above ErgoScript programs are either spendable by everyone or by no one, which is not very useful.

Useful ErgoScript programs are those that allow one to spend the box if they know the private key corresponding 
to some public key, similar to Bitcoin's P2PK addresses. 

ErgoScript provides multiple ways to create such "public-key" scripts, but the most common one uses the predicate `proveDlog(ecPoint)`, 
which evaluates to true if the spender supplies a valid proof of knowledge of the discrete logarithm corresponding to `ecPoint`, a point on an elliptic curve over a finite field. This is equivalent to a "signature" in Bitcoin. 
Ergo uses the same [Secp256k1 curve of Bitcoin](https://en.bitcoin.it/wiki/Secp256k1), so the representation of `ecPoint` is the same, a 33-byte array with the first byte representing the sign (Ergo does not support uncompressed points). 
However, unlike Bitcoin (which uses ECDSA), Ergo uses Schnorr signatures to construct the proofs. 

The following steps illustrate how to create an address encoding the `proveDlog` script. 

1. First obtain the EC point corresponding to the public key. Let us use [the same example of Bitcoin](https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses).
    1. The hex-encoded BigInteger secret is `18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725`.
    2. The corresponding hex-encoded EC point is `0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352`.
    3. Convert the EC point hex to Base64, which turns out to be `AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS`.

2. Create the corresponding script `proveDlog(decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS")))`.

3. Compile the script [to get the address](https://wallet.plutomonkey.com/p2s/?source=cHJvdmVEbG9nKGRlY29kZVBvaW50KGZyb21CYXNlNjQoIkFsQ0dPdFpLaDY2S0wrZzhHdkdvUUR5MVAxUGtodGhSSGEyS0JJaCtXeU5TIikpKQ==) `LQ7iQ4egnCPsZZy5QKsXmaypCRuMxPNtdyGE95fYWCLze8C2hMMwDcAgPNeV8s`

Funds sent to the above address can be spent using the secret above, as can be seen in the transaction with id [dfca9eaa745c79dafbed43b73379fb0008608119080954c337a4022a2a5070a3](https://explorer.ergoplatform.com/en/transactions/dfca9eaa745c79dafbed43b73379fb0008608119080954c337a4022a2a5070a3). 

### Functional Programming

Our next examples demonstrate the functional features of ErgoScript. Suppose we want to allow a box to be spent if all the following 
conditions hold:

1. Spender knows the discrete log of the above EC point `0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352`.
2. All input boxes must be protected by the same ErgoScript program.

The following program encodes these conditions:

    {
       val z = decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS"))
       def sameAsMe(box:Box) = box.propositionBytes == SELF.propositionBytes
       
       proveDlog(z) && INPUTS.forall(sameAsMe)       
    }

The [address corresponding to the above program](https://wallet.plutomonkey.com/p2s/?source=ICAgIHsKICAgICAgIHZhbCB6ID0gZGVjb2RlUG9pbnQoZnJvbUJhc2U2NCgiQWxDR090WktoNjZLTCtnOEd2R29RRHkxUDFQa2h0aFJIYTJLQkloK1d5TlMiKSkKICAgICAgIGRlZiBzYW1lQXNNZShib3g6Qm94KSA9IGJveC5wcm9wb3NpdGlvbkJ5dGVzID09IFNFTEYucHJvcG9zaXRpb25CeXRlcwogICAgICAgcHJvdmVEbG9nKHopICYmIElOUFVUUy5mb3JhbGwoc2FtZUFzTWUpCiAgICB9Cg==) is `3PwBHASpxaJa5i3vmLtUTvEqjbJWcpqnyuX9hSmUbaK2HAmoDLHmYSMm4up5pCRytSStEhsHnzTfpHzvCRZ`
 
One may think that the lack of the `var` keyword may seem restrictive as it enforces everything to be immutable.
For instance, to compute the sum of all the inputs, one might want to store the accumulated value in a `var` and iterate 
over all the inputs, updating the `var` at each iteration.

The following code shows how to compute the sum of all inputs in ErgoScript. Assume that the additional condition
is that the box can only be spent if the sum of all inputs is greater than 1 Erg (or 1000000000 nanoErgs).

    {
       val z = decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS"))
       def sameAsMe(box:Box) = box.propositionBytes == SELF.propositionBytes
       val sum = INPUTS.fold(0L, { (accum:Long, box: Box) => accum + box.value }) 
       
       proveDlog(z) && INPUTS.forall(sameAsMe) && sum > 1000000000       
    }


This [corresponds to the address](https://wallet.plutomonkey.com/p2s/?source=ICAgIHsKICAgICAgIHZhbCB6ID0gZGVjb2RlUG9pbnQoZnJvbUJhc2U2NCgiQWxDR090WktoNjZLTCtnOEd2R29RRHkxUDFQa2h0aFJIYTJLQkloK1d5TlMiKSkKICAgICAgIGRlZiBzYW1lQXNNZShib3g6Qm94KSA9IGJveC5wcm9wb3NpdGlvbkJ5dGVzID09IFNFTEYucHJvcG9zaXRpb25CeXRlcwogICAgICAgdmFsIHN1bSA9IElOUFVUUy5mb2xkKDBMLCB7IChhY2N1bTpMb25nLCBib3g6IEJveCkgPT4gYWNjdW0gKyBib3gudmFsdWUgfSkgCiAgICAgICAKICAgICAgIHByb3ZlRGxvZyh6KSAmJiBJTlBVVFMuZm9yYWxsKHNhbWVBc01lKSAmJiBzdW0gPiAxMDAwMDAwMDAwICAgICAgIAogICAgfQo=)
`49AkSSPuVSQHk17C4JLxhqxH7yL5NMWxdEsELp6MNzYeJZvF7iKk3Jgi4fh96o7RJeaU8JSVPvZ5EhCgboQy9d68QreWaYcVxSUcsd8UCamHPsv9kHzqhe4tAM5D7ZmF` 

### Box Structure

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

### Storing Data 

The most common way to store data on the Ergo blockchain is using *registers* at box creation. The other way to store data is using *context variables* at the time a box is spent. However, we will only discuss the former approach here.
  
An Ergo box consists of ten registers (`R0..R9`), out of which the first four (`R0..R3`) are reserved by the protocol. The remaining six registers (`R4..R9`) are free for storing data and are empty by default. An empty register cannot be sandwiched between full registers. 

The following snippet shows how to use registers in your code:

    {
       val r4 = SELF.R4[GroupElement]
       if (r4.isDefined) {
          val x = r4.get
          proveDlog(x) 
       } else {
          proveDlog(decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS")))
       } 
    }
     
The line `SELF.R4[GroupElement]` returns an `Option[GroupElement]` type. The semantics of the `Option` type is exactly
the [same as in Scala](https://alvinalexander.com/scala/using-scala-option-some-none-idiom-function-java-null/). If the `Option` is defined, i.e., `SELF.R4` indeed contains a `GroupElement` type, then the first branch 
is executed, otherwise, the second branch is executed. 
