---
tags:  
  - Celaut  
  - Nodo  
  - Distributed Systems  
  - Ergo  
  - Reactive Framework  
  - Artificial Economic Intelligence  
  - Service Virtualization  
---

# Celaut

[View on GitHub → Celaut Project](https://github.com/celaut-project)

Celaut is a decentralized, peer-to-peer runtime for deploying and coordinating **autonomous services** and **AI agents**. Inspired by **cellular automata**, Celaut decouples *what* a service does from *who* runs it and *where* it executes. This enables a permissionless digital economy where services compete based on verifiable reputation and performance, rather than central control or advertising.

---

## Background

Celaut draws from the legacy of **cellular automata** developed by John von Neumann and popularized by Conway’s *Game of Life*. It applies this model to software design: services operate as independent, auditable containers that evolve and interact within a distributed network based on demand, trust, and reputational feedback. There is no execution history directory; anyone is free to submit opinions about any service, putting their own reputation on the line by doing so.

---

## The Need for Celaut

Today's options for using intelligent or cloud services are limited:

1. **Centralized Platforms**
      - Convenient but opaque and censorable
      - No guarantees on behavior, security, or long-term integrity

2. **Self-Hosting Open Source**
      - Transparent but resource-intensive and impractical for most users

Celaut introduces a third path:

- Nodes are decentralized and can dynamically allocate tasks.
- Services are deterministic and isolated inside virtual containers.
- Trust and payment are handled via Ergo smart contracts and the [Reputation System](reputation-system.md).
- No central service registry, no vendor lock-in.

---

## Example: Decentralized Trading Bots

With Celaut:

- Trading bots run as portable services with on-chain reputation.
- Users select them based on past performance and trustworthiness.
- Payments and gas usage are settled on Ergo automatically.
- Developers cannot modify deployed bots post-factum, ensuring integrity.

This creates a transparent ecosystem where bot performance and trust are the sole indicators of value.

---

## System Architecture

### Nodes ([Nodo Implementation](https://github.com/celaut-project/nodo))

- Execute services in containerized sandboxes
- Handle communication, scheduling, and gas metering
- Publish metadata such as compute cost, architecture support, and uptime

### Services

- Stateless and deterministic containers
- May spawn sub-services, forming dynamic, reactive graphs
- Can be hosted, delegated, or migrated across trusted nodes

### Economic Layer on Ergo

- **[Reputation System](reputation-system.md)**
  - Tracks the performance and endorsements of nodes and services based on freely submitted opinions; there is no execution history directory, and anyone may provide feedback at the cost of their own reputation
  - Stored on-chain using immutable reputation tokens
  - Used by clients to decide service selection and delegation paths

- **Payments**
  - Handled via Ergo smart contracts
  - Pay-per-use or subscription models
  - Payments correlate to gas usage and may involve dynamic bidding

---

## Gas Metering and Incentives

- Nodes advertise their price-per-gas and capacity
- Clients buy gas via Ergo transactions; deposit tokens are not Ergo tokens but UUIDs used to identify the payment request inside the node
- Gas is consumed during execution; each node has its own internal gas currency to quantify resource use, which is not a chain token
- Nodes pay Ergo in exchange for gas for each of their peers, allowing them to delegate the execution of services to others if beneficial
- Load balancing is guided by gas efficiency, uptime, and reputation
- Each node has its own balance, service delegation, and pricing policies

---

## Reputation System Integration

Reputation is foundational in Celaut. It enables trust in service orchestration without requiring a consensus layer.

- Each node and service accumulates on-chain reputation proofs
- Reputation reflects peer endorsements and client opinions about services
- Smart contracts enforce immutability of trust data
- Reputation influences pricing, visibility, and delegation priority

The system is described in detail in the [Reputation System](reputation-system.md) documentation.

---

## Real-World Use Cases

- Distributed analytics bots for on-chain/off-chain data
- Autonomous trading agents with verifiable records
- Serverless hosting of decentralized APIs
- Economic simulation engines for DAOs
- AI model marketplaces that reward trust and performance

---

## How Celaut Works in Practice

1. A user needs a specific automated task, such as running a DeFi strategy.
2. They select a service with strong [Reputation System](reputation-system.md) proofs.
3. The task is deployed to a Celaut node, which consumes gas.  (take into account that the correct way to operate is that every user has it's own celaut node, because he can trust on it more than the others. Nodes can be close to external execution requests).
4. If optimal, the node delegates execution to a lower-cost peer.
5. The user receives results and optionally updates their trust evaluation.

---

## Celaut is Not a Blockchain

Celaut is an orchestration layer that runs **on top of** blockchains like Ergo. It does not compete with consensus platforms but extends their functionality.

| Component               | On Ergo (On-Chain)                  | On Celaut (Off-Chain)               |
|-------------------------|-------------------------------------|-------------------------------------|
| Service Execution       | ❌                                  | ✅                                   |
| Node Management         | ❌                                  | ✅                                   |
| Gas Metering & Tracking | ✅ (via smart contracts)             | ✅ (within nodes)                    |
| Payments & Licensing    | ✅ (settled on Ergo)                 | ❌                                   |
| Reputation System       | ✅ (reputation tokens and contracts) | ✅ (used in service orchestration)   |
| Service Metadata        | ✅ (optional, for transparency)      | ✅ (mandatory for operations)        |
| Delegation Decisions    | ❌                                  | ✅ (based on cost and reputation)    |

---

## Further Resources

- [Celaut GitHub Repositories](https://github.com/celaut-project)
  - [Nodo: Execution Engine](https://github.com/celaut-project/nodo)
  - [Paradigm: Theoretical Layer](https://github.com/celaut-project/paradigm)
  - [Celaut Docs](https://github.com/celaut-project/docs)
- [Celaut vs / + Netnotes](celaut_v_netnotes.md)
- [Reputation System](reputation-system.md): Architecture, smart contracts, and usage
- [Sigma Reputation Panel UI](https://reputation-systems.github.io/sigma-reputation-panel/)
