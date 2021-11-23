# Autolykos

> Participate in community discussions - [Ergo Emission: details, retargeting via a soft-fork](https://www.ergoforum.org/t/ergo-emission-details-retargeting-via-a-soft-fork/2778)

The security of Proof-of-Work blockchains relies on multiple miners trying to produce new blocks by participating in a *PoW puzzle lottery*. The network is secure if the majority of them are honest.  However, the reality becomes much more complicated than the original one-CPU-one-vote idea from the Bitcoin whitepaper.

Autolykos v1 originally had non-outsourcability built-in. However, it became apparent that it's impossible to prevent pools with smart contracts, so they turned it off so larger players could not take advantage of the loophole. Ergo is now focusing on memory hardness to keep mining as fair as possible, which should help prevent ASIC mining. There are also some improvements for pooling, e.g. Stratum 2 protocol.

> ["Bypassing Non-Outsourceable Proof-of-Work Schemes Using Collateralized Smart Contracts"](https://ia.cr/2020/044)  was presented by Alex Chepurnoy at the WTSC workshop associated with Financial Cryptography and Data Security 2020 in Malaysia.

It's also discussed here on ['Unblocked with Robert Kornacki' (14:45)](https://www.youtube.com/watch?v=2sbTMrQwWOw&feature=youtu.be)



## Difficulty Adjustment

Ergo uses the **linear least square method**, which smoothes over eight epoch's (each epoch is 1024 blocks x 2 minutes), as described in [this paper](https://eprint.iacr.org/2017/731.pdf). 

Autolykos will adjust slowly, yes, but it also helps prevent **adversarial** hopping.

**Can it be quicker?**

Having a quicker difficulty readjustment can lead to Timewarp attacks (amongst others).

Ergo is already using an epoch length of ~1.5 days (with normal block rate), not Bitcoin's two weeks. However, more epochs were considered, but the retargeting function is also non-linear, so that it may adjust sooner than the linear function in certain popular scenarios. 

## Hardforking policy

> Necessary changes require a hard fork, but Ergo has many possibilities to evolve via soft forks.


In the old generation of Proof of Work, hard forks frequently led to community splits. In Ergo, miners can change parameters on the fly in their configs, and 50%+ of blocks mined within 1024 blocks epoch need to be for raising/lowering the limit of some parameter, then it will be changed by 1% in next epoch. It can be block size, computational cost, storage fee factor and many more. The above comment for the old generation doesn't mention those core developers are also 3rd parties. With Ergo`s design, when all basic assumptions are correct, the network should adapt in time to a changing environment without the intervention of any trusted parties.

Ergo aims to avoid hard-forks. As any change regarding core parts of design essentially means another chain. However, developers were able to propose hard-forks within the first 12 months if:

- A hard-fork is about security fixes only. The only exception is making the cost of particular instructions adjustable via miners voting, which was planned but not delivered in the current mainnet.
- 90+% of miners supports a hard fork.
- A hard-fork is not breaking old contracts, freezing or moving any funds.

## [Voting for a soft-fork in Ergo](https://www.ergoforum.org/t/voting-for-a-soft-fork-in-ergo/2958)


## Autolykos V2


**Autolykos v.2** has the following modifications

- *non-outsourceable puzzles* were disabled. It turns out (based on more than one year of non-outsourceable PoW experience) that non-outsourceable PoW is not an attractive option for small miners.
- Now, the algorithm is trying to bind an efficient solving procedure with a single table of ~2 GB (initially), which significantly reduces memory optimizations possibilities
- Table size (memory requirements of a solving algorithm) grows with time
- The table depends solely on the block height, so there is no penalization for recalculating block candidates for the same height

**Basic Ideas:**

- Like Autlykos-1, based on the k-sum problem, so a miner needs to find `k (k=32)` out of `N (2^n = 2^26)` elements and the hash of their sum must be less than the target value (inverse of the difficulty)
- k indexes are pseudorandom values derived from block candidate and nonce
- N elements are derived from block height and constants, unlike Autolykos v.1, so miners can recalculate block candidates quickly now (so only indexes are depending on them)
- Indexes calculation also involving the same table (which elements are last 31 bytes of `H(i | | h | | M )`, where i is in [0, N), `h` is block height, M is padding to slow down hash calculation (8kb of constant data).

So algorithm tries to make mining efficient for ones that store the table, which is `2^26 * 31 = 2,080,374,784` bytes initially (about 2GB). Thus Autolykos is now is friendly to all the GPUs.

Also, table size (N value) is growing with time as follows. Until block `614,400`, `N = 2^{26} = 67,108,864 elements (31 bytes each)`. From this block, and until block `4,198,400`, every `51,200 blocks` `N` is increased by 5 percent. Since block `4,198,400`, value of `N` is fixed and equals to `2,143,944,600`. Test vectors for `N` values are provided in the paper.

- [Ergo PoW](https://www.docdroid.net/mcoitvK/ergopow-pdf)
- [Bypassing Non-Outsourceable Proof-of-Work Schemes Using Collateralized Smart Contracts](https://eprint.iacr.org/2020/044.pdf)


## Decentralisation 


While most active conversations today in the space are about the wider adoption of the blockchain technology, and competition with systems like Visa and Mastercard. This often means sacrifising decentralisation or introducing unclear security assumptions in the name of efficiency, there is an obvious need to revisit the roots of the cryptocurrency movement.

Is it okay when 90% of mining power in Bitcoin [can gather in one room](https://twitter.com/lopp/status/673398201307664384)? 
- Is it okay when 2 or 3 mining pools control the majority of hashing power? 
- Is it okay when almost all the new nodes avoid processing a blockchain from its genesis block? 
- Is it okay when Proof-of-Work coin developers are doing a hard-fork changing the consensus algorithm to make it GPU-friendly again? 
- Can we summarize all the issues with Decentralisation? 
- Can we cover most of the issues with technical means?

Decentralisation is about many issues across many fields, of technical, social, and hybrid kinds. Researchers and developers are trying to find technical solutions, preferably elegant and efficient. However, such solutions are not known; thus, social solutions are also needed. 

### 51% Attacks

Mining pools offer a buffer against such network attacks as the hash rate is distributed across thousands of individual miners.

Ergo's memory-hardened aspect also makes this attack vector more expensive as there is no ASIC support to rent. With the collective rentable rigs at the moment, this isn't a viable path to a 51% attack. In theory, someone could build a massive GPU farm to try to launch such an attack. If a bad actor can rent a warehouse of ASIC and mine on a small chain with 51% attacks are a viable option... if there is an offramp. 

This attack is usually performed for profit and results in massive dumping on an exchange as it is occurring. Meaning the attacker will dump tokens on an exchange then "double-spend" them back into their wallet. The current exchange situation doesn't provide the liquidity for a viable offramp. The rentable ASIC support isn't an option. So is it possible, in theory, yes, practical or likely? I don't think so at all.

Ethereum classic is perhaps a bad example, as it shares the same mining algorithm as Eth. One could buy more than 100% current hash rate of eth classic on NiceHash. It's not the same case for Ergo. Ergo also believes in the 'Good Miner' principle; in the case of Bitcoin - it was a good thing 51% existed. 



### Decentralisation of Mining

The two biggest concerns about decentralising mining are specialized hardware (such as ASICs) and centralized pools. 

With ASICs, a big player capable of investing enough money into R&D can get an unfair advantage from privately owned efficient hardware. In principle, for any computational activity, it is always possible to develop specialized hardware performing better than commodity computing units, such and CPUs and GPUs. However, for different computational tasks, R&D efforts and the possible outcome could vary a lot. The reasoning behind a search for a perfect (or close enough to perfect) could be quite complex (see, e.g. 30 pages long [Equihash paper](http://ledgerjournal.org/ojs/index.php/ledger/article/view/48)).

For most Proof-of-Work cryptocurrencies (including Bitcoin, Ethereum, ZCash), 2 to 4 centralized mining pools control most mining power. This could mean easy censorship or frontrunning on applications (for example, 
reordering exchange orders), as in centralized pools, only the pool decides block candidate for the whole pool to work on.
As a possible outcome, non-outsourceable mining schemes can prevent centralized pools formation. Only [Ergo Platform](https://ergoplatform.org/en/) is known for deploying a practical non-outsourceable Proof-of-Work scheme (based on a supposedly memory-harder problem from the [Equihash paper](http://ledgerjournal.org/ojs/index.php/ledger/article/view/48)) called [Autolykos](https://ergoplatform.org/docs/ErgoPow.pdf).   

As an example where social Decentralisation issues meet the Decentralisation of mining, sometimes developers of 
Proof-of-Work is introducing hard-forks to make a Proof-of-Work algorithm GPU-friendly again once ASICs are going to 
dominate in the mining market for the coin; however, it is always not quite clear why legitimate activity is banned and why developers (along with some users) can do hard-fork for this particular reason. 

### Decentralisation of Verification

Decentralisation of verification is about the possibility to check the validity of blockchain history. Such a check provides confidence that nothing bad (i.e. not conforming to a protocol) was injected into the blockchain. Thus, it gave a user a right to reject a malicious chain even if it has absorbed more work than alternatives. There were many talks about
such the right in the Bitcoin community when it was partly hot about User-Activated Soft Fork (UASF) idea, and  a recent article ["Who secures Bitcoin?"](https://medium.com/@BitcoinErrorLog/who-secures-bitcoin-95b19bbcda3c) is summarizing this way of thinking well. 

If verification can be done in reasonable time only by an entity able to spend millions on renting a data centre, a network is not decentralized. Ideally, it should be possible to check the integrity of the whole blockchain on commodity hardware, like a decent laptop.

However, new blockchains also tend to absorb more and more features, and they are not coming for free. Then the huge topic in the research community is about how to make it possible to check the integrity of the whole blockchain with pruned blocks or system state (or both) under plausible assumptions. Possible solutions here involve bootstrapping state snapshot and blockchain suffix on top of it (popular in Ethereum protocol clients, and formalized in [an academic paper even](https://eprint.iacr.org/2018/129.pdf)), stateless clients ([partially stateless](https://eprint.iacr.org/2016/994), as implemented in [Ergo Platform](https://ergoplatform.org/en/) or [fully stateless](https://eprint.iacr.org/2018/968) which do exist only in research papers currently).


## Test Vectors 

- [Test vectors for increased N values ](https://www.ergoforum.org/t/test-vectors-for-increased-n-values/2887/2)

## Solution Verification
```
Test Vectors - Ergo:
credit: Wolf9466#9466 on Discord

Height = 569806 (0x8B1CE)
Item count = 67108864 (0x4000000)
Prehash Item KAT:

Item index 0          : 0x00596fe417902d8fe61763deb06286d3bf787f3c8ea2cc3063724dd307993caa
Item index 4          : 0x00832cba40f67d525e9c449f17f46e3bfcdb663427d4289e35bc8e04b0c97765
Item index 255        : 0x003f44309d54120e5d41b36a245fea4098948f7e8c5c052247922b74a6c8e7b9
Item index 67108863    : 0x000701c3dd5db987aab0bb57f6e89ea9dbdc1dd88ffcac698bfde407d95063ce


Message = 0x9b8cb36a9b738fa3678521d00c938631e1a192bc1919f004d2cbabdaa33835b4
Nonce = 0x5d340003e9c460dc

Blake #1: 0xbd54dc777dc062c63b2f8cdd4d56f4f57b64d648420f62ef0e6f3935b0046fc99e7ea07b167ccadeaf2cd396504477697f5123e72887f61333358b5edbd5aa66

Blake #2: 0x6dbc710c2fb6e975d93af456686617b97595a0cec9dd22d57b8a7176d3f470b175eccfc1f97cecc13207fb68358c608930e5d7cfcdd0b3a4da8b9acb508e3248

Result = 0x0c3b54f29c8ac1a407f83cd09f3d61bc32996a3d58a7d9fe9fe0e0a08572e367f96b164cc3254ce5379622e007de97c76b1232030d899e0da83bc82e00000000
```

