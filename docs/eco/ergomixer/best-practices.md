
# Mixer Best Practices

There are several different aspects to consider;

- If you send 1000 ERG to the mixer and, after millions of rounds, withdraw all of them to one single address, you will ruin the security gain. It is very important to withdraw carefully, to several addresses and with some time intervals.
- This mixer is **non-interactive with no middle man**. You only work on your side and interact with the blockchain.
Assume the mixing as a series of *mini-mixes* (rounds). At each round, you mix with one available box from another user. (note that there is no interaction with that user. You fetch the available boxes, choose one of them, create a transaction spending your box, and create two 50-50 boxes.) Only you and the other party will know the mapping, and no one else will distinguish the mapping.
- In theory, each round's distinguishability is 2^-1 for any observer but 100% for each participant.
Therefore, in theory, the final distinguishability is 2^(-rounds).
- In the worst-case practice, this distinguishability can be 100%. Consider there are only you and an attacker mixing the boxes. In each step, he knows the mapping, so he knows the final mapping. Here comes the pool size. If there are more people in the mixing pool, at least some of the boxes will be mixed with other people's, resulting in more indistinguishability.
- There is no way to differentiate between boxes in the pool; your mixer only knows yours and the mapping of the last mixed boxes with others. 
- Mixer fetches the available boxes and picks one randomly.  *Note that there are some delays between mixes, and it is configurable, so the whole mixing parties are working asynchronously.*
- you can configure your mixer to mix every 10 minutes or every ten days. *the idea is if there are more than two parties in the mixing pool during your mixing period, suddenly, some of the boxes will be picked from a party that is not the attacker.*
- If you consider the whole system is only mixing by you and the attacker, or if all other parties are corrupted and conspiring with the attacker, the security gain is zero. 
- Simply, it is a non-interactive multi-party protocol in which the colluding parties should not be ALL other parties. So, if at least one honest party is mixing in the pool, the resulting map will be indistinguishable to some degree from the attacker.

Ever wonder how the ErgoMixer clients receive Rings, Fees, Levels, etc.? [Please see this forum post for some insights](https://www.ergoforum.org/t/ergomixer-zerojoin-mixer-for-erg-and-tokens/318/10?u=anon2020s)
