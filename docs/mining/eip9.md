---
tags:
  - EIP-9
  - Hard Fork
  - Protocol
  - Activation
  - Governance
---

# EIP-0009 Hard-fork Activation Protocol

- **Author:** aslesarenko 
- **Status:** Proposed
- **Created:** 04-Jun-2020
- **License:** CC0
- **Forking:** Hard-fork needed 



### Description 

This EIP specifies a hard-fork activation protocol and the necessary implementation details. For the sake of presentation, the description is formulated in terms of switching from Ergo Protocol v1 (v3.x releases) to Ergo Protocol v2 (v4.x releases), hereinafter called EP1 to EP2. However, the protocol and activation process are general enough to be repeated in the future if the need arises.

### Background And Motivation

Ergo is designed to support consensus protocol evolution via soft-fork. Soft-forkability is already implemented in EP1. However, some protocol changes require a hard-fork, which is a significant event in the network lifecycle. Therefore, it is especially important to have a clear, transparent, predictable, safe, and well-understood hard-fork activation process. The following sections describe the process using a switch from EP1 to EP2 as an example.

### Changes in EP2

#### Change from AOTC to JITC

JIT costing (JITC pronounced "jitsy") can only be activated via hard-fork. It is not possible to ensure that JITC always produces the same costs as AOTC by changing CostTable parameters. This is because JITC accurately accumulates the actual operations' cost, whereas AOTC approximates both data sizes and speculates on potential costs in case of branching logic. Please see detailed description of the changes in related [EIP8](https://github.com/ergoplatform/eips/pull/11).

### Implementation of the Hard-Fork on Ergo network

The activation is performed in two phases. The goal of the first phase is to collect votes, select the starting block for a hard-fork, and perform a safe switch. The second phase is dedicated to code cleanup and optimizations enabled by the hard-fork. This is optional, and some verifiers may opt to not do this, however, this is part of the whole transition.

#### Phase 1: Release v4.0.0

This phase consists of the following steps, which are described in subsections:

1. Voting until consensus on `HFVoted` status is achieved and `HFBlock` is defined, waiting for `HFBlock` while following EP1.
2. Switching to EP2 starting from `HFBlock`.

##### Selection of the hard-forking block

In this first HF release, both EP1 and EP2 code will be available. EP1 will be operational until HF voting is finished and HF switch is performed. The full nodes vote for HF by running v4.0.0 release, which behaves as v3.x, but implies voting. Every node can check the voting status using Block Extension section. Once the necessary voting threshold is achieved (`HFVoted` status is reached) in an epoch, we know enough mining nodes upgraded and are running v4.0.0 release. We, therefore, can define the first block of the next epoch as the first hard-forked block. We will refer to it as `HFBlock`.

##### Example: AOTC to JITC switch

It is important to ensure that JITC is functionally equivalent to AOTC for all the blocks in `[1 .. HFBlock-1]` range. Here functional equivalence means that for each script, both AOTC and JITC should evaluate to the same result. This property is necessary to remove the old v3.x ErgoTree interpreter and perform the validation of historical blocks using the JITC interpreter alone. Since the history is immutable, it is enough to check the equivalence by running both v3.x interpreter and JITC on all the blocks up until `HFBlock`.

Thus, all v4.0.0 nodes will run JITC interpreter in parallel with AOTC and compare the results. If at any time the script results are different, then AOTC result is used in the consensus and the problematic transaction is logged. In addition, the voting is blocked by the node. If AOTC validates the problematic transaction, it still should be added to the blockchain to support the current consensus among v4.0.0 and older nodes. This will lead to all v4.0.0 nodes stop voting, thus preventing the HF switch.

If voting is blocked (which is an exceptional case), then a fix in JITC is required, so a new v4.0.1 release should be created, and the HF process should start from scratch.

If voting is not blocked and `HFVoted` network status is achieved, then the majority of nodes are running the latest v4.x version. In this case, the validation of the first block after `HFVoted` (let's call it `HFVotedBlock`) requires both AOTC and JITC to have strictly the same result. Transactions that invalidate this property should be rejected by all v4.0.0 nodes (which are now the majority). This will ensure that in the block range `[HFVotedBlock .. HFBlock]`, AOTC and JITC are functionally equivalent.

#### Switching EP1 to EP2

When voting is not blocked, `HFVoted` status is achieved, and `HFBlock` is selected, then all the v4.0.0 nodes need to switch from EP1 to EP2 starting from `HFBlock`. This switch is implemented as `if` statements in the block validation code of the v4.0.0 release.

Thus, starting from `HFBlock`, EP2 is used for all new block validation, and EP1 is turned off (the code is not executed), and the network is operating according to a new consensus (Ergo Protocol v2).

##### Example: AOTC to JITC switch

Now, because the v2 consensus is based on JITC, there is an opportunity to fix bugs and add new features to ErgoTree, which are all enabled starting from `HFBlock`. NOTE, both fixes and new features should keep backward compatibility of applications in mind.

The fixes in JITC for v2 protocol, however, may be not compatible with v1 protocol. This will require JITC interpreter to have an internal branching logic having both versions of the protocol. Thus, JITC v4.0.0 will process historical blocks according to Ergo Protocol v1 and starting from `HFBlock` as Ergo Protocol v2. This will ensure that each v4.x release will successfully validate all historical blocks.

#### Phase 2: Release v4.0.x (removing AOTC)

This version can be released after `HFBlock`
