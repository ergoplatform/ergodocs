---
tags:
  - On-Chain NFTs
  - NFTs
  - On-Chain
---


# On-chain NFTs

/// admonition | Warning
    type: warning

This method is not yet incorporated in [EIP-0004: Asset Standard](eip4.md). For more information, refer to this discussion [on Discord](https://discord.com/channels/668903786361651200/940209605299036170/942656843619106827).
///

## On-chain NFTs: Technical Aspects

On-chain NFTs on Ergo differ from [regular NFTs](#the-technical-aspects-of-regular-ergo-nfts) as they store images directly on the blockchain, specifically in the `R9` register of the NFT box. This eliminates the need for third-party storage. However, this comes with a size constraint. The maximum size for on-chain NFTs on Ergo is approximately **3.5 Kb**, considering space for the NFT name, description, and other data within the total **4 Kb** limit. This constraint challenges artists to create captivating pieces within a limited space.

**Steps to create an on-chain SVG:**

1. Draw a relatively simple image in SVG vector format and manually optimize your art: smooth lines, remove minor details, reduce the number of colors, etc. Further optimize using svg-optimizers.
2. Convert your *.svg file to [**Data URI format**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs) (_there are many online/offline converters available_).
3. Check if your data fits within the **4 kb** box limit (<3.5 Kb). If not, return to the first step.
4. Place this data in the `R9` register.
5. **Most challenging part**: [Mint](https://docs.ergoplatform.com/dev/tokens/nfts/nft-examples/) the NFT using a tool that allows you to manipulate the `R9` register.

/// admonition | Textual Data
    type: tip

If the data is textual, you can embed the text (using the appropriate entities or **escapes** based on the enclosing document's type). Otherwise, you can specify **base64** to embed base64-encoded binary data.
///


  
### Examples of On-chain Collections
 

**Vector Minimalism** collection:

- [Landscape #06. View from the train window](https://ergotokens.org/#/?token=62e9e8fc25e148a35e4bb99d70b810a897e78a7fd26adda0e8335a2ad17ef58c)
- [Landscape #08. Flight over the desert](https://ergotokens.org/#/?token=cf3f157c32c22749742fb0acc85aa07e6640b61290b26a89efd9e40f5070a938)
- [Monument #11. Moai](https://ergotokens.org/#/?token=1d7430bacd2a0b1d83366cfad766a8dfb221c2de80ee95ab271a29bfdf7fc0a0)
- [Monument #02. Spring Temple Buddha](https://ergotokens.org/#/?token=d935e4fa226bbd89dfc37e45f5a6bbcdee259f1368210aca61f1b6183e01c408) 
- ![VectorMinimalism](https://github.com/ergoplatform/ergodocs/assets/99899807/10efaf86-a7ba-46ec-a620-db9a4f59a29a)


**Tokenart** collection uses SVG as a container for **ASСII art**:

- [Tokenart Cat #2](https://ergotokens.org/#/?token=14435234f5fdf1bfc0f98c2186512db292266bf4ac8d0c74f6ad056dcfaf36d1)  
- [Tokenart Shark #2](https://ergotokens.org/#/?token=723f7eb846895bd0294619300488eb1974e6827e27d1624289019b42ec7252a3)
- The SVG contains pure text:
- ![svgASCII](https://github.com/ergoplatform/ergodocs/assets/99899807/02b1142b-a25d-4cc4-8092-c6026baa046c)


## A Brief History

During the spring and summer of 2021, there were several on-chain projects on Cardano. For instance, the [on-chain interactive NFT](https://pool.pm/6c4fd3073bca09e62e85463e3380546e49d0344e7996c4d1b4cd0bd3.SHDEMO6) stored an entire [HTML page with JS in its metadata](https://cardanoscan.io/transaction/f685d279cfce4eedea32488c60331ea8d0e0b2f3015c6825959dc6c7f6f023fb?tab=metadata). However, if we delve deeper into history, we find that the pioneers were the team from Larva Labs with their [autoglyphs](https://www.larvalabs.com/autoglyphs) project, which was an ETH smart contract dated April 2019.

The NFT hype in the fall of 2021 led to the emergence of guides [like this](https://youtube.com/watch?v=9oERTH9Bkw0) on on-chain NFT mining.

The first Ergo [on-chain NFT](https://ergotokens.org/#/?token=2994d36afcfaf29bb2cfbdcc5280bdd117852ef14044bf9c01b87a83dba8b2c6) was minted on 18/8/2021. You can find the related discussion [here](https://discord.com/channels/668903786361651200/669989266478202917/1010794626338263100). This was achieved by transforming the data into a **Data URI** and encoding it into the `R9` register.

/// admonition | Size Restrictions
    type: note

There are no size restrictions for a register, only for the entire box itself, which is limited to **4 Kb**.
///


## The Technical Aspects of Regular Ergo NFTs

**What should we know about Ergo NFTs?**

Let's consider an NFT with the ID

[**47394b9319353dee45621c5a8d1ffb00cc21c946913f148df5fa4f721fefa8d0**](https://ergotokens.org/#/?token=47394b9319353dee45621c5a8d1ffb00cc21c946913f148df5fa4f721fefa8d0), also known as [AH v.1 link](https://v1.ergoauctions.org/#/auction/specific/f5c660c3b9b4c2c17b98c094126134d3aacca977efe036dd41ab34b43fcfad71).

Here's how the NFT's name, description, and URL are stored on each Ergo node, among the [40 GB+](https://explorer.ergoplatform.com/en/charts/blockchain-size) of all blockchain data.

+ **NFT minting transaction** on Ergo explorer: [Tx](https://explorer.ergoplatform.com/en/transactions/153051163bdaeae8ff31dab0ea15e48bfe97b2f60e57fe30de08d9e102389df9)

+ **NFT name** stored in register `R4`:
![NFT_R4](https://github.com/ergoplatform/ergodocs/assets/99899807/ad99a442-6569-4f66-b3e2-3c0279bc28ec)

+ **NFT description** stored in register `R5`:
![NFT_R5](https://github.com/ergoplatform/ergodocs/assets/99899807/59e3428b-2ed5-45dc-aca3-29c77dbd3a05)

+ **NFT image URL** stored in register `R9`:
![NFT_R9](https://github.com/ergoplatform/ergodocs/assets/99899807/5f5838ca-ae99-43eb-aab4-d2d774c3ff83)

>You can convert hex to string [online](https://string-functions.com/hex-string.aspx)

This is the underlying structure of the majority of NFTs on all blockchains (Ergo, Cardano, Ethereum, etc). In essence, only the name, description, and image link are stored on the blockchain (other technical parameters depending on the blockchain/NFT standard have been omitted for simplicity).
The image itself is stored on a third-party storage service (like ipfs, imgbb.com, etc).