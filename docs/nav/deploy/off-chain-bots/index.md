---
tags:
  - deploy
  - off-chain-bots
  - navigation
owner: docs
last_reviewed: 2026-06-08
---

# Off-Chain Bots

Off-Chain Bots groups operator-facing bot and automation pages. Use this branch when you need to run services that watch Ergo, construct transactions, or execute dApp-specific workflows without becoming part of the consensus layer.

For developer architecture and implementation patterns, see [Off-Chain Services](off-chain-overview.md).

## Where to start

| Goal | Start here |
| --- | --- |
| Run Spectrum/ErgoDEX executors | [Off-Chain Bot Overview](dex_bots.md) |
| Run a grid-order matcher | [Off-the-Grid Bot](off_the_grid_tut.md) |
| Understand the grid trading model | [Grid Trading](grid_trading.md) |
| Design your own service | [Off-Chain Services](off-chain-overview.md) |

## Operator model

Most Ergo bots follow the same pattern:

1. Watch chain and mempool data from an Ergo node or indexer.
2. Detect boxes that match the dApp's contracts.
3. Build a valid transaction for the next state transition.
4. Sign with an operator wallet only when the bot needs fees, rewards, or funding inputs.
5. Submit the transaction and handle conflicts, reorgs, retries, and stale orders.

The contracts still validate the state transition on-chain. A bot can propose an invalid transaction, but the node will reject it.

## Common requirements

| Requirement | Notes |
| --- | --- |
| Ergo node | Prefer your own synced node. Public nodes add latency and can reduce execution success. |
| Node API | Bots usually need `http://host:9053`; wallet-backed bots also need the API key. |
| Wallet or seed | Use a dedicated operator wallet, not a normal hot wallet. Keep only required funds online. |
| Runtime stack | Spectrum/ErgoDEX uses Docker Compose services; Off-the-Grid builds a Rust CLI with Nix or Cargo. |
| Local state | Bots keep scan IDs, caches, RocksDB data, or service volumes. Back these up before host changes. |
| Monitoring | Watch logs, submitted transaction IDs, node sync height, wallet balance, and stuck retries. |

## Bot families

| Family | What it does | Main source |
| --- | --- | --- |
| Spectrum/ErgoDEX executors | Track AMM/order boxes, resolve pools, execute DEX orders, expose market data. | [spectrum-finance/ergo-dex-backend](https://github.com/spectrum-finance/ergo-dex-backend) |
| Spectrum off-chain streams | Rust workspace for chain sync, mempool sync, backlog handling, order execution, and liquidity-mining streams. | [spectrum-finance/spectrum-offchain-ergo](https://github.com/spectrum-finance/spectrum-offchain-ergo) |
| Off-the-Grid matcher | Match grid orders against Spectrum AMM liquidity and collect operator rewards. | [Telefragged/off-the-grid](https://github.com/Telefragged/off-the-grid) |
| Machina Finance | DEX/grid-order project exploring order execution and extensible bot infrastructure. | [Machina Finance](machina-finance.md), [machinafi/sdk](https://github.com/machinafi/sdk) |

## Safety checklist

- Run from a dedicated wallet seed or reward address where the project supports it.
- Keep node API access private; do not expose wallet endpoints publicly.
- Start with small funds and confirm the bot can submit and confirm transactions.
- Check upstream `config-example.env`, sample JSON config, or YAML config after every update.
- Expect failed submissions when other bots spend the same input first.
- Confirm whether the project is maintained before using large balances.

## Map

| Page | What you'll find |
| --- | --- |
| [Off-Chain Bot Overview](dex_bots.md) | Spectrum/ErgoDex off-chain service stack and bot runtime notes. |
| [Off-the-Grid Bot](off_the_grid_tut.md) | Setup and operation guide for the Off-the-Grid trading bot. |
| [Off-the-Grid Concept](off_the_grid.md) | Grid-order dApp overview and bot/batcher role. |
| [Grid Trading](grid_trading.md) | Grid trading use-case overview and related implementations. |
| [Machina Finance](machina-finance.md) | Ecosystem profile and SDK links for the Machina DEX/grid-order project. |
