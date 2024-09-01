# ChainCash - Elastic Peer-to-Peer Money Creation via Trust and Blockchain Assets

[ChainCash](https://github.com/ChainCashLabs) is a decentralized, peer-to-peer monetary system that enables the creation of money through trust and blockchain assets. The system addresses the issue of inelasticity in blockchain asset supply, which often hinders the real-world usage of these assets. ChainCash allows for the elastic creation of money in a self-sovereign way via trust or collateral, with collective backing and individual acceptance.

/// details | Watch the presentation
     {type: info, open: false}
[Chaincash | Ergo Summit - Cypherpunk Finance](https://www.youtube.com/watch?v=NxIlIpO6ZVI)
///


## Overview

ChainCash defines money as a set of digital notes, where each note is collectively backed by all its previous spenders. Every participant, or agent, can create reserves to be used as collateral. When an agent spends a note, whether received from another agent or self-created, they attach their signature to it. A note can be redeemed at any time against any of the reserves of the agents who previously signed the note.

ChainCash allows an agent to issue and spend notes without a reserve. It is up to the agent's counter-parties to decide whether to accept and back the issued note with collateral or trust.

### Key Components

1. **Collateral**: Agents lock up collateral (e.g., cryptocurrency or other assets) in a smart contract, which serves as the backing for the notes they issue. This provides a flexible, decentralized foundation for money creation.

2. **Note Issuance**: Agents can issue digital notes based on their collateral. The elastic money creation process allows for a flexible money supply, adapting to the needs of the economy.

3. **Circulation**: Notes can be transferred between agents in exchange for goods, services, or other assets. Each time a note changes hands, the new holder digitally signs it, indicating their trust in the note.

4. **Acceptance**: When receiving a note, an agent evaluates its credibility based on the signatures of the previous holders and their individual acceptance rules. Widely accepted standards may emerge alongside individual rules, allowing for both flexibility and standardization.

5. **Redemption**: The current holder of a note can redeem it with any of the previous holders for the equivalent value in the agreed-upon unit of account or other assets. If the original issuer's reserve cannot cover the note, the responsibility cascades to previous signers. A redemption fee incentivizes reserve provision and discourages unnecessary redemptions, promoting circulation.

6. **Dynamic Quality**: As a note circulates and accumulates signatures from trusted agents, its perceived credibility and value can increase, even if the original issuer didn't provide full collateral backing.

### Example Scenario

Consider a small gold mining cooperative in Ghana issuing a note backed by tokenized gold. The note is then accepted by the national government as a means of tax payment. The government uses the note, now backed by gold and trust in the Ghana government (making it convertible to Ghanaian Cedi), to buy oil from a Saudi oil company. The oil company, having its own oil reserve, uses the note to buy equipment from China. Now, a Chinese company holds a note backed by gold, oil, and Cedis. It may be challenging for the Chinese company to redeem from the small cooperative in Ghana, so they can redeem from the Ghana government, which in turn may redeem from the cooperative.

### Note Quality Estimation

Each economic agent has an individual note quality estimation predicate Pi(n) that considers the collaterals and trust of previous spenders. Agents may have different collateralization estimation algorithms, whitelists, blacklists, or trust scores assigned to the note's previous spenders. Different agents may analyze the history of a single note, all notes issued by the note's signers, or apply other methods.

In general, the payment sender needs to consult with the receiver to determine if the payment (consisting of one or more notes) can be accepted. However, in practice, standard predicates are likely to emerge, allowing payment receivers (e.g., online shops) to publish their predicate or predicate ID online, enabling payments without prior interaction.

## Blockchain and Layer 2 Implementation

ChainCash is implemented on top of the Ergo blockchain, consisting of on-chain contracts and a ChainCash Server that handles client-side validation. To enhance scalability, ChainCash also supports Layer 2 (L2) implementations, where notes can be transferred off-chain with only redemption requiring on-chain transactions.

### On-Chain Contracts

- **Reserve Contract**: Locks ERG native tokens on the Ergo blockchain and allows for the redemption of native or custom tokens when a note is presented.
- **Note Contract**: Ensures the note has a proper history, with a valid signature from the corresponding reserve owner added on each spend. It also allows for note splitting (payment and change) and redemption.
- **Receipt Contract**: Created during redemption, it contains the ownership history copied from the note input and the position of the redeemed reserve in the ownership chain, along with the note's value.

### Layer 2 Solutions

On Layer 2, notes can be created and transferred without needing blockchain transactions, significantly reducing costs and increasing transaction speed. Redemption happens on Layer 1, involving blockchain transactions. This approach allows for a more scalable implementation of ChainCash while maintaining the security and integrity of the system.

## Applications

ChainCash serves as a foundation for various monetary systems, such as:

1. **Local Exchange Trading Systems (LETS)**: Members can whitelist each other to accept notes regardless of backing reserves, enabling the collective creation of money within the community. ChainCash allows LETS to seamlessly integrate with broader financial systems.

2. **Local Currencies**: Local or national governments can issue notes and enforce their acceptance within their jurisdiction. ChainCash supports customized contracts that can impose redemption fees for non-local users or apply demurrage, enhancing the utility of local currencies.

3. **Multilateral Trade-Credit Set-off**: ChainCash facilitates the clearing of mutual debts by allowing participants to atomically burn tokens backed by counter-parties in a single transaction, enabling more efficient credit clearing.

## Advantages and Drawbacks

### Advantages:
- Combines trust and collateral in a unique way for money issuance.
- Provides elasticity of supply without forcing individual users to accept lower quality notes.
- Supports the development of various monetary systems on top of it, from local currencies to global trade systems.
- Scalable via Layer 2 solutions, reducing the cost and complexity of transactions.

### Drawbacks:
- Notes are non-fungible due to unique backing, which may limit their use in certain DeFi applications (e.g., liquidity pools, lending pools).
- Currently lacks privacy features in payments (this topic is left for further research).

## Conclusion

ChainCash introduces a novel approach to decentralized money creation, combining trust and collateral to enable an elastic money supply. By allowing agents to issue and accept notes based on their individual rules, ChainCash provides a flexible foundation for various monetary systems while maintaining the quality of the currency. Although there are some limitations, such as the non-fungibility of notes and the lack of privacy features, ChainCash offers a promising alternative to traditional centralized currencies and blockchain assets with inelastic supply.

## References

- [Whitepaper](https://github.com/ChainCashLabs/chaincash/blob/master/docs/whitepaper/chaincash.pdf)
- [ChainCash Server Design Document](https://github.com/ChainCashLabs/chaincash/blob/master/docs/server.md)
- [ChainCash Contracts](https://github.com/ChainCashLabs/chaincash/tree/master/contracts)
- [ChainCash Tests](https://github.com/ChainCashLabs/chaincash/blob/master/src/test/scala/kiosk/ChainCashSpec.scala)
- [ergoforum: ChainCash - A Spender Signed Currency on Ergo](https://www.ergoforum.org/t/chaincash-a-spender-signed-currency-on-ergo/4015)
- [The World Needs For More Collateral](https://www.ergoforum.org/t/the-world-needs-for-more-collateral/4451)

---

This updated version incorporates additional technical details and clarifies the implementation and potential applications of ChainCash. Let me know if you'd like further refinements or additions!