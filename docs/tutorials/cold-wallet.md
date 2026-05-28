---
title: Cold Wallet Guide
description: How cold storage and cold signing work on Ergo, when to use them, and what risks remain.
tags:
  - wallet
  - security
  - cold-storage
owner: docs
last_reviewed: 2026-05-28
source_repos:
  - repo: ergoplatform/eips
    branch: master
    paths:
      - eip-0019.md
source_of_truth:
  - https://github.com/ergoplatform/eips/tree/master/eip-0019.md
---

# Cold Wallet Guide

A cold wallet keeps private keys on a device that is offline. Use cold storage for long-term holding or higher-value funds where reducing online exposure matters more than convenience.

For basic wallet choice, start with [Get a Wallet](wallets-overview.md). For general safety habits, read [Security Basics](security-basics.md).

## Available Options

| Option | Use when | Start here |
| --- | --- | --- |
| Ergo Mobile Wallet cold mode | You want an offline phone to sign transactions via QR flow. | [Ergo Mobile Wallet](https://ergoplatform.org/en/ergo-wallet-app/) and [EIP-0019](eip19.md) |
| Ledger with Nautilus | You want hardware signing while using a browser wallet for dApps and payments. | [Ledger](ledger.md) and [Nautilus](nautilus.md) |
| Ledger developer stack | You are testing or integrating the current Ergo Ledger app and JavaScript bindings. | [Ledger](ledger.md) and [Hardware Wallet Integration](hardware-wallet-integration.md) |
| Paper wallet | You want offline key generation for deep storage and understand spending risk. | [Paper Wallet](paper-wallet.md) |
| Multisig | You want shared custody or separate signing authority instead of one cold key. | [Multisig](multisig.md) |

## What Cold Means

| Wallet type | Network exposure | Best use |
| --- | --- | --- |
| Hot wallet | Online device holds keys and signs transactions. | Daily use, dApps, small balances. |
| Hardware wallet | Dedicated signing device protects keys. | Higher-value custody with easier spending. |
| Cold wallet | Offline device holds keys and signs without network access. | Long-term storage and reduced online attack surface. |
| Paper wallet | Seed or key material stored offline on paper or metal. | Deep storage only; spending is error-prone. |

Cold storage reduces remote theft risk, but it does not remove backup, physical, phishing, or user-error risk.

## Ergo Cold Signing

Ergo's cold-wallet standard is [EIP-0019](eip19.md). It defines interaction between:

- **Hot wallet**: online device builds and reduces the transaction.
- **Cold wallet**: offline device reviews and signs the reduced transaction.

The usual flow:

1. Hot wallet prepares an unsigned transaction.
2. Hot wallet reduces it using current blockchain context.
3. Hot wallet shows a QR code or transfer file.
4. Cold wallet scans or imports the request.
5. User checks transaction details on the cold device.
6. Cold wallet signs and shows a response QR code or file.
7. Hot wallet scans or imports the signed transaction and broadcasts it.

Private keys stay on the cold device. The online device handles network access and broadcasting.

## Setup Checklist

- Use a clean device dedicated to cold signing.
- Factory reset before setup if reusing a phone or small computer.
- Disable Wi-Fi, Bluetooth, NFC, cellular, and other connectivity before creating or importing keys.
- Create and verify seed backups offline.
- Store backups separately from the device.
- Test with a small amount before moving larger funds.
- Keep written recovery instructions with backups so funds are not lost if the device fails.

## Spending Checklist

- Confirm recipient address on the cold device, not only on the hot device.
- Confirm amount, token, fee, and change address.
- Reject any transaction you do not understand.
- Prefer small test sends when using a new workflow.
- Keep the cold device offline after signing.

## Common Mistakes

- Photographing or cloud-syncing a seed phrase.
- Typing a cold-wallet seed into a website, browser wallet, or support chat.
- Treating a reused online phone as cold without wiping it first.
- Losing the only seed backup.
- Signing blind because the hot wallet screen looks correct.
- Sending all funds before testing recovery and spending.

## Related Pages

- [Get a Wallet](wallets-overview.md)
- [Security Basics](security-basics.md)
- [Ledger](ledger.md)
- [Paper Wallet](paper-wallet.md)
- [Multisig](multisig.md)
- [EIP-0019 Cold Wallet Standard](eip19.md)
