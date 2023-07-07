# A Systematic Approach To Cryptocurrency Fees

This page is a continuation and summarisation of the paper storage rent was introducted in, *[A Systematic Approach To Cryptocurrency Fees](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf)* (hereinafter referred to as the paper) by Alex (Kushti) Chepurnoy, Vasily Kharin and Dmitry Meshkov. In the paper, the authors address the problem of storage resource utilisation. There is a concern that once an element of the state is created, it exists forever and inevitably balloons node disk space, leading to unreasonable state growth of the blockchain.

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
