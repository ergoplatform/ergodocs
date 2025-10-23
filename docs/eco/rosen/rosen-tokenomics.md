# Tokenomics

Rosen Bridge is designed to bootstrap liquidity across multiple ecosystems. The Rosen Token serves the as a sybil resistance mechanism for the Rosen framework, a fee distribution mechanism, and means to access services of the Rosen Bridge.

[Watchers](watcher.md) are required to put collateral in RSN and ERG by staking, which allows them to acquire reporting permits. Guards need to lock RSN as collateral. Funds will be emitted to the Guard Set and involved Watchers in case of any successful bridge transfers. However, funds will be slashed/collected in case of malicious behavior. When RSN emission has ended, all bridge fees will be collected in the RSN token. Holding RSN will have special fee benefits for projects.

Any user can join as a Watcher given they meet the collateral requirements needed to participate, and earn rewards for their services.

## Overview

- **Token Name**: Rosen Bridge Token
- **Token Ticker**: RSN
- **Max Supply**: 1,000,000,000
- **Initial Liquidity Bootstrapping**: 100,000,000

## Breakdown

 Token Allocation | Number of Tokens | % of Total Supply | Distribution Method |
------------------|------------------|-------------------|---------------------|
 Initial Liquidity Bootstrapping (Ergo and Cardano) | 100,000,000 | 10% | Liquidity pool and ISPO |
 Future Liquidity Bootstrapping (New Chains) | 385,000,000 | 38.5% | Liquidity on new chains |
 Event-Based Emission (Rewards) | 250,000,000 | 25% | Event-based |
 Passive Staking | 25,000,000 | 2.5% | Staking rewards |
 Team Budget | 105,000,000 | 10.5% | 48-Months vested |
 Treasury | 105,000,000 | 10.5% | 48-Months vested |
 Ergo Foundation | 30,000,000 | 3% | 48-Months vested |

## Funding

Rosen Bridge is entirely self-funded, with no private sales, venture capital, or SAFT agreements involved, with all contracts being financed out of pocket as there is no emission yet. The core team consists of 6 main developers.

Initial liquidity for Ergo, accounting for 5%, was deposited on the Spectrum LP. There were no bots or front-running involved.

We collaborated with Zengate for Catalyst, as it involves Cardano politics, an area that falls within their realm of expertise.

We have successfully completed and received funds from milestone 3 and have submitted milestone 4 for F10 funding.

## Why is the RSN token needed?

- Capital Formation. Development has costs. Also need to form liquidity on the market.
- Creates incentives (event-based emission).

See [this answer](https://youtu.be/5p-xmILkS2c?t=1455) from Armeanio in the Weekly Update & AMA - December 14th 2023.

## Guard and Watcher Dynamics

- Guard set is predefined and curated for diversity and resilience. See [Rosen Guards](rosen-guard.md).
- Watchers are open to anyone who meets collateral requirements. See [Watcher](watcher.md).
- Guards perform independent validation and final signing; Watchers propose and reach consensus on events recorded on Ergo.

## RSN Staking and RosenEvent Tokens

- Watchers stake RSN (and ERG collateral) to obtain reporting permits.
- Staked RSN mints “RosenEvent” tokens used to create event boxes on Ergo.
- Upon successful transfer finalization, RosenEvent tokens are returned; if a Watcher reports fraudulent events, the RosenEvent is forfeited, effectively slashing the underlying RSN stake.

## Fee Distribution and Emission

- Watchers and Guards earn a share of bridge fees for successful events.
- Event-based RSN emissions additionally reward active participants during the bootstrapping phase.
- After emission ends, fees are collected in RSN; holding RSN can grant fee discounts for projects.

## Dynamic Watcher Allocation

- High-value paths naturally attract more Watchers due to fee and emission rewards.
- Incentives are tuned so less-utilized routes remain profitable, supporting balanced coverage and liveness across networks.

## Ensuring Independent Monitoring

- Watchers must act independently and are discouraged from replaying others’ reports.
- Mechanisms such as commit–reveal and honeypots penalize copycats and dishonest behavior.
- This preserves the integrity of the Watcher layer and the fairness of fee/emission distribution.

For background on roles and assumptions, review:
- [Concepts & Assumptions](concepts-assumptions.md)
- [Watcher](watcher.md)
- [Rosen Guards](rosen-guard.md)
