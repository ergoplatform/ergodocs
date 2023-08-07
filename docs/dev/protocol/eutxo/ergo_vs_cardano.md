> Please note this is a WIP and may contain inaccuracies. 

# Comparing Ergo and Cardano's eUTXO Models

Ergo and Cardano are two blockchain platforms that have implemented the extended UTXO (eUTXO) model. Despite some differences, both platforms utilize the eUTXO model to offer native asset support and distributed states for decentralized applications (dApps), among other features. In this article, we will explore the key differences between Ergo and Cardano's eUTXO models.


## Languages and Data Storage

Ergo uses a language called [ErgoScript](ergoscript.md), which is inspired by [Scala](scala.md). On the other hand, Cardano employs a language called Plutus, inspired by Haskell. Ergo stores data as [registers](registers.md), while Cardano uses "datum" for data storage. Regardless of these differences, both platforms provide a space within the UTXO to maintain the state of decentralised applications (dApps). Cardano uses a two-layer architecture, with Plutus for smart contracts and Marlowe for financial contracts.

The design of Ergo's scripting language, ErgoScript, facilitates the development of complex smart contracts and advanced features. Cardano's Plutus language is also robust and powerful, but in some cases, certain complex functionalities may require incorporating supplementary components or alternative approaches to implementation.

Here's a comparison of ErgoScript and Plutus (Cardano's smart contract language)

| Feature | ErgoScript (Ergo) | Plutus (Cardano) |
|-----------------------------|---------------------------|---------------------------|
| Language design | Based on Scorex framework, influenced by Scala | Based on Haskell |
| Strongly typed | Yes | Yes |
| First-class functions | Yes | Yes |
| Higher-order functions | Yes | Yes |
| Rich data structures | Registers, boxes | Datum, UTXO |
| Zero-knowledge proofs | Supported | Planned for future development |
| Complex authentication schemes | Supported | Supported |
| Transaction Trees | Supported | Not Supported |

Both Ergo and Cardano's models support non-fungible assets and complex types of representation on the blockchain.

## Minting Policies on Ergo and Cardano

Minting is the process of creating new tokens on a blockchain network, and it is a crucial feature that allows for the creation of native assets, such as NFTs. Both Ergo and Cardano offer native asset support through their respective eUTXO models, but they differ in their approach to minting and issuing tokens.


### Cardano's Minting Policy

Cardano's minting policy defines each native asset with a unique policy ID attached permanently, which stems from the policy script. The policy script defines other attributes, such as the asset's name and amount/value. Asset names are not unique, so Cardano NFTs must be identified by the policy ID, which can be publicly available to differentiate fraudulent/duplicate NFTs from the original tokens. Cardano's minting policy offers a simpler approach to token issuance and is suitable for assets with fewer attributes. It ensures that NFTs are unique and easily identifiable through the policy ID.


### Ergo's Minting Policy

Ergo's minting policy is flexible and supports a wide range of token attributes, making it suitable for complex assets such as NFTs. Developers can create custom policies to define the conditions and rules for creating and managing tokens, including NFTs with various attributes and properties. Ergo's minting policy also supports off-chain data input, which can trigger conditions for transactions to be executed or prevent them from being included in blocks.

Ergo's minting policy is defined by the [Ergo Improvement Proposal (EIP) 0024](eip24.md), which offers two design versions for artwork issuance: V1 and V2. Both designs involve two important boxes in the issuance process: the issuance box and the issuer box. The main difference between V1 and V2 lies in the issuer box.

In V1, the issuer box includes an Int representing 1000 times the royalty percentage of the artwork and the proposition bytes representing the contract to which the royalty percentage will be sent. V1 mainly focuses on handling royalties for the artist or proxy contract.

In V2, the issuer box contains more attributes, such as the artwork standard version, royalty recipients and their respective percentages, artwork traits (Properties, Levels, and Stats), the token ID of the collection, and additional information, such as explicit content. V2 offers more flexibility and features, such as handling multiple royalty recipients and detailed artwork traits. Ergo's minting policy also supports off-chain data input, which can trigger conditions for transactions to be executed or prevent them from being included in blocks.

In terms of tangible examples, Ergo's minting policy allows for more complex NFTs with a wider range of attributes and detailed artwork traits. For instance, NFTs with dynamic or changing attributes could be created using Ergo's minting policy, which is not currently possible on Cardano. 

