---
tags:
  - Data Model
---

# Tokens on Ergo

Tokens on Ergo have broad utility and can represent various assets such as shares, complementary currency units, or any imaginable item. Ergo's token infrastructure ensures seamless representation and transfer of diverse assets, empowering their integration into the blockchain as *first-class citizens*. 

However, ERG has two distinct characteristics compared to other tokens:

- ERGs cannot be burnt; the total input and output amounts must be equal.
- [Storage rent](rent.md) is payable exclusively in ERGs.

Tokens are stored in the `R2` [register](registers.md) of a [box](box.md), which holds pairs of `tokenId` and `amount`.

A box can contain at most 255 secondary tokens.

However, there are also some indirect limits:
- A box can be no more than 4 kilobytes
- Tokens add to the computational cost of the transaction.



