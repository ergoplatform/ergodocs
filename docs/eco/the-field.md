---
tags:
  - The Field
  - Pledging
  - DAO
  - dApp
owner: docs
last_reviewed: '2026-07-02'
source_of_truth:
- https://discord.gg/wa38bX57tY
source_watch_note: Project updates currently come from maintainer Discord posts; no verified public GitHub repository found.
ia_status: directory
---

# The Field

"The Field" is a parimutuel prediction-market protocol on Ergo. Pledgers stake `$USE` on one of four outcomes; winners split the pool and losing pledgers receive non-transferable rebate credits. The design avoids a house edge and does not use an AMM.

## Current Status

The project is moving toward launch but is not yet documented as production-ready. A July 2026 maintainer update said:

- trustless settlement uses AVL oracles for live price data across crypto, commodities, and indices;
- the maintainer has run an Ergo Knowledge Base audit pass over the v2 contracts, including pledging, market resolution, and rebate logic;
- one blocking bug remains in the rebate minting flow, with a few smaller issues also being fixed;
- contracts are intended to be AGPL-3.0 and fully open source once launch timing is locked.

The public oracle dashboard referenced by the maintainer is [multi-oracle-dashboard.vercel.app](http://multi-oracle-dashboard.vercel.app).

- Join the project's Discord server at <https://discord.gg/wa38bX57tY> to learn more and/or volunteer to help move the project and DAO forward.
