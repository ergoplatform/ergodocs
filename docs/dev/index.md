# Developers

This page should provide an entry-point to every section of Ergo development.

## Architecture 

Apps in the Ergo ecosystem looks a bit like this. 

![](../assets/img/arch.png)

Your application will communicate with the blockchain via a locally run instance of the Ergo Node. The Node provides an API that is used by your SDK logic to carry out operations on the blockchain.

## Getting Started

- [Set up a local Node](/node/)
- [Using the TestNet](/dev/start/testnet)
- [Remote Nodes](/node/remote)

## Languages

Users of *AppKit* will usually write Scala code (although AppKit supports many other languages). *Headless dApp Framework (HDF)* users will need to write Rust code, allowing it to be used across platforms. (The HDF also provides some additional abstractions on top of the original ergo API). *JDE*  users will have to write JSON.

- [Back-end libraries (SDKs)](stack/back-end)
- [Start coding in Scala](/dev/Languages/scala)
- [Start coding in Java](/dev/Languages/java)
- [Start coding in Rust](/dev/Languages/rust)
- [Start coding in Python](/dev/Languages/python)

## Front-end

- [Front-end libraries](stack/front-end/)

## ErgoScript

- [ErgoScript](scs/ergoscript/) 


## Walkthroughs

- [Learning Ergo 101 : Development Workflow](https://blog.cryptostars.is/learning-ergo-101-development-workflow-aa17dd63ef6)
- [Tutorial starting with Appkit on Gradle projects](https://github.com/ergoplatform/ergo-appkit/wiki/Tutorial-starting-with-Appkit-on-Gradle-projects)
- [AppKit by Example (Video)](https://www.youtube.com/watch?v=Md5s-XV6-Hs)
- [ErgoPay](/docs/dev/wallet/payments/ergo-pay.md)

## DeCo

Over eight weeks, participants will learn about extended UTXO and boxes, registers, ErgoScript, designing simple systems, multi-transaction systems, and much more. According to their Reddit post, the ErgoLearn (DeCo) course aims to empower individuals with the following skills:

1. Explain basic eUTXOs concepts

2. Design basic Financial Systems on Ergo

3. Interact with Ergo Smart Contract developers

4. Navigate through basic ErgoScript”

Creating and deploying a curriculum takes considerable time and resources and the team behind the project were successfully funded through a fundraiser hosted on [Ergo Raffle: ErgoLearn (DeCo) Funding](https://ergoraffle.com/raffle/show/d6941cb138ff2442d42a9636b8acf1ac06e2ca0665a884030e69499f0a2b139d). 

Join the [ErgoLend Discord](https://discord.gg/W7YXzVdz8k) for the latest information on DeCo.