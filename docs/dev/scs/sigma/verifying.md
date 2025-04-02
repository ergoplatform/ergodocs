# Schnorr Signatures

The **Schnorr signature** scheme is a key cryptographic primitive in Ergo, allowing for efficient, simple, and secure signatures. Whether verifying a transaction or proving the ownership of a private key on-chain, Schnorr signatures play a central role. This page explains how to verify a Schnorr signature in **ErgoScript**, starting from basic signing and verification steps to advanced on-chain validation.

## Overview

Ergo uses the **Secp256k1** elliptic curve (the same curve used in Bitcoin), denoted as **G**, for its Schnorr signature scheme. The Schnorr signature allows a user to prove knowledge of a private key without revealing the key itself.

### Key Setup:
1. The **secret key** is an integer **x**.
2. The corresponding **public key** is **Y = g^x**, where **g** is the generator of the elliptic curve group **G**.

## Schnorr Signing Process

To sign a message **M** (the hash of the message), follow these steps:

1. Generate a random integer **r** and compute **U = g^r**.
2. Compute the challenge **c = Hash(U || M)**.
3. Compute the response **s = r - cx**.

The signature is the pair **(c, s)**, which is sent to the verifier.

## Schnorr Signature Verification

### Schnorr Identification

Before diving into signature verification, it's helpful to understand the Schnorr identification process, a variant of Schnorr signatures:

- Instead of sending **(c, s)**, the prover sends **(U, s)** (a group element and an integer).
- The verifier computes **c = Hash(U || M)** and checks if:
  \[
  g^s = U / Y^c
  \]
  This works because:
  \[
  g^s = g^{r - cx} = g^r / (g^x)^c = U / Y^c
  \]
  
### Schnorr Signature Verification

For Schnorr signatures, the signature **(c, s)** is verified differently. The verifier computes **U = g^s \cdot Y^c** and checks if:
  \[
  c = Hash(U || M)
  \]
This process ensures that the signature is valid and was produced by the holder of the secret key corresponding to the public key **Y**.

---

## On-Chain Verification in ErgoScript

In ErgoScript, verifying a Schnorr signature involves reconstructing **U** on-chain and checking the challenge.

### ErgoScript Example:

```scala
{ 
  // Getting the generator of the elliptic curve group 
  val g: GroupElement = groupGenerator

  // Getting the public key Y from R4
  val Y = SELF.R4[GroupElement].get

  // Getting the message M from R5
  val M = SELF.R5[Coll[Byte]].get

  // Retrieving the c value (challenge) from context variable 0
  val cBytes = getVar .get
  val c = byteArrayToBigInt(cBytes)

  // Retrieving the s value (response) from context variable 1
  val s = getVar .get
  
  // Calculating U = g^s * Y^c
  val U = g.exp(s).multiply(Y.exp(c)).getEncoded // as a byte array
  
  // Checking if the Schnorr signature is valid
  sigmaProp(cBytes == sha256(U ++ M))
}
```

### Script Explanation:

- The generator of the elliptic curve group (`g`) is retrieved using the global value `groupGenerator`.
- The public key (`Y`) is retrieved from register R4 of the box being spent (`SELF`).
- The message hash (`M`) is retrieved from register R5 of the box being spent.
- The signature components, challenge (`cBytes`) and response (`s`), are provided as context variables by the prover during transaction creation.
- The script reconstructs the commitment `U` using the formula `g^s * Y^c`.
- Finally, it verifies the signature by hashing the reconstructed `U` concatenated with the message `M` (`sha256(U ++ M)`) and comparing the result with the original challenge `cBytes`. If they match, the signature is valid, and the `sigmaProp` evaluates to true.

### Reference Test:
The complete off-chain and on-chain interaction, including signature generation and verification, can be seen in [this test case](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/schnorr/SchnorrSpec.scala).

---

## Advanced Schnorr Validation Off-Chain

### Alternative On-Chain Verification (Using Identification Scheme Logic):
While the above method directly verifies the Schnorr signature `(c, s)`, an alternative approach based on the Schnorr *identification* scheme logic can sometimes be simpler, though it requires providing `U` (or `a` in the code below) instead of `c` as part of the proof.

*Note: The primary challenge with on-chain verification is that ErgoScript's `BigInt` is limited to 256 bits. Off-chain signature generation must ensure the response `s` (or `z` below) fits within this limit.*

