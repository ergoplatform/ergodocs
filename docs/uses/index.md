# Applications

> Check out [sigmaverse.io](https://sigmaverse.io/) - *your portal to the Ergo Universe* 


## Core Components

::cards::

[
  {
    "title": "Autolykos",
    "content": "The underlying Memory-hard ASIC-resistant **Proof of Work** (PoW) algorithm oriented towards GPUs. ",
    "url": "../../mining/autolykos"
  },
  {
    "title": "eUTXO",
    "content": "Ergo uses a so-called *extended-UTXO model*, which implies UTXOs with the ability to contain *arbitrary data and sophisticated scripts*. ",
    "url": "/dev/protocol/eutxo/"
  },
  {
    "title": "NIPoPoWs",
    "content": "Enable extended support of light nodes which makes Ergo friendly for end-users, allowing them to run contracts on common devices such as mobile phones without centralised intermediaries. ",
    "url": "/dev/protocol/nipopows/"
  },
  {
    "title": "Privacy",
    "content": "Ergo provides **superior access to discrete log-based zero-knowledge proofs**",
    "url": "/dev/protocol/zkp/"
  },
  {
    "title": "Scaling",
    "content": "Explore the various scaling solutions being explored on Ergo.",
    "url": "/dev/protocol/scaling/"
  },
  {
    "title": "Storage Rent",
    "content": "Storage Rent is a nominal fee incurred by unmoved boxes after four years.",
    "url": "../../mining/rent"
  },
  {
    "title": "ErgoScript",
    "content": "A simple high-level language enabling clear descriptions of contractual logic.",
    "url": "../../dev/scs/ergoscript"
  },
  {
    "title": "Oracles",
    "content": "The messengers in and out of blockchains. Ergo Blockchain’s design allows Oracle Pools, protected by *trust heirarchies*.",
    "url": "/uses/oracles"
  },
  {
    "title": "Parachains/Sidechains",
    "content": "",
    "url": "/dev/protocol/nipopow/sidechains/"
  },


]

::/cards::

## **Main** Use Cases **of Ergo**

- **Multi-Sig:** Multi-Sig or Multi Provers are helpful for the reliability of smart contracts. This kind of implementation is vital for security. So that smart contracts aren’t in control of one person but rather governed by multiple accounts. Multi-stage contracts can also be designed for punishing malicious actors trying to take control of smart contracts.
- **NIPoPoWs**: Non-interactive proofs of proof of works can be used to build an interoperable blockchain ecosystem. With NIPoPoW implementation, Ergo Blockchain can interact with the smart contracts on proof of stake networks. This would open up an integrated use case between different dApps on different blockchains. Cardano is already planning to implement side chains with NIPoPoWs in collaboration with EMURGO. 
- **Oracles:** Oracles are the messengers in and out of blockchains. They contain valuable data (e.g. price feed) so that applications work seamlessly. Ergo Blockchain’s design allows *Oracle Pools*, and this would help to create data hierarchies. A system of oracles that can be scored regarding their trust level is a significant phenomenon. 
- **Time Epoch:** Ergo Blockchain can be designed to have timed operations. For example, during an *ICO* (or *IDO*), a code in a smart contract can provide *timed-release* so that investors have a protective layer if the project owner isn’t delivering his/her promises. In Ethereum, programming such a kind of timed operation isn’t possible. 
- **Parachain/Sidechains:** This is a yet-to-develop area for Ergo Blockchain. It’s certainly possible, and we know that the implementation of parachains has a significant impact on scalability. Our core developer *Alex Chepurnoy* is about to release a paper on it, so stay tuned!

