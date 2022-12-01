# Schnorr Signatures

There are several use-cases where you might need to verify a Schnorr signature on-chain.

This page describes how to do so in ErgoScript.

## Initial Setup

Ergo uses the same curve as Bitcoin (Secp256k1), which we call **G**. 

The curve also defines a default generator **g**.

1. Secret key is integer **x** 
2. Public key is **Y = g<sup>x</sup>**, an element of **G**

## Signing

Let the hash of the message to be signed be **M**. The signature is computed as follows:

1. Generate a random integer **r** and compute **U = g<sup>r</sup>**. 
2. Compute the integer **c = Hash(U || M)** 
3. Compute **s = r - cx**.
4. Send the value **(c, s)** to the verifier as the "signature"

Note that the signature is a **pair of integers**.

## Verification

### Schnorr Identification

To understand verification, first consider a variant called *Schnorr identification*.

In this, instead of **(c, s)**, the value **(U, s)** (a group element and an integer) is sent.

The verifier computes **c = Hash(U || M)** and accepts if **g<sup>s</sup> = U / Y<sup>c</sup>**.

This works because  **LHS = g<sup>s</sup> = g<sup>(r - cx)</sup> = g<sup>r</sup> / (g<sup>x</sup>)<sup>c</sup> = RHS**.  

### Schnorr Signature Verification

Given the signature **(c, s)**, we perform the "reverse" of the identification in some sense.

Recall that the verifier of the identification scheme computes **c** from **U** using **Hash** and then verifies some condition.

The verifier of the signature scheme instead computes **U** from **c** using the condition and then verifies **Hash**.

In other words, the verifier first computes **U = g<sup>s</sup>  Y<sup>c</sup>** and accepts if **c = Hash(U || M)**.

## Verification in ErgoScript

We use the following setup in our example: 

1. The public key **Y** is provided as a **GroupElement** in R4. 
2. The message **M** is provided as a **[Coll](../../sigma/lang-spec/#collt)[Byte]** in R5.
3. The value **c** of the signature is provided as a **Coll[Byte]** (for convenience) in context variable 0.
4. The value **s** of the signature is provided as a **[BigInt](../../sigma/lang-spec/#data-types)** in context variable 1.
5. The hash function is [Sha256](../../global-functions/#sha256). 

Which looks like this in ErgoScript

```scala
{
  // Checking Schnorr signature in a script
  val g: GroupElement = groupGenerator

  // Public key for a signature
  val Y = SELF.R4[GroupElement].get

  // Message to sign
  val M = SELF.R5[Coll[Byte]].get

  // c of signature in (c, s)
  val cBytes = getVar[Coll[Byte]](0).get
  val c = byteArrayToBigInt(cBytes)
  
  // s of signature in (c, s)
  val s = getVar[BigInt](1).get
  
  val U = g.exp(s).multiply(Y.exp(c)).getEncoded // as a byte array
  
  sigmaProp(cBytes == sha256(U ++ M))
}
```

The complete process of signature generation off-chain and verification on-chain is explained in [this test](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/schnorr/SchnorrSpec.scala).