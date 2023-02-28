# Sidechains

A sidechain is a separate blockchain that connects to another blockchain via a **two-way peg**.

Sidechains are beneficial for various elements such as introducing private chains, scalability improvement, and cross-chain interoperability. 

In order to send money to a sidechain they must attach a proof that proves they have the funds. Without these, the sidechain would be prone to double-spending attacks. 


## NiPoPoWs


NiPoPoWs (Non-Interactive Proofs of Proof-of-Work) are a type of proof that allows for the efficient verification of large amounts of data stored in a blockchain. They are useful for creating sidechains, which are separate blockchains that can be linked to a main blockchain. Sidechains can scale a blockchain network by offloading some transaction processing to a separate chain.

NiPoPoWs work by allowing for the efficient verification of a subset of blocks in a blockchain rather than requiring the entire blockchain to be verified. This makes it possible to link a sidechain to a main chain while ensuring it remains secure and trustworthy.

One way that NiPoPoWs can be used for scaling is by allowing for the creation of off-chain state channels. State channels allow transactions to be processed off-chain, reducing the load on the main blockchain. NiPoPoWs can be used to ensure the integrity of state channel transactions while still allowing for efficient verification of the blockchain.

Another way that NiPoPoWs can be used for scaling is by allowing for the creation of ["light"](light-spv-node.md) or ["thin"](pruned-full-node.md) clients that don't need to download and verify the entire blockchain. Instead, they can use NiPoPoWs to verify a subset of blocks, reducing the client's storage and processing requirements.

Overall, NiPoPoWs are useful for creating sidechains and scaling blockchain networks. They allow for efficient verification of a subset of blocks, reducing client storage and processing requirements and enabling off-chain state channel creation.




## Resources

### Papers

- [Proof of Work Sidechains](https://eprint.iacr.org/2018/1048.pdf)

### Articles

- [SIDECHAINS: WHY THESE RESEARCHERS THINK THEY SOLVED A KEY PIECE OF THE PUZZLE](https://bitcoinmagazine.com/technical/sidechains-why-these-researchers-think-they-solved-key-piece-puzzle)
- [The Sidechains Breakthrough Almost Everyone in Bitcoin Missed](https://www.coindesk.com/markets/2018/01/17/the-sidechains-breakthrough-almost-everyone-in-bitcoin-missed/)

### Videos

- [Thoughts on Cross Chain Communication, Sidechains, NiPoPoWs and Litecoin](https://www.youtube.com/watch?v=HvIAgDEUC4o)
- [IOHK Research | Dionysis Zindros, Sidechains](https://www.youtube.com/watch?v=Y5QUGqFQnWg)
- [NiPoPoW Lecture Series](https://www.youtube.com/watch?v=Bky_YlzToSA)
