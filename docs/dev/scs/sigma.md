> Ergo aims to provide an efficient, secure, and easy way to implement financial contracts that will be useful and survivable in the long term. There is plenty of uniqueness in Ergo, but the most significant is probably **Sigma protocols**. These allow a true P2P system with privacy in mind. No one else at the moment is able to build a trustless LETS system, multisig with no signers disclosure, trustless payment networks or has real ring signatures that preserve zero knowledge.


## Zero-Knowledge Proofs

Let's say someone picks up a phone in a bar. You can prove it's yours by hiding the screen, entering the unlock code and showing the unlocked screen to the person who found it. This is a simple example of zero-knowledge proof: you have proven you own the phone without giving away any sensitive information.

In cryptography, most practical problems are associated with secrets. The most popular application lies in digital signatures, used by millions of people around the world every day. Essentially, these involve saying: *'This message proves I know the private key associated with this public key – but I'm not revealing the private key itself'.*

Ergo provides superior access to discrete log based zero-knowledge proofs. 

##  Sigma protocols

ErgoScript is the language used to specify the conditions under which currency can be spent. The language supports a type of non-interactive zero-knowledge proofs called Σ-protocols and is flexible enough to allow for ring-signatures, multi signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.

The overwhelming majority of successful public blockchain use‐cases are related to financial applications. Ergo extends Bitcoin's way of writing contracts by attaching a guard script (together with additional custom data) to every coin. For example, in addition to regular protection by some `m‐of‐n` signature, Ergo allows specifying the possible recipients of these coins, which may be another contract with similar complex conditions. This "chaining" approach allows the implementation of secure and efficient contracts of arbitrary complexity. Keeping all this in mind, we expect ErgoScript and Ergo's design to be uniquely useful as Contractual Money.

Let's say you want to create a 'ring spending contract', where either of us can make a transaction from the same address, but we don't want anyone else to know which one of us is spending the funds. That's not possible with Bitcoin. While Ethereum can, it would be expensive and complicated – especially with a ring size of 10 or 20 members, required for robust privacy.

