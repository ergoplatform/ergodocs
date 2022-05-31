# ERGOHACK

We've hosted three ERGOHACK events so far - which each more successful than the last! Below you can see some of the teams and projects who have origins in ErgoHack.

## [ERGOHACK I](https://ergoplatform.org/en/blog/2021-06-04-ergo-community-launches-its-first-hackathon-ergohack/)

**Participants**

- [ErgoRaffle](https://github.com/ErgoRaffle) _(now live @ [ergoraffle.io](https://ergoraffle.io))_
- [Smart Pools](https://github.com/WilfordGrimley/ErgoSmartPools) _(Inspired [GetBlok.io](https://getblok.io))_
- [Sigma Stamp](https://www.sigmastamp.ml/)
- [Simpler Joint Spending Tool](https://www.ergoforum.org/t/a-simpler-collective-spending-approach-for-everyone/476%20)
- Ergo Index Fund
- Ergo Charts

## [ERGOHACK II](https://ergoplatform.org/en/blog/2021-09-07-ergohack-ii/)

**Participants**

- [ErgoLend](https://github.com/Ergo-Lend/) _(now live @ [ergolend.org](https://ergolend.org))_
- [Minotaur Wallet](https://github.com/minotaur-ergo/minotaur-wallet)
- [Ergopad](https://github.com/Ergohack-Dashboard-Project) _(now live @ [ergopad.io](https://ergopad.io))_
- [Ergo Subpooling](https://github.com/K-Singh/ergo-subpooling) _(now live @ [GetBlok.io](https://getblok.io))_
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

---

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

- Registration - Ownership of Ergo Names can be established by minting a _Ergo Name NFT_.
- Resolution - ergo-dns service can be used to resolve Ergo Name to Wallet Address where the Ergo Name NFT currently resides.
- Transfer - When ownership of Ergo Name NFT changes, the resolution changes automatically.

The service is fully decentralised and all the ownership data is maintained on-chain.

- [Video](https://www.youtube.com/watch?v=G7glbtnAnMY)
- [Demo Website](https://ergo-names.firebaseapp.com/home)
- [Current front end code](https://github.com/jaythiya/ergodns-frontend/)
- [Back end](https://github.com/ergonames/ergo-names-backend)
- [Resolver API](https://github.com/ergonames/ErgoNames.Api)
- [contracts](https://github.com/ergonames/ergo-names-contracts)

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
> Users can connect their Yoroi or Nautilus Wallet and sign transactions. The next step is writing the ErgoScript smart contracts.
> We were also able to integrate our analytics dashboard into the bridge app and our developers will soon release our updated analytics page to track the stats of the protocol.

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

_Special thanks to `@zuozas` for the amazing Ledger illustrations._

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

## ERGOHACKFEST 

ERGOHACKFEST (or ERGOHACK IV) was a three-week long event.

To see all the final submissions, head over to the [Presentations drive](https://drive.google.com/drive/folders/12yBnyMjq0hdVhXGOlpp8X0bwcj_Wvbgh).

Below you'll find some additional links and more information for each project. 

### Azorus

An intelligence platform for UTXO Blockchains

- [Project Demo](https://www.youtube.com/watch?v=SD8bDf-nxTQ)
- [Whitepaper](https://github.com/gsblabsio/azorus)
- [IDO on ergopad](https://ergopad.io/projects/azorus)

### ColivingDAO

ColivingDAO aims to facilitate the creation, development, and operations of an ecosystem of coliving projects all over the world.

- [Website](https://colivingdao.io/)

### dAppStep

Working on interactive tutorials for dapp developers with nodejs/javascript stack exclusively

Two examples live @ [play.dappstep.com](https://play.dappstep.com/)


### ergo-graphql

- [GitHub](https://github.com/capt-nemo429/ergo-graphql)
- [Final Report](pdf/ergo-graphql_-_Final_Report.pdf)


### ErgoNation

A decentralized ID and governance project. Non-profit with full commitment to Ergo ideals.

- [Final Report](pdf/Ergo_Nation_final_report%20(1).pdf)

### ErgoSphere

> Still making some finishing touches to the UI, and started testing projects (explorer, mixer, ErgoDex-bot) with ErgoSphere

### Ergrow

A fun project involving ergo and a love for gardening.


### LETS

- [GitHub - LETS Backend](https://github.com/arkan294/LETS-backend)

> Contracts and respective tests are complete. Off-chain ergopay code is in progress. Frontend is in progress. Diagrams of transactions have been made to easily explain the LETS creation and value transfer process.



### Multisig

- [Documentation](https://github.com/lazypinkpatrick/minotaur-wallet/blob/main/doc/MultiSig.md)
- [Documentation](https://drive.google.com/file/d/1lDOKaz55N3POy2H7Rz5SGWCgAAWJtiqB/view?usp=sharing)
- [Usage Example](https://drive.google.com/file/d/1J4IdlvpqWIo1eV1wtiT2DsfPPmgmVNQb/view?usp=sharing)



> In this week, first I focus on complete signing multisig transaction using QRCode. This transaction can see in linke https://testnet.ergoplatform.com/en/transactions/7bee9e557b81b47617ada7c8cd9e9dd6b9f89483bd4f00c2e38398ebf1d94f2e after complete transaction process I focus on a centeralized server to for communicating data between wallets. I complete this server and generate a multi-sig transaction using this server. In next 2 day I will record a video of how to use multi-sig in minotaur.

### NightOwl

- [Final Presentation](https://docs.google.com/presentation/d/1LBezFjHTNC2JJdL4OFNWIbZMiyCJ5szsr-h95i1PKp8/edit)

- [Night Owl’s Weekly Update (ErgoHack Edition)](https://medium.com/@NightOwlCasino/night-owls-weekly-update-ergohack-edition-25-05-2022-aba01f8ee9f3)
- [dApp connector](https://github.com/nightowlcasino/dApp-connector-react-package)

> In the final week the team was able to finish roulette, complete two novel RNG models, create a dapp connector react package. We have a live demo and also have working swap.

### Oracle-Pools2

- [Final Report](https://docs.google.com/document/d/1YxSc0tKi86tDRU-2RRemwefZTRYBTFBwxnYuYbaOgBk/edit)

### SwampAudio

A Layer-2 Music Launchpad

- [Final Report & Summary](https://docs.google.com/document/d/1ARevOdDiUkqYLzJ3WjjsRNNkgChJebbhcxh8SSANzio/)
- [IDO Details (ergopad)](https://ergopad.io/projects/swampaudio)

### Tensile

A decentralized, open source and non-custodial trading platform that offers derivative contracts, trading with leverage and market hedging 
regarding assets offered on the Ergo blockchain.

- [Final Report](/docs/events/pdf/Tensile_Ergoscript_Course_Final_Presentation.pdf)

### RubyNFTs

- [Presentation submission](https://twotens.art/ergohack_iv.html)
- [open sourced a small lib that uses sigma_rb](https://github.com/thedlop/sigma_mint)


### SentientSWAP

> This week our team was able to successfully fork Ergo and implement our token emission parameters. Moreover, we set up a static IP master Node on a raspberry pie 4G and was able to mine blocks. However, as of right now we have yet to run a test transaction. The plan is to run a test transaction tomorrow if we don’t get the opportunity to finish it tonight. Additionally, we were able to build a mobile raspberry pi that has similar specs to the Nintendo Switch (costing ~250$USD). This establishes proof of concept for a handheld blockchain gaming device that also works as a node overcoming two major obstacles in blockchain gaming: running a full client node on a small device and circumventing companies like Apple who actively disparage/ban blockchain games from their app store. These handheld gaming devices will not only add more nodes to the network (more peers => faster confirmations => more confirmation per min, thus increasing security) but will also put blockchain technology in the hands of the next generation in a fun and easy to understand fashion.


### Loqul

Rental Protocol For Cryptocurrency Payments

### Metadex



### Platform137

> Mining from the app with dynamic selections. Clocking - fans - power - temp limits - mapping outputs from both rig data and internal gpu data. Ability to control 3 fans and both drivers where the official nvidia software isn't even proper. Analytics from minging - etc. The perfect any idiot with a gpu can mine on me tool without hassle. Possibly a built in wallet by 12 pm MTN for quick mining yet you would need to point at a node of oyur choice kaa keep it modular and microservice based to give computation to mining. The tool your grandma can use to get them dank lootz.


### Withdrew
**ergo-family-banners**

ErgoFamilyBanners wants to harness the existing talent and allow all participants to actively engage in the building and support of the Ergo ecosystem, regardless of expertise.

**WolfVentures**

WolfVentures is aiming to bring something akin to Olympus pro to Ergo. (Smart contract 1) Smart contract 2 is an evolution of that process that offers more flexibility to projects around building treasury and liquidity.

> Unfortunately we will have to exit the Hackathon. One of our key resources has a conflict with another project they are working on and wont be available until after the event is over. We wont have the product that we want to deliver ready in time. We will continue to work on the product and will circle back around in a few weeks when things are back on track.

