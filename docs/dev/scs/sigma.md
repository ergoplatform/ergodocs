---
tags:
  - Sigma Protocols
---


# Sigma Protocols



## Introduction

[ErgoScript](ergoscript.md) incorporates proving and verifying as first-class primitives, giving developers access to a subclass of cryptographic proof systems known as non-interactive **Σ-protocols** (pronounced “sigma-protocols”). A script protecting a transaction output can contain statements (**Σ-statements**) that need to be proven (by producing **Σ-proofs**) to spend the output.

Conceptually, [Σ-proofs](https://arxiv.org/abs/1801.00687) are generalizations  of digital signatures. The Schnorr signature scheme  (whose more recent version is popularly known as [EdDSA](https://ed25519.cr.yp.to/)) is the canonical example of a Σ-proof: it proves that the recipient knows the discrete logarithm of the public key (the proof is attached to a specific message, such as a particular transaction, and thus becomes a signature on the message; all Σ-proofs described here are attached to specific messages). 


**ErgoScript provides two elementary Σ-protocols over a group of prime order (such as an elliptic curve)**

- A proof of knowledge of discrete logarithm with respect to a fixed group generator: (Also known as a **Schnorr signature**).
- A proof that of equality of discrete logarithms (i.e., a proof of a **Diffie-Hellman** tuple)

Σ-protocols exist for proving a variety of properties and, importantly for ErgoScript, elementary Σ-protocols can be combined into more sophisticated ones using the techniques described in [*'Proofs of Partial Knowledge and Simplified Design of Witness Hiding Protocols'*](http://www.win.tue.nl/~berry/papers/crypto94.pdf).

For an introduction to Σ-protocols, we refer the reader to the paper [*'On Σ-protocols'*](http://www.cs.au.dk/~ivan/Sigma.pdf).

ErgoScript also provides the ability to build more sophisticated Σ-protocols by using connectives **AND**, **OR**, and THRESHOLD (also known as **k-out-of-n**). Crucially, the proof for an OR and a THRESHOLD connective does not reveal which of the relevant values the prover knows.


## Composability

Sigma Protocols are the foundation of Ergo’s smart contracts, one of the great things about them is that they are composable, using simple AND/OR logic. 

So you can ask for a signature with the following statement: 

> ‘Prove to me knowledge of either this secret OR that secret’ (this is a one-of-two ring signature). 

Or you can ask, 

> ‘Prove to me knowledge of any two of these three secrets’ (a two-of-three ring signature).


## Use Cases

When combined with a blockchain, these composable proofs enable some very powerful use cases and enable us to implement sophisticated tasks that would otherwise be impossible, risky, or expensive on other platforms. 

Let's say you want to create a ring spending contract, where either of us can make a transaction from the same address, but we don't want anyone else to know which one of us is spending the funds. That's not possible with Bitcoin, and while Ethereum can, it would be expensive and complicated – especially with a ring size of 10 or 20 members, required for robust privacy.

The logic for proofs can also include conditions based on blockchain state.  For example, ‘If the deadline block height has been reached, Alice can provide knowledge of a secret key for a refund. OR a ring signature from Alice and Bob is required to spend coins.’ Or ‘If this account holds a minimum of 100 ERG, Alice OR Bob can remove funds above that amount.’


With Ergo, this kind of application can be created quickly, thanks to native Sigma protocols, enabling trustless scripts that can be used to access mixers or other functionality without any third parties required and fully self-sovereign application-level privacy.





## Resources

## Videos

- [Ergo: A Platform for Cryptographic Applications | Kushti | Ergo Summit 2022](https://www.youtube.com/watch?v=h6g5WahEUSk)

### Applications

- [ErgoMixer](/uses/mixer) is a [state of the art](https://ergonaut.space/screenshot_2021-05-15_at_22.26.39.png) (and worlds first) non-interactive and non-custodial token mixer. 
- SigmaJoin is a composable off chain implementation of ErgoMixer. [Documentation](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/mixer/doc/main.pdf) Original forum posts for [Outsourceable mix](https://www.ergoforum.org/t/yet-another-mixing-protocol/3359/2?u=scalahub) & [Stealth transfer](https://www.ergoforum.org/t/yet-another-mixing-protocol/3359/3?u=scalahub)

### DarkFund0

- [DarkFund0 - ZK Fund for privacy applications](https://www.ergoforum.org/t/darkfund0-zk-fund-for-privacy-applications/398) sponsors new developments in regards to privacy and private DeFi. 4000 ERG up for grabs!

### Articles

- [Ergo utilises the eUTXO model for enhanced privacy & scalability options while also employing expressive smart contracts for Defi applications.](https://ergoplatform.org/en/blog/2021-08-17-ergo-advancing-on-bitcoin/)
  
### Tutorials

- [Verifying Schnorr Signatures in ErgoScript](https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407)
- [Updateable Multisig Pattern](https://www.ergoforum.org/t/updateable-multisig-pattern/3356)

### Presentations

- [Sigma Protocols](https://crypto.sjtu.edu.cn/~yandi/2018%20BIU%20winter%20school/Part%203-Techniques%20for%20Efficient%20ZK%20(cont.)/WS-19-11-sigma-protocols-winter-school-2019-1.pdf)
- [On Σ-protocols](https://cs.au.dk/~ivan/Sigma.pdf)