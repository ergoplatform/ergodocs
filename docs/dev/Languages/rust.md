# Rust

[sigma-rust](https://github.com/ergoplatform/sigma-rust) is an alternative and simple implementation of ErgoTree interpreter and transaction building tools. The goal for the Rust version is to be on par with the Scala version feature-wise. Now Rust version is still significantly behind. Also, the goal for the Rust version is to have bindings for web, iOS and Android. The Scala version will continue to be the primary choice for the JVM ecosystem, with the Rust version covering the rest.

## Contributing


A list of "*good first*" issues is [available on GitHub](https://github.com/ergoplatform/sigma-rust/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) - @greenhat on [Discord](https://discord.gg/Q86PNMwRsu) is ready to assist anyone who is interested.

The sigma-rust GitHub repo is [here](https://github.com/ergoplatform/sigma-rust).   There is an issues tab with labelled tasks anyone can pick up.  If you are working on something, leave a comment, so others know. 
- [contributing](https://github.com/ergoplatform/sigma-rust/blob/develop/CONTRIBUTING.md)

## References
- This [document](https://github.com/ergoplatform/sigma-rust/blob/develop/docs/architecture.md) describes the high-level architecture of ErgoScript compiler and ErgoTree interpreter.
- [Rust port of AVL tree from scrypto package.](https://github.com/knizhnik/scorex_crypto_avltree/blob/main/crypto_avltree.md)
- [Ergo Utilities](https://github.com/robkorn/ergo-utilities-rust/) | simplify writing off-chain code in Rust.


Use `https://wallet.plutomonkey.com/p2s/?source=` to compile any contract to P2S address and then use it in rust like this - `https://github.com/ergoplatform/sigma-rust/blob/fd197d0c0892cd24bbcb475e0a83243784700e32/ergotree-interpreter/src/contracts.rs#L159-L167`
This approach should work in JS/TS WASM bindings as well.

## Resources

- [doc.rust-lang.org](https://doc.rust-lang.org/book/)