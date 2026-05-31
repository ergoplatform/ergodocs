---
tags:
 - ecosystem
 - directory
---

# Ergo Ecosystem

Use this page as the main map for Ergo applications, protocols, and project pages. For ordinary wallet tasks, start with [Using Ergo](using-ergo-intermediate.md). For a shorter cross-site route, use the [Ecosystem Map](ecosystem-map.md). For long-tail project pages, use the [Project Directory](project-directory.md).

/// details | External directory
    {type: tip, open: true}
[Sigmaverse](https://sigmaverse.io/) is the external ecosystem portal for browsing projects beyond these docs.
///

## Choose an Area

| Goal | Start here | Related pages |
| --- | --- | --- |
| Bridge assets | [Rosen Bridge](rosen.md) | [Transfer flows](token-transfer-flows.md), [troubleshooting](rosen-troubleshooting.md), [watcher operations](watcher.md) |
| Swap or trade | [Decentralized Exchanges](dex.md) | [Spectrum](spectrum.md), [Mew Finance](mew-finance.md), [P2P Trading](p2p-trading.md) |
| Use stable assets | [Stablecoins](stablecoins.md) | [SigmaUSD](sigmausd.md), [Dexy](dexy.md), [Gluon](gluon.md) |
| Explore DeFi | [Lending](lending.md) | [duckpools](duckpools.md), [SigmaFi](sigmafi.md), [Options](financial-options.md) |
| Mint or trade NFTs | [NFTs](nft.md) | [ErgoAuctionHouse](ergo-auctions.md), [SkyHarbor](skyharbor.md), [Lilium](lilium.md) |
| Find games | [Gaming](gaming.md) | [BlitzTCG](blitz.md), [Cyberverse](cyberverse.md), [SigmaQuest](sigmaquest.md) |
| Use privacy tools | [Mixing Overview](mixer.md) | [ErgoMixer](ergomixer.md), [SigmaJoin](sigmajoin.md), [Stealth Addresses](stealth-address.md) |
| Browse project pages | [Project Directory](project-directory.md) | [Sigmaverse](sigmaverse.md), [BoTTube](bottube.md), [Degens.World](degens-world.md) |
| Explore miner-facing apps | [Miner Tooling](miner-tooling.md) | [GuapSwap](guapswap.md), [Lithos](lithos.md), [CYTI](cyti.md) |

## Ecosystem Sections

### Infrastructure

Cross-chain, oracle, and sidechain material lives here. Start with [Rosen Bridge](rosen.md) for bridging, [Oracles](oracles.md) for data feeds, and [Sidechains](sidechains.md) for sidechain research and designs.

### Finance & Markets

Use this area for trading, stable assets, lending, derivatives, crowdfunding, and token-economic experiments. Start with [DEXs](dex.md), [Stablecoins](stablecoins.md), or [Lending](lending.md).

### NFTs & Gaming

Use this area for marketplaces, NFT standards, art projects, games, and metaverse-style experiments. Start with [NFTs](nft.md) or [Gaming](gaming.md).

### Applications & Utilities

Use this area for wallets-adjacent tools, identity, messaging, analytics, commerce, knowledge bases, and early-stage applications. Start with the [Project Directory](project-directory.md) if you are browsing.

### Privacy Solutions

Use this area for mixers, stealth-address patterns, zero-knowledge treasury ideas, and private coordination tools. Start with [Mixing Overview](mixer.md) or [ErgoMixer](ergomixer.md).

### DAO & Governance Apps

Use this area for community-governance apps and DAO tooling. Start with [DAOs](dao.md) or [Paideia](paideia.md).

### Further Ideas & Research

Use this area for speculative, research-stage, or concept-heavy projects that do not yet fit into a stable user task.

## Core Technical Foundations

These concepts explain why Ergo can support many of the applications above:

::cards::

[{
    "title": "eUTXO",
 "content": "Ergo extends the UTXO model with scripts and registers, enabling expressive contracts while keeping validation predictable.",
    "url": "../dev/protocol/eutxo.md"
  },
  {
 "title": "ErgoScript",
 "content": "ErgoScript is the high-level contract language used to describe spending conditions for boxes.",
 "url": "../dev/scs/ergoscript.md"
 },
 {
    "title": "NIPoPoWs",
 "content": "NIPoPoWs support compact proof-of-work proofs for light clients, sidechains, and related protocols.",
    "url": "../dev/protocol/nipopows.md"
  },
  {
 "title": "Oracle Pools",
 "content": "Oracle pools bring external data on-chain for financial contracts and other applications.",
 "url": "oracles.md"
  },
  {
    "title": "Storage Rent",
 "content": "Storage rent helps manage long-term state growth by allowing old unmoved boxes to be recycled under protocol rules.",
    "url": "../mining/rent.md"
  },
  {
 "title": "Autolykos",
 "content": "Autolykos is Ergo's proof-of-work algorithm and the base layer for network security.",
 "url": "../mining/autolykos.md"
 }]

::/cards::

## Next Steps

- New user: go to [Using Ergo](using-ergo-intermediate.md).
- Builder: go to [Building on Ergo](building-on-ergo-developers.md).
- Operator: go to [Operate Infrastructure](operate-infrastructure.md).
- Contributor: use [Ecosystem Standards](ecosystem-standards.md) before adding or updating project pages.
