---
tags:
  - UTXO
  - Box Modeling
  - Data Model
---
# Ergo Box Design: A Comprehensive Guide

*(Back to: [Box Overview](../box.md) | [Registers](registers.md))*

The [UTXO (Unspent Transaction Output)](eutxo.md) system is the backbone of many blockchain networks, and at its core are [**boxes**](box.md). These boxes are not just containers for the value of a currency within a blockchain; they are also equipped with [**registers**](registers.md) that are protected by a [contract](ergoscript.md), enhancing their functionality on the Ergo blockchain.

Registers are essentially storage units for data and information at specific [addresses](address.md) in the blockchain. To visualize this, think of these boxes as advanced storage units or containers. For instance, consider a cup:

**A Cup:**

- Holds liquid primarily
- Can contain a certain quantity of liquid

Now, let's translate this into a blockchain context:

**A Cup Box:**

- Stores only Ergs or a specific [token](tokens.md)
- Has a storage limit enforced by a guard [script](ergoscript.md)

A guard script or [smart contract](ergoscript.md) sets restrictions on the box. Without it, a box is just a storage unit for information or a certain amount of currency. The introduction of guard scripts, which establish specific rules for the boxes, adds a level of control and functionality to the boxes, much like a remote control. The focus here is not on the internal workings of a remote control (guard script) or the data it transmits (registers and storage), but on its functionality - pressing a button changes the TV channel.

## Understanding Box Modeling

Box modeling is a framework that aids developers or box designers in creating a box to perform specific tasks. This structure promotes a clear and systematic understanding of a box's roles and operational mechanics.

## Key Principles in Box Design

A blockchain serves as a financial canvas, allowing developers, engineers, and designers to build financial systems on top of it. However, design flaws can lead to [security](security.md) vulnerabilities, unscalable designs, and inefficient processes. Therefore, it's crucial to prioritize security, [scalability](scaling.md), and efficiency in design.

The three pillars of box design are:

### Security

The box should be designed to prevent exploitation by unauthorized users. Its protection script must be robust.

### Scalability

The system (involving potentially many boxes and transactions) should be designed to handle multiple concurrent requests smoothly without causing congestion or excessive fees.

### Efficiency

A straightforward design makes it easier for engineers to understand, audit, and improve the design, reducing the chance of errors.

## Box Modeling: A Step-by-Step Guide

Before diving into the principles mentioned above, it's essential to understand the basics of box modeling.

When modeling a box, consider the following:

### What is the box's purpose?

For instance, a lending box is designed to simplify the loan process within a DeFi application.

### What data should the box store?

The box's function determines the data stored in its [registers](registers.md). A lending box, for example, would store lending-related information (like loan amount, interest rate, collateral details, borrower/lender addresses) in its registers (R4-R9).

### How will the box perform its function?

This step involves thinking about the overall [transaction](transactions.md) flow, not just the individual box. It requires scripting the guard script (using [ErgoScript](ergoscript.md)) to enforce the rules and perform its intended function using the data stored in the registers and potentially data from other input boxes or [data inputs](read-only-inputs.md).

### Register Data Types

[Registers](registers.md) can store data in various formats, which can be single or multiple entries. See the [Registers page](registers.md#optional-registers-r4-r9) for a list of supported types like `Long`, `Coll[Byte]`, `GroupElement`, etc.

## Resources

- This guide is based on the [article by Keith Lim](https://keitodot.medium.com/ergo-box-m-f58f444e00d5)
- For more technical details on how boxes are represented in transactions, see the [Transaction Format](format.md) page.
