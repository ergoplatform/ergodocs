# ErgoScript

## Key Concepts

- Ergo is a UTXO based blockchain with Proof-of-Work consensus
- Ergo is considered an *extended-UTXO model*, supporting advanced financial contracts similar to those in Ethereum's account-based model
- Since Ergo is UTXO based, therefore ErgoScript has many UTXO-specific constructs such as: 
  - `Box`, `INPUTS`, `OUTPUTS`
  - A complete list is available [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md)
- A `Box` is essentially a UTXO and consists of up to ten registers for storing data. Similar to Bitcoin, a transaction spends one or more existing boxes (denoted using the `INPUTS` array), and creates one or more new boxes (denoted using the `OUTPUTS` array)
- ErgoScript's syntax is a subset of Scala's. However, knowledge of Scala is not necessary to learn ErgoScript because the amount of Scala needed to write ErgoScript is small e.g. `val`
- Note that arrays in Scala are accessed using round parentheses, not square brackets like in Java or Python. Thus, `OUTPUTS(0)` refers to the first element of the `OUTPUTS` array
- Unlike Scala, ErgoScript does not support the `var` keyword, and thus everything is immutable
- The scripting language in itself is non-Turing complete, but applications can be made to be Turing complete as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).

## Simple Example

```
if (HEIGHT < 100000) alicePubKey else bobPubKey
```

1. Allows Only Alice to spend a box before a certain height 
2. Allows Only Bob to spend the box after that.


Please see this [Quick Primer on ErgoScript](/dev/scs/ergoscript-primer) for an overview of key concepts and some basic examples. 


### Tutorials 

