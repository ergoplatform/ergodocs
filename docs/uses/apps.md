
Ergo Blockchain is Layer 1 Protocol for powerful Decentralized Finance Contracts that builds advanced cryptographic features and radically new DeFi functionality on the rock-solid foundations laid by a decade of blockchain theory and development. The Proof of Work consensus algorithm and underlying UTxO model enable robust scalability and security. 

## Use Cases
### Stablecoins

Blockchain assets can be extremely volatile. That’s why investors often seek digital assets which are pegged to national currencies. A Stablecoin is the most primitive integration of cryptocurrencies with the off-chain world. Until DAI, fiat custody services were provided by centralized services. The first example of a stable coin, USDT, is backed by [actual dollars](https://cryptobriefing.com/external-auditor-first-confirm-tethers-usdt-backing/) held in banks. However, for a decentralized financial system, we need other means of fiat-pegged currencies. 

Launched in February, Ergo’s native stablecoin SigUSD is based on AgeUSD protocol to provide a robust Reserve/Mint contract. Providing a truly decentralized finance experience. It’s collateralized with its own native cryptocurrency reserves ERG using SigRSV as the trust component which gives SigUSD’s $1 value. SigRSV collateral ratio is set to a minimum of a 400% ratio with SigUSD. This design prohibits liquidations such as we saw in [2020 March crash](https://forum.makerdao.com/t/black-thursday-response-thread/1433). As Emurgo states, "Black Thursday," when MakerDAO CDPs were triggered for liquidation due to volatility and then sold for $0 due to blockchain congestion that prevented others from bidding, demonstrated that a new design is needed. For SigmaUSD, this scenario is not possible.

### Oracle

Oracles are the backbone of a decentralized financial system. It connects off-chain data with the on-chain world. Normally, ETH has no info about the current market price. During a swap order in a decentralized exchange, a swap contract needs to call the data from various data sources to obtain market price. Thus, oracles are the messengers of the crypto ecosystem. Not only in atomic swaps but also in more complex interactions such as lending/borrowing assets or dynamic market-making need the data feeds provided by oracles. DeFi ecosystem suffered from Flash Loan attacks, caused by [misinformation from centralized price oracles](https://insights.glassnode.com/defi-attacks-flash-loans-centralized-price-oracles/).

Ergo developed [Oracle Pools](https://ergoplatform.org/en/blog/2020-08-31-ergos-oracle-pools-and-what-they-mean-for-the-ecosystem/) to maintain a robust DeFi ecosystem. Because of the eUTXO design and its rich programming language ErgoScript, oracle networks can be more decentralized. In the extended UTXO model, we have a lot of flexibility and power available to build new protocols. This can be utilized to construct oracle datapoint hierarchies of confidence. In short, they are an abstraction above oracle pools which allows us to scale the benefits of oracle pools as much as we desire, at the cost of price and speed. [ERG/USD oracle pool](https://explorer.ergoplatform.com/en/oracle-pools-list) is running on Ergo Blockchain.

### NFT

Blockchains aren’t only about cryptocurrencies. Audio or visual artworks can also be deployed on immutable smart contracts of blockchains. These artworks are represented by [Non-Fungible Tokens](https://en.wikipedia.org/wiki/Non-fungible_token). Furthermore, artworks can be traded in decentralized auction houses. This would help artists to reach the world without any restriction of governments or without any need for centralized licensing firms. It means the democratization of art markets with the help of public blockchain.

Some examples like [Rarible](https://rarible.com/) or [Opensea](https://opensea.io/) are auction markets running on Ethereum Network. Any artist can create and sell their artwork in there, however, gas prices to mint an NFT can take up to $100. Ergo’s scalable and faster design would reduce the gas costs to almost zero, without giving up security or speed. [Ergo NFT Auctionhouse](https://ergoauctions.org/#/auction/active?type=picture) is open for months and it allows listings for a picture, audio, or any other kind of non-fungible tokens.

### DEX

Until 2020 DeFi Summer, Value Locked in DeFi ([TVL](https://medium.com/coinmonks/google-sheets-analytics-total-value-locked-in-defi-33b926c18a9f)) was too low to use the platforms effectively. After an increasing interest and new token issuance every day, Decentralized Exchanges (DEX) came into the sunlight. Their benefits are for people who don’t want to give up the custody of their funds. DEXes democratized the exchange experience for both blockchain developers and crypto investors. 

[ErgoDEX](https://ergonaut.space/ergodex.pdf) can provide more functions than Ethereum based DEXes. ErgoDEX [has more properties](https://ergoplatform.org/en/blog/2021-04-06-ergodex-model-amm-and-order-book-type-exchange/) such as limit orders, partial filling, and buy-back supports. Ergo’s Multi-Stage Contracts allows for timed release payments, so a code implemented in the contract can help investors to cancel their order with a minimal loss if the developers of the project don’t deliver their promises. With the implementation of NIPoPoWS, DEX will be interoperable in both PoS and PoW blockchains. Users can enjoy the freedom of exchanges with self-custodial wallets.

### DAO

DAO stands for [Decentral Autonomous Organizations](https://www.investopedia.com/tech/what-dao/). Cryptocurrencies are decentralized (not all of them!), and so their platforms. The governance of these platforms is run by decentralized entities. Every decision is made by pseudo-anonym individuals of DeFi platforms for prohibiting the centralization of power. Therefore, certain tokens are used for voting or making enhancements to these DeFi platforms. [New coin issuances](https://wbtc.network/), redefinition of purposes etc. are all very vital features and can’t be left to a small group of individuals if the crypto ecosystem is for the masses. [Zero-Knowledge Treasury Vaults](https://ergoplatform.org/en/blog/2020-09-04-announcing-the-zk-treasury-on-ergo/) with multi-key signature are the first example of a DAO in Ergo Blockchain.

### Lending - Borrowing

Lending and borrowing are two components that increase liquidity flow in financial systems. For example, you have Bitcoins but you want to leverage your holding without selling your BTC. So, you can stake your BTC (you can also use your house as collateral in this sense) as collateral to borrow SigUSD and use it in exchanges or yield farming protocols. On the other side of your interaction, another user can leverage her unused SigUSD by staking in the lending protocol. Traditional banks have very low-interest rates and they might suck up a lot of revenue from your deposits. With decentral lending protocols such as [Compound](https://compound.finance/), users will be able to use lend/borrow services and move their funds across all crypto ecosystems without any need for centralized platforms such as banks or exchanges. Crypto lending protocols are open to more experimental designs such as [interest-free loans](https://www.ergoforum.org/t/interest-free-loan-contract/67), innovating even more use cases on blockchains.

### Derivatives

Besides buying and selling the tokens of a protocol, traders also want to monetize via various strategies such as options or leveraged future contracts. In traditional finance, these tools are provided by brokerage firms and in the crypto world by centralized exchanges. However, this can turn out to be very harmful towards traders by making exchanges big casinos who can see the player’s hands. That’s why in decentralized finance, there is also an alternative as options or derivatives trading smart contract platform. [Synthetix](https://www.synthetix.io/) is an example of leveraged assets trading platform. The platform token creates liquidity for the traders who want to take leveraged positions. [Hegic](https://www.hegic.co/) on the other hand provides an options trading platform for traders who wants to bet on call-put options via smart contracts. These are just two examples of derivatives protocols on Ethereum. Ergo Blockchain’s Multi-Stage Contracts can also provide these protocols on top of it.

### Insurance

Another big sector of the finance industry is Insurance. Every exchangeable asset carries a risk of losing it, whether by unprecedented risks such as taking a bullet to your Ledger Wallet or foreseeable risks such as [rug pulls](https://www.coingecko.com/en/glossary/rug-pulled). New protocols emerged such as [Nexus Mutual](https://nexusmutual.io/) to tackle the decentral insurance problem. If you think about insurance, it pays a premium to risk bearers in case a bad event happens, exchanging your money for security. In a Decentralized Insurance platform: Your participation, risk bearers’ participation and validation of the trade by oracles can all be governed by smart contracts to create a smoothly functioning DeFi ecosystem.

### Yield Aggregation

So after an expansion of new decentralized exchanges such as [Bancor](https://bancor.network/), [Balancer](https://balancer.finance/), [Uniswap](https://uniswap.org/), [Sushiswap](https://www.sushi.com/), and [Curve](https://resources.curve.fi/), people are started to look for easier ways to move capital around those exchanges to create the best yields. Yield Aggregators are helping users to automate the liquidity farming actions. The first example of a yield aggregation protocol is [Yearn Finance](https://yearn.finance/). In the protocol, users can choose different yield farming strategies among the vaults deployed. Not only users but also developers can leverage yield farming platforms by creating their unique yield farming strategies and deploying them on protocols. Such examples will be very useful for market-making algorithms in the future by supporting deep liquidity all across DeFi.

### Index Coins

Not all crypto investors are conscient about different blockchain use cases. Some of the investors may want to benefit from indexed tokens to invest in various cryptocurrencies. For such an innovation dynamic market-making(DMM) algorithms would be necessary to adjust the funds after price changes. Besides, people who will release index tokens must have the market knowledge to decide which tokens must be involved in the indexed and for how many percentage. Some examples of index coins running on Ethereum are ASSY, YETI, PIPT, YLA issued by [Powerpool Protocol](https://powerpool.finance/). 

### Asset Tokenization

Asset Tokenization is meeting traditional financial assets with crypto. A centralized exchange [FTX](https://ftx.com/markets/stocks) provides US stocks in exchange for cryptocurrencies. This phenomenon, however, is very new due to regulation problems. Stock tokens are not yet traded on decentralized exchanges. Another example of tokenization of real-world assets would be real estate tokenization. With the help of cryptocurrencies, [houses can be fractionated](https://labsgroup.io/) into thousands of tokens representing real estate. These kinds of implementations will help retail investors to invest in houses all around the world with minimal savings.

*All the utilities of traditional banks are becoming decentralized applications on smart contract platforms. Ergo is providing robust and rich infrastructure with **ErgoScript** language to support a complex DeFi ecosystem powered by **Multi-Stage Contracts**.*

### Many more possible!

- [Bonds based on Ergo (or the “Yield protocol”)](https://www.ergoforum.org/t/bonds-based-on-ergo-or-the-yield-protocol/128)
- [An ICO Example On Top Of Ergo](https://github.com/ergoplatform/ergo/wiki/An-ICO-Example-On-Top-Of-Ergo)
- [A Local Exchange Trading System On Top Of Ergo](https://github.com/ergoplatform/ergo/wiki/A-Local-Exchange-Trading-System-On-Top-Of-Ergo)
- [A Trustless Local Exchange Trading System](https://github.com/ergoplatform/ergo/wiki/A-Trustless-Local-Exchange-Trading-System)
- [(E)mail Client for Limited or Blocked Internet](https://www.ergoforum.org/t/e-mail-client-for-limited-or-blocked-internet/134)
- [LETS start the discussion](https://ergoplatform.org/en/blog/2021-07-01-lets-start-the-discussion/)
- [Self-Soverign Defi](https://ergoforum.org/t/self-sovereign-defi/260)
- [Payment channels without multisignatures](https://www.ergoforum.org/t/payment-channels-without-multisignatures/2219)
- [Shrimpcoin - The first shrimp-pinned stablecoin on Ergo](https://www.ergoforum.org/t/shrimpcoin-the-first-shrimp-pinned-stablecoin-on-ergo/1381)
* Loans: we have interest-free loan contract example: https://www.ergoforum.org/t/interest-free-loan-contract/67 . With SigmaUSD loans can be attractive to miners and not only. Please also check targeted microloan contract from "Smart Contracts for the People" article: http://chepurnoy.org/blog/2018/10/smart-contracts-for-the-people/
*  Mining power derivatives: https://www.ergoforum.org/t/mining-power-derivatives-two-tokens-approach/277


## Powerful But Safe Contracts

Ethereum is an exceptional platform, but there are things it does not do well. Its Turing-complete smart contracts are powerful, but dangerous – as incidents from The DAO to the Parity wallet exploits have proven, with tens of millions of dollars in collateral damage. With complexity comes uncertainty, and potentially catastrophic vulnerabilities. Contracts can be expensive to run, and depending on network conditions may execute unpredictably – or not at all. 

Ergo takes a fundamentally different approach to smart contract development. The team, which has extensive experience with blockchain platforms, frameworks and organisations from Nxt and Waves to Scorex and IOHK, has adopted a declarative model for programming whereby it’s always known in advance how much code will cost to run – and, indeed, whether it will run precisely as intended. While that might on the surface limit code complexity, it’s nevertheless possible to create Turing-complete scripts by iterating processes across multiple blocks. That means Ergo can support versatile dApps that run predictably, with known costs, and don’t have any of the dangers of unrestricted functionality.

### Sigma protocols

The platform is unashamedly conservative, basing as many features as possible on Bitcoin – after all, Bitcoin is the most battle-tested crypto network in existence. Ergo’s UTXO model, PoW mining and finite supply draw on Bitcoin’s approaches to consensus and economic incentives.

But Ergo also incorporates cutting-edge research into new cryptographic processes, using Sigma protocols to enable DeFi applications that would be either complex and messy or simply impossible on other platforms. Sigma protocols are a well-known class of zero-knowledge proofs that allow developers to implement very powerful processes very elegantly. For example, what if you want to build a privacy service that allows any one of a dozen different accounts to spend funds from an address – but no one can tell who has made each transfer? Such a ‘ring contract’ is possible with Ethereum, but it would require a clunky and expensive workaround. With Ergo’s Sigma protocols, it’s possible to implement this kind of use case and many others quickly, efficiently and – above all – securely. Sigma protocols have not been deployed in such generic form within crypto before. Yet this kind of out-of-the-box functionality is hugely valuable, especially when no other DeFi platform offers it.

_Ergo enables new models of financial interaction, underpinned by smart contracts built on flexible and powerful Sigma protocols but easily accessible to developers._

One of the most exciting things about blockchain is the possibility of making digital agreements without any trusted intermediaries. In the simplest use case, pioneered by Bitcoin, Alice can send a payment directly to Bob, wherever the two of them are located around the world, with no bank or any trusted third party needed. However, with the functionality of a modern blockchain like Ergo, it is possible to make far more complex and sophisticated financial agreements than simple payments. Take the following example.

### Gold-backed tokens

Alice uses ERGs to purchase gold-backed tokens from Bob. Bob stores the gold in a secure vault, and uses the blockchain to issue one token for every Troy ounce of gold he has. Alice can then use these tokens freely in different contracts, transferring and trading them under whatever conditions she specifies in the smart contract code. When Alice wants to sell the tokens for physical gold, she can conduct another transaction with Bob, receiving ERG in return, at market price.

The point of blockchain contracts is to eliminate the need for trust. While the purchase transaction is now trustless, in this instance Alice still needs to trust Bob about two things. Firstly, Bob may refuse to swap the gold tokens back to ERG at the correct price when Alice wants to sell. Secondly, Bob may default on his obligations – running away with the gold, or misusing the funds he receives and running a fractional reserve.

### Extending the contracts

To address these issues, we can create an Oracle, or decentralised price feed. This uses multiple sources of external data to record the price of gold to the blockchain at regular intervals. This price feed will be the reference point for the redemption contract that manages the sale of Alice’s gold with Bob (or any other participant). Thus the system automatically enforces the right price when a swap takes place.

The second situation requires a third-party insurer, Charlie, whose service is also hosted on the blockchain with a smart contract. When Alice purchases gold from Bob, she additionally buys an insurance contract from Charlie. The payment can be dependent on factors including the amount of insurance required, and Bob’s reputation – again, managed by a decentralized feedback mechanism. Now, if Bob defaults, Alice will automatically receive the value of her gold tokens, with Charlie effectively acting as a buyer of last resort.

### Programmable contracts

There are, of course, many other example use cases like this one. We can also extend this use case, adding further economic actors. For example, Charlie may sell shares in his insurance business to Dave and other participants, providing them with a proportion of revenues in return for ensuring he has the capital he needs to cover any liabilities from the outset.

However, even the most complex use case is simpler than general-purpose software that can be used to program any contract. After all, generalised logic must be both far-reaching and secure. Moreover, even a specialised contract is made up of many steps, each of which is fairly simple. Thus another requirement for a general-purpose platform is that it should simplify the process of writing contracts, making them as accessible (and safe) as possible. This can be achieved with the use of template agreements, with customisable parameters. The insurance contract above could be based on a module with flexible parameters, for example. This could be used and reused in many different circumstances.
