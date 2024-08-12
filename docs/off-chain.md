---
tags:
  - Off-Chain Bots
  - Off Chain Bots
  - Grid Bots
  - Dex Bots
  - Bots
---

# Off-Chain Bots

[ErgoDex off-chain services](dex_bots.md)


The Ergo ecosystem, known for its innovative approach to decentralized finance (DeFi), offers numerous opportunities for users to earn rewards not only through on-chain activities but also through off-chain mechanisms. This guide explores how participants can leverage off-chain earnings through roles such as watchers, oracles, and bots, contributing to the ecosystem's health while securing passive income.


## Watchers on Rosen Bridge

Watchers are integral to Rosen Bridge, serving as cross-chain oracles. They observe and report deposit events on their network to Ergo, contributing to the network's security and expansion.



### How to Become a Watcher:

1. **Technical Setup**: Running a watcher node requires a stable internet connection and a machine that meets the technical specifications detailed in [Ergo's documentation](https://docs.ergoplatform.com/eco/rosen/rosen-watcher/) for more information.
2. **Provide Collateral**: Each instance requires 800 ERG and 30,000 RSN as collateral. This collateral is fully redeemable and the amount is adjustable.
3. **Monitor Transactions**: Watchers need to continuously monitor cross-chain transactions, validating them according to the protocol's rules.
4. **Earn Rewards**: Successful watchers earn rewards in ERG, distributed according to their contributions to the network's security and operation.

### Estimated Rewards 
The following data represents an example of the reward distribution for a single watcher on the Rosen network within the period from January 22, 2024, to February 3, 2024. The actual rewards can vary based on the traffic on the bridge.

- ERG Watcher Rewards:  100.217 ERG
- ADA Watcher Rewards:  25.37 ADA
- Total Rewards (ERG + ADA):  125.59

Please note that these figures are subject to change and depend on the actual bridge traffic. The more traffic the bridge has, the higher the potential rewards for the watcher.


## Oracles: Empowering Ergo's dApps

Oracles play a pivotal role in DeFi by providing external data (e.g., price feeds) to smart contracts. Ergo's ecosystem utilizes oracles for various applications, including stablecoins and financial instruments.

> To join the existing Gold oracle pool, you will need a *Gold Pool Oracle Token*. These tokens are periodically made available through [auctions](https://ergoauctions.org/artwork/78263e5613557e129f075f0a241287e09c4204be76ad53d77d6e7feebcccb001), providing a fair and transparent process for potential participants.
{.is-warning}


#### Becoming an Oracle Provider:



1. **Data Source Integration**: Oracle providers need to integrate reliable data sources with the Ergo blockchain, ensuring the information is accurate and timely.
2. **Deploy Oracle Contracts**: Deploy smart contracts on Ergo that will serve as the interface for your data feeds.
3. **Maintain Reliability**: Continuous monitoring and maintenance are required to ensure your oracle remains reliable and trustworthy.
4. **Compensation**: Oracle providers are typically compensated by the users or contracts that rely on their data feeds, often through transaction fees or subscriptions. Operating an Gold oracle nets approximately 24 GORT (Gold Oracle Reward Tokens) per day. 


## Bots for Automated Trading and Order Matching

Decentralized grid trading is a powerful concept implemented on the Ergo blockchain. It allows for automated trading orders while ensuring users maintain control over their funds. Two notable implementations of this concept are the Off the Grid and Machina Finance projects.

Learn more about grid trading on [Investopedia](https://www.investopedia.com/terms/g/grid-trading.asp).


### Off the Grid

Off the Grid is a decentralized application (dApp) that builds on the grid trading contract proposed by kushti. It includes an execution bot/batcher for automating order matching without user interaction.

Explore the project [here](https://github.com/Telefragged/off-the-grid/)

Off the Grid provides the following features:

- Utilizes a contract that permits spending only if orders are correctly filled or with the order owner's signature. This contract can manage multiple orders simultaneously.
- Employs off-chain bots/batchers to monitor grid orders and match them against other liquidity sources.
- Currently, it matches orders against Spectrum Automated Market Makers (AMMs). However, it can be extended to other sources like the SigUSD bank.
- Supports trading of ERG against any token, with profits accumulated in ERGs.
- Enables grid orders to profit from repeated execution of the same orders, while bot operators benefit from arbitraging the price difference between the liquidity source and grid orders.

This concept was introduced by `@kushti` on [ergoforum](https://www.ergoforum.org/t/decentralized-grid-trading-on-ergo/).

> "We can do decentralized grid trading on Ergo (which is automatically compatible with existing DEXes, such as Spectrum LP pools and babel fees). Grid trading is a good way to make profits from volatility, and many CEXes offer it."

Check out the [first decentralized grid order transaction on Ergo](https://twitter.com/chepurnoy/status/1582657292834861057).

### Machina Finance

Machina Finance is another project on Ergo that is exploring the concept of grid trading. It is developing a decentralized exchange (DEX) that utilizes grid order contracts.

Explore the project [here](machina-finance.md)

### Other bots

- [HummingBot: Using Dashboard to Deploy and Backtest Strategies](https://hummingbot.org/academy-content/using-dashboard-to-deploy-and-backtest-strategies/)
- [KuPyBot](https://github.com/FlyingPig69/KuPyBot): A simply buy low sell high bot written in python using Kucoins python library.

## Best Practices for Off-Chain Earnings

- **Stay Informed**: Keep up-to-date with the latest developments in the Ergo ecosystem, including updates to protocols and new opportunities for off-chain earnings.  
- **Security**: Ensure your setup is secure, especially if you are handling private keys or large amounts of ERG.
- **Community Engagement**: Join Ergo's community forums and channels. Sharing insights and collaborating with others can enhance your strategies and impact.
- **Compliance**: Be aware of and comply with any legal or regulatory requirements applicable to your activities, especially when dealing with financial data or assets.

## Conclusion

Ergo's ecosystem offers diverse opportunities for off-chain earnings through roles like watchers, oracles, and automated bots. These positions not only provide ways to earn passive income but also contribute significantly to the functionality and security of the Ergo blockchain. By engaging with these opportunities, users can support the decentralized ecosystem while benefiting from its growth and success.