# Schnorr Signature

In the simplest case a signature in Ergo transaction is a Schnorr signature, in general case it is a signature corresponding to a subset of Generalized Schnorr Proofs.

- Ergo uses the same elliptic curve as Bitcoin (SecP256K1).
- Ergo's Schnorr signature is pretty close to known standards (RFCs). 
- Allows us to adopt known protocols such as [MuSig](https://eprint.iacr.org/2018/068). 
- It's possible to create **adaptor signatures** which can be used for private swaps. 
- There were private swap demos with Bitcoin Cash


| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| Potentially, a lot of protocols | - | The same as Bitcoin |


## Resources

- [sign function based on schnorr protocol](https://github.com/ErgoGravity/gateway-proxy/blob/9cbf72b934b08e258457367e366050a1734f1050/app/gateway/Adaptor.scala#L391) 

Generic auth is used on the blockchain. So in general case if you want to sign an arbitrary message with a pubkey used onchain, the key is in generalized Schnorr statetement aka `SigmaBoolean` form