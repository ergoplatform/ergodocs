*This new approach offers a streamlined interface for interacting with on-chain contracts, enabling anyone to build dApps using simple building blocks.*

So-called headless dApps are a new idea in the blockchain world, and one that offers exciting new possibilities for developers and the DeFi sector. It’s also one that Ergo will be exploring in due course.

Before we make further announcements, it’s worth exploring the idea a little further. If you’re new to the idea of headless dApps, you’ll likely have questions...

## What are ‘headless’ dApps?

Headless dApps are a brand new technical and business model for developing dApps that is just beginning to take hold in the blockchain space. Headless dApps are the pure and portable self-contained logic for reading and participating in on-chain smart contract protocols. In other words, a headless dApp is a piece of software that exposes the complex on-chain protocols to the off-chain world with a streamlined interface that anyone can build on. The dApps themselves have no frontend of their own – hence they are ‘headless’.

## Why is that a good thing?

Headless dApps provide the freedom to build an entire decentralized ecosystem. Because headless dApps are pure and portable by default, they can be compiled to any desktop OS, mobile OS, or browser. Because they have a streamlined interface, they can be integrated into scripts and bots trivially. Because they are composable, they can be used together in applications – for example, to enable arbitrage between different protocols, or entire new user experiences to be developed without having to understand how each and every supported headless dApp works in detail. This makes them ideal for newer devs with limited experience of developing smart contract protocols. They can still create powerful applications and have a real impact in the dApp world without immersing themselves in the intricacies of how every dApp functions.

## What are the business implications of headless dApps?

Headless dApps open up the ecosystem for a whole new business model. Rather than smart contact protocol creators sucking up all potential profit/value from the success of the protocol, headless dApps uncover as yet untapped revenue streams for front-end devs. By decentralizing the potential profit from the protocol creators to include each and every frontend that is developed, we move away from the current model of popular dApps with a single hosted frontend. Instead, there’s the opportunity to incentivize a robust ecosystem composed of numerous independent frontends, built by multiple devs and companies – all of whom can profit from improving the ecosystem as a whole.

## TL;DR?

Headless dApps provide any developer with easy access to powerful blockchain functionality, allowing them to create and monetise their own applications based on these building blocks.

Watch this space – because we have some great new developments on the way very soon!

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



*This new development will have a number of implications for the Ergo ecosystem and developers, making it far easier to build applications on Ergo.*

In a recent article, we looked at the idea of [‘Headless’ dApps](https://ergoplatform.org/en/blog/2020-11-27-an-introduction-to-headless-dapps/): portable dApp off-chain code that can be used by anyone to ship dApps easily by plugging different components together and adding an interface. 

On 30 November, a new release was made from the Emurgo code repository: the [Ergo Headless dApp Framework (HDF)](https://github.com/Emurgo/ergo-headless-dapp-framework)!

**What is the Ergo Headless dApp Framework?**

Ergo HDF is a Rust framework for building Ergo Headless dApps. It provides developers with the very first portable UTXO-based headless dApp development framework on any blockchain.

The Ergo HDF project makes it easy for developers who are new to blockchain to create dApps without understanding smart contracts in detail, but has a number of goals:

1. Enable developers to write their off-chain logic only once, using the HDF to create their own headless dApps, thereby allowing them to target all platforms (desktop, web, mobile) easily.
2. Provide developers with an easy experience to go from [Ergo dApp Specifications](https://github.com/ergoplatform/eips/blob/master/eip-0006.md) to headless dApps with greater assurance and a straightforward implementation path.
3. Separate dApps’ off-chain logic from frontend logic, thereby allowing reusability no matter what application or front-end is attempting to integrate a headless dApp.
4. Provide easy-to-use methods for front-end developers to access the current state of the dApp protocol, without having to understand how any of it works.
5. Abstracting the concept of defining and acquiring input UTXOs for a headless dApp by using a novel design pattern, specifying a ‘BoxSpec’ for each required input UTXO.
6. Enabling scripts, trading bots, and other software to be trivially built on top of multiple headless dApps created with the HDF, thereby offering a standardised interface and high degree of composability.

To give one example, the Ergo HDF makes it really easy to acquire data points from [Ergo’s oracle pools](https://ergoplatform.org/en/blog/2020-08-31-ergos-oracle-pools-and-what-they-mean-for-the-ecosystem/), without needing to understand how they work in depth.

A tutorial series is being created, providing a step-by-step guide to developing your own headless dApp. Check out the first lesson: the [Math Bounty Headless dApp](https://github.com/Emurgo/ergo-headless-dapp-framework/blob/main/tutorials/Math_Bounty/1-math-bounty-dApp-getting-started.md).

To find out more about Emurgo’s work and view the Ergo HDF, see the [Headless dApp Framework on the Emurgo code repo](https://github.com/Emurgo/ergo-headless-dapp-framework).

<!--EndFragment-->