# The Ergo Protocol

Ergo builds advanced cryptographic features and radically new DeFi functionality on the rock-solid foundations laid by a decade of blockchain theory and development. It complements tried and tested principles with the latest peer-reviewed academic research into cryptography, consensus models and digital currencies.

Ergo is a unique **Proof-of-Work (PoW)** cryptocurrency and DeFi platform, building on the first principles of Bitcoin. With a research-driven but practical development model, Ergo has prioritized useful features without compromising on security. The platform's smart contracts are built on the extended **UTXO (eUTXO)** model with a unique data input concept, offering a radically different approach to provide robust, flexible cryptography and easy, safe scripting on privacy-centric **Sigma Protocols** (non-interactive zero-knowledge proofs). Storage rent (~.13 erg every 4 years) for long-term survivability, ultra-efficient **light clients**, and **NiPoPoW** technology.

Ergo is a **UTXO** based blockchain with Proof-of-Work consensus. In this aspect it is similar to Bitcoin. Ergo uses standard **Elliptic Curve** Cryptography and the exact same curve as Bitcoin (`Secp256k1`). Unlike Bitcoin and similar to Cardano, Ergo uses a so called "extended-UTXO model", which implies UTXOs with the ability to contain arbitrary data and sophisticated scripts. 

Due to this, Ergo supports advanced financial contracts similar to those in Ethereum's account-based model.

## Contractual Money
The cryptographic part of Ergo script is based on **Sigma Protocols** and naturally supports threshold m-of-n signatures, ring signatures and more. Keeping all this in mind, we expect ErgoScript and Ergo’s design to be uniquely useful as **Contractual Money** with countless possible applications. 

The overwhelming majority of successful public blockchain use‐cases are related to financial applications. Ergo extends Bitcoin’s way of writing contracts by attaching a guard script (together with additional custom data) to every coin.  For example, in addition to regular protection by some `m‐of‐n` signature, Ergo allows specifying the possible recipients of these coins, which may also be a contract with similar complex conditions. This "chaining" approach allows the implementation of secure and efficient contracts of arbitrary complexity. This, along with Ergo's focus on sustainability is what makes it uniquely useful as contractual money. The scripting language in itself is non-Turing complete but applications ran on the platform can be made to be Turing complete as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf) 

**All cryptocurrencies rely on contributions from the scientific research community. Ergo brings it in its core!**


## The Manifesto                                                       
> Cryptocurrency should provide tools to enrich ordinary people. Their small businesses providing no much above making ends meet, not depersonalized big financial capital. This is what inspired me. This is my dream.

See the [Ergo Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/)


## Ergo Proof-of-Work (PoW)
Ergo uses Autolykos as the underlying PoW algorithm. Autolykos v2 (current version of PoW) is memory-hard ASIC-resistant PoW algorithm oriented towards GPUs.

## Storage Rent
Another unique feature of Ergo is the concept of storage-rent, which is the ability of miners to take out a small amount of Ergs from boxes that have remained unspent for four or more years (the box is spent and a new box is created with the lower value). This allows Ergo to avoid long-term bloat of the UTXO set.

- [Building Ergo: Storage rent](https://ergoplatform.org/en/blog/2020_04_21_ergo_positioning/)

## ErgoScript
Ergo provides advanced programming abilities for financial contracts using a high-level language called ErgoScript. As a simple example, the below script allows only Alice to spend a box before a certain height and only Bob to spend the box after that.

`if (HEIGHT < 100000) alicePubKey else bobPubKey `

