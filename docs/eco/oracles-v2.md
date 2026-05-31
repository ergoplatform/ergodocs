---
tags:
  - Oracle Pools
  - Oracles
  - EIP-23
  - DeFi
owner: docs
last_reviewed: 2026-05-26
source_repos:
  - repo: ergoplatform/eips
    branch: eip16
    paths:
      - eip-0016.md
  - repo: ergoplatform/oracle-core
    branch: develop
    paths:
      - docs/how_to_bootstrap.md
source_of_truth:
  - https://error1100.github.io/oracle-stats/
  - https://multi-oracle-dashboard.vercel.app/
  - https://github.com/ergoplatform/eips/tree/eip16/eip-0016.md
  - https://github.com/ergoplatform/oracle-core/tree/develop/docs/how_to_bootstrap.md
---

# Oracle Pools Version 2

## Overview

Oracle Pools provide on-chain data feeds for Ergo applications. Version 2 reduces the box complexity and dust issues found in the original Oracle Pool design while keeping the pool box usable as a data input for dApps.

The core implementation is [Oracle Core](https://github.com/ergoplatform/oracle-core), written in Rust.

## Project Status

Oracle Core is maintained as the source implementation for running and bootstrapping Oracle Pool v2 infrastructure. The source repository includes operator documentation, release notes, and a testnet bootstrap guide.

For operators, start with [Bootstrap an Oracle Pool](oracle-bootstrap.md). For a technical specification, read [EIP-0023 Oracle Pool 2.0](https://github.com/ergoplatform/eips/pull/41).

## Why Version 2

The document described below outlines a proposed upgrade to Oracle Pool version 1.0, as presently deployed and detailed in [EIP16](https://github.com/ergoplatform/eips/blob/eip16/eip-0016.md). The necessity for these modifications emerges from several perceived limitations within Oracle Pool v1.0:

1. Excessive dust generation from rewards.
2. Inadequate reward provision (interrelated with point 1).
3. Two distinct types of pool boxes, complicating dApps and the update mechanism.
4. Non-transferability of Oracle tokens, resulting in the permanent locking of oracles. This issue also applies to ballot tokens.

Version 2.0 aims to mitigate these issues.

## Core Design Changes

- **Single Pool Address**: In v2.0, the pool will have only a singular address, known as the *pool address*.
- **Epoch Counter**: To accommodate more complex dApps, the pool box will store an additional counter that increments upon each collection.
- **Compact Pool Box**: The pool box is dissociated from pool management logic, which is now encapsulated within a **refresh** box. This results in a considerably smaller pool box, conducive for use in other dApps.
- **Refresh Box**: This box functions for the collection of data-points.

## Rewards And Tokens

- **Reward in Tokens**: Instead of Ergs, rewards for posting will be issued in tokens. These tokens can be redeemed separately, outside of the protocol.
  - The pool box will emit these reward tokens.
- **No Separate Funding Process**: The pool box will only emit reward tokens and will not distribute Ergs. Consequently, a separate funding process is not required.
- **Reward Accumulation**: To avoid dust, a new box for each reward posting will not be created. Instead, rewards will be directly accumulated within the oracle boxes.
- **Oracle Boxes Used in Collection**: As rewards must be accumulated, the oracle boxes will function as inputs instead of data-inputs when collating individual rates for averaging.
  - These inputs will be spent, creating a copy of the box with the reward.
  - This system enables reward accumulation while maintaining a transaction size akin to the usage of them as data-inputs in v1.0.
  - Additionally, it allows us to delegate part of the reward logic to the oracle boxes.
  - **Note:** The pool box will continue to serve as a data input in other dApps.
- **Transferable Oracle Tokens**: Oracle tokens can be freely transferred among public keys.
- **Updated Mechanism**: The update mechanism in v2.0 will remain similar to v1.0, requiring a threshold number of ballot token holders to vote for an update.
- **Transferable Ballot Tokens**: Analogous to oracle tokens, ballot tokens can be freely transferred between public keys.

## Operator Resources

- [Oracle Core](https://github.com/ergoplatform/oracle-core): source implementation.
- [Bootstrap an ERG/XAU pool on testnet](https://github.com/ergoplatform/oracle-core/blob/develop/docs/how_to_bootstrap.md): upstream operator guide.
- [Bootstrap an Oracle Pool](oracle-bootstrap.md): ErgoDocs operator guide.
- [Oracle Stats](https://error1100.github.io/oracle-stats/): status page for v2 oracle pools.
- [oracle-stats repository](https://github.com/error1100/oracle-stats): self-hostable monitoring tool.

## Integration And Monitoring

Oracle Stats was described as a lightweight status page for v2 oracle pools. Its main purpose is visualising oracle activity per epoch, simple health status, and transaction monitoring. Active datapoints link to on-chain transactions, while inactive oracles are shown separately.

The [AVL Oracle Pool](http://github.com/cannonQ/AVL-Multi-Oracle-Ergo-Pool) puts multiple feeds in one on-chain AVL tree. The related [AVL Oracle SDK](https://github.com/cannonQ/avl-oracle-sdk) and [multi-oracle dashboard](https://multi-oracle-dashboard.vercel.app/) support integrations and monitoring.

## Recent updates

- `Jan 9`: [Oracle Core v2.0.5](https://github.com/ergoplatform/oracle-core/releases/tag/v2.0.5) shipped with a Coingecko user-agent fix.
- `Jan 10`: [Oracle Core v2.0.6](https://github.com/ergoplatform/oracle-core/releases/tag/v2.0.6) followed with datapoint robustness work and an overlapping datapoint-submit fix.
- `Jan 9` onward: [robustness work](https://github.com/ergoplatform/oracle-core/pull/343) added Coinpaprika and Bitpanda sources and removed CoinCap.
- `Feb-Apr`: [Oracle Stats](https://error1100.github.io/oracle-stats/) went live, with a self-hostable [oracle-stats repository](https://github.com/error1100/oracle-stats).
- `Apr 1`: the [AVL Oracle Pool](http://github.com/cannonQ/AVL-Multi-Oracle-Ergo-Pool) went public on Ergo mainnet after 1,300+ testing epochs, with 20 feeds in one on-chain AVL tree. The related [AVL Oracle SDK](https://github.com/cannonQ/avl-oracle-sdk) and [multi-oracle dashboard](https://multi-oracle-dashboard.vercel.app/) support integrations and monitoring.

The January robustness work was triggered by CoinCap API removal and CoinGecko requiring a user-agent header. Oracle operators should prefer the current Oracle Core release and configured data-source mix rather than relying on a single external price API.

## Background Video

For historical context, see [Oracle Pool v2 | greenhat | Ergoversary Summit 2023](https://youtube.com/watch?v=WeQcUmVUhoI). This is background material, not the latest development source.
