---
tags:
  - ecosystem
  - privacy
  - navigation
owner: docs
last_reviewed: '2026-05-31'
---

# Privacy

Privacy on Ergo is broader than ErgoMixer. This hub collects live tools, proof-of-concept protocols, user-facing guides, and technical foundations without adding every privacy-related page to the sidebar.

Some entries below are not listed directly in the sidebar because they are research notes, proof-of-concept pages, historical projects, or cross-section references. They remain discoverable here and in the full project directory.

## Tools & Projects

| Page | Status | What you'll find |
| --- | --- |
| [ErgoMixer](ergomixer/index.md) | Live / runnable | Non-custodial mixing, Android guide, safety notes, identifiability notes, FAQ, and token page. |
| [SigmaJoin](../../../eco/sigmajoin.md) | Proof of concept | Research protocol for outsourced, non-interactive mixing based on ZeroJoin ideas. |
| [SCypher](../../../eco/scypher.md) | Unverified project | Blockchain-hosted seed phrase encryption and recovery utility; security/privacy-adjacent rather than a transaction privacy tool. |

## User-Facing Privacy

| Page | What you'll find |
| --- | --- |
| [Privacy Tools](../../../uses/mixer.md) | User-facing overview of Ergo privacy tools and safety notes. |
| [Stealth Addresses](../../../uses/stealth-address.md) | Recipient privacy through one-time payment addresses. |
| [Zero-Knowledge Treasury](../../../uses/zkt.md) | User-facing explanation of anonymous joint signatures and treasury-style coordination. |
| [Mixicles](../../../uses/mixicles.md) | Private contract pattern using oracle data and smart contracts. |

## Technical Foundations

| Page | What you'll find |
| --- | --- |
| [ZeroJoin](../../../dev/crypto/zerojoin.md) | Technical explanation of the ZeroJoin mixing design used by Ergo privacy tooling. |
| [Zero-Knowledge Proofs](../../../dev/protocol/zkp.md) | Conceptual overview of Sigma protocols, optional privacy, and zero-knowledge proofs on Ergo. |
| [Non-Interactive ZK](../../../dev/data-model/nizk.md) | NIZK background and Ergo-specific proof types. |
| [Ring Signatures](../../../dev/data-model/ring.md) | Privacy-preserving signer ambiguity and its role in mixer-style designs. |

## Developer Patterns

| Page | What you'll find |
| --- | --- |
| [Privacy Contract Patterns](../../../dev/contracts/contracts-privacy.md) | Index for privacy-oriented contract patterns. |
| [Stealth Address Pattern](../../../dev/contracts/pattern-stealth-address.md) | Developer implementation notes for one-time address derivation, wallet scanning, and integration concerns. |
