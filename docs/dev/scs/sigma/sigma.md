---
tags:
  - Sigma Protocols
---


# Sigma Protocols

## Introduction


Among the hundreds or even thousands of [zero-knowledge protocols](zkp.md), there is a sub-class of efficient and composable proof-of-knowledge protocols called **Sigma Protocols** (Σ-Protocols or *Generalized Schnorr Proofs*). 

Sigma protocols can be represented as digital signatures in a straightforward way, so we can effectively think of them as signatures in the context of blockchain.

## Composability

Sigma Protocols are the foundation of Ergo’s smart contracts, one of the great things about them is that they are composable, using simple AND/OR logic. 

So you can ask for a signature with the following statement: 

> ‘Prove to me knowledge of either this secret OR that secret’ (this is a one-of-two ring signature). 

Or you can ask, 

> ‘Prove to me knowledge of any two of these three secrets’ (a two-of-three ring signature).

Σ-protocols are flexible enough to allow for ring-signatures, multi signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation. 

## Use Cases

When combined with a blockchain, these composable proofs enable some very powerful use cases and enable us to implement sophisticated tasks that would otherwise be impossible, risky, or expensive on other platforms. 

Let's say you want to create a ring spending contract, where either of us can make a transaction from the same address, but we don't want anyone else to know which one of us is spending the funds. That's not possible with Bitcoin, and while Ethereum can, it would be expensive and complicated – especially with a ring size of 10 or 20 members, required for robust privacy.

The logic for proofs can also include conditions based on blockchain state.  For example, ‘If the deadline block height has been reached, Alice can provide knowledge of a secret key for a refund. OR a ring signature from Alice and Bob is required to spend coins.’ Or ‘If this account holds a minimum of 100 ERG, Alice OR Bob can remove funds above that amount.’


With Ergo, this kind of application can be created quickly, thanks to native Sigma protocols, enabling trustless scripts that can be used to access mixers or other functionality without any third parties required and fully self-sovereign application-level privacy.





## Resources


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