UTXO has many advantages over the account-based model used by Ethereum. It provides superior:

- Privacy, as UTXOs are one-time objects making it possible to formalise privacy leaks.
- Scalability, as parallel transaction processing is more straightforward in UTXO. UTXOs are also more friendly to known stateless client solutions.
- Interoperability, as off-chain and sidechain protocols. One-time objects are more straightforward to work with from an off-chain point of view.
- Transaction Cost Predictability, where the only on-chain action is validating the smart contracts. As a result, the transaction cost is significantly lower, and most importantly, the transaction cost is predictable, eliminating the need for ‘gas.’

ErgoScript is built considering Bitcoin’s security and privacy and the purpose of making all kinds of complex financial contracts accessible to everyone. However, Bitcoin’s design doesn’t allow loops, and building complex smart contracts on top of it aren’t possible. ErgoScript allows for self-replication; therefore, we can use it to create Turing-Complete processes in a blockchain.

Another approach to creating smart contracts in the blockchain is the Account-Based model, like on Ethereum. Ethereum’s design facilitates smart contract opeld coins, so the unspent transaction output (UTXO) show us which private key holds which coiration by processing smart contracts as accounts. In Bitcoin, there aren’t accounts that hons. Coins are in a set of addresses represented with a single UTXO. It’s also easier to include privacy schemes in this model than the Account-Based model.

Therefore, Ergo developed Bitcoin’s UTXO model to the extended UTXO model by introducing a readable UTXO design. This enables smart contracts to use UTXOs as data inputs without changing them. Therefore nodes are checking transactions rather than balances. In comparison, in Ethereum’s Account model, nodes check all accounts to validate the system.

Side by side, the UTXO model is more scalable, but it’s also more complicated to build User Interface tools. The account model provides easier access to developers, but codes are heavier on the blockchain, leading to network congestion. 

Furthermore, UTXO allows for parallel computation, and it’s easier to compute atomic swaps in a non-custodial manner. 

https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/
https://ergoplatform.org/en/blog/2021-09-26-the-utxo-alliance/


Ergo takes the most secure and well-established features of Bitcoin and implements advanced new cryptographic features on its rock-solid foundations. This series explores our choices in creating Ergo, with the first article unpacking the advantages of the UTXO model.

When you’re dealing with financial value, you cannot afford to take chances. Every architecture decision in a cryptocurrency platform has implications. While there are different ways to solve the same problem, some solutions are better tested and more reliable.

Like Bitcoin, Ergo uses the ‘UTXO’ (unspent transaction outputs) model rather than the Account model used by platforms like Ethereum. There are several reasons why we have made this choice, but first, it’s worth explaining a little about how the UTXO or ‘Box’ model works.

Most people think that the balance of an account is a simple number that is updated when you send or receive funds. This is the obvious way to approach the problem; it is effectively how money works in the real world. Your bank account has a balance that is increased or decreased when different transfers are made in and out. This is how the ‘Account’ model operates: your balance on the blockchain is altered by transactions to and from the account.

## How much dough?

The UTXO model, pioneered by Bitcoin, is quite different. You can think of this a bit like a person holding a series of lumps of bread dough. Their balance is the sum of these lumps or UTXOs. Lumps can be divided or combined before they are sent to a new address, but you always know where they came from. For example:

Alice has 100g of bread dough (100 ERG). She breaks off a lump of 75g and gives it to Bob, keeping 25g of ‘change’ for herself.
Charlie has 250g of dough. He breaks off 150g and gives it to Bob, keeping 100g of change for himself.
Bob breaks 20g of dough off the 150g lump he received from Charlie and combines the resulting 130g with the 75g he received from Alice. He gives the total of 205g to Dave, keeping the 20g change for himself.
Dave now has 205g of bread dough, which used to belong to Charlie. Before Charlie owned it, 75g used to belong to Alice, while 130g belonged to Bob.

In the UTXO model, ‘lumps’ of coins can be combined and divided, but they aren’t mixed together, unlike bread dough. You can follow the history of funds right back to the Coinbase transaction in which those coins were first mined. That’s very different to the Account model, where the balance of each account is simply changed. (You can, of course, check the blockchain to make sure the Account says what it should, but that’s not intrinsically necessary like it is with the UTXO approach.)

## Why UTXO?

The UXTO model has several implications. For a start, each object is immutable – lumps of coins cannot be ‘edited’ like an Account balance is edited when a transaction is made. The balance is calculated from the transaction history, right back to when those coins first came into existence. 

That makes security much simpler because either a UTXO exists in the form you are expecting, or it does not exist at all. With the account model, you need to carefully check that the account you’re dealing with is in the state it should be (and developers typically don’t do that correctly). This also makes UTXOs more friendly for off-chain protocols, like sidechains and the Lightning Network.

Accounts make it easier to store the ‘state’, but easy doesn’t always mean better. With Ergo’s extended UTXO model, state transitions are more explicit and cleaner – there are no unwanted surprises. It might be a bit more burdensome to deal with, but it’s a lot better and more straightforward in terms of security.

## Data Inputs
- [Unlocking The Potential Of The UTXO Model](https://github.com/Emurgo/Emurgo-Research/blob/master/smart-contracts/Unlocking%20The%20Potential%20Of%20The%20UTXO%20Model.md)
- [Building A Portable And Reusable (PaR) UTXO dApp Standard](https://www.ergoforum.org/t/building-a-portable-and-reusable-par-utxo-dapp-standard/441)
- [Data Inputs Semantics](https://www.ergoforum.org/t/data-inputs-semantics/654)
- [Multi-Stage Protocol Off-Chain & On-Chain Development Workflow](https://www.ergoforum.org/t/multi-stage-protocol-off-chain-on-chain-development-workflow/269)