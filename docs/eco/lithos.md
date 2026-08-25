---
tags:
  - Lithos
  - Mining Pool
  - Decentralized
  - Infrastructure
  - dApp
  - dApp-InDev
owner: docs
last_reviewed: 2026-08-25
source_repos:
  - repo: Lithos-Protocol/Lithos-Client
    branch: master
    release_watch: true
    paths:
      - README.md
      - TestnetNode.md
source_of_truth:
  - https://github.com/Lithos-Protocol/Lithos-Client
  - https://github.com/Lithos-Protocol/LitePaper
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

## Current Testnet Client

The [Lithos Client](https://github.com/Lithos-Protocol/Lithos-Client) is the reference client for the Lithos Protocol. Recent testnet releases focus on synchronization, mempool tracking, transaction scheduling, rollup evaluation, and Stratum behavior.

The current README describes Lithos as requiring a fully synced Ergo node and Java 11. Miners connect through the Lithos Stratum server, with Rigel Miner recommended. Lithos evaluates Non-Interactive Share Proofs rather than ordinary pool shares, so the miner address and worker name used by the Stratum client are not payout identifiers in the same way they are for a conventional pool.

August 2025 dev updates said the difficulty contract and off-chain work for multiple fraud-proof contracts were finished, Stratum was being adjusted for TRM users and lower resource use, and shares were persisted across Stratum shutdowns. The same update framed this as testnet preparation rather than a production release.

Earlier SNISP/NISP research is now treated as Lithos background rather than a separate ecosystem project. See [SNISP](snisp.md) for the legacy concept page.

The first public testnet releases arrived in November 2025. [`v1.0-test`](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.0-test) introduced the testnet client package, and [`v1.1-test`](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v1.1-test) followed with stability fixes, Stratum error-handling changes, setup simplification, refactoring, and logging changes.

For testnet use, the client needs node API access and a testnet wallet keystore so it can sign and generate transactions. The upstream testnet guide warns users to create a new testnet-only secret key rather than reusing a mainnet wallet.

[v5.0.0-test](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v5.0.0-test) is the current testnet client. It requires an indexed Ergo node running v6.0.4 or later and introduces substantial configuration changes. The release adds the new emissions and collateral flow, stronger wallet UTXO tracking and reservations, MinerDictionary synchronization fixes, LithosDex APIs and local web UI, block-package and fraud-proof-stub transaction support, candidate-builder options, and Stratum concurrency improvements. Existing testnet operators should rebuild their overrides against the current README and `application.conf` rather than reusing an older configuration unchanged.

[v4.2.0-test](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.2.0-test) changes mempool synchronization so subscribers are notified when mempool updates occur rather than receiving full mempool contents. It also moves major transaction code into dedicated transaction actors, represents future transactions as transaction stubs, and fixes rollup synchronization around chained payout-contract rollups.

Open testnet issue: [`#8`](https://github.com/Lithos-Protocol/Lithos-Client/issues/8) reports that one malformed box at the collateral contract can make `parseCollateralUTXO` throw, abort collateral retrieval, and push jobs back to solo-mining mode. The same report notes that a clean `master` build could not resolve `org.ethereum:leveldbjni-all:1.18.3`, so external contributors may be blocked until the dependency path is fixed.

[v4.1.0-test](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.1.0-test) added unified block listening, mempool support for rollups, experimental Scala-based Stratum, separate share-processing threads, and auto-collateralization configuration.

- [Telegram](https://t.me/LITHOS_Protocol)
- [GitHub](https://github.com/Lithos-Protocol)
- [Litepaper](https://github.com/Lithos-Protocol/LitePaper)
