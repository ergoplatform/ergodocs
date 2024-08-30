# Forking

Ergo's view is that disruptive hard forks should be avoided in Ergo unless absolutely critical. Ergo implements various measures to prevent hard forks, such as pushing complexity to the application layer and enabling many things to be implemented via soft-forks.

If a supermajority (90%+) of the network accepts a new feature, it is activated; however, old nodes that do not upgrade continue to operate normally and skip over this feature validation.

- **Velvet-Fork**: Only requires a minority of nodes to upgrade. Introduced by the NiPoPoW paper, the key idea is that you can use the scheme even if only some blocks in the chain include the interlink structure and allows for "gradual deployment" without harming the miners that haven't upgraded to the new rules. In this way, it acts similar to a soft fork in that clients that upgrade to new rules are still compatible with those that don't.
- **Soft-fork:** Requires some nodes to upgrade. The recent re-emission Soft-Fork EIP37 was possible as it's enforced on miner nodes only via protocol rules. These can be approved with 90% support from miners.
- **Hard-Fork:** Requires all nodes to upgrade.

For more information, refer to the [Ergo Improvement Proposals (EIPs)](https://github.com/ergoplatform/eips).

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


## Velvet Forking

Velvet forking is a novel approach introduced in the paper ["A Wild Velvet Fork Appears! Inclusive Blockchain Protocol Changes in Practice"](http://diyhpl.us/~bryan/papers2/bitcoin/A%20wild%20velvet%20fork%20appears:%20Inclusive%20blockchain%20protocol%20changes%20in%20practice%20-%202018.pdf) by Zamyatin et al. It allows for introducing protocol changes in a backward-compatible and inclusive manner. The key idea is to render modifications to the protocol backward-compatible, enabling a gradual deployment without harming miners who have not upgraded to the new rules.

Velvet forks are a special form of protocol update where the new set of reducing protocol rules P' is conditionally applied only when the considered elements, such as blocks or transactions, are valid under the new rules. If not, the new rules are ignored, and the previous protocol rules P are relied upon to determine validity. Since the new rules in P' are reducing, velvet protocol changes never incur a permanent protocol fork, as any element considered valid under P' is also considered valid under P.

The key advantages of velvet forks are:

1. **Inclusive Deployment**: They do not require support from a majority of participants and can potentially avoid rule disagreement forks altogether. Legacy nodes remain unaware of the changes introduced by the velvet fork.

2. **Backward Compatibility**: Valid blocks adhering to the new rules are also valid blocks under the old rules, ensuring compatibility with non-upgraded nodes.

3. **Gradual Adoption**: Velvet forks leverage the consensus mechanism of the existing protocol P to bootstrap their own consensus rules P', allowing for a gradual adoption of the new rules.

While velvet forks present a promising approach for introducing protocol changes, they may also introduce new potential attacks and threats, as well as impact the game-theoretic incentives of the underlying blockchain. Further research is needed to understand the security implications of velvet forks and their potential applications in various blockchain protocols.

Ergo's design allows for the implementation of velvet forks, enabling the introduction of new features and protocol changes in a backward-compatible and inclusive manner. This capability is particularly useful for incorporating auxiliary protocols and data from miners, as well as enabling the gradual deployment of scaling solutions and other improvements without disrupting the network or requiring a hard fork.