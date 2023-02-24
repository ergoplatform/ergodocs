---
tags:
  - NIPoPoWs
  - Plasma
  - Sigma Protocols
---

# Scaling

These sections explore all past and potential scaling across each layer. If you're a developer the [Plasma Library](plasma.md) is available to use in your application.  

- [Layer 0](layer0.md): The *Network* or *P2P* Layer
- [Layer 1](layer1.md): The Blockchain
- [Layer 2](layer2.md): Off-chain

## The next evolution of blockchain.

There are three generations of blockchain, each capable of more complex behaviours than the last. 

- The **first generation** refers to the original use BTC was intended for, that is, to provide a reliable and accurate method of maintaining a public transaction ledger. 
- **Second-generation** blockchains were created with the implementation of smart contracts as a priority, with the most popular one being ETH (Ethereum). One of the big differences in ETH is the language used to smart code contracts. ETH utilizes a [turing complete](https://www.cs.odu.edu/~zeil/cs390/latest/Public/turing-complete/index.html) language (known as Solidity), meaning it is computationally universal. 
- The **third generation** of blockchain technology now focuses on solving issues with congestion and scalability. As this technology becomes more decentralized, there will inevitably be an exponential increase in the number of users interacting with the blockchain. DOT, ADA and ERG are third-generation blockchains, meaning they have smart-contract capabilities while proposing solutions to scalability for a global audience. 

Third-generation blockchains generally can process off-chain transactions, helping speed up transactions significantly. The account model performs both storage changes and validity checks on-chain during code execution. In contrast, Ergo transactions are created off-chain, and only validation checks are performed on-chain, reducing the number of operations performed by every node on the network. In addition, due to the immutability of the transaction graph, various optimization strategies can improve the throughput of transactions per second in the network. 

Light-verifying nodes are also possible, thus further facilitating the scalability and accessibility of the network.

Based on a decade of research, extensive testing pre-launch and ongoing development, the Ergo community has launched a blockchain with all the tools to scale a globally. 


## Settlement Layer

Thanks to the high flexibility of the ErgoScript programming model, large chunks of transactions can happen on layer two and be settled in Ergo using a single transaction. 

Below you will find a developer harnessing the power of eUTXO to airdrop native tokens to [10,000 addresses at once](https://explorer.ergoplatform.com/en/transactions/e2c4954665ccf87791f42983ae4f7031205c2e719709907cbf2ff09e5489d4b8)

ErgoScript adds several improvements such as time-weighted data, Turing completeness, read-only data inputs, multi-stage contracts, sigma protocols, NIPoPoWs and more that make many different protocols possible on Layer 2, each one solving scalability problems in a specific domain (like simple payment transactions, sped up with sub-block confirmation protocols).
**Ergo can be considered a common *settlement layer* for many Level-2 protocols and applications.**






## Roadmap (Dec 2021)

[Ergo protocol research and client development roadmap (Dec, 2021)](https://www.reddit.com/r/ergonauts/comments/qfjhw4/ergo_protocol_research_and_client_development/)

> We are researching different scalability proposals for Bitcoin, Cardano, and Ethereum, such as sidechains (which are also nice for testing new features), commit chains, rollups, isomorphic state channels, FairSwap etc. New opcodes are needed for some solutions for Bitcoin (so a little chance to see things in the real world), while Ergo allows for such constructions with no forks. Ergo will not just be a chain but a king of chains (which will improve the cryptoeconomic security of the protocol as miners will get additional rewards from sidechains).

> for improving the performance of the network, the reference protocol client (Ergo node) is getting different performance improvements in the p2p layer and not only right now

> bootstrapping via UTXO set snapshot and NIPoPoWs are in progress now. This should allow a client to have much faster bootstrapping without compromising security.

> 5.0 soft-fork is going to be proposed to miners soon; the main change is about switching to just-in-time-costing in ErgoTree evaluation which is giving a 5-6x boost in scripts processing (on real blockchain data)

> time to consider long-term cryptoeconomic security of the protocol; discussions have already started: https://www.ergoforum.org/t/ergo-emission-details-retargeting-via-a-soft-fork/2778/7

> for application development, more frameworks and ready apps are needed; there are some results to be announced already

> Plans for supporting the different application is out of the scope of this text and would be a topic of another piece.

## Resources

- [A Scalability Plan for Ergo](https://www.ergoforum.org/t/a-scalability-plan-for-ergo/226)
- [Network congestion on Jul 10th, 2021](https://www.ergoforum.org/t/network-congestion-on-jul-10th-2021/1945)
- [Long-term vision for Ergo](https://www.ergoforum.org/t/long-term-vision-for-ergo/2629)
