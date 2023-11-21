# Ergo Headless dApp Framework

[Ergo Headless dApp Framework](https://github.com/ergoplatform/ergo-headless-dapp-framework) is a Rust framework for developing Ergo Headless dApps. The Ergo HDF provides developers with the first portable UTXO-based headless dApp development framework on any blockchain.

/// admonition | Disclaimer
    type: warning

Please note that the Headless dApp framework [does not work with testnet addresses](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/src/encoding.rs#L104)
///


## What Are Headless dApps?

Headless dApps are a brand new technical and business model for developing dApps that is just beginning to take hold in the wider Blockchain sphere. In short, headless dApps are the pure and portable self-contained logic for reading and participating in on-chain smart contract protocols.

In other words, headless dApps are a piece of software which expose the complex on-chain protocols to the off-chain world with a streamlined interface that anyone can build on top of. What is key here is that headless dApps, as their name suggests, have no frontend built on top of them (thus "*headless*").

What headless dApps do provide is the freedom for an entire decentralized ecosystem to be built on top of them. Because headless dApps by default are pure and portable, they can be compiled to any desktop OS, mobile OS, or browser. Because they have a streamlined interface, they can be integrated into scripts and bots trivially. Because they are composable, they can be used together in applications enabling arbitrage between different protocols trivially, or entire new user experiences to be developed without having to understand how each and every supported headless dApp works at it's core.

Headless dApps are the future for enabling newer devs who have limited experience in developing smart contract protocols to still have a real impact on the dApp sphere. The separation of concerns allows building on top of headless dApps without requiring the substantial time sink in understanding the nitty gritty details that made the dApp possible.

Furthermore, headless dApps open up the ecosystem for a whole new business model. Rather than the smart contact protocol creators sucking up all potential profit/value from the success of the protocol, headless dApps uncover an as-of-yet untapped revenue stream for front-end devs. By decentralizing the potential profit from solely the protocol creators to now encompass each and every frontend that is developed, we take a step back from the centralizing effect that we have today with popular dApps with a single hosted frontend. Instead we can incentivize a robust ecosystem of numerous independent frontends built by various devs/companies which all can profit from improving the ecosystem as a whole.

Headless dApps enable all of this, while further enhancing the developer experience at the exact same time.

## Project Goals
1. Enable developers to write their off-chain logic once using the HDF to create their own headless dApps, thereby targeting all platforms (desktop, web, mobile).
2. Provide developers with an easy experience to go from [Ergo dApp Specifications](https://github.com/ergoplatform/eips/blob/master/eip-0006.md) to headless dApp with greater assurance and a straightforward path of implementation.
3. Separating the dApp off-chain logic from any front-end logic, thereby allowing reusability no matter what application or front-end is attempting to integrate your headless dApp.
4. Providing easy-to-use methods for front-end implementors to easily access current state of the dApp protocol without having to understand how any of it works.
5. Abstracting the concept of defining and acquiring input UTXOs for your headless dApp by using a novel design pattern in specifying `BoxSpec`s for the required input UTXOs.
6. Enabling scripts, (arbitrage) bots, and other software to be trivially built on top multiple headless dApps built using the HDF, thus offering a standardized interface and a level of composability.


## Understanding The Ergo Headless dApp Framework

Before you get started using the HDF, there are a number of terms and concepts that are important to understand. The overarching design of the HDF is based off of [EIP-6: Ergo Smart Contract Protocol Specification Format](https://github.com/ergoplatform/eips/blob/master/eip-0006.md).

What this means is that at the highest level, your dApp is defined as a [smart contract protocol](https://github.com/ergoplatform/eips/blob/master/eip-0006.md#smart-contract-protocol). If your dApp only has a single [stage](https://github.com/ergoplatform/eips/blob/master/eip-0006.md#stage), then it is defined as a "single-stage smart contract protocol". If your dApp has multiple stages, then it is a "multi-stage smart contract protocol. The HDF supports building both single and multi-stage protocol dApps.

Each stage can be considered a state in the protocol where a UTXO with Ergs, tokens, and data (within registers) is at in a given point in time. There may be a single box(UTXO) which moves from one stage to the next throughout the entire protocol, multiple boxes which go through all of the stages in parallel, or a variety of boxes asynchronously moving through certain sub-sets of stages.

No matter the specific design/complexity of your given smart contract protocol, each of these stages require "Actions". Actions are the state transitions (transaction logic) which allow:
1. Ergs/tokens/data to enter the protocol (aka. a bootstrap action)
2. Ergs/tokens/data to go from one stage in the protocol to another stage (or exiting the protocol).
3. Ergs/tokens/data to leave the protocol.

Each of these actions is made up of two key parts in the context of your headless dApp:
1. Acquiring inputs (UTXOs/user input/external data from the outside world)
2. Creating output UTXOs with the result of the state transition

Thus to restate the above, your dApp may either be a single or multi-stage smart contract protocol. Each stage in your dApp's protocol may have one or more actions. These actions are then defined by you the developer via specifying the required inputs required for a given action, and encoding the required state transition logic in order to create output UTXOs which are embedded within a newly created `UnsignedTx`.

The HDF provides you with the required tools to specify each of these building blocks in order to build your headless dApp from the ground-up. In the sections below, we will go through further details about how the HDF is built, and how you yourself can get started using it today.

## Why is that a good thing?

Headless dApps provide the freedom to build an entire decentralized ecosystem. Because headless dApps are pure and portable by default, they can be compiled to any desktop OS, mobile OS, or browser. Because they have a streamlined interface, we can integrate them into scripts and bots trivially. Because they are composable, they can be used together in applications – for example, to enable arbitrage between different protocols, or entire new user experiences to be developed without understanding how every supported headless dApp works in detail. This makes them ideal for newer devs with limited experience developing smart contract protocols. They can still create powerful applications and have a real impact in the dApp world without immersing themselves in the intricacies of how every dApp functions.

## What are the business implications of headless dApps?

Headless dApps open up the ecosystem for a whole new business model. Rather than smart contact protocol creators sucking up all potential profit/value from the protocol's success, headless dApps uncover as yet untapped revenue streams for front-end devs. By decentralizing the potential profit from the protocol creators to include every developed frontend, we move away from the current model of popular dApps with a single hosted frontend. Instead, there’s the opportunity to incentivize a robust ecosystem composed of numerous independent frontends, built by multiple devs and companies – all of whom can profit from improving the ecosystem.



## Resources

In [this video](https://www.youtube.com/watch?v=temmjyKpsEU) Robert Kornacki breaks down the new concept of "Headless dApps". From covering the technical benefits of improving the dApp experience, business perspective of creating a new revenue model, and the overall ecosystem-building effect that Headless dApps enable, this video packs a lot of information into a relatively short time-frame.


##### Tutorials
- [Example: Minting Reserve Coins](https://github.com/ergoplatform/ergo-jde#example-minting-reserve-coins)
- [Writing JDE Scripts](https://github.com/ergoplatform/ergo-jde#writing-jde-scripts)
- [Using the web service](https://github.com/ergoplatform/ergo-jde#using-the-web-service)

##### Math Bounty Series

The Math Bounty Headless dApp tutorial series has been created to guide you through using the Ergo Headless dApp Framework. You will be lead step-by-step in developing your own headless dApp from project creation all the way to implementing a command line based interface.

- [Getting Started Writing Your First Action](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/tutorials/Math_Bounty/1-math-bounty-dApp-getting-started.md)
- [Finishing The Headless dApp](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/tutorials/Math_Bounty/2-math-bounty-dApp-finishing-the-headless-dapp.md)
- [Writing A CLI Frontend For Creating Bounties](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/tutorials/Math_Bounty/3-math-bounty-dApp-writing-a-cli-frontend-that-allows-creating-bounties.md)
  

##### References
- [Sample Scripts](https://github.com/ergoplatform/ergo-jde/tree/main/sample-scripts)
- [Syntax](https://github.com/ergoplatform/ergo-jde/blob/main/syntax.md)




