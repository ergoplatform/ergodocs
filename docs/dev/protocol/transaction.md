



### Anatomy of an Ergo transaction

Each transaction executed on Ergo consists of these three things. 

1. `One or more` **Input boxes** (source of funds). These boxes must already exist and will be destroyed. The guard script in each of these boxes will be evaluated and must return true for the transaction to be considered valid,
2. `One or more` **Output boxes** (destination of funds). These boxes will be created.
3. `Zero or more` **Data-Inputs** boxes. These are additional boxes whose data can be referenced and used by smart contracts of the inputs. The guard script in these boxes will not be evaluated.

Data inputs are unique to Ergo and not yet present in other extended-UTXO systems. Multiple transactions can share a data-input box, and it will store only a single reference to the box in the block. We can also spend a data-input box in the same transaction as long as it existed before the transaction was applied. As an example, the box with id `d2b9b6536287b242f436436ce5a1e4a117d7b4843a13ce3abe3168bff99924a1` was used as both an input and a data-input in this transaction. 

While the use of data-inputs may not be immediately apparent, they play a major role in making Ergo more friendly to DeFi applications where we want to refer to a box without needing (or having the ability) to spend it such as in decentralized order-books (DEX). For instance, the above transaction used a "timestamping service" to timestamp a box provided as data input.

A script in Ergo can refer to other boxes in the transaction. For instance, the code snippet `INPUTS(0).value > 10000 && OUTPUTS(1).value > 20000` in any of the inputs boxes would enforce that the first input and the second output boxes must have a value greater than `10000` and `20000`, respectively.

For a comparison between the logic used in eUTXO and account-based models please see [this article](https://ergoplatform.org/en/blog/2021-10-04-off-chain-logic-and-eutxo/) provides a 


## Model Transaction

You may have experienced some confusion if you have checked the explorer to view your transaction details. The UTXO model is criticially different from the Account model via the concept of "boxes" we introduce for data-keeping. In the Accounts model, there is a single account where you receive your coins. In the UTXO model, however, every tx (transaction) creates a new box, and your balance is the sum of all the boxes linked to your addresses.

To be clear, your Yoroi private key can consist of more than one box in a single address to hold your coins.

![](https://lh6.googleusercontent.com/qxEWrauKaD8yEXAjwXFzlikSNAXFeAxSPwuxUolS410Xf5HgOzJh_1vCL6YOfFfOyWnBhxLVIWZ0scz4BbIF9w4Tm_9aywTKo3EIrvG0zSPhCIPvLoyrlwgvZCHWHqEfXZb43klV=s0)


As you generate a new address, you will create a secondary box to hold your coins. After it is created, you can send funds to this new address, and your funds will be seen as one with your private key. You can create an infinite number of new boxes to hold your coins. As such, every receiving and spending action will also create an additional unique box.



This feature can create misconceptions by the user at first glance. When you make a transaction, the network scans your "boxes" to verify if you have your tokens and then initiates the transaction. 



Things get complex after this point because you can not guess which boxes are going to be spent. Imagine you have three different receiving addresses. You received a couple of coins in each of them, and you want to spend some of your coins. In a Yoroi wallet, you can hold any Ergo native coins such as SigRSV or SigUSD. When you initiate a transaction that accesses the boxes of these coins, you will see that they are taken away and then redeposited. Recently, an Ergonaut raised the following [question](https://www.reddit.com/r/ergonauts/comments/prn7x3/comment/hdty87z/?utm_source=share&utm_medium=web2x&context=3): 



"I just created a Yoroi Nightly wallet. I transferred 31 Erg from my main Yoroi wallet to the Yoroi Nightly wallet. The transaction shows 31 Erg plus a small fee, 0.0011. But it also says +92,000 SigRSV. My balance shows no change in SigRSV. What is the meaning of the +92,000 SigRSV in the transaction?"



Let's take a look at the details of this particular [transaction](https://explorer.ergoplatform.com/en/transactions/143f5ba0ee1482d332d1020c94f261399f220c7f4523063ade8290c478acbd29):



![](https://lh5.googleusercontent.com/HOFhlYx5l3wvUzET-wa9E4dhU8az4srODa_4n09qZm3y-gWQz1L9Obw5qobgQM5Bthokn8SYMuO13cLDNEW5fqbboSj3qAwf2rzYH1rHkyvaoDsIMSDa3zwJU31s5XLEc_n5VbZ0=s0)



To make a transaction of '31 ERG`,  the wallet selected three of the boxes with ERG:

* A box containing `0.029595 ERG` that was received on `07/19/21`
* A second box containing `19.76 ERG` that was received on `07/19/21`
* A third box containing `208.26 ERG` that was received on `06/09/21`



On the left section of the image above, you will see approximately 228 ERG taken, while on the right section, you will see 31 ERG sent and 197 ERG redeposited to your wallet.



So your wallet used three of your boxes to spend the desired amount. This action includes all the assets in that box to the transaction. 



After the desired amount is spent, your funds are simply refunded to your address in a newly created UTXO box or boxes. Therefore, spending any coin in a box means spending the whole box and creating a new UTXO box, which is why you see your tokens are taken away and then redeposited.



The selection of which boxes to spend is a secret of the wallet's random selection strategy. Whatever coins are in the selected boxes, be it SigRSV, SigUSD or NFT, will be displayed as per the example. 



## Summary



The Accounts model contains a single box, and this box is not spent. It remains the same so that non-related coins will remain unaffected.



The UTXO model, on the other hand, contains a set of boxes that represents the total amount of the user's balance and the unspent transaction output has to change with each spending transaction.  



You may see a long list of tokens when swapping just 5 SigRSV as below:![](https://lh6.googleusercontent.com/wK-uprlqrj6wKt74AODkxBt6xR5Dey_qGB4kclXm5OuhWz2nfIuBTZm412oFA1h0OHXRi_oGcx6y7jR6A6kRcgpAUU7vSaQrfAMY6lKzdzy8THl2Hh2uEMzHjs5M5Sdlly6DO8f4=s0)



This is how UTXO model Transaction works - its storage is different from the Accounts model. In the UTXO model, coins will be stored in one-use UTXO boxes and not in long-living accounts.


