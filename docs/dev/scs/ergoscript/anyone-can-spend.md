# Anyone-Can-Spend Scripts

The simplest form of ErgoScript is a single boolean predicate. For example, `true` corresponds to the address [4MQyML64GnzMxZgm](https://wallet.plutomonkey.com/p2s/?source=dHJ1ZQ==) `4MQyML64GnzMxZgm`.

Any funds sent to this address can be spent by anyone, as the script always evaluates to `true`.

Scripts that consistently evaluate to `true`, and their corresponding boxes, are referred to as **anyone-can-spend** scripts.



```
true && (false || true)     // address NwAyzZpF2KcXAGBJvPrAH
```


