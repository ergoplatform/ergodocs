---
tags:
  - Data Model
---

# Ergo Tokens

Ergo tokens are versatile and can represent a wide range of assets, including but not limited to shares, complementary currency units, and other tangible or intangible items. The infrastructure of Ergo ensures a smooth representation and transfer of these diverse assets, integrating them into the blockchain as *first-class citizens*. 

It's important to note that ERG, the native token of Ergo, has two unique characteristics:

- ERGs are non-destructible; the total input and output amounts in any transaction must be equal.
- [Storage rent](rent.md) can only be paid in ERGs.

Tokens in Ergo are stored in the `R2` [register](registers.md) of a [box](box.md). Each box holds pairs of `tokenId` and `amount`.

A single box can hold up to 255 secondary tokens.

There are also some indirect constraints to consider:
- The size of a box cannot exceed 4 kilobytes.
- The presence of tokens increases the computational cost of the transaction.




