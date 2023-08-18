# Exploring Anyone-Can-Spend Scripts in ErgoScript

ErgoScript's most basic form is a single boolean predicate, for instance, `true`. This corresponds to the [address](https://wallet.plutomonkey.com/p2s/?source=dHJ1ZQ==) `4MQyML64GnzMxZgm`.

**Key Insights:**

1. Funds sent to this address can be spent by anyone. This is due to the script's constant evaluation to `true`.
2. Scripts that invariably evaluate to `true`—along with their corresponding boxes—are known as **anyone-can-spend** scripts.

```
true && (false || true)     // address NwAyzZpF2KcXAGBJvPrAH
```

