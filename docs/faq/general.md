# FAQ


## Getting Started

- Ergo is currently available on the following [wallets](https://ergoplatform.org/en/wallets/) and [exchanges](https://ergoplatform.org/en/exchanges/). 
- The development roadmap can be seen [here](https://ergoplatform.org/en/ecosystem/#Roadmap).
- To see the applications currently running on Ergo, check out [sigmaverse.io](https://sigmaverse.io/).
- To read about Ergo from a less technical perspective, visit [ergonaut.space](https://ergonaut.space/en/home). 
- If you want to mine, see the [Miners Handbook](https://ergonaut.space/en/Guides/Mining).

## Why '*Ergo*'? 

Ergo means "therefore" in Latin but "work" in Greek. This is also a play on the fact that the cryptocurrency's design is ***ergo***nomical.

## Why Ergo?

Ergo is a next-generation smart contract platform enabling anyone to participate in the digital DeFi revolution.

Ensuring economic freedom for ordinary people through decentralized, private and secure financial tools.

**🔑 Key Objectives**

- Research-led but real-world-focused.
- Powerful & Safe
- Intelligent and Straightforward
- Secure and Accessible

**🔑 Key Features**

- **[Sigma Protocols](/dev/scs/sigma) (Σ)** - a type of non-interactive zero-knowledge proofs that are flexible enough to allow for ring-signatures, multi signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.
- **[Multi-stage Contracts](/dev/scs/multi)** - In addition to the regular protection offered by using a threshold `m‐of‐n` signature, Ergo also allows specifying the possible recipients of these coins, which may be another contract with similar complex conditions. This *"chaining"* approach enables the implementation of **secure and efficient smart contracts of arbitrary complexity**. 
- **[Non-Interactive Proofs of Proof of Work (NIPoPoWs)](/dev/protocol/nipopow/)**  are essential for two reasons: Light Clients and Side Chains. 
- **[Storage Rent](/dev/protocol/rent/)** acts as *on-chain garbage collection*


Keeping all this in mind, we expect Ergo's design to be uniquely useful as Contractual Money.




## What is the [Emission Schedule](https://ergoplatform.org/en/blog/2019_05_20-curve/)?

Ergo has a maximum supply of **97,739,925** Ergs, to be completed in **8 years** after launch. However, there is currently voting underway to extend this to 2045. 

## When was Ergo launched?

Mainnet July 2019. Before this, there was *Ergo-First-Year-Token*

**What is EFYT?**

Ergo-First-Year-Token was airdropped and distributed on Waves DEX starting with a 100,000 EFYT airdrop in May 2017. EFYT served the dual purposes of helping build an early community of stakeholders and enthusiasts for Ergo and of raising a small number of funds for the platform before launch to fund development, promotion etc. EFYT is strictly a Waves token and is not the same as an Erg; the Ergo mainnet native token is mined after Ergo's mainnet launch.

It should be noted that the max supply of EFYT is 1,970,945.0. This is 10% of the first year of Ergo token emission and the same number of Ergs that the Treasury will receive, meaning that the Treasury will have received 1,970,945.0 Ergs during year 1, sufficient to swap the max supply of EFYT for Erg.

## Why 97,739,924?

> Emission in Ergo is controlled by a pre-agreed smart contract, so we tried to have a simple enough emission curve with total limited supply being close to 100M (and emission to be done in 8-10 years).

The max supply is simply the amount needed to create the initial genesis state: 

- A box with proof-of-no-premine (1 ERG)
- [Foundation treasury](https://explorer.ergoplatform.com/en/addresses/4L1ktFSzm3SH1UioDuUf5hyaraHird4D2dEACwQ1qHGjSKtA6KaNvSzRCZXZGf9jkfNAEC1SrYaZmCuvb2BKiXk5zW9xuvrXFT7FdNe2KqbymiZvo5UQLAm5jQY8ZBRhTZ4AFtZa1UF5nd4aofwPiL7YkJuyiL5hDHMZL1ZnyL746tHmRYMjAhCgE7d698dRhkdSeVy) (4,330,791.5 ERG)
- [Miner Reward Box](https://explorer.ergoplatform.com/en/addresses/2Z4YBkDsDvQj8BX7xiySFewjitqp2ge9c99jfes2whbtKitZTxdBYqbrVZUvZvKv6aqn9by4kp3LE1c26LCyosFnVnm6b6U1JYvWpYmL2ZnixJbXLjWAWuBThV1D6dLpqZJYQHYDznJCk49g5TUiS4q8khpag2aNmHwREV7JSsypHdHLgJT7MGaw51aJfNubyzSKxZ4AJXFS27EfXwyCLzW1K6GVqwkJtCoPvrcLqmqwacAWJPkmh78nke9H4oT88XmSbRt2n9aWZjosiZCafZ4osUDxmZcc5QVEeTWn8drSraY3eFKe8Mu9MSCcVU) with the required ERG for 2,080,800 Blocks according to the emission schedule until rewards equal 0 and storage rent and EIP-27-reemission-box takes over (93,409,132 ERG). 

The treasury box is protected by a vesting smart contract that ensures an initial unlocked amount and then only releases an amount of ERG that provides funds for 2.5 years (never exceeding 10% of the circulating supply). All of this results in these specific amounts.

In total, this happens to be 97,739,924.5 ERG.

For proof-of-no-premine, the pre-genesis state in Ergo contains block hashes from Bitcoin and eth and also headlines from the Guardian, Vedomosti and Xinhua around the moment of launch, which can be seen in [mainnet.conf](https://github.com/ergoplatform/ergo/blob/1935c95560a30b19cdb52c1a291e8a389ba63c97/src/main/resources/mainnet.conf#L11)

```scala
  /**
    * Genesis box that contains proofs of no premine.
    * It is a long-living box with special bytes in registers
    */
  private def noPremineBox(chainSettings: ChainSettings): ErgoBox = {
    val proofsBytes = chainSettings.noPremineProof.map(b => ByteArrayConstant(b.getBytes("UTF-8")))
    val proofs = ErgoBox.nonMandatoryRegisters.zip(proofsBytes).toMap
    createGenesisBox(EmissionRules.CoinsInOneErgo, Constants.FalseLeaf, Seq.empty, proofs)
  }
```

```JSON
 {
"boxId": "b8ce8cfe331e5eadfb0783bdc375c94413433f65e1e45857d71550d42e4d83bd",
"value": 1000000000,
"ergoTree": "10010100d17300",
"assets": [],
"creationHeight": 0,
"additionalRegisters": {
  "R5": "0e42307864303761393732393334363864393133326335613261646162326535326132333030396536373938363038653437623064323632336337653365393233343633",
  "R6": "0e464272657869743a20626f746820546f727920736964657320706c617920646f776e207269736b206f66206e6f2d6465616c20616674657220627573696e65737320616c61726d",
  "R8": "0e45d094d0b8d0b2d0b8d0b4d0b5d0bdd0b4d18b20d0a7d0a2d09fd09720d0b2d18bd180d0b0d181d182d183d18220d0bdd0b02033332520d0bdd0b020d0b0d0bad186d0b8d18e",
  "R7": "0e54e8bfb0e8af84efbc9ae5b9b3e8a1a1e38081e68c81e7bbade38081e58c85e5aeb9e28094e28094e696b0e697b6e4bba3e5ba94e5afb9e585a8e79083e58c96e68c91e68898e79a84e4b8ade59bbde4b98be98193",
  "R4": "0e4030303030303030303030303030303030303031346332653265376533336435316165376536366636636362363934326333343337313237623336633333373437"
}
```
The code for the emission schedule can be found [here](https://github.com/ergoplatform/ergo/blob/e6086e23ecd45f1e01a3e4c0344f003cec1a5b11/src/test/scala/org/ergoplatform/mining/ErgoMinerPropSpec.scala#L24)



## Ergo Foundation


The [Ergo Foundation](https://ergoplatform.org/en/foundation/) is a community-driven entity focused on:

  - Promoting non-breaking development of Ergo Platform protocol;
  - Promoting the widespread adoption and use of Ergo Platform and its native token (ERG);
  - Developing the ecosystem around the Ergo Platform;
  - Promoting the use of Ergo Platform and blockchain technology for social good;
  - Supporting truly decentralized infrastructure and;
  - Supporting privacy as a basic human right.

### Funding

To fund development, promotion, events, and any other activities which may advance the platform, Ergo has in place a Treasury, which will receive **4.43%** of the Ergs released during emission. During the first two years post‐mainnet launch, the Treasury received 7.5 Ergs per block. 

Readers familiar with some other PoW protocols with a Treasury, such as ZCash, may find this to be similar; however, it should be noted that the number of Ergs going to the Treasury comprises a total of only **4,330,791.5**, or 4.43% of the total monetary base, and is completed in just 2.5 years. This compares with ZCash's Treasury, which was 10% of the ZCash total monetary base and 20% of all issued ZCash coins during the first four years. 


## What is the team's background?

Ergo is designed and implemented by experienced developers and researchers who hold publications and PhDs in cryptography, compiler theory, blockchain technology, and cryptographic e-cash. The team has a solid background in core development with cryptocurrencies and blockchain frameworks such as Nxt, Scorex and Waves. Alexander' kushti' Chepurnoy was a co-founder of smartcontract.com (now Chainlink), a core developer at NXT (The first full PoS), and one of the first employees at IOHK; he was a Research Fellow and Team Scorex Manager. 

The full team can be seen on Ergo's [Hall of Fame](https://ergoplatform.org/en/hall_of_fame/).

