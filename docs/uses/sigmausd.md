# Accessing Sigmausd As A Developer

SigmaUSD is the first eUTxO-based stablecoin, implementing the [AgeUSD protocol](https://github.com/Emurgo/age-usd). It was co-designed by IOHK, Ergo, and Emurgo, focusing on conservative collateral reserve settings, thus eliminating the need for liquidations. SigmaUSD supports a fully decentralized stablecoin emission setup, offering a stable, simple, and decentralized stablecoin.

## How does SigmaUSD work?

**Reserve providers** submit ERGs to the dApp's reserves to mint *reserve coins* (**SigmaRSV**), each representing a portion of the underlying ERG reserves. **SigmaUSD** users also submit ERGs to the dApp reserves to mint SigmaUSD, provided there are sufficient reserves within the dApp. Users can redeem their SigmaUSD for an equivalent amount of ERGs from the reserves at the current exchange rate as provided by the ERG-USD [oracle pool](https://explorer.ergoplatform.com/en/oracle-pool-state/ergusd).

Reserve Providers can redeem their *reserve coins* for ERGs if the price of ERGs increases or a significant amount of protocol fees are collected, covering the value of all existing minted SigmaUSD plus an extra margin. This allows Reserve Providers to profit by receiving more underlying reserve cryptocurrency than when they minted their *reserve coins*.


## Common Questions


/// details | What is a stablecoin?
     {type: question, open: false}

> It is a derivate product. This derivative intends to create a way to stabilise volatility.


Price stability is a critical part of finance; without it, it becomes difficult to create long-term financial product modellings. Investment takes a risk; a good business requires modelling and forecasting to estimate profitability, whether on-chain or off. 

The crypto space, by nature, is highly volatile. SigmaUSD and SigmaRSV are mechanisms to create stable value, and stable value is the foundation for a prosperous economy. 

Derivatives were created to minimise volatility when trading in foreign currencies. 

In a globalised economy, the shift in purchasing power of one currency vs another can be a highly destructive force. Instability disrupts trade and destroys business models. 

Stability comes at a cost. Instability in price is often added as a premium, sometimes a price premium, and other times an interest premium. 

The cost of SigmaUSD is the current USD value of ERG plus a 2.5% fee. 

This is a low premium, 2.5%. 

What is your current interest rate? What is the rate at which a bank will collateralise an asset you hold and offer a loan?

Very few have access to this low premium in the global economy, and the bank may not offer liquidity with little to no reserve.

SigmaUSD allows anyone who owns ERG to collateralise their ERG and create liquid value. What does this mean?

The long-term goal will be to create use cases for this stablecoin that offers a return beyond this 2.5% fee. 
///


/// details | Why SigmaUSD
     {type: question, open: false}

> When Dapps and use/utility are in place that supersedes this 2.5% fee, magic happens. 


A user can take their ERG, create SigmaUSD, and then use that to create a return greater than the 2.5% cost of stability. Most business models rely on stability and price/risk prediction rather than asset speculation. 

SigmaUSD is not just an opportunity to take a short position on ERG. Rather it is a way to use your reserve value to generate yield. Defi on Ergo delivers additional gateways, decentralised exchanges, or ergo swap liquidity pools, allowing growth opportunities for this stable value.No economy can function properly with high price volatility. A stable, robust decentralised economy requires a stable and robust mechanism currency. Ideally, a currency backed by a reserve asset ensures its value.  

Once the 2.5% cost of stability is overcome, the dynamic of the SigmaRSV will change dramatically. Users have an incentive to continually mint/redeem SigmaUSD. Perhaps the value of ERG will go up, and a user may have missed some price appreciation; however, if they overcome the 2.5% threshold, the user will have a net USD gain. 

Using stable value as the medium to invest and overcoming the 2.5% threshold generates returns, transforming a short into a way to create value from stability.   

**Imagine the following scenarios.**

- A User chooses stability for a 2.5% premium. 
- Even if the price of ERG appreciates, the user can net again. They will have less redeemable ERG, but growth is growth. They end with a larger position in USD. 
- Perhaps ERG's value goes down; the stable value is used to create a net USD gain. The stable value can be redeemed for a larger ERG position upon redemption. Not only did they grow their position in USD, but they grew their position in ERG as well. 
- When SigmaUSD becomes a pathway of generative value beyond a short, it incentivises users to interact with the AgeUSD protocol on ERG. 
- This result will be a healthy reserve system that nets growth through interaction and exchange.

At this point, expect appreciation in SigmaRSV. Expect the treasury to grow. 

This is the major barrier to overcome, the 2.5% fee. 

All things being equal, this is a very low barrier to success. 

///

/// details | Where can I buy SigmaUSD?
     {type: question, open: false}


- [Tokenjay.app](https://tokenjay.app/)
- [SigmaUSD.io](https://www.sigmausd.io)
- ErgoMixer
- Minotaur Wallet
- Spectrum.fi
///
/// details | How does the reserve work?
     {type: question, open: false}
SigmaUSD operates on larger margin requirements than traditional crypto-backed stablecoins. SigmaUSD is backed by ERG within a floating reserve ratio between 4:1 and 8:1. The minimum threshold (4:1) protects SigmaUSD holders by ensuring that ERG always backs the tokens sufficiently for market volatility. The maximum threshold (8:1) protects SigmaRSV holders from unnecessary dilution of their position, limiting inflationary pressures. SigmaUSD employs locking mechanisms to maintain the reserves within this range, temporarily preventing users from interacting with the contract as an alternative to forced liquidations.

![sigmausd_overview.png](sigmausd_overview.png)
///

/// details | Why might transactions fail?
    {type: question, open: false}
There is currently significant demand. With Ergo being in the UTXO model and all of the dApp design patterns being quite young, we have throughput limitations. We have many high-level design ideas to address this in the future with asynchronous EUTXO protocols, but this is still being deeply researched.

We decided that it was better for the community to have something in the near term rather than waiting another year for the research to solidify into an implementation.
///

/// details | Why might profits be lower?
    {type: question, open: false}
SigRSV is a **long** position. Shorters could use their volume to profit off the dips during the initial launch. Their ability to do so has been reduced so that transactions will build up faster.

[SigmaUSD DAO bank is a complex beast - ergoforums.org](https://www.ergoforum.org/t/sigmausd-dao-bank-is-a-complex-beast/767)
///

/// details | Understanding Fees
    {type: question, open: false}
> The fee to close a MakerDAO CDP and return your Dai is currently 8.5%

Fees are set at 2.25%. 2% goes directly back to the reserves, and 0.25% goes to the frontend implementers.

If you mint SigmaRSV, you get that 1% back since your reserve coins match the reserve. The more SigmaRSV you buy, the lower that fee is for you since you own a larger portion of the reserves.

SigmaUSD still lacks a mature DeFi ecosystem, but with 1% of each transaction going to the reserves as the price appreciates, there is potential for a large return.
///

/// details | What is SigmaUSD based on?
     {type: question, open: false}
- The design was inspired by **StatiCoin**
    - [Documentation](https://github.com/Emurgo/age-usd)
- You can read the official [Emurgo announcement blog post here](https://ergoplatform.org/en/blog/2021_02_26-sigmausd-released/).
///

/// details | How does SigmaUSD compare against other stablecoins?
     {type: question, open: false}
See [comparison](comparison.md)
///




## Explore

/// details | Accessing SigUSD as a Developer
     {type: info, open: false}
This guide introduces key methods for developers to interact with the SigmaUSD stablecoin on the Ergo blockchain, providing detailed steps, code examples, and references to relevant files. Whether you're building a frontend dApp with Mosaik or managing UTXOs with AppKit, this guide covers the essentials. For a deeper dive, see the full documentation [here](sigusd-dev.md).
///


/// details | Useful Links
     {type: info, open: false}
- [ERG/USD Explorer](https://explorer.ergoplatform.com/en/oracle-pool-state/ergusd)
- [ergo.watch](https://ergo.watch/sigmausd)
- [Bank Wallet](https://explorer.ergoplatform.com/en/addresses/MUbV38YgqHy7XbsoXWF5z7EZm524Ybdwe5p9WDrbhruZRtehkRPT92imXer2eTkjwPDfboa1pR3zb3deVKVq3H7Xt98qcTqLuSBSbHb7izzo5jphEpcnqyKJ2xhmpNPVvmtbdJNdvdopPrHHDBbAGGeW7XYTQwEeoRfosXzcDtiGgw97b2aqjTsNFmZk7khBEQywjYfmoDc9nUCJMZ3vbSspnYo3LarLe55mh2Np8MNJqUN9APA6XkhZCrTTDRZb1B4krgFY1sVMswg2ceqguZRvC9pqt3tUUxmSnB24N6dowfVJKhLXwHPbrkHViBv1AKAJTmEaQW2DN1fRmD9ypXxZk8GXmYtxTtrj3BiunQ4qzUCu1eGzxSREjpkFSi2ATLSSDqUwxtRz639sHM6Lav4axoJNPCHbY8pvuBKUxgnGRex8LEGM8DeEJwaJCaoy8dBw9Lz49nq5mSsXLeoC4xpTUmp47Bh7GAZtwkaNreCu74m9rcZ8Di4w1cmdsiK1NWuDh9pJ2Bv7u3EfcurHFVqCkT3P86JUbKnXeNxCypfrWsFuYNKYqmjsix82g9vWcGMmAcu5nagxD4iET86iE2tMMfZZ5vqZNvntQswJyQqv2Wc6MTh4jQx1q2qJZCQe4QdEK63meTGbZNNKMctHQbp3gRkZYNrBtxQyVtNLR8xEY8zGp85GeQKbb37vqLXxRpGiigAdMe3XZA4hhYPmAAU5hpSMYaRAjtvvMT3bNiHRACGrfjvSsEG9G2zY5in2YWz5X9zXQLGTYRsQ4uNFkYoQRCBdjNxGv6R58Xq74zCgt19TxYZ87gPWxkXpWwTaHogG1eps8WXt8QzwJ9rVx6Vu9a5GjtcGsQxHovWmYixgBU8X9fPNJ9UQhYyAWbjtRSuVBtDAmoV1gCBEPwnYVP5GCGhCocbwoYhZkZjFZy6ws4uxVLid3FxuvhWvQrVEDYp7WRvGXbNdCbcSXnbeTrPMey1WPaXX)
///


/// details | SigmaUSD Calculators
     {type: info, open: false}
- [Spreadsheet](https://docs.google.com/spreadsheets/d/1_lX0FrkIpNHmpMNKWrhhJpC93Wt5wco8oKlf-Wef9fw/edit?usp=sharing)
///


/// details | Related Articles
     {type: info, open: false}
- [Building Ergo: How the AgeUSD stablecoin works](https://ergoplatform.org/en/blog/2021-02-05-building-ergo-how-the-ageusd-stablecoin-works/)
- [AgeUSD Protocol: SigRSV and SigUSD](https://ergoplatform.org/en/blog/2021-07-30-ergos-ageusd-protocol-sigrsv-and-sigusd/)
- [SigmaUSD vs the competition.](https://curiaregiscrypto.medium.com/sigmausd-vs-the-competition-e70b23fe37a3)
- [SigmaUSD on Ergo - Privacy, Stability and Governance](https://curiaregiscrypto.medium.com/sigmausd-on-ergo-a36e0cdff743)
- [Risk and reward mechanism](https://veriumfellow.medium.com/introduction-to-ergos-sigmausd-stablecoin-risk-and-reward-mechanism-18690b52d672)
///


/// details | Explainer Threads
     {type: info, open: false}
- [Noob tries to explain SigmaUSD/RSV (an attempt at an ELI5)](https://www.reddit.com/r/ergonauts/comments/nhjc1f/noob_tries_to_explain_sigmausdrsv_an_attempt_at/)
- [PSA: sigRSV is not a simple long position](https://www.reddit.com/r/ergonauts/comments/prxpag/psa_sigrsv_is_not_a_simple_long_position/)
///


/// details | SigmaUSD Videos
     {type: info, open: false}
- [Ergo Summit 2021 - The IOHK Perspective - Designing the AgeUSD StableCoin](https://youtu.be/zG-rxMCDIa0?t=9247)
- [Overview Video (with diagrams)](https://www.youtube.com/watch?v=O3hPEp3tzoU)
- [Youtube Playlist](https://www.youtube.com/playlist?list=PL8-KVrs6vXLSu_rLQV5-Pu8389_PLd06q)
- [Buying Guide](https://youtu.be/FR1NCJbzn7w)
- [Buying Guide2](https://www.youtube.com/watch?v=cJuKRfRrTG4)
///