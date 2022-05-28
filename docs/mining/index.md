> There are active miner communities on [Discord](https://discord.gg/Q86PNMwRsu) and [Telegram](https://t.me/ergo_mining).

# Mining

Ergo mining is based on [Autolykos](/mining/autolykos), an ASIC resistant Proof of Work algorithm written in Scala that runs cool and increases mining equipment longevity. Combined with the eUTXO model, this creates a highly efficient Proof of Work. Ergo had a fair launch with no premine, ICO or VC funding. Total Supply: `97,739,925` ERG.

**Getting Started**

- Mining
    - [Join a pool](join)
    - [Solo Mine](solo)
    - [Host a pool](pool)
- Learn More
    - [Autolykos](autolykos)
    - [Governance](governance)
    - [Storage Rent](rent)


## Background

### Launch
Ergo mainnet launched in 2019.

### The Hardening (Block #417,792)
Autolykos v1 originally had pool-resistance built-in through the use of non-outsourceable puzzles. Ergo had to adapt and support pooled mining to protect the chain’s consensus as unfortunately the non-out-sourceable puzzles concept was broken with smart contracts.

> ["Bypassing Non-Outsourceable Proof-of-Work Schemes Using Collateralized Smart Contracts"](https://ia.cr/2020/044) was presented by Alex Chepurnoy at the WTSC workshop associated with Financial Cryptography and Data Security 2020 in Malaysia.


### EIP27
Extends mining rewards to 2045. 

`777,272`



## Features

### [Governance](governance.md)

Ergo Miners have the ability to adjust the block size which increases the amount of transactions per block. This increases potential rewards but also adds additional storage requirements. adjust the emission macroeconomics, meaning the long term economic security of the protocol is up to miners to decide. 

| ID | Description | Default | Step | Min | Max |
|---|---|---|---|---|---|
| 1 | Storage fee factor (per byte storage period) | 1250000 | 25000 | 0 | 2500000 |
| 2 | Minimum monetary value of a box | 360 | 10 | 0 | 10000 |
| 3 | Maximum block size | 524288 |  | 16384 |  |
| 4 | Maximum cummulative computational cost of a block | 1000000 |  | 16384 |  |
| 5 | Token access cost | 100 |  |  |  |
| 6 | Cost per one transaction input | 2000 |  |  |  |
| 7 | Cost per one data input | 100 |  |  |  |
| 8 | Cost per one transaction output | 100 |  |  |  |
| 120 | Soft-fork (increasing version of a block) |  |  |  |  |

In addition to the protocol parameters above that can be changed via on-chain miner voting, most things on Ergo can be changed via a soft-forking protocol (90% support required). This excludes critical changes such as changing the max supply. 



### SubPooling

### Additional Mining Rewards

### Storage Rent



Storage Rent is a nominal fee (.14ERG per 4 years from an unmoved box) + transaction fees.

The problem with “storage rent fee” is this “fee” part — which may look like a disadvantage. However, programmers can quickly realize the importance of it by just imagining life without garbage collection in their language of choice.

Claiming fees sound great… But what happens if a UTXO cannot pay the fee?

Miners can take over assets inside a UTXO if there are not enough ERGs to pay for rent.
This feature is one of the most interesting reward mechanisms a PoW blockchain can offer miners. The relevance of this is particularly important in a blockchain that has the capacity to have a wide variety of assets.

To summarize, there is a potential for user assets to be seized if they are not active or cannot pay network rent due to inactivity and/or a lack of ERG.

For the average active user that periodically consolidates their UTXO set, this should not be an issue.

Pools may liquidate the assets as a mechanism for boosting the mining reward. This may be on a per block basis or proceeds may go into a reserve that is redistributed to their miners at a stable rate.

The Value of Storage Rent: Mining on Ergo


## Revenue Streams 

- Storage Rent
- Transaction Fees
- Emissions


As Ergo matures, more revenue streams will become available to miners. 

- Sidechain Rewards
- Bridge Infrastructure
- L2 Infrastructure


## FAQ

### 51% Attacks

Mining pools offer a buffer against such network attacks as the hash rate is distributed across thousands of individual miners.

Ergo's memory-hardened aspect also makes this attack vector more expensive as there is no ASIC support to rent. With the collective rentable rigs at the moment, this isn't a viable path to a 51% attack. In theory, someone could build a massive GPU farm to try to launch such an attack. If a bad actor can rent a warehouse of ASIC and mine on a small chain with 51% attacks are a viable option... if there is an offramp. 

This attack is usually performed for profit and results in massive dumping on an exchange as it is occurring. The attacker will dump tokens on an exchange then "double-spend" them back into their wallet. The current exchange situation doesn't provide the liquidity for a viable offramp, and the rentable ASIC support isn't an option. So is it possible, in theory, yes, practical or likely? I don't think so at all.

Ethereum classic is perhaps a bad example, as it shares the same mining algorithm as Eth. One could buy more than 100% current hash rate of eth classic on NiceHash, and it's not the same case for Ergo. Ergo also believes in the 'Good Miner' principle; in the case of Bitcoin - it was a good thing 51% existed. 

### Difficulty Adjustment

Ergo uses the **linear least square method** to calculate difficulty. This function is based on the past eight epochs (1024 blocks), as described in [this paper](https://eprint.iacr.org/2017/731.pdf) to obtain the target block interval of 120s (2 minutes). (On average, during steady-hash). 

- [Coin hopping Attack — What after a month of Bitcoin hardfork?](https://medium.com/nikoin/coin-hopping-attack-what-after-a-month-of-bitcoin-hardfork-f5a92151fb7b)

Autolykos will adjust slowly in response to fluctuating hashrate, but this helps prevent **adversarial** hopping. This algorithm has a 1.9% error rate compared to bitcoins 9.1% error rate (exponential 10% hash rate growth). 

**Can it be quicker?**

Ergo already uses an epoch length of ~1.5 days (with normal block rate), compared to Bitcoin's two weeks. Having a quicker difficulty readjustment can lead to Timewarp attacks (amongst others). More epochs were considered, but the retargeting function is also non-linear, so it can adjust sooner than the linear function in certain popular scenarios; and it is unclear whether any hard-fork would be required at this stage. 

While the consistenty of payouts has not been ideal during price drops, and is more suited for larger hashrates. Changing it at this stage would require a hard-fork to change (and then a HF again to add it back at a larger hash - or some timed mechanism). 

So the general consensus is people would rather deal with the inconsistent rewards until the mining landscape is clearer. 




## Decentralisation

### Decentralisation of Mining

The two biggest concerns about decentralising mining are specialised hardware (such as ASICs) and centralised pools. 

With ASICs, a big player capable of investing enough money into R&D can get an unfair advantage from privately owned efficient hardware. In principle, for any computational activity, it is always possible to develop specialised hardware performing better than commodity computing units, such as CPUs and GPUs. However, R&D efforts and the possible outcome could vary greatly for different computational tasks. The reasoning behind a search for a perfect (or close enough to perfect) could be quite complex (see, e.g. 30 pages long [Equihash paper](http://ledgerjournal.org/ojs/index.php/ledger/article/view/48)).

For most Proof-of-Work cryptocurrencies (including Bitcoin, Ethereum, ZCash), 2 to 4 centralised mining pools control most mining power. This could mean easy censorship or frontrunning on applications (for example, 
reordering exchange orders), as in centralised pools, only the pool decides block candidate for the whole pool to work on.
As a possible outcome, non-outsourceable mining schemes can prevent centralised pools formation. Only [Ergo Platform](https://ergoplatform.org/en/) is known for deploying a practical non-outsourceable Proof-of-Work scheme (based on a supposedly memory-harder problem from the [Equihash paper](http://ledgerjournal.org/ojs/index.php/ledger/article/view/48)) called [Autolykos](https://ergoplatform.org/docs/ErgoPow.pdf).   

As an example where social Decentralisation issues meet the Decentralisation of mining, sometimes developers of 
Proof-of-Work is introducing hard-forks to make a Proof-of-Work algorithm GPU-friendly again once ASICs are going to 
dominate in the mining market for the coin; however, it is always not clear why a legitimate activity is banned and why developers (along with some users) can hard-fork for this particular reason. 

### Decentralisation of Verification

Decentralisation of verification is about the possibility to check the validity of blockchain history. Such a check provides confidence that nothing bad (i.e. not conforming to a protocol) was injected into the blockchain. Thus, it gave a user a right to reject a malicious chain even if it has absorbed more work than alternatives. There were many talks about
such the right in the Bitcoin community when it was partly hot about User-Activated Soft Fork (UASF) idea, and  a recent article ["Who secures Bitcoin?"](https://medium.com/@BitcoinErrorLog/who-secures-bitcoin-95b19bbcda3c) is summarising this way of thinking well. 

If verification can be done in reasonable time only by an entity able to spend millions on renting a data centre, a network is not decentralised. Ideally, it should be possible to check the integrity of the whole blockchain on commodity hardware, like a decent laptop.

However, new blockchains also tend to absorb more and more features, and they are not coming for free. Then the huge topic in the research community is about how to make it possible to check the integrity of the whole blockchain with pruned blocks or system state (or both) under plausible assumptions. Possible solutions here involve bootstrapping state snapshot and blockchain suffix on top of it (popular in Ethereum protocol clients, and formalised in [an academic paper even](https://eprint.iacr.org/2018/129.pdf)), stateless clients ([partially stateless](https://eprint.iacr.org/2016/994), as implemented in [Ergo Platform](https://ergoplatform.org/en/) or [fully stateless](https://eprint.iacr.org/2018/968) which do exist only in research papers currently).


