# Why Ergo?

Ergo is a next-generation Proof of Work smart-contract platform that enables new models of financial interaction, underpinned by a safe and rich scripting language and flexible and powerful Zero-Knowledge proofs. 


## **🔑 Key Objectives**


- **Research-led but real-world-focused:** Ergo draws on ten years of blockchain development, complementing tried and tested principles with the best peer-reviewed academic research into cryptography, consensus models and digital currencies. We start with solid blockchain basics and implement [new and powerful cryptography natively](documents.md).
- **Powerful & Safe**: Ergo provides superior support for real-world financial agreements. Ergo can support versatile dApps that run predictably, with known costs, and don't have any of the dangers of unrestricted functionality. Ergo's [smart contracts](../../dev/scs) allow us to execute wide-ranging tasks and can be Turing complete, but we always know in advance how much the code will cost and whether it will run successfully.
- **Intelligent and Straightforward**: Sigma Protocols [(Σ-Protocols)](sigma.md) are the foundation of Ergo's smart contracts. They allow for a class of efficient zero-knowledge protocols that enable us to implement sophisticated tasks that would otherwise be impossible, risky, or expensive. Welcome to self-sovereign application-level privacy: trustless scripts that can access mixers or other functionality without any third parties required.
- **Secure and Accessible**: Ordinary users who do not run a full node should enjoy the same security benefits as miners. Non-Interactive Proofs of Proof-of-Work [(NIPoPoWs)](nipopows.md) allow us to make and verify transactions with complete confidence without needing the storage, bandwidth and time required to download the full blockchain. As little as 1 MB of data is necessary, meaning you can use any device.

## **🔑 Key Features**

- **[ErgoScript](ergoscript.md)** is the language used to specify the conditions under which currency can be spent which is flexible enough to allow for ring signatures, multi signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.
- **[Sigma Protocols](/dev/scs/sigma) (Σ)** are a type of non-interactive zero-knowledge proof that is composable using simple *AND/OR* logic. 
- **[Multi-stage Contracts](/dev/scs/multi)** In addition to the regular protection offered by using a threshold `m‐of‐n` signature, Ergo also allows specifying the possible recipients of these coins, which may be another contract with similar complex conditions. This *"chaining"* approach enables the implementation of **secure and efficient smart contracts of arbitrary complexity**. 
- **[Non-Interactive Proofs of Proof of Work (NIPoPoWs)](nipopows.md)**  are essential for two reasons: **Light Clients** and Side Chains. Ergo DApps and off-chain protocols may be implemented in a truly decentralised way due to light clients.
- **[Storage Rent](rent.md)** which acts as *on-chain garbage collection* that reduces the problem of blockchain bloat – and even makes it profitable.
- The **[eUTXO](eutxo.md)** model provides superior privacy, scalability and interoperability. 

Most successful public blockchain use cases are related to financial applications. Ergo extends Bitcoin's way of writing contracts by attaching a guard script (together with additional custom data) to every coin. 

**Keeping all this in mind, we expect Ergo's design to be uniquely useful as Contractual Money.**

## Why Proof-of-Work?

Ergo is based on the [Autolykos](autolykos.md) Proof-of-Work protocol. 

Ergo was created for regular people, Proof of Work allows a truly fair start and the highest degree of decentralisation. It's widely studied, has very high-security guarantees and is friendly to light clients meaning you can use the blockchain without third parties.

These are all essential for having useful contractual, programmable money that's ready today.

## Where can I see a Roadmap? 

The roadmap [on our website](https://ergoplatform.org/en/ecosystem/#Roadmap) includes some of the most anticipated projects and features coming to Ergo. (As well as links to read more!)

## What is the team's background?

Ergo was designed and implemented by experienced developers and researchers with publications and PhDs in cryptography, compiler theory, blockchain technology, and cryptographic e-cash. The team has a solid background in core development with cryptocurrencies and blockchain frameworks such as Nxt, Scorex and Waves. 

Alexander' kushti' Chepurnoy was a co-founder of smartcontract.com (now Chainlink), a core developer at NXT (The first full PoS), and one of the first employees at IOHK where he was a Research Fellow and Team Scorex Manager. 

The full team can be seen in Ergo's [Hall of Fame](https://ergoplatform.org/en/hall_of_fame/).

## How was Ergo launched? 

In order to ensure that Ergo had a fair launch and token distribution, the platform did not pursue any initial venture capitalists or deep-pocketed investors. The goal was to resemble Bitcoin as much as possible in this aspect. The only funds that were set aside (through the mining protocol) were allocated for a small treasury to cover essential costs and funding.

The Ergo Foundation is a non-profit foundation dedicated to advancing the adoption of Ergo. The foundation’s treasury is sourced from a small portion of mined blocks during the first 2.5 years from Ergo’s mainnet launch. This allocation amounted to 4,330,791.5 ERGs, or 4.43% of the total supply. 

Additional details on the Ergo Foundation can be found [here](ergo-foundation-2022.md)

> The absence of VC funding for the main protocol early on is a feature not a bug. This motivates the community to take the lead which is the only long-term sustainable decentralized solution.


## What Problems Faced by Bitcoin Does Ergo Solve?

| Problems Faced by Bitcoin | Ergo's Solution |
|---|---|
| Limited smart contract functionality | A rich language (ErgoScript) combined with the eUTXO model, Sigma protocols and transaction chaining (for turing completeness) |
| Unclear network security as the block reward subsidy approaches zero and transaction fees remain low and volatile | More revenue from transaction fees due to DeFi  and higher usage/scalability, storage rent, mining  by subpools of tokens issued on Ergo (providing even more security incentive) |
| Lack of economy around state leading to miners receiving no compensation for holding the UTXO set in high cost memory - this is a big obstacle to scaling |  Storage Rent provides additional rewards  for miners while increasing network security. It also compensates miners for long-term holding of the UTXO set, thus allowing larger state growth and (indirectly) larger block sizes  |
| Inefficient merkle tree data structure leading to inefficient light clients  (Ethereum has the same problem) | AVL trees leading to drastically more efficient light client verification, and thereby allowing the use of commodity hardware to verify transactions. This is also used in Plasma (layer 2 on Ergo built by Getblok.io) |
| Weak and cumbersome optional privacy tools, some of which have been compromised | Sigma protocols enable true peer to peer privacy. ErgoMixer is the only token-mixer that can provide better anonymity than Monero given enough utilisation.  |
| Massive scaling challenges which led  to the ‘Blocksize Wars’ | Decentralized on-chain governance based on extensive research - block size can be increased securely. NiPoPoWs enable light clients with full node security guarantees. Ergo offers more Layer-2 options than Bitcoin.  |

## What Problems Faced by Ethereum Does Ergo Solve?

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


## Where can I find out more?


Here are some good places to start

- Check out the [FAQ](faq.md)
- Read cafebedouin's Article [*Why Ergo*](https://cafebedouin.org/2021/12/09/why-ergo/)
- Come chat to us on:
    - [Telegram](https://t.me/Ergo_Chats)
    - [Discord](https://discordapp.com/invite/gYrVrjS)
    - [Reddit](https://www.reddit.com/r/ergonauts)
    - [ergoforum](https://www.ergoforum.org)


### [The Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)
                                                
> *"Cryptocurrency should provide tools to enrich ordinary people. Small businesses struggling to make ends meet, not big depersonalised financial capital."*
