---
tags:
  - JavaScript
  - TypeScript
---

# JavaScript & TypeScript

JavaScript and TypeScript developers can interact with the Ergo blockchain using various libraries and frameworks. Notably, [JS/TS bindings for sigma-rust](sigma-rust.md#bindings) (via WebAssembly) provide core blockchain interaction capabilities.

[Appkit](appkit.md) was designed as an abstraction layer on top of [Sigma](sigmastate-interpreter.md). This gives a lot of freedom on the core level in Sigma, while keeping [dApp-facing APIs](api.md) stable.

With the availability of [Sigma.js](sigmajs.md), [Fleet](fleet.md) can play the same role for JS/TS.



## Frameworks

::cards::

[
  {
    "title": "Fleet",
    "content": "Lets you easily create [Ergo transactions](transactions.md) with a pure JS library.",
    "url": "../stack/fleet.md"
  },
  {
    "title": "Sigma.JS",
    "content": "JavaScript port of the sigmastate-interpreter",
    "url": "../lib/sigmajs.md"
  },
  {
    "title": "AppKit",
    "content": "can be configured to run JavaScript under GraalVM",
    "url": "../stack/appkit.md"
  },
  {
    "title": "sigma-rust (via WASM)",
    "content": "Core Rust library with JS/TS bindings available via WebAssembly.",
    "url": "../stack/sigma-rust.md#bindings"
  }
]

::/cards::

## Tutorials

::cards::

[
  {
    "title": "🔗 dAppStep Docs",
    "content": "include many practical examples with Javascript and Nodejs that will help you to understand to implement different aspects of [dapp functionality](get-started.md) on Ergo",
    "url": "https://www.dappstep.com/"
  },
  {
    "title": "🔗 dApp Development Course",
    "content": "",
    "url": "https://www.youtube.com/watch?v=uC6QO3I4m8o&list=PLzY-irO3z3G8FVDifned2NMFc-PgQqnny"
  },
  {
    "title": "📹 Video Tutorial",
    "content": "[NightOwl dApp Connector](dApp.md) React Package",
    "url": "https://twitter.com/NightOwlCasino/status/1529452399475179520"
  },
  {
    "title": "Address Generation Demo",
    "content": "using sigma-rust and TypeScript",
    "url": "https://github.com/ergoplatform/sigma-rust/blob/develop/bindings/ergo-lib-wasm/examples/address-generation-demo/README.md"
  },
  {
    "title": "Create Transaction Demo",
    "content": "using sigma-rust and TypeScript",
    "url": "https://github.com/ergoplatform/sigma-rust/blob/develop/bindings/ergo-lib-wasm/examples/create-transaction-demo/README.md"
  },

]

::/cards::



## Resources


- [Ergo-Raffle-Bot](https://github.com/zkastn/ergo-raffle-bot) Github
- [ErgoScript.js](https://www.youtube.com/watch?v=_jwMI8M_vrs)
- The Ergo Raffle [documentation](https://github.com/ErgoRaffle/raffle-documentation) provides a detailed description of their implementation. 
- [hypo10use/quid-games](https://github.com/hypo10use/quid-games) (Angular)
