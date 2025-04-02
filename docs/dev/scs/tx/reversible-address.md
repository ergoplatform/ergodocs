# Reversible Addresses

A reversible address is an example of a multi-stage contract designed with anti-theft features. It functions as follows: funds sent to this address can initially only be spent in a way that allows the payment to be reversed by a trusted party for a specific period. After this period, only the intended recipient can spend the funds. This mechanism is particularly useful for managing hot wallets (e.g., for exchanges or mining pools handling customer withdrawals). A hot wallet's private key is typically stored on a server, making it vulnerable to compromise and theft. To recover funds in case of such a compromise, a trusted party (with a private key stored securely offline) can intervene.

The reversible address uses a two-stage protocol. The first stage ensures that withdrawals from the hot wallet adhere to specific rules, creating outputs protected by a second-stage script. The second stage allows either the intended recipient (after a delay) or the trusted party (before the delay) to spend the funds. If an unauthorized transaction is detected originating from the hot wallet (first stage), the trusted party can use their private key to trigger an abort procedure on the second-stage boxes, diverting the funds to a secure address. Besides securing hot wallets, these addresses can be used for automated-release escrow payments in online shopping.

Let's assume:
*   `alice` represents the `SigmaProp` (public key) of the hot wallet.
*   `carol` represents the `SigmaProp` of the trusted party (whose private key is stored offline and used for reversals).
*   `blocksIn24h` is a constant representing the estimated number of blocks in 24 hours (the reversal period).
*   `bob` represents the `SigmaProp` of a customer wishing to withdraw funds.

In Ethereum, a similar outcome might be achieved by sending funds to an account with a contract (let's call it C<sub>b</sub>) that allows `carol` to withdraw funds for `blocksIn24h` blocks, after which only `bob` can withdraw. While the same contract instance could handle multiple withdrawals, creating a new instance for each withdrawal (emulating the UTXO model) might be preferable. The funds for these withdrawals would need to originate from another contract (C<sub>a</sub>) ensuring outputs are only created according to the structure of C<sub>b</sub>.

In Ergo, this is implemented as a two-stage protocol:
1.  **Stage 1 (Hot Wallet Script - C<sub>a</sub>):** This script guards the main hot wallet funds. It ensures that any spending transaction creates outputs protected by the Stage 2 script (`withdrawScript`).
2.  **Stage 2 (Withdrawal Script - C<sub>b</sub>):** This script guards the individual withdrawal boxes paid out to customers like Bob. It allows either Bob (after the delay) or Carol (before the delay) to spend the box.

The following script, named `withdrawScript`, implements the second stage (C<sub>b</sub>). This script protects the output box created when the hot wallet pays Bob.

```scala
// Get Bob's public key (the recipient) from register R4
val bob = SELF.R4[SigmaProp].get 

// Get the deadline height (when Bob can spend) from register R5
val bobDeadline = SELF.R5[Int].get 

// Check if either:
// 1. Bob is spending AND the deadline has passed (HEIGHT > bobDeadline)
// OR
// 2. Carol (trusted party) is spending AND the deadline has NOT passed (HEIGHT <= bobDeadline)
sigmaProp((bob && HEIGHT > bobDeadline) || (carol && HEIGHT <= bobDeadline))
```

This `withdrawScript` is referenced (e.g., by its hash) in the first stage script (`hotWalletScript`) shown below. This script guards the main hot wallet funds.

```scala
// Define a function `isChange` that checks if an output box `b` is a change box 
// (i.e., returns funds to the hot wallet itself).
val isChange = {(b: Box) => b.propositionBytes == SELF.propositionBytes} 

// Define a function `isWithdraw` that checks if an output box `b` is a valid withdrawal box:
// - Its R5 register (deadline) must be at least the current height + delay.
// - Its script must match the withdrawScript hash.
val isWithdraw = {(b: Box) => 
  b.R5[Int].get >= HEIGHT + blocksIn24h && 
  blake2b256(b.propositionBytes) == withdrawScriptHash // Assuming withdrawScriptHash is a known constant
}

// The final condition requires:
// 1. Alice's signature (the hot wallet owner).
// 2. ALL outputs must satisfy EITHER the isChange condition OR the isWithdraw condition.
sigmaProp(alice && OUTPUTS.forall({(b: Box) => isChange(b) || isWithdraw(b)}))
```

The P2S address derived from the `hotWalletScript` acts as the reversible address. Funds sent to this address are subject to the defined withdrawal rules. Normally, Bob would spend his withdrawal box (protected by `withdrawScript`) after the `bobDeadline` (approximately `blocksIn24h` blocks later). However, if an unauthorized transaction attempts to spend from the hot wallet (violating the `isWithdraw` or `isChange` conditions), or if a legitimate withdrawal box needs to be reversed before `bobDeadline`, Carol can intervene using her private key to spend the second-stage box(es) and redirect the funds to a secure address.

Note that the trusted party (`carol`) is effectively bound to this specific hot wallet setup. A different hot wallet or security policy would require a new contract and potentially a different trusted party.

While designed for securing hot wallets, reversible addresses have other potential applications, such as automated-release escrow payments in online shopping, where `carol` could represent a mutually agreed-upon adjudicator.
