# ErgoMixer

ErgoMixer is the **first *non-custodial, programmable, non-interactive* mixer in the space** (and it is also the only **token mixer** to our knowledge).

ErgoMixer utilises Ergo’s [**Sigma protocols**](/dev/scs/sigma) to enable efficient, trustless mixing of funds, enabling a high degree of privacy and security.



- ErgoMixer must be run as a local application to preserve anonymity. Download the latest release [here](https://github.com/ergoMixer/ergoMixBack/releases) 


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

## Features

- Token mixing
- Covert Addresses
- Stealth Addresses
- Token Mixing
- SigmaUSD minting

## *Covert* Addresses

You can configure a covert address in ErgoMixer, this is handy for displaying an address publicly to receive funds. You can set this address to automatically mix and withdraw your erg (or sigUSD if you prefer). 

## *Stealth* Addresses

- [stealth address contract](https://www.ergoforum.org/t/stealth-address-contract/255)



## Tor support

Since ErgoMixer v3.0.0 there is Tor support available.


## FAQ

### Why is this better than Tornado Cash? 

Tornado.Cash uses `zk-SNARKs`, which requires a "ceremony" to generate parameters required by the zk-SNARKs algorithm itself. This  Multi-party-computation means if only one participant of the MPC setup was honest, all others could try to cheat, and it would be secure. 

However, if all participants cheated and cooperated, they would have the ability to generate fake proofs later, and nobody will know about it.

In the specific case of tornado cash, it would mean that if all of the 1114 ceremony setup participants cheated, they could generate fake proofs and drain money from the tornado.cash smart contract.

However, if only one of them were honest, it would be secure for people to use.

ErgoMixer doesn't require this "ceremony" setup.

The computer where the MPC ceremony holds place should also be secure and destroyed after the ceremony. Otherwise, it could leak keys that a malicious attack can use to construct fake proofs. There's a really strong game theoric incentive to integrate some backdoor to the software or even hardware of MPC computer. 

There were even attacks (not on MPC computer but some computer somewhere), where malware transferred private keys out of the device by extremely fast blinking of LEDs on notebook (people couldn't see it, but the high fps camera could). You can even use high-frequency audio output or even "esoteric" hard to detect things like high-frequency RF noise. You would be surprised what's possible. Imagine that you are building a mixer that will hold billions of dollars. If you are clever enough, you can introduce some genius backdoor, as I mentioned and drain mixer step by step in a clever way that nobody will know about it. So there's a huge game theoric incentive for you to do it. The same goes for the authors of the cryptographic protocol itself. 

### Best Practices

There are several different aspects to consider;

- If you send 1000 ERG to the mixer and, after millions of rounds, withdraw all of them to one single address, you will ruin the security gain. It is very important to withdraw carefully, to several addresses and with some time intervals.
- This mixer is **non-interactive with no middle man**. You only work on your side and interact with the blockchain.
Assume the mixing as a series of *mini-mixes* (rounds). At each round, you mix with one available box from another user. (note that there is no interaction with that user. You fetch the available boxes, choose one of them, create a tx spending your box, and create two 50-50 boxes.) Only you and the other party will know the mapping, and no one else will distinguish the mapping.
- In theory, each round's distinguishability is 2^-1 for any observer but 100% for each participant.
Therefore, in theory, the final distinguishability is 2^(-rounds).
- In the worst-case practice, this distinguishability can be 100%. Consider there are only you and an attacker mixing the boxes. In each step, he knows the mapping, so he knows the final mapping. Here comes the pool size. If there are more people in the mixing pool, at least some of the boxes will be mixed with other people's, resulting in more indistinguishability.
- There is no way to differentiate between boxes in the pool; your mixer only knows yours and the mapping of last mixed boxes with others. 
- Mixer fetches the available boxes and picks one randomly.  *Note that there are some delays between mixes, and it is configurable, so the whole mixing parties are working asynchronously.*
- you can configure your mixer to mix every 10 minutes or every ten days. *the idea is if there are more than two parties in the mixing pool during your mixing period, suddenly, some of the boxes will be picked from a party that is not the attacker.*
- If you consider the whole system is only mixing by you and the attacker, or if all other parties are corrupted and conspiring with the attacker, the security is gain is zero. 
- Simply, it is a non-interactive multi-party protocol in which the colluding parties should not be ALL other parties. So, if at least one honest party is mixing in the pool, the resulting map will be indistinguishable to some degree from the attacker.

Ever wonder how the ErgoMixer clients receive Rings, Fees, Levels, etc.? [Please see this forum post for some insights](https://www.ergoforum.org/t/ergomixer-zerojoin-mixer-for-erg-and-tokens/318/10?u=anon2020s)


### Identifiability

ErgoUtils now support obfuscating entry points for ErgoMixer.

When you withdraw from the mixer to a wallet, it is obvious that that person has received some funds from the mixer and when he spends those boxes, it is also obvious that those boxes are from the mixer.

Those who care about privacy and use ErgoMixer, also probably care about not anyone being able to tell that they are using the mixer easily when they interact with their wallets. This tool is designed to address this issue.

Just create an (or more if you wish) obfuscating address with your desired hop number [here](https://ergoutils.org/#/others) and use it permanently. To use it, withdraw from the mixer to the address that is created for you; your received funds in that address will automatically go through some random addresses (randomly created outputs, both number of outputs and output amounts) and finally be received in your wallet.

As an example, try to figure out if this [transaction](https://explorer.ergoplatform.com/en/transactions/9cf412c71fc49a53f7f6ae498f22730be474127436334e5a38da92ce0d40530b) is from the mixer or not - a lot harder to figure out.

As always, utilities in ErgoUtils are completely free to use!

- [ergoutils GitHub](https://github.com/anon-real/ergoutils)
- [mixerHop.js](https://github.com/anon-real/ErgoUtils/blob/master/src/utils/mixerHop.js)

## Token

@anon2020s has minted a new token, 'FEMX', Future ErgoMixer Token.
Token Id: `83c473e4ad477b1921023f61ab5bd1550a242c287475ff1c804f029d97672ae7`

Holders of this token are eligible to be airdropped ErgoMixer's token when it is ready.

The tokenomics of the final token is not clear yet. Still, whatever it comes to be, they will airdrop some percentage of the tokens to community members, privacy and mixer related dapps, related tutorials, dapps and wallets integrating with the mixer, appkit development, ergo DAO, etc.

- [ErgoProfitSharingDapp](https://github.com/mhssamadani/ErgoProfitSharingDapp)
- [2021: ErgoMixer Tokenization ](https://www.ergoforum.org/t/ergomixer-tokenization/648)


## Resources

- [A tutorial for importing magnum (or any other wallet)](https://www.ergoforum.org/t/magnum-wallet-closing-in-20-days/468/6)
- [Second ErgoMix vulnerability blog post (fixed in 2020)](https://blog.plutomonkey.com/2020/09/another-ergomix-vulnerability/) 
- [2020: ErgoMixer, ZeroJoin Mixer for ERG and Tokens](https://www.ergoforum.org/t/ergomixer-zerojoin-mixer-for-erg-and-tokens/318)
- [2019: ErgoMix: approximately fair mining fees](https://www.ergoforum.org/t/ergomix-approximately-fair-mining-fees/110)
- [2019: Paying fee in ErgoMix in primary tokens](https://www.ergoforum.org/t/paying-fee-in-ergomix-in-primary-tokens/73)
- [More on ergoforum.org](https://www.ergoforum.org/search?q=ergomixer)
- [Join #ergomixer on Discord](https://discord.gg/jFZDGqquXE)