# Developers

This page provides a general entry-point to all aspects of Ergo development. 

Join our [Discord server](https://discord.gg/7kWWQeMCwe) dev-support (and regular [Hackathons](ergohack.md))



## Introduction


To get started, make sure to familiarise yourself with the [Ergo protocol](/dev/protocol) the [eUTXO](eutxo.md) model and it's [differences from the account model](accountveutxo.md).

To get started you should know; 

- Ergo has a Bitcoin-like UTXO transactional model: transactions spend and create one-time objects. We call this object a [box](data-model/box/index.md).
- The **on-chain** code is written in [ErgoScript](ergoscript.md) (a subset of scala), the ***off-chain*** code can be done in a programming langage of your choice. 
- You communicate with the blockchain via a locally run instance of the Ergo [Node](/node/install).
- The node provides a [Swagger API](swagger.md) that is used by your SDK logic to carry out operations on the blockchain. 
- There is a [testnet](testnet.md) available you can use for testing and experimentation without having to use real ERG or worrying about breaking the main chain.

## Getting Started

##### First Steps

- Not sure where to start developing? This [introduction to Mosaik](intro.md) provides a brief overview of some of the design decisions you'll need to make when creating your application. 


##### Articles

- [Learning blockchains like Cardano and Ergo](https://www.youtube.com/watch?v=HDn49bToTMI)
- [Side tooling for building dApps on Ergo](https://dav009.medium.com/ergo-101-side-tooling-for-building-dapps-on-ergo-c71889d60826)
- [DeCo Education: DApp Components - Backend](https://deco-education.github.io/deco-docs/docs/into-the-woods/trail2-ergo-coding/dapp-components)

##### Simple Examples 

- [Interactive tutorials for javascript dApp development](https://play.dappstep.com/)
- Creating a [Simple *pay-to-script* app](p2s.md) 
- Creating a [signature](3-out-of-5.md)
- Sending a [chained transaction](chained.md)

##### Courses

- [Hitchhiker's guide to dApp development on Ergo (JS)](https://www.youtube.com/playlist?list=PLzY-irO3z3G8FVDifned2NMFc-PgQqnny) 
- The [Ergo Blockchain Crash Course](https://www.youtube.com/playlist?list=PL8-KVrs6vXLTVXGwmYXjOBRx3VymB4Vm2)
- [DeCo (Decentralised Collaboration)](deco.md) have introduction, layman and ErgoScript courses available on [YouTube](https://www.youtube.com/channel/UCyOIxD7YSHN5QwLIulOWrew/playlists)


##### Tutorials

- [AppKit By Example](https://www.youtube.com/watch?v=Md5s-XV6-Hs) takes you through the steps to programmatically create and submit a transaction. 
- Using appkit from [python](appkit_py.md)
- [Verifying Schnorr Signatures](verifying.md)


##### Payments

- Handling payments with [ErgoPay tutorial](ep-tutorial.md)
- [Integrating the dApp Connector](dApp.md)

##### Developing on Mobile

- Develop on Mobile (or Desktop!) with [Gradle](gradle.md)

##### [**ErgoScript**](ergoscript.md)

- [The ErgoScript Developer Course from DeCo Education](https://github.com/DeCo-Education/ErgoScript-Developer-Course)
- [Learn ErgoScript By Example Via The Ergo Playground with Robert Kornacki](https://www.youtube.com/watch?v=8l2v1asHgyA)
- [ErgoScript tutorial](https://ergoplatform.org/docs/ErgoScript.pdf)
- [Advanced ErgoScript Tutorial](https://ergoplatform.org/docs/AdvancedErgoScriptTutorial.pdf)



## Tooling

##### Frameworks

**JVM** (Java/Scala/Kotlin)

- [ergo-appkit](appkit.md) for JVM languages (used in Scala, Java and Kotlin projects)

**Rust**

- [sigma-rust](rust.md) is an alternative and simple implementation of ErgoTree interpreter and transaction building tools.
- [Headless dApp Framework](headless.md) is a Rust framework for developing Ergo *Headless* dApps.
- [RustKit](rustkit.md) (WIP) a library on top of sigma-rust for easily creating transactions.
- [ergo-utilities-rust](ergo_utilities.md) houses experimental libraries for writing off-chain Ergo code in Rust.

**JS**

- [Fleet](fleet.md) lets you easily create Ergo transactions with a pure JS library.

**JSON**

- [Mosaik](intro.md) is a JSON-based markup language served via a REST API intended to be used by Ergo platform dApps. Therefore, it provides elements and interactions typically needed for these.
- [JSON dApp Environment (JDE)](jde.md) is another programming tool that you can use to interact with Ergo dApps using JSON.




##### Libraries

- [GetBlok Plasma](plasma.md) is a library on top of Ergo Appkit that provides an abstraction layer to simplify the process of integrating AVL Trees (AKA Plasma) into off-chain code.
- [Scrypto](scrypto.md) is an open source cryptographic toolkit designed to make it easier and safer for developers to use cryptography in their applications.
- [EIP12-types](eip12-types.md) is a static typing library for Ergo Blockchain's dApp Connector Protocol.

##### [Node & Explorer Tools](explorer.md)
##### [APIs](api.md)
##### [Python wrappers](/dev/lang/python)
##### [Off-Chain Tooling](off-chain.md)







##### Utilities

- [Miner rewards script](https://github.com/lorien/ergotools) | Simple command-line tool to find miner rewards not spent and form withdrawing transaction requests for them
- [Ergo P2S Playground](https://wallet.plutomonkey.com/p2s/?source=dHJ1ZQ==) | A web-based tool to quickly get the address corresponding to some script  
- [ergo-monitoring](https://github.com/SabaunT/ergo-monitoring) | Debug service printing out useful for developers and managers information about ergo blockchain state.
- [Transaction builder](https://transaction-builder.ergo.ga/) |  The application allows you to manipulate Ergo json transactions with a UI and to sign them with Yoroi, or to prepare the JSON for the Swagger API. It is also able to load the JSON of an unsigned transaction to edit it.  | [GitHub](https://github.com/ThierryM1212/transaction-builder/)  | [Video](https://youtu.be/0VhfY7osT2k)

##### Test vectors

- [Ergo transaction serialization](https://git.io/fjqwX)
- [Signature scheme](https://git.io/fjqwH)

##### On-Chain Analysis

- [Ergo Vision](https://github.com/CryptoCream/ErgoVision) | A wallet visualization tool to be used for investigating transactions and addresses
- [Ergo Intelligence](https://github.com/Eeysirhc/ergo_intelligence)
- [Ergo.watch](https://ergo.watch)

> Make sure to check out the [resources](resources.md) page and the *dev-tools* tab on [sigmaverse.io](https://sigmaverse.io/). 






