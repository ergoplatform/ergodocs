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

## How much is the fee? 

The default fee is 360 nanoERGs per byte but can be raised by [miners voting](governance.md)

## What is the potential? 

- [Discovering Ergo's Storage Rent Potential](https://www.reddit.com/r/ergonauts/comments/xeke0b/discover_ergos_storage_rent_potential/)


## What about tokens, NFTs, etc?

Miners can take over assets inside a UTXO if there are insufficient ERGs to pay rent. This feature is one of the most interesting reward mechanisms a PoW blockchain can offer miners. The relevance this has is particularly important in a blockchain that can have a wide variety of assets.



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
