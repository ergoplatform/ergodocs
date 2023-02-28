---
tags:
  - ErgoScript
---

# ErgoScript

**ErgoScript is a super-simple subset of Scala.** It is a top-level language translated into a low-level language called [ErgoTree](ergotree.md), which is translated during execution into cryptographic protocol. That's how Ergo supports ring and threshold signatures and much more crypto protocols with no special cases made in the core!

Ergo's support for [sigma-protocols](sigma.md) (aka generalized Schnorr proofs) are truly unique as building blocks for composable statements. Schnorr protocols and proof-of-Diffie-Hellman-tuples are supported by default, with more options available that the community can add via soft forks.


ErgoScript is built considering Bitcoin’s security and privacy to make all kinds of complex financial contracts accessible. In comparison, Bitcoin’s design doesn’t allow loops or building any complex smart contracts on top of it. ErgoScript allows for self-replication; therefore, we can use it to create Turing-Complete processes in a blockchain.



## Key Concepts

- Ergo is a UTXO-based blockchain with Proof-of-Work consensus
- Ergo uses an *extended-UTXO model*, supporting advanced financial contracts comparable to those in Ethereum's account-based model. 
- Since Ergo is UTXO-based, ErgoScript has many UTXO-specific constructs such as: `Box`, `INPUTS`, and `OUTPUTS`. A complete list is available [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md)
- A [Box](box.md) is essentially a UTXO and consists of up to ten registers for storing data. Similar to Bitcoin, a transaction spends one or more existing boxes (denoted using the `INPUTS` array) and creates one or more new boxes (denoted using the `OUTPUTS` array)
- ErgoScript's syntax is a subset of Scala's. However, knowledge of Scala is not necessary to learn ErgoScript because the amount of Scala needed to write ErgoScript is small, e.g. `val`
- Note that arrays in Scala are accessed using round parentheses, not square brackets like in Java or Python. Thus, `OUTPUTS(0)` refers to the first element of the `OUTPUTS` array
- Unlike Scala, ErgoScript does not support the `var` keyword, and thus everything is immutable
- The scripting language is non-Turing complete, but applications can be made to be Turing complete, as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).

## Simple Example

```
if (HEIGHT < 100000) alicePubKey else bobPubKey
```

1. Allows Only Alice to spend a box before a certain height 
2. Allows Only Bob to spend the box after that.


Please see this [Quick Primer on ErgoScript](/dev/scs/ergoscript-primer) for an overview of key concepts and some basic examples. 

## Resources


##### Courses

- [ErgoScript 101 Crash Course](https://docs.google.com/presentation/d/10gYO82z_7qloRrFOcCxTFuzpP40IImPyIKMV2ZFd9M4/edit#slide=id.p) (Slides)
- [Learn ErgoScript By Example Via The Ergo Playground with Robert Kornacki (Video)](https://www.youtube.com/watch?v=8l2v1asHgyA)
- [The ErgoScript Developer Course from DeCo Education](https://github.com/DeCo-Education/ErgoScript-Developer-Course)
- [Deco Education: 2022 Script Class](https://www.youtube.com/watch?v=qR0_k7VH6KI&list=PLopsKGshj0B4DfFnS-pvriZhba050eaXu)


##### Tutorials 

- [ErgoScript by Example Repository](https://github.com/ergoplatform/ergoscript-by-example)
- [Testing Ergo Contracts Off-chain](https://github.com/anon-real/contract-testing)


##### Advanced Tutorials

- [Advanced ErgoScript Tutorial](https://ergoplatform.org/docs/AdvancedErgoScriptTutorial.pdf)
- [ErgoScript tutorial](https://ergoplatform.org/docs/ErgoScript.pdf)


##### Explanations

- [ErgoScript Design patterns](https://www.ergoforum.org/t/ergoscript-design-patterns/222)
- [SigmaState Protocols](https://storage.googleapis.com/ergo-cms-media/docs/sigmastate_protocols.pdf)

##### References

- [ErgoScript Language Spec](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md)
- [ErgoScript](https://ergoplatform.org/docs/ErgoScript.pdf) 
- [ErgoTree](https://ergoplatform.org/docs/ErgoTree.pdf)
- [High-Level Design Patterns In Extended UTXO Systems](https://github.com/Emurgo/Emurgo-Research/blob/master/smart-contracts/High%20Level%20Design%20Patterns%20In%20Extended%20UTXO%20Systems.md)

##### Examples

- [ErgoPad Plasma Staking Contracts](https://github.com/paideiadao/paideia-contracts/blob/main/paideia_contracts/contracts/plasma_staking/ergoscript/latest/plasmaStaking.es)
- [GetBlok.io Smart Pools](https://github.com/GetBlok-io/ergo-smartpooling-contracts)


##### Visual

- [FlowCards](flowcards.md) is *A Declarative Framework for Development of Ergo dApps* 
- [flowcardLib: Ergo FlowCard library for diagrams.net](https://github.com/lucagdangelo/flowcardLib)
- [ergo-castanet](https://github.com/iandebeer/ergo-castanet)

##### Bookmarks


- Compile ErgoScript directly in your browser with [ErgoScript Playground](https://wallet.plutomonkey.com/p2s/)
- [Kiosk](/dev/stack/kiosk) lets anyone play with ErgoScript using a basic web-based UI
- [ergoscript-compiler](https://github.com/ergoplatform/ergoscript-compiler)

##### Box

Here is a box to experiment with 

This [address](https://wallet.plutomonkey.com/p2s/?source=c2lnbWFQcm9wKFNFTEYuaWQgPT0gSU5QVVRTKDApLmlkKQ==) will create an output at this [box](https://api.ergoplatform.com/api/v0/transactions/boxes/byAddress/unspent/ZX44DGQZJ4SoDVh58XRuNZjAq).






