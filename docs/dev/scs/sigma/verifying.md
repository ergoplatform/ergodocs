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
  // (Checking Schnorr signature in a script)
  
  // Getting the generator of the elliptic curve group 
  val g: GroupElement = groupGenerator

  // Getting the public key for a signature
  val Y = SELF.R4[GroupElement].get

  // Getting the message to be signed
  val M = SELF.R5[Coll[Byte]].get

  // Retrieving the c value of the signature (c, s)
  val cBytes = getVar[Coll[Byte]](0).get
  val c = byteArrayToBigInt(cBytes)
  
  // Retrieving the s value of the signature (c, s)
  val s = getVar[BigInt](1).get
  
  // Calculating U = g^s * Y^c
  val U = g.exp(s).multiply(Y.exp(c)).getEncoded // as a byte array
  
  // Checking the validity of the Schnorr signature
  sigmaProp(cBytes == sha256(U ++ M))
}

```

The complete process of signature generation off-chain and verification on-chain is explained in [this test](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/schnorr/SchnorrSpec.scala).

## Off-chain code

The problem with verifying signatures on-chain is that there is only 256-bits big integer data type. 

Thus better to reduce number of bigints used by using simpler textbook version of Schnorr validation (message details missed):


```
{
    val message = ...
    // Computing challenge
    val e: Coll[Byte] = blake2b256(message) // weak Fiat-Shamir
    val eInt = byteArrayToBigInt(e) // challenge as big integer
          
     // a of signature in (a, z)
     val a = getVar[GroupElement](1).get
     val aBytes = a.getEncoded

     // z of signature in (a, z)
     val zBytes = getVar[Coll[Byte]](2).get
     val z = byteArrayToBigInt(zBytes)

     // Signature is valid if g^z = a * x^e
     val properSignature = g.exp(z) == a.multiply(holder.exp(eInt))
    
     sigmaProp(properSignature)
}
```
 
and then in offchain code we need to be sure that `z` big integer fits into 255 bits. The following code is simply iterating over signatures while one which can be provided used on the blockchain 

```
  def randBigInt: BigInt = {
    val random = new SecureRandom()
    val values = new Array[Byte](32)
    random.nextBytes(values)
    BigInt(values).mod(SecP256K1.q)
  }

  @tailrec
  def sign(msg: Array[Byte], secretKey: BigInt): (GroupElement, BigInt) = {
    val r = randBigInt
    val g: GroupElement = CryptoConstants.dlogGroup.generator
    val a: GroupElement = g.exp(r.bigInteger)
    val z = (r + secretKey * BigInt(scorex.crypto.hash.Blake2b256(msg))) % CryptoConstants.groupOrder

    if(z.bitLength <= 255) {
      (a, z)
    } else {
      sign(msg,secretKey)
    }
  }
```


Examples on building transactions can be found in ChainCash repository, e.g. this test  https://github.com/kushti/chaincash/blob/master/src/test/scala/kiosk/ChainCashSpec.scala


/// admonition | Disclaimer
    type: warning

Please note that Schnorr here is using weak Fiat-Shamir transformation, but that should not be a problem as public key is fixed.
///
