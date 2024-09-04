---
tags:
 - NIPoPoWs
 - Sidechains
---

# NiPoPoW Sidechains

Non-Interactive Proofs of Proof-of-Work (NiPoPoWs) are a novel technology that enables trustless sidechains. They leverage [***Simplified Payment Verification***](modes.md) (SPV) proofs to provide resistance against potential attacks, while maintaining a small enough size for efficient network transmission. Previous proposals for "compact SPV proofs" have shown vulnerabilities to certain attacks, particularly those that could allow miners to illicitly acquire funds from the sidechains.

NiPoPoWs introduce a paradigm shift in how information is verified across blockchains without trusting centralized parties. By using NiPoPoWs, sidechains can validate transactions and blocks from other chains securely and efficiently, enabling broader interoperability and enhancing the scalability of blockchains.

## How NiPoPoW Sidechains Work

NiPoPoW sidechains utilize a method where proofs are both succinct and can be quickly verified. This is achieved through the use of superblocks, which are blocks with significantly more work than average blocks. These superblocks form a backbone that provides a high-level, compressed version of the blockchain's proof-of-work history, enabling efficient verification by sidechains.

In our implementation, sidechains equipped with NiPoPoW verifiers can validate proofs without having access to the full blockchain data of another chain. This is crucial for efficient cross-chain transactions, where operations like asset transfers and smart contract executions can occur seamlessly between different blockchains.

### Technical Insights from Academic Research

- **Proof of Work Sidechains**:
  - In the "Proof of Work Sidechains" paper by Aggelos Kiayias and Dionysis Zindros, they discuss a first-of-its-kind construction for sidechains that allows communication between proof-of-work blockchains without trusted intermediaries. Their approach ensures that as long as miners control less than 50% of the network's hash rate, the security of assets and data crossing between chains is maintained.
  - The paper models the security of such sidechains through mathematical proofs, illustrating how NiPoPoWs can be implemented in any blockchain with sufficient expressive power to support the verification of these proofs, such as through smart contracts in Solidity.

## Applications and Use Cases

NiPoPoWs sidechains have a variety of applications, including:  

- **Cross-Chain Transactions**: Enable secure and trustless transactions between different blockchains.
- **Decentralized Finance (DeFi)**: Facilitate the seamless transfer of assets for use in DeFi applications across various blockchains.
- **Scalability Solutions**: Act as a scaling solution by offloading transactions from a congested main chain to a faster, more efficient sidechain.

## Resources

### Academic Papers
- [Proof of Work Sidechains](https://eprint.iacr.org/2018/1048.pdf)

### Articles
- [Sidechains: Why These Researchers Think They Solved a Key Piece of the Puzzle](https://bitcoinmagazine.com/technical/sidechains-why-these-researchers-think-they-solved-key-piece-puzzle)
- [The Sidechains Breakthrough Almost Everyone in Bitcoin Missed](https://www.coindesk.com/markets/2018/01/17/the-sidechains-breakthrough-almost-everyone-in-bitcoin-missed/)

### Videos
- [Thoughts on Cross Chain Communication, Sidechains, NiPoPoWs and Litecoin](https://www.youtube.com/watch?v=HvIAgDEUC4o)
- [IOHK Research | Dionysis Zindros, Sidechains](https://www.youtube.com/watch?v=Y5QUGqFQnWg)
- [NiPoPoW Lecture Series](https://www.youtube.com/watch?v=Bky_YlzToSA)
