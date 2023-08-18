---
tags:
  - Privacy
  - Decision Diffie-Hellman
---
# Exploring ZeroJoin

Mixers are crucial tools for restoring fungibility in digital tokens. In Ergo, ZeroJoin is the first such mechanism implemented. It's built on the principles of ring signatures and a proof of knowledge for a Diffie-Hellman tuple, defined as *(for publicly known g, h, u, v, there exists w, such as g&w == u and h<sup>w</sup> == v)*.

ZeroJoin utilizes two-party interactions known as Σ-protocols. We focus on two distinct types of Σ-protocols as explained below.

Let's consider `G` as a multiplicative group of prime order `q`, where the Decision Diffie-Hellman (DDH) problem is *hard*.

1. The **first protocol**, termed as `proveDlog(u)`, is a proof of knowledge of the Discrete Logarithm of a specific group element `u` in relation to a fixed generator `g`. Essentially, the prover confirms the knowledge of `x` such that u = g<sup>x</sup>, using Schnorr signatures.  

2. The **second protocol primitive**, denoted as `proveDHTuple(g, h, u, v)`, shows proof of knowledge of a Diffie-Hellman Tuple. In this case, the prover confirms the knowledge of `x` such that u = g<sup>x</sup> and v = h<sup>x</sup> for arbitrary generators `g` and `h`.

This second protocol essentially executes two instances of the first protocol simultaneously.

The protocol operates as follows:

1. The prover randomly selects r from Z<sub>q</sub>, computes (t<sub>0</sub>, t<sub>1</sub>) = (g<sup>r</sup> , h<sup>r</sup>), and sends (t<sub>0</sub>, t<sub>1</sub>) to the verifier.
2. The verifier randomly picks c from Z<sub>q</sub> and sends `c` to the prover.
3. The prover then forwards `z = r + cx` to the verifier. The verifier accepts if g<sup>z</sup> equals t<sub>0</sub> · u<sup>c</sup> and h<sup>z</sup> equals t<sub>1</sub> · v<sup>c</sup>.

For non-interactive applications, we employ a variant of the protocol obtained through a Fiat-Shamir transformation. In this case, c equals H(t<sub>0</sub>‖t<sub>1</sub>‖m) for a specific message `m` to be signed.

It's important to note that the verification of `proveDHTuple` requires four exponentiations, while `proveDlog` only needs two.

Both protocols are supported by ErgoScript, offering the essential components for implementing ZeroJoin.

![ZeroJoin Image](../../assets/img/scs/zerojoin.png)

For more details on ZeroJoin, please refer to the [ZeroJoin Presentation](https://storage.googleapis.com/ergo-cms-media/docs/CBT_2020_ZeroJoin_Combining_Zerocoin_and_CoinJoin_v3.pdf).
