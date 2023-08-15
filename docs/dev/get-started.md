# Getting Started

Not sure where to start? This page will provide a basic overview of the entire site and the various entry pathways for developers. 

Any problem come chat to us on [Telegram](https://t.me/Ergo_Chats), [Discord](https://discord.gg/ergo-platform-668903786361651200), or [Matrix](https://matrix.to/#/#ergo-platform:matrix.org) which are bridged between each other. Alternative join us on [ergoforum.org](https://www.ergoforum.org/)

**Community sites**

- [ergo.watch](https://ergo.watch/) for on-chain analytics
- [ergonaut.space](https://ergonaut.space/) is Ergo's community wiki.
- To explore dApps, we have [sigmaverse.io](https://sigmaverse.io/) and [ergcube](https://ergcube.com/) 

## Background

- [Why Ergo](why.md) gives a quick overview of Ergo, some key features and the tech and decisions behind it. The [FAQ](faq.md) leads on from this, providing answers to some of the most frequently asked questions.
- Dive into the [protocol](protocol.md), the benefits of [eutxo](eutxo.md), and key features like [NiPoPoWs](nipopows.md), [Privacy](privacy.md), [Storage Rent](rent.md) and the [Autolykos](autolykos.md) algorithm.
- As well as linking to the foundational papers behind Ergo, the [Documents](documents.md) section also hosts the [EF Transparency Report](ergo-foundation-2022.md), and some commentary on the [Social Contract](social_contract.md), as well as how Ergo holds up to the [Howey Test](security.md).


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


## Learn

- Ergo employs a transactional model akin to Bitcoin, known as the Unspent Transaction Output (UTxO) model. Here, transactions expend and generate single-use entities, referred to as a ['box'](box.md). 
- Each Ergo [transaction](transaction.md) is an atomic state transition operation, which means that it destroys a box from the state and creates new ones.
- These boxes have several [registers](registers.md) that can hold various [assets](tokens.md) as well as complex [ErgoScript](#ergoscript) types.  


::cards::

[
  {
    "title": "📹 Ergo Blockchain Crash Course",
    "content": "",
    "url": "https://www.youtube.com/playlist?list=PL8-KVrs6vXLTVXGwmYXjOBRx3VymB4Vm2"

  },
  {
    "title": "📚 DeCo Intro Lessons",
    "content": "A Great Introductory course from Decentralised Collaboration",
    "url": "https://www.youtube.com/watch?v=qR0_k7VH6KI&list=PLopsKGshj0B4BpMoSMh5hQk8gVfWk-si6"
  },
  {
    "title": "📹 Learning blockchains like Cardano and Ergo",
    "url": "https://www.youtube.com/watch?v=HDn49bToTMI"
  },
]

::/cards::

## Infrastructure

The [Ergo Node](install.md) is a critical component of Ergo's peer-to-peer network, responsible for hosting and synchronizing a copy of the entire blockchain. You can [bootstrap from a verified UTXO snapshot](pruned-full-node.md), allowing you to get a pruned full node up and running on [testnet](testnet.md) in a couple of minutes. 

The [Node API](swagger.md) provides comprehensive access to Ergo node functionalities, including blockchain data retrieval, transaction submission, wallet management, and more. It offers a wide range of endpoints to interact with the Ergo network programmatically. If you don't want or need to run your own node, there are also several public [APIs](api.md) that offer different functionalities.



There is a publicly available explorer at [explorer.ergoplatform.com](https://explorer.ergoplatform.com/) (or [testnet.ergoplatform.com](https://testnet.ergoplatform.com/)), as well as [GraphQL](graphql.md) instances. You can install these all locally at once using a [Explorer & Node Bundles](install.md#Toolkits). 

- [uExplorer](ergo-uexplorer.md), a supplementary, lightweight Ergo explorer with CassandraDB backend. 
- [Blockchain Explorer with Raspberry Pi](rpi-blockchain-explorer.md)
- [Mining your own chain](mine-your-own-chain.md)


## Transactional Basics



- [Ergo Platform Basic Starter Tutorial](basics.md)
- [Create and send a transaction](https://www.youtube.com/watch?v=Md5s-XV6-Hs) using AppKit
- [Sign a transaction](sign-tx.md) using Sigma Rust
- [Sending a chained transaction](chained-tx.md) with Ergpy
- [Getting Started](https://fleet-sdk.github.io/docs/getting-started) with Fleet SDK

**Tokens**

- [Issuing a token](issue.md)
- [Burning a token](burn.md)
- [Minting an NFT](create.md)


## App development

There are many tools, libraries, SDKs, frameworks and utilities developers can use to interact with the blockchain, build their applications, and display them to users. The [Developer](start.md) section provides grid-buttons that let you narrow down your technical stack requirements and find the most appropriate tooling.

There are several *Standard Development Kits* and Frameworks available on Ergo. If your plan is develop a fully fleshed out decentralised application, You'll likely want to use one of the following depending on your needs.

**Primary SDKs**

- [AppKit](appkit.md) is the primary SDK, and the entry-point for JVM developers. (Java, Scala, Kotlin, Mobile)
- [Fleet SDK](fleet.md) lets you easily create Ergo transactions with a pure JS library. 
- [SigmaRust](sigma-rust.md) is an alternative and simple implementation of ErgoTree interpreter and transaction building tools that has bindings for JS/TS/Swift/Java/C/Ruby.

**Alternative SDKs**

- [ergpy](ergpy.md) is a python-jvm wrapper for interacting with the Ergo blockchain.
- [Mosaik](mosaik.md) is a *UI system for Ergo dApps*
- [Headless dApp Framework](headless.md) is a Rust framework for developing Ergo Headless dApps. The Ergo HDF provides developers with the first portable UTXO-based headless dApp development framework on any blockchain.
- [JSON dApp Environment](jde.md)
- [RustKit](rustkit.md) is also in development, which aims to bring the Rust experience in-line with the JVM one. 

**Tutorials**

- [Creating a simple pay-to-script app](p2s.md)
- [Get started with Ergo Mosaik: A UI system for Ergo dApps](mosaik.md)
- [Using AppKit from Python](https://github.com/ergoplatform/ergo-appkit/wiki/Using-Appkit-from-Python)



::cards::

[

  {
    "title": "📕 Side tooling for building dApps on Ergo",
    "url": "https://dav009.medium.com/ergo-101-side-tooling-for-building-dapps-on-ergo-c71889d60826"

  },
  {
    "title": "📕 DeCo Education: DApp Components - Backend",
    "url": "https://deco-education.github.io/deco-docs/docs/into-the-woods/trail2-ergo-coding/dapp-components"
  }
]

::/cards::

## ErgoScript

ErgoScript is a super-simple subset of Scala. It is a top-level language translated into a low-level language called ErgoTree, which is translated during execution into cryptographic protocol. That's how Ergo supports ring and threshold signatures and much more crypto protocols with no special cases made in the core!


- [Quick Primer](ergoscript-primer.md)
- [Sigma Language](sigma-lang.md)

### Experimenting

- To compile any ErgoScript contract in a P2S, you can use [**plutomonkey**](plutomonkey.md). Here are some [simple examples](p2s.md)
- [Scastie](scastie.md) is an online compiler for the Scala programming language. It's an ideal environment for developers looking to experiment, share, or learn Scala.

- [Kiosk](/dev/stack/kiosk) lets anyone play with ErgoScript using a basic web-based UI
- [ergo-puppet](puppet.md) is an advanced tool, building upon the foundational capabilities of the Ergo Playground. It is designed to facilitate experimentation with and unit testing of Ergo contracts in an offchain setting.

Courses, tutorials, explanations and further references can be found on the [ErgoScript Resources](ergoscript.md#resources) page. 

### Interpreters

There are two implementations of the ErgoScript compiler and ErgoTree interpreter for the [*'Sigma Language'*](sigma-lang.md).

- The [sigmastate-interpreter](sigmastate-interpreter.md) for JVM languages which is used by [AppKit](appkit.md)
- [sigma-rust](sigma-rust.md) is an alternative and simple implementation of ErgoTree interpreter and transaction-building tools. 

**Tooling**

- [ErgoScala](ergoscala.md) is a compiler for Ergo smart contracts written in ErgoScala (a subset of Scala).
- [CLI Compiler](compiler.md)
- [FlowCards](flowcards.md) is *A Declarative Framework for Development of Ergo dApps* 
- [flowcardLib: Ergo FlowCard library for diagrams.net](https://github.com/lucagdangelo/flowcardLib)
- [ergo-castanet](https://github.com/iandebeer/ergo-castanet)


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


- [Scrypto](scrypto.md) is a comprehensively built open-source cryptographic toolkit, specifically engineered to simplify and safeguard the process of integrating cryptography into your applications. Supporting AVL+ Trees and Batch Merkle Proof Serialization and Deserialization. 
- Learn how to create a threshold ring signature, verify schnorr signatures and more in the [Zero-Knowledge Tutorials](tutorials.md#zero-knowledge) section.



### AVL Trees

[AVL trees](avl.md) are highly efficient authenticated data structures that provide native support in Ergo. These trees offer several benefits, including the ability to authenticate data properties without accessing the entire dataset. Developers can seamlessly integrate AVL trees into their Ergo applications using the [GetBlok Plasma library](plasma.md).

### Multi-Stage Protocols

Multi-Stage Contracts is a technique wherein using transaction trees we can emulate persistent storage in UTXO-based systems by linking several UTXOs containing small pieces of code to form a large [multi-stage protocol](multi.md). This enables *on-chain computations*, making it possible to process parallelised actions on top of smart contracts.





