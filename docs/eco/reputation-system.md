---
tags:

- Reputation System
- Trust
- Decentralized
- dApp
- Celaut
---

# Reputation System

## Introduction

The Reputation System is a core component of [Celaut](celaut.md), providing a decentralized, user-driven mechanism for managing trust. It leverages the immutability of the Ergo blockchain and a UTXO-based model to create auditable, tamper-proof reputation proofs. This system replaces centralized reputation platforms with a transparent and verifiable trust layer for Web3 services, agents, and smart contracts.

* [Sigma Reputation System on GitHub](https://github.com/sigma-rps)
* [Explainer Post on ErgoForum](https://www.ergoforum.org/t/reputation-system/4782)

---

## Why Is This Necessary?

Modern decentralized ecosystems lack a native, trust-based reputation mechanism. Currently, users rely on fragmented sources like social media for trust assessments, which are prone to misinformation and manipulation.

With this system:

1. Trust signals are recorded on-chain and verifiable by anyone.
2. Reputation is subjective and non-consensual; each user can form their own trust graph.
3. Economic incentives are directly tied to reputation quality, ensuring sustainable growth of trustworthy services.

---

## Conceptual Model

The system follows a subjective, non-consensual trust model:

* Alice can trust Bob more than Chris, while Dave might trust Chris more than Bob.
* These relationships are recorded as signed transactions on Ergo, forming a directed graph of trust.

Each trust declaration is stored as a **Reputation Proof** using Ergo’s UTXO model. This ensures immutability and transparency while preserving user control.

---

## Real-World Use Case: Decentralized Marketplaces

In a decentralized version of Airbnb, a host may charge lower prices to guests with higher reputation scores. Unlike centralized platforms, this system allows each host to define their own evaluation criteria—cleanliness, punctuality, or other subjective factors.

---

## Alignment with the [Ergo Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)

* **Decentralization First**: No universal consensus or token is required.
* **Open and Auditable**: All reputation assignments are stored on-chain and verifiable.
* **Accessible to Regular People**: Simple browser-based and programmatic interfaces.
* **Platform for Contractual Money**: Efficiently reduces switching costs by improving trust discovery.
* **Long-Term Focus**: Built to scale with Celaut’s decentralized economy.

---

## System Design

### Reputation Proof Lifecycle

* **Creation**: Generate from scratch or delegate from an existing proof.
* **Delegation**: Assign a portion of reputation to a new proof using Ergo’s metadata fields.
* **Assignment**: Reputation is assigned without transferring tokens, allowing flexible and non-linear trust graphs.

Each Reputation Proof is stored as an Ergo Box, and its associated token represents the amount of assignable reputation.

### Example ErgoScript Smart Contract

```ergo
// Reputation Token Smart Contract
{
  val isOwner = proveDlog(SELF.R7[GroupElement].get)
  val isDelegated = (SELF.tokens.size == 1) && (OUTPUTS(0).tokens.exists { token => 
    token._1 == SELF.tokens(0)._1 
  })
  val canSpend = isOwner && isDelegated && (SELF.R8[Boolean].getOrElse(false))

  sigmaProp(canSpend)
}
```

**Explanation:**

* `R7`: Public key of the proof owner.
* `R8`: Boolean indicating if delegation is allowed.
* Tokens and metadata enforce the constraints on reputation transfer.

This logic ensures:

* Only the rightful owner can modify a proof.
* Reputation can only be delegated to another valid proof.
* Immutable reputation data remains securely linked to the owner’s public key.

---

## Integration with [Celaut](celaut.md)

This reputation system directly powers Celaut’s trust layer:

* **Node and Service Evaluation**: Nodes and services build reputation through on-chain proofs, influencing their ranking and selection.
* **Economic Incentives**: High-reputation services earn more by offering premium access and better positioning in Celaut’s orchestration layer.
* **Delegation and Load Balancing**: Celaut nodes use reputation data to decide whether to execute tasks locally or delegate to trusted peers.

**Example Workflow:**

1. A Celaut user selects a service with a high on-chain reputation.
2. The node executes the service and metering is tracked via smart contracts.
3. Reputation tokens are updated based on performance outcomes.
4. Future clients reference the reputation graph to make informed decisions.

---

## User Interaction

* **Browser Interface**: [Sigma Reputation Panel](https://reputation-systems.github.io/sigma-reputation-panel/) provides a user-friendly interface to browse, assign, and verify reputation records.

* **Library Integration**: Developers can use the [Sigma Reputation Panel Library](https://github.com/reputation-systems/sigma-reputation-panel) to build bots and services that interact directly with the reputation system. This supports automated evaluation, staking, and advanced analytics.

---

## Marketplace Example: Reputation-Based Ratings

In a decentralized Sigma Chains marketplace:

* Bots evaluate product listings, analyze metadata, and provide trust scores.
* Bots invest portions of their reputation tokens when making evaluations.
* Accurate assessments improve a bot’s reputation and earning potential.
* Poor or misleading evaluations result in reputation loss.

Developers can fine-tune bot behavior to prioritize specific attributes, creating diverse evaluation strategies and a healthy competitive environment.

---

## Security Considerations

* **Tamper-Proof Proofs**: Reputation proofs are cryptographically tied to their owners, ensuring no unauthorized changes.
* **Subjective Trust**: Users independently define trust relationships without relying on centralized scoring algorithms.
* **On-Chain Verification**: All reputation data is fully auditable via Ergo’s blockchain.

---

## Conclusion

The Sigma Reputation System establishes a robust, decentralized trust infrastructure for Celaut and the broader Web3 ecosystem. By leveraging Ergo’s blockchain and a flexible, user-defined trust model, it creates a more transparent, secure, and efficient marketplace for services, agents, and smart contracts.
