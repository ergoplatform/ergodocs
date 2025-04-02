
---
tags:
  - OptionPools
  - Options Trading
  - DeFi
  - AMM
  - dApp
---

# OptionPools: Unleashing the Power of Ergo for Decentralized Options Trading

## Introduction

OptionPools is a groundbreaking pool-to-peer Automated Market Maker (AMM) trading protocol designed to bridge the gap between traditional finance and decentralized finance (DeFi) in the realm of options trading. Built on the robust Ergo blockchain, OptionPools leverages Ergo's unique capabilities to create a secure and efficient platform for trading options directly on Layer 1.

## The Motivation Behind OptionPools

Despite the prevalence and importance of options in traditional finance, their adoption in DeFi has been limited, accounting for less than 0.2% of the total DeFi Total Value Locked (TVL) according to DeFi Llama. This lack of adoption can be attributed to several factors, including:

1. **High Risks**: Existing DeFi options protocols are often built on Layer 2 solutions, relying on third-party oracles and complex smart contracts, leading to potential exploits and deterring institutional engagement due to security concerns.

2. **Liquidity Challenges**: DeFi options face liquidity challenges, exacerbated by the high risk and capital inefficiency of their structures. While order books in DeFi are typically fully collateralized and AMMs may be partially collateralized, traditional finance systems often operate with significant undercollateralization, allowing more options to be created with less capital.

3. **Performance Bottlenecks**: On Layer 1 networks like Ethereum, option pricing is extremely gas-intensive, pushing most activities to Layer 2. Even on Layer 2, costs remain higher for DeFi options compared to their traditional finance counterparts due to liquidity provider protection measures and additional expenses, such as those incurred from using third-party oracles or additional contract interactions.

## Ergo: The Solution to DeFi Options Challenges

Ergo provides a solution to the shortcomings of existing DeFi options protocols. By leveraging Ergo's unique UTXO model and superior performance, OptionPools can be built directly on Layer 1, minimizing the set of risk assumptions and potential attack surfaces. Contracts on Ergo are primarily used to verify outputs rather than execute complex computations, reducing the risk of vulnerabilities.

Furthermore, Ergo's high performance allows for on-chain option pricing using the Black-Scholes model, a feat that was demonstrated during the ErgoHack event. By integrating directly with duckpools for undercollateralized lending, OptionPools can offer capital-efficient options trading, addressing the liquidity challenges faced by existing DeFi options protocols.

## Key Components of OptionPools

The OptionPools submission for the ErgoHack event consists of a comprehensive suite of smart contracts, off-chain code, and a user interface tailored for ERG/SigUSD optionPools. This framework is adaptable to other pairs like ERG/rsBTC or SigUSD/rsBTC.

### Smart Contracts

OptionPools includes specific contracts for managing the AMM, options logic, repayments, and proxy interactions. These contracts can be found in the following repository: [https://github.com/duckpools/off-chain-bot/tree/optionPools/optionPools/contracts](https://github.com/duckpools/off-chain-bot/tree/optionPools/optionPools/contracts)

### Off-Chain Code

The off-chain code, implemented in Python, handles various aspects of the OptionPools platform. While the current implementation may require improvements before production, it can be found in the following repository: [https://github.com/duckpools/off-chain-bot/tree/optionPools/optionPools](https://github.com/duckpools/off-chain-bot/tree/optionPools/optionPools)

### User Interface

A user-friendly website hosts the OptionPools platform, allowing users to interact with the smart contracts and off-chain code. During the video submission, the team demonstrated the successful addition, withdrawal, buying, and selling of both call and put options using the website.

## Innovative Features

OptionPools introduces several innovative features to the DeFi options market:

### Dual-Asset Pools

OptionPools supports dual-asset liquidity provisioning, a novel feature in the DeFi options market. Pools do not need to maintain market ratios of asset pairs and can earn fees in one side or both sides of a pair. This flexibility allows liquidity providers (LPs) to adopt varied investment stances—bullish, neutral, or bearish—by choosing which pools they contribute to.

### Black-Scholes Pricing Model

The team successfully implemented the Black-Scholes pricing model directly into the OptionPools contracts, demonstrating the feasibility of on-chain option pricing on Layer 1. The pricing outputs were reasonably precise, with the d1 and d2 values from the model being extremely accurate. However, there is still room for improvement in the precision of the Cumulative Distribution Function (CDF) data input for practical use.

### Options Price Adjustment Based on Real-Time Utility

OptionPools incorporates the ability to adjust option prices based on the real-time utility of the pool. The more option contracts are circulating (higher utility), the more expensive the option price paid by the trader. This feature enables the pools to reflect real-time sentiment on an option's price, which might not be captured by historical volatility alone. In the current implementation, the team simply multiplied the price by the utility, but more nuanced algorithms could be employed in the future.

## Limitations and Future Goals

While the OptionPools submission for the ErgoHack event showcases the potential of Ergo for decentralized options trading, there are several limitations and future goals to be addressed:

- **Multiple Strikes**: The current implementation supports only a single strike for calls and puts. Expanding this to allow custom strikes dynamically priced by the pool is a planned enhancement.

- **Delta Neutral Strategy**: Future iterations will incorporate delta neutral strategies by aggregating 'd1' values from all options, improving AMM pricing accuracy and risk management. Since the team already calculates d1 in their contracts, this is a relatively simple extension.

## Final Remarks

During the ErgoHack event, the OptionPools team introduced several innovations that enrich the Ergo ecosystem, including useful math functions, a historical volatility oracle, and an entire pool-to-peer options trading platform. They demonstrated technical innovation with their implementation of on-chain Black-Scholes options pricing and packed numerous features into the week of development, such as dual-asset liquidity pools and options price adjustments based on pool utility.

The OptionPools project underscores the potential of Ergo to become a cornerstone in the DeFi options space, providing a compelling reason to bridge Bitcoin into the Ergo ecosystem and leverage its DeFi capabilities. The team welcomes any questions regarding their submission and is more than happy to assist in the duckpools Discord.

[KrasaviceBlasen and the duckPools team present their development of optionPools on Ergo. optionPools can be built on Ergo because it is far more performant than other L1s, and offers a minimized set of risk assumptions.](https://www.youtube.com/watch?v=gJQiAB7H8J4)
