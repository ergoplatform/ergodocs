---
tags:
  - Social
  - Messaging
  - IPFS
  - dApp
  - Experimental
---

# On-chain Social and Messaging Apps

Several experimental social and messaging apps were shared in the January 2026 development log. They use Ergo tokens and client-side apps instead of centralized accounts.

## SIGHT

[SIGHT](https://bafybeia4ysvodk6yiiugukoibfroqysp6z6jsn4zykbwbgotclkdp7z4dy.ipfs.dweb.link/) is a decentralized anonymous reporting dApp.

- Reports are minted as tokens on Ergo and the frontend is hosted on IPFS.
- Token names use `SIGHT-{timestamp}`.
- Metadata is JSON with GPS coordinates, timestamp, tag, and proof-of-work nonce.
- The browser computes client-side proof of work using location, timestamp, and wallet address; readers re-verify the proof and reject invalid reports.
- GPS is truncated to neighborhood level and the app runs in-browser with no account system.

## SAY

[SAY](https://bafybeicooo2vkq3t3x47yvhkgqzdt3ana54xhdpglattqchumkckxc7usu.ipfs.dweb.link) is a P2P social app where posts are tokens.

- Each post is a `SAY-{timestamp}` token minted to the user's wallet.
- Content, timestamp, and address are stored in the token description.
- Anti-spam uses a browser-computed SHA-256 proof of work with 4 leading zeros.
- Feeds verify that each post token is still held by the original minter.
- Profiles use `SAYER` tokens, follows use `SAYFOLLOW` tokens, and ErgoPay enables mobile signing.

## Ephemeral Messenger

[Ephemeral Messenger v1.1](https://bafkreibqyazalnfuw7ojlwtahsjoijgxqv2eq4dcgyfnfc4ati2k4mihbm.ipfs.dweb.link/) is an on-chain self-destructing message dApp.

- Messages are tokens locked in a smart contract with an unlock height in `R7`.
- When the timer expires, anyone can burn the expired message token and claim the locked ERG cleanup reward.
- v1.0 launched with Nautilus only and a weak "vanity" encryption mode that should not be treated as private.
- v1.1 added passcode/passphrase encryption; users must share the passcode out of band.
- The app is a single HTML file using Fleet SDK, Nautilus wallet API, and Ergo node box queries.

## Ergo Wallet Statement

[Ergo Wallet Statement](https://ergo-wallet-statement.vercel.app/) is a wallet reporting tool.

- Shows month-end ERG-equivalent statements back to January 2021.
- Includes wallet distribution, storage rent status, monthly token/NFT/LP breakdowns, transaction activity, and top holdings.
- LP token handling maps 378 active ErgoDEX LP pools to actual pair names.
- Later updates improved T2T/N2T LP pricing, mobile layout, CyberVerse metadata coverage, and planned JSON/CSV/query exports.
