---
tags:
  - UTXO
---
# Exploring Ergo Box Design

At the heart of a UTXO system are boxes. They serve as essential vessels carrying the value of a currency within a blockchain. The Ergo blockchain enhances this concept by equipping boxes with [registers](registers.md) that are protected by a contract.

Registers offer the capability to store data and information at specific addresses in the blockchain. Drawing a comparison with everyday items, you might envision these boxes as remote controls, supercharged piggy banks, or simple cups that only allow liquid to be poured in. Taking the cup as an example:

**A Cup:**

- Primarily used to hold liquid
- Accommodates up to a certain quantity of liquid

This can be translated into a box-like concept:

**A Cup Box:**

- Designed to store only Ergs or a specific token
- Allows storage up to a certain limit (enforced by a guard script)

A guard script or contract imposes restrictions on the box. Without this, a box is merely a storage unit for storing information or a certain amount of currency. The incorporation of guard scripts, which set particular rules for the boxes, introduces rigidity to the boxes and shapes their function, much like a remote control. We're less concerned about the internal workings of a remote control (guard script) or the data it transmits (registers and storage), focusing instead on its functionality - pressing a button changes the TV channel.

## What is Box Modeling?

Box modeling provides a structure that assists developers or box designers in crafting a box to perform certain tasks. This framework promotes a structured and straightforward approach to understanding the roles of a box and the mechanics of its operations.

## Designing a Box: Key Principles

A blockchain acts as a financial canvas, providing developers, engineers, and designers the ability to create financial systems atop it. However, any design shortcomings can lead to vulnerabilities to security breaches, unscalable designs, and inefficient processes. Thus, it is crucial to prioritize security, scalability, and efficiency during design.

Three foundational principles for box design:

##### Security

Ensure that the box is not exploitable by unauthorized users.

##### Scalability

Design the system to handle multiple concurrent requests seamlessly.

#####  Efficiency

A simple design allows engineers to understand and enhance the design effortlessly.

## Steps for Box Modeling

Before addressing the above principles, understanding the fundamentals of box modeling is essential.

While modeling a box, we should ponder:

##### What purpose does this box serve?

A lending box, for example, is designed to streamline the loan process.

##### What data should the box contain?

The function of the box determines the data stored in it. For instance, a lending box would hold lending-related information in its registers.

##### How will the box execute its function?

This step is a bit complex as it requires thinking about the overall transaction, not just the box. This stage involves scripting the guard script (or smart contract) to perform its intended function using the data stored in the registers.

### Register Data Types

Registers can store data in various formats, which can be categorized into single or multiple entries.

**Single data entries include:**

- `Long`
- `Coll[Byte]` also known as *String*
- `Bool`

**Multiple data entries include:**

- `Coll[Long]`
- `Coll[Coll[Byte]]`
- `Coll[Bool]`


> Based on the [article by Keith Lim](https://keitodot.medium.com/ergo-box-m-f58f444e00d5)
