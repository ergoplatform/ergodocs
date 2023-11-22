# Collateral Mining

We are pleased to introduce Collateral Mining, a unique feature of Ergo Blockchain that provides an innovative approach to mining and incentivizes participation in the network. This documentation will explain the intricacies of Collateral Mining, including its architecture, consensus mechanism, transaction validation, smart contracts, APIs, and various features, catering to both developers and end users.

## Introduction

Collateral Mining is a mechanism that allows miners to participate in the mining process by utilizing their collateral as a stake. It offers an alternative to traditional mining pools and provides a secure and efficient method for miners to contribute their computational power to the network.

## Architecture

The Collateral Mining architecture consists of a collateral box script, which governs the rules and conditions for mining rewards. The script defines three main cases that determine the eligibility for receiving rewards:

### Case 1: Block Mined by Alice

In this case, if the block is mined by Alice, the following conditions must be met to receive the pool reward:

- The block contains either one output of value `poolReward` or two outputs, where the first output is of value `poolReward` and the second output goes to Alice.
- The miner's public key decoded from the transaction context should match Alice's public key.
- The block height should be greater than the creation height of the current box (`SELF`).
- The number of outputs should be either 1 or 2, and if there are two outputs, the second output should have the same proposition bytes as `SELF` and the same creation height as the current block.

### Case 2: Collateral Top-Up

In this case, anyone can contribute additional collateral funds to an existing collateral box. The conditions for a successful top-up are as follows:

- The first output of the block should have the same proposition bytes as `SELF`.
- The creation height of the first output should be greater than or equal to the creation height of the current box.
- The value of the first output should be greater than the value of `SELF`.

### Case 3: Collateral Withdrawal by Alice

This case allows Alice to withdraw her collateral at any time. To initiate a withdrawal, Alice needs to prove ownership of her collateral through a discrete logarithm proof.

## Limitations and Considerations

The primary limitation of Collateral Mining is that only one unspent collateral box can exist at a time for a given miner public key. This restriction prevents a pool from spending multiple boxes in the same block and claiming a multiple of the reward. Although this limitation exists, we believe it is reasonable and avoids the complexity associated with miners creating special signatures to address this issue. To mitigate any potential concerns, the top-up mechanism (case 2) enables anyone to contribute additional collateral to a specific box.

Furthermore, it is worth noting that the pool reward, initially set at 67.5 ERG, can be adjusted to provide additional incentives. However, it is important to mention that miners already receive all transaction fees associated with the blocks they mine.

## Additional Resources

For further understanding and engagement with Collateral Mining on Ergo Blockchain, we recommend exploring the following resources:

- Proposal of the Collateral Mechanism by [@scalahub](https://www.ergoforum.org/t/creating-an-ergo-mining-pool/42) in July 2019.
- Research paper authored by [@kushti](https://eprint.iacr.org/2020/044) and [@scalahub](https://eprint.iacr.org/2020/044) detailing the Collateral Mining concept.
- In-depth discussion and community insights on the [Ergo Forum](https://www.ergoforum.org/t/collateral-script-for-pool-mining/200) regarding the Collateral Script for Pool Mining.
