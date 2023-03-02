# Anyone-Can-Spend Scripts

The simplest ErgoScript program is a single boolean predicate such as:

    true

This corresponds to the [address](https://wallet.plutomonkey.com/p2s/?source=dHJ1ZQ==) `4MQyML64GnzMxZgm`.

**Notes:**    

1. Any funds sent to this address can be spent by anyone because the script always evaluates to `true`.
2. Scripts that always evaluate to `true` (and the corresponding boxes) are called **anyone-can-spend**. 

A slightly more complex "anyone-can-spend" script is: 

    true && (false || true)     // address NwAyzZpF2KcXAGBJvPrAH 