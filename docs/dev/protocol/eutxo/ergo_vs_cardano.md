
/// details | DRAFT
     {type: warning, open: true}
This document is a work in progress and may contain inaccuracies.
///

# Comparing Ergo and Cardano's eUTXO Models

Ergo and Cardano are two prominent blockchain platforms that have successfully implemented the extended UTXO (eUTXO) model. Despite their differences, both platforms leverage the eUTXO model to provide native asset support and distributed states for decentralized applications (dApps), among other features. This article aims to elucidate the key differences between Ergo and Cardano's eUTXO models.

## History

Ergo was founded by Alex Chepurnoy (known as "kushti") and Dmitry Meshakov, two respected figures in the decentralized technology space. Alex's expertise, gained from working on projects like NXT and smart-contract.com, before his 'ScoreX' project caught the attention of IOG (Input Output Global), the company behind Cardano and he was hired as Research Fellow and Team Scorex Manager.

However, driven by a shared vision to innovate, Alex and Dmitry decided to pursue an independent path, leaving IOG to create Ergo. They aimed to combine the strengths of the extended UTXO (eUTXO) model with the robustness of Proof-of-Work (PoW).

Central to Ergo's ethos is a fair launch, ensuring a balanced token distribution and preventing wealth concentration. This commitment to fairness has resonated within the Ergo community.

Leveraging their technical expertise, Alex and Dmitry have positioned Ergo at the forefront of innovation by integrating eUTXO with PoW as well as several other novel innovations. This unique framework enables the development of secure, scalable, and efficient decentralized applications.

## Programming Languages and Data Storage

Ergo employs a language known as [ErgoScript](ergoscript.md), which draws inspiration from [Scala](scala.md). Conversely, Cardano uses a language named Plutus, which is inspired by Haskell. Ergo stores data in [registers](registers.md), while Cardano uses *"datum"* for data storage. Despite these differences, both platforms allocate a space within the UTXO to maintain the state of decentralised applications (dApps). Cardano employs a two-layer architecture, utilizing Plutus for smart contracts and Marlowe for financial contracts.

ErgoScript, the scripting language of Ergo, facilitates the development of complex smart contracts and advanced features. Cardano's Plutus language is also robust and powerful, but in some cases, certain complex functionalities may necessitate the incorporation of supplementary components or alternative approaches to implementation.

Here's a comparison of ErgoScript and Plutus (Cardano's smart contract language):

| Feature                         | ErgoScript (Ergo)                                   | Plutus (Cardano)                  |
|---------------------------------|-----------------------------------------------------|-----------------------------------|
| Language design                 | Based on Scorex framework, influenced by Scala      | Based on Haskell                  |
| Strongly typed                  | Yes                                                 | Yes                               |
| First-class functions           | Yes                                                 | Yes                               |
| Higher-order functions          | Yes                                                 | Yes                               |
| Rich data structures            | Registers, boxes                                    | Datum, UTXO                       |
| Zero-knowledge proofs           | Supported                                           | Planned for future development    |
| Complex authentication schemes  | Supported                                           | Supported                         |
| Transaction Trees               | Supported                                           | Not Supported                     |

Both Ergo and Cardano's models support non-fungible assets and complex types of representation on the blockchain.

After compilation, both ErgoScript and Plutus contracts output a JSON representation. For Ergo, this JSON could include the ErgoTree, compile-time constants, and compiler version. Having a standardized JSON output allows transactions to interact with the compiled contracts seamlessly.

