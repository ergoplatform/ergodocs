---
tags:
  - Mining
  - Resources
  - Papers
  - Code
  - EIP
  - Test Vectors
owner: docs
last_reviewed: 2026-08-21
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/scala/org/ergoplatform/mining
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/scala/org/ergoplatform/mining
---

# Mining Resources

This page provides a collection of resources related to Ergo mining. It includes academic papers, code repositories, test vectors, and discussion threads.

## Academic Papers

- [Ergo White Paper](https://www.docdroid.net/mcoitvK/ergopow-pdf): This paper provides a comprehensive overview of Ergo, including its design principles, consensus algorithm, and economic model.

- [Ergo Yellow Paper](https://www.docdroid.net/mcoitvK/ergopow-pdf): The Yellow Paper offers a more technical perspective on Ergo, detailing the platform's underlying algorithms and data structures.

- ["Bypassing Non-Outsourceable Proof-of-Work Schemes Using Collateralized Smart Contracts"](https://ia.cr/2020/044): This paper discusses a novel approach to bypassing non-outsourceable proof-of-work schemes using smart contracts.

## Code

The [Ergo GitHub repository](https://github.com/ergoplatform/ergo/tree/master/src/main/scala/org/ergoplatform/mining) contains the Scala files related to Ergo's mining algorithm. This is a great resource if you're interested in understanding the technical details of Ergo mining.

Recent node versions cache block candidates and regenerate them on a timed interval. The default `blockCandidateGenerationInterval` in the reference configuration is `60s`, and mining code handles expired cached candidates before producing work for miners.

Reference client v6.0.4 also recovers when a locally mined block fails syntactic or semantic validation. The candidate generator clears the rejected solved block and cached candidates, while the node removes an identifiable failing transaction from the mempool; a subsequent mining request then generates fresh work instead of repeatedly returning `Block already solved`.

Mainnet 6.0 voting settings were added to `mainnet.conf` with voting starting height `1561601`. The reference client advertises the 6.0.x app version while mainnet chain settings use protocol version 4 for the 6.0 interpreter feature set.

The mining API also exposes a custom-public-key candidate route at `POST /mining/candidateWithTxsAndPk` for operators who need a block candidate with mandatory transactions and a miner-supplied public key. Treat it as an operator-facing mining helper, not a general node API route.

## Test Vectors

- [Test vectors for increased N values](https://www.ergoforum.org/t/test-vectors-for-increased-n-values/2887/2): This forum post provides test vectors for Ergo's proof-of-work algorithm with increased N values.

## EIPs

- [EIP27](eip27.md)
- [EIP37](eip37.md)
