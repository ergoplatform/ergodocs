---
tags:
  - Auction Coin
  - Token Issuance
  - Auctions
  - DeFi
  - Degen Finance
  - dApp
---

# Auction Coin: A Decentralized Token Issuance Model on Ergo Blockchain

Auction Coin is a decentralized token distribution protocol designed for fairness and trustlessness in the open market. It autonomously manages price discovery and offers several advantages:

- **Token Locking and Emission:** Tokens are initially locked in a smart contract, and emission occurs through periodic auctions, enhancing fairness and decentralization.

- **Token Distribution:** Teams can use Auction Coin for token distribution, ensuring fairness, decentralization, trustlessness, and improved price discovery, promoting community involvement and dApp adoption.

- **Liquidity Provider:** The protocol can generate liquidity for Liquidity Pools (LP) through periodic token auctions, offering advantages over traditional methods.

- **Raising Funds for Development:** Auctions' proceeds can support ongoing team development, aligning interests with project success and preventing market dumping.

- **Built on Existing Infrastructures:** Built upon established Auction infrastructure, it simplifies complexity and enhances versatility for various use cases.

- **Implementation:** The AuctionCoin token represents the initial implementation of this protocol, introducing an innovative financial game.

- **Game-Theoretic Interactions and DegFi:** The transparent nature of Auction Coin invites strategic plays, fostering "pure degen finance" (DegFi).

- **Tokenomics and Fee:** AuctionCoin supply is 100k in total, with allocations for the team, contributors, LP bootstrap, and locked with the main contract. A 3% operational fee from sold auctions supports development.

- **Emission Schedule:** Every 4 days, 10 batches of declining price auctions with a total of 1k AuctionCoins will start and last for 3 days, resulting in a one-year emission schedule.

The protocol offers a novel approach to decentralized token distribution and financial interactions on the Ergo blockchain. You can try it out at [auctioncoin.app](https://auctioncoin.app).

Join the discussion on [Telegram](https://t.me/auction_coin) or [Discord](https://discord.gg/ergo-platform-668903786361651200)

## How Auction Coin Functions

### Token Locking and Initialization

Initially, all newly minted Auction Coin tokens are securely locked within a smart contract, with only a small portion allocated to seed a liquidity pool. This liquidity pool becomes an integral component of the token's ecosystem, ensuring its liquidity.

### Token Auctions

At regular intervals of two days, equivalent to 1,440 blocks on the Ergo blockchain, a fixed quantity of AC tokens is made available for unlocking and subsequently placed into auctions. These auctions commence with predefined bid amounts, governed by the smart contract, and run for precisely one day (720 blocks).

### Dynamic Pricing

The initial bid for each auction is subject to dynamic adjustments. Following a successful auction, the starting bid for the subsequent auction increases by 1%. Conversely, if an auction fails to meet its objectives, the starting bid decreases by 1%. This dynamic pricing mechanism enhances adaptability and responsiveness to prevailing market conditions.

### Erg Accumulation and Token Buyback

Every 20 days or after the completion of 10 successful auctions, the smart contract utilizes the accumulated Ergs (the native token of the Ergo blockchain) to repurchase AC tokens from the liquidity pool. This automated process adheres to a predefined contract logic, mirroring established models for token buybacks from liquidity pools.

## Game-Theoretic Interactions and DegFi

The transparent and predictable nature of the Auction Coin mechanism stimulates a range of strategic interactions. Participants may choose to accumulate AC tokens in anticipation of a forthcoming buyback event, with the intention of selling them at a higher price following the smart contract's intervention. This sets the stage for what is often referred to as "pure degen finance" (DegFi), operating atop a transparent mechanism with well-defined assumptions.

## Resources

- [ergoforum: Auction Coin - auction-based emission and Degen Finance autonomous machine](https://www.ergoforum.org/t/auction-coin-auction-based-emission-and-degen-finance-autonomous-machine/4287)
- [Whitepaper](https://auctioncoin.app/assets/whitepaper.pdf)
- [Twitter](https://twitter.com/Auction_Coin)
- [Git](https://github.com/orgs/Auction-Coin/repositories)
