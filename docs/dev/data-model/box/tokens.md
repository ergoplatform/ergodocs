---
tags:
  - Data Model
---

# Tokens on Ergo

In the Ergo ecosystem, custom tokens are treated as first-class citizens. These tokens are stored in the `R2` [register](registers.md) of a [box](box.md), which holds pairs of `tokenId` and `amount`.

However, Ergs (the native cryptocurrency) have distinct characteristics compared to other tokens:

1. ERGs cannot be burnt; the total input and output amounts must be equal.
2. [Storage rent](rent.md) is payable exclusively in ERGs.

Ergo allows up to **255** secondary tokens per box or transaction, but there are restrictions to consider. Boxes cannot exceed **4** kilobytes in size, and adding tokens increases the computational cost estimation of transactions.

Tokens on Ergo have broad utility and can represent various assets such as shares, complementary currency units, or any imaginable item. Ergo's token infrastructure ensures seamless representation and transfer of diverse assets, empowering their integration into the blockchain as first-class citizens.