```scala
{
    val message = ...
    // Compute challenge
    val e: Coll[Byte] = blake2b256(message)
    val eInt = byteArrayToBigInt(e) // Challenge as big integer
          
    // Retrieve a of signature (a, z)
    val a = getVar .get
    val aBytes = a.getEncoded

    // Retrieve z of signature (a, z)
    val zBytes = getVar .get
    val z = byteArrayToBigInt(zBytes)

    // Verify signature by checking if g^z = a * Y^e
    val properSignature = g.exp(z) == a.multiply(holder.exp(eInt))
    
    sigmaProp(properSignature)
}
```

### Off-Chain Signature Generation (Ensuring Size Limit):

To ensure the response **z** fits within 255 bits (required for ErgoScript's `BigInt`), the off-chain signing code might need to iterate until a suitable random nonce `r` is found:

```scala
  def randBigInt: BigInt = {
    val random = new SecureRandom()
    val values = new Array 
    random.nextBytes(values)
    BigInt(values).mod(SecP256K1.q)
  }

  @tailrec // Scala annotation for tail recursion optimization
  def sign(msg: Array[Byte], secretKey: BigInt): (GroupElement, BigInt) = {
    val r = randBigInt // Generate random nonce
    val g: GroupElement = CryptoConstants.dlogGroup.generator
    val a: GroupElement = g.exp(r.bigInteger) // Calculate U = g^r
    // Calculate challenge e = H(a || msg) - using Blake2b256 here
    val e = BigInt(scorex.crypto.hash.Blake2b256(a.getEncoded ++ msg)) 
    // Calculate response z = r + x*e (mod q) - Note: Schnorr formula is typically r - x*e or r + x*e depending on convention
    val z = (r + secretKey * e) % CryptoConstants.groupOrder 

    // Check if z fits within 255 bits for ErgoScript compatibility
    if(z.bigInteger.bitLength <= 255) { 
      (a, z) // Return signature (a, z)
    } else {
      sign(msg, secretKey) // Retry with a new random nonce r
    }
  }
```

For further examples of constructing off-chain transactions and verifying them on-chain, refer to the [ChainCash repository](https://github.com/kushti/chaincash/blob/master/src/test/scala/kiosk/ChainCashSpec.scala).

---

## Considerations and Limitations

- **Weak Fiat-Shamir Transformation**: The standard Schnorr signature verification shown (`c = H(U || M)`) uses a basic form of the Fiat-Shamir transformation. This is generally secure when the public key `Y` is fixed and known. However, be aware of potential security implications in more complex protocols where public keys might be dynamic or interact in unexpected ways. Stronger transformations might be needed in such advanced scenarios.
  
---

## Conclusion

Schnorr signatures in Ergo provide a powerful, efficient, and flexible way to handle cryptographic authentication both on-chain and off-chain. Whether it's a simple transaction signature or a complex proof involving multi-signatures or privacy-preserving mechanisms, ErgoScript’s built-in support for Schnorr signatures makes it easy to implement.

For more details, explore:

- The [SchnorrSpec test case](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/schnorr/SchnorrSpec.scala), which demonstrates both on-chain verification of Schnorr signatures and off-chain signature generation in ErgoScript.
- The [ChainCash repository](https://github.com/kushti/chaincash/blob/master/src/test/scala/kiosk/ChainCashSpec.scala) for further examples of Schnorr-based signature transactions and how to integrate them in more complex use cases.

By understanding and leveraging Schnorr signatures in Ergo, you can implement secure, efficient, and scalable cryptographic proofs for a variety of applications, ranging from simple transactions to privacy-preserving protocols like atomic swaps, ring signatures, and threshold signatures.

---

## Resources

1. **Schnorr Signature Paper**: [MuSig: A New Multi-Signature Standard](https://eprint.iacr.org/2018/068) – A foundational paper on Schnorr multi-signatures.
2. **Adaptor Signatures**: [Adaptor Signatures for Cross-Chain Protocols](https://eprint.iacr.org/2018/123.pdf) – A deep dive into the use of Schnorr signatures for atomic swaps and privacy-preserving transactions.
3. **Elliptic Curve Cryptography**: [SecP256K1 Curve Information](https://en.bitcoin.it/wiki/Secp256k1) – Detailed information on the elliptic curve used in both Bitcoin and Ergo.
4. **SigmaBoolean Documentation**: [SigmaBoolean in Ergo](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/sigma-dsl.md) – Documentation on how to use SigmaBoolean and generalized Schnorr proofs in Ergo smart contracts.
