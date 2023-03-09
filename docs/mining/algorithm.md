# Autolykos Algorithm

This page provides a brief Overview of the [Autolykos](https://www.docdroid.net/mcoitvK/ergopow-pdf) algorithm, followed by an in-depth, technical line-by-line breakdown.



## Overview

- Autolykos v1 originally had pool-resistance built-in through the use of non-outsourceable puzzles.
- **The Hardening Hard-Fork** on block `417,792` marked the launch of Autolykos v2, enabling mining pools. See this [paper](https://ia.cr/2020/044). 
- [**EIP27:**](eip27.md) was passed with overwhelming community support, extending emission by 4,566,336 blocks (~17.38 years). This was activated on block `777217`


### Autolykos V2

Autolykos V1 was originally pool resistant.  However, it became apparent that pool resistance was infeasible due to large players having an advantage with smart contracts. ["Bypassing Non-Outsourceable Proof-of-Work Schemes Using Collateralized Smart Contracts"](https://ia.cr/2020/044) was presented by Alex Chepurnoy at the WTSC workshop associated with Financial Cryptography and Data Security 2020 in Malaysia.


**Autolykos V2** has the following modifications

- *non-outsourceable puzzles* were disabled. 
- The algorithm tries to bind an efficient solving procedure with a single table of ~2 GB (initially), which significantly reduces memory optimisation possibilities.
- The table size (memory requirements of a solving algorithm) grows with time.
- The table depends solely on the block height, so there is no penalisation for recalculating block candidates for the same height.

**Basic Ideas:**

- Like Autolykos-1, based on the **k-sum** problem, a miner needs to find **k (k=32)** out of **N (2<sup>n</sup> = 2<sup>26</sup>)** elements, and the hash of their sum must be less than the target value (inverse of the difficulty)
- **k** *indexes* are pseudorandom values derived from block candidate and nonce
- **N** *elements* are derived from block height and constants, unlike Autolykos v.1, so miners can recalculate block candidates quickly now (as only indexes depend on them)
- Indexes calculation also involves the same table 
    - (which elements are the last 31 bytes of **H(i | | h | | M )**, where **i** is in [**0, N**), 
        - **h** is block height, 
        - **M** is padding to slow down hash calculation (8kb of constant data).

The algorithm attempts to make mining efficient for ones that store the table, which is **2<sup>26</sup> * 31 = 2,080,374,784** bytes initially (about 2GB). 

The table size (**N** value) grows with time as follows. 

- Until block `614,400`, **N** = 2^{26} = 67,108,864 elements (31 bytes each). 
    - From this block, and until block `4,198,400`, every 51,200 blocks **N** is increased by 5 percent. 
- At block `4,198,400`, the value of **N** is fixed and equals to `2,143,944,600`. 

Test vectors for **N** values are provided in the paper.


## Line-by-line



Autolykos is based on the [Equihash paper and the birthday problem](https://www.researchgate.net/publication/316904748_Equihash_Asymmetric_Proof-of-Work_Based_on_the_Generalized_Birthday_Problem). 

To summarise, the miner is tasked to find **k (=32)** out of **N** elements, such that the hash of the sum of the elements is less than the target. 

**Autolykos Block Mining Pseudocode**

![Screenshot 2022-06-01 at 23.41.49.png](https://storage.googleapis.com/ergo-cms-media/Screenshot_2022_06_01_at_23_41_49_b2cdf73a2a/Screenshot_2022_06_01_at_23_41_49_b2cdf73a2a.png)

Before discussing the block mining procedure, the algorithm first requires 

- a very large cyclic group **G** 
- of prime order **q** 
- with fixed generator **g** 
- and identity element **e**. 

This prime group returns integers in **Z/qZ** during the *Blake2b256*-based hashing function.

_Example cyclic group with generator z, identity element 1, order 6_
![unnamed (1).png](https://storage.googleapis.com/ergo-cms-media/unnamed_1_44d138eaaf/unnamed_1_44d138eaaf.png)

We will not focus extensively on the cyclic group as it only covers a small segment of the PoW scheme. Now, let’s tackle Autolykos Block mining line by line.

### Line 1 – Input h and m

> Input: upcoming block header hash m, block height h


The PoW begins with two inputs: 

- the block height **h** 
- the upcoming block header hash **m**. 

The block header hash is a **hash of the block header components**, (i,e previous block header hash, Merkle root, nonce, etc.)
 
### Line 2 – Calculate list R
 
Firstly, it is important to notice the **H()** notation in line 2. This notation calls the hashing function *Algorithm 3*. Algorithm 3 is a hash function based on *Blake2b256* and is used throughout Autolykos. 

Algorithm 3 states that if the Blake hash of the inputs is below 

> 2<sup>256</sup> (= 16<sup>64</sup> = 0xFFFFFFFFFFFF86633A9E8F1256D61ED5325EBF2A4B4366BA0000000000000000)

then **hash.mod(q)** is returned. 

If not, Algorithm 3 repeats until it reaches a numeric hash within the valid range. For reference, note that **q** is the prime order of group **G**, *Blake2b256* hash outputs are 256 bits, 64 digits long, and Algorithm 3 will always return a numeric hash in **Z/qZ**.
 
***Blake2b256* Based Hash function**
![Screenshot 2022-06-02 at 03.17.18.png](https://storage.googleapis.com/ergo-cms-media/Screenshot_2022_06_02_at_03_17_18_ce898813d8/Screenshot_2022_06_02_at_03_17_18_ce898813d8.png)
 
In line 2, the focus is the creation of **list R**. **List R** contains **r** values which are 31-byte numeric hashes created from integers in [0, N). **r** values are generated by **takeright(31,H(j||h||M))**. 

The variables are as follows:

- **j**, integer in [0, N)
- **h**, block height
- **M**, 8kb of constant data - padding to slow down the hash calculation
 
The section **takeRight(31,H(…))** means that given **H(…)**, a 32-byte *Blake2b256* output, the 31 bytes on the right (i.e. in little-endian (whereas other hash algorithms are bit endian)) are returned. 

In other words, the most significant byte, the byte farthest to the left, is dropped. As a result, each **r** value is the 31 least significant bytes derived from the 32-byte **H(j||h||M))** output. 

For example, 
- if **j** = 1, **r1 = takeRight(31,H(1||h||M))**.
- **List R** consists of **N** elements and can be generated for each block by incrementing **j** by 1 **N-1** times.  

Since **H(…)** returns **hash.mod(q)**, we can state that **list R** consists of **r0, 1, 2, 3 … N-1_ and _list R ⊂ Z/qZ**. 

As stated in the [Autolykos v2 whitepaper](https://www.docdroid.net/mcoitvK/ergopow-pdf) 

> **N** elements are derived from block height and constants, unlike Autolykos v1, so miners can recalculate block candidates easily now (only indexes are depending on them).

**In other words,**

- **j** is always in [0,N),
- **N** is determined by **h**, 
- **M** is always constant, and **h** changes every block, 
- the only variable a miner needs to compute **list R** is **h**. (**List R** is stored in RAM)
 
> In Autolykos, **N** = 2<sup>26</sup> (67,108,864 integers) is used in implementation for every block before 614400. Thus, the memory requirement for blocks before block 614400 is (226 * 31 bytes =) 2.08GB. 

**N** first increased on block 614400. Post block 614400, every 51200 blocks, **N** increases by 5%. In other words, the memory requirement of an Ergo miner increases by 5% every ~71 days. 

[On block 4198400, the value of _N_ becomes constant and equal to 2,143,944,600](https://www.ergoforum.org/t/autolykos-v-2-details/480).

The last two values listed in the table should be 2,143,944,600 and not 2,147,387,550. After block 4198400, the storage requirement of **list R** will be (31 bytes * 2,143,944,600) = 66.46GB.

**N elements based on block height**

![unnamed (3).png](https://storage.googleapis.com/ergo-cms-media/unnamed_3_978ffb3d8a/unnamed_3_978ffb3d8a.png)

**N elements, Ethash vs. Autolykos**
 
Autolykos is like Ethash in the sense that block height determines **N** elements to be stored in RAM. 

- With Autolykos, block height determines **N** 31-byte numeric hashes to be stored. 
- With Ethash, block height determines **N** 128B DAG pages to be stored. 

You might ask yourself if an Ergo block occurs every 2 minutes, how can Ergo miners generate a 2GB+ dataset so quickly? Ethereum miners only regenerate the DAG every 100 hours because it takes so long… 

For an Ergo miner, the burden to compute **list R** is **N** instances of Algorithm 3; remember, each **r value** is computed as **takeRight(31,H(j||h||M))**. 

However, a GPU can do this very quickly as GPUs generally have 32-wide or 64-wide multiprocessors (meaning that 32 or 64 Algorithm 3 instances can be done simultaneously). 

For example, a 32-wide GPU such as the RTX570 can fill **list R** in just a few seconds.


### Lines 3, 4 – begin while loop and guessing

```bash
Calculate r
while true do
```
 
After calculating **list R**, the miner creates a nonce guess and enters a loop to test if the nonce ultimately creates an output below the given target value.
 
### Lines 5, 6 – seed for generating indexes
 
Line 5, **i = takeRight(8, H(m||nonce)) mod N**, produces an integer in [0,N). Algorithm 3 is utilised but with **m** and the **nonce** as inputs. Once the hash **H(m||nonce)** is returned, the eight least significant bytes are kept and passed through **mod N**. As a side note, the highest possible integer value with 8 bytes is 2<sup>64</sup> – 1, and assuming **N** = 2<sup>26</sup>_, an 8-byte hash **mod N** will result in the first few digits being zero. The number of zeros in **i** decreases as **N** grows.
 
Line 6 produces **e**, a seed for index generating. Algorithm 3 is called with inputs **i** (generated in line 5), **h**, and **M**. Then, the most significant byte of the numeric hash is dropped, and the remaining 31 bytes are kept as value **e**. It should also be noted that value **e** can be retrieved from **list R** instead of being computed since **e** is an **r** value.
 
### Line 7 – index generator
 
Element index **J** is created using Algorithm 6 with inputs **e**, **m**,_ and **nonce**. Function **genIndexes** is a pseudorandom one-way that returns a list of **k** (=32) numbers in [0,N).
 
**genIndexes function**

![unnamed (6).png](https://storage.googleapis.com/ergo-cms-media/unnamed_6_987fcaba80/unnamed_6_987fcaba80.png)
 
A couple of extra steps are not shown in the pseudocode, such as a byteswap. The creation and application of genIndexes can be explained via the following example:


**GenIndexes(_e||m||nonce_)...**

- **hash** = *Blake2b256*(e||m||nonce) = [0xF963BAA1C0E8BF86, 0x317C0AFBA91C1F23, 0x56EC115FD3E46D89, 0x9817644ECA58EBFB]_
- **hash64to32** = [0xC0E8BF86, 0xF963BAA1, 0xA91C1F23, 0x317C0AFB, 0xD3E46D89 0x56EC115F, 0xCA58EBFB, 0x9817644E]_
- **extendedhash** (i.e., byteswap and concatenate 4 bytes by repeating first 4 bytes) = [0x86BFE8C0, 0xA1BA63F9, 0x231F1CA9, 0xFB0A7C31, 0x896DE4D3, 0x5F11EC56, 0xFBEB58CA, 0x4E641798, 0x86BFE8C0]_


The following python code shows slicing the extended hash, returning k indexes. In this example we are assuming _h_ < 614,400, thus N = 2<sup>26</sup> (67,108,864).
 
**Slicing and mod N[1]**

```python
for i in range(8):
	idxs[i << 2] = r[i] % np.uint32(ItemCount)
	idxs[(i << 2) + 1] = ((r[i] << np.uint32(8)) | (r[i + 1] >> np.uint32(24))) % np.uint32(ItemCount)
	idxs[(i << 2) + 2] = ((r[i] << np.uint32(16)) | (r[i + 1] >> np.uint32(16))) % np.uint32(ItemCount)
	idxs[(i << 2) + 3] = ((r[i] << np.uint32(24)) | (r[i + 1] >> np.uint32(8))) % np.uint32(ItemCount)
```

The main takeaway is that slicing returns **k** indexes which are pseudorandom values derived from the seed, i.e., **e**, **m**, and **nonce**.
 
return [0x2BFE8C0, 0x3E8C0A1, 0xC0A1BA, 0xA1BA63, 0x1BA63F9, 0x263F923, 0x3F9231F, 0x1231F1C, 0x31F1CA9, 0x31CA9FB, 0xA9FB0A, 0x1FB0A7C, 0x30A7C31, 0x27C3189, 0x31896D, 0x1896DE4, 0x16DE4D3, 0x1E4D35F, 0xD35F11, 0x35F11EC, 0x311EC56, 0x1EC56FB,  0x56FBEB, 0x2FBEB58, 0x3EB58CA, 0x358CA4E, 0xCA4E64, 0x24E6417, 0x2641798, 0x179886, 0x39886BF,  0x86BFE8]
 
This index can be translated to values in base ten as it refers to numbers in [0, N). For instance, 0x2BFE8C0 = 46131392, 0x3E8C0A1 = 65585313, 0xC0A1BA = 12624314, and so on. The miner uses these indexes to retrieve **k r** values.
 
The genIndexes function prevents optimisations as it is extremely difficult, basically impossible, to find a seed such that genIndexes(seed) returns desired indexes.
 
### Line 8 – sum of r elements given k
 
Using the index generated in _line 7_, the miner retrieves the corresponding **k (=32) r** values from **list R** and sums these values. This might sound confusing but let’s break it down.
 
Continuing the example above, the miner stores the following indexes:

```json
{0 | 46,131,392},
{1 | 65,585,313},
{2 | 12,624,314},
{3 | 10,599,011},
…
{31 | 8,830,952}
```

Given the indexes above, the miner retrieves the following r values from **list R** stored in memory.
```json
{0 | 46,131,392} → _dropMsb(H(46,131,392||h||M))_
{1 | 65,585,313} → _dropMsb(H(65,585,313||h||M))_
{2 | 12,624,314} → _dropMsb(H(12,624,314||h||M))_
{3 | 10,599,011} → _dropMsb(H(10,599,011||h||M))_
…
{31 | 8,830,952} → _dropMsb(H(8,830,952||h||M))_
```

Note that **Takeright(31)** operated on a 32-byte hash can also be written as **dropMsb** (drop most significant byte).
 
Since the miner already stores **list R** in RAM, the miner does not need to compute **k (= 32)** *Blake2b256* functions and instead looks up the values. 

This is a key feature of *ASIC resistance*. An ASIC with limited memory needs to compute 32 *Blake2b256* iterations to get the values that could have been looked up in memory, and fetching from memory takes much less time. 

An ASIC with limited memory would require 32 *Blake2b256* instances physically on the die to achieve one hash per cycle, which would require more area and higher costs. It's simple to prove that storing **list R** in memory is well worth the trade-off. 

Assume the following, a GPU has a hash rate of **G** = 100MH/s, **N** = 2<sup>26</sup>, **k** = 32, block interval **t** = 120 seconds, and elements are looked up every four hashes. We can assume that elements are looked up every four hashes because, for each nonce guess, multiple elements such as **i**, **J**, and **H(f)** require Algorithm 3, i.e. blake2b hash, instances. 

We can estimate that each **r** value will be used, on average, **(G * k * t)/(N*4)** = 1430.51 times.
 
Once the 32 **r** values are looked up, they are summed.
 
### Line 9, 10, 11, 12 – check if the hash of sum is below target
 
The sum of the 32 **r** values is hashed using Algorithm 3, and if the output is below target **b**, the PoW is successful, **m** and **nonce** are returned to network nodes, and the miner is rewarded in ERG. If the sum hash is above the target, _Lines 4 – 11_ are repeated with a new nonce.
 
If you have made it this far, congratulations! After reading all of this information, you should have a good understanding of Autolykos v2! If you want a visual demonstration of Autolykos, please see the graphic at the end of this document. If you would like a video explanation, you can find it [here](https://youtu.be/pPYcfLQGIHg). 

