# ChainCash

> From [ergoforum](https://www.ergoforum.org/t/chaincash-a-spender-signed-currency-on-ergo/4015)

Currently, DeFi space has a lot of issues. Stablecoin protocols are requiring solid overcollateralization or depend on external actors to preserve peg (such as Luna Foundation Guard). No any framework to combine collaterals and trust has been proposed to the moment. As a result, DeFi is not widely used outside of cryptocurrency users circles. I am going to propose a possible solution for DeFi which can be useful in the real world.

There is long-standing interest in grassroots financial systems in the Ergo community, such as Local Exchange Trading Systems (LETS). I am going to revive less popular alternative p2p monetary system in this post, which could be more appropriate and powerful to the needs of the real world probably when backed by the Ergo blockchain. As will be shown later, this design, a spender signed currency, is allowing to issue money in form of collectively backed IOU notes with flexibility in collateralization, trust, and thus cooperation (or, otherwise, sovereignity), as well as other properties.

The idea of spender-signed currency initially was described in the paper “Peer-to-Peer Money: Free Currency over the Internet” by Kenji Saito [1], but we are adopting it to the Ergo blockchain setting. Here is the short description of the idea. Anyone can create an IOU note (for starters, let’s assume fixed denomination of 1000 JPY). If owner is going to spend it (and a receiver is going to accept the note), the owner is signing the banknote. In turn, the receiver may spend the note, and he is also obliged to sign it on spending. Thus every note in the system has a chain of signatures of ones who ever spent it. Then, if someone is willing to redeem a note it holds, he reaching last signer first, then in case of last signer’s default, a signer before the last one, and so on. Thus the more signatures a note has, the better reserves behind it are (on average), and it is receiver responsibility to accept a note or not, by observing signatures on it and making a conclusion after (unlike state money or LETS notes, which must be accepted within specified circle or area).

We adopt this idea in the following way. First, a receiver may redeem against any previous holder immediately (so not the last signer first). Second, instead of signatures we have reserve boxes, protected by a contract (single signature, multi-signature in case of DAO, and so on).
A reserve box may hold collateral in different forms (ERG, SigUSD, DexyGold, wrapped ADA tokens from Rosen etc, Comet tokens, options, NFTs, etc). A reserve box is associated with some unique (NFT) token. It is possible to withdraw from reserve boxes, but refund must be done in two-steps way, so initially announced, and after enough time (e.g. 1 month) completed, to give enough time for others to redeem.

Then every note has the same note contract, and also a commitment to previous signers (in form of AVL tree which contains unique ids of reserve box tokens), and id of current holder (next signer in the history), in form of current holder’s reserve box id. To spend a note, one needs to prove ownership for the reserve box (by satisfying reserve box protecting contract). It is not hard to support arbitrary denominations for notes (so during transfer we can have payment note output and change note output).

Then during the payment it is receiver’s responsibility to obtain history of notes, read reserve boxes and estimate backing (possibly consider some whitelists as well, so a note from a friend or known charity may be accepted with no anything backing it even). Complexity of this process could be reduced with software (its default settings or a risk profile to be chosen by user).

Interestingly, this design is about UTXO subcurrency, so monetary system encoded in UTXOs residing in Ergo UTXO set. Thus, unlike e.g. SigUSD, design here is truly eUTXO oriented. And the design is minimizing on-chain storage and decision-making. Also, I guess notes can be done on L2, even more, L1 and L2 notes can be combined (then it is up to processing software which kinds of note contracts to support, the same is true for reserve contracts).

I think ChainCash could be a good name for an implementation, but this question is open.

References:

    Kenji Saito. Peer-to-Peer Money: Free Currency over the Internet https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.98.7726&rep=rep1&type=pdf 18
