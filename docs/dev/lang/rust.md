---
tags:
  - Rust
---
# Rust

On-chain contracts are developed in ErgoScript, a simple language designed for writing smart contracts on the Ergo blockchain. ErgoScript is a Turing-complete language that prioritizes security and is well-suited for the UTXO transactional model used by Ergo.

For off-chain components, such as interacting with the blockchain, creating transactions, and building applications, developers can use Rust along with frameworks like sigma-rust. Rust provides a powerful and efficient language for building off-chain components, while sigma-rust provides a Rust port of the sigmastate-interpreter, allowing developers to interact with the Ergo blockchain from their Rust applications.

One example of using Rust for off-chain components is the Oracle Pools project, a federated protocol for delivering external data to the Ergo blockchain. The on-chain contracts and descriptions are available in the Ergo Improvement Proposals (EIPs), while the off-chain part is implemented in Rust using the oracle-core repository.

Understanding the UTXO transactional model is crucial when developing off-chain components for Ergo, as it differs from the account-based model used by other blockchains. Developers with experience in parallel computing may find the UTXO model more natural to work with.

## Frameworks

::cards::

[
  {
    "title": "sigma-rust",
    "content": "Rust port of the sigmastate-interpreter",
    "url": "../stack/sigma-rust.md"
  },
  {
    "title": "HDF",
    "content": "Headless dApp Framework",
    "url": "../stack/headless.md"
  },
  {
    "title": "RustKit",
    "content": "(WIP), A SDK for building applications on the Ergo blockchain",
    "url": "../stack/rustkit.md"
  },

]

::/cards::

## Utilities


::cards::

[
  {
    "title": "🔗 Ergo Utilities",
    "content": "simplify writing off-chain code in Rust.",
    "url": "https://github.com/robkorn/ergo-utilities-rust/"
  },
  {
    "title": "🔗 ergo-monitoring",
    "content": "Debug service printing out useful for developers and managers information about ergo blockchain state.",
    "url": "https://github.com/SabaunT/ergo-monitoring"
  },
  {
    "title": "🔗 Rust AVL Tree",
    "content": "Rust port of AVL tree from scrypto package.",
    "url": "https://github.com/knizhnik/scorex_crypto_avltree/blob/main/crypto_avltree.md"
  }
  
]

::/cards::
