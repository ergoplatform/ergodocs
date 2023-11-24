# Royalties

Ergo's royalty system is integrated into the minting `metadata` and can be accessed via smart contracts. This integration allows marketplaces to include royalties in their sale contracts, a feature utilized by both Sky Harbor and Auction House. Consequently, any listings on a marketplace that respects royalties will have the royalties embedded in their smart contract, preventing them from being bypassed.

/// admonition | Not enforced by the protocol
    type: warning

However, it's important to note that NFTs can be transferred directly from one party to another, similar to transferring across addresses. In these cases, or in private sales, the decision to honor the royalties lies with the involved parties.
///


The upcoming AuctionHouse V3 will introduce the ability to support multiple recipients for royalties. This feature will facilitate collaborations among artists.

## Resources

- [EIP-0022: Auction Contract](eip22.md)
- [EIP-0024: Artwork Contract](eip24.md)
