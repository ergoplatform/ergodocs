# Stealth Addresses

Stealth Addresses are a key privacy feature in Ergo. They are [DHT](diffie.md) contracts that allow spending without revealing the spender's public key. This feature is especially beneficial for maintaining the recipient's privacy in a transaction.

ErgoMixer, as of version 4.4.0, supports Stealth Addresses. As a receiver, you can create and manage your Stealth Addresses using ErgoMixer. However, it's important to note that Stealth Addresses are not directly payable. As a sender, you must use a tool to generate a Stealth Payment Address and use this as a regular address. This tool is accessible at [ErgoMixer Stealth](https://ergomixer.github.io/stealth/).

## How Stealth Addresses Work

Ergo's implementation of Stealth Addresses is based on a non-interactive Diffie-Hellman key exchange. Here's a simplified explanation:

A merchant, for instance, publishes its public key **g<sup>x</sup>**, which corresponds to the secret **x**. 
The buyer, with public key **g<sup>y</sup>**, obtains the shared secret **(g<sup>x</sup>)<sup>y</sup> = (g<sup>y</sup>)<sup>x</sup>**.
The box created by the buyer could be protected by **[ProveDLog](../../global-functions/#provedlog)(g<sup>xy</sup>** for generator **g<sup>y</sup>**).
Ergo's ProveDLog does not support custom generators, but this can be circumvented with a little Ergo magic: **proveDHTuple(g<sup>y</sup>, g<sup>y</sup>, g<sup>xy</sup>, g<sup>xy</sup>)**. 
The buyer can use a one-time secret **g<sup>r</sup>** for one-time keys.

This mechanism allows a customer to generate a one-time payment address for a store, without revealing the payment to anyone except the store owner. 

| Bitcoin           | Ethereum                           | Ergo                                 |
|-------------------|------------------------------------|--------------------------------------|
| - | - | Efficient |

## Resources

For further exploration, some [draft contracts](https://www.ergoforum.org/t/stealth-address-contract/255) are available. 

- [Stealth address contract](https://www.ergoforum.org/t/stealth-address-contract/255)

During our [ERGOHACKVI](events.md#ergohackvi), two separate teams worked on the stealth address concept introduced in [this forum post](https://www.ergoforum.org/t/stealth-address-contract/255)

`@aragogi` - [Stealth Scanner project + customized version of mixer in this repo](https://github.com/aragogi/Stealth-doc)

`@_jd_` - [adds addSignWithDhtData so user can sign a transaction w/ single dht tuple](https://github.com/ergoplatform/ergo-playgrounds/pull/24)