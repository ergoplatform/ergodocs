---
tags:
  - UTXO
---


# Account vs UTXO


Like Bitcoin, Ergo uses the ‘UTXO’ (unspent transaction outputs) model rather than the Account model used by platforms like Ethereum. We have made this choice for several reasons, but first, it’s worth explaining how the UTXO or [Box](box.md) model works.

Most people think that the balance of an account is a simple number that is updated when you send or receive funds. This is the obvious way to approach the problem; it is how money works in the real world. Your bank account has an increased or decreased balance when different transfers are made in and out. The ‘Account’ model operates: transactions to and from the Account alter your balance on the blockchain.

The UTXO model, pioneered by Bitcoin, is quite different. This is a bit like a person holding a series of lumps of bread dough, and their balance is the sum of these lumps or UTXOs. Lumps can be divided or combined before they are sent to a new address, but you always know where they came from. For example:

Alice has 100g of bread dough (100 ERG). She breaks off a lump of 75g and gives it to Bob, keeping 25g of ‘change’ for herself.
Charlie has 250g of dough, breaks off 150g and gives it to Bob, keeping 100g of change for himself.
Bob breaks 20g of dough off the 150g lump he received from Charlie and combines the resulting 130g with the 75g he received from Alice. He gives the total of 205g to Dave, keeping the 20g change for himself.

Dave now has 205g of bread dough, which used to belong to Charlie. Before Charlie owned it, 75g used to belong to Alice, while 130g belonged to Bob.

In the UTXO model, ‘lumps’ of coins can be combined and divided, but they aren’t mixed, unlike bread dough. You can follow the funds' history back to the Coinbase transaction in which those coins were first mined. That’s very different from the Account model, where the balance of each Account is changed. (You can check the blockchain to make sure the Account says what it should, but that’s not intrinsically necessary like it is with the UTXO approach.)

### Why UTXO?

The UXTO model has several implications. For a start, each object is immutable – lumps of coins cannot be ‘edited’ like an Account balance is edited when a transaction is made. The balance is calculated from the transaction history when those coins first came into existence. 

That makes security much simpler because either a UTXO exists in the form you expect or it does not exist. With the account model, you need to carefully check that the Account you’re dealing with is in the state it should be (and developers typically don’t do that correctly). This also makes UTXOs more friendly for off-chain protocols, like sidechains and the Lightning Network.

Accounts make storing the ‘state’ easier, but easy doesn’t always mean better. With Ergo’s extended UTXO model, state transitions are more explicit and cleaner – there are no unwanted surprises. It might be a bit more burdensome to deal with, but it’s a lot better and more straightforward security.