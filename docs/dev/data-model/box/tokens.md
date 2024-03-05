---
tags:
  - Data Model
  - Storage Rent
  - Registers
---

# Tokens on Ergo

Ergo's native tokens are incredibly versatile and can represent a wide range of assets, including shares, complementary currency units, and various tangible or intangible items. The infrastructure of Ergo is designed to seamlessly handle the representation and transfer of these diverse assets, integrating them into the blockchain as *first-class citizens*.

//// details | What are  **first-class citizens**? 
    {type: info, open: false}
This means that tokens in Ergo are not just metadata attached to transactions, but they are deeply integrated into the Ergo protocol. They can be manipulated and managed with the same level of support and functionality as the native Ergo token (see [EIP-0004](eip4.md)).
/// details | It is crucial to understand that ERG, the native token of Ergo, possesses two unique characteristics:
    {type: warning, open: false}
- ERGs **cannot be burned**; the total input and output amounts in any transaction must be equal.
- [Storage rent](rent.md) can only be paid in ERGs.
///
////

/// details | How do I mint a token?
    {type: info, open: false}
- Use [ergoutils](https://ergoutils.org/#/token) to mint a token directly from your web browser. ([Video Tutorial](https://www.youtube.com/watch?v=I3R6_PceM1k)
))
- For programmatic token minting, refer to this guide: [Minting a Token with Fleet SDK](https://fleet-sdk.github.io/docs/transaction-building#step-4-2-mint-a-token)
///


There is no central database where tokens are registered currently, your best bet is to use community resources like [supported tokens in the ergotipper bot](https://github.com/Luivatra/ergotipper-tokens) and [spectrum-finance/ergo-token-list](https://github.com/spectrum-finance/ergo-token-list).

## Token Storage

- Tokens are stored in a special [register](registers.md) `R2` of a [box](box.md) in the form of (tokenId -> amount) pairs.
- A single box can hold **up to 255 secondary tokens**.


## Register Usage

The Ergo reference implementation wallet uses specific [registers](registers.md) in a unique way, although the protocol doesn't enforce this:

* `R4` - verbose name
* `R5` - description
* `R6` - number of decimal places
* Additional registers (`R7`, `R8`, `R9`) can store asset-specific information


## Limitations

There are certain indirect limitations to consider:

- The size of a box should not exceed 4 kilobytes.
- The presence of tokens increases the computational cost of the transaction.

## Asset Creation

An exception to the rule of weak preservation *(the total amount in inputs should be no less than the total amount in outputs)* is that a transaction can generate tokens from thin air in its outputs if the asset identifier matches the identifier of the transaction's first input box. Given that the box identifier is cryptographically unique, it's impossible to have a second asset with the same identifier, assuming the hash function used is collision-resistant (which it indeed is). This rule also implies that **only one new asset can be created per transaction.**

## Examples

- [How to mint a token with Fleet SDK](https://fleet-sdk.github.io/docs/transaction-building#step-4-2-mint-a-token)
- Creating a [perpetual token](perpetual.md) (designed to exist indefinitely, unless it is removed by garbage collection.)

## Resources

- [Token category on sigmaverse.io](https://sigmaverse.io/all-projects/?category=Tokens)
- [Ergo Token Minter](https://thierrym1212.github.io/tokenminter/index.html) or [CYTI](https://thierrym1212.github.io/cyti/index.html) which uses a Use CYTI minable smart contract to choose your token ID.
- [ergoutils.org](https://ergoutils.org/#/token)
- [Video Tutorial](https://www.youtube.com/watch?v=I3R6_PceM1k)
- [Why does the limitation of 1 new token per transaction exist?](https://github.com/ergoplatform/ergo/issues/2013)


