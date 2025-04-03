---
tags:
  - Contracts
  - Security
  - ErgoScript
---

## Powerful But Safe Contracts

Ethereum is an exceptional platform, but there are things it does not do well. Its Turing-complete smart contracts are powerful but dangerous – as incidents from The DAO to the Parity wallet exploits have proven, with tens of millions of dollars in collateral damage. With complexity comes uncertainty and potentially catastrophic vulnerabilities. Contracts can be expensive to run and, depending on network conditions, may execute unpredictably – or not at all.

Ergo takes a fundamentally different approach to smart contract development. The team, which has extensive experience with blockchain platforms, frameworks, and organizations from NXT and Waves to Scorex and IOG, **has** adopted a declarative model for programming whereby it's always known in advance how much code will cost to run – and, indeed, whether it will run precisely as intended. While that might, on the surface, limit code complexity, it's nevertheless possible to create Turing-complete scripts by iterating processes across multiple blocks. That means Ergo can support versatile dApps that run predictably, with known costs, and don't have the dangers of unrestricted functionality.

### Sigma protocols

The platform is unashamedly conservative, basing as many features as possible on Bitcoin – after all, Bitcoin is the most battle-tested crypto network in existence. Ergo's UTXO model, PoW mining, and finite supply draw on Bitcoin's approaches to consensus and economic incentives.

But Ergo also incorporates cutting-edge research into new cryptographic processes, using Sigma protocols to enable DeFi applications that would be either complex and messy or simply impossible on other platforms. Sigma protocols are a well-known class of zero-knowledge proofs that allow developers to implement very powerful processes very elegantly. For example, what if you want to build a privacy service that allows any one of a dozen different accounts to spend funds from an address – but no one can tell who has made each transfer? Such a 'ring contract' is possible with Ethereum, but it would require a clunky and expensive workaround. With Ergo's Sigma protocols, it's possible to implement this kind of use case and many others quickly, efficiently, and – above all – securely. Sigma protocols have not been deployed in such a generic form within crypto before. Yet this kind of out-of-the-box functionality is hugely valuable, especially when no other DeFi platform offers it.

_Ergo enables new models of financial interaction, underpinned by smart contracts built on flexible and powerful Sigma protocols but easily accessible to developers._

One of the most exciting things about blockchain is the possibility of making digital agreements without trusted intermediaries. In the simplest use case, pioneered by Bitcoin, Alice can send a payment directly to Bob, wherever the two are located around the world, with no bank or trusted third party needed. However, with the functionality of a modern blockchain like Ergo, it is possible to make far more complex and sophisticated financial agreements than simple payments. Take the following example.

### Gold-backed tokens

Alice uses ERGs to purchase gold-backed tokens from Bob. Bob stores the gold in a secure vault and uses the blockchain to issue one token for every Troy ounce of gold he holds. Alice can then use these tokens freely in different contracts, transferring and trading them under whatever conditions she specifies in the smart contract code. When Alice wants to sell the tokens for physical gold, she can conduct another transaction with Bob, receiving ERG in return at the market price.

The point of blockchain contracts is to eliminate the need for trust. While the purchase transaction is now trustless, in this instance, Alice still needs to trust Bob about two things. Firstly, Bob may refuse to swap the gold tokens back to ERG at the correct price when Alice wants to sell. Secondly, Bob may default on his obligations – running away with the gold or misusing the funds he receives and operating a fractional reserve.

### Extending the contracts

We can create an Oracle or decentralized price feed to address these issues. This uses multiple external data sources to record the price of gold on the blockchain at regular intervals. This price feed will be the reference point for the redemption contract that manages the sale of Alice's gold with Bob (or any other participant). Thus, the system automatically enforces the right price when a swap takes place.

The second situation requires a third-party insurer, Charlie, whose service is also hosted on the blockchain with a smart contract. When Alice purchases gold from Bob, she additionally buys an insurance contract from Charlie. The payment can depend on factors like the amount of insurance required and Bob's reputation, managed by a decentralized feedback mechanism. Now, if Bob defaults, Alice will automatically receive the value of her gold tokens, with Charlie effectively acting as a buyer of last resort.

### Programmable contracts

There are, of course, many other example use cases like this one. We can also extend this use case by adding further economic actors. For example, Charlie may sell shares in his insurance business to Dave and other participants, providing them with a proportion of revenues to ensure he has the capital he needs to cover any liabilities from the outset.

However, even the most complex use case is simpler than general-purpose software that can be used to program any contract. After all, generalized logic must be both far-reaching and secure. Moreover, even a specialized contract comprises many steps, each of which is fairly simple. Thus, another requirement for a general-purpose platform is that it should simplify the process of writing contracts, making them as accessible (and safe) as possible. This can be achieved using template agreements with customizable parameters. For example, the insurance contract above could be based on a module with flexible parameters. This could be used and reused in many different circumstances.
