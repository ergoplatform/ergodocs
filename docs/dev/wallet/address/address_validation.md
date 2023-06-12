# Address validation

[ergo-simple-addresses](https://github.com/kushti/ergo-simple-addresses) contains few zero-dependencies Java-friendly utils for working with addresses. The [Integration Guide for Exchanges](guide.md) may also be relevant. There is also a simple method in [Fleet](https://github.com/fleet-sdk/fleet/blob/master/packages/core/src/models/ergoAddress.ts#L164). 

- **P2S** has no limit since it is the serialized script.
- **P2SH** is 192 bits since it is the "first 192 bits of the Blake2b256 hash of serialized script bytes."
- **P2PK** length is fixed. You can use the [linked class](https://github.com/ergoplatform/ergo-appkit/blob/9e19c13d82966eaee59433d16c4fb987bea363a7/lib-impl/src/main/java/org/ergoplatform/appkit/impl/OutBoxBuilderImpl.scala#L66) to validate an address (it gives a runtime exception when created from an invalid string). 

In P2S, everyone can see the script; in P2SH, the script will be known when it will be spent.

P2SH has `0x12` at the beginning, and P2S has `0x13` on testnet and `0x02` and `0x03` on mainnet accordingly (note that in hex, you can see that, but in base58, it can change to anything).

As you can see 

> 88dhgzEuTXaRxf1rbqBRZ6Zbw9iigdB4PCdjyFKLrk22gnmjKcxZBe53vqJVetRa4tTNF9oowQWPp2c6 

equals

> **03** 10 02 04 a0 0b 08 cd 02 a1 f5 67 16 cb 8d f4 fe b9 37 14 37 90 4b 91 25 b8 2d b9 39 23 8c d7 d9 48 78 6d b3 3d e3 13 9f ea 02 d1 92 a3 9a 8c c7 a7 01 73 00 73 01 8c 23 55 af
