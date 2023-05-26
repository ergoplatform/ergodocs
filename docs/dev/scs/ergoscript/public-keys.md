# Public Key Scripts in ErgoScript

The previously discussed ErgoScript programs could be spent by anyone or by no one, which don't offer much practical utility. ErgoScript becomes much more useful when it allows someone to spend a box if they know the private key corresponding to a certain public key. This is similar to the concept of P2PK (Pay to Public Key) addresses in Bitcoin.

In ErgoScript, several methods allow the creation of such "public-key" scripts. The most frequently used one involves the predicate `proveDlog(ecPoint)`. This predicate evaluates to true if the spender provides a valid proof of knowledge of the discrete logarithm corresponding to `ecPoint`—a point on an elliptic curve over a finite field. This is similar to providing a "signature" in Bitcoin.

Ergo employs the same [Secp256k1 curve as Bitcoin](https://en.bitcoin.it/wiki/Secp256k1), thus, the representation of `ecPoint` remains the same: a 33-byte array where the first byte represents the sign. (Please note that Ergo does not support uncompressed points). However, unlike Bitcoin that uses ECDSA, Ergo leverages Schnorr signatures to construct these proofs.

The following steps outline the process of creating an address encoding the `proveDlog` script:

1. Firstly, you must obtain the Elliptic Curve (EC) point corresponding to the public key. Let's use [the same example as Bitcoin](https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses).
    1. The hex-encoded BigInteger secret is `18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725`.
    2. The corresponding hex-encoded EC point is `0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352`.
    3. Convert the EC point from hex to Base64, resulting in `AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS`.

2. Next, create the corresponding script `proveDlog(decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS")))`.

3. Compile the script. This [yields the address](https://wallet.plutomonkey.com/p2s/?source=cHJvdmVEbG9nKGRlY29kZVBvaW50KGZyb21CYXNlNjQoIkFsQ0dPdFpLaDY2S0wrZzhHdkdvUUR5MVAxUGtodGhSSGEyS0JJaCtXeU5TIikpKQ==) `LQ7iQ4egnCPsZZy5QKsXmaypCRuMxPNtdyGE95fYWCLze8C2hMMwDcAgPNeV8s`.

Funds sent to the above address can be spent using the secret mentioned earlier. You can verify this in the transaction with ID [dfca9eaa745c79dafbed43b73379fb0008608119080954c337a4022a2a5070a3](https://explorer.ergoplatform.com/en/transactions/dfca9eaa745c79dafbed43b73379fb0008608119080954c337a4022a2a5070a3).