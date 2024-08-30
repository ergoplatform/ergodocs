
# Voting Cycles and Types of Changes

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


Parameter values are to be written into the extension section on the first block of a voting epoch, that is, in the extension of a block when its $height\,mod\,1024 = 0$.

Parameters for the initial moment of time~$(height = 1)$ are hardcoded.

## How to Propose and Vote for Changes

To propose a change, a miner includes the vote identifier in the first block's header of a voting epoch. The header has three slots: two for everyday changes and one for soft forks. A zero should be set in any unoccupied slot. Votes can be arranged in any sequence.

For example, if a miner proposes to increase the storage fee factor and also initiate a soft-fork, they would input `(0, 1, 120)` in the header slots.
