---
tags:
  - Threshold Signature
  - Multisig
  - ErgoScript
  - P2S
  - Tutorial
  - Guide
---

# 3-out-of-5 Threshold Signature

Let's say you want to create a ***ring spending contract***, where either of us can make a transaction from the same address, but we do not want anyone else to know which one of us is spending the funds. That is not possible with Bitcoin, and while Ethereum can, it would be expensive and complicated – especially with a ring size of 10 or 20 members, required for robust privacy.

With Ergo, this kind of application can be created quickly, thanks to integrating Sigma protocols in the core that enables **self-sovereign application-level privacy**: trustless scripts that can be used to access mixers or other functionality without any third parties required.

```scala
val ringScript = s"""
{
atLeast(
  3, 
  Coll(
    PK("9f8ZQt1Sue6W5ACdMSPRzsHj3jjiZkbYy3CEtB4BisxEyk4RsNk"), 
    PK("9hFWPyhCJcw4KQyCGu4yAGfC1ieRAKyFg24FKjLJK2uDgA873uq"), 
    PK("9fdVP2jca1e5nCTT6q9ijZLssGj6v4juY8gEAxUhp7YTuSsLspS"), 
    PK("9gAKeRu1W4Dh6adWXnnYmfqjCTnxnSMtym2LPPMPErCkusCd6F3"),
    PK("9gmNsqrqdSppLUBqg2UzREmmivgqh1r3jmNcLAc53hk3YCvAGWE")
  )
)
}
```

The above is an example `3-out-of-5` **threshold signature**, which can be compiled to a `P2S` address. 

Sending ergs to the [resulting address](https://wallet.plutomonkey.com/p2s/?source=ewphdExlYXN0KAogIDMsIAogIENvbGwoCiAgICBQSygiOWY4WlF0MVN1ZTZXNUFDZE1TUFJ6c0hqM2pqaVprYll5M0NFdEI0QmlzeEV5azRSc05rIiksIAogICAgUEsoIjloRldQeWhDSmN3NEtReUNHdTR5QUdmQzFpZVJBS3lGZzI0RktqTEpLMnVEZ0E4NzN1cSIpLCAKICAgIFBLKCI5ZmRWUDJqY2ExZTVuQ1RUNnE5aWpaTHNzR2o2djRqdVk4Z0VBeFVocDdZVHVTc0xzcFMiKSwgCiAgICBQSygiOWdBS2VSdTFXNERoNmFkV1hublltZnFqQ1RueG5TTXR5bTJMUFBNUEVyQ2t1c0NkNkYzIiksCiAgICBQSygiOWdtTnNxcnFkU3BwTFVCcWcyVXpSRW1taXZncWgxcjNqbU5jTEFjNTNoazNZQ3ZBR1dFIikKICApCikKfQ==) (protected by the threshold sig).

Here is a good introduction to [making a signature](https://www.youtube.com/watch?v=daP67yp-Czs&list=PLUWruihtE-HtL-JZk8Vb4Yn_H18aE3rb6&index=4).
