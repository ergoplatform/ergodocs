---
tags:
  - Lithos
  - Mining Pool
  - Decentralized
  - Infrastructure
  - dApp
  - dApp-InDev
owner: docs
last_reviewed: 2026-10-21
source_repos:
  - repo: Lithos-Protocol/Lithos-Client
    branch: master
    release_watch: true
    paths:
      - README.md
      - TestnetNode.md
source_of_truth:
  - https://github.com/Lithos-Protocol/Lithos-Client
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.0.0-prerelease
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v5.4.0-test
  - https://github.com/Lithos-Protocol/LitePaper
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v5.2.0-test
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v5.1.0-test
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v5.0.0-test
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.2.0-test
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.1.0-test
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.1-test
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.0-test
  - https://github.com/Lithos-Protocol/Lithos-Client/issues/8
---

# Lithos

## Overview

Lithos is a project that aims to create a decentralized mining pool infrastructure by providing a low-risk opportunity for lenders to earn yield on their ERG by providing collateral to mining pools while promoting increasingly decentralized block production. This means that the project plans to enable miners to directly insert necessary transactions into blocks in a fully decentralized and trustless manner, bringing significant benefits to miners outside of just decentralization.

Traditionally, attempts to create decentralized mining pools have faced challenges such as security concerns, lack of miner usage, and failures to achieve both efficiency and full decentralization. However, Lithos proposes a new solution to these challenges by using a new protocol that verifies miners' work and pays them out accordingly while utilizing Stratum as the "networking layer" for the protocol. The protocol is blockchain-agnostic, meaning that Lithos may support mining pools for any Proof of Work (PoW) blockchain.
Recently, Lithos has completed collateral contracts, and the ability of miners to directly insert necessary transactions into blocks has been successfully demonstrated during the ERGOHACK VI event. Overall, the goal of Lithos is to usher in a new era for PoW mining, where mining pools are fully decentralized, efficient, and trustless.

## Current Client Status

