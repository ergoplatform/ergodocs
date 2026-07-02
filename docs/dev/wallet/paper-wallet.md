---
owner: docs
last_reviewed: 2026-02-07
source_repos:
  - repo: moon-miner/ergo-paper-wallet
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/moon-miner/ergo-paper-wallet
  - https://ergopaperwallet.vercel.app/
---

# Ergo Paper Wallet

The [Ergo Paper Wallet](https://ergopaperwallet.org/) offers a straightforward and lightweight solution for securely managing tokens within the Ergo ecosystem. As a self-custodial option, it empowers users with full control over their assets. To enhance security, the wallet generation process can be completed entirely offline. Simply download the standalone HTML file from GitHub, disconnect from the internet, and open the file in your web browser to create your wallet.

A February 2026 community fork added optional BIP39 passphrase support and was checked against Satergo for matching seed-plus-passphrase address derivation. Treat the passphrase as part of the wallet secret: the same mnemonic with a different passphrase restores a different wallet.

/// details | Comprehensive Video Guide
    {type: info, open: true}
Discover how to utilize the Ergo Paper Wallet effectively by viewing the detailed video tutorial available [here](https://www.youtube.com/watch?v=0qTasq-nSNw).
///

- [GitHub Repository](https://anon-br.github.io/ergo-paper-wallet/)
- [BIP39 passphrase fork](https://github.com/moon-miner/ergo-paper-wallet)
