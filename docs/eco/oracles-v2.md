# Oracle Pools V2

- [How to bootstrap an ERG/XAU pool on testnet](https://github.com/ergoplatform/oracle-core/blob/develop/docs/how_to_bootstrap.md)

This is a proposed update to the oracle pool v1.0 currently deployed and documented in [EIP16](https://github.com/ergoplatform/eips/blob/eip16/eip-0016.md).

In order to motivate the changes proposed in this document, consider the drawbacks of Oracle pool v1.0:

1. Rewards generate a lot of dust
2. Current rewards are too low (related to 1)
3. There are two types of pool boxes. This makes dApps and update mechanism more complex
4. Oracle tokens are non-transferable, so oracles are locked permanently. The same goes for ballot tokens.

Oracle pool v2.0 aims to address the above. 

Below is a summary of the main new features in v2.0 and how it differs from v1.0.

- **Single pool address**: This version of the pool will have only one address, the *pool address*. 
- **Epoch counter**: Pool box will additionally store a counter that is incremented on each collection. This will allow more sophisticated dApps. 
- **Compact pool box**: Pool box is separated from the logic of pool management, which is captured instead in a **refresh** box. This makes the pool box very small for use in other dApps.
- **Refresh box**: The refresh box is used for collecting data-points.   
- **Reward in tokens**: The posting reward will be in the form of tokens instead of Ergs. These tokens can be redeemed separately, which is not part of the protocol.
    - The pool box emits such reward tokens.
- **No separate funding process**: The pool box emits only reward tokens and won't be handing out Ergs. Thus, there won't be a separate funding process required.
- **Reward accumulated**: We will not be creating a new box for rewarding each posting to prevent dust. Instead, the rewards will be accumulated directly in the oracle boxes. 
- **Oracle boxes spent in collection**: Because the rewards must be accumulated, the oracle boxes will be considered as inputs rather than data-inputs when collecting individual rates for averaging. 
    - These inputs will be spent, and a copy of the box with the reward will be created. 
    - This gives us the ability to accumulate rewards while keeping the transaction size similar to when using them as data-inputs in v1.0.
    - Additionally, this allows us to outsource part of the reward logic to the oracle boxes.
    - **Note:** The pool box will still be used as data input in other dApps.
- **Transferable oracle tokens**: Oracle tokens are free to be transferred between public keys.
- **Similar update mechanism**: We will have a similar update mechanism as in v1.0 (threshold number of ballot token holders must vote for an update).
- **Transferable ballot tokens**: Similar to oracle tokens, the ballot tokens are free to be transferred between public keys.


See [EIP-0023 Oracle pool 2.0](https://github.com/ergoplatform/eips/pull/41) for more information. 
