# Compiling ErgoScript

To compile any ErgoScript contract into a P2S (Pay-to-Script) address, you can use **plutomonkey**:

```
https://wallet.plutomonkey.com/p2s/?source=
```

After compiling, the resulting P2S address can be utilized within Rust, as demonstrated in the following code snippet:

```rust
    fn simplified_age_usd_bank_contract() {
        let p2s_addr_str = "7Nq5tKsVYCgneNgEfA2BJKwGsWozezNLhCNsRBihcHVFkDTuTThd4Qt1bi7NfCK1HuuVfjksMrEftV6MEFajjuyp1TMD2PX7SYWvkg9zH4CtgpdoBjekCNXs5XawxXnW6FT7GCqXTpJUP2TkkuqBh1df99PTigehys36uZz9wQnkrJXrv3mw3Yy4CM622qe5wdqLtpEonjazEmsw8weqEYegDyfJnswDvDkLPXtcCB86i19jik4fnSTtCcYj3jpWCQ7WL5dZn1ivs5JGRsR2ioNCRiZd3Gu1zJBgbHkMg41Z6VeCRWXjGY99BUtgtQiepSHGHajFCVcFAHhVxccdVUPCxGeEL6c2dNx6qzEkVfTfHs5qBgJewR8KCZTCVTurNBHeqCSVdxnfFvhW3f72cNrae5E1UhTAXU2iX4LZMHQsKyefY24Aq1b1srTyRWLpixjbcezFqA2TKjGSn1p1ruxbR7AQpW24ByPKT9sFE9ii4qNeXDnLcGtAAGS9FC5SD1s516a4NCu6v9zZfTvRKGkCwt78J8DEVnhTbttjcsvqFsUXQrvAv7TGVsaT4mL6B7F5BhRoZwFkgRXqFUVCWvgqJrwwjFRtbc5aZz";
        let encoder = AddressEncoder::new(NetworkPrefix::Mainnet);
        let addr = encoder.parse_address_from_str(p2s_addr_str).unwrap();
        let script: Rc<Expr> = addr.script().unwrap().proposition().unwrap();
        dbg!(&script);
        let res: bool = eval_out_wo_ctx::<SigmaProp>(script.as_ref())
            .try_into()
            .unwrap();
        assert!(res);
    }

```
See [this link](https://github.com/ergoplatform/sigma-rust/blob/fd197d0c0892cd24bbcb475e0a83243784700e32/ergotree-interpreter/src/contracts.rs#L159-L167) for full context

This approach should also be applicable with JavaScript or TypeScript WASM (WebAssembly) bindings.