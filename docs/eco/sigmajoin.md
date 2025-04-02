---
tags:
  - Sigmajoin
  - Mixer
  - Privacy
  - Zerojoin
  - dApp
  - dApp-Research
---
# Sigmajoin 

## What is Sigmajoin?

Sigmajoin is a privacy protocol designed for use with UTXO-based blockchains, aiming to enhance user anonymity. It builds on the principles of a previous protocol called [Zerojoin](zerojoin.md) but introduces features to make it more practical and efficient.

### Key Advantages


|                        | ZeroJoin (ErgoMixer)                                                | Sigmajoin                                                    |
|------------------------|--------------------------------------------------------------------|--------------------------------------------------------------|
| **Proofs Used**        | Proofs of knowledge of Diffie-Hellman tuples                        | Proofs of knowledge of Diffie-Hellman tuples                 |
| **Interaction Level**  | Partially Non-interactive: Requires online presence for remixing    | Non-interactive                                              |
| **Outsourceability**   | No, mixing cannot be outsourced                                     | Yes, mixes can be outsourced to third-parties                |
| **Types of Boxes**    | 2 (Half-Mix and Full-Mix): Limited to two boxes, constraining scalability and flexibility | More than 2: Offers better scalability and flexibility. Half-mix boxes eliminated as bloat       |
| **Stealth Withdraw**   | Supported                                                           | Supported                                                    |
| **Fee Handling**       | Embedded Fee: Includes fees within mix boxes, requiring meticulous calculation  | Outsourced Fee: Fees paid by third-party "mixer," simplifying the process and adding flexibility  |


## Special Features

### 1. Outsourceability

The mixing process can be outsourced to a third-party service called a mixer. These mixers can perform the mixing operations in a trustless manner, meaning they cannot steal funds.

### 2. Stealth Withdraw

Sigmajoin allows for transactions that appear to be mixes but are actually withdrawals. This makes it even more difficult for an observer to trace transactions, enhancing privacy.

### 3. Outsourced Fee

In many privacy protocols, how to pay the mining fee is a challenge. Sigmajoin allows the fee to be paid by the third-party mixers, further simplifying the process for users.

## How Does Sigmajoin Work?

### Basics

- **Mix-box**: A special kind of coin (or UTXO) used in Sigmajoin. Each mix-box has two registers `a` and `b` which are elements of a mathematical group `G`.
- **Alice**: The generic term for a participant in the protocol. 

### Core Operations

1. **Deposit**: Users can deposit their coins into a special 'pool' as mix-boxes. These boxes can be in fixed denominations.
2. **Mix**: A third-party service or another user can take any two mix-boxes from the pool and mix them. After mixing, two new mix-boxes are added back to the pool. This process conceals the original ownership of the boxes.
3. **Withdraw**: Users can withdraw their coins from the pool at any time.

---

### Steps for Mixing Boxes

1. **Select Two Boxes**: Choose any two mix-boxes from the pool.
2. **Re-randomise Public Key**: Perform a mathematical operation on the registers `a` and `b` of each selected mix-box.
3. **Validation**: Prove that the mathematical operations were done correctly. The new mix-boxes should look identical to an observer.

---




*Note: This is a simplified document. For technical details and mathematical proofs, consult the whitepaper.*

- [Documentation](https://github.com/ergoplatform/ergo-jde/blob/main/kiosk/src/test/scala/kiosk/mixer/doc/main.pdf) 
- Original forum posts for [Outsourceable mix](https://www.ergoforum.org/t/yet-another-mixing-protocol/3359/2?u=scalahub)
- [Stealth transfer](https://www.ergoforum.org/t/yet-another-mixing-protocol/3359/3?u=scalahub)
