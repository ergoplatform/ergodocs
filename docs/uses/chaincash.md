# ChainCash - Elastic Peer-to-Peer Money Creation via Trust and Blockchain Assets

[ChainCash](https://github.com/ChainCashLabs) is a decentralized, peer-to-peer monetary system that enables the creation of money through trust and blockchain assets. The system addresses the issue of inelasticity in blockchain asset supply, which often hinders the real-world usage of these assets. ChainCash allows for the elastic creation of money in a self-sovereign way via trust or collateral, with collective backing and individual acceptance.

/// details | Watch the presentation
     {type: info, open: false}
[Chaincash | Ergo Summit - Cypherpunk Finance](https://www.youtube.com/watch?v=NxIlIpO6ZVI)
///

## Overview

In ChainCash, money is considered as a set of digital notes, where each note is collectively backed by all its previous spenders. Every agent (participant) can create reserves to be used as collateral. When an agent spends a note, whether received from another agent or self-created, they attach their signature to it. A note can be redeemed at any time against any of the reserves of the agents who previously signed the note.

ChainCash allows an agent to issue and spend notes without a reserve. It is up to the agent's counter-parties to decide whether to accept and back the issued note with collateral or trust.

### Key Components

1. **Collateral**: Agents lock up collateral (e.g., cryptocurrency or other assets) in a smart contract, which serves as the backing for the notes they issue.

2. **Note Issuance**: Agents can issue digital notes based on their collateral. The elastic money creation process allows for a flexible money supply.

3. **Circulation**: Notes can be transferred between agents in exchange for goods, services, or other assets. Each time a note changes hands, the new holder digitally signs it, indicating their trust in the note.

4. **Acceptance**: When receiving a note, an agent evaluates its credibility based on the signatures of the previous holders and their individual acceptance rules. Widely accepted standards may exist alongside individual rules.

5. **Redemption**: The current holder of a note can redeem it with any of the previous holders for the equivalent value in the agreed-upon unit of account or other assets. However, any agent after the first one in the signatures chain receives a redemption receipt indicating the debt of previous signers before them. They can then redeem the receipt against the reserve of any previous signer, generating a new redeemable receipt. A redemption fee should be paid, incentivizing reserve provision and note usage instead of redemption.

6. **Dynamic Quality**: As a note circulates and accumulates signatures from trusted agents, its perceived credibility and value can increase, even if the original issuer didn't provide full collateral backing.

### Example Scenario

Consider a small gold mining cooperative in Ghana issuing a note backed by tokenized gold. The note is then accepted by the national government as a means of tax payment. The government uses the note (now backed by gold and trust in the Ghana government, making it convertible to Ghanaian Cedi) to buy oil from a Saudi oil company. The oil company, having its own oil reserve, uses the note to buy equipment from China. Now, a Chinese company holds a note backed by gold, oil, and Cedis. It may be challenging for the Chinese company to redeem from the small cooperative in Ghana, so they can redeem from the Ghana government, which in turn may redeem from the cooperative.

### Note Quality Estimation

Each economic agent has an individual note quality estimation predicate Pi(n) that considers the collaterals and trust of previous spenders. Agents may have different collateralization estimation algorithms, whitelists, blacklists, or trust scores assigned to the note's previous spenders. Different agents may analyze the history of a single note, all notes issued by the note's signers, or apply other methods.

In general, the payment sender needs to consult with the receiver to determine if the payment (consisting of one or more notes) can be accepted. However, in practice, standard predicates are likely to emerge, allowing payment receivers (e.g., online shops) to publish their predicate or predicate ID online, enabling payments without prior interaction.

## Blockchain Implementation

ChainCash is implemented on top of the Ergo blockchain and consists of two main components:

1. **On-chain Contracts**: Contracts for notes, reserves, and redemption receipts are implemented on-chain. The most straightforward option is to have all these contracts on-chain. More scalable options, such as having only reserves (and possibly receipts) on-chain while notes circulate off-chain (e.g., on a side-chain or Layer 2 solution), are being considered.

   - The reserve contract locks ERG native tokens on top of the Ergo blockchain and allows for the redemption of native or custom tokens when a note is presented.
   - The note contract ensures that the note has a proper history, with a valid signature from the corresponding reserve owner added on each spend. It also allows for note splitting (payment and change) and redemption.
   - The receipt contract, created during redemption, contains the ownership history copied from the note input and the position of the redeemed reserve in the ownership chain, along with the note's value. The receipt can then be used to redeem against a reserve.

2. **Client Software (ChainCash Server)**: This software, acting as a self-sovereign bank with client-side note validation, interacts with the blockchain (and possibly a side-chain or p2p network for off-chain note circulation) and implements the functionality of an agent, including the note quality estimation predicate Pi(n). The server can track reserves and notes, and its Pi(n) predicate can be configured via whitelists, blacklists, and collateralization requirements provided in the config.

The on-chain contracts ensure the integrity of the notes, reserves, and redemption process. The ChainCash Server allows for individual agent behavior based on its configuration.

## Applications

ChainCash serves as a foundation for various monetary systems, such as:

1. **Local Exchange Trading Systems (LETS)**: Members can whitelist each other to accept notes regardless of backing reserves, enabling the collective creation of money within the community. Implementations may range from LETS members unconditionally whitelisting only notes issued by other members to whitelisting notes ever signed by LETS members. Unlike traditional LETS, ChainCash notes can also easily circulate outside the LETS circle.

2. **Local Currencies**: Local or national governments can issue notes and enforce their acceptance within their jurisdiction. Enforced acceptance rules may vary, similar to the LETS implementation. Local currencies often introduce redemption fees to promote local usage. In ChainCash, this can be achieved by modifying the reserve contract to charge a fee for non-local redemptions or by modifying the note contract to incur a fee when spending to non-local addresses. Demurrage, a concept associated with local currencies, can also be implemented by modifying the note contract. However, modifying the note contract makes the notes less appealing to others, which is common for local currencies.

3. **Multilateral Trade-Credit Set-off**: Multilateral Trade-Credit Set-off is a technique for clearing invoices in closed loops against one another. In ChainCash, mutual debts can be cleared by atomically burning tokens backed by counter-parties in a single transaction, allowing participants to issue more notes afterward.

## New Developments: L1 and L2 Payments

One of the latest advancements in ChainCash involves the development of contracts that allow payments to be executed either on Layer 1 (L1) or Layer 2 (L2), with a unified redemption contract serving both layers. This opens up the possibility for various applications, such as privacy enhancements like mixing. For instance, you could transfer an asset worth the equivalent of a kilogram of gold on L1 for maximum security, or opt for a quicker L2 transaction equivalent to a couple of grams of gold. The unified redemption contract simplifies the process, working seamlessly irrespective of the initial layer of the transaction. Although still in development, this feature is showing promising capabilities for enhancing both security and efficiency.

## Unit of Account: Gold

Inspired by historical peer-to-peer monetary systems such as the WAT system, ChainCash uses gold as its unit of account. One ChainCash token represents approximately one milligram of gold. This system enables users to issue notes of arbitrary values, which may or may not be backed by reserves in various digital tokens or real-world assets.

## Advantages and Drawbacks

Advantages:
- Combines trust and collateral in a unique way for money issuance
- Provides elasticity of supply without enforcing individual users to accept lower quality notes
- Supports the building of various monetary systems on top of it

Drawbacks:
- Notes are non-fungible due to unique backing, which may limit their use in certain DeFi applications (e.g., liquidity pools, lending pools)
- Currently lacks privacy features in payments (this topic is left for further research)

## Conclusion

ChainCash introduces a novel approach to decentralized money creation, combining trust and collateral to enable an elastic money supply. By allowing agents to issue and accept notes based on their individual rules, ChainCash provides a flexible foundation for various monetary systems while maintaining the quality of the currency. Although there are some limitations, such as the non-fungibility of notes and the lack of privacy features, ChainCash offers a promising alternative to traditional centralized currencies and blockchain assets with inelastic supply.

## References

- [Whitepaper](https://github.com/ChainCashLabs/chaincash/blob/master/docs/whitepaper/chaincash.pdf)
- [ergoforum: ChainCash - A Spender Signed Currency on Ergo](https://www.ergoforum.org/t/chaincash-a-spender-signed-currency-on-ergo/4015)
- [The World Needs For More Collateral](https://www.ergoforum.org/t/the-world-needs-for-more-collateral/4451)
- [ChainCash Server](https://github.com/ChainCashLabs/chaincash-rs)
- [ChainCash Server Design Document](https://github.com/ChainCashLabs/chaincash/blob/master/docs/server.md)
- [ChainCash Contracts](https://github.com/ChainCashLabs/chaincash/tree/master/contracts)
- [ChainCash Tests](https://github.com/ChainCashLabs/chaincash/blob/master/src/test/scala/kiosk/ChainCashSpec.scala)