# Autolykos

## Getting Started

::cards::

[

  {
    "title": "Governance",
    "content": "Learn more about governance on Ergo.",
    "url": "governance.md"
  },
  {
    "title": "Storage Rent",
    "content": "Storage Rent is a nominal fee (.14ERG per 4 years from an unmoved box)",
    "url": "rent.md"
  },
  {
    "title": "Difficulty Adjustment",
    "content": "",
    "url": "difficulty.md"
  },

]

::/cards::

## Key Points

- Autolykos v1 originally had pool-resistance built-in through the use of non-outsourceable puzzles.
- **The Hardening Hard-Fork** on block `417,792` marked the launch of Autolykos v2, enabling mining pools. See this [paper](https://ia.cr/2020/044). 
- [**EIP27:**](../dev/protocol/eip27) was passed with overwhelming community support, extending emission by 4,566,336 blocks (~17.38 years). This will be activated on block `777217`


Autolykos, named after the Greek God Autolycus for the original non-outsourcability built-in in version one. However, it became apparent that pool resistance was infeasible due to large players having an advantage with smart contracts. ["Bypassing Non-Outsourceable Proof-of-Work Schemes Using Collateralized Smart Contracts"](https://ia.cr/2020/044) was presented by Alex Chepurnoy at the WTSC workshop associated with Financial Cryptography and Data Security 2020 in Malaysia.




## Resources

- [Yellow Paper](https://www.docdroid.net/mcoitvK/ergopow-pdf)
- [ergo/src/main/scala/org/ergoplatform/mining/](https://discord.com/channels/668903786361651200/668903786902847502/990962713675055114)

### Test Vectors 

- [Test vectors for increased N values ](https://www.ergoforum.org/t/test-vectors-for-increased-n-values/2887/2)

- [Ergo Emission: details, retargeting via a soft fork](https://www.ergoforum.org/t/ergo-emission-details-retargeting-via-a-soft-fork/2778/2)


