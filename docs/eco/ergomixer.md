---
tags:
  - dApp-Live
---

# ErgoMixer

ErgoMixer is the **first *non-custodial, programmable, non-interactive* mixer in the space** (and the only **token mixer** to our knowledge). 

Download the latest release [here](https://github.com/ergoMixer/ergoMixBack/releases)

ErgoMixer utilises Ergo's [**Sigma protocols**](/dev/scs/sigma) to enable efficient, trustless mixing of funds, enabling a high degree of privacy and security.

## Features

- Token mixing
- Covert Addresses
- Stealth Addresses
- Token Mixing
- [SigmaUSD](sigmausd.md) minting
- Tor support
  

**Introductory**

- [Ergo: What are *'Mixers'* ?](https://ergoplatform.org/en/blog/2021-05-19-ergo-what-are-bitcoin-mixers/)
- [ErgoMixer ELI5](https://ergoplatform.org/en/blog/2021-05-12-ergomixer/)

**Video Tutorials**

- [ErgoMixer Tutorial - Taking Fire](https://www.youtube.com/watch?v=Cc3n8CjaGPE)
- [How to set up and configure mixer on Windows](https://www.youtube.com/watch?v=03_2HH82Plw)
- [Video: How to mix tokens with ErgoMixer](https://www.youtube.com/watch?v=T9M6j6xfx4w)

**Documentation**

- [Technical Paper](https://eprint.iacr.org/2020/560.pdf)
- [Presentation](https://ergoplatform.org/docs/CBT_2020_ZeroJoin_Combining_Zerocoin_and_CoinJoin_v3.pdf)
- [GitHub](https://github.com/ergoMixer/)


## *Covert* Addresses

You can configure a covert address in ErgoMixer; this is handy for displaying an address publicly to receive funds. You can set this address to automatically mix and withdraw your erg (or sigUSD if you prefer). 

## *Stealth* Addresses

A tool to hide recipient privacy. 

A stealth address preserves recipient privacy without per-transaction interaction needed (so the receiver publishes an address, e.g. on its website, and then the sender can obtain some unique one-time address from it.

As a receiver, create and manage your Stealth Addresses in ErgoMixer.

Stealth addresses are not payable directly. If you are a sender, use this tool to create a Stealth Payment Address and use this address as a regular address.

https://ergomixer.github.io/stealth/


Our latest ERGOHACK saw not one but two separate teams working on the stealth address concept introduced in [this forum post](https://www.ergoforum.org/t/stealth-address-contract/255)

Some [draft contracts](https://www.ergoforum.org/t/stealth-address-contract/255) are available. 

`@aragogi` - [Stealth Scanner project + customized version of mixer in this repo](https://github.com/aragogi/Stealth-doc)

`@_jd_` - [adds addSignWithDhtData so user can sign a transaction w/ single dht tuple](https://github.com/ergoplatform/ergo-playgrounds/pull/24)

## Covert vs Stealth Addresses

Both covert addresses and stealth addresses are cryptographic methods used in the realm of digital currencies to enhance privacy during transactions. They prevent the linking of transactions to a user's public address, providing a layer of anonymity that's not typically present in standard blockchain transactions. Here's how they differ:

Covert Addresses:

1. **Function**: Covert addresses allow a user to provide a public-facing address that is not directly linked to their wallet's actual address. This is akin to using a pseudonym that forwards to your real name, protecting your identity.
2. **Use Case**: In scenarios where a user, such as a shop owner, wants to receive payments without exposing their actual wallet address to every customer. This helps in preventing tracking of transactions linked to their personal wallet.
3. **Operation**: Typically, this might involve the creation of a new address that forwards to the user's actual address, keeping the real address out of public view.

Stealth Addresses:

1. **Function**: Stealth addresses take user privacy a step further. They involve the creation of a unique, one-time address for each transaction, even if these transactions are between the same parties.
2. **Use Case**: Ideal for situations where users need to publicly display an address (like on a website) and receive numerous transactions. Since each transaction uses a unique address, it's nearly impossible to link them to each other or to the original published address.
3. **Operation**: Based on a non-interactive cryptographic procedure. The recipient publishes a public key, and the sender uses this in conjunction with their own keys to generate the one-time address. The recipient can recognize and spend funds sent to this one-time address using their private key. In Ergo's context, this involves a Diffie-Hellman key exchange, which is a method of securely exchanging cryptographic keys over a public channel.

The "Ergo magic" mentioned is a workaround specific to the Ergo platform, which doesn't natively support custom generators in its ProveDLog (Prove Discrete Logarithm) function, an essential part of the cryptographic process in creating stealth addresses. The proveDHTuple is a more advanced cryptographic function that allows for this process to happen despite the platform's limitations.

In summary, while both covert addresses and stealth addresses serve the purpose of enhancing transactional privacy, stealth addresses provide a higher level of privacy due to their per-transaction uniqueness, making transaction tracking significantly more difficult.

## Tor support

Since ErgoMixer v3.0.0, there is Tor support available.


## Resources

- [A tutorial for importing magnum (or any other wallet)](https://www.ergoforum.org/t/magnum-wallet-closing-in-20-days/468/6)
- [Second ErgoMix vulnerability blog post (fixed in 2020)](https://blog.plutomonkey.com/2020/09/another-ergomix-vulnerability/) 
- [2020: ErgoMixer, ZeroJoin Mixer for ERG and Tokens](https://www.ergoforum.org/t/ergomixer-zerojoin-mixer-for-erg-and-tokens/318)
- [2019: ErgoMix: approximately fair mining fees](https://www.ergoforum.org/t/ergomix-approximately-fair-mining-fees/110)
- [2019: Paying fee in ErgoMix in primary tokens](https://www.ergoforum.org/t/paying-fee-in-ergomix-in-primary-tokens/73)
- [More on ergoforum.org](https://www.ergoforum.org/search?q=ergomixer)
- [Join #ergomixer on Discord](https://discord.gg/jFZDGqquXE)
