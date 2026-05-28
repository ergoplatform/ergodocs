# Welcome to the Ergo Ecosystem

/// details | Explore the Ergo Universe!
    {type: tip, open: true}
Check out [sigmaverse.io](https://sigmaverse.io/) - ***your portal to the Ergo Universe*** !
///

Use this page as the main map for user-facing Ergo applications, protocols, and project pages. If you are not sure where a project belongs, start with [Ecosystem Map](ecosystem-map.md) or [Using Ergo](using-ergo-intermediate.md).

## Common Paths

| I want to... | Start here | Related pages |
| --- | --- | --- |
| Choose a wallet | [Get a Wallet](wallets-overview.md) | [Wallets Overview](wallets.md), [Security Basics](security-basics.md) |
| Swap or trade | [DEX Overview](dex.md) | [Spectrum](spectrum.md), [P2P Trading](p2p-trading.md), [PiggyTrade](piggytrade.md) |
| Use stablecoins | [Stablecoins](stablecoins.md) | [SigmaUSD](sigmausd.md), [Dexy](dexy.md), [Gluon](gluon.md) |
| Bridge assets | [Rosen Bridge](rosen.md) | [Transfer Flows](token-transfer-flows.md), [Troubleshooting](rosen-troubleshooting.md) |
| Mint or trade NFTs | [NFT Overview](nft.md) | [ErgoAuctionHouse](ergo-auctions.md), [SkyHarbor](skyharbor.md) |
| Explore games | [Gaming](gaming.md) | [NFT Races](nft-races.md), [Cyberverse](cyberverse.md) |
| Use privacy tools | [Privacy Guide](privacy-guide.md) | [ErgoMixer](ergomixer.md), [Stealth Addresses](stealth-address.md) |
| Find recent experiments | [Emerging Projects](emerging-projects.md) | [BoTTube](bottube.md), [Ergo Agent SDK](ergo-agent-sdk.md) |

## Ecosystem Areas

Ergo’s ecosystem is built on a solid foundation of key technologies and applications that cater to diverse use cases.

### Infrastructure

Explore the underlying technologies that power the Ergo blockchain, including our robust Proof of Work consensus algorithm, sidechains, bridges, and oracle systems. These components ensure the scalability, security, and interoperability of the Ergo network.

### Financial Tools

Dive into the financial applications and services within the Ergo ecosystem, including decentralized exchanges, stablecoins, lending platforms, and derivatives. These tools offer users new ways to manage, trade, and grow their assets in a trustless, decentralized environment.

### Privacy Solutions

Ergo is at the forefront of privacy innovation with solutions like non-custodial mixers and stealth addresses. These tools ensure that users can conduct transactions with enhanced privacy while maintaining the security and transparency of the blockchain.

### Decentralized Governance

Discover the tools and platforms that enable decentralized governance within the Ergo ecosystem, including DAOs and community-driven initiatives. These components allow users to participate in decision-making processes and contribute to the future development of the network.

### Gaming and Metaverse

Ergo supports a growing number of gaming and metaverse projects, offering developers the tools they need to create immersive, blockchain-based experiences. From trading card games to expansive virtual worlds, the Ergo ecosystem is home to innovative entertainment platforms.

### Tooling and Developer Resources

Get access to a suite of [developer tools](building-on-ergo-developers.md) and resources designed to create and deploy decentralized applications on Ergo. From smart contract scripting to name services, these tools are essential for building on Ergo.

### Further Ideas and Innovation

Explore new and experimental ideas within the Ergo ecosystem that push the boundaries of what's possible with blockchain technology. This section highlights ongoing research and development efforts aimed at expanding the capabilities of the network.

## Explore the Ecosystem

Use the navigation on the left or the tables above to explore each section. For a shorter cross-site map, use [Ecosystem Map](ecosystem-map.md).

Join us in building the future of decentralized finance and beyond.

## Conceptual Example: Programmable Contracts

Even the most complex use case is simpler than general-purpose software that can be used to program any contract. After all, generalized logic must be both far-reaching and secure. Moreover, even a specialized contract comprises many steps, each of which is fairly simple. Thus, another requirement for a general-purpose platform is that it should simplify the process of writing contracts, making them as accessible (and safe) as possible. This can be achieved using template agreements with customizable parameters.

Consider the following example illustrating how programmable contracts on Ergo can handle complex financial interactions:

### Gold-backed Tokens Example

Alice uses ERGs to purchase gold-backed tokens from Bob. Bob stores the gold in a secure vault and uses the blockchain to issue one token for every Troy ounce of gold he holds. Alice can then use these tokens freely in different contracts, transferring and trading them under whatever conditions she specifies in the smart contract code. When Alice wants to sell the tokens for physical gold, she can conduct another transaction with Bob, receiving ERG in return at the market price.

The point of blockchain contracts is to eliminate the need for trust. While the purchase transaction is now trustless, in this instance, Alice still needs to trust Bob about two things:

1. Bob may refuse to swap the gold tokens back to ERG at the correct price when Alice wants to sell.
2. Bob may default on his obligations – running away with the gold or misusing the funds he receives and operating a fractional reserve.

### Extending the Contracts with Oracles and Insurance

We can create an [Oracle](oracles.md) or decentralized price feed to address these issues. This uses multiple external data sources to record the price of gold on the blockchain at regular intervals. This price feed will be the reference point for the redemption contract that manages the sale of Alice's gold with Bob (or any other participant). Thus, the system automatically enforces the right price when a swap takes place.

The second situation requires a third-party insurer, Charlie, whose service is also hosted on the blockchain with a smart contract (perhaps an [Insurance dApp](insurance.md)). When Alice purchases gold from Bob, she additionally buys an insurance contract from Charlie. The payment can depend on factors like the amount of insurance required and Bob's reputation, managed by a decentralized feedback mechanism. Now, if Bob defaults, Alice will automatically receive the value of her gold tokens, with Charlie effectively acting as a buyer of last resort.

Charlie may even sell shares in his insurance business to Dave and other participants, providing them with a proportion of revenues to ensure he has the capital he needs to cover any liabilities from the outset.

This example demonstrates how Ergo's programmable contracts can model complex, multi-party financial agreements in a secure and trust-minimized way.

## Core Components

::cards::

[
  {
    "title": "Autolykos",
    "content": "The underlying Memory-hard ASIC-resistant **Proof of Work** (PoW) algorithm oriented towards GPUs. ",
    "url": "../mining/autolykos.md"
  },
  {
    "title": "eUTXO",
    "content": "Ergo uses a so-called *extended-UTXO model*, which implies UTXOs with the ability to contain *arbitrary data and sophisticated scripts*. ",
    "url": "../dev/protocol/eutxo.md"
  },
  {
    "title": "NIPoPoWs",
    "content": "Enable extended support of light nodes which makes Ergo friendly for end-users, allowing them to run contracts on common devices such as mobile phones without centralised intermediaries. ",
    "url": "../dev/protocol/nipopows.md"
  },
  {
    "title": "Privacy",
    "content": "Ergo provides **superior access to discrete log-based zero-knowledge proofs**",
    "url": "../dev/protocol/zkp.md"
  },
  {
    "title": "Scaling",
    "content": "Explore the various scaling solutions being explored on Ergo.",
    "url": "../dev/protocol/scaling.md"
  },
  {
    "title": "Storage Rent",
    "content": "Storage Rent is a nominal fee incurred by unmoved boxes after four years.",
    "url": "../mining/rent.md"
  },
  {
    "title": "ErgoScript",
    "content": "A simple high-level language enabling clear descriptions of contractual logic.",
    "url": "../dev/scs/ergoscript.md"
  },
  {
    "title": "Oracles",
    "content": "The messengers in and out of blockchains. Ergo Blockchain’s design allows Oracle Pools, protected by *trust heirarchies*.",
    "url": "oracles.md"
  },
  {
    "title": "Parachains/Sidechains",
    "content": "",
    "url": "../dev/protocol/nipopow/nipopow-sidechains.md"
  }
]

::/cards::
