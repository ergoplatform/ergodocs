---
tags:
  - Data Model
---

# Ergo Tokens

Ergo tokens are incredibly versatile and can represent a wide range of assets, including shares, complementary currency units, and various tangible or intangible items. The infrastructure of Ergo is designed to seamlessly handle the representation and transfer of these diverse assets, integrating them into the blockchain as *first-class citizens*.

It is crucial to understand that ERG, the native token of Ergo, possesses two unique characteristics:

- ERGs are non-destructible; the total input and output amounts in any transaction must be equal.
- [Storage rent](rent.md) can only be paid in ERGs.

Tokens in Ergo are stored in the `R2` [register](registers.md) of a [box](box.md). Each box holds pairs of `tokenId` and `amount`. allowing for the representation of multiple tokens within a single box. A single box has the capacity to hold up to 255 secondary tokens.
However, there are some indirect constraints to consider when working with tokens in Ergo:

- The size of a box cannot exceed 4 kilobytes, ensuring efficient storage and processing of token-related data.
- The presence of tokens increases the computational cost of a transaction, as additional calculations are required to handle the token-related operations.



