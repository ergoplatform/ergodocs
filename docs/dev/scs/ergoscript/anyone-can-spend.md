# Understanding Anyone-Can-Spend Scripts in ErgoScript

The simplest possible ErgoScript is a single boolean predicate, such as `true`. This translates to the [address](https://wallet.plutomonkey.com/p2s/?source=dHJ1ZQ==) `4MQyML64GnzMxZgm`.

**Key Points:**

1. When funds are sent to this address, anyone can spend them. This is because the script always evaluates to `true`.
2. Scripts that always evaluate to `true`—and their respective boxes—are referred to as **anyone-can-spend** scripts.

Consider a more intricate version of an "anyone-can-spend" script:

```
true && (false || true)     // address NwAyzZpF2KcXAGBJvPrAH
```

This script, while more complex, still always evaluates to `true`, meaning the funds sent to its corresponding address are accessible to anyone.