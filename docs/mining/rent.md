# Storage Rent

__We've designed Ergo with long-term economic sustainability in mind, and storage rent is one of the ways we're ensuring miners stay profitable well into the future. This can be thought of as 'on-chain garbage collection' that reduces the problem of blockchain bloat – and even makes it profitable.__

**Key Points**

- After block **1,051,200**, a miner can charge storage rent or spend the box fully if its value is not covering rent.
- An important consequence of storage fees is that they provide miners with additional rewards (besides block and transaction rewards).
- Storage fees decrease the storage load and eliminate extra costs that could be added during excessive state growth.
- Storage fees encourage coin flow and prevent deflation, which can cause illiquidity and the congestion of a currency system.

You can read more about how fees will be levied in [this paper](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf).

## What is *'Storage Rent'* 

Storage rent is a nominal fee charged on unspent output after four years, with a price per byte defined by the storage rent subprotocol. This works out to about 0.14 ERG per four years for a box with no tokens and no complex scripts. You can read more details on [the forum](https://www.ergoforum.org/t/storage-rent-details/256)

## Fee Determination

A box cannot be created with fewer ergs than a minimum value per byte (of the box). The default value is **360 nanoergs per byte**. Miners can vote to adjust this value within the range of `[0, 10000]` nanoergs per byte (inclusive). They can vote to increase by 2 or decrease by -2, with a per-epoch step of 10 nanoergs/byte. 

> For example, if the majority of miners vote to increase the default value during an epoch of 1,024 blocks, the value in the next epoch will be 370 nanoergs/block.

Every four years, **a miner can collect a storage rent fee by spending the box and recreating it while preserving all registers**, except R0 (which holds the monetary value) and R3 (which holds the creation height and a reference to the transaction identifier and output index where the box was created). The storage rent fee is determined through network consensus by voting on the storage rent fee per byte value. The default value for this parameter is 1,250,000 nanoergs/byte. Miners can vote to change this value within the `[0…2,500,000]` range by voting for 1 or -1, with a step of 25,000.

For more information please see the [Governance](governance.md) section

## Modeling 

FeeSimulator.scala is a tool that outputs simulation results related to blockchain storage fees to the console. One of its calculations is the average size of a "standard box," which is derived from the sizes of two P2PK-protected boxes – one containing only ergs and the other containing an additional asset. The results are as follows:

- **Box size**: 105 bytes
- **Storage fee for an ordinary box**: 0.13125 ergs

This means a simple box will incur a storage fee of approximately 0.13 ergs every four years.

The crucial question is how miners will connect transaction fees to storage fees. For instance, let's say miners require a transaction to pay for input boxes' byte size proportionally to their lifetimes. In this case, miners will receive a constant reward from the UTXO set of a fixed size for four years. After that, the reward per block will be calculated as `perOutputFee * (numberOfBoxes / (4 * BlocksPerYear))`. Assuming Ergo's UTXO set size is similar to Bitcoin's (~60 million), the estimated reward per block would be:

- 7.49 Erg + transaction fees

There is also a great post on r/ergonauts, [Discovering Ergo's Storage Rent Potential](https://www.reddit.com/r/ergonauts/comments/xeke0b/discover_ergos_storage_rent_potential/)


## What about tokens, NFTs, etc?

Ergo's storage rent mechanism, which allows miners to take over valuable assets inside a UTXO if there are insufficient ERGs to pay rent, offers a unique reward system for miners in a Proof-of-Work blockchain. This mechanism is particularly relevant in a blockchain ecosystem that supports a wide variety of assets, such as NFTs, oracle tokens, access tokens, and stablecoins like SigUSD.

On the positive side, this mechanism incentivizes miners by offering them additional rewards, making the Ergo blockchain more attractive and encouraging participation. This increased participation can enhance the network's security and overall health. Furthermore, storage rent promotes active management of assets, ensuring that users remain engaged and that their assets do not stagnate. It also allows valuable assets to be reintroduced into the ecosystem if users lose access to their private keys or abandon their assets. Moreover, it helps minimize blockchain bloat by ensuring that only assets with sufficient ERG value to cover their storage rent remain on the blockchain, leading to a more efficient and scalable blockchain.

However, there are drawbacks to this mechanism. Users who are not aware of the storage rent system or fail to maintain enough ERG in their UTXO may lose valuable assets unintentionally. 

It is worth noting that a proposed EIP (Ergo Improvement Proposal) [EIP-33: Token burning during rent collection #68](https://github.com/ergoplatform/eips/pull/68) is under consideration, which could potentially address some of these concerns. Users should carefully weigh the pros and cons of Ergo's storage rent mechanism and ensure they have sufficient ERG to cover their storage rent to protect their valuable assets.

[TokenJay](tokenjay.md) has a handy [Box consolidation tool](https://tokenjay.app/app/#boxconsolidation) that checks the number and age of boxes in your wallet and consolidates when necessary. You can also message [@ergoportbot](https://t.me/ergoportbot) on Telegram and use the command `/ep boxage ADDRESS` to check. 

## How does it work?


The following conditions must be met in order to spend a box:

1. The difference between the upcoming block's height (taken from the preheader) and the box's creation height must be greater than or equal to the storage fee period. In other words, the box must have been stored for at least the required storage fee period.
1. The *spending proof* for the expired box must be empty.


This line of code checks if the box has been stored for at least the required storage fee period. It calculates the difference between the upcoming block's height (`context.preHeader.height`) and the box's creation height (`context.self.creationHeight`). If this difference is greater than or equal to the constant value representing the storage fee period (`Constants.StoragePeriod`), the condition is satisfied.
   
```
context.preHeader.height - context.self.creationHeight >= Constants.StoragePeriod
```
   (Reference: ErgoInterpreter, line 64)

The "spending proof" for the expired box refers to a cryptographic proof that is typically required to authorize the spending of a box (or transaction output). In the case of an expired box, the condition "spending proof must be empty" means that no such cryptographic proof is needed to spend the box. This allows anyone to spend the expired box without providing any proof of ownership, as long as the other conditions are met (such as the box being stored for at least the required storage fee period).

If these conditions are met, anyone can spend the expired box by providing an index of a recreated box (or an index of any box if the expired box doesn't have enough funds to cover the storage fee) in context extension variable #127, which is stored in the input.

## Why is this needed? 

The 2020 block reward reduction was the most important halving event Bitcoin has experienced. This was where the narrative of programmatic scarcity and digital gold was truly proven in the context of the sharpest economic downturn in living memory. In previous halvings, Bitcoin is still a niche experiment in its infancy. Future halvings will confirm the principle. But this one is the watershed.

Looking ahead, though, what happens in 20 or 30 years when block rewards have fallen so far that miners have to rely on transaction fees and potentially other sources of revenue? Will Bitcoin be sustainable? What will be the impact on the ecosystem?

*The simple answer is that we don't know.*

Mining rewards are a key feature in maintaining the security of proof-of-work blockchains like Bitcoin and Ergo. And so, while we have deliberately kept many of Bitcoin's tried and tested features, we have updated this one to boost miners when block rewards have fallen to zero.

- [Ergo Explainer: Storage Rent](https://ergoplatform.org/en/blog/2022-02-18-ergo-explainer-storage-rent/)
- [Tracking storage rent potential](https://www.reddit.com/r/ergonauts/comments/tyymax/tracking_storage_rent_potential/)


## Lost coins

Digital scarcity is an important feature of Ergo. Like Bitcoin, ERG is designed to be a finite resource and long-term store of value. We do not agree with the principle of infinite inflation.

And yet, this has to be balanced against the need to pay miners to secure the blockchain and process transactions. With adequate compensation for miners, there is a viable blockchain. Ergo approaches this by slowly recycling lost coins, in a feature we call 'Storage rent'. 

Studies suggest that as many as [4 million BTC may have been lost forever](https://bitcoinist.com/estimated-4-million-bitcoin-lost-forever-by-users-forgetfulness/). These are coins mined in the early days of Bitcoin and stored on hard drives that were subsequently thrown away or destroyed because the owners forgot about them or thought they were worthless, as well as coins in addresses for which the private keys have been lost. (And, of course, there are Satoshi's estimated holdings of 1 million BTC, which may never move.)

Where coins have been permanently taken out of circulation in this way, it makes sense to have a mechanism to recover them and put them back into the blockchain economy. That way, we can preserve digital scarcity without unnecessarily accelerating it. In other words, by attempting to stick to the intended algorithmic supply for any given point in time.


## A Systematic Approach To Cryptocurrency Fee

This article is a continuation and summarisation of *[A Systematic Approach To Cryptocurrency Fees](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf)* (hereinafter referred to as the paper) by Alex (Kushti) Chepurnoy, Vasily Kharin and Dmitry Meshkov. In the paper, the authors address the problem of storage resource utilisation. There is a concern that once an element of the state is created, it exists forever and inevitably balloons node disk space, leading to unreasonable state growth of the blockchain.

While cryptocurrencies address transaction fees as an atomic concept, the paper suggests that it is reasonable to consider this on a 3-dimensional scale.

![Figure A.](https://ergoplatform.org/img/uploads/3d.png)

### Key Takeaways
- Transaction fee schemes based on space and duration of objects in the state
- State growth in blockchain technology can lead to centralization and SPV mining
- Fee differentiation algorithm for transactions in a blockchain network
- Differentiable pricing curve for storage in a blockchain network
- Evaluation of pricing coefficients in a transaction classification system
- Implementation of a fee component to make state size more predictable
- Side effects of storage fees, such as returning lost coins into circulation
- References to sources on the instability of Bitcoin without the block reward
- Ethereum Project Yellow Paper outlining technical specifications and design principles


### Blockchain Costs

Proof of Work blockchain technology relies on miners to guard the integrity of the blockchain. Miner resources, such as memory and electricity, are costly; therefore, a revenue scheme is needed to incentivise miners. Miner incentives are currently comprised of block rewards and transaction fees, and transaction fees are an important component in preventing spam attacks that exhaust miner resources.

Besides network utilisation, transaction processing requires a miner to spend resources to maintain all the original blockchain data. In the case of Bitcoin, this might be less of a problem because it has yet to implement smart contract functionality. Cryptocurrencies that support smart contract languages, such as Solidity (Ethereum), however, may require a lot of computations, and related costs will be included in the transaction fee.

The 3-dimensional scale shown above is based on storage-oriented, computational, and network load.

* Storage-oriented load refers to the additional cost of storing old data in the blockchain. 
* The execution of smart contracts creates a computational load. 
* Network load is all the transactions that do not exist in the current block but will be added to the next block.

In Ergo, the total size of the state is the sum of the sizes of all UTXOs. This data contains the execution of smart contracts, all the transactions and nodal information. Because the memory resources miners provide are limited, a state deterioration fee should be added to miners' revenue streams to encourage decreasing the system load while securing future miners' contributions.

### State Growth

**Unreasonable state growth** is an economic problem, and it can lead to spam attacks and network congestion. Another problem could be the deflation of a cryptocurrency if coins are lost or forgotten. So instead of being used as the base for smart contracts, the currency becomes unreasonably scarce, making the system heavy and limiting coin flow.

This leads to a perpetually increasing state (e.g. the Bitcoin's total UTXO size), which may grow faster during spam attacks. For example, 15 million outputs were created during spam attacks against Bitcoin in July 2015. An attack on Ethereum created 18 million new accounts added to the state - which previously held only 1 million - and performed successful "denial of service" attacks against the nodes.

The paper proposes a "storage rent" fee to tackle the unreasonable state growth problem. Storage rent is a scheduled fee based on the continuation of each UTXO created in the blockchain. This is achieved by using scheduled payments, and eradicating unused bytes after a certain time.

Additionally, using blockchains as cloud storage is gaining attraction, so permanently storing objects in the state without some form of recirculation procedure of the old data is not a plausible option.

For research and this article, it is worth noting that the concept of storage rent was also proposed in 2014 by [Freicoin](http://freico.in):

> *"Demurrage forces freicoins to circulate at deliberately high rates. Separation of money's roles as store-of-value and medium-of-exchange allows money to flow when it is needed, in good times and bad. "*


## Resources


- [HF-4.0 Reduce storage rent period #1144](https://github.com/ergoplatform/ergo/issues/1144) - Rejected
- [EIP-0045 Redistribution contracts for Storage Rent Fees #93](https://github.com/ergoplatform/eips/pull/93)
- [EIP-39 Monotonic box creation height rule](https://github.com/ergoplatform/eips/blob/master/eip-0039.md)
- [EIP-33: Token burning during rent collection #68](https://github.com/ergoplatform/eips/pull/68)