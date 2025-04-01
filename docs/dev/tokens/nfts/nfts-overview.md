# Non-Fungible Tokens on Ergo

## Overview

*Non-Fungible Tokens* (NFTs) are unique and indivisible blockchain tokens. They can be used to represent and prove ownership of digital products such as works of art, in-game items or characters, virtual trading cards and much, much more.

## Frequently Asked Questions

//// details | Frequently Asked Questions
    {type: note, open: true}
/// details | How do I mint a NFT?
    {type: note, open: false}
Minting a NFT on Ergo is a straightforward process that can be done programmatically or using resources listed in our guide. Learn more about it [here](create.md).
///
/// details | How do royalties work?
    {type: note, open: false}
Royalties in Ergo are integrated into the minting metadata and can be accessed via smart contracts, allowing marketplaces to include royalties in their sale contracts. Find out more [here](royalties.md).
///
////

## Use cases

### Unforgeable identity

Let’s say you create a phenomenally successful exchange dApp, which pays a small percentage of trading fees to the owner – designated by ownership of that NFT. That token, and future revenues, can now be transferred and sold. The token can also be managed by a secondary smart contract, which could divide revenues among 100 tokens representing shareholders. The NFT could be used to update the dApp, or shut it down, if necessary – whatever conditions were coded into it. The point is that the NFT provides guaranteed, unforgeable proof of identity.



### UTXO NFTs

One interesting feature is that Ergo can be used to create [PoW-backed NFTs](PoW_tokens.md). For most NFTs, a user simply generates a UTXO with the token contract attached. But it’s also possible for miners to create special NFTs, where the id of the newly minted token is the id of a coinbase transaction. This has all kinds of potential use cases, but the core idea is that a miner has the opportunity to create a special NFT when they mine a block. While any number of NFTs can be created via a regular smart contract, a finite number of these PoW-backed NFTs can exist.

There are other applications of NFTs that use the extended UTXO model, including facilitating a new generation of complex dApps. For example, a dApp creator can generate an NFT associated with an address and smart contract. While anyone can use that contract, and even create a transaction using the private key of that address, the NFT owner can still maintain administrative rights or other privileges.
