# Exploring Ergo: A Future-Ready Blockchain

Ergo is a forward-thinking, proof-of-work smart contract platform designed to bring innovative financial interaction models to life. This platform is supported by a robust and secure scripting language, an array of potent zero-knowledge proofs, and a foundation built on the best principles and research in cryptography and blockchain technology. 

## Understanding Ergo's Objectives

### Research-oriented, Practical Focus

Ergo is built on a decade of blockchain development, marrying reliable concepts with state-of-the-art peer-reviewed academic research in digital currencies and cryptography. This unique approach has allowed Ergo to integrate [cutting-edge cryptographic features](documents.md) directly into its framework, providing a robust and future-ready platform.

### Robust and Secure

Ergo is designed to support versatile dApps (decentralized applications) that can execute tasks reliably with predictable costs, ensuring financial agreements' security. Ergo's [smart contracts](../../dev/scs) can carry out a broad spectrum of tasks, and though they can be Turing complete, their cost and successful execution can always be forecasted in advance.

### Smart and Easy-to-Use

Sigma Protocols [(Σ-Protocols)](sigma.md) form the foundation of Ergo's smart contracts. These protocols enable efficient zero-knowledge proofs, facilitating complex tasks that would otherwise be impossible or risky. This system fosters trustless scripts with self-sovereign application-level privacy, eliminating the need for third parties.

### Secure and Accessible

Ergo believes in democratizing blockchain security. Thus, regular users, even without running a full node, can enjoy security benefits at par with miners. Non-Interactive Proofs of Proof-of-Work [(NIPoPoWs)](nipopows.md) allow users to make and verify transactions confidently, requiring only 1 MB of data, making it feasible for any device.

## Ergo's Key Features

- **[ErgoScript](ergoscript.md)**: This programming language sets the rules for spending currency. It's designed to support a multitude of features like ring signatures, atomic swaps, multiple currencies, and self-replicating scripts.
- **[Sigma Protocols](/dev/scs/sigma)**: These are non-interactive zero-knowledge proofs that can be composed using basic *AND/OR* logic. 
- **[Multi-stage Contracts](/dev/scs/multi)**: Ergo extends the standard threshold `m‐of‐n` signature protection, enabling the specification of complex recipients of these coins. This feature facilitates the creation of **complex, secure, and efficient smart contracts**. 
- **[Non-Interactive Proofs of Proof of Work (NIPoPoWs)](nipopows.md)**: They enable truly decentralized Ergo DApps and off-chain protocols via light clients.
- **[Storage Rent](rent.md)**: This feature helps manage blockchain bloat and turns it profitable.
- **[eUTXO](eutxo.md)**: This model enhances privacy, scalability, and interoperability.

By extending Bitcoin's contract-writing method, Ergo attaches a guard script and additional custom data to each coin. This feature positions Ergo as a uniquely beneficial platform for Contractual Money.

**Keeping all this in mind, we expect Ergo's design to be uniquely useful as Contractual Money.**

