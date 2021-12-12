# Hierarchical keys


- [EIP-0003: Deterministic Wallet Standard](https://github.com/ergoplatform/eips/blob/ad0730daaebd9783f8db3c3095187a62851ee132/eip-0003.md)


## Derived Addresses

Since very early versions, the Ergo node uses a secret root key (derived from seed) for the *change* address. After switching to EIP-3, supported by CoinBarn and Yoroi around that time, the node switched to the same change address as in the wallets, thus deriving an address corresponding to `m/44’/429’/0’/0/0`.

[Read More](https://www.ergoforum.org/t/an-issue-with-change-address-of-node-wallet/2940)