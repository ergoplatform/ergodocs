---
tags:
  - Voting
  - Soft Fork
  - Forking
---


# Governance

### Overview

In Ergo, many network parameters are adjustable through a decentralized voting mechanism among miners. Such parameters include computational costs, block size limits, and storage fees. The long-term economic stability of the Ergo network is thus steered by miner consensus.

Miners can vote to change specific protocol parameters, as [outlined in the table below](#parameters-table). Soft-forking changes, requiring 90% miner support, can also alter many aspects of Ergo, barring critical elements like maximum supply.

### Voting Cycles and Types of Changes

Votes on foundational changes, such as block version, span **32 epochs** and demand a **90% miner consensus**. Everyday changes, like block size adjustments, require only a simple majority. Each block allows miners to cast votes for up to two everyday changes and one foundational change. These votes are included in the block's header.

### Voting Mechanics

#### Affirmative Votes
To vote "Yes" for a change at the beginning of an epoch, a miner places the change's identifier directly into the block header.

#### Negative or Neutral Votes
To vote "No" or abstain, a miner enters a zero value in place of the identifier byte in the block header.

### System Constants

- Epoch length for voting: `1024` blocks
- Epochs needed for foundational change: `32`
- Epochs before activating approved foundational change: `128`

### Current Network Settings

- Maximum block size: `1271009` bytes
- Maximum box size: `4096` bytes
- Maximum transaction size: `96kb`

## Parameters Table

The following table describes vote identifiers, default values (during launch), possible steps, and minimum and maximum values. 

- If the step is not defined in the table, its value is defined as $\max(\lfloor current\_value / 100 \rfloor, 1)$. 
- If the minimum value for a parameter is not defined, it equals zero. 
- If the maximum value is not defined, it equals `1,073,741,823`.

A miner includes a parameter identifier ($id$) into the block header to propose or vote for increasing a parameter.

If the miner supports decreasing the parameter, they would include ($-id$) into the block header.

> Try out these parameters on [deadit.github.io/paizo/](https://deadit.github.io/paizo/)

| ID | Description | Default | Step | Min | Max |
|---|---|---|---|---|---|
| 1 | Storage fee factor (per byte storage period) | 1250000 | 25000 | 0 | 2500000 |
| 2 | Minimum monetary value of a box | 360 | 10 | 0 | 10000 |
| 3 | Maximum block size | 524288 |  | 16384 |  |
| 4 | Maximum cummulative computational cost of a block | 1000000 |  | 16384 |  |
| 5 | Token access cost | 100 |  |  |  |
| 6 | Cost per one transaction input | 2000 |  |  |  |
| 7 | Cost per one data input | 100 |  |  |  |
| 8 | Cost per one transaction output | 100 |  |  |  |
| 120 | Soft-fork (increasing version of a block) |  |  |  |  |



Parameter values are to be written into the extension section on the first block of a voting epoch,
that is, in the extension of a block when its $height\,mod\,1024 = 0$.

Parameters for the initial moment of time~$(height = 1)$ are hardcoded.

## How to Propose and Vote for Changes

To propose a change, a miner includes the vote identifier in the first block's header of a voting epoch. The header has three slots: two for everyday changes and one for soft forks. A zero should be set in any unoccupied slot. Votes can be arranged in any sequence.

For example, if a miner proposes to increase the storage fee factor and also initiate a soft-fork, they would input `(0, 1, 120) in the header slots.



## Soft-Fork Mechanism in Ergo

Soft forks in the Ergo blockchain allow for backward-compatible protocol updates, enabling the network to introduce new rules or deactivate existing ones without requiring a hard fork. The soft-fork process is governed by a strict voting mechanism that involves miners and unfolds over a series of epochs. This article outlines the key steps, rules, and technical details involved in implementing a soft fork in the Ergo blockchain.

### Preconditions for a Soft Fork

1. **Software Update:** A protocol developer releases an updated version of the Ergo software that includes changes to existing rules or introduces new ones. This updated software version is made available to miners and nodes on the network.
2. **Proposal:** A soft-fork proposal is initiated when a miner includes a specific identifier (e.g., 120) in the first block of a new epoch, signaling the start of the voting process.

### Voting Process

1. **Duration:** The voting process spans 32 epochs, each consisting of 1,024 blocks. The total voting period thus covers 32,768 blocks.
2. **Threshold:** For a soft fork to be approved, it must receive at least 90% of the total votes, which equates to a minimum of 29,491 votes out of a possible 32,768.
3. **Negative Outcome:** If the proposal fails to meet the 90% threshold, the voting process concludes, and new proposals can be initiated in the subsequent epoch.
4. **Positive Outcome:** If the proposal secures the required votes, an activation period of 32 epochs begins immediately.

### Activation and Implementation

1. **Activation Period:** Following a successful vote, the network enters an activation phase that lasts for 32 epochs. During this period, the network prepares for the implementation of the new protocol rules.
2. **Activation Height:** The first block following the activation period is referred to as the 'activation height.' It is at this point that the new protocol rules come into effect.
3. **Block Versioning:** The block version is updated in the extension sections starting from the first block of the activation period. However, the protocol version in the block headers is only updated at the activation height.

### Technical Details

- **Validation Rules and Soft-Fork Process:** Specific validation rules in Ergo, as outlined in the `ValidationRules.scala` file, can be toggled or introduced during a soft-fork. These rules are flagged as `mayBeDisabled`, allowing the protocol to adapt to new requirements without breaking backward compatibility. For instance, the `exCheckForkVote` rule ensures that voting for a new fork is only permissible after the activation period of a previous soft-fork.
  
- **Block Generation and Soft-Fork Voting:** The process of block generation in Ergo is tightly integrated with the soft-fork voting mechanism. As seen in the `CandidateGenerator.scala` file, blocks are generated with considerations for whether they should include votes for a soft-fork based on the current height and state context. This logic ensures that votes are accurately recorded and the network remains synchronized during the voting period.

- **Fork-Ordering Logic:** The `forkOrdered` method plays a crucial role in determining whether the conditions for a soft-fork are met. This method checks the current block height, protocol version, and voting results to decide whether a soft-fork should proceed. This ensures that the network only moves forward with a soft-fork when all predefined conditions are satisfied.

### Examples

1. **Starting a Vote:** Assume a vote is proposed in block #1024 by including the identifier "120" in the extension section. If 500 votes are collected in that epoch, the next epoch's block (#2048) should include the pairs `122: 1024` (indicating the start height of the vote) and `121: 500` (indicating the votes collected).
   
2. **Counting Votes:** If the next epoch (starting at block #2048) gathers an additional 600 votes, the block at height #3072 should include the updated pairs `121: 1100` and `122: 1024`.

3. **Vote Outcome:** If the total votes collected between blocks #1024 and #33791 do not exceed 29,491, the vote fails, and new voting parameters can be initiated in the following epoch (starting at block #34816).

4. **Vote Success and Activation:** If the vote is successful, with more than 29,491 votes collected, the activation period begins immediately after block #33792. During the 32-epoch activation period, no new soft-fork proposals can be introduced. At the end of this period, the protocol version is updated in the block headers at the activation height, and the new rules take effect.

For more practical examples and a detailed discussion on soft-fork voting, refer to this [Ergo Forum post](https://www.ergoforum.org/t/voting-for-a-soft-fork-in-ergo/2958).
