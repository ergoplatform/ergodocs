---
tags:
  - Paideia
  - DAO
  - Staking
  - Governance
  - dApp
  - dApp-Live
---

/// details | DeepWiki Documentation
    {type: info, open: true}
For an alternative and potentially more detailed documentation source generated from the repository, explore the [paideiadao/paideia-app on DeepWiki](https://deepwiki.com/paideiadao/paideia-app)
///



# Paideia
[Paideia](https://www.paideia.im) is a project from the [ergopad](ergopad.md) team whose purpose is to create a functional, secure, and well-documented DAO software suite that supports DAOs as they form and develop. It will make it easy for anyone to initiate a DAO, distribute tokens using various methods, create proposals, and collect votes. It will help various organizations share funds in a secure and fair way.

## Using Paideia
This section will cover how to use Paideia. Alternatively, you can watch [Paideia, Joining Your DAO | One Take Series](https://youtu.be/YUGNLQ6n8BA).

## Prerequisites

1. You'll need an Ergo wallet such as Nautilus to interact with Paideia.
2. Creating a DAO costs 50000 Paideia tokens. Currently to create a DAO, simply reach out to the Paideia team.
3. To create proposals, you'll need to hold at least 500 Paideia tokens in your wallet.

## Getting Started

1. Connect and authenticate your wallet on the Paideia platform using the Connect Wallet button on the top right of the DAO homepage.
2. Once connected, you can create a profile, including a username, short bio, and profile picture.
3. To participate in the DAO, you must then stake the appropriate token for the DAO. This can be done under Staking, then Manage Stake.

## Creating Proposals

1. Ensure you have at least 500 Paideia tokens in your wallet.
2. Navigate to your DAO's page on the Paideia platform and click "Create Proposal".
3. Enter the necessary details about your proposal, including any outputs, as well as the duration, then submit. The dApp connector will ask you to sign the transaction to complete the proposal creation.

## Voting on Proposals
DAO members can vote on active proposals. Check the DAO config for the ammount of Paideia required to vote on a proposal. The Sigmanauts DAO does not require any Paideia to vote. Be aware that there may be a delay before votes are reflected in the UI, and a page refresh may be necessary.

## Staking and Unstaking

You can stake your Paideia tokens! Staking is done through [Paideia](https://app.paideia.im/Paideia/staking). In case of any issues with these functions, try the following:

1. Ensure your wallet is properly synced and connected.
2. Consolidate UTXOs in your wallet using the "Wallet Optimization Tool".
3. Clear browser cache and reconnect your wallet.
4. Reach out to the Paideia team for further assistance.

## Moderation and Spam Prevention

Paideia is developing tools for DAOs to self-moderate their proposals and discussions:

- Creating a proposal will cost a small amount of Paideia tokens to discourage spam.
- DAO members may be assigned different roles based on their token holdings, granting them varying levels of moderation privileges.
- A community thumb up/down system is being considered to hide irrelevant posts.
- Minimum token holding requirements may be implemented for posting comments in the future.

## Development Updates

The Paideia team continues to work hard on improving the platform. Recent updates include:

- Refactoring smart contracts for better code reuse
- Adjusting the staking reward system to allow DAOs to change emission rates
- Implementing generic refund and configuration logic in contracts
- Planning a move to EIP-5 standard for contracts

## Support and Issue Reporting

Please submit any issues directly to the Paideia Discord by opening a support ticket. The link to open a ticket can be found [here](https://discord.gg/jP25DeTC8U) 

If you encounter an error message or unexpected behavior, please capture the console logs (accessible by pressing F12 in most browsers) and share them with the Paideia team to aid in debugging.
