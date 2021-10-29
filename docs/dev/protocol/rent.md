> Participate in community discussions around soft-fork! [Ergo Emission: details, retargeting via a soft-fork](https://www.ergoforum.org/t/ergo-emission-details-retargeting-via-a-soft-fork/2778)

__We’ve designed Ergo with long-term economic sustainability in mind, and storage rent is one of the ways we’re ensuring miners stay profitable well into the future. One community member, Robert, describes this function as ‘on-chain garbage collection’ that reduces the problem of blockchain bloat – and even makes it profitable.__

The 2020 block reward reduction will probably be the most important halving Bitcoin ever experiences. This is the point where the narrative of programmatic scarcity and digital gold will truly be proven, in the context of the sharpest economic downturn in living memory. In previous halvings, Bitcoin has still been in its infancy, a niche experiment. Future halvings will confirm the principle. But this one is the watershed.

Looking ahead, though, what happens in 20 or 30 years, when block rewards have fallen so far that miners have to rely on tx fees and potentially other sources of revenue? Will Bitcoin be sustainable? What will be the impact on the ecosystem?

The simple answer is that we don’t know.

Mining rewards are a key feature in maintaining the security of proof-of-work blockchains like Bitcoin and Ergo. And so, while we have deliberately kept many of Bitcoin’s tried and tested features, we have updated this one to give miners a boost when block rewards have fallen to zero.

## Lost coins

Digital scarcity is an important feature of Ergo. Like Bitcoin, ERG are designed to be a finite resource and long-term store of value. We do not agree with the principle of infinite inflation.

And yet, this has to be balanced against the needs to pay miners to secure the blockchain and process transactions. Without adequate compensation for miners, there is no viable blockchain at all. Ergo approaches this by slowly recycling lost coins, in a feature we call ‘Storage rent’. 

Studies suggest that as many as [4 million BTC may have been lost forever](https://bitcoinist.com/estimated-4-million-bitcoin-lost-forever-by-users-forgetfulness/). These are coins that were mined in the early days of Bitcoin and stored on hard drives that were subsequently thrown away or destroyed because the owners forgot about them or thought they were worthless, as well as coins in addresses for which the private keys have been lost. (And, of course, there’s Satoshi’s estimated holdings of 1 million BTC, which may never move.)

Where coins have genuinely been permanently taken out of circulation in this way, it makes sense to have a mechanism to recover them and put them back into the blockchain economy. That way, we can preserve digital scarcity without unnecessarily accelerating it. In other words, by attempting to stick to the intended algorithmic supply for any given point in time.

Ergo’s halving schedule is faster than Bitcoin’s. Block rewards start at 75 ERG, and decrease steadily after the first two years. There is no ‘long tail’ of emission, and after eight years block rewards will fall to zero. After that, total supply will be fixed. The number of ERG in existence will never be more than 97,739,925.

## Storage fees

From that point, however, miners will need further incentives to secure the network. Miners have ongoing costs in terms of bandwidth and storage, and in cases where coins are simply left for years, there is typically no charge for reflecting the value of securing them. The tx fee that is paid up-front in Bitcoin is the only charge ever made for storing those coins.

In Ergo, in addition to transaction fees, miners will also be able to collect storage rent fees on UTXOs that have not been moved for four years or more. 

Fees will be deducted slowly, over time – the unmoved UTXOs will not simply be appropriated by miners. Anyone who wants to avoid this simply needs to move their balances once every four years, which is not an onerous requirement for helping incentivise miners and avoiding the deflationary consequences of lost coins. You can read more about how fees will be levied in [this paper](https://fc18.ifca.ai/bitcoin/papers/bitcoin18-final18.pdf).

In this way, Ergo seeks to ensure a balance between maintaining digital scarcity, on the one hand, and giving miners long-term incentives to secure the blockchain, on the other – long past the point where new coins have ceased to be released.


Resources

- [Storage rent details](https://www.ergoforum.org/t/storage-rent-details/256)