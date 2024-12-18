# The Ergo Data Model

This document provides a comprehensive and in-depth exploration of Ergo's unique data model, based on the UTXO (Unspent Transaction Output) model, enhanced with powerful smart contract capabilities (eUTXO).

---

## 1. Theoretical Foundations & Core Concepts

### 1.1 Computational Model Evolution & UTXO vs. Account Model

Ergo represents a significant advancement in blockchain computational models, extending the traditional Unspent Transaction Output (UTXO) paradigm through its enhanced eUTXO (Extended UTXO) model. Unlike conventional blockchain architectures, Ergo's model introduces:

* **Programmable State Transitions**: Enabling complex computational logic within transaction outputs. This contrasts with the account-based model used in other blockchains (like Ethereum), where state is globally mutable. See [UTXO Model Explained](accountveutxo.md) for a comparison of Ergo's model in terms of parallelism, privacy, and scalability.
* **Stateless Verification**: Allowing efficient validation without maintaining complete blockchain state.
* **Deterministic Execution**: Ensuring predictable and verifiable transaction outcomes.

### 1.2 Fundamental Design Principles

1. **Computational Completeness**: Supporting Turing-complete smart contract execution within strict cryptographic constraints.
2. **Cryptographic Composability**: Enabling complex cryptographic protocols through [Sigma Protocols](scs/sigma.md).
3. **Scalable State Management**: Designing a model that supports parallel transaction processing and efficient state verification.

---

## 2. Blockchain Structure: Components and Function

A solid understanding of the blockchain structure lays the groundwork for exploring Ergo’s data model. Ergo blocks contain critical metadata, transactions, and proofs.

### 2.1 Block Components

* [Block Overview](block.md): Comprehensive introduction to block structure in Ergo, detailing how blocks aggregate transactions, references, and proofs.
* [Block Header](block-header.md): Detailed examination of block header components, which include references to previous blocks, difficulty, and other crucial metadata.
* [Block Transactions](block-transactions.md): Understanding how transactions are organized within a block to form the ledger state.
* [AD Proofs](block-adproofs.md): Authenticated Data Proofs enable efficient stateless client verification by providing cryptographic proofs of state transitions.
* [Extension Section](extension-section.md): An exploration of Ergo’s flexible data storage section that can hold additional metadata and information beyond basic transactions.

---

## 3. Boxes: Foundational State Units

At the core of Ergo's data model is the "Box," which is Ergo's implementation and extension of the UTXO (Unspent Transaction Output) concept. While traditional UTXOs simply track unspent coins, Ergo's Boxes enhance this model with additional programmable capabilities.

### 3.1 The Box Concept

A Box is essentially a "smart UTXO" - it serves the same role as a UTXO in tracking unspent value, but extends this with sophisticated computational features. Like a UTXO, a Box is created when value is sent in a transaction and is consumed (spent) when that value is transferred elsewhere. However, Boxes add the following capabilities that go beyond basic UTXOs:

* **Immutable State**: Each box represents an atomic, immutable state unit that cannot be modified after creation. See [Box Lifecycle](lifecycle.md) for details on creation, spending, and destruction.

* **Typed Registers**: Boxes contain 10 [registers](registers.md) (R0-R9) with specific purposes and rich computational potential:
    * R0: Monetary Value (in nanoERGs)
    * R1: Protection Script (Smart Contract)
    * R2: Assets/Tokens
    * R3: Creation Details
    * R4-R9: Flexible, Typed Custom Data Storage
        - Supports multiple data types: `Int`, `Long`, `BigInt`, `GroupElement`, `Coll[Byte]`
        - Can store complex structures and collections
        - Densely packed with type-safe access

* **Programmable Spending Conditions**: Each box specifies precise conditions under which it can be spent, enabling complex logic through ErgoScript. See [Box Modeling](box_modeling.md) and [Box Overview](box.md) for detailed exploration.

By transforming UTXOs from simple value trackers to programmable state containers, Ergo enables more expressive and flexible blockchain interactions while maintaining cryptographic integrity and computational efficiency.



---

## 4. Transactions: Engines of State Change

