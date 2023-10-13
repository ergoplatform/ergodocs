# Decentralized Grid Trading

## Overview
Decentralized grid trading is a powerful concept implemented on the Ergo blockchain. It allows for automated trading orders while ensuring users maintain control over their funds. Two notable implementations of this concept are the Off the Grid and Machina Finance projects.

## Off the Grid
Explore the project [here](https://github.com/Telefragged/off-the-grid/)

Off the Grid is a decentralized application (dApp) that builds on the grid trading contract proposed by kushti. It includes an execution bot/batcher for automating order matching without user interaction.

Learn more about grid trading on [Investopedia](https://www.investopedia.com/terms/g/grid-trading.asp).

### Features

Off the Grid provides the following features:

- Utilizes a contract that permits spending only if orders are correctly filled or with the order owner's signature. This contract can manage multiple orders simultaneously.
- Employs off-chain bots/batchers to monitor grid orders and match them against other liquidity sources.
- Currently, it matches orders against Spectrum Automated Market Makers (AMMs). However, it can be extended to other sources like the SigUSD bank.
- Supports trading of ERG against any token, with profits accumulated in ERGs.
- Enables grid orders to profit from repeated execution of the same orders, while bot operators benefit from arbitraging the price difference between the liquidity source and grid orders.

This concept was introduced by `@kushti` on [ergoforum](https://www.ergoforum.org/t/decentralized-grid-trading-on-ergo/).

> "We can do decentralized grid trading on Ergo (which is automatically compatible with existing DEXes, such as Spectrum LP pools and babel fees). Grid trading is a good way to make profits from volatility, and many CEXes offer it."

Check out the [first decentralized grid order transaction on Ergo](https://twitter.com/chepurnoy/status/1582657292834861057).

## Machina Finance

Machina Finance is another project on the Ergo platform that is exploring the concept of grid trading. It is developing a decentralized exchange (DEX) that utilizes grid order contracts.

Explore the project [here](../eco/machina-finance.md)
