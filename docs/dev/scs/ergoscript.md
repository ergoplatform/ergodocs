# ErgoScript

### Tutorials

- [(Video) Learn ErgoScript By Example Via The Ergo Playground with Robert Kornacki](https://www.youtube.com/watch?v=8l2v1asHgyA)
- [ErgoScript by Example](https://github.com/ergoplatform/ergoscript-by-example)

### How-To Guides
- [Advanced ErgoScript Tutorial](https://ergoplatform.org/docs/AdvancedErgoScriptTutorial.pdf)
- [ErgoScript tutorial](https://ergoplatform.org/docs/ErgoScript.pdf)

### Explanations
- [ErgoScript Design patterns](https://www.ergoforum.org/t/ergoscript-design-patterns/222)
- [SigmaState Protocols](https://docs.ergoplatform.com/sigmastate_protocols.pdf)

### References
- [A Quick Primer on ErgoScript](https://github.com/ergoplatform/ergo/wiki/ErgoScript-Overview)
- [ErgoScript Language Description](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md)
- [FlowCards](flowcards.md) | A Declarative Framework for Development of Ergo dApps
- Compile ErgoScript directly in your browser with [ErgoScript Playground](https://wallet.plutomonkey.com/p2s/)

## Getting Started

Ergo Blockchain is a financial smart contract platform that is built on the UTXO model. Its language, “ErgoScript,” is a rich language that supports Multi-Stage Contracts based on Scala. Even if you don’t know Scala, you can get used to it easily by checking [ErgoScript](https://ergoplatform.org/docs/ErgoScript.pdf) (or [ErgoTree](https://ergoplatform.org/docs/ErgoTree.pdf) directly) to understand the logic behind it. The scripting language in itself is non-Turing complete, but applications run on the platform can be made to be Turing complete as demonstrated in [this peer-reviewed paper](https://arxiv.org/pdf/1806.10116v1.pdf).

**Simple Example**
As a simple example, the below script allows only Alice to spend a box before a certain height and only Bob to spend the box after that.

`if (HEIGHT < 100000) alicePubKey else bobPubKey `



## Proxy Contracts

Outsourcing transaction generation to an external service/dApp can be useful or even needed in various circumstances. For example, avoiding wallet limitations to generate any transaction on behalf of the user - Ergo Assembler is designed for this purpose. Another example is to scale dApps to be able to fulfill many requests without double-spending or data invalidation - SigmaUSD dApp can use proxy contracts to avoid bank double-spending and ERG/USD oracle data invalidation.

- [EIP-0017](https://github.com/ergoplatform/eips/blob/master/eip-0017.md)






