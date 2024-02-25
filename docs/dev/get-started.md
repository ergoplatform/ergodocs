
# Developer's Guide

/// admonition | Welcome to the Ergo Developer's Guide
This comprehensive guide is designed to provide an overview of our platform and introduce you to the various resources available for developers. Whether you're a seasoned blockchain developer or just starting out, this guide will help you navigate the Ergo ecosystem and understand its key features and functionalities.
///

### **Connect with Our Community**
If you encounter any issues or have questions, feel free to connect with us on any of the following platforms. All our chat platforms are bridged, ensuring seamless communication:

- [Telegram](https://t.me/Ergo_Chats)
- [Discord](https://discord.gg/ergo-platform-668903786361651200)
- [Matrix](https://matrix.to/#/#ergo-platform:matrix.org)

For in-depth discussions and community interactions, join our forum at [ergoforum.org](https://www.ergoforum.org/).

##### Contributing

- We host regular hackathons which are a great opportunity to get involved. For more information and links to past entries see [this page](ergohack.md)
- See the [Contributing Guidelines](guidelines.md) for information on bounties and grants. 


## Ergo Platform Overview

Ergo is a revolutionary platform that establishes the foundation for a new wave of blockchain-based applications. It is designed with a focus on decentralization, scalability, and security. Ergo's standout features include its advanced smart contract capabilities, efficient proof-of-work consensus algorithm, and robust transactional model. This section provides an overview of Ergo, its key features, and resources for further exploration.




##### **Introduction to Ergo**

- Get a concise overview of Ergo, its standout features, and the technology and decisions that power it on the **[*Why Ergo?*](why.md)** page.
- Find answers to the most common questions about Ergo in our **[FAQ](faq.md)**. 

##### **Technical Insights**

- **[Protocol Overview](protocol.md)**: Dive deep into the core mechanisms of Ergo's protocol.
- **[EUTXO Benefits](eutxo.md)**: Understand the advantages of Ergo's Extended UTXO model, which allows UTXOs to carry arbitrary data and complex scripts.
- **Key Features**:
    -  **Mining**: Ergo utilizes [Autolykos](autolykos.md), an efficient, ASIC-resistant Proof of Work algorithm designed for fair launch.
          -  Learn about Ergo's [Emission](emission.md) schedule.
    - **NiPoPoWs**: Short for Non-Interactive Proofs of Proof-of-Work, [NiPoPoWs](nipopows.md) are compact data structures that validate blockchain events without needing full network connectivity or downloading all block headers. They enable efficient light clients, log-space mining, and trustless sidechains.
    - **ErgoScript**: A simple high-level language that enables clear descriptions of contractual logic and supports flexible crypto-contracts based on Σ-protocols.
    - **Storage Rent**: Also known as [demurrage](rent.md), this mechanism mitigates blockchain bloat and turns it into a profitable venture by charging for on-chain storage.
    - **Turing Complete Smart Contracts**: Ergo supports [Turing complete smart contracts](#multi-stage-protocols), enabling complex on-chain computations.


##### **Documentation & Reports**

- **[Foundational Papers](documents.md)**: Explore the academic and technical papers that laid the groundwork for Ergo.
- **[EF Transparency Report](ergo-foundation.md)**: Gain insights into Ergo Foundation's operations and transparency initiatives.
- **[Ergo's Social Contract](social_contract.md)**: Delve into the principles and commitments that guide Ergo's community and development.
- **[Howey Test Analysis](security.md)**: Understand how Ergo measures up against the Howey Test for securities.

::cards::

[
  {
    "title": "🧾 Blockchain for Beginners: What is a Blockchain?",
    "url": "https://medium.com/@ergoplatform/blockchain-for-beginners-what-is-a-blockchain-23f3b66f7c62"
  },
  {
    "title": "📚 DeCo EU Layman Class - Basics of eUTxO",
    "content": "A Great Introductory course aimed at the laymen from Decentralised Collaboration",
    "url": "https://www.youtube.com/watch?v=SAWeW6wajEw"
  },
  {
    "title": "📹 More introductory videos",
    "url": "tutorials/introductory-video"
  },
  {
    "title": "🧾 Learning Ergo 101 : eUTXO explained for human beings",
    "url": "https://dav009.medium.com/learning-ergo-101-blockchain-paradigm-eutxo-c90b0274cf5e"
  }
]

::/cards::


## **Understanding Ergo**

Ergo is a next-generation Proof of Work smart-contract platform that enables new models of financial interaction, underpinned by a safe and rich scripting language (ErgoScript) and flexible and powerful Zero-Knowledge proofs (Σ-protocols). 


##### **Transactional Model**

- Ergo adopts a transactional approach similar to Bitcoin's Unspent Transaction Output (UTxO) model. In this model, transactions utilize and produce single-use entities known as a ['box'](box.md).
- Every [transaction](transactions.md) in Ergo represents an atomic state transition. This means a transaction eliminates a box from the state and introduces new ones in its place.
- The eUTXO model allows each UTXO to carry arbitrary data and to be protected by an arbitrary predicate (or [spending condition](types.md#sigmaprop)). The data can be used to represent arbitrary tokens or smart contract states.

##### **Boxes & Their Components**

- **[Registers within Boxes](registers.md)**: Boxes come equipped with multiple registers capable of holding various assets and complex [ErgoScript](#ergoscript) types.
- **[Assets in Ergo](tokens.md)**: Dive deeper into the different assets that can be held within these boxes.


Here are some introductory resources that cover these concepts.

::cards::

[
  {
    "title": "📹 Ergo Blockchain Crash Course",
    "content": "Ergo crash course, presented by developer Luca (lgd) covering the eUTXO model, Anatomy of Ergo and more.",
    "url": "https://www.youtube.com/playlist?list=PL8-KVrs6vXLTVXGwmYXjOBRx3VymB4Vm2"

  },
  {
    "title": "📚 DeCo Intro Lessons",
    "content": "Programming basics for the laymen, from DeCo (Decentralised Collaboration)",
    "url": "https://www.youtube.com/watch?v=qR0_k7VH6KI&list=PLopsKGshj0B4BpMoSMh5hQk8gVfWk-si6"
  },
  {
    "title": "📹 Learning blockchains like Cardano and Ergo",
    "content": "Discusses the process of learning blockchain concepts, emphasizing the significance of understanding these theoretical aspects, practical interaction through playgrounds and nodes.",
    "url": "https://www.youtube.com/watch?v=HDn49bToTMI"
  },
]

::/cards::


## **Ergo Infrastructure**


##### **Ergo Node & Network**

- **[Ergo Node](install.md)**: The Ergo Node forms the core of Ergo's P2P network, maintaining and synchronizing the entire blockchain.
  - **[Bootstrap from UTXO Snapshot](pruned-full-node.md)**: Expedite the setup of a pruned full node on the [testnet](testnet.md) by bootstrapping from a UTXO snapshot.
  - **[Fork Your Own Chain](mine-your-own-chain.md)**: Learn how to customize and create your own chain with specific parameters.

##### **API & Programmatic Access**

- **[Node API](swagger.md)**: Gain comprehensive overview of the Ergo node API functionalities.
  - **[Public APIs](api.md)**: If you prefer not to run your own node, you can utilize these public APIs for a variety of functionalities.

##### **Explorers**

- **Public Explorers** can be accessed at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/) and [testnet.ergoplatform.com](https://testnet.ergoplatform.com/).
- Delve deeper into blockchain data with **[GraphQL](graphql.md)**.
- **[Explorer & Node Bundles](install.md#Toolkits)**: Install both locally for a comprehensive blockchain experience.
    - **[uExplorer](explorer.md)**: A lightweight Ergo explorer backed by CassandraDB.
    - **[Blockchain Explorer with Raspberry Pi](rpi-blockchain-explorer.md)**: Learn how to set up an explorer using Raspberry Pi.


##### **Toolkits**

- **[danaides](https://github.com/ergopad/danaides)**: A high-performance blockchain toolkit.

##### **Off-chain**

- [Bootstrap an Oracle Pool on testnet](oracle-bootstrap.md)
- [Running off-chain bots](dex_bots.md)

## **Transactional Basics**

##### **Tutorials & Guides**

- **[Ergo Platform Basic Starter Tutorial](basics.md)**
- **[Create & Send a Transaction](https://www.youtube.com/watch?v=Md5s-XV6-Hs)**: A video tutorial on creating and sending a transaction using AppKit.
- **[Sign a Transaction](sign-tx.md)**: Learn how to sign a transaction with Sigma Rust.
- **[Sending a Chained Transaction](chained-tx.md)**: A guide on sending a chained transaction using Ergpy.
- **[Getting Started with Fleet SDK](https://fleet-sdk.github.io/docs/getting-started)**: A beginner's guide to the Fleet SDK.

##### **Tokens & NFTs**

- **[Issuing a Token](tokens.md)**: A step-by-step guide on how to issue a token on Ergo.
- **[Burning a Token](burn.md)**: Learn how to burn a token, effectively removing it from circulation.
- **[Minting an NFT](create.md)**: A comprehensive guide on creating a Non-Fungible Token (NFT) on Ergo.
- **[Minting a on-chain NFT](on-chain.md)**: Don't want to rely on third-party storage? You can squeeze a NFT directly into the registers!

## App development

Developers have a plethora of tools, libraries, SDKs, frameworks, and utilities at their disposal to seamlessly interact with the blockchain, craft applications, and present them to users. Navigate through the [Developer Section](start.md) to use grid buttons that help refine your technical stack requirements and pinpoint the ideal tooling.


If you're aiming to develop a comprehensive decentralized application on Ergo, consider the following SDKs and frameworks tailored to your specific needs:

/// admonition | As a spreadsheet!
Most repositories are also categories on [grist](https://ergo.getgrist.com/jf9KPR1HUDJH/Project-Management). This is a great place to start if you're looking for a specific repository or want to see what's currently being worked on.
///

##### **Primary SDKs**

- **[AppKit](appkit.md)**: The go-to SDK for JVM developers, supporting Java, Scala, Kotlin, and Mobile platforms.
    - [General Example](tutorial.md)
    - [Using AppKit with Python](https://github.com/ergoplatform/ergo-appkit/wiki/Using-Appkit-from-Python)
    - [AppKit by Example](https://www.youtube.com/watch?v=Md5s-XV6-Hs)
- **[Fleet SDK](fleet.md)**: A pure JS library designed for effortless Ergo transaction creation.
    - [The Ergo Web Template](https://github.com/SavonarolaLabs/ergo-web-template), serves as an introductory guide for individuals new to Ergo. This resource aims to streamline the onboarding process for newcomers by offering them a hands-on experience with essential Ergo functionalities.
- **[SigmaRust](sigma-rust.md)** is a ErgoTree interpreter with transaction tools and bindings for JS/TS/Swift/Java/C/Ruby.
    - [Address Generation Demo](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm/examples/address-generation-demo)
    - [Create Transaction Demo](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm/examples/create-transaction-demo)

##### **Alternative SDKs**

- **[Ergpy](ergpy.md)** is a Python-JVM wrapper facilitating interactions with the Ergo blockchain.
- **[Mosaik](mosaik.md)** is a dedicated UI system crafted for Ergo dApps.
- **[JSON dApp Environment](jde.md)**
- **[Headless dApp Framework](headless.md)**: A Rust-based framework for creating Ergo Headless dApps, marking the debut of a portable UTXO-centric headless dApp development framework on any blockchain.
- **[RustKit (In Development)](rustkit.md)**: An upcoming toolkit aiming to align the Rust development experience with the JVM.

##### **Payments**

- [**ErgoPay**](ergo-pay.md) is Ergo's dApp connector for non-web wallet
- [**dApp Connector**](dApp.md) is for connecting dApps to web-based wallets like Nautilus and SAFEW. 
- [**Proxy Contracts**](proxy.md) are a smart contract design used in blockchain ecosystems to enable secure and controlled interaction between users and decentralized applications. 

##### **Librarie**

- [ergo-lib-go](https://github.com/ergoplatform/ergo-lib-go): Go wrapper around C bindings for ErgoLib from sigma-rust
- [ergo-lib-wasm](https://github.com/ergoplatform/ergo-lib-wasm): ergo-lib bindings for JS/TS
- [ergo_client](https://github.com/ross-weir/ergo_client):	Rust library containing HTTP clients for various Ergo applications
- [sigma-builders](https://github.com/GuapSwap/sigma-builders): Easy to use library for creating protocol abstractions interacting with Ergo blockchain.


##### Templates


::cards::

[

  {
    "title": "📕 Side tooling for building dApps on Ergo",
    "url": "https://dav009.medium.com/ergo-101-side-tooling-for-building-dapps-on-ergo-c71889d60826",
    "content": "Building functional dApps on Ergo requires more than just smart contracts and transactions."

  },
  {
    "title": "📕 DeCo Education: DApp Components - Backend",
    "url": "https://deco-education.github.io/deco-docs/docs/into-the-woods/trail2-ergo-coding/dapp-components"
  }  ,
  {
    "title": "📕 DeCo Intro Lessons: Build a mobile app on Android or iOS",
    "url": "https://www.youtube.com/watch?v=qR0_k7VH6KI&list=PLopsKGshj0B4BpMoSMh5hQk8gVfWk-si6"
  }
]


::/cards::

## ErgoScript

ErgoScript is a super-simple subset of Scala, enabling clear descriptions of contractual logic that can be Turing complete. 

It is flexible enough to allow for ring signatures, multi-signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.

The Account model of Ethereum is imperative. This means that the typical task of sending coins from Alice to Bob requires changing the balances in storage as a series of operations. On the other hand, Ergo's UTXO based programming model is declarative. ErgoScript contracts specify conditions for a transaction to be accepted by the blockchain (not changes to be made in the storage state as a result of the contract execution).

##### **Introduction**

- [Quick Primer](ergoscript-primer.md)
- [Core Concepts of ErgoScript](ergoscript-key-concepts.md)
- [Sigma Language](sigma-lang.md)
- [Creating a simple pay-to-script app](p2s.md)



##### Experimenting

- **[escript.online](https://escript.online/)**
- **[PlutoMonkey](plutomonkey.md)**: Compile any ErgoScript contract into a P2S. Check out these [simple examples](p2s.md).
- **[Scastie](scastie.md)**: An online compiler tailored for Scala, perfect for developers eager to experiment, share, or learn Scala.
- **[Kiosk](/dev/stack/kiosk)**: A web-based UI to explore ErgoScript.
- **[Ergo-Puppet](puppet.md)**: An advanced tool built on the Ergo Playground, designed for off-chain experimentation and unit testing of Ergo contracts.


##### **Tooling**

- **[Ergo Development Generics Elements](https://github.com/Ergo-Lend/edge)**
- **[VSCode ErgoScript Language Support](https://github.com/GuapSwap/vscode-ergoscript-language-support)**
- **[ErgoScala](ergoscala.md)**: A compiler for Ergo smart contracts written in ErgoScala (a subset of Scala).
- **[CLI Compiler](compiler.md)**: A Command Line Interface tool to compile ErgoScript code into an Ergo address.
- **[FlowCards](flowcards.md)**: A declarative framework for developing Ergo dApps.
- **[ergo-playgrounds](https://github.com/ergoplatform/ergo-playgrounds)**: Run contracts + off-chain code in the browser
- **[ergo-script-re](https://github.com/ross-weir/ergo-script-re/tree/main)**: Libraries for Ergo Script reverse engineering and analysis

##### **Courses**

If you're interested in deepening your understanding of ErgoScript and the Ergo ecosystem, consider taking one of the following courses:

- [DeCo Education: Into the Woods](https://deco-education.github.io/deco-docs/docs/category/into-the-woods): This course provides a comprehensive introduction to the Ergo ecosystem.
- [ErgoScript 101 Crash Course](https://docs.google.com/presentation/d/10gYO82z_7qloRrFOcCxTFuzpP40IImPyIKMV2ZFd9M4/edit#slide=id.p) (Slides): A crash course that covers the basics of ErgoScript, perfect for beginners.
- [Learn ErgoScript By Example Via The Ergo Playground with Robert Kornacki (Video)](https://www.youtube.com/watch?v=8l2v1asHgyA): This video tutorial offers practical examples of how to use ErgoScript in the Ergo Playground.
- [DeCo-Education/ErgoScript-Developer-Course](https://github.com/DeCo-Education/ErgoScript-Developer-Course): A more advanced course for developers looking to build on their ErgoScript knowledge.

##### **Tutorials**

- [ErgoScript by Example Repository](https://github.com/ergoplatform/ergoscript-by-example)
- [Testing Ergo Contracts Off-chain](https://github.com/anon-real/contract-testing)
- [Debugging ErgoScript](debugging.md)
- [ergo-playground](https://github.com/jaysee260/ergo-playground): A collection of miscellaneous scenarios implemented on the Ergo blockchain.

##### **Boilerplate**

- [scala-play-next-ergo](https://github.com/kii-dot/scala-play-next-ergo)
- [ergo-scala-skeleton-app](https://github.com/dav009/ergo-scala-skeleton-app)
- [The Ergo Web Template](https://github.com/SavonarolaLabs/ergo-web-template), serves as an introductory guide for individuals new to Ergo. This resource aims to streamline the onboarding process for newcomers by offering them a hands-on experience with essential Ergo functionalities.
- [Ergo-play-boilerplate](https://github.com/kii-dot/ergo-play-boilerplate)


##### **Advanced Tutorials**

- [ErgoScript tutorial](https://ergoplatform.org/docs/ErgoScript.pdf)
- [Advanced ErgoScript Tutorial](https://ergoplatform.org/docs/AdvancedErgoScriptTutorial.pdf)



### Interpreters

ErgoScript has two compiler and ErgoTree interpreter implementations for the [*Sigma Language*](sigma-lang.md):

- **[Sigmastate-interpreter](sigmastate-interpreter.md)** for JVM languages, utilized by [AppKit](appkit.md).
- **[Sigma-Rust](sigma-rust.md)**: A simpler alternative for the ErgoTree interpreter and transaction tools.

### Cryptographic

Ergo has generic support ring and threshold signatures as well as a variety of cryptographic protocols via composable [sigma-protocols](crypto.md) built into the core.

Sigma Protocols (Σ-Protocols) are the foundation of Ergo’s smart contracts. Their advantage is that they are composable, using simple AND/OR logic. 

When combined with a blockchain, these composable proofs enable very powerful use cases, while allowing for the implementation of sophisticated tasks that would otherwise be impossible, risky, or expensive on other platforms. 


##### **Crypto Primitives**

- **Hash**: `Sha256`, `Blake2b256`
- **Encoding**: `Base58`
- **Signing Algorithm**: ECDSA (`secp256k1`) & Schnorr 
- **Primitive Secrets**: [Schnorr Signature](schnorr.md) & [Diffie-Hellman tuple](diffie.md)
    - **[Schnorr signature](schnorr.md)**: A proof of knowledge of discrete logarithm with respect to a fixed group generator.
    - **[Diffie-Hellman tuple](diffie.md)**: A proof of equality of discrete logarithms.
- **Non-Interactive**: The proof of sigma-statements are made non-interactive with the [**Fiat-Shamir** transformation](diffie.md#fiat-shamir-transformation).
- [EIP-0003: Deterministic Wallet Standard](eip3.md)

See [this page](/dev/scs/global-functions/#cryptographic-functions) for a description of the global Cryptographic functions available in ErgoScript.

##### **Tutorials**

- [Creating a 3-out-of-5 Threshold Signature](sig.md)
- [Message signing and user authentication](message-signing.md)
- [Verifying Schnorr Signatures in ErgoScript](https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407)
- [Updateable Multisig Pattern](https://www.ergoforum.org/t/updateable-multisig-pattern/3356)
- [Making and implementing a signature, elliptic curves, and extended keys: Ergo with C#](https://www.youtube.com/watch?v=aUuki-fAxwc&list=PLUWruihtE-HtL-JZk8Vb4Yn_H18aE3rb6)


##### **Tools** 

- **[Scrypto](scrypto.md)** is a comprehensively built open-source cryptographic toolkit, specifically engineered to simplify and safeguard the process of integrating cryptography into your applications. Supporting AVL+ Trees and Batch Merkle Proof Serialization and Deserialization. 

### AVL Trees (Plasma)

**[AVL trees](avl.md)** are highly efficient authenticated data structures natively supported in Ergo. These trees offer several benefits, including the ability to authenticate data properties without accessing the entire dataset. Developers can seamlessly integrate AVL trees into their Ergo applications using one of the **[Plasma](plasma.md)** libraries.

### Multi-Stage Protocols

Multi-Stage Contracts is a technique wherein using transaction trees we can emulate persistent storage in UTXO-based systems by linking several UTXOs containing small pieces of code to form a large [multi-stage protocol](multi.md). This enables *on-chain computations*, making it possible to process parallelised actions on top of smart contracts and construct **Turing-complete** applications.


## **Ergo Community Resources**

##### **Analytics & Insights**

- **[Ergo Watch](https://ergo.watch/)**: Dive into on-chain analytics and data.

##### **Community Knowledge Base**

- **[Ergonaut Space](https://ergonaut.space/)**: Discover Ergo's community-driven wiki, filled with insights and information.

##### **Explore the Ecosystem!**

- **[Sigmaverse.io](https://sigmaverse.io/)**: Explore a diverse range of dApps built on Ergo.
- **[ErgCube](https://ergcube.com/)**: Another platform to discover and interact with Ergo dApps.
- The [**Ecosystem**](../uses/index.md) section on this site acts as directory for projects building on Ergo and potential future ideas.

