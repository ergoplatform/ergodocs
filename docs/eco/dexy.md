---
tags:
  - Dexy
  - Seigniorage
  - Stablecoin
  - dApp
  - dApp-InDev
---

# Dexy: A Seigniorage-Based Stablecoin

Dexy is an innovative stablecoin design that leverages seigniorage and oracle price feeds to maintain a peg. It is currently under development.

Read the [draft whitepaper](../assets/pdf/dexy.pdf) for more details.

## DexyGold

The first implementation of Dexy will be **DexyGold**, which aims to maintain a peg to the USD/XAU (gold) price using a [XAU / ERG](https://explorer.ergoplatform.com/en/oracle-pool-state/xauerg) v2 [oracle pool](oracles.md).

/// details | Beta
    {type: info, open: true}
- [LP UI](https://dexy.interface-ggd.pages.dev/ergo/swap?base=0000000000000000000000000000000000000000000000000000000000000000&quote=0d69a552b30df9be519099ec07682039b0610267aaee48d2a1d3dad398287ef5&initialPoolId=0fa04f3851b18085f160d90bc3dba1c63f2fdc73f884c9fd94395dbfc9c293b6)
- [Bank UI](https://dexy-test.dexygold.com/)
- [Testnet Nautilus (required):](https://github.com/nautls/nautilus-wallet/releases/tag/v0.9.2)
- Testnet ERG is available via [the faucet](https://testnet.ergofaucet.org/)
///

## Design Overview

The Dexy design incorporates the following key components and mechanisms:

1. **Emission (Minting) Contract**: 
    - Allows one-way minting of new Dexy tokens by selling ERG at the oracle pool rate.
    - Reverse swaps (selling Dexy for ERG) are not possible through this contract.

2. **Liquidity Pool (LP)**:
    - Facilitates buying and selling of Dexy tokens using ERG.
    - Utilizes Uniswap V2 logic with modifications based on the oracle pool rate.
    - Prevents LP token redemptions when the oracle rate is significantly below (e.g., 90%) the LP rate.

3. **Arbitrage Mechanism**:
    - When the oracle rate is higher than the LP rate, arbitrageurs can mint Dexy from the emission contract and sell to the LP for a profit.
    - This helps push the Dexy price towards the peg.

4. **Top-up Swaps**:
    - When the oracle rate is lower than the LP rate, ERG from the emission contract can be used to buy Dexy from the LP, pushing the price back up.
    - Controlled by a swapping contract that monitors the oracle and LP rates.
    - Uses a "cross-tracker" in the LP to record when the oracle rate falls below the LP rate.
    - Swaps are only allowed if the oracle rate remains below the LP rate for a minimum number of blocks (e.g., 50).

5. **Anti-Draining Measures**:
    - To prevent cyclic draining of the emission contract through alternating arbitrage and top-up swaps, one or more of the following can be implemented:
      - Locking minted Dexy tokens for a certain period.
      - Locking ERG in the emission contract for a certain period.
      - Disabling minting when it is profitable based on the current rates.

## Potential Vulnerabilities and Considerations

- **Draining Attack**: Alternating between profitable minting/selling and topping up the LP could potentially drain the emission contract's ERG. The anti-draining measures help mitigate this risk.

- **Oracle Manipulation**: The design relies on accurate oracle price feeds. Safeguards against oracle attacks and manipulations should be considered.

- **Demand Shifts**: Significant drops in demand for Dexy could lead to persistent selling pressure. The stabilizing mechanisms may need to be robust enough to handle such scenarios.

- **Modeling and Simulation**: Thorough modeling of the economic incentives, game theory, and attack scenarios would provide valuable insights into the system's stability and resilience.

- **Iteration and Monitoring**: Starting with DexyGold allows for iterative refinement before potentially moving to a USD-pegged version. Close monitoring of the system's performance under various market conditions is crucial.

## Terra Comparison and Collateralization

There have been some discussions comparing Dexy to the original Terra MM (Market Module) algorithm. However, it's important to note that Dexy incorporates overcollateralization, which helps prevent the "death spiral" scenario that affected Terra.

In Terra's system, the base currency (Luna) could experience infinite inflation in an attempt to maintain the peg of the stablecoin. In contrast, Dexy and other Djed-like stablecoins use overcollateralization to avoid this death spiral.

It's worth noting that the collateralization mechanism in Dexy differs from that of SigmaUSD-like stablecoins:

- In Dexy, the ERG used as collateral is explicitly visible in the protocol-owned liquidity in the bank and LP contracts.
- The collateral is not an illusion based on dynamic supply, as was the case with Luna.
- The draft whitepaper discusses the worst-case scenario in Chapter 4.
- Collateral levels in Dexy may vary over time:
  - If the system performs well and mint/LP fees accumulate, the collateral ratio could exceed 400% in the long run.
  - At launch, the collateral ratio is expected to be slightly above 100%.
  - In the worst-case scenario, if the gold price significantly outperforms ERG, the protocol could become undercollateralized.

While there may be some superficial similarities between Dexy and Terra's original MM algorithm, the incorporation of explicit overcollateralization and the transparent nature of the collateral distinguish Dexy from Terra's model.

As with any new stablecoin design, thorough testing, analysis, and monitoring will be crucial to ensure the robustness and stability of the Dexy system under various market conditions.

## Resources and Community

- [DexySpec](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/dexy/DexySpec.scala)
- [Dexy Stablecoin Design](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/dexy/Dexy.md)
- [Dexy: USD Simplest Stablecoin](https://www.ergoforum.org/t/dexy-usd-simplest-stablecoin-design/1430)
- [Dexy Enhancements and Attack Mitigation](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/dexy)
- Join the DexyGold community on [Telegram](https://t.me/dexygold) or [Discord](https://discord.gg/ergo-platform-668903786361651200)
