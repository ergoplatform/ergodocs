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

See [ErgoMixer](ergomixer.md) for more information.


### Stealth Addresses

Stealth Addresses are crafted to ensure *recipient* privacy during transactions. Leveraging a non-interactive [Diffie-Hellman key exchange](diffie.md), they facilitate the creation of distinct one-time addresses for every transaction. While enabling recipients to securely receive funds, the linkage between the transactions and their original public address remains concealed, thereby significantly enhancing the recipient's privacy throughout the transactions.

See the [Stealth Addresses](stealth-address.md) page for more information.


## Resources
- [Diffie-Hellman tuples support in sigma-rust](https://github.com/ergoplatform/sigma-rust/pull/315)
- [First transaction protected by Diffie-Hellman](https://explorer.ergoplatform.com/en/transactions/24f6996bea6b914d3dab7d645cd5e5b9a57e3ac88b2774d34a2be26bdf708d28)
