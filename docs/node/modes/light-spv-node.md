---
tags:
  - NIPoPoWs
---

# Light-SPV Mode

## Overview 


Simplified Payment Verification (SPV) allows for a simplified way of verifying transactions by only downloading and verifying the block headers, rather than the entire blockchain. This makes it possible for users with limited resources to participate in the network and make transactions without needing a full node.

## Ergo's NIPoPoWs

While SPV wallets are already very lightweight compared to full nodes, NIPoPoW-empowered SPV wallets need to download only a tiny sample of block headers, around 250, while other SPV clients need may to download around half a million block headers. The sample needed changes but does not grow much in size as the blockchain grows more extensive, even after accumulated decades of data.


A highly efficient Ergo wallet with SPV security is currently in development. Keep an eye out for updates [here](https://github.com/ergoplatform/sigma-rust/milestone/17).




## Technical Workflow

### Bootstrap

1.  Send **`GetPoPoWProof`** for all connections.
2.  On receiving **`PoPoWProof`**, apply it to History (History should determine whether this PoPoWProof is better than its current best header chain).
3.  **`GOTO`** regular regime.

### Regular

1.  Send ErgoSyncInfo message to connected peers
2.  Get a response with an INV message containing the ids of blocks, better than
    our best block.
3.  Request headers for all ids from 2.
4.  On receiving Header:

```java
    if(History.apply(header).isSuccess) {
        State.apply(header) // just change state roothash
    if(!isInitialBootstrapping) Broadcast INV for this header
    } else {
        blacklist peer
    }
```


## Old

# Simplified Payment Verification 

A full Bitcoin node checks all the blocks in the blockchain (using headers) and ensures no fraudulent transactions. It is a very secure way of using crypto – but there is a problem. It requires significant bandwidth, storage, and processing power. That commodity hardware is expensive, and using a full node to validate and make transactions is unsuitable for mobile devices. This is particularly true for Bitcoin, where the blockchain is over [270 GB and counting](https://www.blockchain.com/charts/blocks-size).

Simplified Payment Verification (SPV) is designed to address this problem, as described in the [Bitcoin white paper](https://bitcoin.org/bitcoin.pdf):

> It is possible to verify payments without running a full network node. A user only needs to keep a copy of the block headers of the longest proof-of-work chain, which he can get by querying network nodes until he's convinced he has the longest chain and obtain the Merkle branch linking the transaction to the block it's timestamped in. He can't check the transaction for himself, but by linking it to a place in the chain, he can see that a network node has accepted it, and blocks are added after it confirms the network has accepted it.
 
Satoshi notes that this is not a perfect solution and is vulnerable to an attacker overpowering the network and fooling SPV users.

Moreover, while SPV mode is intended for resource-limited devices, this 'lite' approach is not always feasible. Ethereum's headers alone total around 5 GB to download. Thus Ethereum mobile clients do not validate chain validity and blindly have to trust third parties.

There are proposals to reduce the requirements for SPV mode by checking just a few random headers instead of all. However, it takes much work to do that securely. 



## Efficient SPV

Several years have been spent researching and developing secure protocols for efficient SPV clients. The two best-known and most reliable protocols are NIPoPoWs and FlyClient.

Ergo implements NIPoPoWs, or Non-interactive Proof-of-Proof-of-Work. 

> *Non-Interactive Proofs of Proof-of-Work (NIPoPoWs) are short stand-alone strings that a computer program can inspect to verify that an event happened on a proof-of-work-based blockchain without connecting to the blockchain network and without downloading all block headers. For example, these proofs can illustrate that a cryptocurrency payment was made.*

NIPoPoWs allow very efficient mobile wallets to be created. [SPV wallets](https://bitcoin.org/en/developer-guide#simplified-payment-verification-spv) are already very lightweight compared to full nodes because they only require the download of block headers, not the whole blockchain. NIPoPoW wallets need to download only a tiny ***sample*** of block headers, around 250, when SPV clients need to download half a million block headers. The sample needed changes but doesn't grow much in size as the blockchain grows more extensive, even after accumulated decades of data.

This enables us to build a mobile SPV client that requires around **just 100KB** of block headers to be downloaded.

A super-efficient Ergo wallet with SPV security is in development, so stay tuned for more updates!

- [sigma-rust: SPV node API](https://github.com/ergoplatform/sigma-rust/milestone/17) milestone on GitHub

