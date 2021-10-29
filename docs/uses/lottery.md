**First some background**

The idea in this post is motivated from the post about [Proof-of-Activity as a Smart Contract](https://www.ergoforum.org/t/proof-of-activity-as-a-smart-contract/132).

The goal of "proof of activity" is to reward members for their "activity" (i.e., for running a full node). 
Without going into details, the approach essentially is based on "proof-of-stake" such that people who are active receive larger rewards than inactive people holding similar stake. The purpose is to discourage people having stake but not actively participating in the network.

The key method behind all proof of stake and proof of activity is *follow-the-satoshi*, which picks a random satoshi from all the generated ones and then the holder of that satoshi is eligible for the reward. If the satoshi is selected unformly then this is similar to a lottery system.

**The Lottery**

The goal of this post is not to have a proof of stake or proof of activity. Rather it is about emulating the follow-the-satoshi protocol to have a provably fair lottery system.

The lottery that we will create emulates the following physical lottery:
1. Company generates lottery tickets in sequential serial numbers
2. There is only one place to buy the tickets
3. Tickets can only be purchased in sequential serial numbers using the "next available serial number" rule, (starting from serial number 0). 
4. After the lottery is closed (so that no more tickets can be sold), the first unsold serial number ***n*** is noted. 
5. A random number ***r*** is generated between 0 and ***n***-1 (both inclusive).
6. The holder of ticket with serial number ***r*** is the winner. 

We can emulate this with Ergo as follows.

The lottery owner creates a "lottery box" containing tokens and the current available serial number in **R4**. This is protected by a script that sells tokens and the balance tokens are kept in an identical box with the serial number appropriately incremented. Furthermore the purchased tokens are to be kept in a "purchase box" box containing in **R4** and **R5** respectively, the start and end serial numbers of purchased tokens. We additionally require the script in the purchase box to "lock" these values, so they cannot be altered by the buyer. 

After the lottery ends, the last serial number ***n***is stored in **R4** of the lottery box. Using this, winner is decided using, say taking randomness from the previous block header to generate  a number uniformly between 0 and ***n*** to decide the winner. The winner can use his purchase box to take the rewards.

The rewards can be stored in the lottery box itself and each ticket purchased contributes to the reward. 

While this works in a fair way, it is not deterministic as it depends on the last block header.

Since each "previous block" decides a different winner for the same ***n***, this also can be used as a proof of activity because the current winner must be onlline.

See [this thread](https://www.ergoforum.org/t/a-lottery-on-top-of-ergo/137) for full discussion