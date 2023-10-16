---
tags:
  - dApp-Live
---

# ErgoMixer

ErgoMixer is a pioneering solution in the crypto space, being the **first *non-custodial, programmable, non-interactive* mixer**. It also stands out as the only known **token mixer**. 

You can download the latest release of ErgoMixer [here](https://github.com/ergoMixer/ergoMixBack/releases).

ErgoMixer leverages Ergo's [**Sigma protocols**](/dev/scs/sigma) to facilitate efficient and trustless mixing of funds, thereby ensuring a high level of privacy and security.

## Features

ErgoMixer comes with a host of features including:

- [Covert Addresses](#covert-addresses)
- [Stealth Addresses](#stealth-addresses)
- Token Mixing
- [SigmaUSD](sigmausd.md) minting
- Tor support
  



## Covert Addresses

ErgoMixer allows you to configure a covert address. This is useful when you want to publicly display an address to receive funds. You can set this address to automatically mix and withdraw your erg or sigUSD, as per your preference.

## Stealth Addresses

Stealth addresses are a tool to maintain recipient privacy.

With a stealth address, the recipient's privacy is preserved without the need for per-transaction interaction. This means that a receiver can publish an address, for example, on a website, and the sender can generate a unique one-time address from it.

For more technical information see the dedicated [stealth addresses](stealth-address.md) page.

As of ErgoMixer version 4.4.0, stealth addresses are supported!

As a receiver, you can create and manage your Stealth Addresses using ErgoMixer. Please note that stealth addresses are not directly payable. If you are a sender, you can use the tool located at [ergomixer.github.io/stealth/](https://ergomixer.github.io/stealth/) to create a Stealth Payment Address and use this address as a regular address.



## Efficiency Comparison

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |


## Tor Support

Starting from ErgoMixer v3.0.0, Tor support is available.

## Learning Resources

To understand ErgoMixer better, you can refer to the following resources:

**Introductory Articles**

- [Ergo: What are *'Mixers'* ?](https://ergoplatform.org/en/blog/2021-05-19-ergo-what-are-bitcoin-mixers/)
- [ErgoMixer ELI5](https://ergoplatform.org/en/blog/2021-05-12-ergomixer/)

**Video Tutorials**

- [ErgoMixer Tutorial - Taking Fire](https://www.youtube.com/watch?v=Cc3n8CjaGPE)
- [How to set up and configure mixer on Windows](https://www.youtube.com/watch?v=03_2HH82Plw)
- [Video: How to mix tokens with ErgoMixer](https://www.youtube.com/watch?v=T9M6j6xfx4w)

**Technical Documentation**

- [Technical Paper](https://eprint.iacr.org/2020/560.pdf)
- [Presentation](https://ergoplatform.org/docs/CBT_2020_ZeroJoin_Combining_Zerocoin_and_CoinJoin_v3.pdf)
- [GitHub](https://github.com/ergoMixer/)


## Additional Resources

For more information and help, you can refer to the following resources:

- [A tutorial for importing magnum (or any other wallet)](https://www.ergoforum.org/t/magnum-wallet-closing-in-20-days/468/6)
- [Second ErgoMix vulnerability blog post (fixed in 2020)](https://blog.plutomonkey.com/2020/09/another-ergomix-vulnerability/) 
- [2020: ErgoMixer, ZeroJoin Mixer for ERG and Tokens](https://www.ergoforum.org/t/ergomixer-zerojoin-mixer-for-erg-and-tokens/318)
- [2019: ErgoMix: approximately fair mining fees](https://www.ergoforum.org/t/ergomix-approximately-fair-mining-fees/110)
- [2019: Paying fee in ErgoMix in primary tokens](https://www.ergoforum.org/t/paying-fee-in-ergomix-in-primary-tokens/73)
- [More on ergoforum.org](https://www.ergoforum.org/search?q=ergomixer)
- [Join #ergomixer on Discord](https://discord.gg/jFZDGqquXE)


