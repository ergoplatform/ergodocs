## Input Blocks and Ordering Blocks – Technical Details

### Background on the Legacy System

* **Previous Process:**
  Transactions from wallets enter a common mempool. Miners select and include them in blocks produced approximately every 2 minutes. These blocks contain full proof-of-work (PoW), enforce consensus, and settle transactions.

* **Replace-By-Fee (RBF):**
  RBF allows a user to rebroadcast a transaction with a higher fee to increase inclusion chances or refund the sender if it fails. Under high network congestion, RBF can cause delays or confusion, particularly for dApps like SigmaUSD which rely on timely confirmations.

### Limitations

* **Unpredictable Confirmation Times:**
  Due to natural PoW variance, a transaction might take anywhere from 2 to 10 minutes to confirm, even under normal conditions.

* **Poor UX in Wallets and dApps:**
  Users face friction from waiting, multiple signing attempts, and retries, which degrades trust and usability.

---

### Introducing Input Blocks and Ordering Blocks

Following ideas in PRISM, Bitcoin-NG, Tailstorm, and Parallel Proof-of-Work, Ergo introduces a dual-block architecture via a soft fork that maintains backward compatibility.

### Redefining the Block Structure

In traditional Ergo:

```
H(b) < T
```

* `H(b)` is the hash of the block header under Autolykos
* `T` is the target value for PoW
* Difficulty `D = 2^256 / T`, adjusted to maintain \~2-minute block intervals

This rule continues to define **ordering blocks**, but Ergo now introduces **input blocks** with a lower difficulty threshold:

```
H(ib) < t   where   t = T / 64
```

This allows miners to produce approximately one input block every second, on average, for each ordering block cycle.

---

### The Role of Superblocks

While input blocks and ordering blocks focus on real-time transaction propagation and consensus anchoring, **superblocks** enable efficient long-range proofs and light client support via NiPoPoWs.

A level-`n` superblock must satisfy:

```
H(S) < T / 2^n
```

* Every superblock is a valid ordering block
* Higher-level superblocks are rarer and used in succinct chain proofs
* Useful for mobile wallets and sidechains needing trust-minimized verification

---

### Input Blocks and Their Mechanics

* **Ordering Blocks:**
  Full PoW blocks that anchor consensus, produced every \~2 minutes. They finalize the inclusion of input blocks and distribute rewards.

* **Input Blocks (Sub-blocks):**
  Low-difficulty blocks generated approximately every second, used for fast transaction propagation. They are not consensus anchors but allow for near-instant detection of transaction inclusion.

```
ordering block → input block → input block → input block → ordering block → input block → ...
```

* Each ordering block is valid as an input block, but not vice versa

---

### Transaction Classes

* **First-Class Transactions:**
  Deterministic and miner-independent, these transactions yield consistent validation across all miners and can safely be included in input blocks only.

* **Second-Class Transactions:**
  May rely on miner-specific data (timestamps, pubkeys, etc.) and are included in both input and ordering blocks to ensure consistency.

---

### Merkle Trees and Digest Extensions

Miners maintain Merkle roots for:

* All first-class transactions since the last ordering block
* Transactions in each individual input block

These roots are embedded in block header extensions to enable efficient proof construction and light client validation.

---

### Block Propagation Protocol

* **Header Announcements:**
  Each input block header is announced immediately, along with its parent input block ID.

* **Verification:**
  Peers request introspection messages (similar to Compact Blocks in Bitcoin) to verify Merkle digests without downloading full block data.

* **Cut-through Propagation:**
  Redundant data across input blocks is eliminated to optimize bandwidth and speed.

---

### Incentives and Rewards

* **Input Blocks:**
  Miners collect transaction fees from first-class transactions included in input blocks.

* **Ordering Blocks:**
  Miners earn full block rewards, second-class transaction fees, and storage rent/emission rewards.

---

### Upgrade Process

* **Soft Fork Activation:**
  Backward-compatible upgrade. Legacy nodes continue to process ordering blocks. Input blocks are only utilized after 90% of hashpower adopts the upgrade.

* **Steps:**

  1. Introduce input blocks alongside ordering blocks
  2. Upgrade mining software
  3. Adjust transaction validation logic and fee scripts
  4. Update dApp interfaces for faster feedback
  5. Enable sidechain commitments within input blocks

---

### Security Considerations

* **Input Block Validation:**
  All ordering blocks must validate preceding input blocks. Invalid transactions are not finalized.

* **Dual Confirmation Model:**
  Input blocks offer fast, provisional feedback. Final settlement still relies on inclusion in an ordering block.

---

### TLDR

Input blocks provide rapid, low-cost transaction propagation (\~1s), greatly improving user feedback without altering the security guarantees of Ergo’s existing PoW system. Ordering blocks retain finality and economic incentives, while superblocks support long-range verification. This architecture balances performance, security, and decentralization.
