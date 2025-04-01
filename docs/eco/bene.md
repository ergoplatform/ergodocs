---
tags:
  - Bene
  - Fundraising
  - Platform
  - dApp
---

# Bene: Fundraising Platform

## Overview

**Bene: Fundraising Platform** is a decentralized application (DApp) that enables projects to receive funding in exchange for participation tokens. This DApp allows projects to request ERGs (the native cryptocurrency of the Ergo blockchain) in exchange for participation tokens.

## How it Works

- **Box Creation**: Project owners can create a box that holds an amount of tokens, which may vary, setting a **block limit** as a deadline.
- **Minimum Token Sale**: A minimum amount of tokens must be sold before the project can withdraw funds. This ensures that the project receives sufficient backing.
- **Refund Option**: If the block limit is reached before the minimum amount of tokens are sold, users have the option to exchange their tokens back for the corresponding ERGs, provided the minimum has not been reached.
- **Self-Replicating Box**: The main box is self-replicating, meaning that anyone can spend the box as long as they re-create it with the same parameters and add ERGs in exchange for a specified amount of tokens.

## Parameters of a Box

A box created by a project will have the following parameters:

- **Amount of Tokens**: Represents the number of participation tokens available.
- **Block Limit (R4)**: The block height limit until which withdrawal or refund is allowed.
- **Minimum Tokens Sold (R5)**: The minimum amount of tokens that must be sold as required by the contract to enable withdrawals.
- **Token Sold Counter (R6)**: Token sale counter.
- **ERGs / Token (R7)**: The exchange rate of ERG per token.
- **Withdrawal Address (R8)**: The address where the funds can be withdrawn if the conditions are met, specified by the SHA-256 hash of the proposition bytes.
- **Project Content (R9)**: JSON content with title, description, and other information.

These parameters ensure that the box remains consistent throughout the funding process and allows for transparency in the exchange process.

In addition, the following constants are added:

- **Developer Fee**: The percentage fee for the developers.
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

The current client implementation only supports the creation of a new project and contributions to a project. The contract implementation is complete, although it may undergo corrections.

In addition to the current functionality, a more advanced implementation could include support for other assets beyond ERG. For example, projects could request GAU or other tokens on Ergo. This would provide even more flexibility in terms of the types of contributions a project can receive and enable a broader range of funding options for projects and participants.

## Repository

The repository can be found at: [https://github.com/StabilityNexus/BenefactionPlatform-Ergo](https://github.com/StabilityNexus/BenefactionPlatform-Ergo)
