---
tags:
  - Flash Loans
---
# Flash Loans in Ergo's eUTXO Model

Flash loans have emerged as a disruptive yet controversial innovation in the decentralized finance (DeFi) landscape, particularly within Ethereum's account-based blockchain. These loans offer a range of financial utilities but also come with inherent risks. The question at hand is: How compatible are flash loans with Ergo's eUTXO (Extended Unspent Transaction Output) blockchain model? The answer is nuanced and warrants a deep dive into the complexities involved.


## The Multifaceted Utility of Flash Loans

Flash loans are not just arbitrage tools; they serve a broader financial function, including leverage, liquidity provision, self-refinancing, and portfolio rebalancing. However, the DeFi community remains divided over the broader applicability of these features.

> **Community Insight**: The Ergo community has discussed the absence of Atomic Chained Transactions (ACTs). While ACTs would support only static outcomes—limiting the dynamic nature of flash loans—they also offer the advantage of mitigating some of the associated risks.

## The UTXO Model: A Unique Paradigm

The [UTXO model](eutxo.md), first introduced by Bitcoin, operates on a deterministic framework. Unlike [account-based models like Ethereum](accountveutxo.md), transactions in UTXO blockchains use and generate unspent transaction outputs (UTXOs). This deterministic approach ensures a high level of security and predictability, making it an attractive alternative for certain use-cases.

## Determinism and Flash Loans: A Complex Interplay

The deterministic nature of UTXO blockchains presents intriguing challenges for inherently dynamic flash loans, where interdependent contracts often operate within a single transaction. Predicting the final state of all affected UTXOs in real-time DeFi markets can be challenging, but it's not necessarily an insurmountable obstacle.

## Challenges and Potential Solutions in eUTXO Architecture

### Multi-Step Transactions and Multi-Stage Contracts

Flash loans typically involve borrowing, action, and repayment within a single transaction. In eUTXO blockchains, each of these steps would be its own transaction, requiring pre-calculation due to the deterministic nature of the model. However, [Multi-stage contracts](multi.md) offer a workaround by holding interim states and facilitating parallel actions, thereby emulating complex, multi-step processes.

### Inter-Protocol Complexity and Data Inputs

Flash loans often interact with multiple DeFi protocols. In eUTXO systems, this would mean bundling various UTXOs into a single transaction, a task that is complex but not necessarily prohibitive. Ergo's [data inputs](read-only-inputs.md) feature allows transactions to reference existing UTXOs without consuming them. This feature could serve as a potential solution by providing a mechanism to reference multiple protocols within a single transaction. It allows for the creation of complex, interdependent transactions without the need for consuming the UTXOs involved. This could potentially pave the way for more dynamic and flexible transactions, akin to those seen in account-based systems, while still maintaining the security and predictability inherent in the UTXO model.

### Atomicity: Soft Fork and Hard Fork Options

Flash loans in account-based systems are [atomic](atomic-composability.md)—eeither the whole chain of transactions is completed, or none are. This is straightforward in account-based blockchains where multiple interactions can occur within the same block. eUTXO blockchains do not offer such guarantees, making it risky if a multi-step flash loan transaction spans across multiple blocks. However, Ergo developers have discussed the possibility of introducing atomicity through a soft fork, using a special ID context variable to enforce a chain of transactions. Alternatively, a hard fork could also be considered to introduce atomicity, although this would be a more significant change requiring community consensus.

> **Community Insight**: A soft fork could be a less disruptive way to introduce atomicity, although it would add another layer of complexity. The hard fork option, while more significant, would also be a definitive way to address the issue.

## Ethical and Security Implications of Flash Loans

Flash loans have increasingly gained notoriety for their role in exploiting vulnerabilities in decentralized finance (DeFi) protocols, as highlighted in a [2021 research paper](https://arxiv.org/pdf/2003.03810.pdf). While the technology itself is neutral, its impact is a topic of ongoing debate, especially within communities like Ergo that are concerned with both the ethical and security aspects of flash loans.

### Risk Factors and Security Concerns

1. **Isolation Factor**: Traditional financial attacks usually require the attacker to commit their own capital, exposing them to market risks. Flash loans, however, allow attackers to operate in isolation, bypassing the natural countermeasures in market-based security mechanisms.

2. **Absence of Market Counterbalance**: Financial markets usually self-correct, where for every action there is an opposite and equal reaction. For example, a large purchase order is often offset by a large sale. Flash loans upset this natural equilibrium by enabling outsized actions without immediate counterbalance.

3. **Lowered Barriers to Entry**: While highly motivated and capitalized actors can exploit financial systems, flash loans make it easier for a wider array of attackers to engage in malicious activities, thus expanding the attack surface.

4. **Time-Sensitivity**: Flash loans must be borrowed and repaid within a single transaction block, minimizing the time for countermeasures or market corrections to take effect.

5. **Vulnerability of On-Chain Oracles**: Protocols relying on on-chain oracles for real-time price information are especially susceptible. Flash loans can rapidly distort market conditions within a single transaction block, effectively manipulating the oracles upon which these protocols depend.

#### Case Study: Oracle Manipulation Scenario

To better understand the security implications, consider the case outlined in the aforementioned research paper:

In this transaction, an attacker uses a flash loan to borrow 7,500 ETH. They then proceed to convert portions of this amount into sUSD through a series of trades, strategically lowering the sUSD/ETH price as reported by Uniswap and Kyber Reserve—two Automated Market Makers (AMMs) serving as on-chain oracles. The attacker exploits this manipulated price to collateralize an excessive amount of sUSD, ultimately repaying the flash loan and walking away with a substantial profit.

Under normal circumstances, rapid price changes on Uniswap and Kyber would trigger arbitrage bots to correct the market imbalance. This natural market reaction would make such an attack infeasible. However, the time-sensitive nature of flash loans circumvents this safeguard.

#### Potential Mitigations

- Implementing moving averages in on-chain oracles could provide a buffer against sudden price manipulations, making it more difficult for flash loans to exploit short-term market distortions.

### Community Insight

The Ergo community has been actively debating the ethical implications of flash loans. Critics question whether the utility these financial instruments provide justifies the heightened risks they introduce, including the potential to democratize financial malfeasance. Proponents argue that the technology itself is a neutral tool and its ethical implications depend on its application. Nonetheless, the community is divided on whether the benefits of flash loans outweigh the serious ethical and security concerns they present.