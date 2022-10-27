---
tags:
  - Sigma Protocols
---


# Sigma Protocols

Among the hundreds or even thousands of [zero-knowledge protocols](zkp.md), there is a sub-class of efficient and composable proof-of-knowledge protocols called **Sigma Protocols**. These are also known as *Generalized Schnorr Proofs*. Sigma protocols can be represented as digital signatures in a straightforward way, so we can effectively think of them as signatures in the context of blockchain.

However, there are dozens of other Sigma protocols. One of the great things about them is that they are composable, using simple `AND` and `OR` logic. So you can ask for a signature with the following statement: 

> ‘Prove to me knowledge of either this secret OR that secret’ (this is a one-of-two ring signature). 

Or you can ask, 

> ‘Prove to me knowledge of any two of these three secrets’ (a two-of-three ring signature).

Σ-protocols are flexible enough to allow for ring-signatures, multi signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation. 

When combined with a blockchain, these composable proofs enable some very powerful use cases. The logic for proofs can include conditions based on blockchain state. For example, ‘If the deadline block height has been reached, Alice can provide knowledge of a secret key for a refund. OR a ring signature from Alice and Bob is required to spend coins.’ Or ‘If this account holds a minimum of 100 ERG, Alice OR Bob can remove funds above that amount.’

Thus some very interesting and flexible DeFi applications can be built on Ergo, using secure, straightforward and efficient Sigma protocols.



## Applications

### [ErgoMixer](/uses/mixer)

ErgoMixer is a [state of the art](https://ergonaut.space/screenshot_2021-05-15_at_22.26.39.png) (and worlds first) non-interactive and non-custodial token mixer. 

### SigmaJoin

- [Documentation](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/mixer/doc/main.pdf)

- Original forum posts for [Outsourceable mix](https://www.ergoforum.org/t/yet-another-mixing-protocol/3359/2?u=scalahub) & [Stealth transfer](https://www.ergoforum.org/t/yet-another-mixing-protocol/3359/3?u=scalahub)

## Resources


- [Ergo utilises the eUTXO model for enhanced privacy & scalability options while also employing expressive smart contracts for Defi applications.](https://ergoplatform.org/en/blog/2021-08-17-ergo-advancing-on-bitcoin/)
- [DarkFund0 - ZK Fund for privacy applications](https://www.ergoforum.org/t/darkfund0-zk-fund-for-privacy-applications/398) | sponsors new developments in regards to privacy and private Defi - 4000 ERG up for grabs!
  
### Tutorials

- [Verifying Schnorr Signatures in ErgoScript](https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407)
- [Updateable Multisig Pattern](https://www.ergoforum.org/t/updateable-multisig-pattern/3356)

**Slides**
- [Sigma Protocols](https://crypto.sjtu.edu.cn/~yandi/2018%20BIU%20winter%20school/Part%203-Techniques%20for%20Efficient%20ZK%20(cont.)/WS-19-11-sigma-protocols-winter-school-2019-1.pdf)
- [On Σ-protocols](https://cs.au.dk/~ivan/Sigma.pdf)