---
tags:
  - UTXO
  - Atomic Swaps
---

# Atomic Swaps

Atomic Swaps are a revolutionary technology that enables direct interaction between different blockchain systems. They facilitate the transfer of digital assets across chains without the need for centralized exchanges.

Blockchain technology is excellent at facilitating secure and efficient decentralized transfers within its network. For instance, Bitcoin (BTC) can be safely and quickly sent to any Bitcoin address, and the same is true for Litecoin (LTC) or any other cryptocurrency within its network.

However, the structure of a blockchain, built around the consensus among miners, isn't inherently designed to communicate with other blockchain systems. Consequently, transferring assets between different blockchain networks has traditionally involved third-party intermediaries like exchanges or Over-The-Counter (OTC) desks, which can introduce additional risks and inefficiencies.

## Cross-chain Swaps

Atomic swaps offer a solution to this challenge, enabling a secure and efficient cross-blockchain trade of cryptocurrencies. This innovative approach facilitates a direct, trustless exchange of assets. Here's a simplified step-by-step overview of how they work:

1. Alice and Bob agree to trade their cryptocurrencies. Alice will send 1 BTC to Bob, and in return, Bob will send Alice 50,000 ERG. As neither party trusts the other completely, both are hesitant to send their assets first.
2. Alice creates a secret - a unique, random number - and generates its hash. She then creates a transaction on the Bitcoin blockchain, attaching a script to lock her 1 BTC. This script specifies a condition: when the original secret (pre-image) of the generated hash is revealed, the locked BTC will be transferred to Bob's address. The hash can be safely included in the script, as the original secret cannot be deduced from it.
3. In response, Bob sets up a similar transaction on the Ergo blockchain, locking 50,000 ERG with a script containing the same hash Alice used. However, without the original secret, he can't execute Alice's transaction.
4. After confirming Bob's transaction on the Ergo blockchain, Alice can reveal the secret and execute Bob's transaction. With the original secret now in the open, Bob can also execute the script to receive his BTC.
5. Once published on the blockchain, neither Alice nor Bob can delete their transactions or scripts. However, they may set a time limit on the transactions to prevent their coins from being locked indefinitely if the secret isn't revealed within the set time.

## The Ergo Advantage in Atomic Swaps

Traditional atomic swaps operate on a binary execution principle - the transactions are either completed in full or not executed at all. This property makes them analogous to 'fill-or-kill' orders in conventional trading environments. While this ensures trustless exchange of assets, it lacks the flexibility found in a dynamic, conventional exchange environment.

Ergo enhances the existing atomic swaps concept by leveraging its unique eUTXO (Extended Unspent Transaction Output) model, a significant evolution over the conventional UTXO model found in Bitcoin-like blockchains.

The eUTXO model allows each UTXO to carry arbitrary data and to be protected by an arbitrary predicate (or spending condition). The data can be used to represent arbitrary tokens or smart contract states, while ErgoScript can implement complex logic akin to Ethereum smart contracts.

In the context of atomic swaps, Ergo utilizes the advanced capabilities of the eUTXO model to support not just the trustless swapping of coins or custom tokens across different blockchains, but also the ability to partially fill orders, tailored to the trader's preference.

This feature is implemented by coding a special type of smart contract into a UTXO's ErgoScript, enabling a UTXO to be split into several smaller ones while keeping the smart contract's state intact. This effectively allows for partial order fulfillment, flexibility unheard of in traditional atomic swaps.

By enabling this, Ergo provides the infrastructure for a fully decentralized exchange (DEX) supporting cross-chain trading. This Ergo-based DEX operates without intermediaries, eliminating the need for mechanisms like gateways or token wrapping often required in other blockchain platforms. This significantly reduces potential bottlenecks and points of failure, thereby promoting a secure and seamless trading environment.

## Python example

Below is a Python-based illustration adapted from [atomicswapexample](https://github.com/dzyphr/atomicswapexample) showing an atomic swap scenario between two parties - Alice (p1) and Bob (p2), which uses the secp256k1 elliptic curve.

The secp256k1 curve is imported as below:

```python
import collections
import hashlib
import random
import binascii
import sys
import libnum
from ECC import *

EllipticCurve = collections.namedtuple('EllipticCurve', 'name p a b g n h')

curve = EllipticCurve(
    'secp256k1',
    p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    a=0,
    b=7,
    g=(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    h=1,
)
```

The starting point is Alice and Bob generating their own key pairs:

```python
p1SecretKey, p1PublicKey = gen_keypair()
p2SecretKey, p2PublicKey = gen_keypair()
```

The `gen_keypair` function randomly selects a private key and computes the corresponding public key. This is done using the secp256k1 curve.

Next, both Alice and Bob select secret random values which are not reused:

```python
rs = random.randrange(0, curve.n) # Alice's secret
rr = random.randrange(0, curve.n) # Bob's secret
```

They then generate additional values using these secrets:

```python
rsG = scalar_mult(rs, curve.g)
rrG = scalar_mult(rr, curve.g)
```

These new values, `rsG` and `rrG`, are the result of the secrets `rs` and `rr` respectively being multiplied by the curve generator. This operation uses elliptic curve scalar multiplication, which essentially means that the curve's generator point is added to itself `rs` or `rr` times.

The process goes on with both parties exchanging generated values and computing additional shared secrets, performing operations on their secrets, and using hashes to secure the integrity of the transaction. The code simulates both parties acting in turns to finalize the atomic swap.

Additionally, they also verify that the computed keys and secrets are valid and fulfill the conditions of the swap. This includes checking that certain values are equal as well as confirming that the correct funds are locked in the smart contract:

```python
assert(check == sr_G)
```

```python
if (vr1[0]==vr2[0]):
    print(vr1[0], "==", vr2[0])
    print ("Success!")
else:
    print ("Failure!")
```



Once all the conditions are met, Alice can spend her value locked in the contract, thus finalizing the atomic swap:

```python
print("Alice can now spend value locked to hash/public pair xG with x and their signature")
```

It's important to note that this is a simplified illustration. In a real-world scenario, multiple additional layers of complexity and security would be required, including secure communication channels for the participants, comprehensive error handling, and transaction fees considerations.

For a more comprehensive understanding of Ergo’s atomic swaps and the possibilities they offer for intra-chain and cross-chain token swaps, refer to the [ErgoScript white paper](https://ergoplatform.org/docs/ErgoScript.pdf).