The [Lithos Client](https://github.com/Lithos-Protocol/Lithos-Client) is the reference client for the Lithos Protocol. The current checked mainnet client is [v1.0.5](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.0.5). Follow the current README and mainnet configuration rather than the older batching-only mainnet prerelease. It requires a fully synced, indexed Ergo node v6.0.7/v6.1.7 or newer and Java 11. The current client supports mining and on-chain difficulty commitments; the earlier prerelease restrictions are historical.

The current README describes Lithos as requiring a fully synced Ergo node and Java 11. Miners connect through the Lithos Stratum server, with Rigel Miner recommended. Lithos evaluates Non-Interactive Share Proofs rather than ordinary pool shares, so the miner address and worker name used by the Stratum client are not payout identifiers in the same way they are for a conventional pool.

August 2025 dev updates said the difficulty contract and off-chain work for multiple fraud-proof contracts were finished, Stratum was being adjusted for TRM users and lower resource use, and shares were persisted across Stratum shutdowns. The same update framed this as testnet preparation rather than a production release.

Earlier SNISP/NISP research is now treated as Lithos background rather than a separate ecosystem project. See [SNISP](snisp.md) for the legacy concept page.

The first public testnet releases arrived in November 2025. [`v1.0-test`](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.0-test) introduced the testnet client package, and [`v1.1-test`](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.1-test) followed with stability fixes, Stratum error-handling changes, setup simplification, refactoring, and logging changes.

For testnet use, the client needs node API access and a testnet wallet keystore so it can sign and generate transactions. The upstream testnet guide warns users to create a new testnet-only secret key rather than reusing a mainnet wallet.

[v5.4.0-test](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v5.4.0-test) is the current testnet client. It adds LithosDex order contracts and a LithosDex batcher, supports swap/deposit/redeem orders in the API and web panel, retains transaction ancestors during candidate building, and adds bounded mempool/order handling intended to keep batching available during spam. It also returns the best candidate work before timeout and retries a rare indexer-lag desynchronization. The client still requires an indexed Ergo node running v6.0.4 or later.

Earlier [v5.2.0-test](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v5.2.0-test) rolled NISP commitments together, reducing reported peak transaction size from about 70 KB to 29 KB, changed bonds and slashing to `0.002 ERG`, and updated contracts, APIs, configuration, transaction construction, and fraud-proof handling. Existing testnet operators should rebuild their overrides against the current README and `application.conf` rather than reusing an older configuration unchanged.

[v4.2.0-test](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.2.0-test) changes mempool synchronization so subscribers are notified when mempool updates occur rather than receiving full mempool contents. It also moves major transaction code into dedicated transaction actors, represents future transactions as transaction stubs, and fixes rollup synchronization around chained payout-contract rollups.

Open testnet issue: [`#8`](https://github.com/Lithos-Protocol/Lithos-Client/issues/8) reports that one malformed box at the collateral contract can make `parseCollateralUTXO` throw, abort collateral retrieval, and push jobs back to solo-mining mode. The same report notes that a clean `master` build could not resolve `org.ethereum:leveldbjni-all:1.18.3`, so external contributors may be blocked until the dependency path is fixed.

[v4.1.0-test](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.1.0-test) added unified block listening, mempool support for rollups, experimental Scala-based Stratum, separate share-processing threads, and auto-collateralization configuration.

- [Telegram](https://t.me/LITHOS_Protocol)
- [GitHub](https://github.com/Lithos-Protocol)
- [Litepaper](https://github.com/Lithos-Protocol/LitePaper)

## Miner Setup and Commitments

The web panel's difficulty calculator targets 17 super shares per window. Submit an on-chain difficulty commitment through the commitment page or `POST /mining/commitment` with the client API key. Upstream advises waiting 65 blocks before starting to mine and notes that payments for blocks begin 125 blocks after the commitment; later difficulty changes can take up to 28 hours to take effect. A change to `stratum.diff` alone is not an immediate on-chain commitment change.

`stratum.bindAddress` defaults to `0.0.0.0`; set an explicit address when rigs should reach only a selected interface. The current node guide sets `offlineGeneration = true`. Inspect the client web panel and commitments state before treating a running Stratum listener as a ready, committed miner.

[Lithos Launcher](https://github.com/Lithos-Protocol/Lithos-Launcher) is a Windows/Linux desktop setup and monitoring tool for Java, the Ergo node, and the client. It handles sync/index/wallet readiness and exposes commitment setup. Its test-mining mode disables transaction-generating services while testing difficulty; normal mining still needs the upstream funding, commitment, and node-readiness steps.

## Community Monitoring

[Lithos Dashboard](https://github.com/arcadiancomp/lithos_dashboard) provides numeric and optional browser views of mining, NISP health, collateral and reward activity. Its browser listener defaults to localhost on port `8787` and has no authentication; keep it local or within a trusted network. Read-only sale quotes do not execute transactions, and projected earnings are estimates.

## Upgrading to 1.0.5

[v1.0.4](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.0.4) temporarily disabled rollup candidate sources after a UTXO-reservation bug. [v1.0.5](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.0.5) fixes that reservation path, re-enables rollups, bounds candidate builds and recovers input reservations after node refusal.

Mainnet startup rejects the shipped `lithos.apiKeyHash` for `hello`; configure a personal key hash. The client unlocks the node wallet through `node.pass` and sweeps mining rewards to the primary address every 30 minutes by default. Keep those credentials private. Browser storage of the API key is optional and off by default.

The first start migrates statistics to schema 8 and removes older schema stores. Statistics must resynchronize, limiting some statistics/API views while mining and normal submissions continue. Downgrading to 1.0.4 afterwards starts with empty statistics history; retain a backup if that history matters.

Difficulty forwards add on-chain, LIT-settled positions on average network difficulty and a webpanel Extensions section. Read/check routes are open; positions, history, collateral earnings and transactions require an API key. This release's default `stratum.diff` is `4.0M`; explicit operator settings remain in force.
