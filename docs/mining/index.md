> There are active miner communities on [Discord](https://discord.gg/Q86PNMwRsu) and [Telegram](https://t.me/ergo_mining).

# Mining

Ergo mining is based on [Autolykos](/mining/autolykos), an ASIC resistant Proof of Work algorithm written in Scala that runs cool and increases mining equipment longevity. Combined with the eUTXO model, this creates a highly efficient Proof of Work. Ergo had a fair launch with no premine, ICO or VC funding. 

**Getting Started**

Unless you have 1TH/s+, you likely want to be mining from a pool. Available miners and pools listed in the pool section. 


- [Mining from a pool](setup/join)
- [Solo Mining](setup/solo) - [Can I solo mine?](https://docs.google.com/forms/d/e/1FAIpQLScBFv3mxpu5Erv55zvfFuIo2NnaWht3cc70xZoRo-3c58Cv0A/viewform)
- [Hosting a pool](setup/pool)
- [Subpooling](/mining/setup/subpool)


**Resources**

- The [Ergo Explorer](https://explorer.ergoplatform.com) can give you various information & stats on mining and the network. 
- [Difficulty and epoch monitor.](http://cds.oette.info/ergo_diff.htm)
- [Wallets](wallets.md)
- [Ergo Mining Breakeven Price Calculator](https://babygrenade.github.io/ergo-profit-calc/)
- [Discovering Ergo's Storage Rent Potential](https://www.reddit.com/r/ergonauts/comments/xeke0b/discover_ergos_storage_rent_potential/)
- [What are smart pools?](https://ergoplatform.org/en/blog/2021-11-19-ergo-smartpools-and-decentralized-mining/)

- [Mining Guide](https://ergonaut.space/en/Mining)

**Discussions**

- [Ergo Emission: details, retargeting via a soft fork](https://www.ergoforum.org/t/ergo-emission-details-retargeting-via-a-soft-fork/2778/2)

## [Autolykos](autolykos)

- Autolykos v1 originally had pool-resistance built-in through the use of non-outsourceable puzzles.
- **The Hardening Hard-Fork** on block `417,792` marked the launch of Autolykos v2, enabling mining pools. See this [paper](https://ia.cr/2020/044). 
- [**EIP27:**](../dev/protocol/eip27) was passed with overwhelming community support, extending emission by 4,566,336 blocks (~17.38 years). This will be activated on block `777217`







## [Governance](governance.md)

Ergo Miners have the ability to adjust the block size which increases the amount of transactions per block. This increases potential rewards but also adds additional storage requirements. adjust the emission macroeconomics, meaning the long term economic security of the protocol is up to miners to decide. 

In addition to the protocol parameters above that can be changed via on-chain miner voting, most things on Ergo can be changed via a soft-forking protocol (90% support required). This excludes critical changes such as changing the max supply. 


## [Storage Rent](rent)



Storage Rent is a nominal fee (.14ERG per 4 years from an unmoved box) + transaction fees.

The problem with “storage rent fee” is this “fee” part — which may look like a disadvantage. However, programmers can quickly realize the importance of it by just imagining life without garbage collection in their language of choice.

> *Claiming fees sound great… But what happens if a UTXO cannot pay the fee?*

Miners can take over assets inside a UTXO if there are not enough ERGs to pay for rent. This feature is one of the most interesting reward mechanisms a PoW blockchain can offer miners. The relevance of this is particularly important in a blockchain that has the capacity to have a wide variety of assets.

As Ergo matures, more revenue streams will become available to miners. 

- Sidechain Rewards
- Bridge Infrastructure
- L2 Infrastructure

