---
tags:
  - USE
  - Stablecoin
  - Dexy
---
# USE (USD stablecoin)

Centralized USD-pegged stablecoins anchor most on-chain liquidity and activity. Their design brings censorship and regulatory risk. Refusing to interoperate isolates Ergo in a niche and reduces utility for regular users. This page lays out the case for a cost-efficient USD stablecoin for the Ergo ecosystem (USE), the core design, initial parameters and a practical roadmap for launch and operations.

**Related docs:** [Use cases overview](use-cases-overview.md), [Dexy](dexy.md)

---

## Summary

- **Objective:** deliver a cost-efficient, highly liquid USD-pegged asset (USE) that maximizes on-chain utility while preserving protocol security.

- **Positioning:** a pragmatic asset that interoperates with broader crypto liquidity (USDT and peers) while keeping protocol-level safety strong and avoiding censorship-prone primitives at the platform layer.

- **Guiding principle:** prioritize cost efficiency (low fees, scalable flows) without compromising security of protocol contracts.

---

## Why USE on Ergo?

- **Liquidity and onboarding:** USD stablecoins function as primary on-ramps and liquidity anchors. Support for them raises accessibility for users and traders.

- **Ecosystem growth:** Interoperability with the most liquid assets supports DEX volume, developer traction, and integrations.

- **Complementary design:** A well-specified USE and its tooling can showcase Ergo’s advantages (privacy features, formal contracts) without forcing users to abandon familiar liquidity.

---

## Design Choices and Recommendations

- **Reserve model (1:1):** adopt a conservative, transparent reserve approach that follows Dexy-style operational assumptions to reduce systemic risk.

- **Cost efficiency:** select mechanisms that minimize fees and friction across composable flows. Dexy’s low-fee properties and Rosen Bridge integration can drive competitive costs.

  - **Recommended fee targets:**

    - **Rosen and cross-chain bridges:** enable custom fees as low as ~0.1% to remain competitive.
    - **Dedicated v3 AMM instance (e.g., BSC):** target 0.05% fees with a tighter price band (0.9–1.1) for stable-stable liquidity.

- **UI fees and fee caps:** adopt a front-end fee that lifts after the protocol-wide collected fees for USE pass a configured threshold. The UI operator (example: C8) should set and enforce this policy for USE only.

- **Decimal precision:** match major liquidity partners. Use **6 decimals** as a minimum. This choice provides fine granularity (0.999999) and aligns with many stablecoins and exchanges. Avoid low-precision choices (for example, 2 decimals) that weaken tight stable-stable markets.

- **Supply considerations:**
  - Supply size does not control peg mechanics. Choose a nominal supply that avoids awkward decimals and matches UX expectations.
  - Community discussions explored ranges from 50 m to very large nominal supplies. Very large nominal supplies (for example, 100 T) require **6 decimals** to keep UX precise.

- **Token identifiers and governance tokens:** prepare and publish canonical token IDs (pool NFT, refresh/update NFTs, oracle, reward, ballot) in initial docs and deployment manifests so trackers and UIs can follow them. Include example formats in release notes.

- **Oracles:** select reliable price oracles and document decimal handling so USDT/USDC pairings behave as expected. Ensure oracle data follows the token’s decimal conventions.

---

## Bank Contract: Stability and Security (Starting Properties)

We aim for a stable peg and robust security under realistic adversarial conditions.

- **Reserves:** 1:1 reserves in segregated, auditable addresses or multisig, with governance-controlled vaults.

- **Oracle design:** multi-source inputs with signatures, aggregation, outlier rejection, and a pause control for anomalous readings.

- **Peg controls:** conservative, auditable adjustments only; no privileged auto-minting.

- **Governance and upgradeability:** minimal, explicit upgrade paths; emergency pause under multisig with time-locks to prevent unilateral actions.

- **Limits and caps:** early per-block and per-wallet mint/redemption limits that reduce exposure to procedural or market errors.

- **Transparency:** public reserve attestations and documented accounting procedures, with on-chain proofs where feasible.

---

## Initial Parameter Suggestions (For Review)

- **Decimals:** 6.

- **Initial nominal supply:** choose a number that avoids awkward UX. Community leaning: **250,000,000**. A larger nominal supply also works when paired with 6 decimals.

- **Fee structure:**
  
  - Protocol/bridge configurable fee floor at **0.1%**, with operator flexibility for competitive rates.
  - Target **0.05%** for dedicated stable-stable AMM pools.
  - UI fee waiver after a defined cumulative-fees threshold for USE (threshold set by the UI operator).

- **Oracle cadence:** conservative configuration with minute-level updates plus aggregation and outlier rejection.

- **Mint/redemption onboarding:** start with off-chain KYC/AML for minting partners if counterparties require it. Publish clear KYC policies.

---

## Operational Notes and Trackers

- **Pre-launch tokens:** no tokens exist until mint. Indexers and off-chain bots should prepare to track and register token IDs once minted. Trackers should ingest token metadata when available.

- **Publication:** publish all token IDs and NFT IDs for pools, refresh, update, oracle, reward, and ballot before or at launch so UIs and indexers can enable support.

---

## Roadmap (Proposal)

- [ ] Finalize high-level design and governance model (multisig, time-locks, upgrade policy).

- [ ] Decide decimals and nominal supply (community vote or dev consensus).

- [ ] Implement bank contract and complete a security review and audit.

- [ ] Implement oracle adapters and aggregator logic; test on testnet.

- [ ] Prepare Rosen Bridge integration and expose custom fee options.

- [ ] Deploy initial tokens on testnet; publish token IDs.

- [ ] Prepare UI integrations, indexers, and off-chain bot updates.

- [ ] Launch mainnet mint with coordinated liquidity onboarding (DEX pools, AMM instances).

- [ ] Continue audits, reserve transparency, and fee tuning based on activity.

---

## Suggested Role Assignments (Initial)

- **Protocol and bridge integration:** Rosen maintainers coordinate custom lower-end fee settings.

- **AMM and liquidity engineering:** Dexy and AMM operators define tight stable-stable pools; consider a v3 instance on BSC for cross-chain liquidity tests.

- **UI fee policy and front-end:** C8 defines the threshold and implements fee-lifting for USE.

- **Token spec and decimals:** Kushti documents implementation details and minting parameters.

- **Audit and security:** independent auditors and core dev reviewers oversee scope and fixes.

- **Community coordination:** one or two community managers publish token IDs and coordinate with exchanges and trackers.

---

## Open Questions Before Launch

- Exact nominal total supply and decimal decision  
  **Proposed:** 6 decimals, nominal supply at 250 m or a different nominal with 6 decimals.

- Final governance signers and time-lock parameters.

- Audit scope and dates.

- Oracle providers and aggregator logic.

---

## Notes From Community Discussions

- Broad support exists for **6 decimals** to match USDT and support tight pricing.

- Dexy’s transparent 1:1 reserve approach and cost focus fit the target UX for USE.

- Very low fees attract flow; security and reserve integrity remain the higher priority.

- A UI fee-waiver after a collected-fees threshold can strengthen UX for USE.

---

## Next Steps

1. Confirm the decimals and nominal supply choice and record the decision.

2. Start the bank contract specification and nominate multisig signers.

3. Produce a detailed technical spec for the bank contract and AMM parameters for audit.

4. Assign owners for roadmap items and set timelines.

---
