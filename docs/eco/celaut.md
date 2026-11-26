---
tags:  
  - Celaut  
  - Nodo  
  - Distributed Systems  
  - Ergo  
  - Reactive Framework  
  - Artificial Economic Intelligence  
  - Service Virtualization  
owner: docs
last_reviewed: 2026-11-26
source_repos:
  - repo: celaut-project/nodo
    branch: stable
    release_watch: true
    paths:
      - README.md
      - docs/CANONICAL_ENCODING.md
      - docs/PRICING.md
      - docs/USAGE.md
  - repo: celaut-project/paradigm
    branch: master
    paths:
      - README.md
  - repo: celaut-project/skills
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/celaut-project/nodo
  - https://github.com/celaut-project/nodo/releases/tag/v2
  - https://github.com/celaut-project/nodo/releases/tag/guest-kernel-v2
  - https://github.com/celaut-project/nodo/pull/239
  - https://github.com/celaut-project/nodo/pull/241
  - https://github.com/celaut-project/nodo/pull/243
  - https://github.com/celaut-project/nodo/pull/266
  - https://github.com/celaut-project/paradigm
  - https://github.com/celaut-project/skills
---

# Celaut

## Overview

[View on GitHub → Celaut Project](https://github.com/celaut-project)

Celaut is a decentralized, peer-to-peer runtime for deploying and coordinating **autonomous services** and **AI agents**. Inspired by **cellular automata**, Celaut decouples *what* a service does from *who* runs it and *where* it executes. This enables a permissionless digital economy where services compete based on verifiable reputation and performance, rather than central control or advertising.

## Recent updates

- `Feb 11` and `Feb 17`: Celaut Node was back in beta testing on Linux sudo and Windows WSL.
- `Apr 1`: Docker was replaced with microVMs, install scripts were improved, and a `doctor` command was added.
- `Apr 9`: Celaut Node was being tested with [Game of Prompts](game-of-prompts.md) before an open competition launch.
- `May 8`: Nodo `v1` shipped a Windows 11 WSL installer. The README now marks local execution and packaging as beta on Linux and Windows, local networking and trustless networking as alpha, and macOS as unsupported.
- `Jul 17`: Nodo `v2` refreshed the Windows 11 WSL release assets. Follow-up source fixes added `iproute2`, systemd startup, and `nodo.service` to the release root filesystem; confirm the current release assets before reinstalling an older WSL image.
- `Aug 14`: Nodo published `guest-kernel-v2`, a pinned guest kernel plus BusyBox userspace for its Cloud Hypervisor microVM path. Install scripts select it through `GUEST_KERNEL_VERSION`; treat this component release separately from the Nodo `v2` application release.
- `Aug 8` to `Aug 14`: Nodo exposed peer payment contracts in its CLI/TUI, replaced UUID-style peer identities with signed public-key identities, and then switched those signatures to Ergo-compatible Schnorr proofs over Blake2b256. These changes break compatibility with older peers and remain pre-production.
- `Aug 11` to `Aug 18`: the old gas model was replaced by per-resource CPU, memory, disk, and network prices. Nodo accounts internally in integer monetary units (MU), while each payment contract declares the MU conversion rate; Ergo is currently the only implemented settlement system. Follow-up fixes aligned quotes with allocated resources and converted balances correctly between peers with different rates.
- `Aug 17`: operator views gained separate peer/client pages, payment and reputation-event histories, counterparties for recorded transactions, and a switch for automatic peer-deposit refills.
- `Nov 26`: the stable Nodo README documents root, service-user, and rootless Linux installation variants, Windows 11 WSL packaging, and alpha status for local/trustless execution and networking; macOS remains unsupported. Its canonical-encoding specification defines deterministic protobuf bytes for service IDs and filesystem messages, with validation at packing, import, service start, and peer retrieval.

---

## Current Operator Interface

The current Nodo README marks its execution/networking surfaces as alpha. The CLI supports non-interactive workflows and structured `--json` results. `nodo execute --no-input` refuses missing required service environment variables; inspect declared variables with `nodo service_envs`. Packaging can run detached and be listed or cancelled, while managed tunnels have explicit lifecycle commands.

`nodo protocol --json` exposes the node's announced protobuf schema and RPCs. Peers are compared through protobuf compatibility rules, rather than requiring identical serialized descriptors. The TUI groups settings under **Policies** and **All**.

`nodo publish` exports a `.celaut.bee` artifact into a GitHub Release of the configured repository. Large artifacts use parts plus a manifest; repeated publication of the same service reuses its release. `nodo download` imports the artifact and recomputes its content-derived service ID. This is artifact distribution, not publication of an executable as source commits.

Resource prices, free-tier budgets, delegation, donations, and reputation remain operator policies. Read the advertised payment method and MU conversion rate; do not infer a fixed settlement value or an unlimited free service from a quote.

### Execution, pricing, and receipts

Nodo's current CLI verifies signed peer offers before using them: quotes are checked against their validity window, price bound, and funding sum. `estimate` reports feasibility, startup cost (including declared initial children), maintenance cost, and the next activity-window close; `execute --for` funds the rounded maintenance periods at the quoted bound, while a quote remains a budget rather than a lifetime guarantee. Delegated execution is accepted only when the local node's advertised charges cover the peer quote after conversion.

The node exposes hash-linked ledger statements for clients, instances, and delegated descendants. Statements identify whether each movement was caused by an operator, client, instance, or node rule; receipt verification checks signatures, counters, closes, and contradictory receipts without needing the daemon database. A close settles the statement and receipt chain; a failed or incomplete chain must not be treated as proof of payment. Descendant funding and estimates include initial child workloads, but peer charges remain measured and reconciled against verified statements.

Resource policy can hibernate an instance when CPU or memory availability reaches the configured condition; hibernation pauses runtime charging while the node records the state, and a funded top-up can resume it. Operators should treat hibernate/stop/refuse as scheduled policy outcomes, not uptime promises. Compatibility updates are gated and migrations are designed to be non-destructive; invite/connect flows can use QR payloads, but peer identity and service/payment validity still require cryptographic verification.

### Canonical service identity

Nodo hashes the canonical bytes of a service specification and its filesystem to derive the service ID. The stable specification uses a restricted protobuf wire encoding: fields are ascending and non-duplicated, varints are shortest-form and unsigned, defaults are omitted unless a field has presence, repeated numeric fields are packed, strings are valid UTF-8, and unsupported protobuf classes/types are refused. This encoding covers identity, not storage indexes, block pointers, compression, or transport. Unknown fields may be forwarded without re-encoding so older nodes do not change an established ID.

The packer, `StartService`, peer `GetService`, and `nodo import` validate the specification; the filesystem content is covered by its content hash, while the block representation is a separate layer. Treat this as current alpha implementation behavior, not a finalized cross-version compatibility guarantee.

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
- Resource use is accounted for by the node and payments are settled through Ergo contracts.
- Developers cannot modify deployed bots post-factum, ensuring integrity.

This creates a transparent ecosystem where bot performance and trust are the sole indicators of value.

---

## System Architecture

### Nodes ([Nodo Implementation](https://github.com/celaut-project/nodo))

- Execute services in containerized sandboxes
- Handle communication, scheduling, and per-resource metering
- Publish metadata such as compute cost, architecture support, and uptime
- Install on Linux with the `stable` branch install script, or use the Windows installer from the current `v2` release.

### Services

The experimental [Celaut Skills registry](https://github.com/celaut-project/skills) indexes problems separately from services that claim to solve them. Its public repository describes on-chain skill, benchmark, result, coverage, service-data, and service-metadata records on Ergo, with competing assertions weighted by reputation. Treat registry entries and benchmarks as claims to evaluate, not as automatic service endorsements.

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
  - Payment contracts advertise how their settlement unit converts to the node's internal MU accounting unit

---

## Resource Pricing and Incentives

- Nodes advertise separate CPU, memory, disk, network, build, tunnel, and resource-modification prices.
- Prices, balances, and charges use integer MU internally. MU has no intrinsic value; each payment contract declares its own `mu_per_unit` conversion rate.
- Ergo is currently the only implemented settlement system and defaults to one MU per nanoERG, but operators can change that rate. Clients and peers must read the advertised contract rate rather than assume a fixed peg.
- Deposit tokens are UUID identifiers for payment requests, not Ergo tokens.
- Nodes can pay peers for delegated execution; cross-peer balances are converted through the matching payment-contract rates.
- Load balancing is guided by resource price, capacity, uptime, and reputation.
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
3. The task is deployed to a Celaut node, which meters the resources it consumes. Users normally operate their own trusted node and may disable incoming execution requests.
4. If optimal, the node delegates execution to a lower-cost peer.
5. The user receives results and optionally updates their trust evaluation.

---

## Celaut is Not a Blockchain

Celaut is an orchestration layer that runs **on top of** blockchains like Ergo. It does not compete with consensus platforms but extends their functionality.

| Component               | On Ergo (On-Chain)                  | On Celaut (Off-Chain)               |
|-------------------------|-------------------------------------|-------------------------------------|
| Service Execution       | ❌                                  | ✅                                   |
| Node Management         | ❌                                  | ✅                                   |
| Resource metering       | ❌                                  | ✅ (within nodes)                    |
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
- [Sigma Reputation System UI](https://reputation-systems.github.io/reputation-system/)

## Linux Installation Permissions

The [current installer guide](https://github.com/celaut-project/nodo#installation) distinguishes root, service-user and current-user installations. Without `sudo`, files live under `~/.local/share/nodo` and the daemon runs as the current user with `CAP_NET_ADMIN`; necessary system steps are shown for approval. Declining those steps leaves work to perform explicitly before rerunning the installer. This is not a promise that host package, subordinate-ID, network or device setup requires no elevated access. The service-user variant keeps the daemon under the selected system user instead of root.
