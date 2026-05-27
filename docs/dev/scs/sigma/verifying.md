---
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ScorexFoundation/sigmastate-interpreter
    branch: develop
    paths:
      - docs/sigma-dsl.md
  - repo: ergoplatform/ergo-jde
    branch: main
    paths:
      - kiosk/src/test/scala/kiosk/schnorr/SchnorrSpec.scala
  - repo: kushti/chaincash
    branch: master
    paths:
      - src/test/scala/chaincash/ChainCashSpec.scala
source_of_truth:
  - https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407
  - https://github.com/ScorexFoundation/sigmastate-interpreter/tree/develop/docs/sigma-dsl.md
  - https://github.com/ergoplatform/ergo-jde/tree/main/kiosk/src/test/scala/kiosk/schnorr/SchnorrSpec.scala
  - https://github.com/kushti/chaincash/tree/master/src/test/scala/chaincash/ChainCashSpec.scala
---

# Schnorr Signatures

The **Schnorr signature** scheme is a key cryptographic primitive in Ergo, allowing efficient proofs of knowledge over the secp256k1 group. This page explains how to verify a Schnorr signature in **ErgoScript** using the maintained forum pattern and linked tests.

## Overview

Ergo uses the **Secp256k1** elliptic curve (the same curve used in Bitcoin), denoted as **G**, for its Schnorr signature scheme. The Schnorr signature allows a user to prove knowledge of a private key without revealing the key itself.

### Key Setup

1. The **secret key** is an integer **x**.
2. The corresponding **public key** is **Y = g^x**, where **g** is the generator of the elliptic curve group **G**.

## Schnorr Signing Process

To sign message bytes **M** for on-chain verification, use the strong Fiat-Shamir layout from the forum reference:

1. Generate random integer **r** and compute commitment **a = g^r**.
2. Compute challenge bytes **e = blake2b256(aBytes || M || YBytes)**.
3. Interpret **e** as a `BigInt`.
4. Compute response **z = (r + x * e) mod q**.
5. Retry with a new nonce if **z** does not fit ErgoScript's 255-bit `BigInt` limit.

The on-chain-friendly signature is the pair **(a, z)**, where `a` is a `GroupElement` and `z` is encoded as bytes for conversion with `byteArrayToBigInt`.

## Schnorr Signature Verification

The verifier recomputes the challenge:
  \[
  e = H(a || M || Y)
  \]
Then accepts when:
  \[
  g^z = a \cdot Y^e
  \]

---

## On-Chain Verification in ErgoScript

In ErgoScript, verifying a Schnorr signature involves recomputing the challenge on-chain and checking the group equation.

### ErgoScript Example

```scala
{ 
  // Getting the generator of the elliptic curve group 
  val g: GroupElement = groupGenerator

  // Getting the public key Y from R4
  val Y = SELF.R4[GroupElement].get

  // Getting the message bytes from R5
  val message = SELF.R5[Coll[Byte]].get

  // Retrieving the commitment a from context variable 1
  val a = getVar[GroupElement](1).get

  // Retrieving response z from context variable 2
  val zBytes = getVar[Coll[Byte]](2).get
  val z = byteArrayToBigInt(zBytes)
  
  // Strong Fiat-Shamir challenge binds commitment, message, and public key
  val eBytes = blake2b256(a.getEncoded ++ message ++ Y.getEncoded)
  val e = byteArrayToBigInt(eBytes)
  
  // Signature valid if g^z = a * Y^e
  sigmaProp(g.exp(z) == a.multiply(Y.exp(e)))
}
```

### Script Explanation

- The generator of the elliptic curve group (`g`) is retrieved using the global value `groupGenerator`.
- The public key (`Y`) is retrieved from register R4 of the box being spent (`SELF`).
- The message bytes (`message`) are retrieved from register R5 of the box being spent.
- The signature components, commitment (`a`) and response (`z`), are provided as context variables by the prover during transaction creation.
- The script recomputes the challenge with `blake2b256(a.getEncoded ++ message ++ Y.getEncoded)`.
- It verifies `g.exp(z) == a.multiply(Y.exp(e))`. If this equality holds, the signature is valid and `sigmaProp` evaluates to true.

### Reference Test

The complete off-chain and on-chain interaction, including signature generation and verification, can be seen in [this test case](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/schnorr/SchnorrSpec.scala).

---

## Advanced Schnorr Validation Off-Chain

### On-Chain Verification With Explicit Commitment

This pattern verifies a Schnorr proof by passing the commitment `a` and response `z` into the script. The script recomputes the challenge from `a`, the message, and the holder public key, then checks the group equation.

*Note: The primary challenge with on-chain verification is ErgoScript's `BigInt` size limit. Off-chain signature generation must ensure the response `z` fits within this limit.*

```scala
{
    val message = ...

    // Retrieve a of signature (a, z)
    val a = getVar[GroupElement](1).get

    // Retrieve z of signature (a, z)
    val zBytes = getVar[Coll[Byte]](2).get
    val z = byteArrayToBigInt(zBytes)

    // Compute challenge
    val e = blake2b256(a.getEncoded ++ message ++ holder.getEncoded)
    val eInt = byteArrayToBigInt(e)

    // Verify signature by checking if g^z = a * Y^e
    val properSignature = g.exp(z) == a.multiply(holder.exp(eInt))
    
    sigmaProp(properSignature)
}
```

### Off-Chain Signature Generation (Ensuring Size Limit)

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
    val holder = g.exp(secretKey.bigInteger)
    val a: GroupElement = g.exp(r.bigInteger)
    // Calculate challenge e = H(a || msg || holder)
    val e = BigInt(scorex.crypto.hash.Blake2b256(a.getEncoded ++ msg ++ holder.getEncoded))
    // Calculate response z = r + x*e (mod q), matching g^z = a * holder^e
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

- **Challenge binding**: The on-chain challenge should bind the commitment, message, and public key, such as `blake2b256(aBytes ++ message ++ holderBytes)`.
- **BigInt limit**: Off-chain signing must retry with a new nonce until `z` fits within ErgoScript's `BigInt` size limit.
  
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
