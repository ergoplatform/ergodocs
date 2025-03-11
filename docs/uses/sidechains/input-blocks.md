#  Input Blocks and Ordering Blocks – Technical Details**

## Background on the Current System

  
- **Current Process:**  
  Transactions from wallets enter a common mempool. Miners include these transactions in blocks that are produced roughly every 2 minutes.
  
- **Replace-By-Fee (RBF):**  
  RBF allows users to increase transaction fees for faster inclusion or even cancel a transaction by refunding the sender’s wallet. This system can sometimes lead to issues, such as with SigmaUSD mint transactions during fee competitions.

### Limitations

  
- **Variable Confirmation Times:**  
  Due to variance in block production, some transactions might take as long as 10 minutes to confirm.
  
- **User Friction:**  
  The current system involves repeated manual steps (like multiple password prompts) that slow down the overall process.

### 2. Introducing Input Blocks and Ordering Blocks

Following ideas in PRISM [3], Parallel Proof-of-Work [4], and Tailstorm [5], Ergo introduces two kinds of blocks via a non-breaking consensus protocol update.

### Revisiting the Current Block Concept

A valid block in the current Ergo protocol is formed by semantically valid header fields and corresponding block sections (including transactions). Miners search for a nonce such that:

```
H(b) < T
```

where:

- **H(b):** is the Autolykos Proof-of-Work function applied to the block header bytes (including nonce),
- **T:** is the Proof-of-Work target, and
- **Difficulty (D):** is defined as D = 2^256 / T (with adjustments for the secp256k1 curve order).

Difficulty is readjusted to maintain an average block production time of 2 minutes.

### The Role of Superblocks

  
- **Superblocks:**  
  Used for building NiPoPoWs, a superblock (e.g., a level-1 superblock *S*) must satisfy:
  ```
  H(S) < T/2
  ```
  In general, an n-level superblock must satisfy:
  ```
  H(S) < T/2^n
  ```
  Every superblock is also a valid block under the standard PoW test.

### Transition to Input Blocks and Ordering Blocks

  
- **Ordering Blocks:**  
  These are the full blocks (with the original PoW requirements) and will continue to be produced every 2 minutes.
  
- **Input Blocks (Sub-blocks):**  
  To enable faster transaction propagation, input blocks are introduced with a lower difficulty threshold. For example, by setting:
  ```
  t = T/64
  ```
  and defining the input block condition as:
  ```
  H(ib) < t
  ```
  a miner can generate, on average, 63 input blocks alongside 1 ordering block per ordering block generation period. Unlike superblocks, input blocks are not required to pass the ordering block PoW check, though every ordering block must pass the input block check.
  
- **Blockchain Structure:**  
  The resulting blockchain may look like:
  ```
  (ordering block) - input block - input block - input block - (ordering block) - input block - input block - (ordering block) …
  ```
  This structure facilitates rapid transaction dissemination while preserving overall network security.

##. Transaction Handling and Data Structures

### Transaction Classes

  
- **First-Class Transactions:**  
  These transactions yield consistent validation results across all input blocks (approximately 99% of typical transactions) and are included solely in input blocks.
  
- **Second-Class Transactions:**  
  Dependent on variables like block timestamps or miner public keys, these transactions might validate differently between input and ordering blocks, so they are included in both.

### Merkle Trees and Digest Fields

  
- **Purpose:**  
  Miners maintain Merkle tree roots for:
  
  - All first-class transactions since the last ordering block.
  - Transactions included in the input blocks.
  
- **Implementation:**  
  These digest fields are embedded in the block header extensions to ensure consistency and efficient verification, even as input blocks are rapidly generated.

## Block Propagation Mechanisms

  
- **Announcement:**  
  When an input block is generated, its header and the identifier of its parent input block are announced.
  
- **Data Verification:**  
  Peers request an introspection message containing proofs and Merkle tree digests (similar to weak IDs in Bitcoin’s Compact Blocks) to verify transaction data efficiently.
  
- **Efficient Protocols:**  
  Cut-through propagation techniques are employed to ensure that transaction identifiers and confirmations are rapidly disseminated across the network.

## Miner Incentives and Protocol Upgrades

### Incentives

  
- **Fee Collection:**  
  Miners earn fees from first-class transactions included in input blocks.
  
- **Additional Rewards:**  
  Ordering blocks yield rewards from second-class transactions, as well as storage rent and emission rewards.

### Soft Fork Upgrade

The new rules will be implemented via a soft fork. This ensures backward compatibility—older nodes will still receive standard block transaction messages until a supermajority (90+% of the hashrate) upgrades.

## Security Considerations

  
- **Validation Checks:**  
  Every ordering block must pass the input block validation check, which prevents invalid transactions from being confirmed.
  
- **Flexible Confirmation Models:**  
  The protocol supports a “weaker” notion of confirmation for rapid user feedback while retaining full network security through ordering blocks.

## Implementation Roadmap

1. **Deployment:**  
   Introduce input blocks alongside existing ordering blocks.
2. **Miner Software Upgrades:**  
   Update mining nodes to support input block generation and propagation.
3. **Transaction and Fee Script Revisions:**  
   Adjust fee scripts (e.g., setting fee scripts to “true” as needed) and update transaction validation procedures.
4. **User Interface Enhancements:**  
   Improve wallet interfaces to streamline transaction signing.
5. **Sidechain Integration:**  
   Enable input blocks to carry sidechain commitments, further enhancing scalability and offloading processing from the main chain.

## References

  
1. [Ergoforum: A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226/5)  
2. [Weak Blocks WIP #1 #2055](https://github.com/ergoplatform/ergo/pull/2055)  
3. [A Sidechain Prototype #2107](https://github.com/ergoplatform/ergo/pull/2107/)  
4. Eyal, Ittay, et al. "Bitcoin-NG: A scalable blockchain protocol." *13th USENIX Symposium on Networked Systems Design and Implementation (NSDI 16), 2016.* [https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf)  
5. Kiffer, Lucianna, et al. "Nakamoto Consensus under Bounded Processing Capacity." *Proceedings of the 2024 ACM SIGSAC Conference on Computer and Communications Security, 2024.* [https://iacr.steepath.eu/2023/381-NakamotoConsensusunderBoundedProcessingCapacity.pdf](https://iacr.steepath.eu/2023/381-NakamotoConsensusunderBoundedProcessingCapacity.pdf)  
6. Bagaria, Vivek, et al. "Prism: Deconstructing the blockchain to approach physical limits." *Proceedings of the 2019 ACM SIGSAC Conference on Computer and Communications Security, 2019.* [https://dl.acm.org/doi/pdf/10.1145/3319535.3363213](https://dl.acm.org/doi/pdf/10.1145/3319535.3363213)  
7. Garay, Juan, Aggelos Kiayias, and Yu Shen. "Proof-of-work-based consensus in expected-constant time." *Annual International Conference on the Theory and Applications of Cryptographic Techniques, 2024.* [https://eprint.iacr.org/2023/1663.pdf](https://eprint.iacr.org/2023/1663.pdf)  
8. Keller, Patrik, et al. "Tailstorm: A secure and fair blockchain for cash transactions." *arXiv preprint arXiv:2306.12206 (2023).* [https://arxiv.org/pdf/2306.12206](https://arxiv.org/pdf/2306.12206)  
9. Garay, Juan, Aggelos Kiayias, and Nikos Leonardos. "The Bitcoin Backbone Protocol: Analysis and Applications." *Journal of the ACM 71.4 (2024): 1-49.* [https://dl.acm.org/doi/pdf/10.1145/3653445](https://dl.acm.org/doi/pdf/10.1145/3653445)

