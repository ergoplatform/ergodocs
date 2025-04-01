---
tags:
  - Sigma Protocols
  - Zero-Knowledge Proofs
  - Privacy
---

# Understanding Zero-Knowledge Proofs and Sigma Protocols



Ergo provides superior access to ***discrete log-based* zero-knowledge proofs**, but what exactly is a zero-knowledge proof?

Imagine you find a phone in a bar and someone claims it's theirs. They can prove it by hiding the screen, entering the unlock code, and then showing the unlocked screen. They've proven ownership without revealing any sensitive information, such as the unlock code. This is the essence of a zero-knowledge proof.

In the realm of [cryptography](crypto.md), zero-knowledge proofs are crucial for maintaining secrets. They're widely used in [digital signatures](crypto.md#sigma-protocols), a tool used by millions daily. In essence, a digital signature says:

> *' This message proves I know the private key associated with this public key – but I'm not revealing the private key itself'.*


## Sigma Protocols: Efficient and Composable Proofs

Among the myriad of zero-knowledge protocols, a sub-class known as [**Sigma Protocols**](sigma.md) (Σ-Protocols or *Generalized Schnorr Proofs*) stands out for its efficiency and composability.

> [**ErgoScript**](ergoscript.md) is the language used to specify the conditions under which currency can be spent. It is flexible enough to allow for [ring signatures](ring.md), [multi-signatures](threshold.md), multiple currencies, [atomic swaps](atomic.md), self-replicating scripts, and long-term computation.

Currently, the two Sigma Protocols in use are [proof of discrete log](schnorr.md) and proof of [Diffie-Hellman tuple](diffie.md).


These composable proofs, when combined with a blockchain, enable powerful use cases. The logic for proofs can include conditions based on the blockchain state. For example, 'If the deadline block height has been reached, Alice can provide knowledge of a secret key for a refund. OR a ring signature from Alice and Bob is required to spend coins.' Or 'If this account holds a minimum of 100 ERG, Alice OR Bob can remove funds above that amount.'

Ergo not only allows for trustless coin or custom token swaps across any Bitcoin-like blockchain, but it also enables partial swaps. This feature facilitates the creation of a fully-fledged [decentralised exchange (DEX)](dex.md) that enables cross-chain trading: a trustless version of existing crypto exchanges. There's no need for gateways, token wrapping or other potential bottlenecks or points of failure.


## The Importance of 'Optional' Privacy

> Privacy must remain an option to protect the individual. It does not have to be forced; let people make their own choices. Privacy is the ability to create barriers and erect boundaries to create a space for the individual. It is up to each what borders and boundaries they choose to make. - [*The Ergo Manifesto*](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)

Ergo prioritizes a rich [smart-contract](ergoscript.md) language, and with non-optional privacy, efficient and powerful contracts are not possible. Formalising leakage is challenging for simple payments, and arbitrary contracts are not feasible.

There are numerous reasons why someone might want optional privacy. Transparent ledgers are a feature for many use cases, such as charities that want everyone to have full access to the flow of funds.

Optional privacy also has strong arguments for adoption and regulation. [ErgoMixer](ergomixer.md) is non-interactive, so it works with the blockchain alone; no [off-chain](off-chain.md) coordination with others (and a trusted coordinator) is needed.

In the future, the community could enable privacy by default for every [transaction](transactions.md) in Ergo. Or we'll see integration mix-nets and other novel ideas on the application layer.
