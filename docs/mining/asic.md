
## ASIC Resistance
 
We know from Ethereum that ‘memory hard’ algorithms can be conquered by integrating memory on ASICs. Ergo is different but let’s first revise why an ASIC with limited memory is uncompetitive and why a miner needs to store _**list R**_. 

Line 8 of Autolykos block mining deters machines with limited memory. 
- If an ASIC miner does not store _**list R**_, they require a lot of cores to generate the 31-byte numeric hashes on the fly. 
- 32 _**r**_ values cannot be efficiently calculated using a single core loop because an output would only be generated every 32nd hash cycle. 
- Given _**J**,_ to compute one nonce _per hash cycle,_ at least 32 *Blake2b256* instances running _**dropMsb(H(j||h||M))**_ are needed. 
- As we mentioned above, this increases die size and cost significantly. Storing _**list R**_ is worthwhile because having 32, or even 16, cores are very expensive. More to the point, reading memory is faster than computing Blake instances every time a nonce is tested.
 
Let’s see if an ASIC with sufficient memory is competitive because that is more relevant to the discussion. Comparing Ethash and Autolykos, the difference is that Ethash involves **N** elements when hashing the nonce and header mixes 64 times. In contrast, Autolykos involves **N** elements when fetching 32 _**r**_ values based on indexes generated. 

For every tested nonce, Autolykos runs about 4 *Blake2b256* instances and 32 memory fetches, while Ethash runs about 65 SHA-3-like instances and 64 memory fetches. Not to mention, _**k**_ is currently set at 32, but this value can be increased to retrieve more _**r**_ values if needed. ASICs that run Ethash have a lot of room to increase SHA3 hashing speed since 65 hashes are completed per tested nonce compared to about four on Autolykos. The ratio of memory fetches to hash instances is much greater on Autolykos. For this reason, Autolykos is more memory-hard than Ethash since memory bandwidth plays a much larger role than hashing speed.
 
An area where Autolykos optimisation could take place is the filling of _**list R**_. The filling of _**list R**_ requires _**N**_ instances of a *Blake2b256* function. _**N**_ is large and only getting larger, so that’s a lot of hashing. An ASIC could optimise the speed of *Blake2b256*, yielding more time for block mining since _**list R**_ is filled sooner. Although this can be done, filling _**list R**_ requires cycling through [0, N) and a GPU with 32-wide multiprocessors can already fill _list R_ very fast (in seconds). One would need an ASIC with many Blake cores to be significantly faster – again, very expensive and probably not worthwhile since the bottleneck could become memory _write_ bandwidth (i.e., writing _**list R**_ to RAM rather than hashing speed).
 
The last area that can be optimised for Autolykos is a memory read/write speed. Ethash ASIC miners have a slightly faster read speed compared to GPUs, as the memory is clocked higher without the effect of GPU throttling. However, this difference is insignificant and is expected to become more insignificant as GPUs advance. This is because the memory hardware itself is the same: DRAM. One may question if faster memory hardware could be utilised whereby memory read and write speed is far quicker. SRAM, for instance, could be an imaginable next step in breaking memory hard algorithms, however, SRAM is not a feasible solution simply because it is less dense.
 
#### SRAM on FPGA[2]
 
![unnamed (7).png](https://storage.googleapis.com/ergo-cms-media/unnamed_7_87793f77f4/unnamed_7_87793f77f4.png)
 
The above photo is an FPGA with eight memory chips on the front and another eight on the back. The total SRAM memory is only 576MB. Fitting sufficient SRAM on a die won’t work because the SRAM will need to be placed further from the core as it is not dense enough to fit in one layer around the core. This can result in read/write delays because electricity needs to travel long distances even though the hardware is faster. Additionally, to mine Ergo, the memory requirement increases as N increases, so fitting sufficient SRAM is not feasible over time. Thus, SRAM ASICs are not worthwhile exploring even if one has enough cash to spend on SRAM itself.
 
## *Blake2b256*
 
One major difference between an algorithm like Autolykos and others is the use of *Blake2b256*. This is no coincidence. Blake relies heavily on addition operations for hash mixing instead of XOR operations. An operation like XOR can be done bit by bit, whereas addition requires carrying bits. Thus, Blake requires more power and core area compared to SHA algorithms, but it is still as secure and faster. As mentioned on the Blake2 website, “BLAKE2 is fast in software because it exploits features of modern CPUs, namely instruction-level parallelism, SIMD instruction set extensions, and multiple cores.”[3] Thus, while an ASIC can output Blake instances faster, the innate nature of the function limits optimisations by requiring addition and involving features found in CPUs and GPUs.
 
#### Blake2b speed relative to other hash functions
 
![unnamed (8).png](https://storage.googleapis.com/ergo-cms-media/unnamed_8_e6913d1172/unnamed_8_e6913d1172.png)