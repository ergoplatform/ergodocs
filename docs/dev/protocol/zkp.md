# Zero-Knowledge Proofs

Ergo provides superior access to ***discrete log-based* zero-knowledge proofs**, but what exactly is a zero-knowledge proof? 

Let's say someone picks up a phone in a bar. You can prove it's yours by hiding the screen, entering the unlock code and showing the unlocked screen to the person who found it. This scenario is a simple example of zero-knowledge proof: you have proven you own the phone without revealing any sensitive information.

In cryptography, most practical problems are associated with secrets. The most popular application lies in digital signatures, used by millions worldwide daily. Essentially, these involve saying: 

> *' This message proves I know the private key associated with this public key – but I'm not revealing the private key itself'.*


## Sigma Protocols

[ErgoScript](ergoscript.md) is the language used to specify the conditions under which currency can be spent. The language supports a type of non-interactive zero-knowledge proof called [Σ-protocols](sigma.md). It is flexible enough to allow for ring signatures, multi-signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.


## 'Optional' Privacy?

A rich smart-contract language is a priority in Ergo, and with non-optional privacy, you can't have (efficient) powerful contracts. Even more, for simple payments, formalising leakage is hard, and for arbitrary contracts simply not feasible.

There are also plenty of reasons someone might want optional privacy - transparent ledgers are a feature for many use cases. e.g. charities that want everyone to have full access to the flow of funds.  

There are also strong arguments for optional privacy for adoption and regulation. ErgoMixer is non-interactive, so it works with the blockchain alone; no off-chain coordination with others (and a trusted coordinator) is needed.

In future, the community could elect to enable privacy by default for every transaction in Ergo. Or we'll see integration mix-nets and other novel ideas on the application layer.  

> Privacy must remain an option to protect the individual. It does not have to be forced; let people make their own choices. Privacy is the ability to create barriers and erect boundaries to create a space for the individual. It is up to each what borders and boundaries they choose to make. - *The Ergo Manifesto*



## Use Cases

These composable proofs enable some very strong use cases combined with a blockchain. The logic for proofs can include conditions based on the blockchain state. For example, 'If the deadline block height has been reached, Alice can provide knowledge of a secret key for a refund. OR a ring signature from Alice and Bob is required to spend coins.' Or 'If this account holds a minimum of 100 ERG, Alice OR Bob can remove funds above that amount.'

Swapping coins or custom tokens trustlessly across any Bitcoin-like blockchain is relatively easy. But beyond that, Ergo allows partial swaps. Like on a regular exchange, we can partially fill orders and enable a fully-fledged decentralised exchange (DEX) that enables cross-chain trading: a trustless version of existing crypto exchanges. There's no need for gateways, token wrapping or other potential bottlenecks or points of failure.