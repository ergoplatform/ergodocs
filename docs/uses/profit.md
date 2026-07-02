---
owner: docs
last_reviewed: '2026-07-02'
source_repos:
  - repo: mhssamadani/ErgoProfitSharingDapp
    branch: master
    paths:
      - README.md
source_of_truth:
  - https://github.com/mhssamadani/ErgoProfitSharingDapp
  - https://github.com/profit-sharing
ia_status: directory
---

# ErgoProfitSharingDapp

ErgoProfitSharingDapp is a historical contract-design example for distributing a dApp's collected income among token holders. It is not an ERG staking product and does not imply guaranteed yield.

The original proposal used ErgoMixer as an example: a project could issue a stakeholder token, let holders lock that token in a contract, and distribute eligible project income in proportion to the locked token amount. The repository describes distribution, staking, config, locker, reserved-token, and income contracts for this flow.

/// admonition | Risk note
    type: warning

Revenue sharing depends on the external dApp actually producing distributable income, the contract implementation being correct, enough liquidity for exits, and users understanding the token they lock. Treat any "profit" display as a calculation to verify, not a promise of returns.
///

The original README now points readers to the `profit-sharing` GitHub organization for the working dApp code, but those frontend/backend repositories have not seen recent public activity. Use this page as a pattern reference, not as current deployment guidance.

- [A solution for staking](https://www.ergoforum.org/t/a-solution-for-staking/1057)
- [Ergo Profit Sharing dApp](https://github.com/mhssamadani/ErgoProfitSharingDapp)
- [Profit Sharing GitHub organization](https://github.com/profit-sharing)
