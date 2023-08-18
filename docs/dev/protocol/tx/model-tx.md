---
tags:
  - Data Model
---

# Understanding Model Transaction

The UTXO (Unspent Transaction Output) model, which we use, can be a bit confusing if you're used to the Account model. Here's a simple way to understand it: In the Account model, you have a single account where you receive your coins. In the UTXO model, every transaction creates a new "box", and your balance is the sum of all the boxes linked to your addresses.

In other words, your Yoroi private key can consist of multiple boxes within a single address to hold your coins.

![](https://lh6.googleusercontent.com/qxEWrauKaD8yEXAjwXFzlikSNAXFeAxSPwuxUolS410Xf5HgOzJh_1vCL6YOfFfOyWnBhxLVIWZ0scz4BbIF9w4Tm_9aywTKo3EIrvG0zSPhCIPvLoyrlwgvZCHWHqEfXZb43klV=s0)

When you generate a new address, a secondary box is created to hold your coins. Once created, you can send funds to this new address. These funds will be linked with your private key. You can create an unlimited number of new boxes to hold your coins. Therefore, every receiving and spending action will also create an additional unique box.

This feature can initially create misconceptions. When you make a transaction, the network scans your "boxes" to verify if you have your tokens and then initiates the transaction. 

Things get complex after this point because you can not predict which boxes are going to be spent. Let's say you have three different receiving addresses. You received a couple of coins in each of them, and you want to spend some of your coins. In a Yoroi wallet, you can hold any Ergo native coins such as SigRSV or SigUSD. When you initiate a transaction that accesses the boxes of these coins, you will see that they are taken away and then redeposited. Recently, an Ergonaut raised the following [question](https://www.reddit.com/r/ergonauts/comments/prn7x3/comment/hdty87z/?utm_source=share&utm_medium=web2x&context=3): 

> "I just created a Yoroi Nightly wallet. I transferred 31 Erg from my main Yoroi wallet to the Yoroi Nightly wallet. The transaction shows 31 Erg plus a small fee, 0.0011. But it also says +92,000 SigRSV. My balance shows no change in SigRSV. What is the meaning of the +92,000 SigRSV in the transaction?"

Let's break down this particular [transaction](https://explorer.ergoplatform.com/en/transactions/143f5ba0ee1482d332d1020c94f261399f220c7f4523063ade8290c478acbd29):

![](https://lh5.googleusercontent.com/HOFhlYx5l3wvUzET-wa9E4dhU8az4srODa_4n09qZm3y-gWQz1L9Obw5qobgQM5Bthokn8SYMuO13cLDNEW5fqbboSj3qAwf2rzYH1rHkyvaoDsIMSDa3zwJU31s5XLEc_n5VbZ0=s0)

To make a transaction of '31 ERG`,  the wallet selected three of the boxes with ERG:

* A box containing `0.029595 ERG` that was received on `07/19/21`
* A second box containing `19.76 ERG` that was received on `07/19/21`
* A third box containing `208.26 ERG` that was received on `06/09/21`

On the left section of the image above, you will see approximately 228 ERG taken, while on the right section, you will see 31 ERG sent and 197 ERG redeposited to your wallet.

So your wallet used three of your boxes to spend the desired amount. This action includes all the assets in that box to the transaction. 

After the desired amount is spent, your funds are simply refunded to your address in a newly created UTXO box or boxes. Therefore, spending any coin in a box means spending the whole box and creating a new UTXO box, which is why you see your tokens are taken away and then redeposited.

The selection of which boxes to spend is determined by the wallet's random selection strategy. Whatever coins are in the selected boxes, be it SigRSV, SigUSD or NFT will be displayed as per the example. 

## Summary

The Account model contains a single box, and this box is not spent. It remains the same so that non-related coins will remain unaffected.

The UTXO model, on the other hand, contains a set of boxes that represents the total amount of the user's balance and the unspent transaction output has to change with each spending transaction.  

You may see a long list of tokens when swapping just 5 SigRSV as below:![](https://lh6.googleusercontent.com/wK-uprlqrj6wKt74AODkxBt6xR5Dey_qGB4kclXm5OuhWz2nfIuBTZm412oFA1h0OHXRi_oGcx6y7jR6A6kRcgpAUU7vSaQrfAMY6lKzdzy8THl2Hh2uEMzHjs5M5Sdlly6DO8f4=s0)

This is how UTXO model Transaction works - its storage is different from the Accounts model. In the UTXO model, coins will be stored in one-use UTXO boxes and not in long-living accounts.