With Ergo, this kind of application can be created quickly, thanks to the integration of Sigma protocols in the core. This enables self-sovereign application-level privacy: **trustless scripts that can be used to access mixers or other functionality without any third parties required.**

    val ringScript = s"""
    {
    atLeast(
      3, 
      Coll(
        PK("9f8ZQt1Sue6W5ACdMSPRzsHj3jjiZkbYy3CEtB4BisxEyk4RsNk"), 
        PK("9hFWPyhCJcw4KQyCGu4yAGfC1ieRAKyFg24FKjLJK2uDgA873uq"), 
        PK("9fdVP2jca1e5nCTT6q9ijZLssGj6v4juY8gEAxUhp7YTuSsLspS"), 
        PK("9gAKeRu1W4Dh6adWXnnYmfqjCTnxnSMtym2LPPMPErCkusCd6F3"),
        PK("9gmNsqrqdSppLUBqg2UzREmmivgqh1r3jmNcLAc53hk3YCvAGWE")
      )
    )
    }


This an example 3-out-of-5 threshold signature which can be compiled to a P2S address sending ergs to [resulting address (protected by the threshold sig)](https://wallet.plutomonkey.com/p2s/?source=ewphdExlYXN0KAogIDMsIAogIENvbGwoCiAgICBQSygiOWY4WlF0MVN1ZTZXNUFDZE1TUFJ6c0hqM2pqaVprYll5M0NFdEI0QmlzeEV5azRSc05rIiksIAogICAgUEsoIjloRldQeWhDSmN3NEtReUNHdTR5QUdmQzFpZVJBS3lGZzI0RktqTEpLMnVEZ0E4NzN1cSIpLCAKICAgIFBLKCI5ZmRWUDJqY2ExZTVuQ1RUNnE5aWpaTHNzR2o2djRqdVk4Z0VBeFVocDdZVHVTc0xzcFMiKSwgCiAgICBQSygiOWdBS2VSdTFXNERoNmFkV1hublltZnFqQ1RueG5TTXR5bTJMUFBNUEVyQ2t1c0NkNkYzIiksCiAgICBQSygiOWdtTnNxcnFkU3BwTFVCcWcyVXpSRW1taXZncWgxcjNqbU5jTEFjNTNoazNZQ3ZBR1dFIikKICApCikKfQ==)

Here is a good intro to [making a signature](https://www.youtube.com/watch?v=daP67yp-Czs&list=PLUWruihtE-HtL-JZk8Vb4Yn_H18aE3rb6&index=4)


## Manifesto

> Privacy must remain an option to protect the individual. It does not have to be forced; let people make their own choices. Privacy is the ability to create barriers and erect boundaries to create a space and for the individual. It is up to each what borders and boundaries they choose to make. 
>
> Civilization exists under a continuous tension between what is best for society and what is best for the individual. The only real entities in a community are individuals. All collectives, associations, and governments stem from individual participation and interaction. 


## Use Cases

When combined with a blockchain, these composable proofs enable some very powerful use cases. The logic for proofs can include conditions based on blockchain state. For example, 'If the deadline block height has been reached, Alice can provide knowledge of a secret key for a refund. OR a ring signature from Alice and Bob is required to spend coins.' Or 'If this account holds a minimum of 100 ERG, Alice OR Bob can remove funds above that amount.'

It's relatively easy to swap coins or custom tokens trustlessly across any Bitcoin-like blockchains. But beyond that, Ergo allows partial swaps. Just like on a regular exchange, orders can be partially filled if that's what the trader wants. This means it's possible to build a fully-fledged decentralised exchange (DEX) that enables cross-chain trading: a totally trustless version of existing crypto exchanges. There's no need for any gateways, token wrapping or other potential bottlenecks or points of failure.




## 'Optional' Privacy?

A Rich smart-contract language and simplicity are the priority in Ergo, and smart contracts make privacy a lot harder. There are plenty of reasons to want optional privacy - transparent ledgers are a feature for many use-cases.  e.g. charities that want everyone to have full access to the flow of funds.   The ability to operate with privacy or with transparency is a feature. 
There are also strong arguments for optional privacy for adoption and regulation. ErgoMixer is non-interactive, so it works with the blockchain alone; no off-chain coordination with others (and trusted coordinator) is needed.

In future, privacy by default could be enabled for every transaction in Ergo. Maybe the community will do it someday, or maybe integrating mix-nets and other novel ideas on the application layer will be sufficient.  

- ["With non-optional privacy you can't have (efficient) powerful contracts. Even more, even for simple payments formalizing (in order to minimize with guarantee) leakage is hard, for arbitrary contracts not feasible at all I guess"](https://discord.com/channels/668903786361651200/668903786902847502/819670159769337938)

## ErgoMixer 

ErgoMixer is a [state of the art](https://ergonaut.space/screenshot_2021-05-15_at_22.26.39.png) (and worlds first) non-interactive and non-custodial token mixer and the first real implementation of Sigma protocols on Ergo. [Mac/Windows applications are available!](https://github.com/ergoMixer/ergoMixBack/releases). Check out this page on [ergonaut.space](https://ergonaut.space/en/ErgoMixer) for more information including research papers / presentations; and these discussions in Discords.

- [Tornado Cash vs ErgoMixer](https://discord.com/channels/668903786361651200/762308254159863818/871703354970103818)
- [anon2020s explaining the how ErgoMixer retains its anonymity](https://discord.com/channels/668903786361651200/762308254159863818/885284185173024799)



## Resources


- [Ergo utilizes the eUTXO model for enhanced privacy & scalability options while also employing expressive smart contracts for DeFi applications.](https://ergoplatform.org/en/blog/2021-08-17-ergo-advancing-on-bitcoin/)
- [DarkFund0 - ZK Fund for privacy applications](https://www.ergoforum.org/t/darkfund0-zk-fund-for-privacy-applications/398) | sponsors new developments in regards to privacy and private DeFi - 4000 ERG up for grabs!
