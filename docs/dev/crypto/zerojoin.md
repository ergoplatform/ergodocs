# Understanding ZeroJoin

Mixers serve as fundamental tools in the process of restoring fungibility for digital tokens. In Ergo, the first such mechanism implemented is known as ZeroJoin. It's constructed on the foundation of ring signatures and a proof of knowledge for a Diffie-Hellman tuple, defined as *(for publicly known g, h, u, v, there exists w, such as g&w == u and h<sup>w</sup> == v)*.

ZeroJoin employs two-party interactions called Σ-protocols. Specifically, we require two different types of Σ-protocols explained below.

Assume `G` to be a multiplicative group of prime order `q`, where the Decision Diffie-Hellman (DDH) problem is *hard*.

1. The **first protocol** is labeled as `proveDlog(u)`. It is a proof of knowledge of the Discrete Logarithm of a certain group element `u` in relation to a fixed generator `g`. In other words, the prover validates the knowledge of `x` such that u = g<sup>x</sup>, employing Schnorr signatures.  

2. The **second protocol primitive**, denoted `proveDHTuple(g, h, u, v)`, demonstrates proof of knowledge of a Diffie-Hellman Tuple. Here, the prover verifies the knowledge of `x` such that u = g<sup>x</sup> and v = h<sup>x</sup> for arbitrary generators `g` and `h`.

This second protocol essentially runs two instances of the first protocol concurrently.

The protocol proceeds as follows:

1. The prover chooses r from Z<sub>q</sub> at random, calculates (t<sub>0</sub>, t<sub>1</sub>) = (g<sup>r</sup> , h<sup>r</sup>), and forwards (t<sub>0</sub>, t<sub>1</sub>) to the verifier.
2. The verifier randomly selects c from Z<sub>q</sub> and transfers `c` to the prover.
3. The prover then sends `z = r + cx` to the verifier. The verifier accepts if g<sup>z</sup> equals t<sub>0</sub> · u<sup>c</sup> and h<sup>z</sup> equals t<sub>1</sub> · v<sup>c</sup>.

For non-interactive application, we use a variant of the protocol acquired through a Fiat-Shamir transformation. Here, c equals H(t<sub>0</sub>‖t<sub>1</sub>‖m) for a specific message `m` to be signed.

Note that the verification of `proveDHTuple` necessitates four exponentiations, while `proveDlog` requires only two.

Both protocols are supported by ErgoScript, providing the necessary components for implementing ZeroJoin.

![ZeroJoin Image](../../assets/img/scs/zerojoin.png)

For additional information on ZeroJoin, please refer to the [ZeroJoin Presentation](https://storage.googleapis.com/ergo-cms-media/docs/CBT_2020_ZeroJoin_Combining_Zerocoin_and_CoinJoin_v3.pdf).