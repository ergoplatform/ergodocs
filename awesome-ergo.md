<!-- Awesome Ergo – Redesigned 🍀 -->

<p align="center">
  <img src="https://raw.githubusercontent.com/ergoplatform/ergodocs/master/docs/assets/logo.png" width="120" alt="Ergo logo"/>
</p>

<h1 align="center">🌟 Awesome <span style="color:#f04e23">Ergo</span></h1>

<p align="center">
  A hand‑picked treasure chest of projects, tools & resources powering the <strong>Ergo Blockchain</strong> ecosystem.<br/>
  Every link is community‑verified & battle‑tested — pull requests are very welcome!
</p>

<p align="center">
  <a href="https://github.com/ergoplatform/awesome-ergo/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen?logo=github" alt="PRs welcome"></a>
  <a href="https://github.com/ergoplatform/awesome-ergo/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-CC0_1.0-lightgrey.svg" alt="License: CC0"></a>
</p>

> **Contributing:** open a PR to add or update projects. Items must be active & have a working URL.
> Docs live in <https://github.com/ergoplatform/ergodocs>, while this list lives in <https://github.com/ergoplatform/awesome-ergo>.

---

## 📚 Table of Contents

- 🏗️ [Core Infrastructure](#core-infrastructure)
  - ⚙️ [Nodes](#nodes)
  - 🔮 [Oracles](#oracles)
  - 🌉 [Bridges](#bridges)
- 💼 [Wallets](#wallets)
  - 🖥️ [Browser & Desktop](#browser--desktop)
  - 📱 [Mobile](#mobile)
  - 🛟 [Utilities & Recovery](#utilities--recovery)
- 📚 [SDKs & Libraries](#sdks--libraries)
  - 🎯 [Primary SDKs](#primary-sdks)
  - 🔒 [Core Libraries & Cryptography](#core-libraries--cryptography)
  - 🔗 [Language Bindings & Wrappers](#language-bindings--wrappers)
  - 🤝 [Community SDKs/Libraries](#community-sdkslibraries)
- 🛠️ [Development Tooling](#development-tooling)
  - 📜 [Smart Contracts & ErgoScript](#smart-contracts--ergoscript)
  - 🧱 [Frameworks](#frameworks-dev)
  - 📄 [Templates](#templates)
  - 🔧 [Utilities](#utilities)
  - ⌨️ [CLI Tools](#cli-tools)
  - 🔌 [Node Interaction & APIs](#node-interaction--apis)
  - 🧪 [Testing & Debugging](#testing--debugging)
  - 💳 [Payments](#payments)
  - ✨ [Examples & Snippets](#examples--snippets)
- 💸 [DeFi & dApps](#defi--dapps)
  - 💹 [DEXs & Swaps](#dexs--swaps)
  - 🏦 [Stablecoins & Lending](#stablecoins--lending)
  - 🚀 [Launchpads](#launchpads)
  - 🆔 [Identity & DNS](#identity--dns)
  - 🤫 [Privacy](#privacy)
  - 🎮 [Gaming & Metaverse](#gaming--metaverse)
  - 🏛️ [DAO Frameworks](#dao-frameworks)
  - 🧩 [Other dApps & Services](#other-dapps--services)
- 🖼️ [NFT Ecosystem](#nft-ecosystem)
  - 🛒 [Marketplaces & Auctions](#marketplaces--auctions)
  - 🎨 [Minting & Utilities](#minting--utilities)
  - 🗿 [NFT Projects](#nft-projects)
- ⛏️ [Mining](#mining)
  - 🏊 [Pools](#pools)
  - 💻 [Software](#software)
  - 🔧 [Utilities & Tooling](#utilities--tooling)
  - 🧠 [Smart Pooling](#smart-pooling)
  - 🔐 [Hardware Wallet Support](#hardware-wallet-support) <!-- Moved Here -->
- 📜 [Standards (EIPs)](#standards-eips)
- 🔍 [Explorers & Dashboards](#explorers--dashboards)
- 📊 [Analytics](#analytics)
- 🤝 [Community & Resources](#community--resources)
  - 📰 [Information Hubs](#information-hubs)
  - 💰 [Contribution Platforms](#contribution-platforms)
  - 🎓 [Education & Tutorials](#education--tutorials)
  - 📄 [Papers & Specifications](#papers--specifications)
  - 🔩 [Utilities](#utilities)

---

## 🏗️ Core Infrastructure <a id="core-infrastructure"></a>

> See also: [Protocol Overview on ErgoDocs](https://docs.ergoplatform.com/dev/protocol/protocol-overview/)

### ⚙️ Nodes <a id="nodes"></a>

- **[Reference Client (Node)](https://github.com/ergoplatform/ergo)** – official Scala implementation. [`Scala`] *(Active)*
  - *See [Ergo Documentation](https://docs.ergoplatform.com/node/install/) for installation guides, including [bootstrapping from a UTXO snapshot](https://docs.ergoplatform.com/node/pruned-full-node/).*
- [Ergode](https://github.com/ross-weir/ergode) – experimental TypeScript node. [`TS`]

### 🔮 Oracles <a id="oracles"></a>

- **[Oracle Core](https://github.com/ergoplatform/oracle-core)** – core implementation for oracle pools V2. [`Rust`] *(Active)*
  - [Oracle Pool Bootstrap](https://github.com/ergoplatform/oracle-core/tree/master/oracle-pool-bootstrap)
  - [Connector Library](https://github.com/ergoplatform/oracle-core/tree/master/connectors/connector-lib)
  - [How-To Guide](https://github.com/ergoplatform/oracle-core/blob/develop/docs/how_to_bootstrap.md)
  - [Tutorial: How I bootstrapped an ERG/XAU pool on testnet](https://github.com/ergoplatform/oracle-core/blob/develop/docs/how_to_bootstrap.md)
- [EIP-23 Oracle Pools 2.0 Spec](https://github.com/ergoplatform/eips/pull/41)
- [Ergo Oracles V1 Overview](https://github.com/Emurgo/Emurgo-Research/blob/master/oracles/Oracle-Pools.md)
- [Ergo Easy Oracle](https://github.com/reqlez/ergo-easy-oracle) – Docker deployment helper. [`Docker`]
- [Oracle Core ETH Connector Fork](https://github.com/Luivatra/oracle-core/tree/eth-connector) [`Rust`]
- [Sininen Taivas Oracle CLI](https://github.com/sininen-taivas/ergo-oracle) [`Go`?]
- [Oracle Pool V1 Kiosk Example](https://github.com/scalahub/Kiosk/tree/master/src/test/scala/kiosk/oraclepool/v4a) [`Scala`]
- [Oracle Pool Stats Backend (Delphi)](https://github.com/thedelphiproject/ergo-oracle-stats-backend)
- [Oracle Tools JS (Delphi)](https://github.com/thedelphiproject/ergo-oracle-tools-js) [`JS`]

### 🌉 Bridges <a id="bridges"></a>

- **[Rosen Bridge](https://rosen.tech/)** – primary cross-chain bridge *(Live)*. [GitHub Org](https://github.com/rosen-bridge) *(Active)*
  - [Contracts](https://github.com/rosen-bridge/contract) [`JS/TS`, `Scala`]
  - [Watcher & Guard](https://github.com/rosen-bridge/operation) [`Scala`?]
  - [CLI Utils](https://github.com/rosen-bridge/utils/tree/dev/packages/cli) [`TS`?]
  - [Docker Deploy Guide](https://github.com/rosen-bridge/operation/blob/dev/docs/watcher/deploy-docker.md)

## 💼 Wallets <a id="wallets"></a>

> See also: [Wallets Overview on ErgoDocs](https://docs.ergoplatform.com/dev/wallets/)

- **[Nautilus Wallet](https://nautilus-wallet.io/)** – browser extension with dApp Connector *(Live)*. [GitHub](https://github.com/nautls/nautilus-wallet) [`JS/TS`] *(Active)*
- **[Satergo](https://satergo.com/)** – privacy-focused desktop wallet with full node *(Live)*. [GitHub](https://github.com/Satergo/Satergo) [`Java`] *(Active)*
- **[Ergo Mobile Wallet (Android)](https://play.google.com/store/apps/details?id=org.ergoplatform.android)** – official Android wallet *(Live)*. [GitHub](https://github.com/ergoplatform/ergo-wallet-app) [`Kotlin`] *(Active)*
- **[Ergo Mobile Wallet (iOS)](https://apps.apple.com/us/app/ergo-wallet-app/id1569044501)** – official iOS wallet *(Live)*. [GitHub](https://github.com/ergoplatform/ergo-wallet-app) [`Swift`] *(Active)*
- [Minotaur Wallet](https://minotaur-wallet.io/) – Android, iOS & Desktop wallet with multi-sig *(Live)*. [GitHub](https://github.com/minotaur-ergo/minotaur-wallet) [`JS/TS`] *(Active)*
  - [Multi-Sig Server](https://github.com/minotaur-ergo/Minotaur-Signing-Server) / [Alternative](https://github.com/lazypinkpatrick/cosigning-server)
- [SAFEW](https://chrome.google.com/webstore/detail/safew/lmjcdljhgidjbcpdkfknpfknbbkfpogg) – browser wallet with dApp Connector *(Live)*. [GitHub](https://github.com/ThierryM1212/SAFEW) [`JS/TS`] *(Active)*

### 🛟 Wallet Utilities & Recovery <a id="utilities--recovery"></a>

- **[Ergo Paper Wallet Generator](https://anon-br.github.io/ergo-paper-wallet/)** – generate paper wallets *(Live)*. [GitHub](https://github.com/anon-br/ergo-paper-wallet) [`JS/TS`]
- [Yoroi Wallet Recovery Tool](https://github.com/satsen/yoroi-ergo-wallet-recover) – recover funds from old Yoroi wallets. [`Java`]
- [Stealth Address Generator](https://ergomixer.github.io/stealth/) – web tool for stealth addresses.
- [Cold Wallet Setup Guide (Wiki)](https://github.com/ergoplatform/ergo-wallet-app/wiki/Cold-wallet) – guide for official mobile apps.
- [Ergo Poor Man's Wallet (EPMW)](https://github.com/epmw/epmw) – ultra-low-cost DIY hardware wallet. [`Hardware`]
- [Ergo Light Client (iOS Beta)](https://github.com/bjenkinsgit/ErgoIOSLiteClient) – community iOS light client. [`Swift`] *(Beta)*

---

## 📚 SDKs & Libraries <a id="sdks--libraries"></a>

> See also: [Libraries Overview on ErgoDocs](https://docs.ergoplatform.com/dev/libraries/)

### 🎯 Primary SDKs

- **[AppKit](https://github.com/ergoplatform/ergo-appkit)** – Java/Scala SDK for building Ergo apps. [`Java`, `Scala`] *(Active)*
- **[Fleet SDK](https://fleet-sdk.github.io/docs/)** – JS/TS SDK for web dApps. [GitHub](https://github.com/fleet-sdk) [`JS/TS`] *(Active)*
- **[Sigma-Rust](https://github.com/ergoplatform/sigma-rust/)** – core primitives & serialization in Rust. [`Rust`] *(Active)*

### 🔒 Core Libraries & Cryptography

- **[Sigmastate Interpreter](https://github.com/ScorexFoundation/sigmastate-interpreter)** – ErgoScript core interpreter & type system. [`Scala`, `ErgoScript`] *(Active)*
- [Scrypto](https://github.com/input-output-hk/scrypto/) – crypto primitives library. [`Scala`]
- [Scorex Util](https://github.com/ScorexFoundation/scorex-util) – utility classes for Scorex projects. [`Scala`]
- [Debox](https://github.com/ScorexFoundation/debox) – efficient primitive type Boxes. [`Scala`]
- [BouncyCastle JS](https://github.com/aslesarenko/bouncycastle-js) – BouncyCastle compiled for JS. [`JS`]
- [Scorex Crypto AVLTree](https://github.com/knizhnik/scorex_crypto_avltree) – Rust AVL Tree implementation. [Paper](https://github.com/knizhnik/scorex_crypto_avltree/blob/main/crypto_avltree.md) [`Rust`]
- [AVLIODB](https://github.com/ScorexFoundation/AVLIODB) – Authenticated dictionary implementation based on AVL+ trees (used in Ergo). [`Scala`]
- [Scorex ProofOfStake Example](https://github.com/ScorexFoundation/ProofOfStake) – example PoS implementation using Scorex. [`Scala`]
- [Scorex SimpleTransactions Example](https://github.com/ScorexFoundation/SimpleTransactions) – simple transaction example using Scorex. [`Scala`]

### 🔗 Language Bindings & Wrappers

- **[ErgoLib (sigma-rust)](https://github.com/ergoplatform/sigma-rust/tree/develop/ergo-lib)** – high-level Rust abstractions. [Docs](https://docs.rs/ergo-lib/) [`Rust`]
- **[ergo-lib-wasm](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-wasm)** – WASM bindings for JS/TS. [NPM (Browser)](https://www.npmjs.com/package/ergo-lib-wasm-browser) | [NPM (NodeJS)](https://www.npmjs.com/package/ergo-lib-wasm-nodejs) [`JS/TS`, `Rust`]
- [ergo-lib-jni](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-jni) – JNI bindings for JVM. [Docs](https://docs.rs/ergo-lib-jni/) [`Java`, `Rust`]
- **[ergo-lib-python](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-python)** – Python bindings (recommended). [PyPI](https://pypi.org/project/ergo-lib/) [`Python`, `Rust`] *(Active)*
- [ergo-lib-c](https://github.com/ergoplatform/sigma-rust/tree/develop/bindings/ergo-lib-c) – C bindings. [Docs](https://docs.rs/ergo-lib-c/) [`C`, `Rust`]
- [ergo-lib-go](https://github.com/sigmaspace-io/ergo-lib-go) – Go bindings (via C). [Docs](https://pkg.go.dev/github.com/ergoplatform/ergo-lib-go) [`Go`, `C`, `Rust`] *(Community)*
- [Ergo Wallet Core (JVM)](https://mvnrepository.com/artifact/org.ergoplatform/ergo-wallet) – wallet logic from reference node. [Source](https://github.com/ergoplatform/ergo/tree/master/ergo-wallet) [`Java`]

### 🤝 Community SDKs/Libraries <a id="community-sdkslibraries"></a>

- **[FleetSharp](https://github.com/pulsarz/FleetSharp)** – C# transaction builder inspired by Fleet. [`C#`]
  - [SigmaFi Plugin](https://github.com/pulsarz/FleetSharp.SigmaFi) | [Spectrum Plugin](https://github.com/pulsarz/FleetSharp.SpectrumFi) | [CoinGecko Plugin](https://github.com/pulsarz/FleetSharp.CoinGecko)
- [RustKit](https://github.com/rust-ergo/rustkit) – Community Rust SDK built on `sigma-rust`. [`Rust`]
- [Ergpy](https://github.com/mgpai22/ergpy) – Python wrapper using JPype (AppKit based, consider `ergo-lib-python`). [`Python`, `Java`]
- [ergo-golang](https://github.com/azhiganov/ergo-golang) – early-stage Go library. [`Go`]
- [sigma_rb](https://github.com/thedlop/sigma_rb) – Ruby bindings (via C). [`Ruby`, `C`, `Rust`]
- [sigma-rust-mini](https://github.com/aslesarenko/sigma-rust-mini) – minified sigma-rust for constrained environments. [`Rust`]
  - [No-Std Fork](https://github.com/Alesfatalis/sigma-rust-mini/tree/no_std) – focus on `no_std` compatibility.
- [ergo-python-appkit](https://github.com/ergo-pad/ergo-python-appkit) – alternative Python wrapper for AppKit (JPype). [`Python`, `Java`]
- [ogre](https://github.com/ross-weir/ogre) – TS node client library (Web/Deno/Native). [`JS/TS`]
- [ergo_client](https://github.com/ross-weir/ergo_client) – Rust library with HTTP clients for Ergo apps. [`Rust`]
- [sigma-builders](https://github.com/GuapSwap/sigma-builders) – protocol abstractions on AppKit for Scala dApps. [`Scala`]
- [eip12-types](https://github.com/capt-nemo429/eip12-types) – TS types for EIP-12 dApp Connector. [`TS`]
- [GetBlok Plasma](https://github.com/GetBlok-io/GetBlok-Plasma) – AppKit library for Plasma L2 AVL Trees. [`Scala`]
- [sigmajs-crypto-facade](https://github.com/anon-br/sigmajs-crypto-facade) – aims to replace BouncyCastle in SigmaJS. [`JS/TS`]
- [ScalaSigmaParticle](https://github.com/dzyphr/ScalaSigmaParticle) – Ergpy-based framework for cross-chain pipelines. [`Python`]
- [dApp Connector React Package (NightOwl)](https://github.com/nightowlcasino/dApp-connector-react-package) – React package for EIP-12. [`JS/TS`, `React`]
- [Ergo SDK JS (ErgoLabs)](https://github.com/ergolabs/ergo-sdk-js) – community JS SDK using Wasm bindings. [`JS/TS`, `Wasm`]
- [ergo-ts](https://github.com/coinbarn/ergo-ts) – TypeScript library (CoinBarn). [`TS`]

---

## 🛠️ Development Tooling <a id="development-tooling"></a>

> See also: [Developer Getting Started Guide on ErgoDocs](https://docs.ergoplatform.com/dev/get-started/)

### 📜 Smart Contracts & ErgoScript <a id="smart-contracts--ergoscript"></a>

- **[Sigmastate Interpreter](https://github.com/ScorexFoundation/sigmastate-interpreter)** – core interpreter & type system. [`Scala`, `ErgoScript`]
- **[escript.online](https://escript.online/)** – online editor & playground. [GitHub](https://github.com/SavonarolaLabs/escript-online) [`JS/TS`]
- **[Ergo Playgrounds](https://github.com/ergoplatform/ergo-playgrounds)** – Scala-based contract/off-chain testing. [`Scala`]
- [Ergoscript Compiler (Rust)](https://github.com/ergoplatform/sigma-rust/tree/develop/ergoscript-compiler) – Rust implementation. [`Rust`]
- [Ergoscript Compiler (Scala)](https://github.com/ergoplatform/ergoscript-compiler) – Scala CLI tool. [`Scala`]
- [ErgoScala Compiler](https://github.com/ergoplatform/ergoscala-compiler) – compile subset of Scala to ErgoScript. [`Scala`] *(Needs link update if available)*
- [ErgoScript CLI Compiler](https://github.com/ergoplatform/ergoscript-compiler) – CLI tool to compile ErgoScript to address. [`Scala`] *(Duplicate link? Check source)*
- [VSCode ErgoScript Language Support](https://marketplace.visualstudio.com/items?itemName=ergoscript.ergoscript-language-support) – syntax highlighting. [Source](https://github.com/GuapSwap/vscode-ergoscript-language-support)
- [FlowcardLib](https://github.com/lucagdangelo/flowcardLib) – library of contract templates. [`ErgoScript`]
- [FlowCards Framework](https://github.com/ergoplatform/ergo-jde/tree/main/flowcards) – declarative framework for dApps (part of JDE). [`JSON`, `Scala`]
- [ergo-script-re](https://github.com/ross-weir/ergo-script-re) – reverse engineering & analysis tools. [`Rust`]
- [ergo-castanet](https://github.com/iandebeer/ergo-castanet) – Dhall-based development tooling. [`Dhall`, `Scala`]
- [Plutomonkey](https://wallet.plutomonkey.com/) – web compiler (ErgoScript/Plutus).
- [Ergo Playground (Scastie)](https://scastie.scala-lang.org/ergoplatform) – online Scala/ErgoScript playground.
- [KioskWeb](https://github.com/scalahub/KioskWeb) – web interface for Kiosk framework. [`Scala`, `JS/TS`?]

### 🧱 Frameworks <a id="frameworks-dev"></a>

- **[Mosaik](https://github.com/MrStahlfelge/mosaik)** – framework for native-feel mobile dApp frontends *(Paused)*. [`Java`]
- [Kiosk](https://github.com/scalahub/Kiosk) – framework for secure dApps (Archived). [`Scala`]
- [Ergo JSON Development Environment (JDE)](https://github.com/ergoplatform/ergo-jde) – dApp framework using JSON config. [`JSON`, `Scala`]
- [Edge](https://github.com/Ergo-Lend/edge) – Ergo Development Generics Elements (by ErgoLend). [`Scala`]
- [Mosaik Web Executor](https://github.com/MrStahlfelge/mosaik-kt-js) – browser executor for Mosaik. [`Kotlin`, `JS`]
- [Headless dApp Framework](https://github.com/ergoplatform/ergo-headless-dapp-framework) – Rust framework for portable off-chain logic (EIP-6). [`Rust`]
- [Terahertz Starter](https://github.com/nn-dmt/terahertz-starter) – Framework/template for building dApps. [`JS/TS`?]

### 📄 Templates <a id="templates"></a>

- [ergo-scala-skeleton-app](https://github.com/dav009/ergo-scala-skeleton-app) – Scala skeleton template. [`Scala`]
- [ergo-web-template](https://github.com/SavonarolaLabs/ergo-web-template) – JS/TS web template. [`JS/TS`]
- [ergo-js-template](https://github.com/anon-real/ergo-js-template) – basic JS template. [`JS/TS`]
- [Ergo Off-Chain Bot Template](https://github.com/mgpai22/Ergo-OffChain-Bot-Template) – Scala off-chain bot template. [`Scala`]
- [scala-play-next-ergo](https://github.com/kii-dot/scala-play-next-ergo) – Scala Play, Appkit, NextJs template. [`Scala`, `JS/TS`]
- [ergo-play-boilerplate](https://github.com/kii-dot/ergo-play-boilerplate) – Scala Play boilerplate. [`Scala`]
- [ergo-basic-template](https://github.com/ERGnomes/ergo-basic-template) – basic React template. [`JS/TS`, `React`]

### 🔧 Utilities <a id="utilities"></a>

- [Ergo Utils (JS)](https://github.com/anon-real/ErgoUtils) – utility library in JS/TS. [`JS/TS`]
- [TokenJay](https://tokenjay.app/) – mobile-friendly token minting/management tool. *(Live)*
- [Yet Another Airdrop Tool (YAAT)](https://github.com/FlyingPig69/YAAT/) – Python batch transfer/airdrop tool. [`Python`]
- [Ergo Node Interface (Rust)](https://github.com/ergoplatform/ergo-node-interface-rust) – Rust interface for node API. [`Rust`]
- [ergo-assembler](https://github.com/anon-real/ergo-assembler) – off-chain transaction assembly service. [`Scala`]
- [Transaction Builder UI](https://thierrym1212.github.io/txbuilder/) – web UI for manipulating/signing TX JSON. [GitHub](https://github.com/ThierryM1212/transaction-builder/) [`JS/TS`]
- [ErgoSimpleAddresses](https://github.com/kushti/ergo-simple-addresses) – Java address utilities. [`Java`]
- [ErgoUtilsUploadService](https://github.com/arobsn/ErgoUtilsUploadService) – backend for ErgoUtils NFT uploads. [`C#`]
- [Ergo Vanity Address Generator](https://github.com/jellymlg/ergo-vanitygen) – generate custom addresses. [`Scala`]
- [Ergo Monitoring](https://github.com/SabaunT/ergo-monitoring) – debug service for node/blockchain state. [`Rust`]
- [Ergo Faucet](https://github.com/zargarzadehm/ergo-faucet) – simple faucet implementation. [`Scala`]
- [Chain Name Service (Experimental)](https://github.com/ross-weir/chain-name-service) – experimental name service. [`Scala`]
- [Transaction Group Framework](https://github.com/GetBlok-io/Subpooling#frameworks--abstractions) – manage large interrelated TXs (from GetBlok).
- [Ergo Utilities (Rust)](https://github.com/ergoplatform/ergo-utilities-rust) – utility library for Rust off-chain code. [`Rust`] *(Official)*
- [Token Reward Dispenser](https://github.com/FlyingPig69/TokenRewardDispenser) – utility for distributing token rewards. [`Python`]
- [Ergo Setup](https://github.com/abchrisxyz/ergo-setup) – Docker setup (Node, Explorer, GraphQL). [`Docker`]
- [Ergo Handshake (Reference)](https://github.com/SabaunT/ergo-handshake) – reference P2P handshake implementation. [`Rust`]
- [MobilERG](https://github.com/ladopixel/mobilERG) – interact via phone calls/SMS. [`Python`]
- [tERGminal](https://github.com/ladopixel/tERGminal) – interact from the terminal. [`Python`]
- [On-Chain Notifications Service](https://github.com/ergopad/onchain-notifications-service) – TX monitoring/event tracking service. [`Scala`]
- [Ergo-node-TUI-installer](https://github.com/Itaggergaard/Ergo-node-TUI-installer) – TUI installer for nodes. [`Shell`]
- [Ergo Synced Node Helper](https://github.com/mgpai22/ergo-synced-node) – helper scripts for synced nodes. [`Python`, `Shell`]
- [Ergo Portable Node](https://github.com/ross-weir/ergo-portable) – scripts for portable node setup. [`Shell`]
- [Ergo Nix Toolkit](https://github.com/ergoplatform/ergo-nix) – Nix toolkit for Ergo packages. [`Nix`]
- [Ergo Bootstrap](https://github.com/ergoplatform/ergo-bootstrap) – Nix-based cluster deployment tool. [`Nix`, `Shell`]
- [Ergo RPI Scripts](https://github.com/Eeysirhc/ergo-rpi) – scripts/guide for RPi node setup. [`Shell`?]
- [ErgoScripts (Misc)](https://github.com/glasgowm148/ergoscripts) – misc community scripts (e.g., nginx config). [`Shell`, `Other`]
- [ErgoNodeAndroid (Termux)](https://github.com/rustinmyeye/ErgoNodeAndroid) – one-click Android node setup app. [`Shell`, `Android`]
- [ErgoTool](https://github.com/aslesarenko/ergo-tool) – CLI for blockchain interaction via AppKit. [`Scala`]
- [ErgoSphere](https://github.com/jellymlg/ErgoSphere) – Collection of tools/utilities. [`Scala`?]
- [Ergo Meta](https://github.com/nautls/ergo-meta) – Metadata service for Nautilus wallet. [`JS/TS`]

### ⌨️ CLI Tools <a id="cli-tools"></a>

- [Yet Another Airdrop Tool (YAAT)](https://github.com/FlyingPig69/YAAT/) – Python batch transfer/airdrop tool. [`Python`]
- [Ergo Vanity Address Generator](https://github.com/jellymlg/ergo-vanitygen) – generate custom addresses. [`Scala`]
- [MobilERG](https://github.com/ladopixel/mobilERG) – interact via phone calls/SMS. [`Python`]
- [tERGminal](https://github.com/ladopixel/tERGminal) – interact from the terminal. [`Python`]
- [Ergo-node-TUI-installer](https://github.com/Itaggergaard/Ergo-node-TUI-installer) – TUI installer for nodes. [`Shell`]
- [Ergo Synced Node Helper](https://github.com/mgpai22/ergo-synced-node) – helper scripts for synced nodes. [`Python`, `Shell`]
- [Ergo Portable Node](https://github.com/ross-weir/ergo-portable) – scripts for portable node setup. [`Shell`]
- [Ergo Nix Toolkit](https://github.com/ergoplatform/ergo-nix) – Nix toolkit for Ergo packages. [`Nix`]
- [Ergo Bootstrap](https://github.com/ergoplatform/ergo-bootstrap) – Nix-based cluster deployment tool. [`Nix`, `Shell`]
- [Ergo RPI Scripts](https://github.com/Eeysirhc/ergo-rpi) – scripts/guide for RPi node setup. [`Shell`?]
- [ErgoScripts (Misc)](https://github.com/glasgowm148/ergoscripts) – misc community scripts (e.g., nginx config). [`Shell`, `Other`]
- [ErgoNodeAndroid (Termux)](https://github.com/rustinmyeye/ErgoNodeAndroid) – one-click Android node setup app. [`Shell`, `Android`]

### 🔌 Node Interaction & APIs <a id="node-interaction--apis"></a>

- **[Danaides](https://github.com/ergopad/danaides)** – high-performance blockchain toolkit/indexer. [`Python`]
- **[Ergo Node API Swagger UI](http://127.0.0.1:9053/swagger)** – interactive API docs (local node). [OpenAPI Spec](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/api/openapi.yaml)
- [Ergo GraphQL](https://github.com/capt-nemo429/ergo-graphql) – GraphQL interface for blockchain data. [`JS/TS`]
- [Rosetta API for Ergo](https://github.com/ross-weir/rosetta-ergo) – Rosetta standard implementation. [`Go`]
- [Ergo Scanner](https://github.com/ergoplatform/scanner) – framework for scanning chain events. [`Scala`]
- [ergo-indexer-rust](https://github.com/darkdrag00nv2/ergo-indexer-rust) – blockchain indexer in Rust. [`Rust`]
- [Strainer](https://github.com/dav009/strainer) – listen and pipe TXs/eUTXOs from node. [`Rust`]
- [ergo-node-zmqpub](https://github.com/cruxfinance/ergo-node-zmqpub) – publish node events via ZeroMQ. [`Scala`]
- [Pragmaxim Chain Indexer (Ergo)](https://github.com/pragmaxim-com/chain-indexer/tree/ergo-boxes) – custom indexer implementation. [`Scala`]
- [Ergonnection](https://github.com/Satergo/Ergonnection) – P2P networking library. [`Java`]
- [General API Docs](https://api.ergoplatform.com/api/v1/docs/) – overview of Node/Explorer APIs.
  - [Node API Specification (OpenAPI)](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/api/openapi.yaml)
  - [Explorer API v1 Specification (OpenAPI)](https://github.com/ergoplatform/explorer-backend/blob/master/modules/explorer-api/src/main/resources/openapi.yaml)
- [Ergonode Spyder](https://github.com/chriswill/ergonode-spyder) – network spider for node analytics. [`C#`]
- [Ergo Blockchain Scanner (Aragogi)](https://github.com/aragogi/scanner) – alternative scanner implementation. [`Scala`]

### 🧪 Testing & Debugging <a id="testing--debugging"></a>

- **[Contract Testing Framework](https://github.com/anon-real/contract-testing)** – off-chain ErgoScript contract testing. [`Scala`]
- [Ergoscript Simulator](https://github.com/spectrum-finance/ergoscript-simulator) – community tool for simulating ErgoScript. [`Scala`?]
- [Ergo Puppet](https://github.com/dav009/ergo-puppet) – off-chain experimentation/unit testing tool. [`Scala`]
- [Ergo Test Vectors](https://github.com/ergoplatform/ergo-test-vectors) – standard test vectors for crypto/serialization.

### 💳 Payments <a id="payments"></a>

- [ErgoPay (EIP-20)](https://github.com/ergoplatform/eips/blob/master/eip-0020.md) – URI scheme for wallet-dApp interaction (non-web). [Docs](https://docs.ergoplatform.com/dev/stack/ergo-pay/)
- [dApp Connector (EIP-12)](https://github.com/ergoplatform/eips/pull/23/files) – interface for web wallet-dApp interaction. [Docs](https://docs.ergoplatform.com/dev/stack/dApp-connector/)
- [Proxy Contracts (EIP-17)](https://github.com/ergoplatform/eips/blob/master/eip-0017.md) – standard for secure dApp interaction. [Docs](https://docs.ergoplatform.com/dev/stack/proxy-contracts/)

### ✨ Examples & Snippets <a id="examples--snippets"></a>

- **[ErgoScript by Example](https://github.com/ergoplatform/ergoscript-by-example)** – simple contracts demonstrating features. [`ErgoScript`]
- **[AppKit Examples](https://github.com/aslesarenko/ergo-appkit-examples)** – multi-language AppKit usage examples. [`Java`, `Scala`, `JS`, `Python`, `Ruby`, `C`]
- **[Fleet Examples](https://github.com/fleet-sdk/fleet-by-example)** – repository showcasing Fleet SDK usage. [`TS`]
- [Ergo Contracts](https://github.com/ergoplatform/ergo-contracts) – early contract examples with verification. [`Scala`]
- [SigmaState Interpreter Examples](https://github.com/ScorexFoundation/sigmastate-interpreter/tree/develop/sc/src/test/scala/sigmastate/utxo/examples) – examples within interpreter tests. [`Scala`]
- [Kiosk Offchain Examples](https://github.com/scalahub/Kiosk/tree/master/src/test/scala/kiosk/offchain) – examples using Kiosk off-chain assembler. [`JSON`]
- [Headless dApp Framework Tutorials](https://github.com/ergoplatform/ergo-headless-dapp-framework/tree/main/tutorials) – Math Bounty dApp tutorial. [`Rust`]
- [Mosaik Examples](https://github.com/MrStahlfelge?tab=repositories&q=mosaik&type=source) – various Mosaik UI framework examples. [`Kotlin`, `Java`]
- [Atomic Swap Example (secp256k1)](https://github.com/dzyphr/atomicswapexample) – 2-party atomic swap example. [`Scala`?]
- [ErgoRaffle Bot (JS)](https://github.com/zkastn/ergo-raffle-bot) – JS bot interacting with ErgoRaffle. [`JS`]
- [Quid Games (ErgoHack)](https://github.com/hypo10use/quid-games) – gaming example from ErgoHack. [`Angular`, `TS`]
- [NFT Minting for Dummies](https://github.com/lucagdangelo/minting-for-dummies) – basic NFT minting script. [`Scala`]
- [Profit Sharing dApp](https://github.com/mhssamadani/ErgoProfitSharingDapp) – example profit sharing contract. [`Scala`?]
- [Trade-In Protocol](https://github.com/lucagdangelo/trade-in) – example token burning/trading protocol. [`Scala`, `JS/TS`]
- [SigmaFi UI Plugins](https://github.com/capt-nemo429/sigmafi-ui/blob/main/src/offchain/plugins.ts) – example off-chain logic for SigmaFi. [`TS`]
- [Ergo Payroll (ErgoHack)](https://github.com/andrehafner/ergo-payroll) – payroll project from ErgoHack.
- [LETS Backend (ErgoHack)](https://github.com/arkan294/LETS-backend) – LETS backend from ErgoHack.
- [Inergitance (ErgoHack)](https://github.com/inergitance) – inheritance dApp PoC from ErgoHack.
- [dAppStep Play (ErgoPay Example)](https://github.com/nirvanush/dappstep-play) – example backend using ErgoPay. [`TS`]
- [Ergo Android](https://github.com/aslesarenko/ergo-android) – example Android app demonstrating AppKit. [`Java`, `Kotlin`]
- [Node Wallet Address Generation Demo (Java)](https://github.com/ergoplatform/ergo/blob/master/ergo-wallet/src/test/java/org/ergoplatform/wallet/AddressGenerationDemo.java) – example using node's wallet logic. [`Java`]
- [Node Wallet Create Transaction Demo (Java)](https://github.com/ergoplatform/ergo/blob/master/ergo-wallet/src/test/java/org/ergoplatform/wallet/CreateTransactionDemo.java) – example using node's wallet logic. [`Java`]
- [Ergo Asset Locker Demo](https://github.com/mowreez/ergo-asset-locker) – demo dApp locking assets. [`JS/TS`]
- [Ergo Audit Backend Demo](https://github.com/jlsachse/ergo-audit-backend) – demo backend for auditing. [`Java`]
- [SchedulERG Demo](https://github.com/ladopixel/schedulERG) – demo using encrypted descriptions. [`Python`]
- [Ergo Offchain Demo](https://github.com/MrStahlfelge/ergo-offchain) – examples of off-chain interactions. [`Kotlin`]
- [Fleet SDK Send NFT Demo](https://github.com/ladopixel/fleet-sdk-sendnft) – demo sending NFTs with Fleet. [`JS/TS`]
- [Fleet SDK Create Token Demo](https://github.com/ladopixel/fleet-sdk-createtoken) – demo creating tokens with Fleet. [`JS/TS`]
- [Fleet SDK Burn Tokens Demo](https://github.com/ladopixel/fleet-sdk-burntokens) – demo burning tokens with Fleet. [`JS/TS`]
- [MultiSig Input Demo (WASM)](https://github.com/SavonarolaLabs/multisig-input) – example tests for multisig with ergo-lib-wasm. [`JS`]
- [Fleet Chained Token Sender](https://github.com/mgpai22/fleet-ergo-chained-token-sender) – demo sending tokens in chained TXs. [`JS/TS`]
- [AppKit by Example (ApexTheory)](https://github.com/ApexTheory/appkit-by-example) – example usage of AppKit. [`Scala`]
- [Go Ergo Example](https://github.com/ross-weir/go-ergo-example) – example using Go with C bindings. [`Go`, `C`]
- [Ergo Stealth Address Example](https://github.com/ross-weir/ergo-stealth-address-example) – example stealth address implementation. [`JS/TS`]
- [Ergo Playground Scenarios](https://github.com/jaysee260/ergo-playground) – collection of miscellaneous scenarios. [`Scala`?]
- [ErgoPay Server Example](https://github.com/MrStahlfelge/ergopay-server-example) – example ErgoPay backend. [`Java`, `Spring`]
- [Ergo Android Example App](https://github.com/aslesarenko/ergo-android) – example Android app using AppKit. [`Java`, `Kotlin`]
- [Mosaik AgeUSD Demo](https://github.com/MrStahlfelge/mosaik-ageusddemo) – Mosaik UI example for AgeUSD. [`Kotlin`?]
- [Mosaik Tutorial Series App](https://github.com/MrStahlfelge/mosaik-tutorial-series) – example app for Mosaik tutorial. [`Kotlin`]
- [Mosaik Token Burn Demo](https://github.com/MrStahlfelge/mosaik-demo-tokenburn) – Mosaik demo UI for burning tokens. [`Kotlin`]
- [Mosaik NFT Marketplace Example](https://github.com/MrStahlfelge/mosaiknftmarketplace) – example Mosaik UI for NFT marketplace. [`Kotlin`?]
- [ErgoPay Frontend Example](https://github.com/MrStahlfelge/ergopay-frontend-example) – example ErgoPay frontend UI. [`JS/TS`?]
- [Scalahub AgeUSD Example](https://github.com/scalahub/AgeUSD) – Example implementation of AgeUSD protocol. [`Scala`]
- [Scalahub Oracle Pool Example](https://github.com/scalahub/OraclePool) – Example implementation of Oracle Pools V1. [`Scala`]

---

## 💸 DeFi & dApps <a id="defi--dapps"></a>

> See also: [Ecosystem Overview on ErgoDocs](https://docs.ergoplatform.com/uses/use-cases-overview/)

### 💹 DEXs & Swaps <a id="dexs--swaps"></a>

- **[Spectrum Finance](https://spectrum.fi/)** – cross-chain DEX (AMM & Order Book) *(Live)*. [Contracts](https://github.com/spectrum-finance/ergo-dex/tree/master/contracts) | [Backend](https://github.com/spectrum-finance/spectrum-offchain-ergo) *(Active)*
- [DexyGold](https://dexygold.com/) – decentralized exchange *(Live)*. [Telegram](https://t.me/dexygold) | [Contracts/Spec](https://github.com/ergoplatform/ergo-jde/tree/main/kiosk/src/test/scala/kiosk/dexy) *(Active)*
- [GuapSwap](https://github.com/GuapSwap) – decentralized profit swapping for miners *(Live)*. [Contracts](https://github.com/GuapSwap/guapswap-ronin/tree/main/src/main/scala/contracts) *(Active)*
- [Single Transaction Swap](https://www.single-tx-swap.com/) – UI for single TX atomic swaps *(Live)*. [GitHub](https://github.com/danieloravec/ergo-token-swap) *(Active)*
- [Arbit](https://github.com/ConnecMent/arbit) – simple arbitrage platform. [`JS`] *(Active?)*
- [Analog Ergo](https://github.com/dzyphr/ScalaSigmaParticle) – P2P atomic swap protocol. [Contract](https://github.com/dzyphr/ScalaSigmaParticle/blob/main/ScalarLock/src/main/scala/ScalarLock.scala) | [UI PoC](https://github.com/dzyphr/AtomicAnalogSwapWebsite)
- [Mew Finance](https://mewfinance.com/) – DEX, NFT marketplace, and DeFi suite *(Live)*. [Docs](mew-finance.md) | [Telegram](https://t.me/MewFinance) *(Active)*

### 🏦 Stablecoins & Lending <a id="stablecoins--lending"></a>

- **[SigmaUSD](https://sigmausd.io/)** – algorithmic stablecoin (AgeUSD) *(Live)*. [EIP-15](https://github.com/ergoplatform/eips/blob/master/eip-0015.md) | [Bot](https://github.com/anon-real/sigma-usd) | [Spec](https://github.com/Emurgo/age-usd) | [Telegram](https://t.me/SigmaUSD) *(Active)*
- [Duckpools](https://duckpools.io/) – lending platform *(Live)*. [GitHub Org](https://github.com/duckpools) | [Contracts](https://github.com/duckpools/lend-protocol-contracts/tree/main/contracts) | [Option Pools](https://github.com/duckpools/off-chain-bot/tree/optionPools/optionPools) | [Telegram](https://t.me/duckpools_chat) *(Active)*
- [EXLE (ErgoLend)](https://ergolend.org/) – lending platform *(Live)*. [Contracts/Edge Lib](https://github.com/Ergo-Lend/edge) | [Telegram](https://t.me/ErgoLend) *(Active)*
- [SigmaFi](https://sigmafi.org/) – DeFi yield strategies *(Live)*. [UI](https://github.com/capt-nemo429/sigmafi-ui) | [Contracts](https://github.com/K-Singh/Sigma-Finance) | [Telegram](https://t.me/sigmafi) *(Active)*
- [Phoenix Finance](https://github.com/PhoenixErgo/phoenix-hodlcoin-contracts) – Hodlcoin DeFi platform *(Live)*. *(Active)*
- [Hodlcoin Contracts](https://github.com/lucagdangelo/hodlcoin-contracts) – contracts for Hodlcoin concept. *(Active)*
- [Gluon](https://github.com/DjedAlliance) – cross-chain stablecoin infrastructure (Djed based). [Twitter](https://twitter.com/DjedAlliance) *(In Development)*

### 🚀 Launchpads <a id="launchpads"></a>

- [ErgoPad](https://ergopad.io/) – IDO launchpad platform *(Live)*. [GitHub Org](https://github.com/ergo-pad) | [Telegram](https://t.me/ergopad_chat) *(Active)*

### 🆔 Identity & DNS <a id="identity--dns"></a>

- [ErgoNames](https://ergonames.com/) – decentralized domain name service *(Live)*. [API Repo](https://github.com/ergonames/ErgoNames.Api) *(Active)*
- [Ergo Reputation System](https://reputation-systems.github.io/) – on-chain reputation system *(Beta)*. [GitHub Org](https://github.com/sigma-rps) | [Library](https://github.com/reputation-systems/reputation-system-lib) | [Forum](https://www.ergoforum.org/t/reputation-system/4782) *(Active)*
- [ErgoDNS Frontend (ErgoHack)](https://github.com/jaythiya/ergodns-frontend) – Frontend concept for Ergo domain names. [`JS/TS`] *(Inactive/Concept)*

### 🤫 Privacy <a id="privacy"></a>

- **[ErgoMixer](https://ergomixer.com/)** – non-custodial, non-interactive mixer *(Live)*. [GitHub Org](https://github.com/ergoMixer/) | [Backend](https://github.com/ergoMixer/ergoMixBack) | [Releases](https://github.com/ergoMixer/ergoMixBack/releases) *(Active)*
- [Sigmajoin](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/mixer/doc/main.pdf) – CoinJoin protocol spec using Sigma protocols. [Tests](https://github.com/ergoplatform/ergo-jde/tree/main/kiosk/src/test/scala/kiosk/mixer) *(Concept/Spec)*

### 🎮 Gaming & Metaverse <a id="gaming--metaverse"></a>

- [BlitzTCG](https://blitz-tcg.com/) – Trading Card Game *(Beta)*. *(Active)*
- [CyberVerse](https://cyberverseteam.itch.io/cyberverse) – Metaverse/Gaming project *(Live)*. [Telegram](https://t.me/CyberVersegame) *(Active)*
- [NightOwl Casino](https://nightowlcasino.io/) – decentralized casino *(Live)*. [GitHub Org](https://github.com/nightowlcasino) | [Telegram](https://t.me/nightowlcasino) *(Active)*
- [Comet Community](https://github.com/Koutelier/CometCommunity) – community project with various dApps. [Website](https://github.com/Koutelier/CometGag-Webiste) *(Active?)*
- [ObolFlip](https://github.com/ObolFlip) – decentralized CoinFlip betting example. [Client](https://github.com/ObolFlip/obolflip-client)
- [Comet Lottery](https://github.com/mgpai22/comet-lottery) – lottery dApp contracts & bot. [`Scala`] *(Active?)*

### 🏛️ DAO Frameworks <a id="dao-frameworks"></a>

- **[Paideia](https://paideia.im/)** – DAO management platform *(Beta)*. [Contracts](https://github.com/paideiadao/paideia-contracts) | [Telegram](https://t.me/paideiaDAO) *(Active)*
- [Ergo Team](https://github.com/anon-real/ergo-team) – simple DAO/team treasury example. [`ErgoScript`]

### 🧩 Other dApps & Services <a id="other-dapps--services"></a>

- [CruxFinance](https://github.com/cruxfinance) – cross-chain liquidity solutions *(Live)*. [`Scala`, `Rust`, `JS/TS`] *(Active)*
- [Machina Finance](https://github.com/nautls/machina-finance) – off-chain execution bot platform (Ergomatic). [`JS/TS`] *(Active)*
- [Hodlbox](https://hodlbox.xyz/) – time-locked token boxes *(Live)*. [GitHub](https://github.com/SavonarolaLabs/hodlbox-xyz) | [Contracts](https://github.com/SavonarolaLabs/hodlbox-xyz/tree/main/src/lib/contract) *(Active)*
- [SigmaO](https://sigmao.cc/) – options trading platform *(Beta)*. [GitHub](https://github.com/ThierryM1212/sigmao) | [Telegram](https://t.me/SigmaOpts) *(Active)*
- [Netnotes](https://github.com/networkspore/Netnotes-Linux/releases) – secure P2P messaging/notes *(Beta)*. [`Java`] *(Active)*
- [TabbyPOS](https://tabbypos.com/) – Point-of-Sale system *(Live)*. [GitHub](https://github.com/Kolmen-Tech/ErgoPOS) | [Telegram](https://t.me/tabbypos) *(Active)*
- [Benefaction Platform](https://github.com/StabilityNexus/BenefactionPlatform-Ergo) – charity/donation platform prototype. *(Development)*
- [Moria Finance](https://github.com/Moria-Finance) – ERG derivatives project. *(Development)*
- [ChainCash](https://github.com/ChainCashLabs) – decentralized monetary system. [Whitepaper](https://github.com/kushti/chaincash/blob/master/paper/chaincash.pdf) | [Server](https://github.com/ChainCashLabs/chaincash-rs) | [Contracts](https://github.com/ChainCashLabs/chaincash/tree/master/contracts) *(Active)*
- [Sigma Subscriptions](https://github.com/cornbelt-dev/sigma-subscriptions) – subscription service framework. [Manager UI](https://github.com/cornbelt-dev/sigma-subscriptions-manager) *(Paused?)*
- [ErgoWell](https://github.com/mhssamadani/ErgoWell) – crowdfunding/investment platform concept. [`JS/TS`] *(Inactive/Concept)*
- [Lithos Protocol](https://lithosprotocol.org/) – DeFi protocol for ERG liquidity. [GitHub Org](https://github.com/Lithos-Protocol) | [LitePaper](https://github.com/Lithos-Protocol/LitePaper) *(Active)*
- [Off The Grid](https://github.com/Telefragged/off-the-grid) – decentralized grid trading bot. [`Rust`]
- [Sigmarand](https://github.com/noob77777/ergo-randgen) – commit-reveal RNG scheme. [`Scala`]
- [Community Liquidity Bootstrap](https://github.com/AcoSmrkas/community-liquidity-bootstrap) – platform from ErgoHack VII. [`JS/TS`?]
- [Perma Ergo](https://github.com/firashebili/permergo-microfinancing-dao) – RealFi micro-finance project (ErgoHack VI).
- [DumDumDum](https://github.com/kii-dot/dumdumdum) – on-chain Twitter alternative (ErgoHack V). [`Scala`?]
- [Ergo Index](https://github.com/ergo-index) – decentralized indexing service (ErgoHack VII). [Backend](https://github.com/ergo-index/ergo-index-backend) | [Python Backend](https://github.com/ergo-index/ergo-index-backend-python) | [Contracts](https://github.com/ergo-index/ergo-index-contracts) | [Frontend](https://github.com/ergo-index/ergo-index-frontend) *(Development)*
- [SigmaStamp](https://sigmastamp.com/) – document timestamping service (ErgoHack VII). [GitHub Org](https://github.com/sigmastamp) | [Docs](https://github.com/sigmastamp/docs) | [Frontend](https://github.com/sigmastamp/sigmastamp-frontend) *(Development)*
- [ErgoHack Dashboard Project](https://github.com/Ergohack-Dashboard-Project) – Dashboard concept from Ergohack. *(Inactive/Concept)*

---

## 🖼️ NFT Ecosystem <a id="nft-ecosystem"></a>

> See also: [NFTs Overview on ErgoDocs](https://docs.ergoplatform.com/uses/nft/)

### 🛒 Marketplaces & Auctions <a id="marketplaces--auctions"></a>

- **[SkyHarbor](https://skyharbor.io/)** – NFT marketplace *(Live)*. [Contracts](https://github.com/skyharbor-market/contracts) *(Active)*
- [AuctionHouse](https://ergoauctions.org/) – EIP-22 auction platform *(Live)*. [GitHub](https://github.com/anon-real/ErgoAuctionHouse) | [EIP-22](https://github.com/ergoplatform/eips/blob/master/eip-0022.md) | [Telegram](https://t.me/ergoauctionhouse) *(Active)*

### 🎨 Minting & Utilities <a id="minting--utilities"></a>

- **[Lilium](https://lilium.digital/)** – NFT tools, minting & services *(Live)*. [GitHub Org](https://github.com/LiliumErgo) | [Contracts](https://github.com/LiliumErgo/scala-api/blob/main/app/contracts/LiliumContracts.scala) [`Scala`, `JS/TS`, `Python`] *(Active)*
- [ErgoRaffle](https://ergoraffle.com/) – decentralized raffle platform *(Live)*. [GitHub](https://github.com/ErgoRaffle) | [Contracts](https://github.com/ErgoRaffle/raffle-backend/blob/master/app/raffle/RaffleContract.scala) *(Active)*
- [Ergo NFT Bulk Minter](https://github.com/mgpai22/ergo-nft-bulk-minter) – Python bulk minting script (with royalties). [`Python`]
- [Ergo Token Minter](https://thierrym1212.github.io/tokenminter/) – web UI for minting tokens/NFTs. [GitHub](https://github.com/ThierryM1212/ergo-token-minter) [`JS/TS`]
- [CYTI](https://thierrym1212.github.io/cyti/) – Choose Your Token ID (mineable minting contract). [GitHub](https://github.com/ThierryM1212/cyti) [`JS/TS`]
- [Sigma Mint](https://github.com/thedlop/sigma_mint) – Ruby NFT minting library (ErgoHack IV). [`Ruby`]

### 🗿 NFT Projects <a id="nft-projects"></a>

- [ErgoSapiens](https://ergosapiens.com/) – NFT collection & community project *(Live)*. [GitHub](https://github.com/mgpai22/ergosapiens) | [Payment Portal](https://github.com/mgpai22/ergosapiens-payment-portal) *(Active)*
- [Auction Coin](https://auctioncoin.app/) – auction platform using NFTs *(Live)*. [GitHub Org](https://github.com/orgs/Auction-Coin/repositories) | [Contracts](https://github.com/Auction-Coin/contracts) *(Active)*
- [Blobstopia](https://github.com/ThierryM1212/blobs-topia/) – completed generative NFT project/game. [Release](https://github.com/ThierryM1212/blobs-topia/releases/tag/v1.1.0) *(Done)*

---

## ⛏️ Mining <a id="mining"></a>

> See also: [Mining Overview on ErgoDocs](https://docs.ergoplatform.com/mining/mining-overview/)

### 🏊 Pools <a id="pools"></a>

- **[Sigmanauts Mining Pool](https://sigmanauts.com/mining/)** – community mining pool.
- [MiningCore](https://github.com/oliverw/miningcore) – open-source pool software. [Config Wiki](https://github.com/oliverw/miningcore/wiki/Configuration)
- [NOMP (ergo-nomp)](https://github.com/btclinux/ergo-nomp) – Node Open Mining Portal adapted for Ergo.
- [Node Stratum Pool](https://github.com/vorujack/node-stratum-pool) – Node.js stratum pool server. [`JS`]
- [ergo-mining-pool (MGpai)](https://github.com/mgpai22/ergo-mining-pool) – open source mining pool. [`Go`?]
- [Ergopool.io Software](https://github.com/ergopool-io) – components for running an Ergo mining pool (Accounting, API, Frontend, Proxy). [`Go`, `JS/TS`]

### 💻 Software <a id="software"></a>

- **[Autolykos2 Nvidia Miner](https://github.com/mhssamadani/Autolykos2_NV_Miner)** – open-source Nvidia GPU miner.
- **[Autolykos2 AMD Miner](https://github.com/mhssamadani/Autolykos2_AMD_Miner)** – open-source AMD GPU miner.
- [Autolykos2 CPU Miner](https://github.com/mhssamadani/Autolykos2-CPUMiner) – open-source CPU miner.
- [Autolykos GPU Miner (v1)](https://github.com/ergoplatform/Autolykos-GPU-miner) – original open-source GPU miner (Autolykos v1).
- [Ergo AMD Miner (v1)](https://github.com/mhssamadani/ergoAMDminer) – open-source AMD miner (Autolykos v1).
- *Note: Several closed-source miners exist (lolMiner, Nanominer, SRBMiner, NBMiner, TeamRedMiner, T-Rex), see [Mining Software Comparison](software.md) for links and fee info.*

### 🔧 Utilities & Tooling <a id="utilities--tooling"></a>

- [ErgoStratumServer](https://github.com/mhssamadani/ErgoStratumServer) – Stratum server implementation. [`Scala`] | [Reqlez Fork](https://github.com/reqlez/ErgoStratumServer)
- [ErgoStratumProxy](https://github.com/mhssamadani/ErgoStratumProxy) – Stratum proxy for open-source miners. [`Scala`]
- [Stratum4Ergo](https://github.com/Satergo/stratum4ergo) – Java library for Stratum servers. [`Java`]
- [Ergo Profit Calculator](https://babygrenade.github.io/ergo-profit-calc/) – web-based profitability calculator.
- [ErgoTools (Mining Rewards)](https://github.com/lorien/ergotools) – CLI tool to find/withdraw miner rewards.
- [Miner Rewarder](https://github.com/mgpai22/miner-rewarder) – bot to reward miners. [`JS/TS`]
- [Miner Reward Consolidator](https://github.com/mgpai22/ergo-miner-reward-consolidator) – tool to consolidate rewards. [`JS/TS`?]
- [Miner Rights Protocol](https://github.com/The-Last-Byte-Bar/Miner-Rights-Protocol) – concept for rights-based token distribution.
  - [Token Flight](https://github.com/The-Last-Byte-Bar/Token-Flight) – related implementation.
  - [Token Flight Bot](https://github.com/The-Last-Byte-Bar/Token-Flight-Bot) – bot for Token Flight.
- [Sigmanaut Mining Pool UI](https://github.com/marctheshark3/sigmanaut-mining-pool-ui) – community UI for Sigmanauts pool. [`JS/TS`]
- [Ergo CYTI Miner](https://github.com/Telefragged/ergo-cyti-miner) – miner for CYTI NFT minting contract. [`Rust`]

### 🧠 Smart Pooling <a id="smart-pooling"></a>

- [ErgoSmartPools](https://github.com/WilfordGrimley/ErgoSmartPools) – decentralized mining pool using smart contracts.
- [GetBlok Subpooling Contracts](https://github.com/GetBlok-io/ergo-smartpooling-contracts) – contracts for GetBlok's subpooling. [`Scala`]
- [GetBlok Subpooling Plasma Configs](https://github.com/GetBlok-io/Subpooling/tree/mainnet_plasma/conf/scripts) – scripts for GetBlok's Plasma subpooling.

### 🔐 Hardware Wallet Support <a id="hardware-wallet-support"></a>

- **[Ledger App for Ergo (Official)](https://github.com/LedgerHQ/app-ergo)** *(Live)* [`C`] *(Active)*
- [Ledger App for Ergo (Tesseract Fork)](https://github.com/tesseract-one/ledger-app-ergo) – community-maintained fork. [`C`] *(Active)*
  - [LedgerJS Bindings](https://github.com/anon-br/ledgerjs-hw-app-ergo) [`JS`]
  - [Ledger4j Bindings](https://github.com/aionnetwork/ledger4j) [`Java`]
  - [Ledger Core Lib](https://github.com/LedgerHQ/lib-ledger-core) [`C++`]

---

## 📜 Standards (EIPs) <a id="standards-eips"></a>

- **[EIP Repository](https://github.com/ergoplatform/eips)** – official Ergo Improvement Proposals.
- [EIP-1: Ergo Address Types](https://github.com/ergoplatform/eips/blob/master/eip-0001.md)
- [EIP-3: HD Wallet Derivation Paths](https://github.com/ergoplatform/eips/blob/master/eip-0003.md)
- [EIP-4: Asset Standard (Tokens & NFTs)](https://github.com/ergoplatform/eips/blob/master/eip-0004.md)
- [EIP-5: ErgoScript Templates (Deprecated)](https://github.com/ergoplatform/eips/blob/master/eip-0005.md)
- [EIP-6: Headless dApp Protocol](https://github.com/ergoplatform/eips/blob/master/eip-0006.md)
- [EIP-11: Asset Issuance Box Standard](https://github.com/ergoplatform/eips/pull/11)
- [EIP-12: dApp Connector Interface](https://github.com/ergoplatform/eips/pull/23/files)
- [EIP-15: SigmaUSD Protocol](https://github.com/ergoplatform/eips/blob/master/eip-0015.md)
- [EIP-16: Oracle Pool V2 (Draft)](https://github.com/ergoplatform/eips/blob/eip16/eip-0016.md)
- [EIP-17: Proxy Contracts Standard](https://github.com/ergoplatform/eips/blob/master/eip-0017.md)
- [EIP-19: Cold Wallet Standard](https://github.com/ergoplatform/eips/blob/master/eip-0019.md)
- [EIP-20: ErgoPay URI Scheme](https://github.com/ergoplatform/eips/blob/master/eip-0020.md)
- [EIP-21: URI Scheme for Token Payments](https://raw.githubusercontent.com/ergoplatform/eips/master/eip-0021.md) (Draft)
- [EIP-22: Auction Contract Standard](https://github.com/ergoplatform/eips/blob/master/eip-0022.md)
- [EIP-23: Oracle Pool V2 Bootstrap Standard](https://github.com/ergoplatform/eips/tree/cae50b722d6929c794847d21668500acb01f3c8c/eip-0023/contracts)
- [EIP-24: Digital Artwork / NFT Standard](https://github.com/ergoplatform/eips/blob/master/eip-0024.md)
- [EIP-25: Payment Request URI Scheme](https://github.com/ergoplatform/eips/blob/master/eip-0025.md)
- [EIP-27: Miner Voting Parameters](https://github.com/ergoplatform/eips/blob/master/eip-0027.md)
- [EIP-31: Babel Fees Standard](https://github.com/ergoplatform/eips/blob/master/eip-0031.md)
- [EIP-33: Crowdfunding Contract Standard](https://github.com/ergoplatform/eips/pull/33)
- [EIP-37: Autolykos v2 Update](https://github.com/ergoplatform/eips/blob/ddbca24fef5e91e0c80c6881fc31d8831ae69768/eip-0037.md)
- [EIP-38: Partial Voting for Miners (Draft)](https://github.com/WilfordGrimley/eip38PartialVoting)
- [EIP-39: Just-In-Time Costing (JITC)](https://github.com/ergoplatform/eips/blob/master/eip-0039.md)
- [EIP-41: Stealth Addresses (Draft)](https://raw.githubusercontent.com/ergoplatform/eips/d21280977f2c21dc733632c48c98d0f614bc6123/eip-0041.md)
- [EIP-43: Reduced Transaction](https://github.com/ergoplatform/eips/pull/91) – [Implementation Example](https://github.com/zkastn/reduced-transactions)
- [EIP-44: Arbitrary Data Signing](https://github.com/ergoplatform/eips/pull/92)
- [EIP-45: Storage Rent Redistribution (Draft)](https://github.com/ergoplatform/eips/pull/93)
- [EIP-46: Authentication Message Signing (Draft)](https://github.com/ergoplatform/eips/blob/2de4ea0deff12a276f74df57ef3a14dab2c5dfb8/eip-0046.md)
- [EIP-47: Re-emission Contract Standard (Draft)](https://github.com/ergoplatform/eips/blob/0836dd1eca323c6b5fd6b5172c27a465bd4449cd/eip-0047.md)
- [EIP-50: Context Extension Clarification (Draft)](https://github.com/ergoplatform/eips/blob/a24fc414abbc10e6ee59f878b280d9ecc725e10c/eip-0050.md)
- [SigmaUSD Improvement Proposals (SIPs)](https://github.com/ergoplatform/sips): Repository for proposals related to the SigmaUSD protocol.

---

## 🔍 Explorers <a id="explorers"></a>

> See also: [Explorer Overview on ErgoDocs](https://docs.ergoplatform.com/dev/stack/explorer/)

- **[Ergo Explorer (Official)](https://explorer.ergoplatform.com/)** – canonical chain explorer. [Frontend](https://github.com/ergoplatform/explorer-frontend) | [Backend](https://github.com/ergoplatform/explorer-backend)
- [Sigmaspace](https://sigmaspace.io/) – alternative explorer with tools & charts. [GitHub](https://github.com/pulsarz/sigmaexplorer)
- [erg-explorer](https://github.com/AcoSmrkas/ErgExplorer) – community-built explorer. [`JS/TS`] [Telegram](https://t.me/ErgExplorer)
- [uexplorer](https://github.com/pragmaxim/ergo-uexplorer) – minimalist UTXO set explorer. [`Scala`]
- [Indexed Node Explorer](https://github.com/Luivatra/indexed-node-explorer) – simple UI for indexed node. [`JS/TS`]
- [Testnet Explorer](https://testnet.ergoplatform.com/) – explorer for the test network.
  - [Using Ergo Testnet (Wiki)](https://github.com/ergoplatform/ergo/wiki/Ergo-Testnet)

## 📊 Dashboards & Network Stats <a id="dashboards"></a>

- [ErgoWatch](https://ergo.watch/) – network stats, tokenomics & analytics. [GitHub](https://github.com/abchrisxyz/ergowatch)
- [Ergo Nodes Dashboard](http://ergonodes.net/) – network map & node stats. [GitHub](https://github.com/Satergo/Ergonnection)
- [Paizo Mining Vote Simulator](https://deadit.github.io/paizo/) – EIP-27 miner voting simulator. [GitHub](https://github.com/deadit/paizo)
- [ErgCube](https://ergcube.com/) – community dashboard & info site.
- [Testnet Faucet](https://testnet.ergofaucet.org/) – faucet for testnet ERG.

---

## 📊 Analytics <a id="analytics"></a>

- **[ErgoVision](https://github.com/CryptoCream/ErgoVision)** – wallet visualizer & transaction investigator. [`Python`]
  - [Colab Notebook](https://colab.research.google.com/drive/13O_6XEHi7xbjuhzby0s7YGX0rshrClXK?usp=sharing)
- [SigmaUSD Bank Analysis Notebook](https://colab.research.google.com/drive/1iA_PPvWrJGjdpOFYME7W_lQrU4BemaE4?usp=sharing) – Colab notebook for SigmaUSD analysis. [`Python`]
- [ergo-intelligence](https://github.com/Eeysirhc/ergo-intelligence) – tools & resources for blockchain analysts.
- [tidyergo](https://github.com/Eeysirhc/tidyergo) – R/Tidyverse package for Ergo stats. [`R`]
- [ergo-analytics](https://github.com/gsblabsio/ergo-analytics) – Docker setup for network insights. [`Docker`]
- [ErgoStats Android](https://github.com/sachindayl/ErgoStatsAndroid) – Android app for network stats. [`Kotlin`/`Java`]
- [ErgoStats iOS](https://github.com/ach2swift/ErgoStats) – iOS app for network stats. [`Swift`]
- [Ergo Tokenautics](https://github.com/babygrenade/ergo-tokenautics) – token distribution analysis tool. [`Python`]
- [Ergo Token Analysis (Freebyo)](https://github.com/freeboy0/ergo-token-analysis) – token analysis tools. [`Python`?]
- [Developer Activity (Artemis)](https://app.artemis.xyz/developer-activity?ecosystemValue=Ergo) – tracks dev activity via GitHub commits.
- [Developer Activity (DeveloperReport)](https://www.developerreport.com/ecosystems/ergo) – alternative dev activity view.
- [Ergo Node Metrics Report Notebook](https://github.com/ergoplatform/ergo/blob/master/metrics/Report.ipynb) – Jupyter notebook for node performance metrics. [`Python`]
- [Ergo Notebooks (Glasgowm)](https://github.com/glasgowm148/ergo-notebooks) – collection of Jupyter notebooks for analysis. [`Python`]
- [Ergo Explorer Queries (FlyingPig)](https://github.com/FlyingPig69/Ergo_Explorer_Queries) – SQL queries for analyzing explorer data. [`SQL`]
- [ergo-status](https://github.com/bdkent/ergo-status) – community-run network status dashboard. [`JS/TS`?]

---

## 🤝 Community & Resources <a id="community--resources"></a>

### 📰 Information Hubs <a id="information-hubs"></a>

- **[Ergo Platform Website](https://ergoplatform.org/)** – official entry point & news. [GitHub](https://github.com/ergoplatform/website)
- **[Ergo Documentation](https://docs.ergoplatform.com/)** – official docs for users, devs, miners. [GitHub](https://github.com/ergoplatform/ergodocs)
- [Ergonaut Handbook](https://ergonaut.space/) – community-driven wiki & handbook.
- [Sigmaverse](https://sigmaverse.io/) – directory of dApps & tools. [GitHub](https://github.com/ergoplatform/sigmaverse)
- [ErgoForum](https://www.ergoforum.org/) – official community discussion forum.
- [Ergo Discord](https://discord.gg/ergo-platform-668903786361651200) – main community chat server. *(Verify invite)*
- [Ergo Telegram](https://t.me/ergoplatform) – main Telegram group.
- [Ergo Reddit](https://www.reddit.com/r/ergonauts/) – subreddit for discussion.
- [Awesome Ergo](https://github.com/ergoplatform/awesome-ergo) – this curated list.
- [Ergo Sites](https://ergosites.github.io/) – community-maintained website list.
- [Ergo Platform Wiki](https://github.com/ergoplatform/ergo/wiki) – official node software wiki.
- [Ergo Foundation Website](https://ergofoundation.org/) – info about the Ergo Foundation.
- [Ergo Platform GitHub Discussions](https://github.com/ergoplatform/ergo/discussions) – forum for node dev/technical topics.
- [ergohack.io](https://ergohack.io/resources) – resource hub for ErgoHack events.
- [ErgoNation](https://github.com/nirojan95/ergonation) – community project/news site. [`JS/TS`]
- [Sigmanauts (Cafebedouin)](https://github.com/cafebedouin/sigmanauts) – community/resource site. [`JS/TS`]

### 💰 Contribution Platforms <a id="contribution-platforms"></a>

- **[Ergo Bounties](https://github.com/ErgoDevs/Ergo-Bounties)** – platform for finding & funding bounties.
- [Grow Ergo Issues](https://github.com/ergoplatform/grow-ergo/issues) – GitHub issues for ecosystem growth tasks.
- [Ergo Node Issues](https://github.com/ergoplatform/ergo/issues) – main issue tracker for reference node.
- [Analytics Ecosystem Data](https://github.com/electric-capital/crypto-ecosystems/blob/master/data/ecosystems/e/ergo.toml) – add project for dev activity tracking.

### 🎓 Education & Tutorials <a id="education--tutorials"></a>

- **[DeCo Education](https://deco-education.github.io/deco-docs/docs/intro)** – educational platform with Ergo courses. [GitHub Org](https://github.com/DeCo-Education)
  - [Into the Woods Course](https://deco-education.github.io/deco-docs/docs/category/into-the-woods)
  - [ErgoScript Developer Course](https://github.com/DeCo-Education/ErgoScript-Developer-Course)
  - [DeCo Homeworks](https://github.com/DeCo-Education/DeCo-Homeworks)
  - [Ergo School](https://github.com/DeCo-Education/Ergo-School)
- [Learn Ergo](https://github.com/learn-ergo) – Community-driven educational resources.
  - [Developer Tutorials](https://github.com/learn-ergo/DeveloperTutorials)
- [ErgoScript 101 Crash Course (Slides)](https://docs.google.com/presentation/d/10gYO82z_7qloRrFOcCxTFuzpP40IImPyIKMV2ZFd9M4/edit#slide=id.p) – quick overview slides.
- [Zack Balbin's Ergo Tutorials](https://github.com/zackbalbin/ErgoTutorials) – Scala tutorials. [`Scala`]
- [ErgoTutorials.com (LadoPixel)](https://github.com/ladopixel/ErgoTutorials.com) – Community tutorial website.
- [dAppStep](https://github.com/ilyaLibin/dAppStep) – Educational platform/tool.
- [SigmaFi Docs (Noah)](https://github.com/NoahErgo/SigmaFi-Docs) – Documentation for SigmaFi.
- [Ergo Community YouTube](https://www.youtube.com/@ErgoPlatform) – official channel (AMAs, tutorials).
- [ErgoFoundation YouTube](https://www.youtube.com/@ErgoFoundation) – Foundation-focused channel.
- [Starting with Appkit on Gradle projects](https://github.com/ergoplatform/ergo-appkit/wiki/Tutorial-starting-with-Appkit-on-Gradle-projects) – AppKit setup tutorial.
- [AppKit by Example (Video)](https://www.youtube.com/watch?v=Md5s-XV6-Hs) – video tutorial.
- [Learn ErgoScript By Example Via The Ergo Playground (Video)](https://www.youtube.com/watch?v=8l2v1asHgyA) – video tutorial.
- [Multi-Stage Contracts in the UTXO Model (Video)](https://www.youtube.com/watch?v=g3FlM_WOwBU) – presentation.
- [ErgoScript Design patterns (Forum)](https://www.ergoforum.org/t/ergoscript-design-patterns/222) – forum discussion.
- [Advanced ErgoScript Tutorial (PDF)](https://ergoplatform.org/docs/AdvancedErgoScriptTutorial.pdf) – in-depth PDF tutorial.
- [Ergo with C# 101 (Video Playlist)](https://www.youtube.com/watch?v=aUuki-fAxwc&list=PLUWruihtE-HtL-JZk8Vb4Yn_H18aE3rb6) – YouTube playlist.
- [A Quick Primer on ErgoScript (Wiki)](https://github.com/ergoplatform/ergo/wiki/ErgoScript-Overview) – wiki overview.
- [Building Ergo: ErgoScript (Blog)](https://ergoplatform.org/en/blog/2021-06-09-building-ergo-ergoscript/) – blog post.
- [Using Appkit from Python (Wiki)](https://github.com/ergoplatform/ergo-appkit/wiki/Using-Appkit-from-Python) – guide using JPype.
- [Ergo Full Node on Raspberry Pi Guide](https://github.com/ccgarant/ergo-full-node-raspi) – community guide.
- [Fleet SDK Documentation](https://fleet-sdk.github.io/docs/) – official Fleet SDK docs.
  - [Fleet Compiler Docs](https://fleet-sdk.github.io/docs/compiler)
  - [Fleet Serializer Overview](https://fleet-sdk.github.io/docs/serializer-overview)
  - [Fleet Babel Fees Plugin Docs](https://fleet-sdk.github.io/docs/plugins/babel-fees)
- *Note: The main [Ergo Documentation](https://docs.ergoplatform.com/dev/tutorials/) contains many specific guides (e.g., debugging, message signing, running off-chain bots).*

### 📄 Papers & Specifications <a id="papers--specifications"></a>

- **[Ergo Whitepaper](https://ergoplatform.org/en/documents/)** – foundational design document.
- [ErgoScript Whitepaper](https://ergoplatform.org/docs/ErgoScript.pdf) – detailed language paper.
- [Autolykos PoW Algorithm](https://ergoplatform.org/docs/ErgoPow.pdf) – PoW algorithm paper.
- [NiPoPoWs Paper](https://eprint.iacr.org/2016/994.pdf) – research paper.
- [Storage Rent Paper](https://ergoplatform.org/docs/StorageRent.pdf) – storage rent mechanism paper.
- [Sigma Protocols Paper](https://ergoplatform.org/docs/ergoscript.pdf) – covered in ErgoScript Whitepaper.
- [ErgoTree Specification](https://raw.githubusercontent.com/ScorexFoundation/sigmastate-interpreter/master/docs/spec/ergotree.pdf) – formal spec.
- [ErgoScript Language Specification](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md) – syntax & semantics spec.
- [Sigma Language DSL Documentation](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/sigma-dsl.md) – Sigma protocol language features.
- [Know Your Assumptions (KYA)](https://github.com/kushti/kya) – protocol assumption analysis framework. [PDF](https://github.com/kushti/kya/blob/master/kya.pdf)
- [ChainCash Whitepaper](https://github.com/kushti/chaincash/blob/master/paper/chaincash.pdf) – ChainCash protocol paper.
  - [ChainCash Server Docs](https://github.com/ChainCashLabs/chaincash/blob/master/docs/server.md)
- [High Level Design Patterns In Extended UTXO Systems](https://github.com/Emurgo/Emurgo-Research/blob/master/smart-contracts/High%20Level%20Design%20Patterns%20In%20Extended%20UTXO%20Systems.md) – eUTXO dApp patterns research.
- [Ergo Scala Style Guide](https://github.com/ergoplatform/ergo-scala-style-guide) – style guide for Scala contributions.
- [Ergo Social Contract](https://ergoplatform.org/en/blog/2022-04-26-the-ergo-manifesto-revised-edition/) – guiding principles & manifesto.
- [On Contractual Money](https://ergoplatform.org/docs/AdvancedErgoFeatures.pdf) – advanced features paper.
- [ErgoScript Compiler Documentation](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/ergoscript-compiler.md) – compiler internals.
- [ErgoScript Performance & Style Guide](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/perf-style-guide.md) – efficiency tips.
- [Ergo Platform Improvement Proposals (EIPs)](https://github.com/ergoplatform/eips) – EIPs repository.
- [SLIP-0044 : Registered coin types for BIP-0044](https://github.com/satoshilabs/slips/blob/master/slip-0044.md) – Ergo coin type `429`.
- [Ergo Subblocks Paper](https://raw.githubusercontent.com/ergoplatform/ergo/e15dcd0b4ca0a72d32d97228f010d813540de39d/papers/subblocks/subblocks.md) – sub-block concept paper.
- [Ergohack Sidechain Whitepaper](https://github.com/ross-weir/ergohack-sidechain/blob/main/docs/whitepaper/sidechain.pdf) – Ergohack sidechain PoC paper.
- [Ergohack Sidechain Repo](https://github.com/ross-weir/ergohack-sidechain) – Ergohack sidechain PoC repo. [`Rust`?]
- [Stealth Address Docs (Aragogi)](https://github.com/aragogi/Stealth-doc) – stealth address scanner/mixer docs.
- [Test Vectors - Transaction Serialization](https://github.com/ergoplatform/ergo-test-vectors/blob/master/src/test/resources/vector/tx_ser.json) – TX serialization test examples.
- [Test Vectors - Signature Scheme](https://github.com/ergoplatform/ergo-test-vectors/blob/master/src/test/resources/vector/sig.json) – signature scheme test examples.
- [Difficulty Algorithms (Zawy)](https://github.com/zawy12/difficulty-algorithms) – research and analysis of difficulty adjustment algorithms.
- **[Scorex](https://github.com/scorexfoundation/scorex)** – modular blockchain framework that *underpins* Ergo's core node implementation. [`Scala`]

### 🔩 Utilities <a id="utilities"></a>

- [ErgoTipper Token List](https://github.com/Luivatra/ergotipper-tokens) – tokens recognized by ErgoTipper bot.
- [Spectrum Token List](https://github.com/spectrum-finance/ergo-token-list) – token list curated by Spectrum Finance.
- [ErgoToolsBot (Telegram)](https://t.me/ergotoolsbot) – Telegram bot with various utilities. [GitHub](https://github.com/ladopixel/ErgoToolsBot) [`Python`]
- [Matterbridge](https://github.com/42wim/matterbridge) – software for bridging community chats.
- [SharkNet](https://github.com/The-Last-Byte-Bar/SharkNet) – community dataset of ErgoScript examples for AI/ML.
- [ErgoLLM](https://github.com/glasgowm148/ErgoLLM) – experimental LLM/AI tooling for Ergo. [`Python`]
- [General Ergo Chatbot](https://www.chatbase.co/chatbot-iframe/zxB2uzZfYoHIpA98eTzgM) – AI assistant trained on Ergo docs.
- [ErgoScript Chatbot](https://www.chatbase.co/chatbot-iframe/INAIfQ2ts4E6ykf4rseVu) – AI assistant focused on ErgoScript.

---

> **Tip:** bookmark this page and ⭐ star it on GitHub to stay in the loop. New tools appear every week!
