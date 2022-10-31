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