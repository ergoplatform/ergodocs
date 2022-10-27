# Developers

This page provides a general entry-point to all aspects of Ergo development. 

> Join our [Discord server](https://discord.gg/7kWWQeMCwe) dev-support (and regular [ERGOHACKs](ergohack.md))



## Introduction


To get started, make sure to familiarise yourself with the [Ergo protocol](/dev/protocol) the [eUTXO](eutxo.md) model and it's [differences from the account model](accountveutxo.md).

The Ergo development stack looks a bit like this, 

- Ergo has a Bitcoin-like UTXO transactional model: transactions spend and create one-time objects. We call this object a [box](data-model/box/index.md).
- The **on-chain** code is written in [ErgoScript](ergoscript.md) (a subset of scala), the ***off-chain*** code can be done in a programming langage of your choice. 
- You communicate with the blockchain via a locally run instance of the Ergo [Node](/node/install). 
- The node provides an [API](resources.md#api) that is used by your SDK logic to carry out operations on the blockchain. 


## Getting Started

- For Java, [AppKit By Example](https://www.youtube.com/watch?v=Md5s-XV6-Hs) takes you through the steps to programmatically create & submit a transaction. 
- For JavaScript, we have the [Hitchhiker's guide to dApp development on Ergo](https://www.youtube.com/playlist?list=PLzY-irO3z3G8FVDifned2NMFc-PgQqnny). 
- Start from the basics with the [DeCo Education Laymen's Course](https://www.youtube.com/channel/UCyOIxD7YSHN5QwLIulOWrew/playlists) or the [Ergo Blockchain Crash Course](https://www.youtube.com/playlist?list=PL8-KVrs6vXLTVXGwmYXjOBRx3VymB4Vm2)
- Dive into [ErgoScript](scs/ergoscript/)


## Frameworks, Toolkits and Standard Development Kits (SDKs)

There are several robust options now available with the most popular being [ergo-appkit](appkit.md) for JVM languages (used in Scala, Java and Kotlin projects), and JS languages through [sigma-rust](rust.md) or more recently [Fleet](fleet.md). There are also [Python wrappers](/dev/lang/python) and a [JSON dApp Environment (JDE)](jde.md).

This [introduction to Mosaik](stack/mosaik/intro.md) provides a brief overview of some of the design decisions you'll need to make when creating your application.



## Resources 

> Make sure to check out the [resources](resources.md) page and the *dev-tools* tab on [sigmaverse.io](https://sigmaverse.io/). 

##### DeCo (Decentralised Collaboration)

DeCo teaches participants about extended UTXO and boxes, registers, ErgoScript, designing simple systems, multi-transaction systems, and more. Join their 

- [Discord](https://discord.gg/PQPyFbKZ9z)
- [Documentation site](https://deco-education.github.io/deco-docs/docs/intro)
- Introduction, layman and ErgoScript courses available on [YouTube](https://www.youtube.com/channel/UCyOIxD7YSHN5QwLIulOWrew/playlists)


##### Educational Courses

- [Ergo Blockchain Crash Course](https://www.youtube.com/playlist?list=PL8-KVrs6vXLTVXGwmYXjOBRx3VymB4Vm2)
- [Educational Classes on Game Building and Design](https://medium.com/@lgmeister/the-future-of-ergogames-io-hosting-educational-classes-on-game-building-and-design-679afd2632d4) from [ErgoGames.io](https://ergogames.io)

##### Introductionary Articles 

- [Learning blockchains like Cardano and Ergo](https://www.youtube.com/watch?v=HDn49bToTMI)
- [Side tooling for building dApps on Ergo](https://dav009.medium.com/ergo-101-side-tooling-for-building-dapps-on-ergo-c71889d60826)
- [DApp Components - Backend | DeCo Education]()

##### Tutorials

- `JS` [Interactive tutorials for javascript dApp development](https://play.dappstep.com/)
- [ErgoTutorials](https://www.youtube.com/channel/UCyOIxD7YSHN5QwLIulOWrew)

##### Test vectors

- [Ergo transaction serialization](https://git.io/fjqwX)
- [Signature scheme](https://git.io/fjqwH)

##### Utilities

- [Miner rewards script](https://github.com/lorien/ergotools) | Simple command-line tool to find miner rewards not spent and form withdrawing transaction requests for them
- [Ergo P2S Playground](https://wallet.plutomonkey.com/p2s/?source=dHJ1ZQ==) | A web-based tool to quickly get the address corresponding to some script  
- [ergo-monitoring](https://github.com/SabaunT/ergo-monitoring) | Debug service printing out useful for developers and managers information about ergo blockchain state.

##### On-Chain Analysis

- [Ergo Vision](https://github.com/CryptoCream/ErgoVision) | A wallet visualization tool to be used for investigating transactions and addresses
- [Ergo Intelligence](https://github.com/Eeysirhc/ergo_intelligence)
- [Ergo.watch](https://ergo.watch)

##### Tools

- [Transaction builder](https://transaction-builder.ergo.ga/) |  The application allows you to manipulate Ergo json transactions with a UI and to sign them with Yoroi, or to prepare the JSON for the Swagger API. It is also able to load the JSON of an unsigned transaction to edit it.  | [GitHub](https://github.com/ThierryM1212/transaction-builder/)  | [Video](https://youtu.be/0VhfY7osT2k)









