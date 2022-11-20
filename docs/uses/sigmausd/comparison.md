## Other Stablecoins

- [SigmaUSD vs the competition](https://curiaregiscrypto.medium.com/sigmausd-vs-the-competition-e70b23fe37a3)

## Direct Comparison

### Advantages over MakerDAO
> **No liquidations!**


Unlike Ethereum-based crypto-backed stablecoins, such as DAI, Emurgo introduces a Staticoin protocol-inspired design that does not rely on CDPs (Collateralized Debt Positions). The reason for this is the vulnerability of CDP-based protocols in terms of high volatility and blockchain congestion. As Emurgo states, "Black Thursday," when MakerDAO CDPs were triggered for liquidation due to volatility and then sold for $0 due to blockchain congestion that prevented others from bidding, demonstrated that a new design is needed. For SigmaUSD, this scenario is not possible.

### Advantages over UST

SigUSD is over-collateralised; every sigusd is backed by 3$ currently. Everyone can see that there is money in the bank, which stops a bank's run at its inception. The breaking point of the peg is explicit and open for anyone to see. With UST, you have no idea, which gives you an incentive to get out first.


- Luna supply depends on terra usage; Ergo does not. Burning luna when the trend is up pumps its price. However, the luna price will dump harder when the trend is down because more luna is printed. 

- collateral ratio for sigusd is higher. This means that the capital efficiency (less collateral tied for each stablecoin) is better for terra, which is why luna/terra can offer a better yield. 

However, this means luna/terra needs an additional mechanism to ensure stability. When collateral (luna) value drops, someone needs to stabilise it. Those people are incentivised with promises of larger profits in the future. This assumes that people will always believe that the protocol survives the crash. No one knows at which price point luna the trust disappears. This creates a seed for a bank run. Everyone wants to take their stablecoin out faster than others if there is any doubt.

In contrast, sigusd shows explicitly when the peg will be lost. No one needs to guess how long the protocol can last.


## Overview

### **Fiat-Collateralized**

#### Tether 

Best for liquidity, accepted on almost all crypto exchanges.

> A fiat-pegged stablecoin built on top of Bitcoin via the Omni Layer Protocol. Each Tether issued into circulation is said to be backed by a one-to-one ratio with the equivalent amount of fiat currency held in a custodial account by Hong Kong-based Tether Limited.

#### US Dollar Coin ($USDC) 

(Coinbase) Issued and managed by a trusted party, has a considerable market cap

>  Fully collateralized US dollar ERC20 tokens founded by CENTRE,  a joint venture founded by Circle and Coinbase. USDC is an open-source project which operates within US money transmission laws. The project uses established banks and auditors while leveraging Ethereum-based smart contracts.


#### True USD

>  A USD-backed ERC20 stablecoin that is fully collateralized, legally protected, and transparently verified by third-party attestations. TrueUSD uses multiple escrow accounts to reduce counterparty risk and to provide token-holders with legal protections against misappropriation. TrueUSD is the first asset token built on the TrustToken platform.

#### Paxos Standard 

> Backed one-to-one by USD deposits and available through Paxos. PAX is available one-to-one in exchange for USD and redeemable one-to-one for USD. Upon redemption, PAX tokens are immediately removed from the supply; PAX are only in existence when the corresponding dollars are in custody.

#### Gemini Dollar ($GUSD)

> Created at the time of withdrawal from the Gemini platform. Gemini customers may exchange US dollars for Gemini dollars at a 1:1 exchange rate by initiating a withdrawal of Gemini dollars from their Gemini account to any Ethereum address they specify.

#### Binance USD

#### HUSD

#### StableUSD (USDS)

> Stably is the startup behind the StableUSD token. The StableUSD stablecoin is pegged against the US dollar at a 1:1 ratio. The collateral itself is held by Prime Trust, an American trust company. StableUSD is slightly different from other fiat-collateralized stablecoins as they allow you to deposit cryptocurrencies such as Bitcoin, Ethereum, or the USDT stablecoin to buy USDS tokens.

#### BitUSD

### **Crypto-Fiat Hybrids**

#### **Reserve tokens ($RSV)**

> Hybrid-collateralized token backed by both fiat and digital assets. Initially built on Ethereum, Reserve tokens aim to be interoperable across any blockchain in the future. Similar to Maker Dai, Reserve tokens utilize a governance token, $RSR, to monitor price stability in a decentralized fashion. #burning

- [Warning on Reddit](https://www.reddit.com/r/CryptoMoonShots/comments/knzgct/warning_about_reserve_protocol_stay_away_from_rsr/)


#### **FRAX** (USDC)

[Backed by USDC](https://support.usdc.circle.com/hc/en-us/articles/360016060352-Can-a-customer-send-USDC-tokens-to-any-address-Can-addresses-be-blacklisted-)

### **Crypto-Collateralized**

#### [A Public Good Stablecoin](https://www.ergoforum.org/t/a-proposal-for-a-public-good-stablecoin/3432)

#### AgeUSD/SigmaUSD/Djed

#### **Maker DAO/DAI – valued $940M**

> Dai is a crypto-collateralized ERC20 token backed by an excess amount of digital asset collateral (most commonly $ETH) through Maker Vaults. Dai utilizes smart contracts and a governance token, $MKR, to monitor price stability.  

Generally regarded as the '*best*' algorithmic stablecoin

Advantage SigmaUSD has over **MakerDAO** : 

- No liquidation on price-spike
- Unlike Ethereum-based crypto-backed stablecoins, such as DAI, Emurgo introduces a Staticoin protocol-inspired design that does not rely on CDPs (Collateralized Debt Positions). The reason for this is the vulnerability of CDP-based protocols in terms of high volatility and blockchain congestion.As Emurgo states, “Black Thursday,” when MakerDAO CDPs were triggered for liquidation due to volatility and then sold for $0 due to blockchain congestion that prevented others from bidding, demonstrated that a new design is needed. For AgeUSD, this scenario is not possible.
- For those unfamiliar with the MakerDAO system, the entire project is centred around the governance, growth and expansion of the Dai ecosystem. While Ether  and Basic Attention Token are currently the only forms of collateral supported to mint Dai, it’s common knowledge that Maker will gradually introduce new collateral types over the course of the next few years.
- Maker provides an innovate mechanism for users to further leverage their belief in cryptocurrencies. Unlike fiat-collateralized stablecoins which use centralized reserves to retain custody of the fiat used to create new tokens, Maker’s system leverages smart contracts to hold the underlying system in escrow.

#### [RAI](https://reflexer.finance/)

> RAI provides a stablecoin protocol with the capabilities for eschewing the fiat-pegging aspect in stablecoins. It features considerable similarities with the deprecated, single-collateral DAI by MakerDAO. Users could deposit Ether in a ‘safe,’ just like DAI vaults. The minimum collateralization rate in the case of this example in algorithmic stablecoins list is just below 150%. Users would receive RAI tokens in return. The algorithm of RAI features a dedicated PID controller, which receives an input of the existing price of RAI. Then, it makes adjustments in the supply according to the price by following a continuous feedback loop.

> Most importantly, all the parameters are hard-coded in the algorithm alongside ensuring responsive, automatic reactions to market data without direct manual intervention. Apart from the value benefit of ‘self-peg,’ RAI presents considerable differences from DAI in terms of governance. It aims to take various parameters of governance out of the process in 2022, thereby reducing the need for depending on governance.

#### FEI

> FEI is also another notable protocol you could find in an algorithmic stablecoins list. It focuses on addressing the capital inefficiencies identified in the case of stablecoins such as DAI. FEI presents stark differences in comparison to other algorithm-based stablecoins. One of the foremost differences refers to the fact that it does not feature the mechanism for swapping collateral for stablecoin. On the contrary, digital wealth comes into the system by leveraging a bonding curve, which sells FEI in exchange for ETH. Then, the digital wealth remains locked in the Protocol Controlled Value or PCV, which is basically the pool of collateral for the stablecoin.

> PCV helps in maintaining the peg by managing liquidity on exchanges like Uniswap. With the limitations on sell-side liquidity, FEI is one of the best algorithmic stablecoins for avoiding the ‘death spiral’ scenario. The FEI protocol leverages its TRIBE token for enabling holders to determine the following aspects of governance,


#### **Equilibrium ($EOSDT)**

Decentralized stablecoin on the EOS blockchain (PoS). 

#### **Synthetix ($sUSD)**

> Previously known as Havven, Synethetix is a crypto-collateralized network enabling the creation of on-chain synthetic assets on the Ethereum blockchain. These assets are over-collateralized to provide sufficient liquidity for users to redeem collateral at face value. Beyond $sUSD, Synthetix plans to offer stablecoins for other legal tenders such as the euro, yen, and the Korean won.

#### MIM

### **Seigniorage**

#### **TerraUSD (UST) ($LUNA)**

TerraUSD (UST) is a stablecoin built on the Terra blockchain. Following a successful launch and increased adoption of Terra, the printing of UST commenced in September 2020. UST is not technically collateralized. Rather, the creation of UST is enabled by the burning of the LUNA coin.

- Terra is a stablecoin that achieves price-stability via an elastic money supply, enabled by stable mining incentives.
- The protocol ensures price-stability by algorithmically expanding and contracting supply. It also uses seigniorage created by its minting operations as transaction stimulus, thereby facilitating adoption.
- Pegged to the world’s major currencies, Terra aims to be able to support a global payment network.
- The team believes that a currency that cannot be used at checkout is useless. Terra is partnered with an alliance of eCommerce platforms, collectively pushing $50 billion in annual transaction volume with 50 million users. Terra aims to become a medium of exchange at a massive scale.

#### xUSD (Haven/XHR)

- https://havenprotocol.org/2021/01/25/spotlight-on-xusd/
- https://havenprotocol.medium.com/why-haven-protocols-xhv-offshore-storage-is-the-best-crypto-stable-coin-storage-solution-61f118129784

#### DexyUSD

### Gold-Backed

https://www.stablecoinswar.com/gold-stable-coins.php

#### Digital Gold (GOLD)

#### Tether Gold (XAUT)

#### PAX Gold (PAXG)

#### Digix Gold Token (DGX)

## Notes

#### asset-backed

#### asset-backed (volatile)

#### algorithmic

- non-custodial
   - Implicit Collateral
   - Endogenous Collateral
   - Exogenous Collaterol
- custodial
   - Reserve Fund
   - Fractional Reserve Fund
      - Money Market Fund
      - Bank Fund
   - Central Bank
