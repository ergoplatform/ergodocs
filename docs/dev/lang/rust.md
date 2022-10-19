---
tags:
  - Rust
---


# Rust

[sigma-rust](https://github.com/ergoplatform/sigma-rust) is an alternative and simple implementation of ErgoTree interpreter and transaction building tools. The goal for the Rust version is to be on par with the Scala version feature-wise. Now Rust version is still significantly behind. Also, the goal for the Rust version is to have bindings for web, iOS and Android. The Scala version will continue to be the primary choice for the JVM ecosystem, with the Rust version covering the rest.


## Compiling 

Use **plutomonkey** to compile any contract to P2S address 

```
https://wallet.plutomonkey.com/p2s/?source=
```
and then use the resulting P2P address in rust like this
```
https://github.com/ergoplatform/sigma-rust/blob/fd197d0c0892cd24bbcb475e0a83243784700e32/ergotree-interpreter/src/contracts.rs#L159-L167`
```
This approach should work in JS/TS WASM bindings as well.


## Contributing
There is a labelled issues tab on [sigma-rust](https://github.com/ergoplatform/sigma-rust/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) that anyone can pick up.  If you are working on something, leave a comment, so others know. [@greenhat](https://discord.gg/Q86PNMwRsu) is ready to assist with anyone interested.

Read the full [contributing](https://github.com/ergoplatform/sigma-rust/blob/develop/CONTRIBUTING.md) guidelines.

## References
- This [document](https://github.com/ergoplatform/sigma-rust/blob/develop/docs/architecture.md) describes the high-level architecture of ErgoScript compiler and ErgoTree interpreter.
- [Rust port of AVL tree from scrypto package.](https://github.com/knizhnik/scorex_crypto_avltree/blob/main/crypto_avltree.md)
- [Ergo Utilities](https://github.com/robkorn/ergo-utilities-rust/) | simplify writing off-chain code in Rust.



