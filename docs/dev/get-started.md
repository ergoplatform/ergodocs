# Getting Started Guide

Welcome! If you're new here and feeling a bit overwhelmed, don't worry. This guide is designed to give you a comprehensive overview of our site and introduce you to the various resources available for developers.

### **Connect with Us**
If you encounter any issues or have questions, feel free to reach out to us on any of the following platforms. Remember, all our chat platforms are bridged, ensuring seamless communication:

- [Telegram](https://t.me/Ergo_Chats)
- [Discord](https://discord.gg/ergo-platform-668903786361651200)
- [Matrix](https://matrix.to/#/#ergo-platform:matrix.org)

For in-depth discussions and community interactions, join our forum at [ergoforum.org](https://www.ergoforum.org/).

## Background

**Introduction to Ergo**

- **[Why Ergo?](why.md)**: Get a concise overview of Ergo, its standout features, and the technology and decisions that power it.
- **[FAQ](faq.md)**: Find answers to the most common questions about Ergo.

**Technical Insights**

- **[Protocol Overview](protocol.md)**: Delve into the core of Ergo's protocol.
- **[EUTXO Benefits](eutxo.md)**: Understand the advantages of the Extended UTXO model.
- **Key Features**:
    -  Ergo mining is based on [Autolykos](autolykos.md), a fairly launched efficient ASIC-resistant Proof of Work algorithm.
    - [NiPoPoWs](nipopows.md) are compact data structures that validate the occurrence of events on a blockchain using proof-of-work, without needing to connect to the blockchain network or download all block headers
    - Optional Privacy
    - [Storage Rent](rent.md) or *demurrage* can be likened to 'on-chain garbage collection', a mechanism that not only mitigates the issue of blockchain bloat but also turns it into a profitable venture.


**Documentation & Reports**

- **[Foundational Papers](documents.md)**: Explore the academic and technical papers that laid the groundwork for Ergo.
- **[EF Transparency Report (2022)](ergo-foundation-2022.md)**: Gain insights into Ergo Foundation's operations and transparency initiatives.
- **[Ergo's Social Contract](social_contract.md)**: Delve into the principles and commitments that guide Ergo's community and development.
- **[Howey Test Analysis](security.md)**: Understand how Ergo measures up against the Howey Test for securities.

::cards::

[
  {
    "title": "🧾 Blockchain for Beginners: What is a Blockchain?",
    "url": "https://medium.com/@ergoplatform/blockchain-for-beginners-what-is-a-blockchain-23f3b66f7c62"
  },
  {
    "title": "📚 DeCo Laymens Course",
    "content": "A Great Introductory course aimed at the laymen from Decentralised Collaboration",
    "url": "https://www.youtube.com/watch?v=SAWeW6wajEw&list=PLopsKGshj0B6C1mg6RpDsj0rhYxam3_RZ"
  },
  {
    "title": "📹 More introductionary videos",
    "url": "tutorials/introductory-video"
  }
]

::/cards::

**Ergo Community Resources**

**Analytics & Insights**

- **[Ergo Watch](https://ergo.watch/)**: Dive into on-chain analytics and data.

**Community Knowledge Base**

- **[Ergonaut Space](https://ergonaut.space/)**: Discover Ergo's community-driven wiki, filled with insights and information.

**Explorer the ecosystem!**

- **[Sigmaverse.io](https://sigmaverse.io/)**: Explore a diverse range of dApps built on Ergo.
- **[ErgCube](https://ergcube.com/)**: Another platform to discover and interact with Ergo dApps.
- The [**Ecosystem**](ecosystem.md) section on this site acts as directory for projects building on Ergo and potential future ideas.


## **Understanding Ergo**

**Transactional Model**

- **[UTxO Model](#)**: Ergo adopts a transactional approach similar to Bitcoin's Unspent Transaction Output (UTxO) model. In this model, transactions utilize and produce single-use entities known as a ['box'](box.md).

**Transactions & State Transition**

- **[Ergo Transactions](transactions.md)**: Every transaction in Ergo represents an atomic state transition. This means a transaction eliminates a box from the state and introduces new ones in its place.

**Boxes & Their Components**

- **[Registers within Boxes](registers.md)**: Boxes come equipped with multiple registers capable of holding various assets and complex [ErgoScript](#ergoscript) types.
- **[Assets in Ergo](tokens.md)**: Dive deeper into the different assets that can be held within these boxes.


Here are some introductory videos that cover these concepts.

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

**Ergo Node & Network**

- **[Ergo Node](install.md)**: The backbone of Ergo's P2P network, responsible for hosting and synchronizing the entire blockchain.
  - **[Bootstrap from UTXO Snapshot](pruned-full-node.md)**: Quickly set up a pruned full node on the [testnet](testnet.md).
  - **[Fork Your Own Chain](mine-your-own-chain.md)**: Customize and create your own chain with specific parameters.

**API & Programmatic Access**

- **[Node API](swagger.md)**: Comprehensive access to Ergo node functionalities, from blockchain data retrieval to wallet management.
  - **[Public APIs](api.md)**: If running your own node isn't for you, utilize these public APIs for varied functionalities.

**Explorers**

- **Public Explorers**: Accessible at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/) and [testnet.ergoplatform.com](https://testnet.ergoplatform.com/).
- **[GraphQL Instances](graphql.md)**: Dive deeper with GraphQL.
- **[Explorer & Node Bundles](install.md#Toolkits)**: Install both locally for a comprehensive experience.
    - **[uExplorer](explorer.md)**: A lightweight Ergo explorer with a CassandraDB backend.
    - **[Blockchain Explorer with Raspberry Pi](rpi-blockchain-explorer.md)**: Set up an explorer using Raspberry Pi.


**Toolkits**

- **[danaides](https://github.com/ergopad/danaides)** is a performant blockchain toolset from ergopad.

**Off-chain**

- [Bootstrap an Oracle Pool on testnet](oracle-bootstrap.md)
- [Running off-chain bots](dex_bots.md)

## **Transactional Basics**

**Tutorials & Guides**

- **[Ergo Platform Basic Starter Tutorial](basics.md)**
- **[Create & Send a Transaction](https://www.youtube.com/watch?v=Md5s-XV6-Hs)** using AppKit
- **[Sign a Transaction](sign-tx.md)** with Sigma Rust
- **[Sending a Chained Transaction](chained-tx.md)** using Ergpy
- **[Getting Started with Fleet SDK](https://fleet-sdk.github.io/docs/getting-started)**

**Tokens & NFTs**

- **[Issuing a Token](issue.md)**
- **[Burning a Token](burn.md)**
- **[Minting an NFT](create.md)**


## App development


Developers have a plethora of tools, libraries, SDKs, frameworks, and utilities at their disposal to seamlessly interact with the blockchain, craft applications, and present them to users. Navigate through the [Developer Section](start.md) to use grid buttons that help refine your technical stack requirements and pinpoint the ideal tooling.

If you're aiming to develop a comprehensive decentralized application on Ergo, consider the following SDKs and frameworks tailored to your specific needs:

**Primary SDKs**

- **[AppKit](appkit.md)**: The go-to SDK for JVM developers, supporting Java, Scala, Kotlin, and Mobile platforms.
    - [Using AppKit with Python](https://github.com/ergoplatform/ergo-appkit/wiki/Using-Appkit-from-Python)
    - [General Example](tutorial.md)
    - [AppKit by Example](https://www.youtube.com/watch?v=Md5s-XV6-Hs)
- **[Fleet SDK](fleet.md)**: A pure JS library designed for effortless Ergo transaction creation.
- **[SigmaRust](sigma-rust.md)**: A straightforward ErgoTree interpreter and transaction tool with bindings for JS/TS/Swift/Java/C/Ruby.

**Alternative SDKs**

- **[Ergpy](ergpy.md)**: A Python-JVM wrapper facilitating interactions with the Ergo blockchain.
- **[Mosaik](mosaik.md)**: A dedicated UI system crafted for Ergo dApps.
- **[JSON dApp Environment](jde.md)**
- **[Headless dApp Framework](headless.md)**: A Rust-based framework for creating Ergo Headless dApps, marking the debut of a portable UTXO-centric headless dApp development framework on any blockchain.
- **[RustKit (In Development)](rustkit.md)**: An upcoming toolkit aiming to align the Rust development experience with the JVM.

**Payments**

- [**ErgoPay**](ergo-pay.md) is Ergo's dApp connector for non-web wallet
- [**dApp Connector**](dApp.md) is for connecting dApps to web-based wallets like Nautilus and SAFEW. 
- [**Proxy Contracts**](proxy.md) are a smart contract design used in blockchain ecosystems to enable secure and controlled interaction between users and decentralized applications. 

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

ErgoScript is a simplified subset of Scala. It's a high-level language that gets translated into a mid-level language named ErgoTree. During execution, ErgoTree is further translated into a cryptographic protocol. This unique architecture allows Ergo to seamlessly support ring and threshold signatures, along with various other cryptographic protocols, without any special core modifications.

**Introduction**

- [Quick Primer](ergoscript-primer.md)
- [Sigma Language](sigma-lang.md)
- [Creating a simple pay-to-script app](p2s.md)



### Experimenting

- **[PlutoMonkey](plutomonkey.md)**: Compile any ErgoScript contract into a P2S. Check out these [simple examples](p2s.md).
- **[Scastie](scastie.md)**: An online compiler tailored for Scala, perfect for developers eager to experiment, share, or learn Scala.
- **[Kiosk](/dev/stack/kiosk)**: A web-based UI to explore ErgoScript.
- **[Ergo-Puppet](puppet.md)**: An advanced tool built on the Ergo Playground, designed for off-chain experimentation and unit testing of Ergo contracts.


**Tooling**

- **[VSCode ErgoScript Language Support](https://github.com/GuapSwap/vscode-ergoscript-language-support)**
- **[ErgoScala](ergoscala.md)**: A compiler for Ergo smart contracts written in ErgoScala (a subset of Scala).
- **[CLI Compiler](compiler.md)**: A Command Line Interface tool to compile ErgoScript code into an Ergo address.
- **[FlowCards](flowcards.md)**: A declarative framework for developing Ergo dApps.


**Courses**

- [ErgoScript 101 Crash Course](https://docs.google.com/presentation/d/10gYO82z_7qloRrFOcCxTFuzpP40IImPyIKMV2ZFd9M4/edit#slide=id.p) (Slides)
- [Learn ErgoScript By Example Via The Ergo Playground with Robert Kornacki (Video)](https://www.youtube.com/watch?v=8l2v1asHgyA)

**Tutorials**

- [ErgoScript by Example Repository](https://github.com/ergoplatform/ergoscript-by-example)
- [Testing Ergo Contracts Off-chain](https://github.com/anon-real/contract-testing)
- [Debugging ErgoScript](debugging.md)


**Advanced Tutorials**

- [ErgoScript tutorial](https://ergoplatform.org/docs/ErgoScript.pdf)
- [Advanced ErgoScript Tutorial](https://ergoplatform.org/docs/AdvancedErgoScriptTutorial.pdf)



### Interpreters

ErgoScript has two compiler and ErgoTree interpreter implementations for the [*Sigma Language*](sigma-lang.md):

- **[Sigmastate-interpreter](sigmastate-interpreter.md)** for JVM languages, utilized by [AppKit](appkit.md).
- **[Sigma-Rust](sigma-rust.md)**: A simpler alternative for the ErgoTree interpreter and transaction tools.

### Cryptographic

Ergo has generic support ring and threshold signatures as well as a variety of cryptographic protocols via composable [sigma-protocols](crypto.md) built into the core.

ErgoScript provides two elementary Σ-protocols over a group of prime order (such as an elliptic curve)

**Crypto Primitives**

- **Hash**: `Sha256`, `Blake2b256`
- **Encoding**: `Base58`
- **Signing Algorithm**: ECDSA (`secp256k1`) & Schnorr 
- **Primitive Secrets**: [Schnorr Signature](schnorr.md) & [Diffie-Hellman tuple](diffie.md)
    - **[Schnorr signature](schnorr.md)**: A proof of knowledge of discrete logarithm with respect to a fixed group generator.
    - **[Diffie-Hellman tuple](diffie.md)**: A proof of equality of discrete logarithms.
- **Non-Interactive**: The proof of sigma-statements are made non-interactive with the [**Fiat-Shamir** transformation](diffie.md#fiat-shamir-transformation).
- [EIP-0003: Deterministic Wallet Standard](eip3.md)

See [this page](/dev/scs/global-functions/#cryptographic-functions) for a description of the global Cryptographic functions available in ErgoScript.


**Tutorials**

- [Creating a 3-out-of-5 Threshold Signature](sig.md)
- [Message signing and user authentication](message-signing.md)
- [Verifying Schnorr Signatures in ErgoScript](https://www.ergoforum.org/t/verifying-schnorr-signatures-in-ergoscript/3407)
- [Updateable Multisig Pattern](https://www.ergoforum.org/t/updateable-multisig-pattern/3356)
- [Making and implementing a signature, elliptic curves, and extended keys: Ergo with C#](https://www.youtube.com/watch?v=aUuki-fAxwc&list=PLUWruihtE-HtL-JZk8Vb4Yn_H18aE3rb6)


**Tools** 

- **[Scrypto](scrypto.md)** is a comprehensively built open-source cryptographic toolkit, specifically engineered to simplify and safeguard the process of integrating cryptography into your applications. Supporting AVL+ Trees and Batch Merkle Proof Serialization and Deserialization. 

### AVL Trees

**[AVL trees](avl.md)** are highly efficient authenticated data structures that provide native support in Ergo. These trees offer several benefits, including the ability to authenticate data properties without accessing the entire dataset. Developers can seamlessly integrate AVL trees into their Ergo applications using the **[GetBlok Plasma library](plasma.md)**.

### Multi-Stage Protocols

Multi-Stage Contracts is a technique wherein using transaction trees we can emulate persistent storage in UTXO-based systems by linking several UTXOs containing small pieces of code to form a large [multi-stage protocol](multi.md). This enables *on-chain computations*, making it possible to process parallelised actions on top of smart contracts.