## Global State

Ergo and Cardano handle global state differently in terms of their scripting languages and transaction validation. Ergo uses ErgoScript, designed as a call-by-value, higher-order functional language without recursion. ErgoScript defines a guarding proposition for a coin as a logic formula that combines predicates over a context and cryptographic statements provable via Σ-protocols with AND, OR, k-out-of-n connectives. 

While ErgoScript is not inherently Turing complete, it is possible to achieve Turing completeness in Ergo by using transaction trees as outlined in this [peer reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf). A transaction tree is a structure where transactions are organized into a tree, with each transaction referencing its parent transaction(s). This allows for complex, multi-step computations to be executed across multiple transactions, effectively making the Ergo platform Turing complete.

By organizing transactions in this way, developers can create more complex and flexible smart contracts on the Ergo platform, similar to those written in Cardano's Plutus language. However, it is important to note that this method requires more manual construction of transaction structures and may not be as intuitive as using a Turing-complete language like Plutus.

Ergo's transaction validation uses the ErgoLikeStateContext trait and [ErgoLikeStateContext](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sdk/shared/src/main/scala/org/ergoplatform/sdk/wallet/protocol/context/ErgoLikeStateContext.scala) case class to represent the blockchain context. The sigmaLastHeaders method provides information about the previous blocks, while the previousStateDigest method provides the UTXO set digest from the last header. The sigmaPreHeader method provides information about the current block being validated.

On the other hand, Cardano uses Plutus, a Turing-complete, higher-order functional programming language subset of Haskell, designed specifically for smart contracts. While ErgoScript focuses on the transactional model and guarding propositions for coins, Plutus provides a more general-purpose language for writing smart contracts.

See these foundational papers for more information. 

