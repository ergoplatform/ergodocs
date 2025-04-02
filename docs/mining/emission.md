---
tags:
  - Emission
  - Tokenomics
  - Mining
  - Ergo Foundation
---

# Ergo Emission Schedule

Ergo's journey, which began in 2017, saw the successful launch of its mainnet in July 2019. 


/// admonition | Ergo-First-Year-Token
Prior to the mainnet,  '*Ergo-First-Year-Token*' (EFYT) was in circulation and swapped with the treasury on launch. For comprehensive insights into EFYT, including its tokenomics and distribution strategy, please visit [this page](efyt.md).
///


## Total Supply and Allocation

Ergo's total supply is capped at **97,739,925 ERGs** and distributed as follows:

- **Genesis State Inclusions**: Includes 1 ERG for proof-of-no-premine and 4,330,791.5 ERGs for the [Foundation Treasury](https://explorer.ergoplatform.com/en/addresses/4L1ktFSzm3SH1UioDuUf5hyaraHird4D2dEACwQ1qHGjSKtA6KaNvSzRCZXZGf9jkfNAEC1SrYaZmCuvb2BKiXk5zW9xuvrXFT7FdNe2KqbymiZvo5UQLAm5jQY8ZBRhTZ4AFtZa1UF5nd4aofwPiL7YkJuyiL5hDHMZL1ZnyL746tHmRYMjAhCgE7d698dRhkdSeVy).
- **Miner Rewards**: 93,409,132 ERGs, designated for 2,080,800 blocks, as per the emission schedule ([Miner Reward Box](https://explorer.ergoplatform.com/en/addresses/2Z4YBkDsDvQj8BX7xiySFewjitqp2ge9c99jfes2whbtKitZTxdBYqbrVZUvZvKv6aqn9by4kp3LE1c26LCyosFnVnm6b6U1JYvWpYmL2ZnixJbXLjWAWuBThV1D6dLpqZJYQHYDznJCk49g5TUiS4q8khpag2aNmHwREV7JSsypHdHLgJT7MGaw51aJfNubyzSKxZ4AJXFS27EfXwyCLzW1K6GVqwkJtCoPvrcLqmqwacAWJPkmh78nke9H4oT88XmSbRt2n9aWZjosiZCafZ4osUDxmZcc5QVEeTWn8drSraY3eFKe8Mu9MSCcVU)).

The Treasury's funds were governed by a smart contract that released ERGs gradually over the first 2.5 years, without exceeding 10% of the circulating supply.


## Ergo Foundation

The Ergo Foundation is dedicated to protocol development, ecosystem growth, promoting the use of Ergo for social good, supporting decentralized infrastructure, and upholding privacy rights. The Foundation's Treasury, which received 4.43% of the total ERG emission, is utilized to support a wide range of initiatives. For more detailed information, refer to the [transparency report](ergo-foundation-2022.md).



## Mining and Emission Duration

Ergo's block reward decreases by 3 ERG per block every quarter until 2026 and stabilizes at 3 ERG per block thereafter. The mining process is projected to continue until around 2045, extended from the original 2027 timeline with the passage of the [EIP27](eip27.md) soft-fork. For a visual overview, see the emission schedule on [ergo.watch](https://ergo.watch/emission).

/// details | Sustaining Ergo Mining: Revenue Streams Beyond Emissions
As Ergo's emission schedule is set to conclude around the year 2045, questions naturally arise about the mechanisms that will incentivize miners to continue securing the network. Fortunately, Ergo's architecture includes support for a variety of revenue streams designed to promote both network growth and long-term sustainability. See [this page](revenue.md) for more information.
///


## Unique Aspects of Ergo's Emission

### Proof of No Premine

Ergo includes Bitcoin and Ethereum block hashes and headlines from The Guardian, Vedomosti, and Xinhua in its pre-genesis state for verification purposes. This is detailed in the [mainnet.conf](https://github.com/ergoplatform/ergo/blob/1935c95560a30b19cdb52c1a291e8a389ba63c97/src/main/resources/mainnet.conf#L11) file.


### Verification Process

Ergo's emission logic underwent rigorous verification using the Stainless formal verification tool, ensuring accuracy and validity. Details can be found in [this code section](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/580/files#diff-18d3c92c2086c9ddd9b462191b55cf5e8438a29b0e786c6ab541f7def8330808).

### No Out-of-Thin-Air Emission

Ergo's "coinbase" transaction, the first transaction in each block, does not create new tokens out of thin air. This policy ensures traceability of every coin or token from a legitimate source, enhancing the integrity and scarcity of Ergo's native currency, and contributing to economic stability.
