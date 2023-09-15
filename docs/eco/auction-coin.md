---
tags:
  - dApp-InDev
---

# Auction Coin: An Autonomous, Decentralized Token Issuance Model

Auction Coin (AC) represents a novel way of issuing tokens autonomously and in a decentralized manner on the Ergo blockchain. By employing smart contracts as its core engine, Auction Coin simulates a digital commodity—akin to digital gold—but with unique and dynamic properties. This concept not only opens up avenues for asset issuance but also sets up an interesting game-theoretic environment that invites human interaction, offering a variant of decentralized finance, or "DegFi."

## How Auction Coin Works

### Token Locking and Initialization

Initially, all new Auction Coin tokens are locked in a smart contract, except for a few that are used to seed a liquidity pool. This pool is referenced in the contract, making it a part of the token's ecosystem.

### Token Auctions

Every two days, corresponding to 1,440 blocks on the Ergo blockchain, a fixed quantity of AC tokens can be unlocked. These unlocked tokens are then put up for auction. The auction starts with a bid amount predefined by the smart contract and runs for one day (720 blocks).

### Dynamic Pricing

The starting bid for the auction can adjust dynamically. If the previous auction was successful, the starting bid for the next auction increases by 1%. Conversely, if the auction was not successful, the starting bid decreases by 1%. This dynamic pricing mechanism adds an element of adaptability and responsiveness to market conditions.

### Accumulating Ergs and Buying Back Tokens

Every 20 days, or after 10 successful auctions, the smart contract uses the accumulated Ergs (the native token of the Ergo blockchain) to buy AC tokens back from the liquidity pool. This process is automated and follows specific contract logic similar to existing models for buying back tokens from liquidity pools.

## Game-Theoretic Interactions and DegFi

The transparent and predictable nature of the Auction Coin mechanism invites various strategic plays. For instance, participants might choose to accumulate AC tokens before an expected buyback to sell them at a higher price after the smart contract's intervention. This sets the stage for "pure degen finance" (DegFi), which operates on top of a transparent mechanism with known assumptions.

## Resources

- [ergoforum: Auction Coin - auction-based emission and Degen Finance autonomous machine](https://www.ergoforum.org/t/auction-coin-auction-based-emission-and-degen-finance-autonomous-machine/4287)