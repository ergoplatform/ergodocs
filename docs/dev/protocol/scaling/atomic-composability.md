---
tags:
  - Atomic Composability
  - DeFi
  - Blockchain
  - Scaling
  - Sharding
  - Layer 2
---

# Atomic Composability 

## The Importance of Atomic Composability

Decentralized Finance (DeFi) derives its power from its open-source nature, which allows for the reuse, modification, and integration of decentralized applications (dApps) into existing ones. This composability enhances the overall ecosystem's value. However, achieving atomic composability, where all relevant transactions either execute successfully or none at all, is crucial for certain DeFi applications involving flash loans and instant arbitrage. Some scaling solutions, such as sharding and Layer 2 platforms, can introduce complexity and hinder reliable atomic composability.

## The Challenge of Scaling with Atomic Composability

The challenge for blockchain technology is not just scalability but maintaining atomic composability at scale. Ergo aims to utilize the available "headroom" in conventional blockchain platforms by employing resources more intelligently, rather than implementing untested technologies.

## Scaling Solutions and Atomic Composability

Scaling solutions often involve dividing the platform into subsections, such as shards or introducing a new layer on top of the base layer. However, incorrect implementation of these solutions can impede seamless interaction between assets and applications residing in different parts of the platform.

## Achieving Atomic Composability in Ergo

In Ergo, atomic composability is achieved through a combination of the eUTXO model, ErgoScript, Layer 2 solutions, and other proposed techniques.

### eUTXO Model and ErgoScript

The [eUTXO](https://ergoplatform.org/docs/utxo/) model, along with the ErgoScript smart contract language, enables the execution of complex, [multi-stage transactions](multi.md) atomically within a single transaction. Multistage protocols ensure that all parts of a transaction are executed or none are, which is fundamental to atomic composability. ErgoScript facilitates the creation and execution of intricate smart contracts with confidence in their outcomes, while leveraging the advantages of the UTXO model, such as statelessness, better parallelism, and more reliable data handling.

### Layer 2 Solutions - Hydra State Channels

Layer 2 solutions like [Hydra state channels](https://ergoplatform.org/docs/hydra/) also support atomic composability. Hydra enables cross-head communication, allowing complex operations to be executed atomically across different heads, even when involving multiple state channel participants.

### ACE (Asynchronous and Concurrent Execution of Complex Smart Contracts)

Ergo could further enhance its ability to execute complex and composable smart contracts by implementing ideas like [ACE](https://eprint.iacr.org/2019/835.pdf). ACE proposes breaking down smart contracts into smaller, concurrent tasks that can be executed independently, improving overall performance and throughput. It enables one contract to safely call another contract executed by a different set of service providers, facilitating off-chain execution of interactive smart contracts with flexible trust assumptions and enhancing atomic composability.

## Sharding and Atomic Composability

### Sharding Explained

Sharding is a technique that partitions a blockchain network into smaller sections called shards to improve scalability. Each shard independently processes a subset of transactions. However, ensuring atomic composability, where all parts of a multi-step transaction execute or none do, can be challenging in a sharded environment.

### Strategies for Maintaining Atomic Composability in Sharding

Here are potential strategies to maintain atomic composability when sharding:

#### Cross-shard transactions

Implement a mechanism for secure and efficient communication between shards, enabling cross-shard transactions. This mechanism ensures that all parts of a multi-step transaction are either committed or rolled back, even when spanning multiple shards.

#### Locking mechanisms

Introduce locking mechanisms to prevent double-spending and fraud during cross-shard transactions. Temporarily locking involved assets until the transaction completes helps maintain atomic composability.

#### Two-phase commit protocols

Utilize [two-phase commit protocols](layer2.md) to coordinate cross-shard transactions. In the first phase, shards tentatively execute the transaction and lock relevant assets. In the second phase, when all shards confirm the transaction, it is committed, and locked assets are released. If any shard fails to confirm, the transaction is rolled back, and locked assets are released.

#### Optimistic execution

Allow shards to optimistically execute transactions assuming resolved dependencies between shards. If conflicts arise later, the transaction can be rolled back, and the network can learn from the conflict to prevent similar issues.

#### State channels or sidechains

Employ state channels or sidechains to process transactions off-chain, settling the final state back on the main chain. These off-chain solutions enable complex, multi-step transactions without directly involving multiple shards, thus maintaining atomic composability.

These strategies provide a general framework for maintaining atomic composability in a sharded blockchain environment. Specific implementation details would depend on the requirements and design of yet-to-emerge dApps.