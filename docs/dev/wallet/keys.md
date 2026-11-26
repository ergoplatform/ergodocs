---
owner: docs
last_reviewed: 2026-11-26
source_repos:
  - repo: satoshilabs/slips
    branch: master
    paths:
      - slip-0044.md
source_of_truth:
  - https://github.com/bitcoin/bips/tree/master/bip-0044.mediawiki
  - https://github.com/satoshilabs/slips/tree/master/slip-0044.md
  - https://github.com/satoshilabs/slips/commit/cb1f56dd8cd1f8488f7e18357b06922d4fa90259
  - https://github.com/satoshilabs/slips/commit/b7fb1b681c4ebf074bd285454c04e5eb73e44963
  - https://github.com/satoshilabs/slips/commit/c93705964102594e0f153c901acbb7f4faeaab40
---

# Hierarchical keys

[BIP-0044](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) defines a logical hierarchy for deterministic wallets. This is a common standard that is used directly (or used as inspiration) by countless projects in the cryptocurrency sphere.

Such a standard allows end users to move between different wallet software trivially and established the framework for a more cohesive ecosystem to grow.

The standard has five levels as part of its path:

```bash
m / 44' / coin_type' / account' / change / address_index
```

[EIP-0003: Deterministic Wallet Standard](https://github.com/ergoplatform/eips/blob/ad0730daaebd9783f8db3c3095187a62851ee132/eip-0003.md) attempts to define a specific `coin_type` for the Ergo ecosystem, as well as a policy for how wallets use the `change` level.

## Coin Type

Registered **coin_type**s can be found in [SLIP-0044](https://github.com/satoshilabs/slips/blob/master/slip-0044.md)

SLIP-0044 is a live registry, not a fixed table: entries and tickers continue to be added and corrected. For example, the current registry lists `OAG` (Orange) at coin type `1033` and `QTC` (Quantus Network) at `189189`; the Quantus ticker was updated from `QUAN` to `QTC`. Check the linked registry for the current entry before relying on an older snapshot. Ergo remains `429` in EIP-0003.

We will be using the word **ergo** summed based on the numerical values of the ASCII characters for the **coin_type**. As shown below, this means that our **coin_type** is `429`.

```text
101 + 114 + 103 + 111 = 429
```

Thus our path will look as such:

```bash
m / 44' / 429' / account' / change / address_index
```

And the first default key pair for an Ergo wallet will be:

```bash
m / 44' / 429' / 0' / 0 / 0
```

## Change

In BIP-44 the constant 0 is used for the external addresses and constant 1 for internal addresses (aka change addresses).

For EIP-3, we instead do not use constant 1 at all. Thus we do not support internal/change addresses, but only external addresses.

As such all wallets supporting EIP-3 should have any change within a transaction go back to the address using constant 0.

This decision was made to simplify the experience for end-users and solidify a cohesive standard for wallets to target in the Ergo ecosystem. A full-blown privacy-preserving mixer is already available within the ecosystem, ErgoMix, and thus the pseudo-anonymity provided by internal addresses is not particularly vital.

That said, in the future new wallets are more than welcome to create a new EIP for wallets that may wish to support internal addresses as well as an alternate standard (if valuable use cases arise).

## Derived Addresses

Ergo node uses a secret root key (derived from seed) for the *change* address. After switching to EIP-3, supported by CoinBarn and Yoroi around that time, the node switched to the same change address as in the wallets, thus deriving an address corresponding to `m/44’/429’/0’/0/0`. (originally `m/1/2`)

[Read More](https://www.ergoforum.org/t/an-issue-with-change-address-of-node-wallet/2940)

## Deriving Addresses

Navigate to `localhost:9053/swagger#/wallet/walletDeriveKey`

Click ***"Try it out"***

```bash
"derivationPath": "m/44'/429'/0'/0/0" 
```

- The wallet needs to be unlocked, and you need to authorize on top right on swagger
- Click execute and check the address you get in the response
