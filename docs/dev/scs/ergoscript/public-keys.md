# Public Key Scripts in ErgoScript

ErgoScript, the smart contract language in Ergo, allows for the creation of scripts that can be spent by specific individuals, thereby increasing its practical utility. This is achieved by enabling someone to spend a box if they possess the private key corresponding to a certain public key, a concept similar to P2PK (Pay to Public Key) addresses in Bitcoin.

ErgoScript offers several methods for creating these "public-key" scripts. The most commonly used method involves the predicate `proveDlog(ecPoint)`. This predicate returns true if the spender can provide a valid proof of knowledge of the discrete logarithm corresponding to `ecPoint`—a point on an elliptic curve over a finite field. This is akin to providing a "signature" in Bitcoin.

Ergo uses the same [Secp256k1 curve as Bitcoin](https://en.bitcoin.it/wiki/Secp256k1), so the representation of `ecPoint` is identical: a 33-byte array where the first byte indicates the sign. (Note: Ergo does not support uncompressed points). However, Ergo differs from Bitcoin in that it uses Schnorr signatures, not ECDSA, to construct these proofs.

Here's a step-by-step guide to creating an address that encodes the `proveDlog` script:

1. First, obtain the Elliptic Curve (EC) point that corresponds to the public key. For this example, we'll use [the same one as Bitcoin](https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses).
    1. The BigInteger secret, hex-encoded, is `18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725`.
    2. The corresponding EC point, hex-encoded, is `0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352`.
    3. Convert the EC point from hex to Base64, which gives `AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS`.

2. Then, create the corresponding script `proveDlog(decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS")))`.

3. Compile the script. This [results in the address](https://wallet.plutomonkey.com/p2s/?source=cHJvdmVEbG9nKGRlY29kZVBvaW50KGZyb21CYXNlNjQoIkFsQ0dPdFpLaDY2S0wrZzhHdkdvUUR5MVAxUGtodGhSSGEyS0JJaCtXeU5TIikpKQ==) `LQ7iQ4egnCPsZZy5QKsXmaypCRuMxPNtdyGE95fYWCLze8C2hMMwDcAgPNeV8s`.

Funds sent to the above address can be spent using the secret mentioned earlier. You can verify this in the transaction with ID [dfca9eaa745c79dafbed43b73379fb0008608119080954c337a4022a2a5070a3](https://explorer.ergoplatform.com/en/transactions/dfca9eaa745c79dafbed43b73379fb0008608119080954c337a4022a2a5070a3).