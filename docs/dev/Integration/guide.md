---
tags:
  - Integration
  - Integration Guide
  - Tutorial
---


# Ergo Platform Blockchain Integration Guide

This guide explains every step required to connect software and services to the Ergo blockchain. It keeps all original detail while arranging information in a logical build‑order: **concepts → infrastructure → transactions → operations → reference**. Send questions or suggestions to **[team@ergoplatform.org](mailto:team@ergoplatform.org)** or join the [**`#development` Discord channel**](https://discord.gg/kj7s7nb).

---

## 1. Core Concepts

| Topic                 | Essential facts                                                                                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Transaction Model** | Each transaction spends one‑time “boxes” (UTXOs) and creates new boxes. Examine the full [Ergo Box model](box.md).                                                |
| **Addresses**         | Standard P2PK scripts appear at regular wallets. The [address scheme](address.md) documents every variant.                                                        |
| **Boxes & Registers** | A box stores an ERG amount **and** an optional list of `{tokenId, tokenAmount}` pairs inside typed registers. Details live in the [register guide](registers.md). |
| **Precision**         | Smallest unit = 0.000 000 001 ERG (10⁻⁹ ERG).                                                                                                                     |
| **Block Interval**    | Average block time ≈ 2 minutes.                                                                                                                                   |

---

## 2. Infrastructure & Tooling

### 2.1 Ergo Node

Running an independent node maximises security and performance.

* **Installation** — follow the [node install guide](install.md).
* **Public alternative** — `http://213.239.193.208:9053` (dynamic list at [api.tokenjay.app/peers/list](https://api.tokenjay.app/peers/list)).
* **Disk space** — secure at least **100 GB**.
* **Web panel** — open `127.0.0.1:9053/panel` on main‑net or `127.0.0.1:9052/panel` on [test‑net](testnet.md).
* **Pruned mode** — accelerate sync with a [pruned node snapshot plus NiPoPoWs](pruned-full-node.md).


/// admonition | Swagger
    type: tip
Ergo node offers a REST API accessible via HTTP. The complete API specification, in OpenAPI format, can be found [here](openapi.md). When the node is operational, access the user-friendly Swagger UI at `127.0.0.1:9053/swagger` or experiment with it [here](swagger_api.md). An optional [indexed node API](indexed-node.md) is also available.
///

Major wallet functionalities include:

- Wallet creation (`/wallet/init`) and mnemonic generation
- Wallet restoration (`/wallet/restore`) from mnemonic
- Wallet unlock (`/wallet/unlock`) for transaction signing
- Wallet lock (`/wallet/lock`)
- Sending a simple payment (`/wallet/payment/send`)
- Checking wallet status (`/wallet/status`)
- Deriving a new key according to [EIP-3](eip3.md) (BIP 44 implementation for Ergo) (`/wallet/deriveNextKey`)
- Checking wallet balance (`/wallet/balances`) for all addresses
- Retrieving wallet transactions (`/wallet/transactions`) for all addresses.

##### RPC Documentation

- [Overview](swagger.md)
- [API Spec](openapi.md)
- [Indexed Node](indexed-node.md)
 


### 2.2 Wallet Configuration (for exchanges & pools)

/// admonition | Dust Collection
    type: warning
Wallets that receive continuous micro‑deposits must enable **dust collection**; otherwise transactions will time‑out or exceed the execution‑cost ceiling. The [dust‑collection guide](dust-collection.md) shows you how to automate sweeping, perform manual clean‑ups, and monitor UTXO counts.
///



### 2.3 Explorers & GraphQL Endpoints

Ergo data can be accessed through several public services or directly from an indexed node:

* **Official Explorer (UI + REST)** — [https://explorer.ergoplatform.com](https://explorer.ergoplatform.com)
* **Community Explorer** — [https://ergexplorer.com](https://ergexplorer.com)
* **Community Explorer** — [https://sigmaspace.io](https://sigmaspace.io)
* **Public GraphQL API** — `https://explore.sigmaspace.io/api/graphql`
* **Self‑hosted Indexed Node** — enable indexing via [Indexed Node Setup](indexed-node.md) to expose explorer‑style REST **and** GraphQL endpoints directly from your own node—no separate explorer UI needed (recommended for exchanges & other high‑volume backends).

High‑volume operators should run a private indexed node so queries never depend on external rate limits or third‑party uptime. 

---

## 3. Transactions & Wallet Operations 

Before accepting or returning funds, you’ll need addresses.

The **[Transaction Lifecycle](transaction-lifecycle.md)** section walks through an Ergo transaction step by step:

1. **Generate an address** for incoming funds
2. **Select UTXOs** and build an unsigned transaction
3. **Sign**—via the node wallet or an offline key store
4. **Broadcast** and track confirmations

---

## 4. Protocol Governance & Security Essentials

### 4.1 Forking & Upgrade Mechanisms

| Mode            | Who must upgrade?       | Back‑compatibility          | Typical use                                | More                          |
| --------------- | ----------------------- | --------------------------- | ------------------------------------------ | ----------------------------- |
| **Soft‑fork**   | Miner majority (≥ 90 %) | ✅ old nodes keep syncing    | Protocol tweaks like EIP‑37 re‑emission    | [Soft‑fork](soft-fork.md)     |
| **Velvet‑fork** | Minority of miners      | ✅ 100 % backward compatible | Opt‑in features (e.g., NiPoPoW interlinks) | [Velvet‑fork](velvet-fork.md) |
| **Hard‑fork**   | All nodes               | ❌ split if some stay old    | Only for critical consensus changes        | [Hard‑fork](hard-fork.md)     |

Ergo deliberately keeps hard‑fork risk low by pushing complexity to the application layer and preferring soft‑ or velvet‑forks whenever possible.

### 4.2 51 %‑Attack Resistance

Ergo’s ASIC‑resistant **Autolykos** PoW requires large memory and favours off‑exchange solo mining, making hashrate capture expensive. Diversified pools (see [pools.md](pools.md)) further dilute control.

### 4.3 Storage Rent

Unspent boxes older than ≈ 4 years pay **storage rent** (\~0.14 ERG for a simple box). This recycles lost coins and keeps the UTXO set bounded. Rent rules live in [storage‑rent.md](rent.md).

