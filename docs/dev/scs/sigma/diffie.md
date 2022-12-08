# Diffie

Diffie-Hellman generates a shared secret between two people so that the secret cannot be seen by observing the communication. That is an important distinction: 

**You are not sharing information during the key exchange. You are creating a key together.** This is useful for creating shared public keys in MultiSig and Ring Signature settings.


## Diffie-Hellman Tuple

Let **g, h, u, v** be public group elements. 

The prover proves knowledge of **x** such that **u = g<sup>x</sup>** and **v = h<sup>x</sup>**

1. The prover picks **r ←<sup>R</sup> Z<sub>q</sub>**, computes (**t<sub>0</sub>, t<sub>1</sub>**) = (**g<sup>r</sup> , h<sup>r</sup>**) and sends (**t<sub>0</sub>, t<sub>1</sub>**) to the verifier.
2. The verifier picks **c ←<sup>R</sup>  Z<sub>q</sub>** and sends **c** to prover.
3. The prover sends **z = r + cx** to the verifier, who accepts if **g<sup>z</sup> = t<sub>0</sub> · u<sup>c</sup>** and **h<sup>z</sup> = t<sub>1</sub> · v<sup>c</sup>**.

## Fiat-Shamir Transformation

You can obtain a **non-interactive variant** of the above protocol via a *Fiat-Shamir transformation*, where **c = H(t<sub>0</sub>‖t<sub>1</sub>‖m)** (for some message **m** to be signed).

We call this **[proveDHTTuple](../../global-functions/#provedhtuple)(g, h, u, v)**

## Uses
### Mixers


The security of ZeroJoin is based on the [Decision Diffie-Hellman (DDH) assumption](https://en.wikipedia.org/wiki/Decisional_Diffie%E2%80%93Hellman_assumption), a computational hardness assumption about a certain problem involving discrete logarithms in cyclic groups.

- A basic tool to restore the fungibility of digital notes.
- Basic scheme, ZeroJoin, is based on ring signatures and proof of knowledge for a **Diffie-Hellman tuple** 
- [Paper with contracts](https://eprint.iacr.org/2020/560)

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| No onchain mixing | Trusted setup-based or inefficient | Efficient, minimal trust assumptions |



### Stealth Addresses

Another solution for improving privacy is using stealth addresses. A stealth address preserves recipient privacy without per-transaction interaction needed (so the receiver publishes an address, e.g. on its website, and then the sender can obtain some unique one-time address from it.

A solution in Ergo can be based on a non-interactive Diffie-Hellman key exchange. 

- So a merchant, for example, is publishing its public key **g<sup>x</sup>** corresponding to the secret **x**. 
- Then the buyer with public key **g<sup>y</sup>** obtains shared secret **(g<sup>x</sup>)<sup>y</sup> = (g<sup>y</sup>)<sup>x</sup>**
- The box created by the buyer could be protected by **[ProveDLog](../../global-functions/#provedlog)(g<sup>xy</sup>** for generator **g<sup>y</sup>**).
- Unfortunately, Ergo ProveDLog in Ergo does not support custom generators, but it can be bypassed with a little Ergo magic: **proveDHTuple(g<sup>y</sup>, g<sup>y</sup>, g<sup>xy</sup>, g<sup>xy</sup>)**. 
The buyer can use a one-time secret **g<sup>r</sup>**for one-time keys.



| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |

Some [draft contracts](https://www.ergoforum.org/t/stealth-address-contract/255) are available. 


## Resources
- [Diffie-Hellman tuples support in sigma-rust](https://github.com/ergoplatform/sigma-rust/pull/315)
- [First transaction protected by Diffie-Hellman](https://explorer.ergoplatform.com/en/transactions/24f6996bea6b914d3dab7d645cd5e5b9a57e3ac88b2774d34a2be26bdf708d28)
