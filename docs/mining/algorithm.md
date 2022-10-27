
There is a detailed three part series on the Ergo blog; [Ergo and the Autolykos Consensus Mechanism](https://ergoplatform.org/en/blog/Ergo-and-the-Autolykos-Consensus-Mechanism-Part-I/)


**Autolykos V2** has the following modifications

- *non-outsourceable puzzles* were disabled. It turns out (based on more than one year of non-outsourceable PoW experience) that non-outsourceable PoW is not an attractive option for small miners.
- Now, the algorithm is trying to bind an efficient solving procedure with a single table of ~2 GB (initially), which significantly reduces memory optimisations possibilities
- Table size (memory requirements of a solving algorithm) grows with time
- The table depends solely on the block height, so there is no penalisation for recalculating block candidates for the same height

**Basic Ideas:**

- Like Autolykos-1, based on the k-sum problem, a miner needs to find `k (k=32)` out of `N (2^n = 2^26)` elements and the hash of their sum must be less than the target value (inverse of the difficulty)
- k indexes are pseudorandom values derived from block candidate and nonce
- N elements are derived from block height and constants, unlike Autolykos v.1, so miners can recalculate block candidates quickly now (so only indexes are depending on them)
- Indexes calculation also involving the same table (which elements are last 31 bytes of `H(i | | h | | M )`, where i is in [0, N), `h` is block height, M is padding to slow down hash calculation (8kb of constant data).

So algorithm tries to make mining efficient for ones that store the table, which is `2^26 * 31 = 2,080,374,784` bytes initially (about 2GB). Thus Autolykos is now is friendly to all the GPUs.

Also, table size (N value) is growing with time as follows. Until block `614,400`, `N = 2^{26} = 67,108,864 elements (31 bytes each)`. From this block, and until block `4,198,400`, every `51,200 blocks` `N` is increased by 5 percent. Since block `4,198,400`, value of `N` is fixed and equals to `2,143,944,600`. Test vectors for `N` values are provided in the paper.

