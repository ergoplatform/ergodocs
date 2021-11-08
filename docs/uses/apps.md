
Ergo Blockchain is Layer 1 Protocol for powerful Decentralized Finance Contracts that builds advanced cryptographic features and radically new DeFi functionality on the rock-solid foundations laid by a decade of blockchain theory and development. The Proof of Work consensus algorithm and underlying UTxO model enable robust scalability and security. 





## **Use** Cases **of Ergo**

    *Oracles:* Oracles are the messengers in and out of blockchains. They contain valuable data (e.g. price feed) so that applications work seamlessly. Ergo Blockchain’s design allows *Oracle Pools*, and this would help to create data hierarchies. A system of oracles that can be scored regarding their trust level is a significant phenomenon. Chainlink’s oracles aren’t capable of forming oracle pools because it’s built on the Ethereum network. Yet Chainlink recently published a whitepaper about decentralized computational networks interacting with blockchains, an idea that Ergo already working on with oracle pools.

    *NIPoPoWs*: Non-interactive proofs of proof of works can be used to build an interoperable blockchain ecosystem. With NIPoPoW implementation, Ergo Blockchain can interact with the smart contracts on proof of stake networks. This would open up an integrated use case between different dApps on different blockchains. Cardano is already planning to implement side chains with NIPoPoWs in collaboration with EMURGO. Limits are yet to be discovered. 

   *Multi-Sig:* Multi-Sig or Multi Provers are helpful for the reliability of smart contracts. This kind of implementation is vital for security. So that smart contracts aren’t in control of one person, but rather governed by multiple accounts. Multi-stage contracts can also be designed for punishing malicious actors trying to take control of smart contracts.

   *Time Epoch:* Ergo Blockchain can be designed to have timed operations. For example, during an *ICO* (or *IDO*), a code in a smart contract can provide *timed release* so that investors have a protective layer if the project owner isn’t delivering his/her promises. In Ethereum, programming such a kind of timed operation isn’t possible. 

   *Parachain/Sidechains:* This is a yet-to-develop area for Ergo Blockchain. It’s certainly possible, and we know that the implementation of parachains has a significant impact on scalability. Our core developer *Alex Chepurnoy* is about to release a paper on it, so stay tuned!

## Stablecoins

