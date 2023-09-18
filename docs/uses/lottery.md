# Background

The concept discussed in this post is inspired by the idea of [Proof-of-Activity as a Smart Contract](https://www.ergoforum.org/t/proof-of-activity-as-a-smart-contract/132).

The primary objective of "proof of activity" is to incentivize members for their "activity", which in this context refers to running a full node.

The underlying approach is essentially based on "proof-of-stake". This means that active participants receive larger rewards than those who hold a similar stake but are inactive. The aim is to deter individuals from holding a stake without actively contributing to the network.

The fundamental method behind both proof of stake and proof of activity is *follow-the-satoshi*. This method selects a random satoshi from all the generated ones, and the holder of that satoshi becomes eligible for the reward. If the satoshi is selected uniformly, this process resembles a lottery system.

# The Lottery

The focus of this post is not on proof of stake or proof of activity. Instead, it is about replicating the follow-the-satoshi protocol to establish a provably fair lottery system. It's worth noting that a similar lottery system is currently live in the COMET project.

The lottery system we aim to create will mimic the following physical lottery:

1. A company generates lottery tickets with sequential serial numbers.
2. There is a single location to purchase the tickets.
3. Tickets can only be bought in sequential serial numbers using the "next available serial number" rule (starting from serial number 0).
4. Once the lottery is closed (meaning no more tickets can be sold), the first unsold serial number ***n*** is recorded.
5. A random number ***r*** is generated between 0 and ***n***-1 (both inclusive).
6. The holder of the ticket with serial number ***r*** is declared the winner.

This can be emulated with Ergo as follows:

The lottery owner creates a "lottery box" that contains tokens and the current available serial number in **R4**. This box is protected by a script that sells tokens, and the remaining tokens are stored in an identical box with the serial number incremented accordingly.Moreover, the purchased tokens are stored in a "purchase box" that contains the start and end serial numbers of purchased tokens in **R4** and **R5** respectively. We also require the script in the purchase box to "lock" these values, preventing the buyer from altering them.

After the lottery concludes, the last serial number ***n*** is stored in **R4** of the lottery box. Using this, the winner is determined by, for example, using randomness from the previous block header to generate a number uniformly between 0 and ***n***. The winner can then use their purchase box to claim the rewards.

The rewards can be stored in the lottery box itself, and each ticket purchased contributes to the reward. 

While this system operates fairly, it is not deterministic as it depends on the last block header.

Since each "previous block" determines a different winner for the same ***n***, this can also be used as a proof of activity because the current winner must be online.

For a comprehensive discussion, refer to [this thread](https://www.ergoforum.org/t/a-lottery-on-top-of-ergo/137).
