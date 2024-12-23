## Off the Grid

Off the Grid is a decentralized application (dApp) that builds on the grid trading contract proposed by kushti. It includes an execution bot/batcher for automating order matching without user interaction.

Explore the project [here](https://github.com/Telefragged/off-the-grid/) and check out our [Getting Started Guide](off_the_grid_tut.md).

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