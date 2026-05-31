---
tags:
  - Developers
  - Getting Started
  - Overview
---

# Developers

There are many tools, libraries, SDKs, frameworks and utilities developers can use to interact with the blockchain, build their applications, and display them to users.

For current source-backed tooling, see [Libraries & SDKs](libraries.md), [Fleet](fleet.md), [Sigma Rust](sigma-rust.md), [ergots](ergots.md), and [Ergo Agent SDK](ergo-agent-sdk.md).

## Stack

::cards::

[{
    "title": "Server",
    "content": "Interact with the blockchain locally or via a remote server.",
    "image": "../assets/img/dev-grid/server.png",
    "url": "stack/server.md"
  },
  {
    "title": "Browser",
    "content": "Interact with users in browser",
    "image": "../assets/img/dev-grid/browser.png",
    "url": "stack/browser.md"
  },
  {
    "title": "Desktop",
    "content": "Create a local application.",
    "image": "../assets/img/dev-grid/desktop.png",
    "url": "stack/desktop.md"
  },
  {
    "title": "Mobile Application",
    "content": "Creating a bundled mobile app for Android or iOS.",
    "image": "../assets/img/dev-grid/mobile.png",
    "url": "stack/mobile.md"
 }]

::/cards::

## Just Starting Out

::cards::

[{
    "title": "Basics Tutorial",
    "content": "Generate keys and address, send and receive payments.",
    "image": "../assets/img/dev-grid/noob.png",
    "url": "stack/basics.md"
  },
  {
    "title": "Beginner",
    "content": "Just testing the waters? Not sure where to start?",
    "image": "../assets/img/dev-grid/noob.png",
    "url": "stack/introduction.md"
  },
  {
    "title": "Frameworks",
    "content": "Jump straight to an overview of all frameworks",
    "image": "../assets/img/dev-grid/frameworks.jpg",
    "url": "stack/introduction.md#frameworks"
 }]

::/cards::

## Where To Go Next

## Choose a Stack

| Build target | Best fit | Why | Main docs |
| --- | --- | --- | --- |
| Browser dApp | Fleet + dApp Connector | Common TypeScript path for browser wallets and transaction building. | [Fleet](fleet.md), [Browser](browser.md), [dApp Connector](dApp.md) |
| JVM backend or exchange service | AppKit | Mature JVM tooling for node-backed services and transaction workflows. | [AppKit](appkit.md), [JVM](jvm.md), [Exchange Integration](guide.md) |
| Rust service or constrained environment | sigma-rust | Core Rust libraries and bindings for wallets, WASM, and lower-level tooling. | [Sigma Rust](sigma-rust.md), [Rust](rust.md), [Constrained Environments](sigma-rust-constrained.md) |
| Python automation or agents | Ergo Agent SDK / ergo-lib-python | Good fit for scripted workflows, agents, and data-heavy automation. | [Ergo Agent SDK](ergo-agent-sdk.md), [Ergo-Lib-Python](ergo-lib-python.md), [Python](python.md) |
| C# application | FleetSharp | .NET-oriented transaction tooling. | [FleetSharp](fleetsharp.md), [C#](csharp.md) |
| Mobile app | Native stack + sigma-rust bindings where needed | Mobile builds need wallet UX, signing constraints, and platform-specific packaging. | [Mobile](mobile.md), [Android](android.md), [iOS](iOS.md) |
| Contract prototype | ErgoScript tools + playgrounds | Best path for learning contract behavior before building full off-chain flows. | [ErgoScript Tooling](ergoscript-tooling.md), [Kiosk](kiosk.md), [Compiler](compiler.md) |

Use [Libraries & SDKs](libraries.md) when you need a fuller inventory.

## Where To Go Next

| Goal | Start here | Related |
| --- | --- | --- |
| Web dApp | [Browser](browser.md) | [Fleet](fleet.md), [dApp Connector](dApp.md), [ErgoPay](ergo-pay.md) |
| Backend or bot | [Server](server.md) | [Off-chain Services](off-chain-overview.md), [Blockchain Indexing](blockchain-indexing.md), [Node API](swagger.md) |
| Mobile or constrained app | [Mobile](mobile.md) | [Android](android.md), [iOS](iOS.md), [Mobile Build Constraints](mobile-build-constraints.md) |
| Contract development | [ErgoScript](ergoscript.md) | [Kiosk](kiosk.md), [Compiler](compiler.md), [Contract Patterns](contracts-library.md) |
| Library selection | [Libraries & SDKs](libraries.md) | [AppKit](appkit.md), [Sigma Rust](sigma-rust.md), [Fleet](fleet.md), [ergots](ergots.md) |
| Tutorials | [Tutorials and Recipes](tutorials.md) | [Fleet Recipes](fleet-sdk-recipes.md), [Hardware Wallets](hardware-wallet-integration.md), [Indexing](blockchain-indexing.md) |
