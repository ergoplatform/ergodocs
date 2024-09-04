# Schnorr Signature

In the simplest case, a signature in an Ergo transaction is a **Schnorr signature**. In more complex cases, it corresponds to a **subset of Generalized Schnorr Proofs**, which are used in privacy-preserving applications and advanced cryptographic protocols.

The **Schnorr signature** is a core cryptographic primitive in Ergo, used both in basic transaction validation and as part of more complex proof systems. It is simple, efficient, and secure, making it an ideal choice for the wide range of cryptographic functionalities in Ergo.

## Overview

Ergo’s Schnorr signatures are implemented using the **SecP256K1 elliptic curve**, the same curve used in Bitcoin. The flexibility of Schnorr signatures enables Ergo to support a range of applications, from simple transactions to more advanced multi-signature schemes and privacy-enhancing protocols.

### Key Properties:

- **Elliptic Curve**: Ergo uses **SecP256K1**, ensuring compatibility with Bitcoin-based systems.
- **Generalized Proofs**: In Ergo, Schnorr signatures can be generalized into complex Sigma protocol proofs that allow for privacy-preserving multi-party computations and other advanced cryptographic applications.
- **Standards Compliance**: Ergo’s implementation closely follows established cryptographic standards (RFCs), allowing for interoperability with protocols like **MuSig**.

---

## How Schnorr Signatures Work

The Schnorr signature process consists of **key generation**, **signing**, and **verification**.

### Key Generation

- A user generates a private key \( x \) and computes the corresponding public key \( P = xG \), where \( G \) is the generator point on the elliptic curve.

### Signing

To sign a message \( m \), the following steps are performed:

1. Generate a random nonce \( k \) and compute \( R = kG \).
2. Hash the values \( R \), \( P \), and the message \( m \) to generate a challenge \( e \):
   \[
   e = H(R \parallel P \parallel m)
   \]
3. Compute the signature \( s \) as:
   \[
   s = k + ex
   \]

### Verification

To verify a signature \( (s, e) \), the verifier computes:
\[
R' = sG - eP
\]
and checks if:
\[
e = H(R' \parallel P \parallel m)
\]
If the condition holds, the signature is valid, demonstrating that the signer knows the private key corresponding to the public key \( P \).

---

## Generalized Schnorr Proofs

In more complex cases, Ergo extends Schnorr signatures into **Generalized Schnorr Proofs** as part of the Sigma protocol framework. These generalized proofs enable advanced cryptographic functionalities such as:

- **Multi-Signature Protocols**: Implementations like **MuSig**, which allows multiple participants to collectively sign a transaction. This reduces the overall transaction size and preserves privacy by aggregating public keys and signatures.
- **Ring Signatures**: Where one can prove they belong to a group of signers without revealing which specific individual signed the message.
- **Threshold Signatures**: Schemes like **k-out-of-n** signatures, where a subset of signers must collaborate to authorize a transaction.

---

## Use Cases of Schnorr Signatures

### 1. **MuSig (Multi-Signature Protocols)**

The **MuSig** protocol allows multiple participants to collaboratively generate a Schnorr signature. This enhances privacy and efficiency, as the final signature is indistinguishable from a regular Schnorr signature, and the transaction size is reduced.

- **Use Case**: Multi-signature wallets, where multiple parties must sign off on a transaction.
- **Privacy**: The individual signers are indistinguishable from each other.

### 2. **Adaptor Signatures for Atomic Swaps**

Adaptor signatures are an extension of Schnorr signatures that facilitate **atomic swaps** and cross-chain exchanges. These signatures enable conditional transactions, allowing a swap to be completed only when a specific secret is revealed.

### 3. **Privacy-Preserving Transactions**

Ergo uses Schnorr signatures in combination with Sigma protocols to enable **privacy-preserving applications**, such as:

- **Mixers**: Anonymous transaction systems like **ZeroJoin** rely on Schnorr-based ring signatures.
- **Stealth Addresses**: Ensure recipient privacy by generating one-time addresses for each transaction.

---

## Sigma Protocols and Schnorr Signatures

Schnorr signatures are a foundational part of Ergo’s **Sigma protocol** framework. Sigma protocols generalize Schnorr signatures, allowing them to be composed into complex cryptographic proofs. For example:

- **Ring signatures**: Prove that a signer belongs to a group without revealing which individual actually signed.
- **Threshold signatures**: Require collaboration between multiple parties to authorize a transaction.
- **Non-Interactive Proofs**: Sigma proofs can be transformed into non-interactive proofs via the **Fiat-Shamir transformation**, which allows them to be used in blockchain environments without interactive verification.

---

## Resources for Developers

To dive deeper into Schnorr signatures and how they are implemented in Ergo, refer to the following resources:

- **Schnorr-based signing function**: [Sign function based on Schnorr protocol](https://github.com/ErgoGravity/gateway-proxy/blob/9cbf72b934b08e258457367e366050a1734f1050/app/gateway/Adaptor.scala#L391).
- **Generalized Schnorr proofs**: Learn how **SigmaBoolean** is used to create advanced cryptographic conditions on the Ergo blockchain in the [SigmaBoolean Documentation](sigmaboolean.md).

---

## Conclusion

Schnorr signatures are central to Ergo’s cryptographic framework, both as simple transaction signatures and as the basis for **Generalized Schnorr Proofs**. By leveraging Sigma protocols, Ergo extends Schnorr signatures into powerful cryptographic tools for privacy-preserving applications, multi-signature schemes, and complex cryptographic contracts.

For developers, these tools enable the creation of advanced decentralized applications (dApps) that prioritize both privacy and security. As part of the broader cryptographic infrastructure, Schnorr signatures ensure that Ergo remains at the forefront of privacy-focused blockchain technology.

For further reading, explore:

- [MuSig paper](https://eprint.iacr.org/2018/068)
- [Adaptor Signatures](https://eprint.iacr.org/2018/123.pdf)
- [SigmaBoolean Documentation](sigmaboolean.md)
