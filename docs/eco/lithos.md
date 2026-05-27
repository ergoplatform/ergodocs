---
tags:
  - Lithos
  - Mining Pool
  - Decentralized
  - Infrastructure
  - dApp
  - dApp-InDev
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: Lithos-Protocol/Lithos-Client
    branch: master
    paths:
      - README.md
      - TestnetNode.md
source_of_truth:
  - https://github.com/Lithos-Protocol/Lithos-Client
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.2.0-test
  - https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.1.0-test
---

# Lithos

## Overview

Lithos is a project that aims to create a decentralized mining pool infrastructure by providing a low-risk opportunity for lenders to earn yield on their ERG by providing collateral to mining pools while promoting increasingly decentralized block production. This means that the project plans to enable miners to directly insert necessary transactions into blocks in a fully decentralized and trustless manner, bringing significant benefits to miners outside of just decentralization.

Traditionally, attempts to create decentralized mining pools have faced challenges such as security concerns, lack of miner usage, and failures to achieve both efficiency and full decentralization. However, Lithos proposes a new solution to these challenges by using a new protocol that verifies miners' work and pays them out accordingly while utilizing Stratum as the "networking layer" for the protocol. The protocol is blockchain-agnostic, meaning that Lithos may support mining pools for any Proof of Work (PoW) blockchain.
Recently, Lithos has completed collateral contracts, and the ability of miners to directly insert necessary transactions into blocks has been successfully demonstrated during the ERGOHACK VI event. Overall, the goal of Lithos is to usher in a new era for PoW mining, where mining pools are fully decentralized, efficient, and trustless.

## Current Testnet Client

The [Lithos Client](https://github.com/Lithos-Protocol/Lithos-Client) is the reference client for the Lithos Protocol. Recent testnet releases focus on synchronization, mempool tracking, transaction scheduling, rollup evaluation, and Stratum behavior.

[v4.2.0-test](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.2.0-test) changes mempool synchronization so subscribers are notified when mempool updates occur rather than receiving full mempool contents. It also moves major transaction code into dedicated transaction actors, represents future transactions as transaction stubs, and fixes rollup synchronization around chained payout-contract rollups.

[v4.1.0-test](https://github.com/Lithos-Protocol/Lithos-Client/releases/tag/v4.1.0-test) added unified block listening, mempool support for rollups, experimental Scala-based Stratum, separate share-processing threads, and auto-collateralization configuration.

- [Telegram](https://t.me/LITHOS_Protocol)
- [GitHub](https://github.com/Lithos-Protocol)
- [Litepaper](https://github.com/Lithos-Protocol/LitePaper)
