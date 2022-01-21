## ErgoMixer

[ErgoMixer](https://github.com/ergoMixer/ergoMixBack) is the first working non-custodial, programmable, non-interactive mixer in the cryptocurrency space. 


ErgoMixer must be run as a local application to preserve anonymity. (Mac/Windows applications [are available!](https://github.com/ergoMixer/ergoMixBack/releases)). 

### Why is this better than Tornado Cash? 

Tornado.Cash uses `zk-SNARKs`, which requires a "ceremony" to generate parameters required by the zk-SNARKs algorithm itself. This used to be done in a Multi-party-computation way, so it's enough if only one participant of the MPC set-up was honest, all others can try to cheat, and it will be secure. 

However, if all participants cheated and cooperated, they would have the ability to generate fake proofs later, and nobody will know about it.

In the specific case of tornado cash, it would mean that if all of the 1114 ceremony setup participants cheated, they could generate fake proofs and drain money from the tornado.cash smart contract.

However, if only one of them were honest, it would be secure for people to use.

ErgoMixer doesn't require this "ceremony" setup.

The computer where the MPC ceremony holds place should also be secure and destroyed after the ceremony - otherwise, it could leak keys that can be used to construct fake proofs. There's a really strong game theoric incentive to integrate some backdoor to the software or even hardware of MPC computer. 

There were even attacks (not on MPC computer but some computer somewhere), where malware transferred private keys out of the device by extremely fast blinking of LEDs on notebook (people couldn't see it, but the high fps camera could). You can even use high-frequency audio output or even "esoteric" hard to detect things like high-frequency RF noise. You would be surprised what's possible. Imagine that you are building a mixer that will hold billions of dollars, and if you are clever enough, you can introduce some genius backdoor, as I mentioned and drain mixer step by step in a clever way that nobody will know about it. So there's a huge game theoric incentive for you to do it. The same goes for the authors of the cryptographic protocol itself. 


### Resources
- [ErgoMixer GitHub](https://github.com/ergoMixer/ergoMixBack)
- Technical Paper: [ZeroJoin: Combining ZeroCoin and CoinJoin](https://eprint.iacr.org/2020/560.pdf)
- [Presentation: ZeroJoin - Combining Zerocoin and CoinJoin](https://ergoplatform.org/docs/CBT_2020_ZeroJoin_Combining_Zerocoin_and_CoinJoin_v3.pdf)
- [Video tutorial](https://www.youtube.com/watch?v=03_2HH82Plw)
- [ErgoMixer ELI5](https://ergoplatform.org/en/blog/2021-05-12-ergomixer/)
- [Ergo: What are *'Mixers'* ?](https://ergoplatform.org/en/blog/2021-05-19-ergo-what-are-bitcoin-mixers/)
- [anon2020s explaining the how ErgoMixer retains its anonymity](https://discord.com/channels/668903786361651200/762308254159863818/885284185173024799)