Blockchain assets can be extremely volatile. That’s why investors often seek digital assets which are pegged to national currencies. A Stablecoin is the most primitive integration of cryptocurrencies with the off-chain world. Until DAI, fiat custody services were provided by centralized services. The first example of a stable coin, USDT, is backed by [actual dollars](https://cryptobriefing.com/external-auditor-first-confirm-tethers-usdt-backing/) held in banks. However, for a decentralized financial system, we need other means of fiat-pegged currencies. 

Launched in February, Ergo’s native stablecoin SigUSD is based on AgeUSD protocol to provide a robust Reserve/Mint contract. Providing a truly decentralized finance experience. It’s collateralized with its own native cryptocurrency reserves ERG using SigRSV as the trust component which gives SigUSD’s $1 value. SigRSV collateral ratio is set to a minimum of a 400% ratio with SigUSD. This design prohibits liquidations such as we saw in [2020 March crash](https://forum.makerdao.com/t/black-thursday-response-thread/1433). As Emurgo states, "Black Thursday," when MakerDAO CDPs were triggered for liquidation due to volatility and then sold for $0 due to blockchain congestion that prevented others from bidding, demonstrated that a new design is needed. For SigmaUSD, this scenario is not possible.

## Oracles

Oracles are the backbone of a decentralized financial system. It connects off-chain data with the on-chain world. Normally, ETH has no info about the current market price. During a swap order in a decentralized exchange, a swap contract needs to call the data from various data sources to obtain market price. Thus, oracles are the messengers of the crypto ecosystem. Not only in atomic swaps but also in more complex interactions such as lending/borrowing assets or dynamic market-making need the data feeds provided by oracles. DeFi ecosystem suffered from Flash Loan attacks, caused by [misinformation from centralized price oracles](https://insights.glassnode.com/defi-attacks-flash-loans-centralized-price-oracles/).

Ergo developed [Oracle Pools](https://ergoplatform.org/en/blog/2020-08-31-ergos-oracle-pools-and-what-they-mean-for-the-ecosystem/) to maintain a robust DeFi ecosystem. Because of the eUTXO design and its rich programming language ErgoScript, oracle networks can be more decentralized. In the extended UTXO model, we have a lot of flexibility and power available to build new protocols. This can be utilized to construct oracle datapoint hierarchies of confidence. In short, they are an abstraction above oracle pools which allows us to scale the benefits of oracle pools as much as we desire, at the cost of price and speed. [ERG/USD oracle pool](https://explorer.ergoplatform.com/en/oracle-pools-list) is running on Ergo Blockchain.

- [Shrimpcoin - The first shrimp-pinned stablecoin on Ergo](https://www.ergoforum.org/t/shrimpcoin-the-first-shrimp-pinned-stablecoin-on-ergo/1381)


## NFT

Blockchains aren’t only about cryptocurrencies. Audio or visual artworks can also be deployed on immutable smart contracts of blockchains. These artworks are represented by [Non-Fungible Tokens](https://en.wikipedia.org/wiki/Non-fungible_token). Furthermore, artworks can be traded in decentralized auction houses. This would help artists to reach the world without any restriction of governments or without any need for centralized licensing firms. It means the democratization of art markets with the help of public blockchain.

Some examples like [Rarible](https://rarible.com/) or [Opensea](https://opensea.io/) are auction markets running on Ethereum Network. Any artist can create and sell their artwork in there, however, gas prices to mint an NFT can take up to $100. Ergo’s scalable and faster design would reduce the gas costs to almost zero, without giving up security or speed. [Ergo NFT Auctionhouse](https://ergoauctions.org/#/auction/active?type=picture) is open for months and it allows listings for a picture, audio, or any other kind of non-fungible tokens.

## DEX

Until 2020 DeFi Summer, Value Locked in DeFi ([TVL](https://medium.com/coinmonks/google-sheets-analytics-total-value-locked-in-defi-33b926c18a9f)) was too low to use the platforms effectively. After an increasing interest and new token issuance every day, Decentralized Exchanges (DEX) came into the sunlight. Their benefits are for people who don’t want to give up the custody of their funds. DEXes democratized the exchange experience for both blockchain developers and crypto investors. 

[ErgoDEX](https://ergonaut.space/ergodex.pdf) can provide more functions than Ethereum based DEXes. ErgoDEX [has more properties](https://ergoplatform.org/en/blog/2021-04-06-ergodex-model-amm-and-order-book-type-exchange/) such as limit orders, partial filling, and buy-back supports. Ergo’s Multi-Stage Contracts allows for timed release payments, so a code implemented in the contract can help investors to cancel their order with a minimal loss if the developers of the project don’t deliver their promises. With the implementation of NIPoPoWS, DEX will be interoperable in both PoS and PoW blockchains. Users can enjoy the freedom of exchanges with self-custodial wallets.

## DAO

DAO stands for [Decentral Autonomous Organizations](https://www.investopedia.com/tech/what-dao/). Cryptocurrencies are decentralized (not all of them!), and so their platforms. The governance of these platforms is run by decentralized entities. Every decision is made by pseudo-anonym individuals of DeFi platforms for prohibiting the centralization of power. Therefore, certain tokens are used for voting or making enhancements to these DeFi platforms. [New coin issuances](https://wbtc.network/), redefinition of purposes etc. are all very vital features and can’t be left to a small group of individuals if the crypto ecosystem is for the masses. [Zero-Knowledge Treasury Vaults](https://ergoplatform.org/en/blog/2020-09-04-announcing-the-zk-treasury-on-ergo/) with multi-key signature are the first example of a DAO in Ergo Blockchain.

## Lending - Borrowing

Lending and borrowing are two components that increase liquidity flow in financial systems. For example, you have Bitcoins but you want to leverage your holding without selling your BTC. So, you can stake your BTC (you can also use your house as collateral in this sense) as collateral to borrow SigUSD and use it in exchanges or yield farming protocols. On the other side of your interaction, another user can leverage her unused SigUSD by staking in the lending protocol. Traditional banks have very low-interest rates and they might suck up a lot of revenue from your deposits. With decentral lending protocols such as [Compound](https://compound.finance/), users will be able to use lend/borrow services and move their funds across all crypto ecosystems without any need for centralized platforms such as banks or exchanges. Crypto lending protocols are open to more experimental designs such as [interest-free loans](https://www.ergoforum.org/t/interest-free-loan-contract/67), innovating even more use cases on blockchains.


## Derivatives

Besides buying and selling the tokens of a protocol, traders also want to monetize via various strategies such as options or leveraged future contracts. In traditional finance, these tools are provided by brokerage firms and in the crypto world by centralized exchanges. However, this can turn out to be very harmful towards traders by making exchanges big casinos who can see the player’s hands. That’s why in decentralized finance, there is also an alternative as options or derivatives trading smart contract platform. [Synthetix](https://www.synthetix.io/) is an example of leveraged assets trading platform. The platform token creates liquidity for the traders who want to take leveraged positions. [Hegic](https://www.hegic.co/) on the other hand provides an options trading platform for traders who wants to bet on call-put options via smart contracts. These are just two examples of derivatives protocols on Ethereum. Ergo Blockchain’s Multi-Stage Contracts can also provide these protocols on top of it.

## Insurance

Another big sector of the finance industry is Insurance. Every exchangeable asset carries a risk of losing it, whether by unprecedented risks such as taking a bullet to your Ledger Wallet or foreseeable risks such as [rug pulls](https://www.coingecko.com/en/glossary/rug-pulled). New protocols emerged such as [Nexus Mutual](https://nexusmutual.io/) to tackle the decentral insurance problem. If you think about insurance, it pays a premium to risk bearers in case a bad event happens, exchanging your money for security. In a Decentralized Insurance platform: Your participation, risk bearers’ participation and validation of the trade by oracles can all be governed by smart contracts to create a smoothly functioning DeFi ecosystem.

## Yield Aggregation

So after an expansion of new decentralized exchanges such as [Bancor](https://bancor.network/), [Balancer](https://balancer.finance/), [Uniswap](https://uniswap.org/), [Sushiswap](https://www.sushi.com/), and [Curve](https://resources.curve.fi/), people are started to look for easier ways to move capital around those exchanges to create the best yields. Yield Aggregators are helping users to automate the liquidity farming actions. The first example of a yield aggregation protocol is [Yearn Finance](https://yearn.finance/). In the protocol, users can choose different yield farming strategies among the vaults deployed. Not only users but also developers can leverage yield farming platforms by creating their unique yield farming strategies and deploying them on protocols. Such examples will be very useful for market-making algorithms in the future by supporting deep liquidity all across DeFi.

- [Bonds based on Ergo (or the “Yield protocol”)](https://www.ergoforum.org/t/bonds-based-on-ergo-or-the-yield-protocol/128)


## Index Coins

Not all crypto investors are conscient about different blockchain use cases. Some of the investors may want to benefit from indexed tokens to invest in various cryptocurrencies. For such an innovation dynamic market-making(DMM) algorithms would be necessary to adjust the funds after price changes. Besides, people who will release index tokens must have the market knowledge to decide which tokens must be involved in the indexed and for how many percentage. Some examples of index coins running on Ethereum are ASSY, YETI, PIPT, YLA issued by [Powerpool Protocol](https://powerpool.finance/). 

## Asset Tokenization

Asset Tokenization is meeting traditional financial assets with crypto. A centralized exchange [FTX](https://ftx.com/markets/stocks) provides US stocks in exchange for cryptocurrencies. This phenomenon, however, is very new due to regulation problems. Stock tokens are not yet traded on decentralized exchanges. Another example of tokenization of real-world assets would be real estate tokenization. With the help of cryptocurrencies, [houses can be fractionated](https://labsgroup.io/) into thousands of tokens representing real estate. These kinds of implementations will help retail investors to invest in houses all around the world with minimal savings.

*All the utilities of traditional banks are becoming decentralized applications on smart contract platforms. Ergo is providing robust and rich infrastructure with **ErgoScript** language to support a complex DeFi ecosystem powered by **Multi-Stage Contracts**.*


## Initial Coin Offerings
- [An ICO Example On Top Of Ergo](https://github.com/ergoplatform/ergo/wiki/An-ICO-Example-On-Top-Of-Ergo)

## Local Exchange Trading Systems

- [A Local Exchange Trading System On Top Of Ergo](https://github.com/ergoplatform/ergo/wiki/A-Local-Exchange-Trading-System-On-Top-Of-Ergo)
- [A Trustless Local Exchange Trading System](https://github.com/ergoplatform/ergo/wiki/A-Trustless-Local-Exchange-Trading-System)
- [LETS start the discussion](https://ergoplatform.org/en/blog/2021-07-01-lets-start-the-discussion/)

## Self-Soverign Defi
- [Self-Soverign Defi](https://ergoforum.org/t/self-sovereign-defi/260)


## misc
- [Payment channels without multisignatures](https://www.ergoforum.org/t/payment-channels-without-multisignatures/2219)
* Loans: we have interest-free loan contract example: https://www.ergoforum.org/t/interest-free-loan-contract/67 . With SigmaUSD loans can be attractive to miners and not only. Please also check targeted microloan contract from "Smart Contracts for the People" article: http://chepurnoy.org/blog/2018/10/smart-contracts-for-the-people/
*  Mining power derivatives: https://www.ergoforum.org/t/mining-power-derivatives-two-tokens-approach/277


