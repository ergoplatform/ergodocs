---
tags:
  - Options Trading
  - SigmaO
  - DeFi
  - Tutorial
  - Guide
---

**Ergo's decentralized finance (DeFi) landscape is about to expand with the introduction of SigmaO, a pioneering platform designed to facilitate options trading on the Ergo blockchain. SigmaO aims to leverage Ergo's unique capabilities to offer a versatile and secure environment for trading options, enhancing the financial instruments available within the Ergo ecosystem.**

## **What are Options?**

Options are like contracts that give you the choice to buy or sell something (like stocks or cryptocurrencies) at a fixed price before a certain date. There are two main types:

- **Call Options:** These let you **buy** something at a set price in the future.
- **Put Options:** These let you **sell** something at a set price in the future.

**How are Options Used?**

- **Hedging:** Imagine you own Ergo tokens and are worried their value might drop. You could buy a put option, which gives you the right to sell your Ergo tokens at a fixed price, protecting you from losses if the price falls.
  
- **Speculation:** Let's say you believe the price of Ergo tokens will increase soon. You could buy a call option, allowing you to purchase Ergo tokens at a set price in the future. If the price goes up, you can buy them at the lower price stated in the option and then sell them at the higher market price, making a profit.
  
- **Generating Income:** Alternatively, you could sell a call option if you don't think Ergo's price will rise significantly. You'll receive money upfront for selling the option, and if the price stays below the agreed price, you keep the money without having to sell any tokens.


**Learning More:**

