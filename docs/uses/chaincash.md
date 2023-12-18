---
tags:
  - dApp-InDev
---

# ChainCash

[ChainCash](https://github.com/ChainCashLabs) is a decentralized, peer-to-peer monetary system aimed at creating money collectively through trust and blockchain assets. The system addresses the issue of inelasticity in blockchain asset supply, which hinders the real-world usage of blockchain assets in many cases. ChainCash allows for the elastic creation of money in a decentralized manner while maintaining the quality of the currency.

## Introduction

In our digital monetary system, we conceptualize money as a collection of digital notes. Each note's value is underpinned by the collective trust and collateral of all previous holders. Here's how it works:

### Creation and Circulation of Digital Notes

- **Issuing Notes**: Any participant, referred to as an agent, can create a digital note. This creation can serve as a form of collateral.
- **Spending and Endorsing**: When an agent spends a note, either one received from another agent or self-created, they essentially endorse it with their signature.
- **Redemption**: At any point, a note can be exchanged based on the reserves (collateral) of any agent who has previously signed it.
- **Issuing Without Reserve**: Agents can issue and spend notes even without having reserves. In such cases, the decision to accept the note depends on the trustworthiness and willingness of the counter-party to back the note with their collateral or trust.

### Practical Example

Consider a scenario where a small gold mining cooperative in Ghana issues a digital note, which is backed by their gold reserves (tokenized gold). This note is accepted by the Ghanaian government for tax payments, adding a layer of trust and government backing to the note. The government then uses this note, now backed by gold and trust, to purchase oil from a Saudi company. The Saudi company, with its oil reserves, uses the note to buy equipment from China. Thus, a Chinese company ends up holding a note backed by gold, oil, and the Ghanaian Cedi.

### Quality Estimation of Notes

- **Individual Assessment**: Economic agents evaluate the quality of a note (`Pi(n)`) based on the collaterals and trust associated with its previous owners.
- **Diverse Algorithms**: Different agents might use varied methodologies to assess collateralization. This could include analyzing the history of a specific note (`n`), considering all known notes, or applying different whitelists, blacklists, and trust scores.
- **Standardization and Interaction**: In reality, there's likely to be a standardization of these estimation algorithms. Therefore, a receiver of payment (like an online shop) might publish their specific criteria or algorithm identifier. This allows for payments to be processed without needing prior approval or interaction between the payer and payee.

In summary, ChainCash relies on a unique approach where the value and trustworthiness of digital notes are dynamically shaped by the collective history and credibility of its prior endorsers, creating a fluid and interconnected digital economy.

## New Developments: L1 and L2 Payments

One of the latest advancements in ChainCash involves the development of contracts that allow payments to be executed either on Layer 1 (L1) or Layer 2 (L2), with a unified redemption contract serving both layers. This opens up the possibility for various applications, such as privacy enhancements like mixing. For instance, you could transfer an asset worth the equivalent of a kilogram of gold on L1 for maximum security, or opt for a quicker L2 transaction equivalent to a couple of grams of gold. The unified redemption contract simplifies the process, working seamlessly irrespective of the initial layer of the transaction. Although still in development, this feature is showing promising capabilities for enhancing both security and efficiency.

## Unit of Account: Gold

Inspired by historical peer-to-peer monetary systems such as the WAT system, ChainCash uses gold as its unit of account. One ChainCash token represents approximately one milligram of gold. This system enables users to issue notes of arbitrary values, which may or may not be backed by reserves in various digital tokens or real-world assets.

## Currency Quality and Trust

To maintain the quality of the currency, acceptance of a note depends on the collateral or trust in the issuer. Participants can issue notes without any reserves, allowing for different collateralization levels within various economic circles. As notes circulate, their quality generally improves due to the collective collateral and trust backing them.

## Implementation Details

ChainCash is implemented using two contracts on the Ergo blockchain: one for notes and one for reserves. The off-chain logic can track different note and reserve contracts, support various acceptance predicates and redemption mechanisms, and accommodate complementary currency systems such as Local Exchange Trading Systems (LETS) and local currencies.

Although Layer Two implementation is still under consideration, ChainCash offers a flexible and decentralized monetary system that can potentially cater to different economic agents globally, addressing the limitations of traditional blockchain assets.

## References

- [ergoforum: ChainCash - A Spender Signed Currency on Ergo](https://www.ergoforum.org/t/chaincash-a-spender-signed-currency-on-ergo/4015)