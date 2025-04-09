---
tags:
  - Autolykos
  - Mining
  - Algorithm
  - Proof of Work
---

# Autolykos


Ergo mining is based on **Autolykos**, a fairly launched efficient [ASIC-resistant](asic.md) Proof of Work algorithm.

## Overview

Autolykos, in its first version, was designed with inherent pool-resistance through the use of non-outsourceable puzzles. The transition to Autolykos v2 was marked by [EIP-0009: Hard-fork Activation protocol](eip9.md) ***'The Hardening Hard-Fork'*** on block `417,792`, which facilitated the formation of mining pools by removing the non-outsourceable puzzles.

In addition to EIP-0009, several other proposals have been implemented which impact the autolykos algorithm in regards to the emission and difficulty adjustment:

- [**EIP27: Emission Retargeting Soft-Fork**](standards/eip27.md) was a significant milestone, passed with overwhelming community support, that extended emission by 4,566,336 blocks (~17.38 years). This change was activated on block `777217`. For more information see the [emission](emission.md) section.
- [**EIP37: Tweaking Difficulty Adjustment Algorithm**](standards/eip37.md) made the difficulty adjustment mechanism more responsive by considering a shorter and more recent history of blocks. EIP37 didn't replace Autolykos but refined it, making it more resilient against sudden hash rate changes and adversarial disruptions. For more information see the [difficulty adjustment](difficulty.md) section.

### Pool Resistance (Autolykos v1)

Autolykos V1 was initially designed to resist pooling. However, it was observed that large players could bypass this resistance using smart contracts. This issue was discussed in the paper ["Bypassing Non-Outsourceable Proof-of-Work Schemes Using Collateralized Smart Contracts"](https://ia.cr/2020/044) presented by Alex Chepurnoy at the WTSC workshop associated with Financial Cryptography and Data Security 2020 in Malaysia.

### Autolykos V2

**Autolykos V2** introduced the following changes:

- The *non-outsourceable puzzles* were removed.
- The algorithm was optimized to bind an efficient solving procedure with a single table of ~2 GB (initially), significantly reducing the scope for memory optimization.
- The table size, which determines the memory requirements of the solving algorithm, increases over time.
- The table is solely dependent on the block height, eliminating any penalties for recalculating block candidates for the same height.

### Key Concepts (Autolykos v2)

- Autolykos, both v1 and v2, is based on the **k-sum** problem. A miner is required to find **k (k=32)** out of **N (2<sup>n</sup> = 2<sup>26</sup> initially)** elements, such that the hash of their sum is less than the target value (inverse of the difficulty).
- The *indexes* (**k**) are pseudorandom values derived from the block candidate and nonce.
- The *elements* (**N**) are derived from the block height and constants. Unlike Autolykos v1, miners can now recalculate block candidates quickly as only the indexes depend on them.
- The calculation of indexes also involves the same table
    - (where elements are the last 31 bytes of **H(i | | h | | M )**, with **i** in the range [**0, N**),
        - **h** representing the block height,
        - and **M** serving as padding to slow down hash calculation (8kb of constant data).

The algorithm is designed to be efficient for miners who store the table, which initially requires **2<sup>26</sup> * 31 = 2,080,374,784** bytes (about 2GB).

### Table Size Evolution

The table size (**N** value) evolves over time as follows:

- Until block `614,400`, **N** = 2<sup>26</sup> = 67,108,864 elements (31 bytes each).
- From block `614,401` until block `4,198,400`, **N** increases by approximately 5% every 51,200 blocks (specifically, `n` increases by 1 every 102,400 blocks, so N doubles every 102,400 blocks).
- At block `4,198,400`, the value of **N** is fixed at `2,143,944,600`.

*(Note: Test vectors for N values are provided in the [Autolykos paper](https://www.docdroid.net/mcoitvK/ergopow-pdf)).*

::cards::

[
  {
    "title": "Start Mining",
    "url": "setup/join.md",
    "content": "Getting setup with a mining pool."
  },
  {
    "title": "Algorithm",
    "url": "algo-technical.md",
    "content": "Dive into the Autolykos Algorithm technical details."
  },
  {
    "title": "Governance",
    "url": "governance.md",
    "content": "PoW To The People"
  },
  {
    "title": "Storage Rent",
    "url": "rent.md",
    "content": "On-chain garbage collection that reduces the problem of blockchain bloat"
  },
  {
    "title": "Difficulty Adjustment",
    "url": "difficulty.md",
    "content": "See how the mining difficulty is calculated."

  },
  {
    "title": "Emission",
    "url": "emission.md",
    "content": "The Ergo emission schedule"
  },

]

::/cards::



/// details | FAQ
     {type: note, open: true}
For information on how miners will be supported after emission ends see [this page](revenue.md)
///
