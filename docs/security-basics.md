---
title: Security Basics
description: Basic safety checklist for using Ergo wallets, dApps, bridges, and signing flows.
tags:
  - start
  - security
  - wallet
owner: docs
last_reviewed: 2026-05-27
---

# Security Basics

Use this checklist before holding funds, connecting to dApps, signing messages, or using bridges.

## Wallet Safety

- Write your seed phrase offline.
- Never type your seed phrase into websites, chat messages, screenshots, or support forms.
- Keep backup copies away from networked devices.
- Verify receiving addresses before sending.
- Send a small test transaction before moving large amounts.
- Keep wallet software updated from official sources.
- Advanced users handling sensitive local input can review external tools such as [NoteDaemon](https://github.com/networkspore/NoteDaemon), which experiments with exclusive input-device access on Linux. This is not Ergo-specific wallet software; verify its threat model before use.

## dApp and Signing Safety

- Read wallet prompts before signing.
- Check the site URL before connecting a browser wallet.
- Disconnect wallets from dApps you no longer use.
- Treat message signing as an authorization action, not a harmless click.
- Avoid signing transactions you do not understand.

## Bridge and DeFi Safety

- Confirm the network, token, amount, and destination address.
- Understand bridge timing, fees, and failure modes before sending.
- Check liquidity and slippage before swaps.
- Understand impermanent loss before providing liquidity.
- Be careful with unofficial support accounts and private messages.

## If Something Breaks

| Problem | Start here |
| --- | --- |
| Wallet will not load or connect | [Access Issues](tutorials/access-issues.md) |
| Need offline storage | [Cold Wallet Guide](tutorials/cold-wallet.md) |
| Need hardware-wallet flow | [Ledger](dev/wallet/payments/ledger.md) |
| Need to verify a signed message | [Message Signing](tutorials/message-signing.md) |
| Need bridge help | [Rosen Troubleshooting](eco/rosen/rosen-troubleshooting.md) |
