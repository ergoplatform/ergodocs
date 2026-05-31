---
title: Braid
description: Research notes for Braid, a proposed Bitcoin and Ergo double merged-mined
  sidechain.
tags:
  - Sidechains
  - Braid
  - Bitcoin
  - Ergo
  - Merged Mining
  - Stablecoins
  - RWA
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: BetterMoneyLabs/braid
    branch: master
    paths:
      - README.md
      - docs/ergo-mergedmining.md
      - docs/bitcoin-mergedmining.md
      - docs/braid.md
      - whitepaper/whitepaper.tex
      - whitepaper/whitepaper.pdf
source_of_truth:
  - https://github.com/BetterMoneyLabs/braid
  - https://github.com/BetterMoneyLabs/braid/blob/master/README.md
  - https://github.com/BetterMoneyLabs/braid/blob/master/whitepaper/whitepaper.pdf
  - https://github.com/BetterMoneyLabs/braid/blob/master/whitepaper/whitepaper.tex
  - https://github.com/BetterMoneyLabs/braid/blob/master/docs/ergo-mergedmining.md
  - https://github.com/BetterMoneyLabs/braid/blob/master/docs/bitcoin-mergedmining.md
ia_status: directory
---

# Braid

[Braid](https://github.com/BetterMoneyLabs/braid) is a proposed double merged-mined sidechain of Bitcoin and Ergo. Its whitepaper frames the chain around stablecoins, real-world assets, Bitcoin DeFi, and programmable money with low trust assumptions.

Treat Braid as research and prototype material, not as a deployed Ergo sidechain. The public repository contains the whitepaper, early merged-mining notes, and minimal implementation scaffolding; it has no published releases.

## Design Goals

Braid aims to combine Bitcoin's proof-of-work security, Ergo's contractual model, and fast transaction-carrying blocks.

The whitepaper targets:

- Bitcoin and Ergo double merged mining.
- Fast proof-of-work-secured blocks, using Ergo input-block ideas for low-latency transaction inclusion.
- Stablecoin and real-world-asset issuance with precise transfer rules.
- Trust-minimized Bitcoin DeFi through Bitcoin collateral and Bitcoin-chain metadata.
- Ergo-style UTXO programmability, including Sigma protocols and contract-first token logic.
- Liquidity routes with Bitcoin, Ethereum, BNB Chain, Cardano, and a two-way Ergo peg as design goals.

## Consensus Sketch

Braid separates consensus into two block roles:

- **Bitcoin-merged ordering blocks**: committed through Bitcoin merged-mining data. They witness the best input-block chain seen by a miner and commit to state such as the UTXO-set digest and interlink vector.
- **Ergo-merged input blocks**: committed through Ergo input blocks, allowing transaction-carrying Braid blocks every few seconds in the proposal.

This design tries to get slow, high-security Bitcoin ordering plus fast Ergo-style input blocks. The result is not the same as a normal Ergo sidechain: Braid explicitly depends on both Bitcoin and Ergo for merged-mined commitments.

## Programmable Money Model

Braid follows Ergo's UTXO and contract-first approach:

- Boxes carry typed registers and token data.
- Contracts define spending rules directly.
- Applications can use data from both Bitcoin and Ergo as contract context.
- Existing Ergo applications could, in principle, be ported because the model stays close to ErgoScript and UTXO semantics.

The whitepaper also proposes **Global Transfer Policies**: token-level policy contracts that can require whitelist/blacklist checks, application-specific rules, mandatory payments, jurisdiction-specific transfer logic, or policy propagation across outputs.

## Privacy And Compliance Circuits

Braid's design tries to support both transparent and private monetary circuits:

- **Dark tokens** would hide amounts with homomorphic commitments and validity proofs.
- Transfer policies could require stealth-address-like receiver handling or other privacy constraints.
- Issuers could keep one circuit transparent and bridge into a darker circuit under defined policy rules.

This is still design-level material. Do not treat these features as live wallet or node functionality.

## Stablecoins And RWAs

The whitepaper explicitly connects Braid to Ergo stablecoin work:

- SigmaUSD / Djed-style collateralized stablecoins.
- Gluon-style assets such as GluonGold.
- Dexy-style assets such as DexyGold.
- ChainCash-style peer-to-peer credit and stablecoin designs.
- Insurance-style contracts for tokenized physical asset delivery risk.

Braid's core motivation is to give issuers programmable circuits with policy granularity, while still retaining proof-of-work security and interoperability with Bitcoin and Ergo.

## Ergo Merged-Mining Notes

The repository's Ergo merged-mining note sketches how sidechain progress can be stored on Ergo. It models sidechain progress as a tuple containing height, state changes, a UTXO-set AVL+ digest, and a commitment chain over previous sidechain states.

The note proposes:

- Identifying the sidechain data box with an NFT.
- Storing a hash of sidechain data in register `R4`.
- Storing the previous sidechain data box id in register `R5`.
- Updating sidechain data through miner-authorized refresh transactions.
- Using Merkle proofs and sigma-rust support to verify sidechain data refreshes.

## Status

Braid is early research:

- Public repository: [BetterMoneyLabs/braid](https://github.com/BetterMoneyLabs/braid)
- Whitepaper: [whitepaper.pdf](https://github.com/BetterMoneyLabs/braid/blob/master/whitepaper/whitepaper.pdf)
- Source whitepaper: [whitepaper.tex](https://github.com/BetterMoneyLabs/braid/blob/master/whitepaper/whitepaper.tex)
- Ergo merged-mining note: [docs/ergo-mergedmining.md](https://github.com/BetterMoneyLabs/braid/blob/master/docs/ergo-mergedmining.md)
- No public release is published in the repository.

For current Ergo sidechain context, also see [Sidechains on Ergo](sidechains.md), [Sigma Chains](sigma-chains.md), and [Weak Blocks](weak-blocks.md).
