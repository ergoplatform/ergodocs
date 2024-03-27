# SigmaUSD

SigmaUSD, the first eUTxO-based stable coin, is an implementation of the [AgeUSD protocol](https://github.com/Emurgo/age-usd). It was designed by IOHK, Ergo, and Emurgo with an economic model that maintains conservative settings for collateral reserves, thus avoiding the need for liquidations. It supports a fully decentralised stablecoin emission setup, offering the world a stable, simple, and decentralised stablecoin.

## Overview 

**Reserve providers** submit ERGs to the dApp's reserves to mint *reserve coins* (**SigmaRSV**), each representing a portion of the underlying ERG reserves held. **SigmaUSD** users also submit ERGs to the dApp reserves to mint SigmaUSD, provided sufficient reserves are within the dApp. SigmaUSD users can redeem their SigmaUSD for an amount of ERGs from the reserves equal to the current exchange rate as sourced by the ERG-USD [oracle pool](https://explorer.ergoplatform.com/en/oracle-pool-state/ergusd). 

Reserve Providers can redeem their *reserve coins* for ERGs if the price of ERGs goes up (or a substantial amount of protocol fees are collected) and thus cover the value of all existing minted SigmaUSD plus an extra margin. By doing so, they profit as they receive more underlying reserve cryptocurrency than when they minted their *reserve coins*.

**SigmaUSD** Users also submit ERGs to the dApp reserves; however, in their case, they mint SigmaUSD instead. The protocol only allows this if sufficient reserves are within the dApp (reserves are above the minimum reserve ratio). At any given moment, a SigmaUSD user can redeem their SigmaUSD in exchange for an amount of ERGs from the reserves equal to the current exchange rate as sourced by the ERG-USD [oracle pool](https://explorer.ergoplatform.com/en/oracle-pool-state/ergusd). 

## Where can I buy SigmaUSD?



- [Tokenjay.app](https://tokenjay.app/)
- [SigmaUSD.io](https://www.sigmausd.io)
- ErgoMixer
- Minotaur Wallet
- Spectrum.fi


## How does the reserve work? 

SigmaUSD operates on larger margin requirements than traditional crypto-backed stablecoins. ERG backs SigmaUSD in a floating reserve between 4x1 to 8x1. The minimum threshold (4x1) protects SigmaUSD holders, ensuring sufficient ERG ALWAYS backs tokens for market volatility. The maximum threshold (8x1) protects SigmaRSV holders from experiencing unnecessary dilution of their P/B position, limiting inflationary pressures. SigmaUSD has locking mechanisms to keep the Reserves within this range, which may temporarily prevent users from interacting with the contract. This is the alternative to forced liquidations.

## I don't understand SigmaUSD - Where can I find more information?

![sigmausd_overview.png](sigmausd_overview.png)


## Contract Locks

![photo_2021-05-19_10.01.10.jpeg](photo_2021-05-19_10.01.10.jpeg)

![photo_2021-05-26_01.56.49.jpeg](photo_2021-05-26_01.56.49.jpeg)


## Is there any technical documentation?

![screenshot_2021-02-25_at_19.14.01.png](screenshot_2021-02-25_at_19.14.01.png)


## What is the *Bearwhale*?

- [Bearwhale Saga](https://ergoplatform.org/en/blog/2021-05-13-bearwhale-saga/)

**SigmaUSD v1**

This is v2, to read about v1 see these articles:

- [Finding The Right Balance](https://ergoplatform.org/en/blog/2021_03_04-finding-right-balance/)
- [Community Discussion on Reddit](https://www.reddit.com/r/ergonauts/comments/lx7an4/sigmausd_dao_bank_is_a_complex_beast_highlevel/gpr96fq/?context=3)
- [SigmaUSD (v1) Release](https://ergoplatform.org/en/blog/2021_02_26-sigmausd-released/)

## Can I accept SigUSD as payment on my website? 

Yes! SigmaUSD is accepted in [Cryptocurrency Checkout](https://cryptocurrencycheckout.com/coin/sigmausd) 

## My funds are stuck

If your funds are stuck in a proxy address, use this link for a refund anytime: 

```
https://assm.sigmausd.io/return/your_address_set_in_ui/the_long_address_you_sent_to
```

## If ERG goes 10x, can I get 10x more ERG?

If people are minting and redeeming stablecoins a lot in future, the 1% fee can add up quickly. Your return ratio depends on many factors, such as when you entered, when you exit, the oracle price fluctuations, the initial reserves, and the total amount of SigmaUSD in reverse. 


You must go through the equations and run them with a specific scenario to predict the exact return. 

> SigRSV is a [**reserve**](https://explorer.ergoplatform.com/en/addresses/2zYVHmdQDGtyyZfeqFPdMFqWzMdK299yCj5uDJjiSxRgpHyjiV3mVfZCimFbEVkNkCuypT1khjhupnEb6af3ztdatgag24UzLjW7heidiBF4MqK42TBZC1mLNcm851kvjaEwMsm8bnT2ZwJ6g18ZdDtdKTqEq7KBtp9gkvXiScoNNrA55JhC5o1ZdKRfjRqKMsfWBqmUqTNZfLXy62ddoP8oGT6HafqzKp9YLdSr172KYsnJoK3MhRciMG3McYHfkCFzT3fgNiaTosEtDKUSxaDEmY3r6eTF5H1QmYdkDfEe9AGxzjPgcwR19CfTkuGt8Xg3iUnLRciZ6hVBJc642qDR1EBjY8g7sAtestKYxRLKvUrjV9o3rbFccpgREynwf63mHUZ2jFnuuP2YfeJZdhPf6eK7dnLQ6HDkq5JBd76G7ErB17V1yCr7J6DrC6m47B8aY1XU5fFFQ6Hy6fJm7jzb5DHdn3U4V3TdUM5WwMe6hAmTBz3kFtJBKAiqTw5g53doV7CuUWqC9fTKhGo3BYfXtjFCxeJLwxsXx91s5MWT4tST4XBFnoJP6SZKkfuW7ZvtRbcgpVsz37X6o7YxitwNzaDNmkR9GVLU1XK4cQZjfBijQrTXTTApXnq6wPzzvHTgKyxVuQdDcniEDcgQwttTX4mqooCqxshjy79XL3sFCSTxh4Pjm9UjCgq9daTn83Ro2LnHHifaMjXpFGAbySvqwNvxwBHJnsTXKh2fRggxLDLVobBUfq7DxssPfSaeF4exmdU3mhtuhVhFxAaUVY3LBigWcm4642GtzECVmFRLy1y96m7utcqBiMoyNDy8K3hrM6uzpnA5VYuC6s3jqYp6wZ95QCcRyc3roZL6qTrRXiJupiwYXL3FA1THXPAXLm3PgM7VosJth3bj). If SigUSD holders withdraw at a lower price than they entered, the reserve makes up the difference.


Here is an advanced [introduction to ERGO's SigmaUSD stablecoin risk and reward mechanism.](https://veriumfellow.medium.com/introduction-to-ergos-sigmausd-stablecoin-risk-and-reward-mechanism-18690b52d672)

## Why would anyone buy SigUSD?

**SigmaUSD is a call option on the dollar amount held in reserves.** So if the price of ERG drops, the same amount of $ buys more ERG


This offers decentralised liquidity for miners and large holders who can choose to mint SigUSD to ensure they can always redeem the dollar value - while keeping the option to buy back into ERG on an unexpected dip quickly. 

SigmaUSD also serves a second purpose when there is a Defi ecosystem; 

If price appreciation runs past the opening position of SigmaUSD, the short position offers no gain in ERG but does become a useful stablecoin.

An example, if ERG doubled, there is no incentive for SigmaUSD holders to close a short at a loss of ERG. The incentive changes to build an ecosystem that gives further utility or returns to that stable locked value, creating a market incentive to build a further utility for SigmaUSD. 

Ergonauts can support the network by 'cashing out' into SigmaUSD. It's important to remember that this is still a bull run; it is wise to set cash-out points.

An example, someone who invested $1000 may set a 'cash-out' point at $10,000, where they withdraw their initial investment. This prevents complete loss in the event of a market crash. Using SigmaUSD for this purchase can be done decentralised, without dealing with an exchange - and also gives you the bonus of easily redeeming bonus ergs if the market dips and you want to take profits. It's essentially a very low-risk short position, as you can never be liquidated and will never lose dollar value. 


## My transaction failed
There is currently significant demand. With Ergo being in the UTXO model and all of the dApp design patterns being quite young, we have limitations for the throughput. We have many high-level design ideas to address this for the future with asynchronous EUTXO protocols, but this is still being deeply researched. 

We decided that it was better for the community to have something in the near term rather than waiting another year for the research to solidify into an implementation.


## My profits are lower than expected

SigRSV is a **long** position; shorters could use their volume to profit off the dips during the initial launch. Their ability to do so has been reduced so that transactions will be building up faster. 

[SigmaUSD DAO bank is a complex beast - ergoforums.org](https://www.ergoforum.org/t/sigmausd-dao-bank-is-a-complex-beast/767)

## Why are the fees so high?

> The fee to close a MakerDAO CDP and return your dai is currently 8.5%

Fees are set at 2.25%. 2% goes directly back to the reserves and 0.25% to the frontend implementors. 

If you mint sigmaRSV, you get that 1% back since your reserve coins match the reserve. The more SigRSV you buy, the lower that fee is for you since you own a larger portion of the reserves.

SigmaUSD still lacks a mature DeFi ecosystem, with 1% of each transaction going to the reserves as the price appreciation; there is potential for a large return. 


## What is SigmaUSD based on? 

- The design was inspired by **StatiCoin**
    - [Documentation](https://github.com/Emurgo/age-usd)
- You can read the official [Emurgo announcement blog post here](https://ergoplatform.org/en/blog/2021_02_26-sigmausd-released/)


## How does SigUSD compare against other stablecoins?

See [comparison](comparison.md)


## Explore

- [ERG/USD Explorer](https://explorer.ergoplatform.com/en/oracle-pool-state/ergusd) 
- [ergo.watch](https://ergo.watch/sigmausd)
- [Bank Wallet](https://explorer.ergoplatform.com/en/addresses/MUbV38YgqHy7XbsoXWF5z7EZm524Ybdwe5p9WDrbhruZRtehkRPT92imXer2eTkjwPDfboa1pR3zb3deVKVq3H7Xt98qcTqLuSBSbHb7izzo5jphEpcnqyKJ2xhmpNPVvmtbdJNdvdopPrHHDBbAGGeW7XYTQwEeoRfosXzcDtiGgw97b2aqjTsNFmZk7khBEQywjYfmoDc9nUCJMZ3vbSspnYo3LarLe55mh2Np8MNJqUN9APA6XkhZCrTTDRZb1B4krgFY1sVMswg2ceqguZRvC9pqt3tUUxmSnB24N6dowfVJKhLXwHPbrkHViBv1AKAJTmEaQW2DN1fRmD9ypXxZk8GXmYtxTtrj3BiunQ4qzUCu1eGzxSREjpkFSi2ATLSSDqUwxtRz639sHM6Lav4axoJNPCHbY8pvuBKUxgnGRex8LEGM8DeEJwaJCaoy8dBw9Lz49nq5mSsXLeoC4xpTUmp47Bh7GAZtwkaNreCu74m9rcZ8Di4w1cmdsiK1NWuDh9pJ2Bv7u3EfcurHFVqCkT3P86JUbKnXeNxCypfrWsFuYNKYqmjsix82g9vWcGMmAcu5nagxD4iET86iE2tMMfZZ5vqZNvntQswJyQqv2Wc6MTh4jQx1q2qJZCQe4QdEK63meTGbZNNKMctHQbp3gRkZYNrBtxQyVtNLR8xEY8zGp85GeQKbb37vqLXxRpGiigAdMe3XZA4hhYPmAAU5hpSMYaRAjtvvMT3bNiHRACGrfjvSsEG9G2zY5in2YWz5X9zXQLGTYRsQ4uNFkYoQRCBdjNxGv6R58Xq74zCgt19TxYZ87gPWxkXpWwTaHogG1eps8WXt8QzwJ9rVx6Vu9a5GjtcGsQxHovWmYixgBU8X9fPNJ9UQhYyAWbjtRSuVBtDAmoV1gCBEPwnYVP5GCGhCocbwoYhZkZjFZy6ws4uxVLid3FxuvhWvQrVEDYp7WRvGXbNdCbcSXnbeTrPMey1WPaXX)

### Calculators

- [Spreadsheet](https://docs.google.com/spreadsheets/d/1_lX0FrkIpNHmpMNKWrhhJpC93Wt5wco8oKlf-Wef9fw/edit?usp=sharing)

### Articles

- [Building Ergo: How the AgeUSD stablecoin works](https://ergoplatform.org/en/blog/2021-02-05-building-ergo-how-the-ageusd-stablecoin-works/)
- [AgeUSD Protocol: SigRSV and SigUSD](https://ergoplatform.org/en/blog/2021-07-30-ergos-ageusd-protocol-sigrsv-and-sigusd/)
- [SigmaUSD vs the competition.](https://curiaregiscrypto.medium.com/sigmausd-vs-the-competition-e70b23fe37a3)
- [SigmaUSD on Ergo - Privacy, Stability and Governance](https://curiaregiscrypto.medium.com/sigmausd-on-ergo-a36e0cdff743)
- [Risk and reward mechanism](https://veriumfellow.medium.com/introduction-to-ergos-sigmausd-stablecoin-risk-and-reward-mechanism-18690b52d672)

### Explainer threads

- [Noob tries to explain SigmaUSD/RSV (an attempt at an ELI5)](https://www.reddit.com/r/ergonauts/comments/nhjc1f/noob_tries_to_explain_sigmausdrsv_an_attempt_at/)
- [PSA: sigRSV is not a simple long position](https://www.reddit.com/r/ergonauts/comments/prxpag/psa_sigrsv_is_not_a_simple_long_position/)

### Videos

- [Ergo Summit 2021 - The IOHK Perspective - Designing the AgeUSD StableCoin](https://youtu.be/zG-rxMCDIa0?t=9247)
- [Overview Video (with diagrams)](https://www.youtube.com/watch?v=O3hPEp3tzoU)
- [Youtube playlist](https://www.youtube.com/playlist?list=PL8-KVrs6vXLSu_rLQV5-Pu8389_PLd06q)
- [Buying Guide](https://youtu.be/FR1NCJbzn7w)
- [Buying Guide2](https://www.youtube.com/watch?v=cJuKRfRrTG4)