Transactions define how boxes are created, transformed, and consumed, and are central to Ergo’s dynamic state evolution.

### 4.1 Transaction Foundations

* [Transaction Overview](transactions.md): Fundamental principles of how transactions work in Ergo.
* [Transaction Composition](composing.md): Detailed guide to constructing complex transactions off-chain before submitting them on-chain.
* [Transaction Format](format.md): Technical specification of transaction structure, ensuring interoperability and standardization.

### 4.2 Advanced Transaction Mechanisms

* [Chained Transactions](chained.md): Explore how sequentially dependent transactions can be composed.
* [Merkle Tree in Transactions](tx-merkle.md): Understanding how Merkle trees provide data integrity and facilitate efficient proofs.
* [Transaction Signing](signing.md) and [Backend Signing](sign-tx.md): Cryptographic principles and implementations for authenticating transactions.
* [Transaction Validation](validation.md): Comprehensive overview of on-chain verification processes that ensure correctness and adherence to protocol rules.

### 4.3 Specialized Transaction Features

* [Data Inputs (Read-Only Inputs)](read-only-inputs.md): Access additional data in transactions without spending boxes.
* [Transaction Fees](min-fee.md): Understanding fee structures, ensuring that miners are incentivized.
* [Babel Fees](babel-fees.md) and [Babel Fees Plugin](babel-fleet.md): Innovative mechanisms allowing fees to be paid in alternative tokens.

---

## 5. Assets and Tokens: Powering a Diverse Economy

Ergo supports a rich ecosystem of assets, from fungible tokens to NFTs, enabling complex economic models.

### 5.1 Fungible Tokens

* [Token Basics](tokens.md): Introduction to tokens within the Ergo ecosystem and their fundamental characteristics.
* [Asset Standard (EIP-4)](eip4.md): Standard for creating and managing tokens in Ergo.
* [Token Verification (EIP-21)](eip21.md): Ensuring token authenticity and integrity.

### 5.2 Non-Fungible Tokens (NFTs)

* [NFT Overview](index.md): Comprehensive introduction to NFTs on Ergo.
* [NFT Creation](create.md): Guide to minting NFTs.
* [NFT Versions (V1 vs V2)](v1v2.md): Comparison of different NFT implementation standards.
* [On-Chain NFTs](on-chain.md): Storing NFT data directly on the blockchain.
* [NFT Royalties](royalties.md): Mechanisms for continuous compensation to creators.

### 5.3 Special Token Concepts

* [Perpetual Tokens](perpetual.md): Tokens designed to exist indefinitely.
* [Token Burning](burn.md): Permanently removing tokens from circulation.
* [Singletons](singletons.md): Unique tokens with special properties.
* [Auction Contract (EIP-22)](eip22.md): Standard auction contract implementation details.
* [Artwork Contract (EIP-24)](eip24.md): Specialized standard for managing digital artwork tokens.

---

## 6. Addressing and Identity

Ergo uses an address system that ensures security, privacy, and flexibility.

* [Address Basics](address.md): Fundamental concepts of Ergo addresses, including encoding, format, and usage
* [Address Types](address_types.md): Detailed overview of Pay-to-Public-Key (P2PK), Pay-to-Script-Hash (P2SH), and Pay-to-Script (P2S) address types
* [Address Validation](address_validation.md): Methods and best practices for validating Ergo addresses, including checksum verification and format validation

---

## 7. Payment Standards and Protocols

Ergo defines protocols to streamline user interactions with wallets and applications.

* [ErgoPay Protocol (EIP-20)](eip20.md): Interaction protocol for mobile wallets and dApps.
* [Payment Request URI (EIP-25)](eip25.md): Standard format for payment requests.
* [Proxy Contracts (EIP-17)](eip17.md): Mechanisms to manage funds and logic via intermediary contracts.

---

## 8. Cryptographic Foundations

Ergo’s cryptographic design ensures robust security, privacy, and flexibility.

### 8.1 Sigma Protocols

* [Non-interactive Zero-Knowledge Proofs](nizk.md): Private transaction verification without revealing sensitive data.
* [Flexible Signature Schemes](sigma.md): Supporting multiple signature types.
* [Privacy-Preserving Mechanisms](privacy.md): Advanced features to protect user privacy.

