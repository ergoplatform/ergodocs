---
tags:
  - Diffie
---

# Diffie-Hellman (DH) Protocol in Ergo

The **Diffie-Hellman (DH)** protocol is a cornerstone of cryptography, allowing two parties to generate a shared secret over a public communication channel. This shared secret can then be used to encrypt future communications. Importantly, **Diffie-Hellman does not involve exchanging the secret itself**—instead, the two parties collaboratively generate it, ensuring that the secret remains secure, even if an observer intercepts their communication.

This principle makes Diffie-Hellman invaluable in settings where **multi-signature** schemes, **ring signatures**, and other privacy-preserving cryptographic protocols are required, such as in Ergo's mixer or stealth address applications.

## Diffie-Hellman Tuple

In the context of Ergo, **Diffie-Hellman tuples** (DHTs) are used to prove knowledge of a shared secret without revealing it. The tuple consists of public group elements **g, h, u, v**, and the goal is to prove knowledge of a secret **x** such that:

$$ u = g^x \quad \text{and} \quad v = h^x $$

The protocol works as follows:

### Interactive Protocol

1. The prover selects a random value **r ←<sup>R</sup> Z<sub>q</sub>** and computes two temporary values **t<sub>0</sub>** and **t<sub>1</sub>**:
   \[
   t_0 = g^r, \quad t_1 = h^r
   \]
   The prover sends **(t<sub>0</sub>, t<sub>1</sub>)** to the verifier.

2. The verifier selects a random challenge **c ←<sup>R</sup> Z<sub>q</sub>** and sends it to the prover.

3. The prover computes the response **z = r + cx** and sends it to the verifier.

4. The verifier accepts the proof if:
   \[
   g^z = t_0 \cdot u^c \quad \text{and} \quad h^z = t_1 \cdot v^c
   \]
This process allows the prover to demonstrate knowledge of **x** without actually revealing **x**.

### Fiat-Shamir Transformation (Non-Interactive Variant)

In blockchain environments like Ergo, interactive protocols are often impractical. Instead, a non-interactive version of the Diffie-Hellman protocol is used, employing the **Fiat-Shamir transformation**. This transformation replaces the verifier’s challenge **c** with a cryptographic hash function **H**:

$$ c = H(t_0 \parallel t_1 \parallel m) $$

Here, **m** is the message to be signed or validated. This makes the protocol non-interactive, as the prover can generate the challenge independently, creating a self-contained proof.

In ErgoScript, this transformation is implemented as **[proveDHTuple](global-functions.md#provedhtuple)(g, h, u, v)**, allowing users to generate non-interactive proofs of Diffie-Hellman tuples.

---

## Use Cases of Diffie-Hellman Tuples in Ergo

### Mixers

Diffie-Hellman tuples are essential for maintaining privacy in Ergo’s **ZeroJoin** mixer, a non-custodial, non-interactive token mixer. The security of ZeroJoin is based on the **Decision Diffie-Hellman (DDH) assumption**, a well-established cryptographic assumption that ensures no information about the secret can be gleaned from the public values exchanged.

- **ZeroJoin** utilizes **ring signatures** and Diffie-Hellman tuples to restore fungibility to digital notes, ensuring that coins become indistinguishable from one another after mixing.
- Ergo's mixers avoid the need for trusted setups or intermediaries, ensuring minimal trust assumptions.

#### Comparison with Other Platforms:

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| No on-chain mixing | Trusted setup-based or inefficient mixers | Efficient, minimal trust assumptions, using ring signatures and DHTs |

For more information, see [ErgoMixer](ergomixer.md).

### Stealth Addresses

Stealth addresses leverage **non-interactive Diffie-Hellman key exchanges** to provide privacy in financial transactions. Each payment generates a new one-time-use address, ensuring that the recipient’s identity remains private while still enabling them to securely receive funds.

- Stealth addresses prevent anyone except the recipient from linking transactions to their public address, significantly enhancing privacy.
- Diffie-Hellman key exchanges are at the core of this functionality, ensuring that only the intended recipient can derive the private key needed to spend the funds.

For more details, refer to the [Stealth Addresses](stealth-address.md) page.

---

## Technical Details

### Fiat-Shamir Transformation

The **Fiat-Shamir transformation** is crucial for turning interactive protocols like Diffie-Hellman into non-interactive ones suitable for blockchain environments. In Ergo, the Fiat-Shamir transformation ensures that proof generation remains non-interactive and compact, making it efficient for on-chain use.

The transformation replaces the interactive challenge **c** with a hash of the prover's commitment and the message being signed:

$$ c = H(t_0 \parallel t_1 \parallel m) $$

This allows the prover to generate the challenge on their own, without needing an external verifier. This transformation is implemented in ErgoScript via functions like **proveDHTuple**, which allows developers to create non-interactive proofs for Diffie-Hellman tuples, among other cryptographic statements.

### Integration in Ergo's Sigma Protocols

In Ergo, Diffie-Hellman tuples are a critical part of the overall **Sigma protocol** framework. By allowing composable cryptographic proofs, Sigma protocols enable developers to create contracts that require privacy-preserving proofs, such as:

- **Ring signatures**: Used in mixers and privacy-focused contracts, where participants can prove they are part of a group without revealing which member they are.
- **Threshold signatures**: Multi-signature setups that require a subset of participants to agree to spend funds.

These proofs can be combined using logical operators such as **AND**, **OR**, and **k-out-of-n**, enabling complex and flexible cryptographic conditions for smart contracts.

---

## Diffie-Hellman Tuple Applications in Ergo

### Example: Proving Knowledge of a Diffie-Hellman Tuple in ErgoScript

Below is an example of how the **proveDHTuple** function can be used in an ErgoScript contract to prove knowledge of a shared secret **x**:

```scala
{
  val g = decodePoint("028D84...")
  val h = decodePoint("02F937...")
  val u = decodePoint("03C89B...")
  val v = decodePoint("02B1DA...")

  proveDHTuple(g, h, u, v)
}
```

This script proves knowledge of **x** such that **u = g^x** and **v = h^x**, enabling privacy-preserving contracts that can securely verify knowledge of shared secrets without revealing them.

---

## Resources

- [Diffie-Hellman tuples support in sigma-rust](https://github.com/ergoplatform/sigma-rust/pull/315)
- [First transaction protected by Diffie-Hellman](https://explorer.ergoplatform.com/en/transactions/24f6996bea6b914d3dab7d645cd5e5b9a57e3ac88b2774d34a2be26bdf708d28)
- [Decision Diffie-Hellman (DDH) Assumption](https://en.wikipedia.org/wiki/Decisional_Diffie%E2%80%93Hellman_assumption)

---

### Conclusion

The Diffie-Hellman protocol plays a vital role in enabling privacy-preserving applications on Ergo, from stealth addresses to mixers like ZeroJoin. By leveraging Diffie-Hellman tuples and their non-interactive proofs through the **Fiat-Shamir transformation**, Ergo enables secure and efficient cryptographic operations. These tools, integrated with Sigma protocols, empower developers to create powerful decentralized applications that prioritize both security and privacy.

For additional details, explore:

- [ErgoMixer](ergomixer.md)
- [Stealth Addresses](stealth-address.md)
