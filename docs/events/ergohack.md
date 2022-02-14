# ERGOHACK

We've hosted three ERGOHACK events so far - which each more successful than the last! Below you can see some of the teams and projects who have origins in ErgoHack.



## [ERGOHACK I](https://ergoplatform.org/en/blog/2021-06-04-ergo-community-launches-its-first-hackathon-ergohack/))

**Participants**

- [ErgoRaffle](https://github.com/ErgoRaffle) *(now live @ [ergoraffle.io](https://ergoraffle.io))*
- [Smart Pools](https://github.com/WilfordGrimley/ErgoSmartPools) *(Inspired [GetBlok.io](https://getblok.io))*
- [Sigma Stamp](https://www.sigmastamp.ml/)
- [Simpler Joint Spending Tool](https://www.ergoforum.org/t/a-simpler-collective-spending-approach-for-everyone/476%20)
- Ergo Index Fund
- Ergo Charts

## [ERGOHACK II](https://ergoplatform.org/en/blog/2021-09-07-ergohack-ii/)

**Participants**

- [ErgoLend](https://github.com/Ergo-Lend/) *(now live @ [ergolend.org](https://ergolend.org))*
- [Minotaur Wallet](https://github.com/minotaur-ergo/minotaur-wallet)
- [Ergopad](https://github.com/Ergohack-Dashboard-Project) *(now live @ [ergopad.io](https://ergopad.io))*
- [Ergo Subpooling](https://github.com/K-Singh/ergo-subpooling) *(now live @ [GetBlok.io](https://getblok.io))*
- [HYPO10USE: QUIDGAMES](https://github.com/hypo10use/quid-games)
- Ergo Audio


## [ErgoHack III: Privacy & Security](https://ergoplatform.org/en/blog/2021-12-21-ergohack-iii-privacy-security/)

Our biggest Hackathon yet, with thirteen teams in total participating.

### Overview


**Tooling**

- [The Delphi Project](https://hackmd.io/@abchris/S1dHZcwyc)
- [Ergo-Castanet](https://github.com/iandebeer/ergo-castanet/blob/main/docs/Conclusion.md)

**Exchange**

- [SkyHarbor](https://www.youtube.com/watch?v=nnLmTG-43m8)
- [GuapSwap](pdf/GuapSwap_-_ErgoHack3_Project_Report.pdf)
- [anetaBTC](https://medium.com/@anetaBTC/ergohack-summary-and-development-update-dad3224227b7)

**Gaming**

- [Hypo10use](https://github.com/hypo10use/quid-games)
- [NightOwl](pdf/Night_Owl_-_Ergo_Hack_lll_Presentation_Final.pdf)

**Identity**

- [ErgoDNS](https://www.youtube.com/watch?v=G7glbtnAnMY)
- [Stealth Addresses #1](https://github.com/aragogi/Stealth-doc)
- [Stealth Addresses #2](https://github.com/ergoplatform/ergo-playgrounds/pull/24)

**Wallets**

- [Nautilus](https://github.com/capt-nemo429/nautilus-wallet/pull/6)
- [SAFEW](pdf/SAFEW_ergohack3_report.pdf)
- [Satergo](https://drive.google.com/drive/folders/1ERas6ZyJpkY_7W1az5q0X88OfYu5OipC?usp=sharing)


---- 
### The Delphi Project

The Delphi Project aims to help anyone explore, run, and launch decentralized oracles on the Ergo blockchain. 

- [Website](https://delphiproject.org/#)
- [Final Report](https://hackmd.io/@abchris/S1dHZcwyc)

### NightOwl

A Decentralised Casino ontop Ergo. 

- [Website](https://dev.nightowlcasino.io/)
- [GitHub](https://github.com/nightowlcasino)
- [Slides](pdf/Night_Owl_-_Ergo_Hack_lll_Presentation_Final.pdf)

### ErgoDNS

a MVP for ergo-dns service to resolve Ergo Names to the wallet addresses. 

Features;

- Registration - Ownership of Ergo Names can be established by minting a *Ergo Name NFT*.
- Resolution - ergo-dns service can be used to resolve Ergo Name to Wallet Address where the Ergo Name NFT currently resides.
- Transfer - When ownership of Ergo Name NFT changes, the resolution changes automatically.

The service is fully decentralised and all the ownership data is maintained on-chain.

- [Video](https://www.youtube.com/watch?v=G7glbtnAnMY)
- [Demo Website](https://ergo-names.firebaseapp.com/home)


### SkyHarbor

> Sky Harbor will be the primary place to quickly buy and sell NFT’s on the Ergo blockchain using Ergo Smart Contracts. Connect your wallet and immediately put your NFT up for sale for the price you’re looking for, or buy an NFT from our verified collections. It will also be fast and efficient, making it super easy and simple to interact with the blockchain, using databases and the latest infrastructure to make the website blazing fast.

Current features:
- Buy and sell NFT's, cancel sales

Features in progress:
- DB setup to speed up retrieval of blockchain data
- Previous sales, volume and floor price of collections

- [Video](https://www.youtube.com/watch?v=nnLmTG-43m8)

### GuapSwap

Guapswap is a fully decentralized smart contract profit swapping service on the Ergo Blockchain.

- [GitHub](https://github.com/GuapSwap)
- [Project Report](pdf/GuapSwap_-_ErgoHack3_Project_Report.pdf)
  
### HYPO10USE

HYPO10USE joins us again after getting their POC live in ERGOHACKII. 

> Our Dapp, a game platform to feature various multiplayer games is still early work in progress. In the last hackathon we were focusing on how to break down game mechanics into the eUTXO model and found good examples of elaborate use cases such as the ErgoRaffle example and worked on them. This time we were focusing mainly on compiling the contracts and building the transactions and submitting them to the blockchain, which we managed to do after long debugging and troubleshooting sessions. 
> 
> **Firstly**, we have managed to create a site to trigger a new round of a game, which will be automated in the backend to generate a new round every n blocks for each game. User then can participate in this round until n-x blocks, as x will be used to evaluate the round and the winners. We start with one example but quickly will add on top of each other. We have some great ideas but we will start testing them once our framework stands and allows to quickly explore the possibilites of the Ergo infrastructure. We cannot wait to get into this phase, but first the "hard" job needs to be done. 
>
> **Secondly**, we managed to create a transaction to participate in a games round. The last step missing here is the collection of any winnings, once this is also setup, conceptually any game could be concluded, there will be variations to this model, but this is our concept for now. We were trying to do as much as we can in the frontend using angular but we saw that there are still unimplemented stuff not featuring all functions of ergo appkit, hence we still have a backend doing the composition and compilation of all the contracts.

- [Website](https://quid-game.netlify.app/)
- [Github](https://github.com/hypo10use/quid-games)
  
### ergo-castanet

ergo-castanet uses Petri Nets as a tool to define and validate Smart Contract Protocol specifications (EIP-0006), for creation of headless dApps.
Using a Colored Petri Net for Smart Contract orchestration and testing. 

- [Project Report](https://github.com/iandebeer/ergo-castanet/blob/main/docs/Conclusion.md)

### anetaBTC

> This weekend we released a sneak peek of our frontend. Over the weekend we were able to integrate Yoroi and Nautilus Wallet into the anetaBTC app.
Users can connect their Yoroi or Nautilus Wallet and sign transactions. The next step is writing the ErgoScript smart contracts.
We were also able to integrate our analytics dashboard into the bridge app and our developers will soon release our updated analytics page to track the stats of the protocol.

- [Website](http://anetabtc.io/)
- [Project Report](https://medium.com/@anetaBTC/ergohack-summary-and-development-update-dad3224227b7)

### Stealth Addresses

This hackathon seen not one, but two seperate teams working on the stealth addresses concept introduced in [this forum post](https://www.ergoforum.org/t/stealth-address-contract/255)

`@aragogi` - [Stealth Scanner project + customized version of mixer in this repo](https://github.com/aragogi/Stealth-doc)

`@_jd_` - [adds addSignWithDhtData so user can sign a transaction w/ single dht tuple](https://github.com/ergoplatform/ergo-playgrounds/pull/24)

### Wallets

With Nautilus nearing the finish line with Ledger they extended an invitation to help any other projects integrate either Ledger or the dApp connector.

> **Nautilus**

- Ledger support added using the ledgerjs-hw-app-ergo binding library
 - All ledger interactions are done, however transactions are getting rejected by the mempool due to an issue on the device app, which is being fixed by tesseract team.
- Helped another teams with dApp connector integration


*Special thanks to `@zuozas` for the amazing Ledger illustrations.*

- [Implementation](https://github.com/capt-nemo429/nautilus-wallet/pull/6)
- [Video Report](https://twitter.com/NautilusWallet/status/1493064272028393473)

> **Satergo**

Project: Implement Ledger support into Satergo

- Implemented HID for Nano S and Nano X
- Implemented Speculos Ledger emulator interface
- Implemented the Ergo Ledger app protocol in Java
- Created utils to attest and sign transactions
- Integrated Ledger support into program
 
Both the Ledger interface library and the Ergo Ledger app protocol are reusable and can easily be integrated to other Java Ergo applications.

> **SAFEW**

Implemented Ledger support and the beginnings of ErgoMixer support. 

- [Project report](pdf/SAFEW_ergohack3_report.pdf)