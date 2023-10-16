---
tags:
  - Sidechains
  - NiPoPoWs
---

# Sidechains on Ergo

Ergo's architecture supports the development and implementation of sidechains. This document explores the concept of sidechains, their utility, the use of NiPoPoWs, and a proposed method for two-way pegged sidechains on the Ergo platform.

## What is a Sidechain?

A sidechain is a separate blockchain that connects to another blockchain (usually referred to as the "main chain") via a two-way peg, allowing assets to be interchangeably transferred between the two chains. These sidechains operate independently, which means they can employ different rules, functionality, and use cases than the main chain.

Sidechains are advantageous for various reasons:

- **Experimentation**: They can serve as a platform for testing new features or upgrades before implementing them on the main chain.
- **Scalability**: By offloading transactions from the main chain, sidechains can help improve the performance of the network.
- **Enhanced Functionality**: Sidechains can support features not available on the main chain, such as improved privacy options, different consensus mechanisms, or unique transaction types.

To prevent double-spending attacks and ensure the security of transactions, users must submit a proof of funds when transferring assets to a sidechain.

Some proposed sidechains include:

- [ErgoData](ErgoData.md): A potential sidechain designed to cater to data-intensive applications such as land registries, certificate directories, etc.
- [Proof of Useful Work (PoUW)](pouw.md)


## Non-Interactive Proofs of Proof-of-Work (NiPoPoWs)

[NiPoPoWs](nipopows.md) are cryptographic proofs that enable efficient verification of blockchain data. They are particularly useful for sidechains, allowing these chains to securely connect to the main chain without requiring validators to download and verify the entire main chain's history.

NiPoPoWs function by enabling the compact verification of block headers within a blockchain, negating the need for full blockchain verification. This feature is crucial for the practical deployment of sidechains and is also beneficial for light clients that cannot support the storage requirements of an entire blockchain.

NiPoPoWs facilitate several scalability solutions:

- [**State Channels**](atomic-composability.md#the-eutxo-model-and-ergoscript): By allowing transactions to occur off-chain, state channels alleviate the computational burden on the main chain. NiPoPoWs provide the security mechanism to verify these off-chain transactions.
- [**Light and Thin Clients**](nipopow_nodes.md): Clients with limited storage capacity can use NiPoPoWs to verify specific aspects of the blockchain without the need to store the entire chain.

## Implementing Two-Way Pegged Sidechains on Ergo

In the context of the Ergo platform, we can establish a two-way pegged sidechain by ensuring that the sidechain can interact with the main Ergo chain and recognize its state. This interaction happens through the process described simply below, for a more technical overview please see the [ergohack-sidechain](https://github.com/ross-weir/ergohack-sidechain/tree/main) project. 

1. **Initiating the Transfer**: A user sends a specified amount of ERG (Ergo's native cryptocurrency) to a specific contract on the main chain. This contract locks the funds and allows them to be unlocked only when there's proof of a corresponding deposit in the sidechain.

2. **Sidechain Interaction**: The sidechain contract, recognizing the state of the main chain, issues a corresponding amount of sERG (the sidechain's equivalent of ERG) to the user's address on the sidechain.

3. **Returning to the Main Chain**: The process works in reverse when transferring funds back to the main chain. The user sends sERG to a contract on the sidechain, which burns the tokens and records this transaction. Once the main chain contract recognizes proof of this burn transaction, it releases the corresponding amount of ERG back to the user.

### Security Considerations

The security of this two-way peg relies heavily on the consensus mechanism of the sidechain. The sidechain must maintain a robust and secure method of consensus to prevent double-spending and other types of fraud.

### Data Storage on the Main Chain

For a two-way peg to work, certain data relevant to the sidechain's state needs to be stored on the main chain. This data can include transactions, current UTXO set representations, and other relevant information. This data is crucial for the main chain to verify the authenticity of requests to unlock funds that were previously locked when moving assets to the sidechain.

Ergo's design allows for this data to be stored directly within the blockchain, using either the block's extension section or by creating specific transactions that encode this data.

### Consensus on the Sidechain

The sidechain's progress can be securely recorded on the main chain by embedding a succinct representation of the sidechain's state within the main chain data. This process requires a consensus mechanism ensuring that the data recorded on the main chain is an accurate representation of the sidechain's state. Options for this include Proof-of-Work (merged mining with the Ergo main chain) or other consensus algorithms compatible with the Ergo ecosystem.

## Conclusion and Further Work

Sidechains present a compelling avenue for scalability, enhanced privacy, and experimental features outside the main Ergo chain. Their implementation requires careful consideration of security aspects, particularly concerning the consensus mechanism and the interaction between the main chain and the sidechain. Further work will involve rigorous testing, developing more sophisticated security mechanisms, and exploring additional use cases for sidechains within the Ergo ecosystem.