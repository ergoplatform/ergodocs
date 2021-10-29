
__Because a blockchain is a siloed, self-contained system by design, it interacts with other blockchain protocols. Atomic Swaps enable the cross-chain exchange of digital assets, avoiding the need for centralised exchanges.__

Blockchains are excellent at decentralised value transfer within their domains. That is, you can send BTC to any Bitcoin address securely and efficiently, and you can send LTC to any Litecoin address securely and efficiently too.

But because blockchains are based on consensus between miners, they are not designed to interface with other blockchains. Trading assets on different blockchains has, therefore, traditionally involved third parties like exchanges and OTC desks – with all the risks and inefficiencies they bring.

## Cross-chain swaps

Atomic swaps solve this problem by enabling cryptocurrencies to be traded across blockchains. This allows the trustless exchange of assets quickly and efficiently. Here’s how they work in theory:

* Alice and Bob agree to exchange some cryptocurrency. Alice will send Bob 1 BTC, and Bob will send Alice 50,000 ERG. Neither party trusts the other, so neither wants to send their crypto first.
* Alice generates a secret – a long random number – and hashes it. She then creates a transaction on the Bitcoin blockchain with a script attached, locking 1 BTC and specifying a condition: when the secret (pre-image) to the hash she has created is revealed, the BTC will be sent to Bob’s address. The hash can safely be included in the transaction script because the pre-image cannot be calculated.
When the pre-image is revealed, 50,000 locked ERG will be sent from Bob’s address to Alice’s address.* Bob then similarly creates a transaction on the Ergo blockchain, including a script with the same hash Alice has used. Because Bob doesn’t have the pre-image, he can’t execute Alice’s transaction before he has created his own.
* Once Alice sees that Bob has created his transaction on the Ergo blockchain, she can publish the secret and execute his transaction. Because the pre-image is now public, Bob can also execute the script that will send him his BTC.
* Neither party can delete their transactions and scripts once they have been posted to the blockchain. They may include a condition that the transaction will expire within a certain time to avoid their coins being locked indefinitely if Alice does not reveal the secret.

* Ergo’s atomic swaps

They are called ‘atomic’ swaps because the orders are either executed in their entirety or not – a kind of fill-or-kill order. But while that’s useful up to a point, it doesn’t allow for active trading, like you would be able to do on an exchange.  

Ergo’s implementation of atomic swaps develops the concept further. It’s relatively easy to swap coins or custom tokens trustlessly across any Bitcoin-like blockchains. But beyond that, Ergo allows partial swaps. Like on a regular exchange, We can partially fill orders if that’s what the trader wants.

This means it’s possible to build a fully-fledged decentralised exchange (DEX) that enables cross-chain trading: a trustless version of existing crypto exchanges. There’s no need for any gateways, token wrapping or other potential bottlenecks or points of failure.

You can learn more about Ergo’s implementation of atomic swaps and intra-chain and cross-chain token swaps in the [ErgoScript white paper](https://ergoplatform.org/docs/ErgoScript.pdf).
