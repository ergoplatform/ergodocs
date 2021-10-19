# Back-end

This page provides an overview of the tools used to interact with the Ergo blockchain. Developers can use these tools to read data from the blockchain, compute using that data and optionally create transactions to be broadcast. Each tool requires the developer to "program" in some language.

Users of AppKit will usually write Scala code (although AppKit supports many other languages). HDF users will need to write Rust code. JDE users will have to write JSON.


## JDE

[Ergo JDE](https://github.com/ergoplatform/ergo-jde) 

### Tutorials
### How-to Guides
- [Example: Minting Reserve Coins](https://github.com/ergoplatform/ergo-jde#example-minting-reserve-coins)
- [Writing JDE Scripts](https://github.com/ergoplatform/ergo-jde#writing-jde-scripts)
- [Using the web service](https://github.com/ergoplatform/ergo-jde#using-the-web-service)
### Explanations
### References
- [Sample Scripts](https://github.com/ergoplatform/ergo-jde/tree/main/sample-scripts)
- [Syntax](https://github.com/ergoplatform/ergo-jde/blob/main/syntax.md)

## Headless dApp Framework
[Ergo Headless dApp Framework](https://github.com/ergoplatform/ergo-headless-dapp-framework). The premier Rust framework for developing Ergo Headless dApps. The Ergo HDF provides developers with the very first portable UTXO-based headless dApp development framework on any blockchain.
### Tutorials
- [Math Bounty Headless dApp - Getting Started Writing Your First Action](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/tutorials/Math_Bounty/1-math-bounty-dApp-getting-started.md)
- [Math Bounty Headless dApp - Finishing The Headless dApp](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/tutorials/Math_Bounty/2-math-bounty-dApp-finishing-the-headless-dapp.md)
- [Math Bounty Headless dApp - Writing A CLI Frontend For Creating Bounties](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/tutorials/Math_Bounty/3-math-bounty-dApp-writing-a-cli-frontend-that-allows-creating-bounties.md)
  
### Explanations
[Understanding The Ergo Headless dApp Framework](https://github.com/ergoplatform/ergo-headless-dapp-framework#understanding-the-ergo-headless-dapp-framework)

## Appkit

AppKit provides methods for the following

- Fetch data from Ergo Explorer API
- Interact with Ergo Node, both public and private methods
- Build transactions and sign them
- Helper methods to handle cryptographics like calculating PK addresses from secrets

[Appkit: A Library for Polyglot Development of Ergo Applications](https://github.com/aslesarenko/ergo-appkit) has an idiomatic Java API and is written in Java/Scala. It is a thin wrapper around core components provided by the ErgoScript interpreter and Ergo protocol implementations which are written in Scala. It is published on [maven repository](https://mvnrepository.com/artifact/org.ergoplatform/ergo-appkit) and cross compiled to both Java 7 and Java 8+ jars.

Using Appkit Ergo applications can be written in one of the languages supported by GraalVM (i.e. Java, JavaScript, C/C++, Python, Ruby, R) and using this library applications can communicate with Ergo nodes via unified API and programming model provided by Appkit. In addition Appkit based Ergo applications can be compiled into native code using native-image ahead of time compiler and then executed without Java VM with very fast startup time and lower runtime memory overhead compared to a Java VM. This is attractive option for high-performance low-latency microservices.


### Tutorials
- [Tutorial starting with Appkit on Gradle projects](https://github.com/ergoplatform/ergo-appkit/wiki/Tutorial-starting-with-Appkit-on-Gradle-projects)
- [AppKit by Example (Video)](https://www.youtube.com/watch?v=Md5s-XV6-Hs)
- [Appkit Examples](https://github.com/aslesarenko/ergo-appkit-examples)
  
### How-to Guides

- [Ergo Android](https://github.com/aslesarenko/ergo-android) | Example Android application which demonstrates how Ergo Appkit can be used to develop Ergo applications running on Android.

### Explanations
- [AppKit Introduction](https://ergoplatform.org/en/blog/2019_12_03_top5/).

### References

- [ErgoTool](https://github.com/aslesarenko/ergo-tool) | A Command Line Interface for Ergo based on Appkit and [GraalVM](https://www.graalvm.org/) native-image. Read the [introduction and overview](https://ergoplatform.org/en/blog/2019_12_31_ergo_tool/).

