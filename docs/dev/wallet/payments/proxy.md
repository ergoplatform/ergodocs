---
tags:
  - dApp Development
  - EIPs
---

# Proxy Contracts


The idea of proxy contracts came to life with the [Ergo Assembler](https://github.com/anon-real/ergo-assembler) which helped dApp developments like [Ergo Auction House](https://ergoauctions.org/), [ErgoUtils](https://ergoutils.org/), and [SigmaUSD web interface](https://sigmausd.io/#/) despite not having a wallet-bridge like MetaMask (Ethereum wallet) in the ecosystem.

During this time, the structure of proxy contracts evolved as some malicious users tried to take advantage of some minor vulnerabilities, mostly in the [SigmaUSD dApp](https://sigmausd.io/#/).

**Generally, you should ensure your proxy contracts**

- Prevent dApp developers or any other attacker from taking advantage of user's funds in any manner
- Preserve the integrity of the dApp by preventing attacks like the ones explained in the above examples.

For more information please see [EIP-0017](https://github.com/ergoplatform/eips/blob/master/eip-0017.md)