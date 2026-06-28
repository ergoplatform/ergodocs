---
tags:
  - ErgoNames
  - Naming System
  - ENS
  - dApp
owner: docs
last_reviewed: '2026-06-27'
source_repos:
  - repo: ergonames/ergonames-contracts
    branch: main
    paths:
      - README.md
  - repo: ergonames/ergonames-nextjs
    branch: main
    paths:
      - README.md
  - repo: ergonames/sdk
    branch: master
    paths:
      - README.md
  - repo: ergonames/ergonames-services
    branch: master
    paths:
      - sdk/INTEGRATION.md
source_of_truth:
  - https://ergonames.io
  - https://github.com/ergonames/ergonames-contracts
  - https://github.com/ergonames/ergonames-nextjs
  - https://github.com/ergonames/sdk
  - https://github.com/ergonames/ergonames-services/blob/master/sdk/INTEGRATION.md
ia_status: directory
---

# ErgoNames: Decentralized Naming System for Ergo

ErgoNames is a decentralized naming system for the Ergo blockchain. It lets users register human-readable names such as `~yourname` instead of sharing a 51-character wallet address.

ErgoNames is active again and is currently in public beta at [ergonames.io](https://ergonames.io). The beta site supports searching for a name, connecting Nautilus, and registering test names.

/// admonition | Public beta caveats
    type: warning

- Nautilus and a small amount of ERG are required for testing.
- Only names with 8 or more characters are available during beta; shorter and premium names are planned for launch.
- Beta registrations may be reset before mainnet genesis.
- Beta testers receive a one-of-one Beta Tester NFT badge. The badge is intended to carry over and later be burnable for a Founder flair on the name artwork.
- Registration steps are designed to be refundable by the user's own signature if registration cannot complete.
///

## Key Features

- Register human-readable names for Ergo addresses.
- Use names as NFTs held in the user's wallet.
- Resolve a name to an address and an address back to a name.
- Use one payment for lifetime ownership, with no renewals or expiry.
- Test the beta flow with Nautilus and receive a beta badge NFT.
- Report issues directly from the beta site.

ErgoNames is an important project for improving the usability and adoption of the Ergo ecosystem. By providing a user-friendly naming system, it reduces the friction of using Ergo addresses and enables a better overall experience for users.

## Current Status

The current deployment is a public beta. It is intended for testing, not for names with economic value.

The team has stated that the current mainnet beta deployment is a throwaway set of test names and that beta names are planned to be purged at genesis. Contract fixes from recent review findings are expected to land in the same genesis bundle before a funds-at-risk launch or wallet integration.

Subname functionality is not enabled in the beta. Money-moving resolution should use live on-chain owner lookup.

The live bot and API source are not fully represented in the public repositories yet. The team has said they plan to make the deployment reviewable with source snapshots, deployed constants, genesis transaction IDs, and known-good mint/refund fixtures for end-to-end review.

## Wallet and dApp Integration

The `ergonames` SDK is intended for wallet and dApp resolution. It supports `resolveAddress("~name")` for name-to-address lookup and `primaryName(address)` for reverse display labels.

There are two integration paths:

- Public API resolution through the ErgoNames service for lowest-latency lookups.
- `ChainResolver` resolution through a node or explorer, which reads ownership from chain state and is the preferred path for wallets that already depend on their own node or explorer.

For send flows, failed lookup and failed network verification must be treated differently. The SDK returns `null` when a name does not exist, but throws on network or lookup failure; wallets should not send funds when resolution cannot be verified.

During beta, the SDK API surface is expected to remain stable, but launch will use fresh genesis constants. API users should switch automatically when the service updates; direct-chain users should upgrade the SDK or override the launch constants.

## Project Overview

The project is actively being developed by the Ergo community, with contributions from various developers. The core components include:

- **Ergo Contracts**: Smart contracts for registering and managing names on the Ergo blockchain.
- **Off-chain Tools and Libraries**: Tools and libraries for interacting with the naming system off-chain.
- **Wallet and Application Integration**: Integration with Ergo wallets and applications for seamless user experience.

## Get Involved

Test the public beta at [ergonames.io](https://ergonames.io): search for a name, connect Nautilus, and register a beta name. Use the site's issue-reporting flow for bugs and feedback.

- [GitHub Repository](https://github.com/ergonames)
- [Beta Site](https://ergonames.io)