- [Beginner's Options Course](https://learn.tastylive.com/courses/beginner-options-course)
- [The Options Playbook](https://www.optionsplaybook.com/option-strategies/)

## What is SigmaO?

SigmaO is an innovative platform that brings the complex world of options trading to the Ergo blockchain, allowing users to engage in call and put options across a variety of Ergo EIP-4 tokens. With a focus on accessibility and security, SigmaO is poised to become a key player in Ergo's DeFi offerings. For an insightful presentation on Sigma'O features, watch the video titled "[Sigma'O | Ergo Summit - Cypherpunk Finance](https://www.youtube.com/watch?v=a1f0F24Ld9w)" by Haileypdll.

**Website:** [sigmao.cc](https://www.sigmao.cc/)
**About:** [sigmao.cc/about](https://www.sigmao.cc/about)
**Twitter:** [SigmaOptions](https://twitter.com/SigmaOptions)
**Explainer Article:** [SigmaO Options on Ergo Tokens](https://medium.com/@Haileypdll/sigmao-options-on-ergo-tokens-18adaa098416)
**GitHub:** [ThierryM1212/sigmao](https://github.com/ThierryM1212/sigmao)
**SigmaO Telegram chat:** [t.me/SigmaOpts](https://t.me/SigmaOpts)
## How Does SigmaO Work?

SigmaO plans to make options trading accessible by providing a platform where users can easily create and trade options. The platform utilizes Ergo's smart contracts to ensure transactions are secure and efficient. Pricing mechanisms for these options are derived from Spectrum Liquidity Pools, providing transparent and fair valuation.

> Join qx() as he takes you through a [one shot no edits no nonsense take on how to do options trading on Ergo!](https://youtube.com/watch?v=XoJT7aR7o4w) This is only for buying call options, more videos to come with how to execute the call, and create calls and puts. 
{.is-success}


## The Benefits of Trading Options on SigmaO

- **Hedging**: SigmaO offers traders the ability to hedge their investments, protecting against market volatility and minimizing potential losses.
- **Speculation**: Traders can speculate on the future price movements of various tokens, with the potential for high returns.
- **Accessibility**: By simplifying the options trading process, SigmaO makes sophisticated financial strategies available to a broader audience.
- **Security**: Leveraging Ergo's blockchain technology, SigmaO ensures that all trades are secure and transparent.

## Understanding Sigma'O: Simplified Explanation

Sigma'O is a decentralized application (dApp) built on the Ergo blockchain. It was initially developed for the Ergohack VI event and is now available for testing at [sigmao.cc](https://www.sigmao.cc/).

**What Sigma'O Does:**

- **Token Creation**: It allows users to create standard EIP-4 tokens, representing the value of an option on another Ergo EIP-4 token.
- **Trading Platform**: Sigma'O provides contracts for trading Ergo tokens and Sigma'O options in an order book style exchange.
- **Permissionless Contracts**: All contracts used by Sigma'O are permissionless, meaning developers and UIs interacting with Sigma'O contracts do not have any privileges. There's no updatable configuration by an "app owner."

**Option Contracts:**

- **Type**: Sigma'O options can be either Call (grant to buy an underlying token) or Put (grant to sell an underlying token).
- **Style**: They can be American (exercisable up to the maturity date) or European (exercisable during 24h after the maturity date).
- **Share Size**: Represents the number of tokens granted per option.
- **Strike Price**: The price of the underlying asset when exercising the option.
- **Maturity Date**: The end of the grant of the option.



**Minting Option Tokens:**

When Sigma'O options are created, a reserve is ensured to allow for the option's exercise.

**Exercising Options:**

- Exercising an option burns the options used, as the associated reserve is consumed.
- The exercise period depends on the type of option (American or European) and the exercise type (Call or Put).

**Order Book Trading:**

Sigma'O implements "Open sale order" and "Open buy order" contracts for trading options and tokens. These contracts are refundable at any time to the issuer and ensure fair trading.

**Priced Sell Contracts:**

Sigma'O also supports priced sell options for options on an underlying token with an Oracle price or Spectrum liquidity pool. This allows for real-time pricing based on market conditions.

- **Exact Formula:** The exact computation implemented in Ergoscript and JS can be found [here](https://github.com/ThierryM1212/SigmaO/blob/main/front-end/src/utils/utils.js#L98) and [here](https://github.com/ThierryM1212/SigmaO/blob/main/contract/Option_Sell.es#L107).


**Future Developments:**

The SigmaO team is dedicated to enhancing the platform with user-friendly interfaces and off-chain bots for efficient transaction processing. This will not only improve the trading experience but also contribute to the overall liquidity and dynamism of Ergo's DeFi ecosystem.
 
## Examples

- **Gold Oracle Token Option:**
  - An opportunity was presented for users to engage in European options for gold oracle tokens. These options allowed participants to speculate on the future price of gold oracle tokens by acquiring the option for a set ERG amount and exercising it before a specified date with a predetermined strike price. This mechanism enabled users to potentially capitalize on price movements within the given timeframe. [View Option Details](https://www.sigmao.cc/)

- **GORT Token Option:**
  - Options were introduced for GORT tokens, providing users with the ability to speculate on its price dynamics. Participants could purchase a predetermined amount of GORT at the current price within a specified time frame by investing a set amount of ERG. If the price of GORT increased during this period, users could exercise the option, acquiring GORT at the initial price and potentially profiting from the price difference. Conversely, if the price remained stagnant or decreased, users could choose not to exercise the option, limiting their loss to the initial investment. This mechanism served as a tool for hedging against market volatility and exploring potential profit opportunities. [View Option Details](https://www.sigmao.cc/option-details/3ebf26d359b339fcbd04de777cc712d1f451afcbd8b5b79d97b5b5ff71aa017f)
  
- **Innovative Options Experiment:**
	- A creative exploration within the SigmaO ecosystem showcased the creation of four option packages, each displaying the price and expiration date prominently. These options were designed to degrade in price over time, reflecting market conditions and providing an incentive for timely decision-making. Purchasing the option offered the right to buy the underlying asset (Ada) at a predetermined price within a specified timeframe, enabling speculation on potential price movements without immediate commitment. This experiment highlighted the versatility and potential of SigmaO on the Ergo blockchain, leveraging real-time pricing data to create attractive option packages for potential buyers.
