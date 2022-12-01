# Diffie

Diffie-Hellman is a way of generating a shared secret between two people in such a way that the secret can't be seen by observing the communication. That's an important distinction: **You're not sharing information during the key exchange, you're creating a key together.**

Create a box protected by the script

```
proveDHTuple(g^r, g^y, u^r, u^y).
```

- [Diffie-Hellman tuples support in sigma-rust](https://github.com/ergoplatform/sigma-rust/pull/315)
- [First transaction protected by Diffie-Hellman](https://explorer.ergoplatform.com/en/transactions/24f6996bea6b914d3dab7d645cd5e5b9a57e3ac88b2774d34a2be26bdf708d28)

## Uses

### Mixers


The security of ZeroJoin is based on the Decision Diffie-Hellman (DDH) assumption.

- Basic tool to restore fungibility of digital notes.
- Basic scheme, ZeroJoin, is based on ring signatures and proof of knowledge for a **Diffie-Hellman tuple** 
- [Paper with contracts](https://eprint.iacr.org/2020/560)

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| No onchain mixing | Trusted setup-based or inefficient | Efficient, minimal trust assumptions |


Join is based on two-party interactions called Σ-protocols. Specifically, we need two types of Σ-protocols described below. Let `G` be a multiplicative group of prime order `q` where the decision Diffie-Hellman (DDH) problem is **hard**. 

The **first protocol**, denoted `proveDlog(u)`, is a **proof of knowledge of Discrete Logarithm** of some group element `u` with respect to some fixed generator `g`. 

That is, the prover proves knowledge of `x` such that `u = g x` by using Schnorr signatures. 

The second protocol primitive, denoted `proveDHTuple(g, h, u, v)`, is a proof of knowledge of DiffieHellman Tuple, where the prover proves knowledge of `x` such that `u = g x` and `v = h x` for a arbitrary generators `g` and `h`. 

This is essentially two instances of the first protocol running in parallel as follows.

1. The prover picks `r R ← Zq`, computes `(t0, t1) = (g r , hr )` and sends `(t0, t1)` to the verifier.
2. The verifier picks `c R ← Zq` and sends `c` to prover.
3. The prover sends `z = r + cx` to the verifier, who accepts `if g z = t0 · u c` and `h z = t1 · v c` .

We use the non-interactive variant of the above protocol obtained via the Fiat-Shamir transform, where `c = H(t0kt1km)` for some message `m` to be signed. 

Observe that `proveDHTuple` requires 4 exponentiations for verification, while `proveDlog` requires 2. 

ErgoScript supports both the protocols, and thus has all the primitives needed to implement ZeroJoin.

![](../../../assets/img/scs/zerojoin.png)

### Stealth Addresses

Another solution for improving privacy is using stealth addresses. A stealth address preserves recipient privacy without per-transaction interaction needed (so receiver published an address e.g. on its website, and then sender can obtain some unique one-time address from it.

A solution in Ergo can be based on non-interactive Diffie-Hellman key exchange again. So a merchant, for example, is publishing its public key g^x corresponding to the secret x. Then the buyer with public key g^y obtains shared secret (g^x)^y = (g^y)^x , then the box created by the buyer could be protected by prove_dlog(g^xy for generator g^y). Unfortunately, Ergo does not have prove dlog with custom generator, but it can be bypassed by proveDHTuple(g^y, g^y, g^xy, g^xy) (a little bit weird trick but okay). To have one-time keys, buyer can use one-time secret g^r.

- A tool to hide recipient privacy
- [Contracts](https://www.ergoforum.org/t/stealth-address-contract/255)

This allows a customer to derive a one-time payment address for a store, without revealing the payment to anyone but the store owner. 


| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |