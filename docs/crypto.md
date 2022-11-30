# Ergo: A Platform for Cryptographic Applications.

[ErgoScript](ergoscript.md) incorporates proving and verifying as first-class primitives, giving developers access to a subclass of cryptographic proof systems known as non-interactive **Σ-protocols** (pronounced “sigma-protocols”). A script protecting a transaction output can contain statements (**Σ-statements**) that need to be proven (by producing **Σ-proofs**) to spend the output.

Conceptually, [Σ-proofs](https://arxiv.org/abs/1801.00687) are generalizations  of digital signatures. The Schnorr signature scheme  (whose more recent version is popularly known as [EdDSA](https://ed25519.cr.yp.to/)) is the canonical example of a Σ-proof: it proves that the recipient knows the discrete logarithm of the public key (the proof is attached to a specific message, such as a particular transaction, and thus becomes a signature on the message; all Σ-proofs described here are attached to specific messages). 

Σ-protocols exist for proving a variety of properties and, importantly for ErgoScript, elementary Σ-protocols can be combined into more sophisticated ones using the techniques described in [*Proofs of Partial Knowledge and Simplified Design of Witness Hiding Protocols*](http://www.win.tue.nl/~berry/papers/crypto94.pdf).

For an introduction to Σ-protocols, we refer the reader to the paper [*On Σ-protocols*](http://www.cs.au.dk/~ivan/Sigma.pdf).

**ErgoScript provides two elementary Σ-protocols over a group of prime order (such as an elliptic curve)**

- A proof of knowledge of discrete logarithm with respect to a fixed group generator: (Also known as a **Schnorr signature**).
- A proof that of equality of discrete logarithms (i.e., a proof of a **Diffie-Hellman** tuple)

There are proofs of Schnorr (discrete log) and Diffie-Hellman tuple but more can be added via a soft fork. Native support for ring and threshold signatures, where from k-out-of-n signatures, it could not be concluded which k signers were real.

ErgoScript also provides the ability to build more sophisticated Σ-protocols by using connectives AND, OR, and THRESHOLD (also known as k-out-of-n). Crucially, the proof for an OR and a THRESHOLD connective does not reveal which of the relevant values the prover knows


## Crypto Primitives

- **Hash**: Sha256, Blake2b, Blake2b256
- **Encoding**: Base58
- **Signing Algorithm**: ECDSA & Schnorr
- **Symmetric encryption**: 

## Before Ergo

- **Bitcoin**: ECDSA signature with Schnorr signature [added recently](https://news.bitcoin.com/bitcoin-cash-protocol-successfully-upgrades-schnorr-signatures-are-here/)
- **Bitcoin Forks** Usually adding some cryptography to the protocol (e.g new instructions in ZCASH)
- **Ethereum / EVM chains**: Instructions and precompiled contracts. Pairing operations to support 


## Use Cases

### Schnorr Signature

In the simplest case a signature in Ergo transaction is a Schnorr signature, in general case it is a signature corresponding to a subset of Generalized Schnorr Proofs.

- Ergo uses the same elliptic curve as Bitcoin. 
- Ergo's Schnorr signature is pretty close to known standards (RFCs) with certain differences. 
- Allows us to adopt known protocols such as [MuSig](https://eprint.iacr.org/2018/068). 
- It's possible to create **adaptor signatures** which can be used for private swaps. 
- There were private swap demos with Bitcoin Cash


| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| Potentially, a lot of protocols | - | The same as Bitcoin |


### Mixers

- Basic tool to restore fungibility of digital notes.
- Basic scheme, ZeroJoin, is based on ring signatures and proof of knowledge for a **Diffie-Hellman tuple** 
- [Paper with contracts](https://eprint.iacr.org/2020/560)

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| No onchain mixing | Trusted setup-based or inefficient | Efficient, minimal trust assumptions |




### Stealth Addresses

- A tool to hide recipient privacy
- [Contracts](https://www.ergoforum.org/t/stealth-address-contract/255)

This allows a customer to derive a one-time payment address for a store, without revealing the payment to anyone but the store owner. 


| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |

### Ring and Threshold Signatures

- Native support in Ergo, also, more complex schemes support (e.g ring AND threshold)
- Implementations: node API, [Zero-Knowledge Treasury](zkt.md) on top of Ergo



| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |

### Checking A Signature

You can do basic things in a contract like calculating the hash, but what if you want to to check a signature for abitrary message in a contract. This can be done trivially in Ergo, an example is available in SuSy bridge implementation

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | Efficient ECDSA | Efficient Schnorr |



