# No-one-Can-Spend Scripts

At the other end of the spectrum are ErgoScript programs that always evaluate to `false`, such as 

    true && false               // address m3iBKr65o53izn

**Notes:**    

1. Funds sent to such addresses cannot be spent by anyone and consequently such scripts are called **no-one-can-spend**. Please do not send funds to these addresses.  
2. Ergo has the concept of [*garbage collection* / storage rent](rent.md), so such boxes will eventually be removed from the blockchain over a long period.
 