There's a cheap way to do bonding curves on Ergo, with most of the load done off-chain.

Assume a project is willing to issue 100 tokens and sell the first one for 100 ergs, second for 200, ..., 100th for 10,000 ergs (to raise 505,000) in total in case of full sale. This is the very simple example of a bonding curve. See https://blog.relevant.community/bonding-curves-in-depth-intuition-parametrization-d3905a681e0a for more details. Bonding curves is a useful primitive for continuous token offerings (CTOs), augmented bonded curves (https://medium.com/giveth/deep-dive-augmented-bonding-curves-3f1f7c1fa751), AMM DEXes maybe. 

Sell-only 
-------------

First, assume token sale scenario only. Token issuer is creating 100 boxes with 1 token each, ैwith setting price for the token in register R4 of a box. The box is spendable if spending transaction is paying the price to the issuer's address (issuer's script in general). 


Sell with buy-back
--------------------------

Now assume that token sell is coming with buy-back guarantee, e.g. seller is buying back tokens within 1 year since sell for 95% of the selling price. In this case the selling contract is requiring spending transaction to lock 95% of the price at least with buying contract. Buying contract is time-locked and also requiring from spending transaction to send token bought-back to a predefined address (e.g. issuer's).


Clients
----------

As the curve is made upon many boxes, some work required on the client-side, namely possibility to find boxes associated with the token and also selling-script, and then sort the boxes by R4.