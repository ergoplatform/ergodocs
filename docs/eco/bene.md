---
tags:
  - Bene
  - Fundraising
  - Platform
  - dApp
owner: docs
last_reviewed: '2026-05-30'
source_repos:
  - repo: StabilityNexus/BenefactionPlatform-Ergo
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/StabilityNexus/BenefactionPlatform-Ergo
---

# Bene: Fundraising Platform

## Overview

**Bene: Fundraising Platform** is a decentralized application (dApp) for proof-of-funding campaigns on Ergo. It lets projects raise ERG or another base token through a smart contract, while contributors receive temporary receipt tokens that can later be redeemed for project participation tokens or refunds depending on the campaign outcome.

Bene is designed as a fully client-side application. It does not rely on a central backend or private database; users connect the interface to public Ergo infrastructure and the contract holds the campaign state and funds.

## How it Works

- **Box Creation**: Project owners create a campaign box with the project token supply, deadline, minimum goal, price, owner address, fee settings, and project metadata.
- **Minimum Token Sale**: A minimum amount of tokens must be sold before the project can withdraw funds. This ensures that the project receives sufficient backing.
- **Refund Option**: If the deadline passes before the minimum has been reached, contributors can return their receipt tokens and receive their original funds back.
- **Receipt and Participation Tokens**: Contributors receive an auxiliary project token (APT) as a temporary receipt. If the campaign succeeds, APTs can be exchanged for the real proof-funding token (PFT).
- **Self-Replicating Box**: The main box is self-replicating, meaning that anyone can spend the box as long as they re-create it with the same parameters and add ERGs in exchange for a specified amount of tokens.

## Parameters of a Box

A box created by a project will have the following parameters:

- **Amount of Tokens**: Represents the number of participation tokens available.
- **Deadline (R4)**: The block-height or timestamp deadline used for refund eligibility.
- **Minimum Tokens Sold (R5)**: The minimum amount of tokens that must be sold as required by the contract to enable withdrawals.
- **Counters (R6)**: Tracks sold tokens, refunded tokens, and exchanged receipt tokens.
- **Price (R7)**: The exchange rate for the sale.
- **Immutable Configuration (R8)**: Owner script hash, fee address hash, fee percentage, PFT ID, and optional base token ID.
- **Project Content (R9)**: JSON content with title, description, and other information.

These parameters ensure that the box remains consistent throughout the funding process and allows for transparency in the exchange process.

In addition, the following constants are added:

- **Developer Fee**: The upstream README documents a 5% developer fee.
- **Developer Address**: The address to which it will be sent, specified by its proposition bytes.

## Processes

The Bene: Fundraising Platform supports six main processes:

1. **Box Creation**:
   - Allows anyone to create a box with the specified script and parameters.
   - The box represents the project's request for funds in exchange for a specific amount of tokens.
   - The tokens of the box are provided by the box creator, that is, the project owner.

2. **Token Acquisition**:
   - People should be allowed to exchange ERGs for tokens (at the R7 exchange rate) until there are no more tokens left (even if the deadline has passed).
   - People receive tokens in their own boxes, which can adhere to the standards for tokens, making them visible and transferable through wallets like Nautilus.

3. **Refund Tokens**:
   - People should be allowed to exchange tokens for ERGs (at the R7 exchange rate) if and only if the deadline has passed and the minimum number of tokens has not been sold.
   - This ensures that participants can retrieve their contributions if the funding goal isn't met.

4. **Withdraw ERGs**:
   - Project owners are allowed to withdraw ERGs if and only if the minimum number of tokens has been sold.
   - Project owners can only withdraw to the address specified in R8.

5. **Withdraw Unsold Tokens**:
   - Project owners may withdraw unsold tokens from the contract at any time.
   - Project owners can only withdraw to the address specified in R8.

6. **Add Tokens**:
   - Project owners may add more tokens to the contract at any time.

Bene also integrates an on-chain discussion layer for project comments, using the reputation-systems forum protocol.

## Repository

The repository can be found at: [https://github.com/StabilityNexus/BenefactionPlatform-Ergo](https://github.com/StabilityNexus/BenefactionPlatform-Ergo)
