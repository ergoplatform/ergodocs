# Developers

This page provides a general entry-point to all aspects of Ergo development. 


## Introduction


To get started, make sure to familiarise yourself with the Ergo [protocol](/dev/protocol) the [eUTXO](eutxo.md) model and it's [differences from the account model](accountveutxo.md).

Essentially, 

- You communicate with the blockchain via a locally run instance of the Ergo [Node](/node/install). 
- The node provides an [API](resources.md#api) that is used by your SDK logic to carry out operations on the blockchain. 
- Ergo has a Bitcoin-like UTXO transactional model: transactions spend and create one-time objects. We call this object a ['box'](data-model/box/index.md).
- The **on-chain** code is [ErgoScript](ergoscript.md) (a subset of scala), the ***off-chain*** code can be done in a programming langage of your choice. 

## Getting Started

Dive in if you have a language in mind you want to use, or some of the best introductionary pathways are outlined directly below. 


- [JVM (Scala/Java)](/dev/stack/appkit/appkit)
- [Rust](/dev/Languages/rust)
- [Python](/dev/Languages/python)
- [JavaScript](js.md)
- [JSON](/dev/stack/jde)
- [ErgoScript](scs/ergoscript/)

> Join our [Discord](https://discord.gg/7kWWQeMCwe) server for regular [Hackathons](ergohack.md) or dev-support


### Youtube

- (Java) [AppKit By Example](https://www.youtube.com/watch?v=Md5s-XV6-Hs) takes you through the steps to programmatically create & submit a transaction. 
- (JS) [Hitchhiker's guide to dApp development on Ergo](https://www.youtube.com/playlist?list=PLzY-irO3z3G8FVDifned2NMFc-PgQqnny)

### Tutorials

- (JS) [Interactive tutorials for javascript dApp development](https://play.dappstep.com/)
- [ErgoScript by example](https://github.com/ergoplatform/ergoscript-by-example)
- [ErgoTutorials](https://www.youtube.com/channel/UCyOIxD7YSHN5QwLIulOWrew)


### Introductionary Articles 

- [Kbit: Learning blockchains like Cardano and Ergo](https://www.youtube.com/watch?v=HDn49bToTMI)
- [Ergo 101 : Side tooling for building dApps on Ergo](https://dav009.medium.com/ergo-101-side-tooling-for-building-dapps-on-ergo-c71889d60826)

### Educational Courses

- DeCo (Decentralised Collaboration) teaches participants will learn about extended UTXO and boxes, registers, ErgoScript, designing simple systems, multi-transaction systems, and more. 
    - Join their [Discord](https://discord.gg/PQPyFbKZ9z) for more information or watch their full courses on [youtube](https://www.youtube.com/channel/UCyOIxD7YSHN5QwLIulOWrew/playlists). 
- [Educational Classes on Game Building and Design](https://medium.com/@lgmeister/the-future-of-ergogames-io-hosting-educational-classes-on-game-building-and-design-679afd2632d4) from [ErgoGames.io](https://ergogames.io)





> Make sure to check out the [resources](resources.md) page and the *dev-tools* tab on [sigmaverse.io](https://sigmaverse.io/)







