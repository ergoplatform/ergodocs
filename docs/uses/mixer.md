## ErgoMixer

**ErgoMixer** is the first working non-custodial, programmable, non-interactive mixer in the cryptocurrency space, and it is also the only **token mixer** to our knowledge. 

ErgoMixer must be run as a local application to preserve anonymity. (Mac/Windows applications [are available!](https://github.com/ergoMixer/ergoMixBack/releases)). 

### Why is this better than Tornado Cash? 

Tornado.Cash uses `zk-SNARKs`, which requires a "ceremony" to generate parameters required by the zk-SNARKs algorithm itself. This  Multi-party-computation means if only one participant of the MPC setup was honest, all others could try to cheat, and it would be secure. 

However, if all participants cheated and cooperated, they would have the ability to generate fake proofs later, and nobody will know about it.

In the specific case of tornado cash, it would mean that if all of the 1114 ceremony setup participants cheated, they could generate fake proofs and drain money from the tornado.cash smart contract.

However, if only one of them were honest, it would be secure for people to use.

ErgoMixer doesn't require this "ceremony" setup.

The computer where the MPC ceremony holds place should also be secure and destroyed after the ceremony. Otherwise, it could leak keys that a malicious attack can use to construct fake proofs. There's a really strong game theoric incentive to integrate some backdoor to the software or even hardware of MPC computer. 

There were even attacks (not on MPC computer but some computer somewhere), where malware transferred private keys out of the device by extremely fast blinking of LEDs on notebook (people couldn't see it, but the high fps camera could). You can even use high-frequency audio output or even "esoteric" hard to detect things like high-frequency RF noise. You would be surprised what's possible. Imagine that you are building a mixer that will hold billions of dollars. If you are clever enough, you can introduce some genius backdoor, as I mentioned and drain mixer step by step in a clever way that nobody will know about it. So there's a huge game theoric incentive for you to do it. The same goes for the authors of the cryptographic protocol itself. 

## Best Practices

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


## Identifiability

You can tell if a coin is mixed or not due to its history and contract address. 

But, when you withdraw the mixed coins (during or after), there are strategies to mitigate this, such as regularly moving them around since they are regular boxes with regular contracts (like other coins in the network). This eliminates the *tainting issue* to some degree. You can do this manually or using multi-hop withdrawal (available at https://ergoutils.org/#/others).
ErgoMixer will integrate this feature in future.
"Your mixer withdrawal will go through many random addresses, and you will receive them from an ordinary address."

## Token

@anon2020s has minted a new token, 'FEMX', Future ErgoMixer Token.
Token Id: `83c473e4ad477b1921023f61ab5bd1550a242c287475ff1c804f029d97672ae7`

Holders of this token are eligible to receive ErgoMixer's token when ready.

The tokenomics of the final token is not clear yet. Still, whatever it comes to be, they will airdrop some percentage of the tokens to community members, privacy and mixer related dapps, related tutorials, dapps and wallets integrating with the mixer, appkit development, ergo DAO, etc.



### Resources

**Tutorials**

- [Video tutorial](https://www.youtube.com/watch?v=03_2HH82Plw)
- [ErgoMixer ELI5](https://ergoplatform.org/en/blog/2021-05-12-ergomixer/)
- [Ergo: What are *'Mixers'* ?](https://ergoplatform.org/en/blog/2021-05-19-ergo-what-are-bitcoin-mixers/)

**GitHub**

- [ErgoMixer GitHub](https://github.com/ergoMixer/)

**Documentation**

- Technical Paper: [ZeroJoin: Combining ZeroCoin and CoinJoin](https://eprint.iacr.org/2020/560.pdf)
- [Presentation: ZeroJoin - Combining Zerocoin and CoinJoin](https://ergoplatform.org/docs/CBT_2020_ZeroJoin_Combining_Zerocoin_and_CoinJoin_v3.pdf)


