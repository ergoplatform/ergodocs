---
tags:
  - Signature Schemes
---

# Signature Scheme Internals on Ergo

This document gives a clear view of the signature schemes in the Ergo blockchain. Transactions rely on cryptographic signatures that ensure only authorized parties approve spending and that data integrity stays intact. This page outlines the internal mechanics and the concrete form that scripts and libraries use in Ergo. References point to [`sigmastate-interpreter`](https://github.com/ScorexFoundation/sigmastate-interpreter) and [`sigma-rust`](https://github.com/ergoplatform/sigma-rust), and to the forum post “Verifying Schnorr Signatures in ErgoScript” at https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407.

## Overview

In the Ergo blockchain, signature schemes prove that a transaction came from the owner of the relevant private key. This protects funds and supports secure smart contracts. Ergo uses Schnorr signatures and Sigma protocols.

Two repositories provide the main code paths:

- [`sigmastate-interpreter`](https://github.com/ScorexFoundation/sigmastate-interpreter): Scala-based ErgoTree interpretation and verification.
- [`sigma-rust`](https://github.com/ergoplatform/sigma-rust): Rust-based cryptographic primitives and APIs for native and WASM targets.

### 1. Schnorr Signatures

Schnorr signatures form a core tool in Ergo. The scheme is simple, efficient, and secure under the discrete logarithm assumption. ErgoScript favors a signature pair `(a: GroupElement, z: BigInt)` for on-chain checks, as described in the forum post at https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407.

#### Concrete form for Ergo

- Curve: secp256k1.  
- Generator in ErgoScript: `groupGenerator`.  
- Public key: `Y = g^x`, with secret scalar `x`.  
- Challenge hash on-chain: `blake2b256`.

**Signing flow (off-chain):**

1. Pick a fresh nonce `r`.  
2. Set `a = g^r`.  
3. Set `eBytes = blake2b256(aBytes || message || YBytes)`.  
4. Interpret `e = byteArrayToBigInt(eBytes)`.  
5. Set `z = (r + x * e) mod q`.  
6. Ensure `z.bitLength <= 255`. If not, pick a new `r` and retry.

**Verification flow (on-chain in ErgoScript):**

- Layout:
  - `R4`: `Y` as `GroupElement`.
  - `R5`: `message` as `Coll[Byte]`.
  - Context var `1`: `a` as `GroupElement`.
  - Context var `2`: `z` as `Coll[Byte]` (encode `z` off-chain).

- Check:
  - `eBytes = blake2b256(aBytes || message || YBytes)`.
  - `e = byteArrayToBigInt(eBytes)`.
  - Accept if `g^z == a * Y^e`.

**Drop-in script (aligned with the forum post at https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407):**
```scala
{
  val g: GroupElement = groupGenerator

  val Y: GroupElement = SELF.R4[GroupElement].get
  val message: Coll[Byte] = SELF.R5[Coll[Byte]].get

  val a: GroupElement = getVar.get
  val zBytes: Coll.get
  val z: BigInt = byteArrayToBigInt(zBytes)

  val eBytes: Coll[Byte] = blake2b256(a.getEncoded ++ message ++ Y.getEncoded)
  val e: BigInt = byteArrayToBigInt(eBytes)

  val ok = g.exp(z) == a.multiply(Y.exp(e))
  sigmaProp(ok)
}
```

**Notes:**

* Use `blake2b256` for `e` during signing and verification.
* Keep `z` within 255 bits to satisfy the on-chain `BigInt` limit.
* Keep byte layouts identical off-chain and on-chain.

For background on the discrete log protocol and Schnorr logic in Scala, see [`DLogProtocol.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/sigmastate/crypto/DLogProtocol.scala). Rust-side helpers for wallets appear in [`signing.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/wallet/signing.rs) and key management appears in [`secret_key.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/wallet/secret_key.rs).

### 2. Sigma Protocols

Sigma protocols allow a prover to convince a verifier that a statement about a secret holds, without disclosure of the secret. Each proof follows three steps: commitment, challenge, and response. The Fiat–Shamir transform replaces the verifier’s challenge with a hash.

Core pieces in Ergo:

* **DLog**: knowledge of `x` such that `Y = g^x`.
* **AND / OR**: composition over multiple statements.
* **Threshold**: proof that at least `k` out of `n` statements hold.

Scala-side proof creation and checking live in the interpreter and related modules. See [`ErgoLikeInterpreter.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/org/ergoplatform/ErgoLikeInterpreter.scala) and proof serialization in [`SigSerializer.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/sigmastate/SigSerializer.scala). Rust-side proof data in transactions appears in [`prover_result.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/chain/transaction/input/prover_result.rs).

### 3. ErgoTree and Signature Schemes

ErgoTree defines spending rules for boxes (UTXOs). Scripts may require one signature, several signatures, time checks, or mixed conditions.

Examples:

* Single-key spending with a DLog proof for one `Y`.
* Multi-signature with `AND` or threshold logic.
* Policies that include height checks along with signatures.

The Scala interpreter verifies each node and enforces the script. See [`ErgoLikeInterpreter.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/org/ergoplatform/ErgoLikeInterpreter.scala). Rust-side contract helpers appear in [`contract.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/chain/contract.rs).

### 4. Implementation in Ergo

Both repositories cover the same cryptographic ideas with language-specific APIs.

* **sigmastate-interpreter**:

  * Core verification logic: [`ErgoLikeInterpreter.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/org/ergoplatform/ErgoLikeInterpreter.scala)
  * Discrete log protocol: [`DLogProtocol.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/sigmastate/crypto/DLogProtocol.scala)
  * Proof serialization: [`SigSerializer.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/main/scala/sigmastate/SigSerializer.scala)

* **sigma-rust**:

  * Signing helpers: [`signing.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/wallet/signing.rs)
  * Secret key management: [`secret_key.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/wallet/secret_key.rs)
  * Proofs in transactions: [`prover_result.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/chain/transaction/input/prover_result.rs)
  * Contract helpers: [`contract.rs`](https://github.com/ergoplatform/sigma-rust/blob/develop/ergo-lib/src/chain/contract.rs)

### 5. Security Considerations

* Strong nonce generation for `r`.
* No nonce reuse across messages.
* The `z ≤ 255 bits` rule in the signer.
* Exact byte concatenation for `a`, `message`, and `Y` in the challenge.
* Consistent `blake2b256` use in both directions.
* Test coverage that includes valid and invalid paths.
* Reference tests in Scala: [`SigningSpecification.scala`](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/test/scala/sigmastate/crypto/SigningSpecification.scala).

### 6. Use Cases and Applications

* Confidential flows that rely on Sigma conditions.
* Multi-signature wallets with `AND` or threshold rules.
* Access rules for dApps that combine signatures with height checks.
* Voting or attestations that depend on key possession.

### Off-chain helper: reference signer (Scala-style sketch)

```scala
import java.security.SecureRandom
import org.ergoplatform.sdk.wallet.secp256k1.{CryptoConstants => CC}
import special.sigma.GroupElement

def randScalar(): BigInt = {
  val bytes = new Array
  new SecureRandom().nextBytes(bytes)
  (BigInt(1, bytes) % CC.groupOrder)
}

@annotation.tailrec
def sign(message: Array[Byte], x: BigInt): (GroupElement, Array[Byte]) = {
  val g = CC.dlogGroup.generator
  val Y = g.exp(x.bigInteger)

  val r = randScalar()
  val a = g.exp(r.bigInteger)

  val aBytes = a.getEncoded.toArray
  val YBytes = Y.getEncoded.toArray
  val eBytes = scorex.crypto.hash.Blake2b256(aBytes ++ message ++ YBytes)
  val e = BigInt(1, eBytes)

  val z = (r + x * e) % CC.groupOrder

  if (z.bitLength <= 255) (a, z.toByteArray)
  else sign(message, x)
}
```

### Conclusion

Ergo uses Schnorr signatures and Sigma protocols in a form that scripts can verify on-chain without friction. The `(a, z)` signature form, the `blake2b256` challenge, the `g^z == a * Y^e` check, and the `z` ≤ 255-bit rule give a recipe that matches real scripts and tools. Detailed reasoning and examples appear in the forum post at [https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407](https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407) and in the repositories at [https://github.com/ScorexFoundation/sigmastate-interpreter](https://github.com/ScorexFoundation/sigmastate-interpreter) and [https://github.com/ergoplatform/sigma-rust](https://github.com/ergoplatform/sigma-rust).
