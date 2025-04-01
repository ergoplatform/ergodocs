---
tags:
  - Analog Ergo
  - Marketplace
  - Atomic Swaps
  - dApp
  - dApp-InDev
---

# Analog Ergo

This project aims to use cryptographic primitives (well established, low level algorithms) as the basis for a cross-chain peer-to-peer marketplace. It will enable users to set and agree to listing prices and other parameters in a private and fungible manner, without the involvement of intermediaries.



## ScalarLock

> Successfully tested a Scalar Lock contract, this allows you to lock funds to a scalar value like a random 256bit number that you can test by comparing it with an Elliptic curve multiplication operation against the Secp256k1 Generator. A key component of how values are checked when verifying cryptographic signatures and will enable the final step to Atomic Swaps!. 
ErgoScript makes this quite easy (Once the constants and [registers](registers.md) are figured out):

```scala
 val scalarLockScript: String = {
        s"""
            {
            val xBYTES = OUTPUTS(0).R4[Coll[Byte]].get
            val x = byteArrayToBigInt(xBYTES)
            val G = decodePoint(generator)
              sigmaProp(
                receiver &&
                G.exp(x) == xG
              )
            }
        """.stripMargin
```

 It compares a given scalar value (x) to an elliptic curve multiplication operation of Secp256k1 generator (G) and checks if they are equal.

 It decodes the generator point and extracts a scalar value from the transaction output. It then checks if the point computed from the scalar multiplication of the generator point and the extracted scalar value is equal to a predefined point. If the two points are equal, the transaction is valid.




- [Deploying](https://tn-ergo-explorer.anetabtc.io/en/transactions/b9d6a5796e0fa7b8fdf374426219d8fe2d64e7d9976e04845a0a6886414343b9)
- [Spending](https://tn-ergo-explorer.anetabtc.io/en/transactions/8c2440eff436a0c2f2af4b8b2d2ac53fbcfd43762b411217a26899f0ce749ba0)
- [Scala](https://github.com/dzyphr/ScalaSigmaParticle/blob/main/ScalarLock/src/main/scala/ScalarLock.scala)

## 2-Party Atomic Swap

A working python example of a 2-party atomic swap that you can simulate from 2 shell/terminal windows is available at [2pAtomicSwapExample](https://github.com/dzyphr/2pAtomicSwapExample). This might help people reason about the way in which secrets are shared through this protocol and at what steps what data transfer or blockchain interaction is supposed to occur.
