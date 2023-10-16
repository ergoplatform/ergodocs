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

A solution in Ergo can be based on a non-interactive Diffie-Hellman key exchange. 

- So a merchant, for example, is publishing its public key **g<sup>x</sup>** corresponding to the secret **x**. 
- Then the buyer with public key **g<sup>y</sup>** obtains shared secret **(g<sup>x</sup>)<sup>y</sup> = (g<sup>y</sup>)<sup>x</sup>**
- The box created by the buyer could be protected by **[ProveDLog](../../global-functions/#provedlog)(g<sup>xy</sup>** for generator **g<sup>y</sup>**).
- Unfortunately, Ergo ProveDLog in Ergo does not support custom generators, but it can be bypassed with a little Ergo magic: **proveDHTuple(g<sup>y</sup>, g<sup>y</sup>, g<sup>xy</sup>, g<sup>xy</sup>)**. 
The buyer can use a one-time secret **g<sup>r</sup>**for one-time keys.



| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |

Some [draft contracts](https://www.ergoforum.org/t/stealth-address-contract/255) are available. 

- [stealth address contract](https://www.ergoforum.org/t/stealth-address-contract/255)

Our latest ERGOHACK saw not one but two separate teams working on the stealth address concept introduced in [this forum post](https://www.ergoforum.org/t/stealth-address-contract/255)

`@aragogi` - [Stealth Scanner project + customized version of mixer in this repo](https://github.com/aragogi/Stealth-doc)

`@_jd_` - [adds addSignWithDhtData so user can sign a transaction w/ single dht tuple](https://github.com/ergoplatform/ergo-playgrounds/pull/24)

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
