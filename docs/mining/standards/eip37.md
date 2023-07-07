---
tags:
  - EIPs
---

# Tweaking Difficulty Adjustment Algorithm


## EIP Details

* Author: kushti
* Status: Implemented
* Created: 23-Sep-2022
* Last edited: 02-Oct-2022
* License: CC0
* Forking: hard fork needed 

> 🔗 From [EIP-0037](https://github.com/ergoplatform/eips/blob/ddbca24fef5e91e0c80c6881fc31d8831ae69768/eip-0037.md)


## Motivation 

A difficulty adjustment algorithm attempts to stabilise the average time to generate a block by changing the difficulty of solving the Proof-of-Work puzzle. It does this by observing the difficulties and timestamps of historical blocks to determine how fast the current hashrate is mining blocks, and how much it needs to increase to reduce or increase the difficulty to reach the target of 120 seconds per block in Ergo's case.  

Bitcoin uses a simple [linear difficulty recalculation](https://en.bitcoinwiki.org/wiki/Difficulty_in_Mining), with some caveats, such as the difficulty never being changed by more than a factor of four each way to prevent large changes. 

Bitcoin's difficulty readjustment algorithm works fairly well when dedicated, and loyal mining hardware works on the PoW puzzles. However, in other environments, different issues were observed with it, including coin hopping. Thus different solutions to coin hopping appeared, including using the least squares method-based predictive algorithm (Meshkov D., Chepurnoy A., Jansen M. Short paper: Revisiting difficulty control for blockchain systems) as done in Ergo.

The original Ergo algorithm worked well in most cases, including huge price drops, 100x initial difficulty misestimation during mainnet launch, etc.However, the current simplified and limitless version of the algorithm is bumpy. A big influx of mining hash rate over multiple epochs, especially with super-linear hash rate growth over time, can result in a huge difficulty spike. Similarly, a few slow epochs may cause a huge drop. Also, for dapps and other applications, it would be desirable to make difficulty readjustment more reactive (currently, readjustment takes place every 1024 blocks, and eight epochs, so about two weeks normally, are considered).   

## Related Work

To prevent disastrous effects of hopping, a general approach (see, e.g. [bch](https://read.cash/@jtoomim/bch-upgrade-proposal-use-asert-as-the-new-daa-1d875696) ) is to use a weighted averaging function over past `x` epochs with no preference for the latest epochs.

However, in the case of natural hash rate migration, such functions will likely lag (in contrast to the proactive nature of the predictive least square method). 

## Proposed Changes

We propose to make current difficulty readjustment more reactive and smoother by shortening epoch length, amplifying the weight of the last epoch, and putting some limits on difficulty change as follows.

1. The epoch length will be set to 128 blocks. 
2. We calculate two figures. A *predictive* difficulty according to the past eight epochs (128 blocks each); and *classic* difficulty as done in Bitcoin
3. We limit predictive difficulty change so that it never be changed by more than 50% per epoch. Then we take the average from the classic and predictive difficulties. 
4. We limit change so that difficulty never be changed by more than 50% per epoch.


## Simulations

For some previous simulations, see the [BCH upgrade proposal](https://read.cash/@jtoomim/bch-upgrade-proposal-use-asert-as-the-new-daa-1d875696) and [DifficultyControlSimulator.scala](https://github.com/ergoplatform/ergo/blob/0af9dd9d8846d672c1e2a77f8ab29963fa5acd1e/src/test/scala/org/ergoplatform/tools/DifficultyControlSimulator.scala)). However, these are based on observed historical data and ignore that miners will behave differently in the presence of different difficulty adjustment methods.

To combat this, we made a playground simulating random price walking in an uptrend or downtrend. In this simulation, the blockchain is mined by rational hash power only, and Hashrate looks at the current price and difficulty. 

1. We assume that price and difficulty are changed simultaneously, and then the hash rate moves in or out, affecting average block generation time **t**. 
2. We may assume then that **t = d * c / p**, so average block generation time **t** is proportional to difficulty **d** and inversely proportional to price **p**. 
3. Fixing **t** (set to target block generation time, so 2 minutes), **d**, and **p** at the beginning of the experiment, we can evaluate **c**. 
4. Then, on each step, we are randomly changing **p**, and according to the difficulty from the previous epoch, we can get the average block generation time for the new epoch.
5. To have a trend in price, we are changing **p** by adding (or subtracting) a random value with a fixed average and a random fluctuation. 

**Test results:**

> If price growth is up to 5% per epoch, and possible fluctuation (up or down) is up to 10%:

- *Bitcoin DAA*: total error: 158841, max delay: 133
- *Current DAA*: total error: 189403, max delay: 151
- *Proposed DAA*: total error: 163893, max delay: 141 


> If no price growth and possible fluctuation (up or down) is up to 25% (so the price is jumping up and down like crazy):

- *Bitcoin DAA*: total error: 393770, max delay: 161
- *Current DAA*: total error: 528003, max delay: 224
- *Proposed DAA*: total error: 429667, max delay: 193 

> If average price growth is up 2% per epoch (max delay missed as it is 120s max for all the options):

- *Bitcoin DAA*: total error: 30409
- *Current DAA*: total error: 19111
- *Proposed DAA*: total error: 20691

> If average price growth is up 10% per epoch (max delay missed as it is 120s max for all the options):

- *Bitcoin DAA*: total error: 143161
- *Current DAA*: total error: 92861
- *Proposed DAA*: total error: 105741

> 3 epochs price going up, three epochs down, 25% max change

- *Bitcoin DAA*: total error: 380139, max delay: 160
- *Current DAA*: total error: 464081, max delay: 221
- *Proposed DAA*: total error: 387880, max delay: 185

> Coin hopping - first epoch up to 50% of the total hash rate jumping on, next epoch jumping off 

- *Bitcoin DAA*: total error: 770422, max delay: 192
- *Current DAA*: total error: 586972, max delay: 210
- *Proposed DAA*: total error: 670691, max delay: 182

The total error is the sum of differences between the observed block generation time and target (120s): the less total error, the better.

As we can see, the proposed DAA, as well as the current one, is working better during trends, and also, in the case of 1-epoch coin hopping, the proposed DAA softens swings better than the current one. 

## Activation

- It is possible to activate EIP-37 after block #843,776 and before block #851,969. 
- For activation, 232 or more votes for activation required in the last 256 blocks, with voting checked every 128 blocks (for blocks whose height % 128 == 1)
- Immediate activation once the threshold is met. 

## Implementation

The proposed difficulty adjustment algorithm and activation procedure are implemented in the reference protocol client 4.0.100 and [all newer versions]((https://github.com/ergoplatform/ergo/releases).