See the [Ecosystem](https://docs.ergoplatform.com/uses/) section for an overview of all the current and potential uses for Ergo.

## The Launch of Ergo 

The Ergo Blockchain, launched in 2019, is a brainchild of a group of respected developers and cryptocurrency experts, most notably Alex Chepurnoy and Dmitry Meshkov, who have made significant contributions to the blockchain community. The primary goal behind Ergo's creation was to provide a highly efficient, secure, and easy-to-use platform for financial contracts, harnessing the power of blockchain technology in the process.

The developers recognized the need for a decentralized, yet secure, platform to facilitate the creation and execution of complex financial contracts in a digital environment. They saw a future in which DeFi could play a critical role in a variety of industries and thus, Ergo was launched to deliver a robust infrastructure for building such applications.

### Fair Start

Ergo prioritized a fair and balanced launch and token distribution. This approach was designed to avoid the influence of venture capitalists or large-scale investors, thereby closely emulating Bitcoin's launch model. Ergo adopted a strategy of setting aside funds via its mining protocol, primarily intended for a modest treasury to cover fundamental costs and to provide the necessary funding.

The Ergo Foundation, a non-profit organization, is committed to promoting the widespread adoption of Ergo. The Foundation's treasury has been accumulated through a small fraction of the blocks mined during the first 2.5 years since the launch of Ergo's mainnet. This sum equates to 4,330,791.5 ERGs or approximately 4.43% of the total supply.

More information about the Ergo Foundation can be found [here](ergo-foundation-2022.md).

> The lack of venture capital funding for the primary protocol at the initial stages should be seen as a strength rather than a weakness. It encourages community-driven leadership, which is the only truly sustainable solution for maintaining decentralization in the long run.

### Research-Based Approach

The Ergo Blockchain is a result of extensive research and uses innovative solutions to address the issues and inefficiencies that have been identified in previous blockchains. It employs an array of research-driven features such as non-interactive proof of proof of works ([NiPoPoWS](nipopow.md)), which offer enhanced privacy, and a memory-hard mining proof of work mining algorithm which ensures decentralisation and adaptability.

The architecture is designed to be flexible, allowing it to adapt to new technologies and changes in user requirements over time. Its blockchain pruning feature allows nodes to discard unnecessary historical data while still maintaining complete security, which is a significant step towards improving the scalability of the blockchain.

Ergo’s unique approach to smart contracts, called ErgoScript, is also a result of extensive research. It allows the platform to host more complex financial contracts in a highly secure and efficient environment. ErgoScript contracts are based on the principles of Σ-protocols, a type of zero-knowledge proof, which allows for greater flexibility and security.


### What Problems Faced by Bitcoin Does Ergo Solve?

Ergo is designed to address several key challenges that are inherent to Bitcoin, enhancing the functionality, security, scalability, and privacy of the cryptocurrency ecosystem. The table below presents a comprehensive comparison between the issues faced by Bitcoin and the innovative solutions proposed by Ergo. These solutions involve advanced smart contract functionality, improved network security, efficient data structures for light clients, robust privacy tools, and scalable governance mechanisms. These improvements are geared towards creating a more inclusive and versatile blockchain platform.

| Problems Faced by Bitcoin | Ergo's Solution |
|---|---|
| Limited smart contract functionality | A rich language (ErgoScript) combined with the eUTXO model, Sigma protocols and transaction chaining (for turing completeness) |
| Unclear network security as the block reward subsidy approaches zero and transaction fees remain low and volatile | More revenue from transaction fees due to DeFi  and higher usage/scalability, storage rent, mining  by subpools of tokens issued on Ergo (providing even more security incentive) |
| Lack of economy around state leading to miners receiving no compensation for holding the UTXO set in high cost memory - this is a big obstacle to scaling |  Storage Rent provides additional rewards  for miners while increasing network security. It also compensates miners for long-term holding of the UTXO set, thus allowing larger state growth and (indirectly) larger block sizes  |
| Inefficient merkle tree data structure leading to inefficient light clients  (Ethereum has the same problem) | AVL trees leading to drastically more efficient light client verification, and thereby allowing the use of commodity hardware to verify transactions. This is also used in Plasma (layer 2 on Ergo built by Getblok.io) |
| Weak and cumbersome optional privacy tools, some of which have been compromised | Sigma protocols enable true peer to peer privacy. ErgoMixer is the only token-mixer that can provide better anonymity than Monero given enough utilisation.  |
| Massive scaling challenges which led  to the ‘Blocksize Wars’ | Decentralized on-chain governance based on extensive research - block size can be increased securely. NiPoPoWs enable light clients with full node security guarantees. Ergo offers more Layer-2 options than Bitcoin.  |

### What Problems Faced by Ethereum Does Ergo Solve?

The Account model of Ethereum is imperative. This means that the typical task of sending coins from Alice to Bob requires changing the balances in storage as a series of operations. On the other hand, Ergo's UTXO based programming model is **declarative**. 

ErgoScript contracts specify conditions for a transaction to be accepted by the blockchain (not changes to be made in the storage state as a result of the contract execution).

| Problems Faced by Ethereum | Ergo's Solution |
|---|---|
| Creating transactions and utilizing smart contracts requires paying fees in ETH and maintaining an ETH balance, thereby leading to a poor user experience | Babel Fees on Ergo allow the user to pay the transaction fee in whatever native tokens they have in a wallet  |
| Gas requirement and the ‘stopping problem’ | Ergo does not have gas fees, nor the stopping problem, as most computations are done off-chain. They are also cost predictable for on-chain verification and computation |
| High gas fees and network congestion | Ergo is engineered from the ground up with long-term scaling in mind, using the most advanced and well researched tools |
| Node centralization in AWS / Infura | Anyone can run a node on Ergo (similar to Bitcoin), and while the miners may increase block size limit, there are mitigants built in to prevent this from leading to a bad node running experience |
| Censorship: Most blocks are OFAC blocks | Decentralization and PoW is deeply ingrained in Ergo’s ethos and Ergo will resist censorship in any form |
| Centralization of Monetary Policy with Vitalik and Ethereum Foundation able to change emission at their whim | All ERGs were created on day 1 in the genesis block and can only be released to miners per the pre-set emission schedule. Any proposed changes to the emission via hard fork or soft fork requires a supermajority approval of miners. Under NO circumstances can the supply of 97.7 million ERGs ever be increased. |
| Poor security and frequent hacks costing billions | UTXO model and efficient onchain verification with most computation done off chain |
| Poor privacy tools because the Account ledger model is not suitable for attaining high privacy | Combination of the eUTXO model and sigma protocols can achieve optional privacy superior to that achieved by Monero |



## Why Choose Proof-of-Work?

Ergo harnesses the power of the [Autolykos](autolykos.md) Proof-of-Work protocol. 

Designed with a view to democratizing access to the benefits of blockchain technology, Ergo leverages Proof of Work to guarantee the highest levels of decentralization and fairness. Proof of Work, a well-studied and highly secure protocol, is ideal for creating a user-friendly environment, enabling lightweight clients to interact directly with the blockchain without the need for intermediaries.

This feature is critical in the establishment of a truly contractually programmable currency that's accessible and ready to use today.

## Where Can I Find the Roadmap? 

Head over to the 'Roadmap' section [on our website](https://ergoplatform.org/en/ecosystem/#Roadmap) to stay updated with upcoming projects and innovative features Ergo has in the pipeline. You'll also find links there that delve deeper into each roadmap item!

## Who are the People Behind Ergo?

The Ergo team consists of seasoned developers and researchers who boast of a strong academic background with PhDs and multiple publications in fields such as cryptography, compiler theory, blockchain technology, and cryptographic e-cash. They bring substantial hands-on experience in core development for cryptocurrencies and blockchain frameworks such as Nxt, Scorex, and Waves.

Alexander *kushti* Chepurnoy, one of Ergo's notable members, co-founded smartcontract.com (now known as Chainlink), served as a core developer at NXT (the pioneering full PoS blockchain), and was among the first few employees at IOHK where he was a Research Fellow and Team Scorex Manager. 

To know more about the people contributing to Ergo's success, visit Ergo's [Hall of Fame](https://ergoplatform.org/en/hall_of_fame/), you can see more information on the foundation members in the [2022 Transparency Report](ergo-foundation-2022.md)



## Where can I find out more?

Here are some good places to start

- [The Ergo Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)
- Check out the [FAQ](faq.md)
- Read cafebedouin's Article [*Why Ergo*](https://cafebedouin.org/2021/12/09/why-ergo/)
- Come chat to us on:
    - [Matrix]()
    - [Telegram](https://t.me/Ergo_Chats)
    - [Discord](https://discordapp.com/invite/gYrVrjS)
    - [Reddit](https://www.reddit.com/r/ergonauts)
    - [ErgoForum](https://www.ergoforum.org)

                                               
> *"Cryptocurrency should provide tools to enrich ordinary people. Small businesses struggling to make ends meet, not big depersonalised financial capital."*
