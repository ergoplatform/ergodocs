
# Mixer Best Practices

The ErgoMixer is a non-interactive, decentralized mixing protocol that enhances privacy by obfuscating the trail of transactions. To maximize the security benefits, it's essential to follow best practices:

## Withdrawal Strategy

- Avoid withdrawing all mixed funds to a single address. Instead, withdraw to multiple addresses over time intervals to maintain privacy.

## Understanding the Mixing Process

- The mixer operates as a series of "mini-mixes" or rounds, where your funds are mixed with another user's available box (UTXO) from the pool.
- There is no direct interaction between users. You fetch available boxes, select one, create a transaction spending your box, and generate two new 50-50 boxes.
- Only you and the other party involved in the round know the mapping, ensuring privacy from external observers.

## Anonymity Set and Security

- Theoretically, each round's distinguishability for an external observer is 2^-1, while it's 100% for the participants.
- The final distinguishability is 2^(-rounds) in theory, but in practice, it can be 100% if there are only two parties (you and an attacker) mixing.
- A larger pool size with more honest participants increases indistinguishability, as some boxes will be mixed with parties other than the attacker.
- The mixer cannot differentiate between boxes in the pool and only knows your boxes and the mapping of the last mixed boxes.

## Mixing Frequency and Timing

- You can configure the mixer to mix at intervals ranging from every 10 minutes to every 10 days.
- Longer intervals increase the likelihood of mixing with honest parties, reducing the attacker's ability to track your funds.

## Security Considerations

- If all other parties are colluding with an attacker, the security gain is zero.
- As long as at least one honest party is mixing in the pool, the resulting mapping will be indistinguishable to some degree from the attacker's perspective.

For more insights into how ErgoMixer clients receive Rings, Fees, Levels, and other details, please refer to [this forum post](https://www.ergoforum.org/t/ergomixer-zerojoin-mixer-for-erg-and-tokens/318/10?u=anon2020s).
