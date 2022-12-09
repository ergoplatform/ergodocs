# ErgoFund

ErgoFund will eventually provide a more sophisticated crowdfunding experience, with contracts for campaigns with thousands of pledges and enable [*'Self-Soverign DeFi'*](https://www.ergoforum.org/t/self-sovereign-defi/260)


- [[WIP] ErgoFund structures and contracts](https://github.com/ergoplatform/eips/pull/33) proposes the contracts and standardized box formats for announcing crowdfunding campaigns and collecting funds
- The design of the crowdfunding contracts and box templates is centred around blockchain scanning efficiency of an [off-chain](https://github.com/ergoplatform/scanner/pull/7) application
- The ErgoFund [backend](https://github.com/ergoplatform/ergofund) will be built on top of the [Scanner](https://github.com/ergoplatform/scanner)

Please see the [#ergofund](https://discord.gg/YB9WdQYHWr) channel on Discord to contribute to this project.

- A simple ErgoFund contract with an [interactive scastie playground](https://scastie.scala-lang.org/FzcCv7pzTb2lQAamWsv1MQ) is available.  
- The [pledge contract](https://wallet.plutomonkey.com/p2s/?source=ewogICB2YWwgY2FtcGFpZ25JZCA9IFNFTEYuUjRbSW50XS5nZXQKICAgdmFsIGJhY2tlclB1YktleSA9IHByb3ZlRGxvZyhTRUxGLlI1W0dyb3VwRWxlbWVudF0uZ2V0KQogICB2YWwgcHJvamVjdFB1YktleSA9IFNFTEYuUjZbU2lnbWFQcm9wXS5nZXQKICAgdmFsIGRlYWRsaW5lID0gU0VMRi5SN1tJbnRdLmdldCAvLyBoZWlnaHQKICAgdmFsIG1pblRvUmFpc2UgPSBTRUxGLlI4W0xvbmddLmdldAoKICAgdmFsIGZ1bmRyYWlzaW5nRmFpbHVyZSA9IEhFSUdIVCA+PSBkZWFkbGluZSAmJiBiYWNrZXJQdWJLZXkKICAgdmFsIGVub3VnaFJhaXNlZCA9IHsob3V0Qm94OiBCb3gpID0+IG91dEJveC52YWx1ZSA+PSBtaW5Ub1JhaXNlICYmIG91dEJveC5wcm9wb3NpdGlvbkJ5dGVzID09IHByb2plY3RQdWJLZXkucHJvcEJ5dGVzICYmIG91dEJveC5SNFtJbnRdLmdldCA9PSBjYW1wYWlnbklkfQoKICAgdmFsIGZ1bmRyYWlzaW5nU3VjY2VzcyA9IEhFSUdIVCA8IGRlYWRsaW5lICYmIGVub3VnaFJhaXNlZChPVVRQVVRTKDApKQogICBmdW5kcmFpc2luZ0ZhaWx1cmUgfHwgZnVuZHJhaXNpbmdTdWNjZXNzCiB9) supports ANY recipient contract 
so it would be possible to crowdfund to a threshold sig address (controlled via Zero-Knowledge treasury), or emission script (so the project will receive the money slowly), etc

 

## CLI

This [forum post](https://www.ergoforum.org/t/simple-crowdfunding/70) walks you through the proposal of the first campaign ever, which was to fund the [EIP1](https://github.com/ergoplatform/eips/blob/master/eip-0001.md) crowdfunding script development. There is also [Ergo Crowdfunding CLI](https://github.com/robkorn/ergo-crowdfunding-cli), a command-line tool enabling participation and interacting with crowdfunding campaigns on Ergo, and 