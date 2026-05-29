---
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ergoplatform/ergo-jde
    branch: main
    paths:
      - kiosk/src/test/scala/kiosk/dexy
      - kiosk/src/test/scala/kiosk/dexy/Dexy.md
      - kiosk/src/test/scala/kiosk/dexy/DexySpec.scala
  - repo: arkadianet/citadel
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/ergoplatform/ergo-jde/tree/main/kiosk/src/test/scala/kiosk/dexy
  - https://github.com/ergoplatform/ergo-jde/tree/main/kiosk/src/test/scala/kiosk/dexy/Dexy.md
  - https://github.com/ergoplatform/ergo-jde/tree/main/kiosk/src/test/scala/kiosk/dexy/DexySpec.scala
  - https://github.com/arkadianet/citadel/releases/tag/v0.2.4-alpha
  - https://github.com/DefiLlama/peggedassets-server/pull/700
---

# Stablecoins

Blockchain assets can be extremely volatile. That’s why investors often seek digital assets which are pegged to national currencies. A Stablecoin is the most primitive integration of cryptocurrencies with the off-chain world. Until DAI, fiat custody services were provided by centralized services. The first example of a stable coin, USDT, is backed by [actual dollars](https://cryptobriefing.com/external-auditor-first-confirm-tethers-usdt-backing/) held in banks. However, for a decentralized financial system, we need other means of fiat-pegged currencies.

## SigmaUSD
>
> [sigmausd.io](https://sigmausd.io), The worlds first UTxO-based stable coin - an instantiation of the [AgeUSD protocol](https://github.com/Emurgo/age-usd). Its economic model designed in partnership between IOHK, Ergo, and Emurgo maintains the conservative settings for collateral reserves and avoids the need for liquidations. Along with that, it supports a fully decentralised stablecoin emission setup.

The UI for the front-end is available at [anon-real/sigma-usd](https://github.com/anon-real/sigma-usd). For more information and a more general overview please see [ergonaut.space](https://ergonaut.space)

- [Ergo Summit 2021 - The IOHK Perspective - Designing the AgeUSD StableCoin](https://youtu.be/zG-rxMCDIa0?t=9247)
- [Overview Video (with diagrams)](https://www.youtube.com/watch?v=O3hPEp3tzoU)
- [Building Ergo: How the AgeUSD stablecoin works](https://ergoplatform.org/en/blog/2021-02-05-building-ergo-how-the-ageusd-stablecoin-works/)
- [Lessons for sigmausd from the DJED paper](https://www.ergoforum.org/t/lessons-for-sigmausd-from-the-djed-paper/2345)

## Dexy

Dexy uses seigniorage

- [Dexy overview](dexy.md)
- [USE stablecoin](use_stablecoin.md)
- [DexySpec](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/dexy/DexySpec.scala)
- [Dexy Stablecoin Design](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/dexy/Dexy.md)
- [Dexy: USD Simplest Stablecoin](https://www.ergoforum.org/t/dexy-usd-simplest-stablecoin-design/1430)
- [Dexy enhancements to counter various attacks in vanilla proposal](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/dexy)
- [Citadel v0.2.4-alpha](https://github.com/arkadianet/citadel/releases/tag/v0.2.4-alpha) added SigUSD routing, token-to-token swaps, LP deposit/redeem support, and Dexy LP display fixes.
- [USE pegged asset on DefiLlama](https://github.com/DefiLlama/peggedassets-server/pull/700) tracks the USE stablecoin alongside its public protocol information.

## Gluon

[Gluon](gluon.md) is a stablecoin protocol on Ergo using fission, fusion, and beta-decay operations. Its current Ergo UI is tracked separately from SigmaUSD and Dexy.
