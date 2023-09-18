# Understanding Cryptocurrency Fees: A Multi-Dimensional Approach

This article builds upon the research presented in the paper *[A Systematic Approach To Cryptocurrency Fees](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf)*. Authored by Alex (Kushti) Chepurnoy, Vasily Kharin, and Dmitry Meshkov, the paper delves into the complexities surrounding blockchain storage and suggests a multi-dimensional fee structure as a solution.

## The Double-Edged Sword of Blockchain Storage

Blockchain technology is remarkable for its capabilities of ensuring security, transparency, and an immutable transaction history. However, this very feature of permanence leads to ever-expanding blockchain states, raising a series of concerns:

1. **Risk of Centralization**: As the state grows, fewer entities can effectively store it, escalating the centralization threat.
2. **Spam Attack Vulnerability**: A bloated state is an inviting target for spam and denial-of-service attacks.
3. **Resource Drain**: Larger states require more computational power, leading to increased operational costs.
4. **Deflationary Pressures**: Lost or dormant coins risk deflating the currency’s value, undermining its utility.

![A 3-Dimensional Scale for Fees](https://ergoplatform.org/img/uploads/3d.png)

The image above introduces a 3-dimensional scale to assess cryptocurrency fees based on three crucial factors: space (storage load), duration (time), and computational load. This visualization aids in understanding how a multi-faceted fee system could mitigate the inherent challenges tied to blockchain storage and resource utilization.

### Case Studies: Bitcoin and Ethereum

To illustrate these concerns, consider the spam attack on Bitcoin in July 2015 that led to 15 million new outputs, bloating the total UTXO size significantly. Ethereum faced a similar fate with an attack that added 18 million new accounts to its state, causing resource-intensive denial-of-service attacks on nodes.

### A Multi-Faceted Solution: Storage Rent

The paper suggests the concept of "storage rent" as a remedy. This involves a recurring fee on each Unspent Transaction Output (UTXO) aimed at deterring indefinite data storage. By implementing this mechanism, blockchain systems could become more efficient, secure, and sustainable, aligning with earlier ideas such as the 2014 [Freicoin](http://freico.in) proposal for currency demurrage.

## Highlights and Contributions of the Paper

- **Dimensional Fee Complexity**: The paper breaks new ground by considering fees in three dimensions—space, time, and computation—rather than as a monolithic entity.
- **Unsustainability of Unchecked Growth**: State growth, if left unchecked, risks centralization and compromised security through reliance on Simplified Payment Verification (SPV) mining.
- **Innovative Fee Algorithms**: The paper introduces fresh algorithms for fee differentiation and pricing curves for storage, aiming for a more predictable and economical fee structure.
- **Strategic State Management**: The paper advocates for the introduction of a fee component specifically tailored to regulate state size effectively.
- **Unintended Ripple Effects**: The research also touches on the secondary impacts of storage fees, such as the reactivation of lost or dormant coins.

## Miner Costs and Ecosystem Sustainability

In a Proof-of-Work blockchain system, miners play a pivotal role, safeguarding the network's integrity at the cost of electricity and computational resources. To sustain this ecosystem, miners are compensated through block rewards and transaction fees.

In platforms like Ethereum that support smart contracts, transactions may involve substantial computational overhead, necessitating a multi-dimensional fee structure that accounts for:

- **Storage Load**: Represents the costs associated with preserving historical blockchain data.
- **Computational Load**: Entails the computational resources expended in executing smart contracts.
- **Network Load**: Includes the bandwidth and processing capacity needed to accommodate new, yet-to-be-blocked transactions.

For instance, in the Ergo blockchain, the paper recommends introducing a "state deterioration fee." This would incentivize miners to streamline system performance by effectively managing the state size, including all UTXOs, smart contracts, and transactional data.