- [Improving authenticated dynamic dictionaries, with applications to cryptocurrencies](https://eprint.iacr.org/2016/994.pdf)
- [Self-reproducing Coins as Universal Turing Machine](https://arxiv.org/pdf/1806.10116)
- [Multi-stage Contracts in the UTXO Model](https://ergoplatform.org/docs/paper_26.pdf)
- [EDRAX: A Cryptocurrency with Stateless Transaction Validation](https://eprint.iacr.org/2018/968.pdf)


## Privacy Features
Security and privacy are essential aspects of both Ergo and Cardano's designs. Ergo's cryptographic design, which incorporates the Sigma protocol, provides extensive access to discrete log-based zero-knowledge proofs, offering potential advantages in privacy and security. Zero-knowledge proofs are cryptographic techniques that enable a prover to demonstrate the truth of a statement to a verifier without revealing any additional information. In the context of blockchain technology, zero-knowledge proofs can enhance privacy and security by allowing transactions and smart contracts to be executed without disclosing sensitive data.

Discrete log-based zero-knowledge proofs refer to a class of zero-knowledge proofs that rely on the hardness of the discrete logarithm problem, a foundational concept in modern cryptography. ErgoScript, the scripting language used in Ergo, provides access to Σ-protocols, a subclass of cryptographic proof systems known as non-interactive Σ-protocols. These Σ-protocols include the Schnorr signature scheme and Diffie-Hellman tuple, which can be used to prove knowledge of discrete logarithms. This efficient and flexible implementation of zero-knowledge proofs can improve privacy-enhancing features and applications on the Ergo platform.

Ergo's Sigma Protocols enable the implementation of sophisticated tasks that would otherwise be impossible, risky, or expensive, allowing for self-sovereign application-level privacy. Trustless scripts can access mixers or other functionality without any third parties required. Using Ergo for such applications, users can achieve enhanced privacy and security compared to other platforms.

## Data Inputs

Spending UTXOs is at the core of the extended UTXO smart contract model, and all execution happens when a UTXO is spent. That said, having to spend every single UTXO which you wish to read data from has several strong drawbacks:

- The smart contract of the UTXO with the data must execute, thereby increasing computation complexity/cost.
- The UTXO must be spent, meaning only one tx can use the UTXO data per block/slot.
- Tx fees increase due to needless excess execution & recreation of the output data UTXO.
- Every UTXO which wishes to allow read access through spending must encode the logic directly within their smart contract.
- It is liable to spam attacks by bad actors who wish to wreak havoc on a protocol.
- Increased off-chain complexity in tx creation & finding the latest UTXO.

Thankfully an extremely useful innovation was figured out by the core Ergo developers, Alexander Slesarenko, Alex Chepurnoy, and Dmitry Meshkov.

Rather than forcing all transactions to destroy/spend all inputs as is the norm in historic UTXO-based Blockchains, what if we instead brought in the concept of "*read-only inputs*"? These would allow any transaction to reference any other box(UTXO) currently in the UTXO set and read the data without any problems listed in the previous section.

### Ergo's Data Inputs

Ergo's eUTXO model supports data inputs, which allow transactions to read data from other boxes (UTXOs) without consuming them. This feature enables Ergo to access off-chain data and use oracles, facilitating various applications, such as decentralized finance (DeFi), prediction markets, and data-driven smart contracts. Data inputs can also help minimize transaction fees, as only the necessary boxes are consumed in the transaction process.

### Cardano's Reference Inputs

Cardano introduced reference inputs in the Vasil Hardfork, enabling functionality similar to Ergo's data inputs. In Cardano's eUTXO model, reference inputs allow transactions to access data from other datums without consuming them. This facilitates the integration of off-chain data and oracles into Cardano's smart contracts, expanding the platform's possible applications and use cases.
Collaboration

Ergo and Cardano are pioneers in implementing the extended UTXO (eUTXO) model and have collaborated to advance research and development in this area through the eUTXO Alliance. Cardano’s implementation of data inputs is just one example of how we can work together.

One notable development between the Ergo and Cardano communities is the Rosen Bridge, currently in beta testing. This bridge enables the transfer of wrapped ADA tokens from Cardano to Ergo and vice versa, promoting interoperability and collaboration between the platforms and their communities. Cardano users can access the DeFi ecosystem on Ergo with this bridge using wrapped ADA or native ADA tokens.

Moreover, ErgoMixer, as the only token mixer in the space, enables users to mix wrapped ADA and other native tokens, such as wrapped HOSKY. After mixing the tokens in ErgoMixer, users can bridge them back to Cardano. These native tokens can be used in SigmaFi, SigmaO, or any budding dApps available on sigmaverse.io.

Through these collaborations and developments, Ergo and Cardano can enhance their respective platforms, promote interoperability, and advance the adoption of the eUTXO model in the blockchain community.



## Conclusion

Ergo and Cardano are both innovative blockchain platforms that have implemented the extended UTXO model, offering native asset support, distributed states for decentralized applications, and a range of other features. While ErgoScript and Plutus, their respective scripting languages, have different foundations and design principles, they both enable the creation of sophisticated smart contracts and blockchain applications.

Ergo's approach to minting policies allows for more complex NFTs and token attributes, while Cardano's policy provides a simpler method for token issuance. Both platforms have implemented solutions to access off-chain data and oracles through data inputs, broadening their potential applications and use cases. Furthermore, their collaboration through the eUTXO Alliance and developments like Spectrum, Rosen and Reference Inputs demonstrate the potential for cross-platform cooperation and growth in the blockchain ecosystem.

Ultimately, both Ergo and Cardano offer unique strengths and capabilities, making them appealing choices for developers, users, and investors alike. As these platforms continue to evolve and collaborate, they will undoubtedly contribute significantly to the advancement of blockchain technology and the adoption of the eUTXO model.

## Frequently Asked Questions

### Are Ergo native assets basically the same as Cardano ones?

While Ergo and Cardano both support native assets, their implementations and characteristics may differ. Both blockchains use the eUTXO model, but they have different scripting languages (ErgoScript for Ergo and Plutus for Cardano) and slightly different approaches to data storage, global state management, and minting policies. 

### Is Ergo's multiasset ledger compatible with Cardano's?

Ergo and Cardano's ledger models have similarities due to their shared use of the eUTXO model. However, their ledgers are not directly compatible due to differences in their scripting languages, minting policies, and data handling. 

### Is there an equivalent of CIP25 in Ergo?

- 

### Is there an Ergo equivalent of dbsync?

- [explorer](explorer.md)


### Mithril vs NiPoPoWs

- [NiPoPoW and Mithril](youtube.com/watch?v=tXHids3WAb4) from *PG: Blockchain & Deep Learning* on YouTube