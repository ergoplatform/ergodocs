---
tags:
  - dApp-InDev
---

# ChainCash

[ChainCash](https://github.com/ChainCashLabs) is a decentralized, peer-to-peer monetary system aimed at creating money collectively through trust and blockchain assets. The system addresses the issue of inelasticity in blockchain asset supply, which hinders the real-world usage of blockchain assets in many cases. ChainCash allows for the elastic creation of money in a decentralized manner while maintaining the quality of the currency.

## ChainCash Explained: A Decentralized Monetary System

ChainCash is an innovative approach to creating and using digital money. It allows participants to issue their own notes, which are backed by collateral and trust. Here's a step-by-step explanation of how it works:

1. **Collateral (Backing the Notes)**: Participants, called agents, lock up some collateral (like cryptocurrency or other assets) in a smart contract. This collateral serves as the backing for the notes they'll issue.

2. **Issuing Notes (Creating Digital Money)**: Based on their collateral, agents can issue digital notes. Each note represents a promise to pay a certain amount of gold (or equivalent value). The gold is used as a stable unit of account.

3. **Circulation (Exchanging Notes)**: Agents can transfer their notes to other participants in exchange for goods, services, or other assets. Each time a note changes hands, the new holder digitally signs it, indicating their trust in the note.

4. **Acceptance (Receiving Notes)**: When an agent receives a note, they evaluate its credibility based on the signatures of the previous holders. If they trust the signers, they're more likely to accept the note as valid payment.

5. **Redemption (Cashing Out)**: At any point, the current holder of a note can redeem it with any of the previous holders. They can ask for the equivalent value of the note in gold or other agreed-upon assets.

6. **Dynamic Quality (Note Reputation)**: As a note circulates and accumulates signatures from trusted agents, its perceived credibility and value can increase, even if the original issuer didn't have full collateral backing.

The key advantages of ChainCash are:

- **Transparency**: The collateral backing the notes is publicly verifiable on the blockchain.
- **Flexibility**: Notes can be issued and endorsed by multiple agents, not just the original issuer.
- **Stability**: By using gold as a unit of account, ChainCash provides a stable measure of value.

In essence, ChainCash is a decentralized monetary system that enables the creation and exchange of digital notes based on collateral, trust, and a golden standard. It offers a flexible and transparent alternative to traditional centralized currencies.


### Creation and Circulation of Digital Notes

In our digital monetary system, we conceptualize money as a collection of digital notes. Each note's value is underpinned by the collective trust and collateral of all previous holders. Here's how it works:


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