# Resources

This page outlines the resources available on Ergo. Also check out the [dev-tools section on sigmaverse](https://sigmaverse.io/)


## Libraries

### SDKs

- [Appkit](appkit.md) (Java)
- [Sigma-Rust](rust.md)


### Frameworks

- [Headless dApp Framework](headless.md) (Rust)
- [Mosaik](mosaik.md) (Kotlin)
- [JDE](jde.md) (JSON)

### Wrappers

- [ErgPy](https://github.com/mgpai22/ergpy) (python-jvm)
- [ergo-python-appkit](https://github.com/ergo-pad/ergo-python-appkit)

### Toolkits

- [Fleet (JS)](https://github.com/capt-nemo429/fleet)

## Blockchain

### Explorer

- [Mainnet explorer](https://explorer.ergoplatform.com/)

### Testnet

- [Testnet explorer](https://testnet.ergoplatform.com/)
    - [Using Ergo-Testnet](https://github.com/ergoplatform/ergo/wiki/Ergo-Testnet)
    - [Testnet Faucet](https://testnet.ergofaucet.org/)

### API

- [API Docs](https://api.ergoplatform.com/api/v1/docs/)
  - [Node API](https://git.io/fjqwb)
  - [Explorer API](https://git.io/fjqwN)
  - [Ergo.Watch API](https://api.ergo.watch/docs)
 - [TokenJay API](https://api.tokenjay.app/swagger-ui/index.html;jsessionid=59429AD4DF081E2E3450C2834095D427?attribute=redirectWithRedirectView)

### Test vectors

- [Ergo transaction serialization](https://git.io/fjqwX)
- [Signature scheme](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/interpreter/shared/src/test/scala/sigmastate/crypto/SigningSpecification.scala)

## Utilities

- [Miner rewards script](https://github.com/lorien/ergotools) | Simple command-line tool to find miner rewards not spent and form withdrawing transaction requests for them
- [Ergo P2S Playground](https://wallet.plutomonkey.com/p2s/?source=dHJ1ZQ==) | A web-based tool to quickly get the address corresponding to some script  
- [ergo-monitoring](https://github.com/SabaunT/ergo-monitoring) | Debug service printing out useful for developers and managers information about ergo blockchain state.

## On-Chain Analysis

- [Ergo Vision](https://github.com/CryptoCream/ErgoVision) | A wallet visualization tool to be used for investigating transactions and addresses
- [Ergo Intelligence](https://github.com/Eeysirhc/ergo_intelligence)
- [Ergo.watch](https://ergo.watch)

## Tools

- [Transaction builder](https://thierrym1212.github.io/txbuilder/) |  The application allows you to manipulate Ergo json transactions with a UI and to sign them with Yoroi, or to prepare the JSON for the Swagger API. It is also able to load the JSON of an unsigned transaction to edit it.  | [GitHub](https://github.com/ThierryM1212/transaction-builder/)  | [Video](https://youtu.be/0VhfY7osT2k)

## Burning

`4MQyMKvMbnCJG3aJ` is a P2S (Pay-to-Script) representation of “false” condition, i.e. the box is unspendable. Hash is written into R4 register of the box, in the explorer 

> It looks like `0e2047ee2cbd52be01e0876c3e0b989a0d4d5f8955200b1fab0e6eeb2b182555c2fb`, where `0e` is type descriptor (byte array), `20` is bytestring length (0x20 in hex = 32), `47ee2cbd52be01e0876c3e0b989a0d4d5f8955200b1fab0e6eeb2b182555c2fb` is the hash of the file.


## External 

- [awesome-ergo](https://github.com/ergoplatform/awesome-ergo)
- [ergonaut.space](https://ergonaut.space/)
- [ergosites.github](https://ergosites.github.io/)
- [ErgoWiki](https://github.com/ergoplatform/ergo/wiki) | The official ergoplatform GitHub wiki
- [ergotutorials.com](https://ergotutorials.com/)
