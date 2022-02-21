# Developers

This page should provide an entry-point to every section of Ergo development. For a high-level introduction to Ergo please see the [protocol page](/dev/protocol)

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

## [ErgoScript](scs/ergoscript/) 

ErgoScript is a rich smart-contract language based on scala.



## Walkthroughs

- [Learning Ergo 101 : Development Workflow](https://blog.cryptostars.is/learning-ergo-101-development-workflow-aa17dd63ef6)
- [Tutorial starting with Appkit on Gradle projects](https://github.com/ergoplatform/ergo-appkit/wiki/Tutorial-starting-with-Appkit-on-Gradle-projects)
- [AppKit by Example (Video)](https://www.youtube.com/watch?v=Md5s-XV6-Hs)
- [ErgoPay](/docs/dev/wallet/payments/ergo-pay.md)
- [You can do some simple apps](https://www.youtube.com/watch?v=d6Mf-oxaLIc) with just the node and ErgoScript to `P2S` address compiler available at [wallet.plutomonkey.com/p2s](https://wallet.plutomonkey.com/p2s/).

## DeCo

Over eight weeks, participants will learn about extended UTXO and boxes, registers, ErgoScript, designing simple systems, multi-transaction systems, and much more. Join the [ErgoLend Discord](https://discord.gg/NBJ68Fvr) for more information. 