For a tangible example, please refer to this [ErgoScript contract](https://gist.github.com/mgpai22/638dcd9efdec5f74113a476175c7ee74) that has been ported to the [Winter Cardano Contracts](https://github.com/zenGate-Global/winter-cardano-contracts) framework.

In this example, the original ErgoScript contract has been adapted to work with the Cardano Contracts framework. The ported contract demonstrates how the logic and functionality of an ErgoScript contract can be translated to the Cardano ecosystem using the Winter framework. This allows developers to leverage their existing knowledge of ErgoScript and apply it to building smart contracts on Cardano.

## Token Minting Policies on Ergo and Cardano

Minting, the process of creating new tokens on a blockchain network, is a critical feature that enables the creation of native assets, such as NFTs. Both Ergo and Cardano offer native asset support through their respective eUTXO models, but their approach to minting and issuing tokens varies.


## Native Tokens on Ergo

Ergo's token issuance is standardized through [EIP4](eip4.md). In Ergo, tokens are stored in the `R2` [register](registers.md) of a [box](box.md).

| Register | Value                               |
|----------|-------------------------------------|
| R0       | Value (in nanoErgs as Base58)      |
| R1       | Protection script (Smart Contract) |
| R2       | Assets (tokens)                    |
| R3       | Creation details                   |
| R4-R9    | Available for custom use           |

Each box can hold multiple tokens, represented as pairs of `tokenId` and `amount`. A single box can hold up to 255 secondary tokens. However, there are some constraints to consider:

- The size of a box cannot exceed 4 kilobytes to ensure efficient storage and processing of token-related data.
- The presence of tokens increases the computational cost of a transaction due to additional calculations required for token-related operations.

Ergo's NFT minting policy is defined by the [Ergo Improvement Proposal (EIP) 0024](eip24.md), which offers two design versions for artwork issuance: V1 and V2.

## Native Tokens on Cardano

Native tokens on Cardano allow for the transacting of multiple assets, including ada and custom tokens, without the need for smart contracts. This feature extends the accounting infrastructure to accommodate various assets. Native tokens are different from non-native tokens that require smart contracts.

Assets on Cardano are uniquely identified by an asset ID, consisting of a policy ID and asset name. Tokens with the same asset ID are fungible. Ada is the principal currency for fees and rewards, while native tokens can be used for payments and transactions.

Cardano's minting policy uniquely identifies each native asset with a permanent policy ID, which originates from the policy script. The policy script further defines other attributes, such as the asset's name and amount/value. Since asset names are not unique, Cardano NFTs must be identified by the policy ID, which can be publicly available to distinguish fraudulent/duplicate NFTs from the original tokens.

A minimum ada value is required to transfer native tokens between addresses. Token bundles organize tokens and are the standard way to represent assets on Cardano.

Minting policies specify the rules for creating and burning tokens, and each asset has a permanent association with a minting policy. The native token lifecycle involves minting, issuing, using, redeeming, and burning tokens, with various actors involved, such as asset controllers, token issuers, and token holders. Tokens can also be reissued by token holders acting as reissuers for trading or liquidity purposes.

## Global State Management

The management of global state in Ergo and Cardano is influenced by their respective scripting languages and transaction validation processes. Ergo utilizes ErgoScript, a call-by-value, higher-order functional language without recursion. ErgoScript defines a guarding proposition for a coin as a logical formula that combines predicates over a context and cryptographic statements provable via Σ-protocols with AND, OR, k-out-of-n connectives. 

Although ErgoScript is not inherently Turing complete, Turing completeness can be achieved in Ergo using transaction trees, as outlined in this [peer reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf). A transaction tree is a structure where transactions are organized into a tree, with each transaction referencing its parent transaction(s). This allows for complex, multi-step computations to be executed across multiple transactions, effectively making Ergo Turing complete.

This organization of transactions enables developers to create more complex and flexible smart contracts on Ergo, similar to those written in Cardano's Plutus language. However, this method requires more manual construction of transaction structures and may not be as intuitive as using a Turing-complete language like Plutus.

Ergo's transaction validation uses the *ErgoLikeStateContext* trait and [ErgoLikeStateContext](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/sdk/shared/src/main/scala/org/ergoplatform/sdk/wallet/protocol/context/ErgoLikeStateContext.scala) case class to represent the blockchain context. The sigmaLastHeaders method provides information about the previous blocks, while the previousStateDigest method provides the UTXO set digest from the last header. The sigmaPreHeader method provides information about the current block being validated.

In contrast, Cardano uses Plutus, a Turing-complete, higher-order functional programming language subset of Haskell, designed specifically for smart contracts. While ErgoScript focuses on the transactional model and guarding propositions for coins, Plutus provides a more general-purpose language for writing smart contracts.

For more information, refer to these foundational papers:

- [Improving authenticated dynamic dictionaries, with applications to cryptocurrencies](https://eprint.iacr.org/2016/994.pdf)
- [Self-reproducing Coins as Universal Turing Machine](https://arxiv.org/pdf/1806.10116)
- [Multi-stage Contracts in the UTXO Model](https://ergoplatform.org/docs/paper_26.pdf)
- [EDRAX: A Cryptocurrency with Stateless Transaction Validation](https://eprint.iacr.org/2018/968.pdf)

## Privacy Features

Ergo's cryptographic design incorporates [Sigma protocols](sigma.md), providing extensive access to discrete log-based zero-knowledge proofs, offering potential advantages in privacy and security. Zero-knowledge proofs are cryptographic techniques that enable a prover to demonstrate the truth of a statement to a verifier without revealing any additional information. In the context of blockchain technology, zero-knowledge proofs can enhance privacy and security by allowing transactions and smart contracts to be executed without disclosing sensitive data.

Discrete log-based zero-knowledge proofs refer to a class of zero-knowledge proofs that rely on the hardness of the discrete logarithm problem, a foundational concept in modern cryptography. ErgoScript, the scripting language used in Ergo, provides access to Σ-protocols, a subclass of cryptographic proof systems known as non-interactive Σ-protocols. These Σ-protocols include the Schnorr signature scheme and Diffie-Hellman tuple, which can be used to prove knowledge of discrete logarithms. This efficient and flexible implementation of zero-knowledge proofs can improve privacy-enhancing features and applications on Ergo.

Ergo's Sigma Protocols enable the implementation of sophisticated tasks that would otherwise be impossible, risky, or expensive, allowing for self-sovereign application-level privacy. Trustless scripts can access mixers or other functionality without any third parties required. Using Ergo for such applications, users can achieve enhanced privacy and security compared to other platforms.

## Data Inputs

Spending UTXOs is at the core of the extended UTXO smart contract model, and all execution happens when a UTXO is spent. However, having to spend every single UTXO which you wish to read data from has several drawbacks:

- The smart contract of the UTXO with the data must execute, thereby increasing computation complexity/cost.
- The UTXO must be spent, meaning only one transaction can use the UTXO data per block/slot.
- Transaction fees increase due to needless excess execution & recreation of the output data UTXO.
- Every UTXO which wishes to allow read access through spending must encode the logic directly within their smart contract.
- It is liable to spam attacks by bad actors who wish to wreak havoc on a protocol.
- Increased off-chain complexity in transaction creation & finding the latest UTXO.

To address these issues, the core Ergo developers, Alexander Slesarenko, Alex Chepurnoy, and Dmitry Meshkov, introduced the concept of "*read-only inputs*". These allow any transaction to reference any other box(UTXO) currently in the UTXO set and read the data without any problems listed in the previous section.

### Ergo's Data Inputs

Ergo's eUTXO model supports data inputs, which allow transactions to read data from other boxes (UTXOs) without consuming them. This feature enables Ergo to access off-chain data and use oracles, facilitating various applications, such as decentralized finance (DeFi), prediction markets, and data-driven smart contracts. Data inputs can also help minimize transaction fees, as only the necessary boxes are consumed in the transaction process.

### Cardano's Reference Inputs

Cardano introduced reference inputs in the Vasil Hardfork, enabling functionality similar to Ergo's data inputs. In Cardano's eUTXO model, reference inputs allow transactions to access data from other datums without consuming them. This facilitates the integration of off-chain data and oracles into Cardano's smart contracts, expanding the platform's possible applications and use cases.

## Collaboration

Ergo and Cardano are pioneers in implementing the extended UTXO (eUTXO) model and have collaborated to advance research and development in this area through the eUTXO Alliance. Cardano's implementation of data inputs is just one example of how we can work together.

One notable development between the Ergo and Cardano communities is [Rosen Bridge](rosen.md), which is currently live. This bridge enables the transfer of wrapped ADA tokens from Cardano to Ergo and vice versa, promoting interoperability and collaboration between the platforms and their communities. Cardano users can now access the DeFi ecosystem on Ergo with this bridge using wrapped ADA or native ADA tokens.

Moreover, ErgoMixer, as the only token mixer in the space, enables users to mix wrapped ADA and other native tokens, such as wrapped HOSKY. After mixing the tokens in ErgoMixer, users can bridge them back to Cardano. These native tokens can be used in SigmaFi, SigmaO, or any budding dApps available on sigmaverse.io.

## Conclusion

Ergo and Cardano are both innovative blockchain platforms that have implemented the extended UTXO model, offering native asset support, distributed states for decentralized applications, and a range of other features. While ErgoScript and Plutus, their respective scripting languages, have different foundations and design principles, they both enable the creation of sophisticated smart contracts and blockchain applications.

Ergo's approach to minting policies allows for more complex NFTs and token attributes, while Cardano's policy provides a simpler method for token issuance. Both platforms have implemented solutions to access off-chain data and oracles through data inputs, broadening their potential applications and use cases. Furthermore, their collaboration through the eUTXO Alliance and developments like Rosen and Reference Inputs demonstrate the potential for cross-platform cooperation and growth in the blockchain ecosystem.

Both Ergo and Cardano offer unique strengths and capabilities, making them appealing choices for developers, users, and investors alike. As these platforms continue to evolve and collaborate, they will undoubtedly contribute significantly to the advancement of blockchain technology and the adoption of the eUTXO model.



## Frequently Asked Questions

### What are the similarities and differences between Ergo and Cardano's native assets?

Ergo and Cardano both support native assets within their respective blockchain ecosystems. They both utilize the eUTXO model, but they employ different scripting languages (Ergo uses ErgoScript, while Cardano uses Plutus) and have distinct approaches to data storage, global state management, and minting policies. 

### Can Ergo's multiasset ledger interact with Cardano's ledger?

While Ergo and Cardano share similarities due to their use of the eUTXO model, their ledgers are not directly interoperable. This is primarily due to differences in their scripting languages, minting policies, and data handling mechanisms. 

### Does Ergo have a feature similar to Cardano's CIP25?

Ergo has a robust set of features and improvements, but as of now, there is no direct equivalent to Cardano's CIP25 in the Ergo ecosystem.

### Does Ergo offer a feature like Cardano's dbsync?

Yes, Ergo provides a similar feature through its [Explorer](explorer.md) tool, which allows users to synchronize and interact with the Ergo blockchain.

### How do Mithril and NiPoPoWs compare in the context of Ergo?

Both Mithril and NiPoPoWs are important concepts in the blockchain space. For a detailed comparison and understanding, you can refer to this [video](https://youtube.com/watch?v=tXHids3WAb4) from *PG: Blockchain & Deep Learning* on YouTube.
