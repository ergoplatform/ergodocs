# Developers

This page should provide an entry-point to every section of Ergo development. For a high-level introduction to Ergo please see the [protocol page](/dev/protocol)

## Architecture 

Apps in the Ergo ecosystem looks a bit like this. 

![](../assets/img/arch.png)

Your application will communicate with the blockchain via a locally run instance of the Ergo Node. The Node provides an API that is used by your SDK logic to carry out operations on the blockchain.

- [Set up a local Node](/node/)



## Libraries

- [Back-end libraries (SDKs)](stack/back-end)
- [Front-end libraries](stack/front-end/)

## Languages

Users of *AppKit* will usually write Scala code (although AppKit supports many other languages). *Headless dApp Framework (HDF)* users will need to write Rust code, allowing it to be used across platforms. (The HDF also provides some additional abstractions on top of the original ergo API). *JDE*  users will have to write JSON.

- [Start coding in JVM (Scala/Java)](/dev/stack/appkit/)
- [Start coding in Rust](/dev/Languages/rust)
- [Start coding in Python](/dev/Languages/python)
- [Start coding in JSON](/dev/stack/jde)
- [Start coding in ErgoScript](scs/ergoscript/)


## DeCo

[DeCo (Decentralised Collaboration)](https://www.youtube.com/channel/UCyOIxD7YSHN5QwLIulOWrew) teaches participants will learn about extended UTXO and boxes, registers, ErgoScript, designing simple systems, multi-transaction systems, and much more. Join the [ErgoLend Discord](https://discord.gg/NBJ68Fvr) for more information. 
