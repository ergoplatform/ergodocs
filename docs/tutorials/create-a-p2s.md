---
tags:
  - P2S
  - Pay-to-Script
  - ErgoScript
  - Tutorial
  - Guide
  - Crowdfunding
  - Multisig
---

# Developing Simple Pay-to-Script Applications with ErgoScript

With ErgoScript, you can create basic applications using the pay-to-script (P2S) address compiler available at [wallet.plutomonkey.com/p2s](https://wallet.plutomonkey.com/p2s/). Check out [this video tutorial](https://www.youtube.com/watch?v=d6Mf-oxaLIc) for more details. When you transmit a transaction to this P2S address, the output is locked with the script you input.

## Example Applications

Here are a few examples of what you can create:

- **Wrapped ERG**: This script lets you exchange Wrapped ERG tokens for native ERG on a trustless 1:1 basis. For more information, check out the [Wrapped ERG forum thread](https://www.ergoforum.org/t/wrapped-erg-wrapping-native-erg-as-a-1-1-token/469).

- **Crowdfunding**: This script provides a method to raise funds within a specified timeframe. The funds can only be accessed if the fundraising goal is met by the deadline. If the deadline passes without reaching the goal, the funds can be returned to the backers. See the script on [Pluto Monkey P2S](https://wallet.plutomonkey.com/p2s/?source=ewogICB2YWwgY2FtcGFpZ25JZCA9IFNFTEYuUjRbSW50XS5nZXQKICAgdmFsIGJhY2tlclB1YktleSA9IHByb3ZlRGxvZyhTRUxGLlI1W0dyb3VwRWxlbWVudF0uZ2V0KQogICB2YWwgcHJvamVjdFB1YktleSA9IFNFTEYuUjZbU2lnbWFQcm9wXS5nZXQKICAgdmFsIGRlYWRsaW5lID0gU0VMRi5SN1tJbnRdLmdldCAvLyBoZWlnaHQKICAgdmFsIG1pblRvUmFpc2UgPSBTRUxGLlI4W0xvbmddLmdldAoKICAgdmFsIGZ1bmRyYWlzaW5nRmFpbHVyZSA9IEhFSUdIVCA+PSBkZWFkbGluZSAmJiBiYWNrZXJQdWJLZXkKICAgdmFsIGVub3VnaFJhaXNlZCA9IHsob3V0Qm94OiBCb3gpID0+IG91dEJveC52YWx1ZSA+PSBtaW5Ub1JhaXNlICYmIG91dEJveC5wcm9wb3NpdGlvbkJ5dGVzID09IHByb2plY3RQdWJLZXkucHJvcEJ5dGVzICYmIG91dEJveC5SNFtJbnRdLmdldCA9PSBjYW1wYWlnbklkfQoKICAgdmFsIGZ1bmRyYWlzaW5nU3VjY2VzcyA9IEhFSUdIVCA8IGRlYWRsaW5lICYmIGVub3VnaFJhaXNlZChPVVRQVVRTKDAp

KQogICBmdW5kcmFpc2luZ0ZhaWx1cmUgfHwgZnVuZHJhaXNpbmdTdWNjZXNzCiB9).

- **3-out-of-5 Threshold Signature**: This script allows the creation of a multi-signature wallet that requires the agreement of at least three out of five participants to authorize transactions. The script can be found on [Pluto Monkey P2S](https://wallet.plutomonkey.com/p2s/?source=ewphdExlYXN0KAogIDMsIAogIENvbGwoCiAgICBQSygiOWY4WlF0MVN1ZTZXNUFDZE1TUFJ6c0hqM2pqaVprYll5M0NFdEI0QmlzeEV5azRSc05rIiksIAogICAgUEsoIjloRldQeWhDSmN3NEtReUNHdTR5QUdmQzFpZVJBS3lGZzI0RktqTEpLMnVEZ0E4NzN1cSIpLCAKICAgIFBLKCI5ZmRWUDJqY2ExZTVuQ1RUNnE5aWpaTHNzR2o2djRqdVk4Z0VBeFVocDdZVHVTc0xzcFMiKSwgCiAgICBQSygiOWdBS2VSdTFXNERoNmFkV1hublltZnFqQ1RueG5TTXR5bTJMUFBNUEVyQ2t1c0NkNkYzIiksCiAgICBQSygiOWdtTnNxcnFkU3BwTFVCcWcyVXpSRW1taXZncWgxcjNqbU5jTEFjNTNoazNZQ3ZBR1dFIikKICApCikKfQ==).
