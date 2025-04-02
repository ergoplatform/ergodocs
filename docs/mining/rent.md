---
tags:
  - Storage Rent
  - Demurrage
  - Mining
  - Economics
---

# Ergo's Demurrage (aka Storage Rent)

Ergo's design emphasizes long-term economic sustainability. One of the key strategies to ensure this is the implementation of *'demurrage'* or storage rent. This mechanism, akin to 'on-chain garbage collection', not only mitigates the issue of blockchain bloat but also turns it into a profitable venture.

## Key Features

- Starting from block **1,051,200** (July 20th, 2023), miners can charge storage rent or fully spend the box if its value doesn't cover the rent.
- Storage fees serve as an additional source of rewards for miners, supplementing block and transaction rewards.
- By reducing the storage load, storage fees eliminate potential extra costs that could arise from excessive state growth.
- Storage fees stimulate coin circulation and deter deflation, thereby preventing illiquidity and congestion in the currency system.

## Understanding *'Demurrage'* 

Demurrage is a nominal fee levied on unspent output after four years. The fee per byte is determined by the _storage rent_ subprotocol. For a box without tokens and complex scripts, this amounts to approximately 0.14 ERG every four years. 

For a comprehensive understanding of the storage rent fees within the Ergo blockchain, including how these fees are calculated, applied, and adjusted over time, visit [this page](rent-fees.md).

## What About Tokens, NFTs, etc?

Ergo's demurrage mechanism rewards miners uniquely by allowing them to claim valuable assets within a UTXO if the ERGs available are insufficient to cover the rent. This principle applies to various assets, including NFTs and stablecoins like SigUSD, and promotes increased participation and active asset management. While it enhances network security and reduces blockchain bloat, it could lead to uninformed users inadvertently losing valuable assets if they fail to maintain enough ERGs. **Users are strongly advised to thoroughly understand Ergo's demurrage mechanism and ensure they possess enough ERGs to protect their valuable assets.** For more information, [click here](rent-tokens.md).

## How to Check the Age of Your Boxes? 

[TokenJay](token-jay.md) offers a convenient [Box consolidation tool](https://tokenjay.app/app/#boxconsolidation) that checks the number and age of boxes in your wallet and consolidates them when necessary. [Nautilus](nautilus.md) also features a built-in box consolidation tool that alerts you if your UTxO set requires consolidation. Alternatively, you can message [@ergoportbot](https://t.me/ergoportbot) on Telegram and use the command `/ep boxage ADDRESS` to check. 

## Additional Resources

- [How to consolidate a wallet](https://ergonaut.space/en/Guides/how-to-consolidate-a-wallet)
- [HF-4.0 Reduce storage rent period #1144](https://github.com/ergoplatform/ergo/issues/1144) - Rejected
- [EIP-0045 Redistribution contracts for Storage Rent Fees #93](https://github.com/ergoplatform/eips/pull/93)
- [EIP-39 Monotonic box creation height rule](https://github.com/ergoplatform/eips/blob/master/eip-0039.md)
- [EIP-33: Token burning during rent collection #68](https://github.com/ergoplatform/eips/pull/68)
- [Demurrage details (ergoforum)](https://www.ergoforum.org/t/storage-rent-details/256).
