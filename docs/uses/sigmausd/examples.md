## SigmaRSV (Reservecoin) Simplified
- SigmaRSV is a call option on a % of the ERG held in the reserve portion of the SigmaUSD contract
- Fees are continually added to the ERG held in reserve as users interact with the contract. This mechanism ensures liquidity and offers a mechanism of return beyond trading. SigmaRSV represents a price/book (P/B Ratio) on the ERG held in reserve.

> It is important to understand three mechanisms that influence the outcome of each user of SigmaRSV 

1. Fees accumulate as users interact with the contract. Nothing is Free. 
2. The amount of ERG held in reserve floats (up/down) as users interact with the contract.
3. The price ERG/USD floats (up/down) as users trade ERG.


### Overview

- Imagine the Reserve amount is 100 ERG.
- Alice holds SigmaRSV, which represents 10% of the (P/B Ratio) contained in the reserves.
- Alice's SigmaRSV position is a call option on 10 ERG (minus the exchange fee)
- Let's imagine the price of ERG is 2$.
- Alice's SigmaRSV represents 20$ in ERG (minus the exchange fee)

**THE BALANCE IN RESERVE CAN GO UP**

- Imagine, based on use, the reserve now holds 114 ERG.
- Alice has SigmaRSV, which represents 10% of the (P/B Ratio) contained in the reserves.
- Alice's SigmaRSV represents a call option on 11.4 ERGs.
- Let's imagine the price of ERG is still 2$.
- Alice has 22.80$ in ERG (minus the exchange fee)

**THE BALANCE IN RESERVE CAN GO DOWN**

- Imagine, based on use, the reserve now holds 90 ERG.
- Alice has SigmaRSV, which represents 10% of the (P/B Ratio) contained in the reserves.
- Alice's SigmaRSV represents a call option on 9 ERGs.
- Let's imagine the price of ERG is still 2$.
- Alice has 18.00$ in ERG (minus the exchange fee)

**THE VALUE, ERG/USD, CAN GO UP**

- Imagine, based on use, the reserve now holds 114 ERG.
- Alice has SigmaRSV, which represents 10% of the (P/B Ratio) contained in the reserves.
- Alice's SigmaRSV represents a call option on 11.4 ERGs.
- Let's imagine the price of ERG is still NOW 3$.
- Alice has a call option 34.20$ in ERG (minus the exchange fee)

**THE VALUE, ERG/USD, CAN GO DOWN**

- Imagine, based on use, the reserve now holds 114 ERG.
- Alice has SigmaRSV, which represents 10% of the (P/B Ratio) contained in the reserves.
- Alice's SigmaRSV represents a call option on 11.4 ERGs.
- Let's imagine the price of ERG is still NOW 1$.
- Alice has a call option 11.40$ in ERG (minus the exchange fee)


##  SigmaUSD (Stablecoin) Simplified

> SigmaUSD represents a call option on the dollar value of ERG held in reserve. 


SigmaUSD uses Ergo's oracle pools infrastructure to calculate and adjust the current ERG/USD exchange rate. Reserve always backs sigma USD. The price ERG/USD floats (up/down) as users trade ERG.


**BASIC OVERVIEW**

- Bobs has 20 SigmaUSD, representing a 20 USD value in ERG.
- These ERGs are held in Reserve.
- This 20$ value is backed by reserves of at least
- (4x1)(80$ of ERG)(40 ERG @ $2)
- Bob at 2$ Bob can Redeem his 20 SigmaUSD for 10 ERG (minus the exchange fee)

**ERG/USD VALUE DROPS**

- Let us imagine the price of ERG drops from $2 to $1.
- Bobs 20$ of value is backed by at least
- (4x1)(80$ of ERG)(80 ERG @ $1)
- Bob can call 20 ERG (minus the exchange fee)

**ERG/USD VALUE INCREASES**

- Let us imagine the price of ERG increases from $2 to $4.
- Bob's $20 value is backed by at least
- (4x1)(80$ of ERG)(20 ERG @ $4)
- Bob can call 5 ERG (minus the exchange fee)



### Longterm framework of SigmaUSD.
- SigmaUSD is an essential building block for a functioning DeFi System.  
- The focus for ERG now shifts to building on the foundation it has set. 
- Gateways, Dex's, Liquidity Pools, LETS systems. It is time to build use and utility. 
- The importance and significance of stable value cannot be overstated. 
- This is critical to the long-term prosperity of the Ergo Network and is important to understand. 