---
tags:
  - Box
  - Registers
---

# Boxes and Registers

In [ErgoScript](ergoscript.md), a ['box'](box.md) is akin to a more versatile version of what a [UTXO (Unspent Transaction Output)](eutxo.md) represents in Bitcoin and many other [cryptocurrencies](protocol-overview.md). A box is not only a ledger entry denoting the amount of cryptocurrency owned by a particular [address](address.md), but it also carries ['registers'](registers.md), allowing it to contain additional data. This data could range from simple values to more complex structures, which can later be integrated into [transactions](transactions.md) and used in the execution of [smart contracts](contracts.md). Interpreting this register data off-chain is a common task; see [Fleet SDK Recipes](fleet-sdk-recipes.md) for examples using JavaScript/TypeScript.

This makes Ergo's box different from a traditional UTXO, which only represents an amount of unspent cryptocurrency associated with a certain address. In [UTXO-based cryptocurrencies](eutxo.md), each [transaction](transactions.md) consumes one or more [UTXOs](eutxo.md) as [inputs](transactions.md) and creates one or more [UTXOs](eutxo.md) as [outputs](transactions.md), with the 'unspent' outputs being the 'coins' that can be spent in future [transactions](transactions.md).

The term ['box'](box.md) in Ergo's context captures the idea that these entities are like containers holding various types of information (value, [tokens](eip4.md), custom data, etc.), beyond just the [unspent transaction output balance](eutxo.md). This makes the boxes in Ergo significantly more flexible and functional, enabling more complex operations, such as running [scripts](ergoscript.md) or [smart contracts](contracts.md), directly on the [blockchain](protocol-overview.md).
