# JSON dApp Environment (JDE) 

Ergo enables sophisticated dApps via smart contracts written in [ErgoScript](ergoscript.md).

Interacting with such smart contracts requires a developer to write code in a language such as Scala (using the [AppKit](appkit.md) framework) or Rust (using [HDF](headless.md) or [sigma-rust](sigma-rust.md))

The [JSON dApp Environment (JDE)](https://github.com/ergoplatform/ergo-jde) described on this page is another programming tool you can use to interact with Ergo dApps. The differentiating feature of JDE is that its programming language is **JSON**.

### Goals

This JDE is designed with the following goals in mind:

1. Enable tech-savvy users and developers to interact with existing (and future) Ergo dApps such as Sigma USD by programming the off-chain logic user-friendly. 
 
2. Provide a "sandbox" mode, where users can send arbitrary scripts for execution such that the server does not have to worry about malicious programs. This enables the JDE service to be hosted remotely. An example is [Kiosk-Web](https://kioskweb.org/session/#kiosk.Wallet.txBuilder), where you can post arbitrary scripts (such as [this](https://raw.githubusercontent.com/ergoplatform/ergo-jde/main/sample-scripts/getReserveCoinInfo.json), which gets the reserve coin rate) in "Tx Builder" and obtain results.

Goal #2 rules out many programming languages such as Java/Scala and Rust. This rules out all the so-called "Turing-complete" languages.

### Capabilities

Let us take the use-case of purchasing, say, 10 Sigma-USD reserve coins as an example, which involves the following steps: 

   1. Find the current oracle pool box and obtain the rate from register R4.
   2. Find the current bank box and obtain the relevant parameters (tokens in circulation and base reserves).
   3. Use the formulae to obtain the delta in base reserves. 
   4. Compute the details of the new bank box to be created (nano-Ergs, tokens, registers)
   5. Compute the details of the new receipt box to be created (nano-Ergs, tokens, registers)
   6. Make a transaction creation request to the Ergo node with the above details. 

All the above tasks can be programmed in JDE, as done [in this script](https://raw.githubusercontent.com/ergoplatform/ergo-jde/main/sample-scripts/mintReserveCoinAdvanced.json).  

In general, JDE allows us to do the following:

1. Find some boxes by address and/or box Id
2. Extract values from those boxes (nanoErgs, registers and tokens), and define variables using those.
3. Define constant values
4. Perform computation using the constants and variables. JDE supports the if-then-else construct for control flow. However, it does not support loops. 
5. Define outputs using the values computed
6. Make a transaction creation request to the Ergo node

### How to use JDE

A compiled JAR is available on the [release](https://github.com/ergoplatform/ergo-jde/releases) page. You can also generate the JAR yourself using the `sbt assembly` command. 

The following are the steps in using JDE. 

1. Understand the scripting language by looking at the sample scripts and the documentation.
2. Ensure you have a fully synced Ergo node running.
3. Write your script or edit the existing script for the task at hand.
4. Invoke JDE via CLI to generate a transaction creation request (aka unsigned transaction) and some returned values.

Depending on your use case, you will be using the output of Step 4 differently.

- End users will use it to send a transaction on the Ergo blockchain
- Wallet authors will append some of their inputs/outputs before sending the transaction.
- dApp authors will use the returned values for further computation.

JDE also includes a web-service mode for the last two use-cases. 

Please see the [documentation](https://github.com/ergoplatform/ergo-jde/blob/main/readme.md) for details. 

### Important Notes
- JDE is experimental. Please use with caution at your own risk. Always inspect the created transaction before sending it. 
- If you discover a bug, please make an issue and a PR. 
- If you find some feature missing, please make an issue.
