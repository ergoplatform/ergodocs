# EIP-0027

EIP 0027 Emission Retargeting Soft-Fork
https://github.com/ergoplatform/eips/blob/eip27/eip-0027.md
Intent
Soft-forking Ergo Emission
There are a lot of concerns about the emission being over in less than six years from now.
The long-term sustainability of the short emission schedule is an inherent risk to the long-term viability of the Ergo Network.
The UTXO set is seeing good growth (visible here), but due to the nature of storage rent (which charges a fee on unmoved UTXOs after four years), the viability of storage rent economy as a way to protect the long-term economic viability and security of the network is in question.
We would like to create a system that offers economic incentives to miners in the short term while protecting the long-term crypto-economic security of the network.
Principles
Having unlimited emissions has given ETH tremendous flexibility in playing with its economic policy and network adjustments.
Ergo is committed to the principle that the total supply must be preserved.
Unfortunately, post-non-outsourceable puzzles, the governance scheme has changed. The governance model shifted from a democratic model where individual miners vote to a representative model where mining pools vote.
We know that this is not a very efficient form of governance as a select group of actors has massive representation.
We have encouraged mining pools to poll individual miners and as soon as we hear back from pools, we will be open and transparent about which pools are in favor of and which are not.
Getblok, one of our community pools, has created a Proof of Vote (PoV) voting mechanism.
A 90% approval rate is required, which is a supermajority.
The governance model we are following is modeled on the following paper. https://eprint.iacr.org/2021/577.pdf
Process
Emission and Treasury Emission are boxes created before the genesis block and associated with corresponding contracts.
This is a part of the Proof of No Pre-mine and the associated monetary policy of the network.
It is important to understand that the original emissions contract is still valid. It is simply interacting with a re-emission contract that is collecting rewards to be used to extend the original emission.
This EIP offers the following procedure for that:
Starting from block #699,393 (first block of 684th epoch), new emission rules “If Approved” would be applied on top of the rules described in the Ergo Whitepaper.
The current Block Reward 66 ERGs
The initial change would drop the mining reward per block by 12 ERGs.
Subject to approval the block reward would be 66–12= 54 ERGS
In simple terms, the initial reduction of 12 ERGs is being put into a box where it will pay miners after the initial emission period is complete.
66 Old 54 New Block Height 699,393
63 Old 51 New Block Height 720,000
60 Old 48 New Block Height 784,000
57 Old 45 New Block Height 849,600
54 Old 42 New Block Height 914,400
51 Old 39 New Block Height 979,200
48 Old 36 New Block Height 1,044,000
45 Old 33 New Block Height 1,108,800
42 Old 30 New Block Height 1,173,600
39 Old 27 New Block Height 1,238,400
36 Old 24 New Block Height 1,303,200
33 Old 21 New Block Height 1,368,000
30 Old 18 New Block Height 1,432,800
27 Old 15 New Block Height 1,497,600
24 Old 12 New Block Height 1,562,400
21 Old 9 New Block Height 1,627,000
18 Old 6 New Block Height 1,691,800
15 Old 3 New Block Height 1,821,600
12 Old 3 New Block Height 1,886,400
9 Old 3 New Block Height 1,951,200
6 Old 3 New Block Height 2,016,000
3 Old 3 New Block Height 2,016,000
0 Old 3 New Block Height 2,080,800
The Original Emission hit zero at block 2,080,800.
The proposed Re-Emission Soft Fork creates an extended period of block rewards at 3 ERG
There is an interactive graph available on ergo.watch that model the original emission and proposal.
In the future, it is possible to create a soft fork that requires storage rent to be collected into the re-emission contract to potentially smooth payment and extend the block rewards into the future.
ERG cannot be burned in the conventional manner miners are accustomed to due to storage rent. Any future burns can be directed into the re-emission contract potentially stabilizing the re-emission at 3 ERG.
The goal of this proposal is to secure the crypto-economic security of the chain long-term to create a sustainable ecosystem that incentivizes miners. Our goal is not to rob miners or have developers dictate policy.
We believe that governance in a Proof of Work system should be representative of the opinions of miners. This is a part of why the threshold for Soft Power is set at 90%. Due to the previous hard fork, the governance model changed, which shifted power to mining pools. This is not ideal, but we will try to be transparent about how to vote.
The consensus among miners and those that support our ecosystem is important.
Developers have proposed updates in the past that have been rejected.
This is a part of governance and decentralized management.
If EIP-0027 is rejected we will talk with the community and propose alternatives in the future.