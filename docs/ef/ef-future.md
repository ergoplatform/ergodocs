---
tags:
  - Ergo Foundation
  - Future
  - Roadmap
  - Community
---

# The Ergo Foundation's Future

/// details | What's been done so far?
     {type: info, open: true}

- For an overview of what has been achieved since launch, please see [this page](roadmap.md)
- For a comprehensive overview of the scope of the Ergo Foundation see [this page](ef-scope.md)
///

## Initial Role of the Ergo Foundation

The Ergo Foundation's initial role was to bootstrap the Ergo ecosystem in the early years and build the necessary infrastructure to facilitate adoption, addressing the 'hard side' of Ergo. This has led to the vibrant ecosystem we see today, with:

- Over 300 community developers
- More than 100 active contributors in the weekly developer chat on Discord
- Hosting multiple [events](events-overview.md) annually
- Over 140 projects developing on Ergo (see [sigmaverse.io](https://sigmaverse.io) for an overview)
- Consistently ranked among the top 100 for development activity on [artemis.xyz](https://app.artemis.xyz/developer-activity?ecosystemValue=Ergo)


# The Future

As the Ergo ecosystem matures, the Foundation's role is evolving. The goal has always been to build an ecosystem that can sustain itself without centralised support. That transition is now accelerating. The Foundation's treasury is now nearing depletion, and the organisation no longer has independent funding to operate as it once did. However, this does not mark the end of the Foundation's relevance.

The Ergo Foundation DAO has been renewed for another year, allowing the Foundation to continue serving a critical function: acting as a legal entity that can sign agreements on behalf of community-driven initiatives. When community members or projects raise funds, the Foundation can formalise partnerships, engage service providers, and interact with centralised entities requiring legal counterparty signatures. This "signatory services" model ensures the ecosystem maintains access to exchanges, onramps, and institutional partnerships that require traditional legal frameworks.

The Foundation remains committed to its foundational objectives:

- Promoting blockchain technology for societal benefit
- Advocating for truly decentralised infrastructure
- Upholding privacy as a fundamental human right

The optimal path forward involves building robust infrastructure that positions the ecosystem for future liquidity shifts from legacy systems. Emphasis remains on user security, privacy, and long-term resilience. The Foundation may continue indefinitely as a legal wrapper, but operational funding must now come from the community it serves.

## The Sigmanauts Program

The Sigmanauts Program is a grassroots initiative designed to empower individuals to take ownership of Ergo's future. Launched to build the structures necessary for community self-governance, it enables contributors to shape development priorities, manage resources, and drive ecosystem growth independently. This program represents the practical implementation of the handover strategy.

# The Transition

The treasury successfully bootstrapped Ergo's early years. That phase is complete. We are now in active transition, preparing to hand over remaining core functions to community-led entities. **The Foundation's operational runway has effectively concluded**—there are no longer sufficient funds to support grants, development initiatives, or market-making operations from the central treasury.

This transition has been anticipated. Documentation, ownership maps, and named community stewards are in place so that handover can proceed at short notice. The goal is to preserve continuity of critical services—exchange listings, onramp access, and infrastructure maintenance—while shifting responsibility and funding to the community.

Current treasury balances and burn rates remain transparently published. Remaining funds cover active grant commitments and minimal operational overhead. The Foundation's ongoing value lies in its legal personality: the ability to sign agreements when the community raises funds for specific initiatives. This ensures that decentralised projects can still interface with the traditional financial and legal systems when necessary.

## Key Implications

- **Community-funded initiatives**: Projects requiring Foundation signatory services must secure their own funding. The Foundation provides the legal framework; the community provides the resources.
- **DAO renewal**: The DAO's one-year renewal provides a window for the community to establish alternative structures or fund specific initiatives through the Foundation.
- **Exchange and partner access**: The Foundation's legal entity status ensures continuity of relationships with centralised exchanges and service providers that require formal agreements.
- **Decentralisation milestone**: The depletion of central treasury funds, while challenging, represents progress toward the ecosystem's ultimate goal of genuine decentralisation.

This transition from a funded entity to a community-driven ecosystem is intentional. It follows a structured handover of responsibilities and reflects the natural evolution of a decentralised project. The Foundation's role has shifted from primary driver to facilitator—ready to sign agreements, maintain legal continuity, and support community-funded initiatives, but no longer operating as an independent funding source.

### Handover of Core Responsibilities

As the Foundation's funding ceases, the operational services it maintained have been successfully migrated to various community groups:

* **Development:** All core protocol funding has transitioned to community-driven efforts, primarily organized through the **DevDAO**.
  * Key ecosystem projects, like the **Nautilus wallet**, must also finalize their transition from EF funding to self-sustaining models. The community will need to explore new funding mechanisms to support them, such as direct donations, subscription models, bounties, community raffles, or applying for grants from the DevDAO.
* **Infrastructure & Hosting:** The **InfraDAO** has successfully assumed responsibility for the vast majority of ecosystem infrastructure. The final item, the hosting of the `ergoplatform.org` website, is in the process of its final transfer from the EF to this community entity.
* **Social Media & Community Management:** The **Sigmanauts program** has taken full ownership of key social channels, including the primary `@ergo_platform` (X) account. This group now manages community engagement, news dissemination, and outreach independently of the Foundation.
* **Editorial & Content:** Content creation and editorial oversight are being integrated into new community structures, such as a dedicated **"EditorialDAO"** or being absorbed by the InfraDAO, to ensure high-quality communication continues.

### The Foundation's Evolving Role

With its operational treasury depleted and its day-to-day duties fully transferred to the community, the Ergo Foundation will contract to a minimalist state whose purpose will be to persist as a minimal legal entity for as long as is required. The ongoing cost for this (approximately $2,000 per year) is worthwhile, as it provides a crucial function that a decentralized body cannot: **acting as a legal signatory.** This is vital for interactions with centralized entities, such as signing new exchange listing agreements or contracts for community-crowdfunded initiatives.

While the Foundation will no longer have an operational treasury for grants, it does hold a potential long-term, illiquid asset: a future claim on a significant portion of Rosen Bridge's RSN token (approximately 2% of the total supply), which may not be accessible for years.

Should this asset gain significant value in the distant future, the Foundation (or a community-appointed successor DAO) would be positioned to manage these funds, distributing them or using them as best determined by the community to further Ergo's decentralized mission.

The future sustainability, resilience, and growth of Ergo are now, by design, fully in the hands of the community, the DAOs, and the robust, decentralized infrastructure built over the past several years.


### Innovation in the Community Era: Current Ecosystem Momentum

The transition to a fully community-led ecosystem has not slowed development. Instead, active work continues on new applications and protocol refinements. As of early 2026, a primary focus of this new development is the creation of "bottom-up" financial tools and new models for monetary issuance.

Several key projects are advancing, demonstrating the continued activity from decentralized contributors.

#### 1. Core Protocol and Infrastructure Upgrades

Work continues on the foundational layer of the protocol to improve security, scalability, and decentralization.

* **SigmaV6 Live:** The SigmaV6 update is live, hardening the network's foundational cryptographic security and efficiency.
* **Node Releases 6.0.3 & 6.0.4:** Preparing PRs for upcoming node releases. The plan is to release 6.0.3 and 6.0.4 in the coming weeks, then extract sub-blocks related PRs for review one-by-one. See the [release plan on GitHub](https://github.com/ergoplatform/ergo/pull/2291).
* **Sub-blocks in Devnet:** The sub-blocks scaling solution has progressed significantly in devnet testing. The devnet is now running with 3-4 mining peers, using 60s average ordering block delay with 60 input blocks per ordering. Occasional issues with candidate block generation and ordering block syncing are being addressed. A monitoring script for devnet stress testing has been created, tracking input block production rate, ordering block commits, TX inclusion rates, input chain reorganizations, and time since last ordering block.
* **Lithos Testnet:** The **Lithos** project is approaching its testnet launch. It aims to provide a **blockchain-agnostic, decentralized mining pool infrastructure** to address centralization risks in Proof-of-Work mining.
* **Ergo Book:** A new effort to conceptualize the ideological and philosophical foundation of the Ergo movement alongside technical documentation. Now built as an mdbook for simplified publishing and self-hosting. Contributors are welcome—see the [current structure draft](https://github.com/kushti/ergo-book/blob/master/src/SUMMARY.md).

#### 2. New Monetary and Financial Primitives

A significant area of focus is the development of new financial applications that leverage Ergo's eUTXO model.

* **USE (Ultimate Stable E-coin):** A Dexy-based, crypto-backed algorithmic stablecoin pegged to USD. It is based on the previously tested DexyGold design.
    * **Status:** The v2 USD pool is launched, and the DORT (USD oracle reward token) liquidity pool has been bootstrapped.
    * **Recent Progress:** [UIP-001: Balancing the Interventions](https://github.com/kushti/dexy-stable/pull/7) is under review, addressing how to handle rapid ERG price drops on exchanges. Intervention bots (98% and 101%) and a DORT buy-back bot are now operational.
* **GitCircles:** A **community currencies framework** designed for open-source developer communities.
    * **Status:** This project is being developed by a team new to the Ergo ecosystem. Manual testing is underway, and a testing liquidity pool is being established before onboarding the first communities.
* **Basis (ChainCash):** This simplified version of Chaincash enables off-chain cash backed by on-chain reserves. The model allows notes to be backed by blockchain assets or by peer-to-peer trust, creating a framework for localized credit.
    * **Status:** Fixed the missed R6 register in the offchain server and resolving various redemption issues. The intended application extends beyond simple wallets for human interaction; the goal is to use Basis for agent-to-agent payments and P2P network incentives, potentially serving as an alternative to many "DePIN" models.

#### 3. Ecosystem and Interoperability Growth

In parallel, other key ecosystem components are also advancing to improve user access and connectivity.

* **Rosen Bridge Expansion:** The **Rosen Bridge** is preparing its next integrations: **Runes and Monero (XMR)**. Additionally, teams from **Firo** and **Handshake** are working on integrations using the Bridge Expansion Kit, with Firo extractor, address codec, and scanner implementations already merged or under review.
* **Citadel Desktop App:** A new desktop application for interacting with Ergo DeFi. [v0.2.0-alpha](https://github.com/arkadianet/citadel/releases/tag/v0.2.0-alpha) has been released, with swap functionality tested using both local and remote nodes. Borrowing on Duckpools is still in development.
* **Ergo Mobile Wallet (Degens.World):** A fork of Ergo Wallet with a new UI, now in testing. Desktop mode is functional, Android testing is underway, in-wallet swap functionality is complete, and the dapp browser is being finalized. Published on Google Play for internal testing with beta release expected soon.
* **ErgoMonitor:** A monitoring bot with significant updates—fixed ERG/USD pricing to fetch directly from on-chain oracle data, added charts for Spectrum and Dexy pools (`/dexchart` command), whale notifications for Dexy LP swaps, and automatic RosenBridge token map updates.
* **CyberPets Racing:** An NFT racing game where players train and race their CyberPet NFTs from CyberVerse. Connect Nautilus to auto-discover NFTs on-chain, train them with diminishing returns, enter races, and earn UTXO-style rewards. Phase 1 is live in multi-user alpha with deterministic results seeded by Ergo block hashes; Phase 2 will move game state on-chain via ErgoScript contracts.
* **Game of Prompts:** A platform for creating AI robot competitions through Ergo contracts. Contracts and UI are now finalized, with a Telegram community created for DePIN, trustless bots, and autonomous agents.
* **Ergo Transcripts Archive:** Over 88 hours of developer call transcripts now available at [ergo-transcripts.vercel.app](https://ergo-transcripts.vercel.app/), with workflows being developed for Twitter Spaces and Reddit Community AMAs.
* **Hardware Wallet Integration:** Keystone Hardware Wallet integration is in progress, with some delays due to the latest signature curve update on Ergo requiring additional testing.
* **Sigmaverse Updates:** The ecosystem project directory is being updated with new projects and contributors, with plans for an archive section for inactive projects.