- [Learn ErgoScript By Example Via The Ergo Playground with Robert Kornacki (Video)](https://www.youtube.com/watch?v=8l2v1asHgyA)
- [ErgoScript by Example Repository](https://github.com/ergoplatform/ergoscript-by-example)
- [Testing Ergo Contracts Off-chain](https://github.com/anon-real/contract-testing)
- [Deco-Education/ErgoScript-Developer-Course](https://github.com/DeCo-Education/ErgoScript-Developer-Course)
- [Deco Education: 2022 Script Class](https://www.youtube.com/watch?v=qR0_k7VH6KI&list=PLopsKGshj0B4DfFnS-pvriZhba050eaXu)
### Advanced Tutorials

- [Advanced ErgoScript Tutorial](https://ergoplatform.org/docs/AdvancedErgoScriptTutorial.pdf)
- [ErgoScript tutorial](https://ergoplatform.org/docs/ErgoScript.pdf)


### Explanations

- [ErgoScript Design patterns](https://www.ergoforum.org/t/ergoscript-design-patterns/222)
- [SigmaState Protocols](https://docs.ergoplatform.com/sigmastate_protocols.pdf)

### References

- [ErgoScript Language Spec](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md)
- [ErgoScript](https://ergoplatform.org/docs/ErgoScript.pdf) 
- [ErgoTree](https://ergoplatform.org/docs/ErgoTree.pdf)
- [High Level Design Patterns In Extended UTXO Systems](https://github.com/Emurgo/Emurgo-Research/blob/master/smart-contracts/High%20Level%20Design%20Patterns%20In%20Extended%20UTXO%20Systems.md)

### Examples

- [ErgoPad Staking Contracts](https://github.com/ergo-pad/ergopad/blob/staking-contracts/backend/app/contracts/staking.md)
- [GetBlok.io Smart Pools](https://github.com/GetBlok-io/ergo-smartpooling-contracts)


### Resources
- [FlowCards](flowcards.md) | A Declarative Framework for Development of Ergo dApps (Also see [flowcardLib](https://github.com/lucagdangelo/flowcardLib))
- [flowcardLib: Ergo FlowCard library for diagrams.net](https://github.com/lucagdangelo/flowcardLib)
- Compile ErgoScript directly in your browser with [ErgoScript Playground](https://wallet.plutomonkey.com/p2s/)
- [Kiosk](/dev/stack/kiosk) lets anyone play with ErgoScript using a basic web-based UI
- [ergoscript-compiler](https://github.com/ergoplatform/ergoscript-compiler)

### P2S

[You can do some simple apps](https://www.youtube.com/watch?v=d6Mf-oxaLIc) with just the node and ErgoScript to `P2S` address compiler available at [wallet.plutomonkey.com/p2s](https://wallet.plutomonkey.com/p2s/). A transaction to this P2S or *pay-to-script* address will create an output locked with the script

- [Wrapped ERG](https://www.ergoforum.org/t/wrapped-erg-wrapping-native-erg-as-a-1-1-token/469) can always be trustlessly exchanged 1:1 for native ERG.
- [Crowdfunding](https://wallet.plutomonkey.com/p2s/?source=ewogICB2YWwgY2FtcGFpZ25JZCA9IFNFTEYuUjRbSW50XS5nZXQKICAgdmFsIGJhY2tlclB1YktleSA9IHByb3ZlRGxvZyhTRUxGLlI1W0dyb3VwRWxlbWVudF0uZ2V0KQogICB2YWwgcHJvamVjdFB1YktleSA9IFNFTEYuUjZbU2lnbWFQcm9wXS5nZXQKICAgdmFsIGRlYWRsaW5lID0gU0VMRi5SN1tJbnRdLmdldCAvLyBoZWlnaHQKICAgdmFsIG1pblRvUmFpc2UgPSBTRUxGLlI4W0xvbmddLmdldAoKICAgdmFsIGZ1bmRyYWlzaW5nRmFpbHVyZSA9IEhFSUdIVCA+PSBkZWFkbGluZSAmJiBiYWNrZXJQdWJLZXkKICAgdmFsIGVub3VnaFJhaXNlZCA9IHsob3V0Qm94OiBCb3gpID0+IG91dEJveC52YWx1ZSA+PSBtaW5Ub1JhaXNlICYmIG91dEJveC5wcm9wb3NpdGlvbkJ5dGVzID09IHByb2plY3RQdWJLZXkucHJvcEJ5dGVzICYmIG91dEJveC5SNFtJbnRdLmdldCA9PSBjYW1wYWlnbklkfQoKICAgdmFsIGZ1bmRyYWlzaW5nU3VjY2VzcyA9IEhFSUdIVCA8IGRlYWRsaW5lICYmIGVub3VnaFJhaXNlZChPVVRQVVRTKDApKQogICBmdW5kcmFpc2luZ0ZhaWx1cmUgfHwgZnVuZHJhaXNpbmdTdWNjZXNzCiB9)
- [3-out-of-5 Threshold Signature](https://wallet.plutomonkey.com/p2s/?source=ewphdExlYXN0KAogIDMsIAogIENvbGwoCiAgICBQSygiOWY4WlF0MVN1ZTZXNUFDZE1TUFJ6c0hqM2pqaVprYll5M0NFdEI0QmlzeEV5azRSc05rIiksIAogICAgUEsoIjloRldQeWhDSmN3NEtReUNHdTR5QUdmQzFpZVJBS3lGZzI0RktqTEpLMnVEZ0E4NzN1cSIpLCAKICAgIFBLKCI5ZmRWUDJqY2ExZTVuQ1RUNnE5aWpaTHNzR2o2djRqdVk4Z0VBeFVocDdZVHVTc0xzcFMiKSwgCiAgICBQSygiOWdBS2VSdTFXNERoNmFkV1hublltZnFqQ1RueG5TTXR5bTJMUFBNUEVyQ2t1c0NkNkYzIiksCiAgICBQSygiOWdtTnNxcnFkU3BwTFVCcWcyVXpSRW1taXZncWgxcjNqbU5jTEFjNTNoazNZQ3ZBR1dFIikKICApCikKfQ==)

#### P2SH

Typically most people use P2S because it is a lot easier to use. P2SH means you have to keep the contract ready off-chain to be submitted when you create the transaction, and if you lose it, then your funds are stuck forever. This also makes it harder for other people to use your dApp as they need the contract themselves, rather than just the address. P2SH is technically cheaper since you store less data on-chain, but likely we won't see anyone using P2SH until we start to get heavy load on-chain.

#### Box

Here is a box to experiment with - this [address](https://wallet.plutomonkey.com/p2s/?source=c2lnbWFQcm9wKFNFTEYuaWQgPT0gSU5QVVRTKDApLmlkKQ==) will create an output at this [box](https://api.ergoplatform.com/api/v0/transactions/boxes/byAddress/unspent/ZX44DGQZJ4SoDVh58XRuNZjAq)






