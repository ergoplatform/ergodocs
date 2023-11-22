---
tags:
  - EIP
---
# EIP27: Emission Retargeting Soft-Fork

## Ergo Tokenomics and Emission
As a Proof of Work blockchain, Ergo has a defined emission schedule for the release of ERG tokens. When Ergo launched in 2019, there was no ICO (initial coin offering), no pre-mine and no pre-allocation of tokens to any founders or venture capitalists. Once the mainnet was activated, Ergo’s emission schedule was set to be completed within eight years with a strict supply of 97,739,925 ERG. During the first two and a half (2.5) years, the emission schedule sent a small portion of each block to the Ergo Foundation Treasury - for the purposes of funding promotion and development on Ergo. After two and a half years, the Ergo Foundation ceased to receive any rewards from the mining protocol and will have received 4.43% of the total ERG supply to fund that entity’s initiatives.

## The Original Emission Schedule
Ergo currently mines blocks every two minutes. For the first two years, each block was set to release 75 ERG into circulation. At the end of the 2nd year, the emission rate was set to drop by 3 ERG/block with a schedule that would see block rewards further reduced by 3 ERG every three months. After eight years, the total supply of ERG would have been completely mined and the mining protocol would be reliant on transaction fees and Storage Rent to reward miners.

## EIP27 and the Adjustment of Ergo’s Emission Schedule
Recently, the Ergo Foundation undertook the initiative to ensure the long-term sustainability of the mining protocol by proposing an amendment to the emission schedule. As the blockchain is still in the early stages of focusing on promotion and development, there was a concern that the ecosystem may need more time before the end of the eight-year emission schedule. If there are not enough dApps and users in the ecosystem at the end of the original emission schedule, there may not be enough transactions to incentivize miners to maintain the network.

Ergo’s co-founder, Alex Chepurnoy, proposed a solution to this possible scenario. The proposal, EIP27, would see Ergo emissions extended by approximately 17.38 years, thereby offering the time to develop the necessary crypto-economic security for the blockchain. The plan alters the amount of the block rewards so that a portion of the supply can be put into a remission contract that will release block rewards until approximately 2045.

On Ergo, miners enjoy the ability to suggest and vote on proposed changes to the network. With EIP27, the proposal required a 90% pass vote in order to be scheduled for implementation. The mining community voted over 90% in favor of this proposal and after successful testnet implementation, the new emission schedule is slated for deployment with block #777217.

Chepurnoy provided the following breakdown of the remission in a recent EIP27 update on an Ergo Forum post:

> “If block reward is not less than 15 ERG, send 12 ERG from it to the remission contract".
> "Otherwise, block reward R is less than 15 ERG, send R - 3 ERG from it to the remission contract.”

These new emission rules will be integrated with the original emission schedule of the Whitepaper. Currently, block rewards are reduced every three months by 3 ERG/block - this will still be the case after EIP27 is activated. However, once implemented (approximately June 21), the block size will be 51 ERG/block. Based on the original emission schedule, the next reduction in rewards will take place around July 2, 2022. The block rewards will be reduced by 3 ERG, therefore the total reward for each block will be 48 ERG. Three months from that date, the block rewards will be 45 ERG/block, and so on. This reduction schedule will continue until block rewards are 3 ERG/block. Block rewards will remain steady at 3 ERG/block until the remission contract has been depleted.

EIP27 is a commitment to ensuring the long-term and sustained growth of Ergo. Since changes in the emission schedule can not be implemented without consensus within the mining community (90% pass is required), EIP27 represents the collaborative spirit of the Ergo community to collectively build a better blockchain for everyone. For more details on the implementation of EIP27, please see Chepurnoy's Ergo Forum post.

