---
tags:
  - Box
  - Registers
---

# Boxes and Registers

In [ErgoScript](ergoscript.md), a 'box' is akin to a more versatile version of what a UTXO (Unspent Transaction Output) represents in Bitcoin and many other cryptocurrencies. A box is not only a ledger entry denoting the amount of cryptocurrency owned by a particular address, but it also carries 'registers', allowing it to contain additional data. This data could range from simple values to more complex structures, which can later be integrated into transactions and used in the execution of smart contracts.

This makes Ergo's box different from a traditional UTXO, which only represents an amount of unspent cryptocurrency associated with a certain address. In UTXO-based cryptocurrencies, each transaction consumes one or more UTXOs as inputs and creates one or more UTXOs as outputs, with the 'unspent' outputs being the 'coins' that can be spent in future transactions.

The term 'box' in Ergo's context captures the idea that these entities are like containers holding various types of information (value, tokens, custom data, etc.), beyond just the unspent transaction output balance. This makes the boxes in Ergo significantly more flexible and functional, enabling more complex operations, such as running scripts or smart contracts, directly on the blockchain.


