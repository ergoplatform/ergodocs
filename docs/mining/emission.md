# Emission Schedule

Ergo has a maximum supply of 97,739,925 Ergs, which is expected to be completed by 2045. The block reward is set to decrease to 3 ERG in 2026 as per [EIP27](eip27.md). 

You can view a graph of the emission schedule on [ergo.watch](https://ergo.watch/emission).

## Launch Date

Ergo development began in 2017, and the mainnet was successfully launched in July 2019. Prior to the mainnet launch, during the year leading up to it, there was a token called "Ergo-First-Year-Token" (EFYT).

## What is EFYT?

Ergo-First-Year-Token (EFYT) was airdropped and distributed on the Waves DEX. The airdrop began with 100,000 EFYT tokens in May 2017. The purpose of EFYT was twofold: to foster an early community of stakeholders and enthusiasts for Ergo and to raise funds for the platform's development and promotion before the mainnet launch. 

> It's essential to understand that EFYT is a Waves token and is not the same as Erg, the native token of Ergo. After Ergo's mainnet launch, mining began to produce ERG tokens.

The maximum supply of EFYT is 1,970,945.0, which corresponds to 10% of Ergo's first-year token emission. The Treasury receives an equivalent number of ERG, allowing for the conversion of EFYT to Erg.

Here are some resources related to EFYT:

- [Asset Distribution Report](http://pywaves.org/assets/725Yv9oceWsB4GsYwyy4A52kEwyVrL5avubkeChSnL46)
- [EFYT on Waves Explorer](https://wavesexplorer.com/assets/725Yv9oceWsB4GsYwyy4A52kEwyVrL5avubkeChSnL46?search=725Yv9oceWsB4GsYwyy4A52kEwyVrL5avubkeChSnL46)

## Why 97,739,924 ERGs?

The maximum supply of 97,739,924.5 ERGs was determined based on a pre-agreed smart contract that controls emission in Ergo. The goal was to create a simple emission curve with a total limited supply close to 100 million Ergs, to be completed within 8-10 years.

This specific amount was chosen to cover the initial genesis state, including:

- A box with proof-of-no-premine (1 ERG)
- The Foundation treasury, which currently holds 4,330,791.5 ERGs
- The Miner Reward Box, which contains the required ERGs for 2,080,800 blocks according to the emission schedule until rewards reach 0 and storage rent and EIP-27-reemission-box take over (93,409,132 ERGs)

The Treasury box is protected by a vesting smart contract that ensures an initial unlocked amount and then releases ERGs to provide funds for 2.5 years, without exceeding 10% of the circulating supply. These allocations result in a total supply of 97,739,924.5 ERGs.

For proof-of-no-premine, the pre-genesis state in Ergo contains block hashes from Bitcoin and Ethereum, as well as headlines from news sources like The Guardian, Vedomosti, and Xinhua around the time of the launch. You can find the relevant information in the [mainnet.conf](https://github.com/ergoplatform/ergo/blob/1935c95560a30b19cdb52c1a291e8a389ba63c97/src/main/resources/mainnet.conf#L11) file.

The code for the emission schedule can be found [here](https://github.com/ergoplatform/ergo/blob/e6086e23ecd45f1e01a3e4c0344f003cec1a5b11/src/test/scala/org/ergoplatform/mining/ErgoMinerPropSpec.scala#L24).

## Ergo Foundation

The Ergo Foundation is a community-driven entity focused on various aspects:

- Promoting the non-breaking development of the Ergo Platform protocol.
- Encouraging the widespread adoption and use of Ergo Platform and its native token (ERG).
- Developing the ecosystem surrounding the Ergo Platform.
- Promoting the use of Ergo Platform and blockchain technology for social good.
- Supporting truly decentralized infrastructure.
- Upholding privacy as a fundamental human right.

To support the development, promotion, events, and other activities that advance the platform, Ergo has a Treasury in place. The Treasury receives 4.43% of the Ergs released during emission. In the first two years after the mainnet launch, the Treasury received 7.5 Ergs per block.

For more information, you can refer to the latest [transparency report](ergo-foundation-2022.md).