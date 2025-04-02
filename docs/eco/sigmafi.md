---
tags:
  - SigmaFi
  - DeFi
  - Bonds
  - Lending
  - P2P
  - dApp
  - dApp-Live
---

# SigmaFi 

[SigmaFi](https://sigmafi.app/) is a P2P DeFi bond market that is currently live and open-source. 

SigmaFi enables any Ergo wallet holder to request a loan, specifying the loan amount, term, and interest. The loans are guaranteed by collateral, which the lender can claim if the loan is not repaid by the end of the term. Due to the volatility of cryptocurrencies, loans need to be over-collateralized to get funded. For instance, a loan of 100 SigUSD might require ERG worth 150 SigUSD as collateral.

Each new loan request generates a smart contract that outlines the loan terms. This contract holds the collateral and offers the loan on the SigmaFi website. If a user agrees to the loan terms, they can lend the money via the website. The requester then receives the loan, and the lender is either repaid with interest or claims the collateral.

SigmaFi exemplifies decentralized finance (DeFi), facilitating the creation and funding of loan requests directly between individuals, without the need for banks or other intermediaries.

The platform utilizes the extended unspent transaction output (eUTXO) model to create these loans. All SigmaFi contracts are open-source, providing a foundation for developers to build upon. SigmaFi implements various real-world financial instruments and agreements, encouraging developers to learn from and enhance DeFi applications in the Ergo ecosystem.

## Resources

- [Telegram](https://t.me/sigmafi)
- [Documentation](https://sigmafi.gitbook.io/sigmafi-docs/)
- [Contracts](https://github.com/K-Singh/Sigma-Finance)
- [User Interface](https://github.com/capt-nemo429/sigmafi-ui)
- [Off-chain Plugins](https://github.com/capt-nemo429/sigmafi-ui/blob/main/src/offchain/plugins.ts)
