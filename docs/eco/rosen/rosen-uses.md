# Rosen Bridge: Connecting Cardano, Ergo, Bitcoin, Ethereum, Dogecoin, and Binance Smart Chain

Rosen Bridge enables seamless movement of value across Cardano, Ergo, Bitcoin, Ethereum, Dogecoin, and Binance Smart Chain (BSC). Rather than swapping native tokens directly, Rosen locks the native asset on its origin chain and mints a representation (rsToken) on the destination chain. Examples:
- ADA to rsADA on Ergo
- ERG to rsERG on Cardano
- BTC to rsBTC on Ergo or Cardano
- ETH to rsETH on Ergo or Cardano
- BNB to rsBNB on Ergo or Cardano (check asset list for current availability)

This unlocks cross-ecosystem DeFi, liquidity, and utility without sacrificing origin-chain exposure.

## What you'll get

- Access to all existing and future networks integrated with Rosen Bridge (Ergo, Ethereum, Bitcoin, Cardano, Dogecoin, BNB Chain) with one integration
- Lock the native asset on the origin chain and mint an rsToken on the target
- Use assets as native on Cardano and Ergo with wallets, DEXs, lending, and options
- Create liquidity pools across the ecosystems you choose
- Build sustainable liquidity on-chain, fewer exchange fees, market maker retainers
- Access to stablecoins, ecosystem and protocol tokens from the Rosen network of chains.
- Path to Monero support that preserves privacy: see [Bringing Monero](bringing-monero.md)
- Runes plus support to bring stablecoins and rich assets to Bitcoin layer one (upcoming) — see [A Runes strategy for rich cross-chain assets](https://curiaregiscrypto.medium.com/a-runes-strategy-for-rich-cross-chain-assets-c6868b7d4ac3)

## Integration Opportunities and Tutorials

When Rosen adds a new network, typical opportunities open up immediately for LPs, traders, and protocols. Always verify token contracts via the Rosen assets page before interacting.

| Opportunity | Ergo (Spectrum) | Cardano (Minswap/Spectrum) | Ethereum (Uniswap) | BSC (PancakeSwap) | Tutorials/Guides |
|---|---|---|---|---|---|
| Provide LP for bridged rsTokens (e.g., rsERG/ETH, rsBTC/XY) | [Spectrum DEX](spectrum.md) | Minswap (https://app.minswap.org/) / Spectrum | Uniswap (https://app.uniswap.org/) | PancakeSwap (https://pancakeswap.finance/) | Uniswap rsERG LP guide: [rsERGLP.md](rsERGLP.md) • DEX overview: [dex.md](dex.md) • Minswap Docs: https://docs.minswap.org • PancakeSwap Docs: https://docs.pancakeswap.finance |
| Swap/Trade bridged rsTokens | [Spectrum DEX](spectrum.md) | Minswap / Spectrum | Uniswap | PancakeSwap | DEX overview: [dex.md](dex.md) • Uniswap Help: https://support.uniswap.org |
| Lend/Borrow (when listed by protocol) | [DuckPools](duckpools.md) | Liqwid (https://v2.liqwid.finance/) / Lenfi (https://app.lenfi.io/) | Varies by listings | Varies by listings | DuckPools Docs: https://docs.duckpools.io • Liqwid Docs: https://docs.liqwid.finance • Lenfi Docs: https://docs.lenfi.io |
| Options/Derivatives (where available) | [SigmaO](sigmao.md) | — | — | — | [sigmao.md](sigmao.md) |
| Privacy (where available) | [ErgoMixer](ergomixer.md) | — | — | — | [ergomixer.md](ergomixer.md) |
| NFT Trading/Marketplace (where available) | [Auction House](ergo-auctions.md) | Cardano marketplaces | EVM marketplaces | EVM marketplaces | [ergo-auctions.md](ergo-auctions.md) |

Notes:
- “When listed/where available” means the opportunity exists once the asset is supported on that venue. Listings and pools are created permissionlessly on many DEXs, but lending markets and some venues are curated.
- For LP creation on Uniswap with rsERG, follow the detailed tutorial: [rsERGLP.md](rsERGLP.md).

## Quick How-To: Bridging with Rosen

- Open the Rosen app: https://app.rosen.tech/
- Select source chain and target chain
- Enter your destination address on the target chain
- Choose token and amount
- Review displayed bridge fees and confirm

Tips:
- If you see “insufficient ERG” but have funds, consolidate in Nautilus (Wallet Optimization).
- Typical transfers take around ~2 hours; delays are possible.
- Track status via Rosen Events: https://app.rosen.tech/events

## Supported Tokens and Live Status

View the live list of locked assets and metadata here:
- https://app.rosen.tech/assets

Below are examples by network (not exhaustive — always verify using the assets page).

### Ergo Network (examples)
| Token | Description |
|-------|-------------|
| ERG   | Native Ergo token |
| [SigUSD / SigRSV](sigmausd.md) | Ergo stablecoin and reserve |
| RSN   | Rosen Bridge token |
| [COMET](https://thecomettoken.com/) | Ergo ecosystem token |
| SPF   | Spectrum Finance token |
| AHT   | ergouactions.org |
| Bober | [Meme Coin](https://t.co/DXEIXJC8AW) |
| COS   | [Cup of Sugar](cup-of-sugar.md) |
| EPOS  | [tabbypos](tabbypos.md) Point of sale |
| ErgOne| [ErgOne](ergone.md) |
| GIF   | GreasyCex |
| GluonW GAU | [Gluon](gluon.md) |
| GluonW GAUC | [Gluon](gluon.md) |
| MEW   | [MewFinance](mew-finance.md) |
| Paideia | [DAO Toolkit](paideia.md) |
| QUACKS | [Duckpools](duckpools.md) (Lending) |
| Troll | New supported token |
| WALRUS| New supported token |
| CYPX  | [Cyberverse](cyberverse.md) |

### Cardano Network (examples)
| Token | Description |
|-------|-------------|
| ADA   | Native Cardano token |
| Hosky | Cardano meme token |
| NIKEPIG | Cardano meme token |
| SUGAR | New supported token |
| BANA  | New supported token |
| O     | New supported token |
| DIS   | New supported token |
| sOADA | New supported token |
| OADA  | New supported token |
| MNT   | New supported token |

### Bitcoin Network (examples)
| Token | Description |
|-------|-------------|
| BTC   | Native Bitcoin token |

### Ethereum Network (examples)
| Token | Description |
|-------|-------------|
| ETH   | Native Ethereum token |

### Dogecoin Network (examples)
| Token | Description |
|-------|-------------|
| DOGE  | Native Dogecoin token |

### Binance Smart Chain Network (examples)
| Token | Description |
|-------|-------------|
| BNB   | Native Binance Smart Chain token |

## Ecosystem Opportunities

### Ergo

- Token swaps and LP
   - Use [Spectrum Finance](spectrum.md) to acquire rsADA, rsBTC, rsETH, rsBNB, or ecosystem tokens.
- [Auction House](ergo-auctions.md)
   - Decentralized NFT and token marketplace; accepts rsADA, rsBTC, rsETH, and rsBNB. List in bulk or make offers.
- SigmaFi
   - Decentralized P2P bonds market using wrapped tokens as collateral: https://sigmafi.app/#/
- DuckPools
   - Lend rsADA, rsBTC, rsETH, rsBNB and other supported tokens: https://www.duckpools.io/
- [ErgoMixer](ergomixer.md)
   - Enhance privacy by mixing wrapped tokens.
- [SigmaO](sigmao.md)
   - Create American-style call and put options on wrapped tokens.

Tip: Short on ERG for fees? Use [babel-fees](babel-fees.md) to pay Ergo transaction fees with supported tokens.

### Cardano

- Cardano DEXs
   - Gain exposure to Ergo, Bitcoin, Ethereum, and BSC bridged tokens on Cardano DEXs like Spectrum, Minswap, and SundaeSwap.
- Liqwid Finance
   - DeFi markets for bridged assets (e.g., rsERG, rsBTC, rsETH, rsBNB): https://v2.liqwid.finance/market/ERG
- Lenfi
   - Explore lending and borrowing with bridged assets: https://app.lenfi.io/

### Ethereum

- Trade and LP on Uniswap
   - rsERG/ETH pool (1% fee tier). See the full step-by-step Uniswap LP guide: [Participating in rsERG Liquidity Pools](rsERGLP.md)
   - You can also add liquidity to the rsBTC pool (Uniswap UI supports direct pool links).
- Token details and safety
   - rsERG (Ethereum) token contract: 0x6C060Ba738af39A09F3b45ac6487dFC9Ebb885f6  
     Always verify against the Rosen [assets page](https://app.rosen.tech/assets) or Etherscan.
- Notes
   - Gas fees are variable — consider batching actions where appropriate.
   - Use hardware wallets and only import verified token contracts.

### Bitcoin

- Bitcoin is a source chain for BTC -> rsBTC on Ergo/Cardano. Users can utilize rsBTC in DeFi on Ergo/Cardano (e.g., LPing, lending, options), then bridge back to native BTC if desired.

### Binance Smart Chain (BSC)

- BSC support and bridged assets are evolving. Check the live assets page for current availability and integrations: https://app.rosen.tech/assets

## Best Practices and Risk Notes

- Verify assets and contracts via the official Rosen assets list before interacting.
- Bridging involves multiple chains and confirmations — delays can occur.
- DeFi carries risks (smart contract risk, liquidity risk, impermanent loss).
- Prefer reputable DEXs, audited protocols, and hardware-wallet flows.
- Monitor your transactions via Rosen Events: https://app.rosen.tech/events

## Future Developments

Rosen continues to expand supported assets, routes, and protocol integrations. Expect deeper DeFi liquidity, additional pools and markets across Cardano, Ergo, Ethereum, and BSC, and broader utility for rsADA, rsERG, rsBTC, rsETH, rsBNB, and other bridged tokens.
