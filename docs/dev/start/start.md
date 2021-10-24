# Where to start?

The [dApp Development](dApp-dev.md) page provides a broad overview on creating your first decentralised app. 

See the [Backend](../stack/back-end.md) page for an overview of the tools available to interact with the blockchain. This is also broken down on a per-language basis. 

## dApp Development

For most developers, [Appkit](#appkit) is the best entry point unless you're wanting to dive straight into [ErgoScript](#ergoscript) smart-contract development.

**System Architecture**

Below is a example system architecture diagram highlighting the main components of a decentralised application (dApp)


![](../assets/sys.png)

- **Front-end** | The user-interface built in your framework of choice.
    - For payments, we have the Yoroi dApp connector, proxy contracts, or Ergo-Pay. 
- **REST** | A *REST*ful API to interact with the backend
- **Backend** | Perform the off-chain logic
- **Database** (Optional) 
- **Contract** | Where the magic happens, the on-chain validation of the off-chain logic.



## Resources

### Explorer

**Explorer**

- [Mainnet explorer](https://explorer.ergoplatform.com/)

### Testnet

- [Testnet explorer](https://testnet.ergoplatform.com/)
  - [Using Ergo-Testnet](https://github.com/ergoplatform/ergo/wiki/Ergo-Testnet)
  - [Testnet Faucet](https://testnet.ergofaucet.org/)

### API

- [API Docs](https://api.ergoplatform.com/api/v1/docs/)
  - [Node API](https://git.io/fjqwb)
  - [Explorer API](https://git.io/fjqwN)

### Misc. Resources
**Test vectors:**

- [Ergo transaction serialization](https://git.io/fjqwX)
- [Signature scheme](https://git.io/fjqwH)

**Utilities** 

 - [Miner rewards script](https://github.com/lorien/ergotools) | Simple command-line tool to find miner rewards not spent and form withdrawing transaction requests for them
 - [Ergo P2S Playground](https://wallet.plutomonkey.com/p2s/?source=dHJ1ZQ==) | A web-based tool to quickly get the address corresponding to some script  

**Resources** 

- [ErgoWiki](https://github.com/ergoplatform/ergo/wiki) | The official ergoplatform GitHub wiki
- [ergosites.github.io](https://ergosites.github.io/) | Resource page which links to various websites and utilities. 
- [ergohack.io](https://ergohack.io/resources) | Your introduction to developing on Ergo.


## Basic Tutorials

- [ergotutorials.com](https://ergotutorials.com/)
- [Ergo API basic query](https://www.youtube.com/watch?v=B3W9uNwk_DM)
- [Create mini web for your NFT.](https://www.youtube.com/watch?v=mP6D9Pf6p88)