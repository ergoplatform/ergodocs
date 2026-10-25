---
title: Ergo Technical Reference Lookup
description: Find Ergo transaction formats, script types, node APIs, wallet standards, and proof specifications.
tags:
 - reference
 - api
 - standards
---

# Technical Lookup

Use this page to jump to exact technical references that live in Develop, Deploy, or Reference.

## Find by Question

| Question | Reference |
| --- | --- |
| What can an ErgoScript contract access? | [Blockchain Context](blockchain-context.md), [Types](types.md), [Global Functions](global-functions.md) |
| How is a transaction signed or validated? | [Signing](signing.md), [Validation](validation.md) |
| Which specifications govern wallet integration? | [Wallet EIP Standards](eip-standards.md), [dApp Connector](dApp.md) |
| How do I check a Merkle proof? | [Merkle Proof Format](merkle-format.md), [Merkle Validation](merkle-validation.md) |

## APIs

Node API Reference:

- [Swagger Overview](swagger.md): node API overview.
- [OpenAPI Spec](openapi.md): generated node API reference.
- [Interactive Schema](swagger_api.md): browse the checked-in OpenAPI specification; use your own node’s `/swagger` to execute requests.
- [Indexed Node API](indexed-node.md): indexed-node API notes.
- [Explorer API](explorer-apis.md): explorer API usage for indexing.

## Configuration

- [Configuration Reference](configuration.md): node, network, and operator configuration index.
- [Node Configuration](conf.md): node configuration overview.
- [Full Example](applicationconf.md): full example configuration.
- [testnet.conf](testnetconf.md): testnet configuration.
- [devnet.conf](devnetconf.md): devnet configuration.

## Standards And Specs

- [EIP Index](eip.md): Ergo Improvement Proposals.
- [Wallet EIP Standards](eip-standards.md): wallet, dApp connector, ErgoPay, ErgoAuth, and payment standards.
- [Transaction Format](format.md): transaction structure reference.
- [ErgoTree Serialization](serialization.md): ErgoTree serialization reference.
- [ErgoTree Templates](ergotree-templates.md): constant-segregated templates.

## Data Model

- [Data Model Overview](data-model.md): boxes, transactions, registers, and structures.
- [Boxes](box.md): box model reference.
- [Registers](registers.md): register usage.
- [Merkle Proof Format](merkle-format.md): Merkle proof format.
- [AVL Trees](avl.md): authenticated dictionary reference.
