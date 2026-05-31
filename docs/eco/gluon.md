---
tags:
  - Gluon
  - Stablecoin
  - Djed
  - SigmaGold
  - SigGold
  - Oracles
  - dApp
  - dApp-Live
owner: docs
last_reviewed: 2026-05-30
source_repos:
  - repo: StabilityNexus/Gluon-Ergo-UI
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://gluon.gold/
  - https://github.com/StabilityNexus/Gluon-Ergo-UI
---

# Gluon

## Introduction

During the [Ergoversary Summit 2023](https://www.youtube.com/watch?v=tnvm1we6xts&list=PL8-KVrs6vXLRxmOmprVdXkHDcO4IaQZOY&index=23&t=803s), Bruno Woltzenlogel Paleo presented a new stablecoin protocol called Gluon W±. The protocol aims to address the limitations and issues found in existing stablecoin protocols like Djed and SigmaUSD. Bruno, along with Alexander Chapournoy, Kii, and Sangeet, has been working on developing Gluon W± with the support of the Djed Alliance.

/// details | Now Live!
    {type: info, open: true}
Now live at [gluon.gold](https://gluon.gold/)
///

For nearby monetary-system pages, see [Stablecoins](stablecoins.md), [SigmaUSD](sigmausd.md), and [Dexy](dexy.md).

## Performance and Issues

Gluon W± has demonstrated strong performance on Ergo, surviving market crashes since early 2021 while many other stablecoins have failed. However, Bruno acknowledges that there is always room for improvement. He highlights some of the concerns with the current protocol, such as sensitivity to the oracle and reserve drainage by whales, inconvenience for reserve coin holders unable to sell back reserve coins below the threshold, and the zero equity problem. These issues have been addressed in talks and proposals for a future extended Djed protocol.

## Concept and Functionality

Bruno had a breakthrough moment while contemplating liquidity pools and their relationship with Djed. This led to the idea of creating a new stablecoin protocol that functions as the dual of a liquidity pool. Gluon W± does not operate as a liquidity pool for the ERG and SigmaUSD pair but rather focuses on the pair of Stablecoin ReserveCoin (SigRSV and SigUSD).

## Actions and Reactions

The protocol introduces several actions or reactions, including fission, fusion, beta decay plus, and beta decay minus. Fission allows for the splitting of Ergs into stablecoins and reservecoins, while fusion combines the neutrons and protons (stablecoins and reservecoins) to regenerate Ergs. Beta decay plus and minus resemble swaps in liquidity pools, enabling the conversion of protons to neutrons and vice versa.

## Price Determination

To determine the amounts obtained from fission and fusion, reaction equations and price equations are utilized. The price equations, although auxiliary in this protocol, help calculate the prices of neutrons and protons based on the Q function, which considers the oracle price. The Q ratio and beta decay fee formulas are vital components of the Gluon W± protocol.

## User Interface and Operations

The protocol allows for buying and selling stablecoins and reservecoins through compositions of primitive reactions. Bruno explains how these derived operations can be achieved by combining fission and beta decay. The user interfaces can simplify these processes for users, enabling them to focus on their desired transactions.

The current [Gluon Ergo UI](https://github.com/StabilityNexus/Gluon-Ergo-UI) is the source repository for the Gluon Gold implementation on Ergo. It is a Next.js frontend with Gluon Gold SDK integration, wallet/protocol components, automatic testnet/mainnet configuration, and live protocol data such as price feeds, reserve ratios, and volume metrics.

The repository README describes the application stack as Next.js, Tailwind CSS, Shadcn UI, Zustand, Framer Motion, and Bun. The source tree separates wallet/protocol components, layout components, reactor swap logic, constants, providers, and utility functions. The documented test suite covers ERG conversion and formatting, error handling, node-service logic, transaction monitoring, token validation, and reactor swap actions.

## Duality Concept

Bruno introduces the concept of duality in relation to liquidity pools. While liquidity pools involve two assets remaining in the pool, Gluon W± operates with one asset (base coin) remaining in the reserve while the newly generated assets (stablecoins and reservecoins) exist outside the reserve. The protocol's design reflects this duality and mirrors the operations found in liquidity pools.

## Implementation and Future Plans

Although a beta testnet for Gluon W± was not completed in time for the Ergoversary Summit, implementation on Ergo is underway. The contract is being developed by Kii for the backend, while Sangeet works on the frontend. The protocol will utilize the new Gold Oracle, similar to DexyGold. Depending on the success of SigmaGold, Gluon W± might replace minimal Djed in SigmaUSD or be used to deploy a new USD stablecoin.

## Get Involved

Bruno invites interested individuals to join the [Djed Alliance Discord server](https://discord.gg/6FY8qJesjn), follow them on [Twitter](https://twitter.com/DjedAlliance), and explore their [GitHub](https://github.com/DjedAlliance) repositories to stay updated on the development of Gluon W± and related projects.
