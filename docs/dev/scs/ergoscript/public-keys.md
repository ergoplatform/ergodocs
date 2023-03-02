
# Public-keys

The above ErgoScript programs are either spendable by everyone or by no one, which is not very useful.

Useful ErgoScript programs are those that allow one to spend the box if they know the private key corresponding 
to some public key, similar to Bitcoin's P2PK addresses. 

ErgoScript provides multiple ways to create such "public-key" scripts, but the most common one uses the predicate `proveDlog(ecPoint)`, 
which evaluates to true if the spender supplies a valid proof of knowledge of the discrete logarithm corresponding to `ecPoint`, a point on an elliptic curve over a finite field. This is equivalent to a "signature" in Bitcoin. 
Ergo uses the same [Secp256k1 curve of Bitcoin](https://en.bitcoin.it/wiki/Secp256k1), so the representation of `ecPoint` is the same, a 33-byte array with the first byte representing the sign (Ergo does not support uncompressed points). 
However, unlike Bitcoin (which uses ECDSA), Ergo uses Schnorr signatures to construct the proofs. 

The following steps illustrate how to create an address encoding the `proveDlog` script. 

1. First obtain the EC point corresponding to the public key. Let us use [the same example of Bitcoin](https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses).
    1. The hex-encoded BigInteger secret is `18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725`.
    2. The corresponding hex-encoded EC point is `0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352`.
    3. Convert the EC point hex to Base64, which turns out to be `AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS`.

2. Create the corresponding script `proveDlog(decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS")))`.

3. Compile the script [to get the address](https://wallet.plutomonkey.com/p2s/?source=cHJvdmVEbG9nKGRlY29kZVBvaW50KGZyb21CYXNlNjQoIkFsQ0dPdFpLaDY2S0wrZzhHdkdvUUR5MVAxUGtodGhSSGEyS0JJaCtXeU5TIikpKQ==) `LQ7iQ4egnCPsZZy5QKsXmaypCRuMxPNtdyGE95fYWCLze8C2hMMwDcAgPNeV8s`

Funds sent to the above address can be spent using the secret above, as can be seen in the transaction with id [dfca9eaa745c79dafbed43b73379fb0008608119080954c337a4022a2a5070a3](https://explorer.ergoplatform.com/en/transactions/dfca9eaa745c79dafbed43b73379fb0008608119080954c337a4022a2a5070a3). 