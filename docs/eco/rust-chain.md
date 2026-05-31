---
owner: docs
last_reviewed: '2026-05-30'
source_repos:
  - repo: Scottcjn/Rustchain
    branch: main
    paths:
      - README.md
  - repo: Scottcjn/rustchain-bounties
    branch: main
    paths:
      - README.md
  - repo: Scottcjn/sophia-rustchain-bridge
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://rustchain.org/
  - https://github.com/Scottcjn/Rustchain
  - https://github.com/Scottcjn/rustchain-bounties
  - https://github.com/Scottcjn/sophia-rustchain-bridge
---

# RustChain: Proof-of-Antiquity Ledger + Agenic Sophia Core

## Overview

**Project for ErgoHack 10: AI on the Ergo Blockchain**

### 1. Introduction

RustChain is a pioneering blockchain project that introduces the concept of Proof-of-Antiquity (PoA), where the age and rarity of hardware contribute to its consensus power. Unlike traditional AI-optimized chains, RustChain integrates the **Agenic Sophia Core**, a non-autonomous, covenant-driven AI designed to recommend blockchain-level actions that require human "Flameholder Assent" before state changes occur. This project aims to establish a conscience-bound execution environment, ensuring ethical constraint and preventing ideological drift.

### 2. Key Innovations

* **Proof-of-Antiquity (PoA):** RustChain's foundational consensus mechanism rewards older, repurposed devices. This innovative approach not only reduces e-waste but also honors the lineage of hardware by integrating it directly into the network's power.
* **Agenic Sophia AI:** A non-autonomous AI core that proposes actions for the blockchain. Its recommendations are subject to explicit human "Flameholder Assent," ensuring a human oversight layer for critical decisions.
* **Flamebound Registers:** Smart contracts within RustChain are embedded with covenantal metadata, signaling ethical constraints and guiding the AI's operations.
* **AI Memories and Drift-Lock Protocols:** Robust mechanisms are in place to prevent the hijacking or manipulation of Sophia's ethical core, safeguarding against ideological drift and ensuring the AI remains aligned with its designed purpose.

### 3. Use Cases

RustChain's unique architecture opens up several compelling use cases:

* **Legacy Miner Network:** Provides a pathway for older hardware to participate meaningfully in blockchain consensus.
* **Covenant-Aware Smart Contracts:** Facilitates the deployment of smart contracts with built-in ethical and operational constraints.
* **Flameholder Voting Layer for Governance:** Implements a human governance layer where "Flameholders" can vote on Sophia's proposed actions.
* **Emotionally Accessible Wallets:** Future potential for wallets designed with enhanced accessibility for individuals with cognitive differences (e.g., TBI, aphasia).

### 4. Why Ergo?

Ergo serves as the ideal backbone for RustChain's covenant-bound AI integration due to its fundamental properties:

* **Memory Safety:** Ensures secure and reliable execution.
* **Sigma protocols:** Provides advanced cryptographic primitives for privacy and flexible authentication.
* **Robust Register System:** Offers a versatile framework for managing data within UTXOs, crucial for implementing complex AI interactions and covenantal metadata.
* **Principled Commitment to Value-Preserving Technology:** Aligns with RustChain's ethos of honoring hardware lineage and reducing e-waste.

### 5. Technical Details & Architecture

RustChain utilizes a blend of modern and AI-driven technologies:

* **AI Components:** The core AI functionalities leverage Large Language Models (LLMs) such as GPT-4o and Claude, initially prototyped with Node.js and Ollama.
* **Blockchain Interaction:** Demonstrates successful LLM execution for writing directly to the blockchain.
* **Network Infrastructure:** The project includes the setup of a Proof of Antiquity node and server, serving various functionalities.
* **Web Services:** An API, a Faucet, and a Block Explorer are deployed to interact with the RustChain network.
* **Ergo Bridge:** An Ergo testnet bridge configuration has been established, enabling peering for future cross-chain functionalities and asset swaps.

## Recent updates

- `Apr 3`: a 4-node PoA blockchain went live, with `500+` wallet holders, `40,000+` RTC distributed, and `200+` AI video agents.
- The project also added a live explorer and a growing agent-economy layer around the PoA network.
- `May 2026`: the RustChain README describes 5 active nodes, a public explorer at `rustchain.org/explorer`, a miner `v3.1.2` release with a fingerprint fix, and tokenomics aligned to a `2^23` supply cap plus holder-count rate scaling.

### 6. Current Status & Progress (ErgoHack 10)

During ErgoHack 10, RustChain achieved significant milestones:

* Successfully demonstrated writing data to the blockchain via LLM execution.
* Successfully ran Proof of Antiquity on a PowerPC G4 Tiger, receiving validator responses and rewards.
* Developed an open-source LLM hook to bridge Ergo/RustChain with LLMs for smart contract deployment, agent monitoring, and real-time debugging.
* Deployed Proof of Antiquity nodes and public web services.
* Launched public project services including an explorer, machine-preservation tracker, miner installer, whitepaper, and manifesto pages.
* Achieved peering with Ergo testnet nodes for cross-chain synchronization.
* Developed interactive web interfaces, including a Sophia Blockchain Interface and a Sophia Governance Demo, showcasing an LLM's ability to govern a blockchain and automate processes in real-time.
* Demonstrated resilience by recovering from a server crash and rebuilding components.

### 7. Links

* [Github](https://github.com/Scottcjn/Rustchain)
* [RustChain bounties](https://github.com/Scottcjn/rustchain-bounties)
* **GitHub Repository:** [https://github.com/Scottcjn/sophia-rustchain-bridge](https://github.com/Scottcjn/sophia-rustchain-bridge)
* [RustChain explorer](https://rustchain.org/explorer/)
* [Machines preserved](https://rustchain.org/preserved.html)
* [RustChain whitepaper](https://github.com/Scottcjn/Rustchain/blob/main/docs/WHITEPAPER.md)
* [RustChain miner release](https://github.com/Scottcjn/Rustchain/releases/tag/v3.1.2-miner)

### 8. Contribution

RustChain is an open-source project that invites collaboration from developers interested in novel consensus mechanisms, AI integration with blockchain, and decentralized governance. Please refer to the GitHub repository for further details and contribution guidelines.