### 8.2 Cryptographic Primitives

* [Discrete Logarithm Proofs](dlog.md): Foundational to signature verification.
* [Ring Signatures](ring.md): Enhanced privacy through signer ambiguity.
* [Threshold Signatures](threshold.md): Enabling multi-party computational scenarios.

---

## 9. Verification, Consensus, and Sustainability

### 9.1 Transaction Validation and Script Execution

Ergo employs a robust, stateless transaction validation approach:

- **Transaction Construction & Signing**: See [Transaction Composition](composing.md), [Transaction Format](format.md), and [Signing](signing.md).
- **On-Chain Verification**: [Transaction Validation](validation.md) and [Merkle Proofs](tx-merkle.md).
- **Script Validation**: Detailed in [Script Validation](script-validation.md) and [ErgoScript Language Specification](ergoscript.md).
- **Execution Environment**: Access blockchain state via [Context Variables](context-variables.md), ensure deterministic [evaluation](evaluation.md), and apply [cost constraints](jitc.md).

### 9.2 Consensus Algorithm & Storage Rent

* **Difficulty Adjustment**: A dynamic mechanism that adjusts mining difficulty every block to maintain a target block time of approximately 2 minutes, ensuring network stability and predictable block creation despite fluctuations in mining power. See [this page](mining/difficulty.md) for technical details.
* **Storage Rent Mechanism**: A novel approach that prevents blockchain bloat and ensures long-term sustainability by requiring users to pay rent for storing data on-chain. See [this page](storage-rent.md) for details on implementation, fees, and economic incentives.

---

## 10. Data Structures and Performance

* [General Data Structures](data-structures.md)
* [Proof of Proof-of-Work (PoPow)](popow.md): Consensus mechanism enhancement for light clients.


### 10.1 Authenticated Data Structures

* [Merkle Trees](merkle-tree.md) for efficient state commitment.
    * [Merkle Batch Proof](merkle-batch-proof.md)
    * [Merkle Extension](merkle-extension.md)
    * [Merkle Light Proof](merkle-light-proof.md)
* [AVL+ Trees](avl.md) for authenticated key-value storage.
* [Interlink Vectors](interlink-vectors.md): Lightweight blockchain verification.
* [AD Proofs](block-adproofs.md): Supporting stateless clients.




### 10.2 Scalability and Efficiency

* Parallel transaction validation inherent in the eUTXO model.
* Stateless validation reduces computational and storage overhead.
* Just-in-time costing ensures resource use is always checked.

For more information see the [scaling](scaling.md) section.

---

## 11. Advanced Concepts: Mastering Ergo's Capabilities

### 11.1 Multi-Stage Transactions

* [Multi-Stage Transactions](multi-stage-txs.md): Understanding how to design and implement complex, multi-step transaction flows.

<!--### 11.2 Data Preservation

* [Data Longevity on Ergo](data-longevity.md): Strategies for ensuring long-term data availability.

### 11.2 Context Variables Revisited

* [Context Variables and Usage](context-variables.md): Deep dive into variables like HEIGHT, SELF, INPUTS, and OUTPUTS.

---

## 12. Development: Building on Ergo

### 12.1 Contract Design Patterns

* [Contract Design Patterns](contract-patterns.md): Best practices and common solutions.

### 12.2 Testing and Debugging

* [Testing Strategies](testing.md): Methods for ensuring reliability and security in Ergo contracts.
* [Debugging Guide](debugging.md): Techniques for identifying and resolving contract issues.

### 12.3 Best Practices

* [Smart Contract Security](ergoscript-security.md): Avoiding common vulnerabilities.
* [ErgoScript Optimization](ergoscript-optimisation.md): Performance improvements for ErgoScript code.

### 12.4 Developer Tools

* [ErgoTool](ergotool.md): Command-line utility for interacting with Ergo.
* [Model Transaction](model-tx.md): Detailed guide to creating and manipulating transaction models.
* [Payments Overview](payments.md): Overview of payment mechanisms and their implementations.

-->