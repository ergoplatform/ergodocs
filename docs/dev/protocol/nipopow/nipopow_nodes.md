
## Light Nodes

**Light Clients** are essential when considering the hurdles cryptocurrency faces with mass adoption. Most crypto users do not have the necessary tools to run a full node. Running a full node means having a strong processor with high electricity wattage and more than a hundred gigabytes of memory to store the entire blockchain. Light clients are useful because they enable verification with a limited supply of data providers (nodes) and significantly reduce the amount of data storage and bandwidth needed for everyday users.

The use of light clients with the implementation of NIPoPoWs makes it possible to interact with the blockchain through block headers by using only a couple of kilobytes. Verifying whether a transaction happened on the blockchain becomes simplified. NIPoPoWs can help people interact with the blockchain by using more efficient and convenient mobile wallets.

NIPoPoWs allow very efficient mobile wallets to be created. SPV wallets are already very lightweight compared to full nodes because they only require the download of block headers, not the whole blockchain. NIPoPoW wallets need to download only a small sample of block headers, around 250, when SPV clients need to download half a million block headers. The sample needed changes but doesn't grow much in size as the blockchain grows larger over the years, even after accumulated decades of data.

NIPoPoWs enable Ergo to build a mobile SPV client that requires around just 100KB of block headers to be downloaded.

### SPV Security

A full Bitcoin node checks all the blocks in the blockchain (using headers) and makes sure there are no fraudulent transactions. It's a very secure way of using crypto – but there's a problem. It requires significant bandwidth, storage, and processing power. That kind of commodity hardware is expensive, and using a full node to validate and make transactions is unsuitable for mobile devices. This is particularly true for Bitcoin, where the blockchain is over [270 GB and counting](https://www.blockchain.com/charts/blocks-size).

Simplified Payment Verification (SPV) is designed to address this problem, as described in the [Bitcoin white paper](https://bitcoin.org/bitcoin.pdf):

- *It is possible to verify payments without running a full network node. A user only needs to keep a copy of the block headers of the longest proof-of-work chain, which he can get by querying network nodes until he's convinced he has the longest chain and obtain the Merkle branch linking the transaction to the block it's timestamped in. He can't check the transaction for himself, but by linking it to a place in the chain, he can see that a network node has accepted it and blocks added after it further confirms the network has accepted it.*
 
Satoshi notes that this is not a perfect solution and is vulnerable to an attacker overpowering the network and fooling SPV users.

Moreover, while SPV mode is intended for resource-limited devices, this 'lite' approach is not always feasible. Ethereum's headers alone total around 5 GB to download. Thus Ethereum mobile clients do not validate chain validity and so blindly have to trust third parties.

There are proposals to reduce the requirements for SPV mode by checking just a few random headers instead of all of them. But it's hard to do that securely. 



### Efficient SPV

Several years have been spent researching and developing secure protocols for efficient SPV clients. The two best-known and most reliable protocols are NIPoPoWs and FlyClient.

Ergo implements NIPoPoWs, or Non-interactive Proof-of-Proof-of-Work. You can explore this technology in full on this dedicated website: [https://NIPoPoWs.com](https://NIPoPoWs.com):

- *Non-Interactive Proofs of Proof-of-Work (NIPoPoWs) are short stand-alone strings that a computer program can inspect to verify that an event happened on a proof-of-work-based blockchain without connecting to the blockchain network and without downloading all block headers. For example, these proofs can illustrate that a cryptocurrency payment was made.*

- *NIPoPoWs allow very efficient mobile wallets to be created. [SPV wallets](https://bitcoin.org/en/developer-guide#simplified-payment-verification-spv) are already very lightweight compared to full nodes because they only require the download of block headers, not the whole blockchain. NIPoPoW wallets need to download only a tiny ***sample*** of block headers, around 250 when SPV clients need to download half a million block headers. The sample needed changes but doesn't grow much in size as the blockchain grows more extensive, even after accumulated decades of data.*

This enables us to build a mobile SPV client that requires around **just 100KB** of block headers to be downloaded.

A super-efficient Ergo wallet with SPV security is in development, so stay tuned for more updates!

