# On-chain NFTs
> *Please note:* This method is not yet included in [EIP-0004: Asset Standard](eip4.md) - [See discussion](https://discord.com/channels/668903786361651200/940209605299036170/942656843619106827)


### A bit of history

The first Ergo [on-chain NFT](https://ergotokens.org/#/?token=2994d36afcfaf29bb2cfbdcc5280bdd117852ef14044bf9c01b87a83dba8b2c6), [Auction House v.1](https://v1.ergoauctions.org/#/auction/specific/07d1c4367a2ff26492bbbb57b0cafb336aca19315646c73ab8a819fe55635152) was minted 18/8/2021, see discussion [here](https://discord.com/channels/668903786361651200/669989266478202917/1010794626338263100). This is done by converting the data into **Data URI** and then encoding it into `R9` register. There are no limits for the size of a register, howe
ver no limits for registers, just the entire box itself (**4 Kb**).

There was Cardano on-chain projects in the spring-summer of 2021, example:
[on-chain interactive NFT](https://pool.pm/6c4fd3073bca09e62e85463e3380546e49d0344e7996c4d1b4cd0bd3.SHDEMO6) where whole [HTML page with JS is stored in metadata](
https://cardanoscan.io/transaction/f685d279cfce4eedea32488c60331ea8d0e0b2f3015c6825959dc6c7f6f023fb?tab=metadata). 
But if look deeper in history we can say that first was guys from Larva Labs with [autoglyphs](https://www.larvalabs.com/autoglyphs) (ETH smart contract dated April 2019).
Thanks to the hype around NFT, in the fall of 2021, [guides](youtube.com/watch?v=9oERTH9Bkw0) to on-chain NFT mining appeared.


### Technical side of regular Ergo NFTs

What can be said about Ergo NFTs?

For example, let's take NFT with ID 
[**47394b9319353dee45621c5a8d1ffb00cc21c946913f148df5fa4f721fefa8d0**](https://ergotokens.org/#/?token=47394b9319353dee45621c5a8d1ffb00cc21c946913f148df5fa4f721fefa8d0), [AH v.1 link](https://v1.ergoauctions.org/#/auction/specific/f5c660c3b9b4c2c17b98c094126134d3aacca977efe036dd41ab34b43fcfad71)

Here's how the NFT name/description/URL is stored on each Ergo node, somewhere among the [40 GB+](https://explorer.ergoplatform.com/en/charts/blockchain-size) of all blockchain data.

+ **NFT minting transaction** on Ergo explorer: [Tx](https://explorer.ergoplatform.com/en/transactions/153051163bdaeae8ff31dab0ea15e48bfe97b2f60e57fe30de08d9e102389df9)

+ **NFT name** stored in register `R4`:
![NFT_R4](https://github.com/ergoplatform/ergodocs/assets/99899807/ad99a442-6569-4f66-b3e2-3c0279bc28ec)

+ **NFT description** stored in register `R5`:
![NFT_R5](https://github.com/ergoplatform/ergodocs/assets/99899807/59e3428b-2ed5-45dc-aca3-29c77dbd3a05)

+ **NFT image URL** stored in register `R9`:
![NFT_R9](https://github.com/ergoplatform/ergodocs/assets/99899807/5f5838ca-ae99-43eb-aab4-d2d774c3ff83)

>Convert hex to string [online](https://string-functions.com/hex-string.aspx)

This is the background of the vast majority of NFTs on all blockchains (Ergo, Cardano, Ethereum, etc). In other words, only the name, description and link to the image are stored on the blockchain (other technical parameters depending on the blockchain/NFT standard was omitted for brevity).
The picture itself is stored somewhere on a third-party storage (ipfs, imgbb.com, etc).


### Technical side of on-chain NFTs

Ergo on-chain NFTs do not use third-party storage, their images are stored directly on the blockchain, in the `R9` register of NFT box. Here is the fundamental difference with regular NFTs. But there are significant limitations (in any blockchain) for on-chain NFTs. In Ergo the size cannot exceed **4 Kb**. The actual limit is approximately **3.5 Kb**, as space is needed for the NFT name, description, and other data. It's a challenge for an artist to be able to fit something more or less interesting for a collector into such a small size.

**How to make on-chain SVG:**
 - draw something relatively simple in SVG vector format;
 - optimize your art by hand: smoothe lines, remove small details, decrease color number, etc;
 - optimize again programmatically by svg-optimizers;
 - convert your *.svg file to [**Data URI format**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs) (_there are many online/offline converters_):
 >If the data is textual, you can embed the text (using the appropriate entities or **escapes** based on the enclosing document's type). Otherwise, you can specify **base64** to embed base64-encoded binary data.
 - сheck if you fit within the **4 kb** box limit (<3.5 Kb), if not, then return to the beginning
 - place these data in `R9` register;
 - **hardest part**: [mint](https://docs.ergoplatform.com/dev/tokens/nfts/nft-examples/) NFT with a tool that allows you to manipulate the `R9` register.
  
  
### On-chain collections examples
 

**Vector Minimalism** collection:
- [Landscape #06. View from the train window](https://ergotokens.org/#/?token=62e9e8fc25e148a35e4bb99d70b810a897e78a7fd26adda0e8335a2ad17ef58c)
- [Landscape #08. Flight over the desert](https://ergotokens.org/#/?token=cf3f157c32c22749742fb0acc85aa07e6640b61290b26a89efd9e40f5070a938)
- [Monument #11. Moai](https://ergotokens.org/#/?token=1d7430bacd2a0b1d83366cfad766a8dfb221c2de80ee95ab271a29bfdf7fc0a0)
- [Monument #02. Spring Temple Buddha](https://ergotokens.org/#/?token=d935e4fa226bbd89dfc37e45f5a6bbcdee259f1368210aca61f1b6183e01c408) 
- ![VectorMinimalism](https://github.com/ergoplatform/ergodocs/assets/99899807/10efaf86-a7ba-46ec-a620-db9a4f59a29a)


**Tokenart** collection where SVG used as a container for **ASСII art**:
- [Tokenart Cat #2](https://ergotokens.org/#/?token=14435234f5fdf1bfc0f98c2186512db292266bf4ac8d0c74f6ad056dcfaf36d1)  
- [Tokenart Shark #2](https://ergotokens.org/#/?token=723f7eb846895bd0294619300488eb1974e6827e27d1624289019b42ec7252a3)
- inside svg is pure text:
     - ![svgASCII](https://github.com/ergoplatform/ergodocs/assets/99899807/02b1142b-a25d-4cc4-8092-c6026baa046c)
