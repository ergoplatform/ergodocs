---
tags:
  - ErgoScript
  - Contracts
---

# ErgoScript Contracts

### Ergo Contracts

The [ergo-contracts](https://github.com/ergoplatform/ergo-contracts) repository contains source code for Ergo smart contracts, along with compilation, testing, and formal verification tooling.

- [AssetsAtomicExchange.scala](https://github.com/ergoplatform/ergo-contracts/blob/42719326656e4764f214f57fa8f45205ee20d58d/verified-contracts/src/main/scala/org/ergoplatform/contracts/AssetsAtomicExchange.scala)
- [CrowdFundingContractVerification.scala](https://github.com/ergoplatform/ergo-contracts/blob/42719326656e4764f214f57fa8f45205ee20d58d/verified-contracts/src/main/scala/org/ergoplatform/contracts/CrowdFundingContractVerification.scala)
- [DummyContractVerification.scala](https://github.com/ergoplatform/ergo-contracts/blob/42719326656e4764f214f57fa8f45205ee20d58d/verified-contracts/src/main/scala/org/ergoplatform/contracts/DummyContractVerification.scala)
- [Edex.scala](https://github.com/ergoplatform/ergo-contracts/blob/42719326656e4764f214f57fa8f45205ee20d58d/verified-contracts/src/main/scala/org/ergoplatform/contracts/Edex.scala)
- [ICOContractVerification.scala](https://github.com/ergoplatform/ergo-contracts/blob/42719326656e4764f214f57fa8f45205ee20d58d/verified-contracts/src/main/scala/org/ergoplatform/contracts/ICOContractVerification.scala)

### ErgoScript Examples

| Number | Difficulty | Title |
| ---  | ---  | ---  |
| 1 | Beginner | [Pin Lock Contract](https://github.com/ergoplatform/ergoscript-by-example/blob/main/pinLockContract.md) |
| 2 | Intermediate | [Single-Chain Swap Contracts](https://github.com/ergoplatform/ergoscript-by-example/blob/main/singleChainSwap.md) |
| 3 | Starter | [Simple Send](https://github.com/ergoplatform/ergoscript-by-example/blob/main/simpleSend.md) |
| 4 | Intermediate | [Double-Chain Swap Contracts](https://github.com/ergoplatform/ergoscript-by-example/blob/main/doubleChainSwap.md) |
| 5 | Beginner | [Timed Fund Contract](https://github.com/ergoplatform/ergoscript-by-example/blob/main/timedFund.md) |
| 6 | Beginner | [Grantor/Beneficiary Pin Lock Contract](https://github.com/ergoplatform/ergoscript-by-example/blob/main/grantorBeneficiaryPinLock.md) |
| 7 | Beginner | [Escrow Deposit Contract](https://github.com/ergoplatform/ergoscript-by-example/blob/main/escrowDepositContract.md) |
| 8 | Expert | [Token sales service contract](https://github.com/ergoplatform/ergoscript-by-example/blob/main/tokenSalesService.md) |
| 9 | Beginner | [Self-Replicating Sale Contract](https://github.com/ergoplatform/ergoscript-by-example/blob/main/selfReplicatingTokenSale.md) |
| 10 | Intermediate | [Heads or Tails game Contract](https://github.com/ergoplatform/ergoscript-by-example/blob/main/headsOrTails.md) |
| 11 | Expert| [Stealth Address](https://github.com/ergoplatform/ergoscript-by-example/blob/main/stealthAddress.md) |
| 12 | Expert | [Heads or Tails game Contract with Parallelization](https://github.com/ergoplatform/ergoscript-by-example/blob/main/headsOrTailsParallel.md) |

### sigmastate-interpreter examples

- [IcoExample.scala](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/c863a9b1a82589e47b15f76f3affdb30a475e740/sigmastate/src/test/scala/sigmastate/utxo/examples/IcoExample.scala#L254-L303)
- [Many more](https://github.com/ScorexFoundation/sigmastate-interpreter/tree/c863a9b1a82589e47b15f76f3affdb30a475e740/sigmastate/src/test/scala/sigmastate/utxo/examples)

## dApps and Tooling Contracts


### Deployed Contracts

- [GuapSwap](https://github.com/GuapSwap/guapswap-ronin/tree/main/src/main/scala/contracts)
- [Lilium](https://github.com/LiliumErgo/scala-api/blob/main/app/contracts/LiliumContracts.scala)
- [Paideia](https://github.com/paideiadao/paideia-contracts)
- [ErgoMixer](https://github.com/ergoMixer/ergoMixBack/tree/master/mixer/app/mixer)
- [Rosen Bridge](https://github.com/rosen-bridge/contract)
- [Thz.FM](https://github.com/TremendouslyHighFrequency/SmartContracts)
- [EXLE](https://github.com/Ergo-Lend/edge/blob/main/src/main/scala/edge/contracts/Contract.scala)
- [Spectrum Finance](https://github.com/spectrum-finance/ergo-dex/tree/master/contracts)
- [Pheonix Finance (Hodlcoin V2)](https://github.com/PhoenixErgo/phoenix-hodlcoin-contracts)
- [SkyHarbor](https://github.com/skyharbor-market/contracts)
- [Hodlbox](https://github.com/SavonarolaLabs/hodlbox-xyz/tree/main/src/lib/contract)
- [SigmaO](https://github.com/ThierryM1212/SigmaO/tree/main/contract)
- [SigmaUSD](https://github.com/anon-real/sigma-usd/tree/master/ageusd) 
- [Ergo Raffle](https://github.com/ErgoRaffle/raffle-backend/blob/master/app/raffle/RaffleContract.scala)
- [Auction Coin](https://github.com/Auction-Coin/contracts)
- [Sigma Finance](https://github.com/K-Singh/Sigma-Finance/tree/master/contracts)
- [Comet Lottery](https://github.com/mgpai22/comet-lottery/blob/main/comet-lottery-bot/src/main/scala/contracts/LotteryContracts.scala)
- [Duckpools](https://github.com/duckpools/lend-protocol-contracts/tree/main/contracts)
- [ergopad](https://github.com/ergopad/ergopad-api/tree/dev/app/contracts)

### EIPs

- [Babel Fees](https://github.com/ergoplatform/eips/blob/master/eip-0031.md)
- [Oracle Pools v2](https://github.com/ergoplatform/eips/tree/cae50b722d6929c794847d21668500acb01f3c8c/eip-0023/contracts)
- [Stealth Addresses](https://github.com/ergoplatform/eips/pull/87/files)
- [Auction contract V2](https://github.com/ergoplatform/eips/blob/master/eip-0022.md)
- [SigmaUSD Bank](https://github.com/ergoplatform/eips/blob/master/eip-0015.md)
- [ErgoFund](https://github.com/ergoplatform/eips/pull/33)


### In Development
- [Dexy](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/dexy/DexySpec.scala)
- [Bitdomains](https://github.com/bitdomains/contracts)
- [ErgoNames](https://github.com/ergonames/ergonames/blob/master/src/main/scala/)
- [Analog Ergo](https://github.com/dzyphr/ScalaSigmaParticle)
- [Chaincash](https://github.com/ChainCashLabs/chaincash/tree/master/contracts)
- [AnetaBTC](https://github.com/anetabtc/aneta_contracts)
- [Lithos](https://github.com/Lithos-Protocol/Lithos/tree/master/src/main/scala)
- [SigmaJoin](https://github.com/ergoplatform/ergo-jde/tree/main/kiosk/src/test/scala/kiosk/mixer)
- [Trade-In Contracts (BlitzTCG)](https://github.com/lucagdangelo/trade-in/tree/main/src/main/scala/contracts)

### Misc

- [smartpooling-contracts](https://github.com/GetBlok-io/ergo-smartpooling-contracts/tree/master/src/main/scala/contracts)
- [ergo-index](https://github.com/ergo-index/ergo-index-contracts)
- [Subpooling](https://github.com/GetBlok-io/Subpooling/tree/mainnet_plasma/conf/scripts)
- [chain-name-service](https://github.com/ross-weir/chain-name-service/tree/main/contracts)
- [AgeUSD](https://github.com/ergoplatform/eips/pull/33)
- [ErgoGravity](https://github.com/mhssamadani/gravity-core/blob/dev/contracts/ergo/gravity.scala) & [ErgoNebula](https://github.com/mhssamadani/gravity-core/blob/dev/contracts/ergo/nebula.scala)
- [Oracle Pools v0.4a](https://github.com/scalahub/Kiosk/tree/master/src/test/scala/kiosk/oraclepool/v4a)
- [NightOwl](https://github.com/nightowlcasino/ergoscript-contracts)
- [Hodlcoin (V1?)](https://github.com/lucagdangelo/hodlcoin-contracts)

### ToDo

- [single-tx-swap](https://github.com/danieloravec/ergo-token-swap)
- [Gluon](gluon.md)
- [Palmyra](palmyra.md)
- [on-chain swaps contracts](https://github.com/ergoplatform/sigma-rust/pull/209)


## Resources

- [contract-testing](https://github.com/anon-real/contract-testing) provides a quick tutorial that may be useful for testing your contracts off-chain.



### Ergoforum

- [Offchain Bank operating at Layer 2](https://www.ergoforum.org/t/offchain-bank-operating-at-layer-2/3367)
- [Decentralised Grid Contract](https://www.ergoforum.org/t/decentralized-grid-trading-on-ergo/3750/5)
- [Market-driven emission contracts](https://www.ergoforum.org/t/market-driven-emission-contracts/3749)
- [Interest-Free Loan Contract ](https://www.ergoforum.org/t/interest-free-loan-contract/67)
