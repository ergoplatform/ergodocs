---
tags:
  - Wallets
  - EIPs
  - Standards
  - dApp Connector
  - EIP-0012
  - EIP-0001
  - EIP-0003
  - get_used_addresses
  - dApp Development
  - Security
  - Testing
owner: docs
last_reviewed: 2026-10-26
source_repos:
  - repo: ergoplatform/eips
    branch: master
    paths:
      - eip-0001.md
      - eip-0003.md
  - repo: nautls/nautilus-wallet
    branch: master
    paths:
      - docs/dapp-connector
      - src/extension/content-scripts/injected.ts
      - src/extension/background/ergoHandlers.ts
source_of_truth:
  - https://github.com/ergoplatform/eips/tree/master/eip-0001.md
  - https://github.com/ergoplatform/eips/tree/master/eip-0003.md
  - https://github.com/ergoplatform/eips/pull/23
  - https://github.com/nautls/nautilus-wallet/blob/v1.3.6/docs/dapp-connector/wallet-connection.md
  - https://github.com/nautls/nautilus-wallet/blob/v1.3.6/docs/dapp-connector/wallet-interaction.md
---

# Wallet Interaction Standards (EIPs) for dApp Developers

Ergo Improvement Proposals (EIPs) define standards for interaction between dApps and wallets, ensuring a consistent and secure experience for users and developers. This page highlights key EIPs and expected behaviors relevant to dApp development, focusing primarily on EIP-0012 (dApp Connector).

*(Note: This page is not a substitute for the full EIP specifications. Refer to the official [Ergo EIPs repository](https://github.com/ergoplatform/eips) for complete details. This aims to clarify common implementation points based on developer feedback.)*

## Supported Wallets (EIP-0012)

The examples below target the [Nautilus browser extension](nautilus.md), checked against `v1.3.6`. Other wallets may implement different subsets or extensions. The original [EIP-0012 proposal](https://github.com/ergoplatform/eips/pull/23) remains open, so check the chosen wallet's implementation as well as the proposal.

The native Ergo Mobile Wallet advertises ErgoPay and ErgoAuth support. Those signing/authentication flows do not imply that the wallet injects a browser `ergoConnector` API. See the main [Wallets page](wallets-overview.md) for platform-specific options.

## EIP-0012: dApp Connector Overview

EIP-0012 describes a JavaScript bridge between a dApp and a wallet. Nautilus exposes its connection API at `window.ergoConnector.nautilus`; after connection, obtain its context with `getContext()`. A global `window.ergo` is optional. The implementation separates functions into two categories:

* **Connection API:** Wallet-specific functions such as `connect`, `disconnect`, `isAuthorized`, `isConnected`, and `getContext`, accessed through `ergoConnector.nautilus` in this example.
* **Context API:** Functions available *after* a connection is established, allowing the dApp to interact with the wallet's context (e.g., get addresses, balances, request signing). These are accessed via the `ergo` object obtained after successful connection.

### Typical Connection Flow (Conceptual JS)

```javascript
async function connectWallet() {
  // Browser example: call from an explicit Connect button action.
  const connector = window.ergoConnector?.nautilus;
  if (!connector) {
    console.error("Nautilus Wallet Connector not found.");
    return null;
  }

  try {
    if (!(await connector.isConnected())) {
      const granted = await connector.connect({ createErgoObject: false });
      if (!granted) return null;
    }
    return await connector.getContext();
  } catch (error) {
    console.error("Error connecting to wallet:", error);
    // Handle specific errors (e.g., user cancellation, timeouts)
    return null;
  }
}

// Usage:
// const ergoContext = await connectWallet();
// if (ergoContext) {
//   // Now use ergoContext.get_used_addresses(), ergoContext.sign_tx(), etc.
// }
```

### Connection API Functions (Examples)

* **`ergoConnector.nautilus.connect()`:** Connects the current page. Returns `true` if access is granted, `false` otherwise.
* **`ergoConnector.nautilus.disconnect()`:** Disconnects and revokes the site's authorization.
* **`ergoConnector.nautilus.isConnected()`:** Checks whether the current page has a context.
* **`ergoConnector.nautilus.isAuthorized()`:** Checks the site's saved authorization. After a page reload, authorization may persist while connection does not; call `connect()` again to restore the context.
* **`ergoConnector.nautilus.getContext()`:** Returns the connected context without relying on a global `ergo` variable.

### Context API Functions (`ergo.*`) & Expected Behavior

*(Available only after `connect()` returns `true`)*

* **`ergo.get_used_addresses()`:**
  * **Purpose:** Returns addresses involved in past transactions. Crucial for discovering user funds.
  * **Return (Empty Wallet):** **MUST return `[]` (empty array)** if no addresses have been used. Do not rely on error codes for this case, although older wallets might have thrown errors.
  * **Pagination:** The proposal describes pagination, but Nautilus `v1.3.6` rejects pagination arguments with `InvalidRequest`. Call without arguments; verify other wallets' capabilities separately.
  * **Error Handling:** Catch potential errors (e.g., user session expired, wallet internal error).
* **`ergo.get_unused_addresses()`:**
  * **Purpose:** Returns addresses generated but not yet seen on-chain. Useful for providing fresh deposit addresses.
  * **Error Handling:** Catch potential errors.
* **`ergo.get_balance(token_id?)`:**
  * **Purpose:** Returns the wallet's available ERG balance in nanoERG, or a token balance in its smallest unit. Nautilus returns a string; use integer-safe handling such as `BigInt`, not floating-point conversion. Its zero-confirmation setting determines whether mempool changes are included; this is not a separate confirmed/unconfirmed balance pair.
  * **Error Handling:** Catch potential errors.
* **`ergo.sign_tx(unsignedTx)`:**
  * **Purpose:** Sends an *unsigned* transaction (built according to EIP-12 structure) to the wallet for the user to review and sign.
  * **Return:** Returns the *signed* transaction if approved by the user.
  * **Shape:** Nautilus requires full box objects in both `inputs` and `dataInputs`, rather than just box IDs. Fleet's `.build().toEIP12Object()` produces this signing representation; a node's unsigned-transaction JSON is not interchangeable with it.
  * **Input selection:** EIP-12 carries the full unsigned transaction object for signing; wallets should not need to query the chain and patch transaction data before signing. If a specific box must be spent, include that input explicitly. Default SDK or wallet input selection does not guarantee any particular wallet box will be chosen.
  * **Error Handling:** Crucial to handle user rejection (often throws a specific error code/message), insufficient funds errors from the wallet's pre-check, or malformed transaction errors.
* **`ergo.sign_tx_inputs(unsignedTx, indexes)` (Nautilus):**
  * **Purpose:** Requests signatures for selected input indexes in a multi-party transaction.
  * **Return:** An array of signed inputs in the requested order, not a complete signed transaction. Combine the required parties' proofs before submission. Verify method support for each wallet; the original proposal uses the singular name `sign_tx_input`.
* **`ergo.submit_tx(signedTx)`:**
  * **Purpose:** Sends a *signed* transaction to the wallet for submission to the network via the wallet's connected node.
  * **Return:** Returns the transaction ID upon successful submission.
  * **Error Handling:** Handle network errors, node rejection errors (e.g., double spends, invalid transaction), or wallet internal errors. Note that successful submission doesn't guarantee inclusion in a block.

*(Refer to the full EIP-0012 specification for exact function signatures, parameter/return types, and detailed error codes.)*

## Security Best Practices

* **Request Minimal Permissions:** Only request read access initially (`connect`). Don't request signing permissions upfront if not immediately needed.
* **User Intent:** Ensure all signing requests (`sign_tx`) clearly correspond to an explicit user action within your dApp. Don't trigger signing requests unexpectedly.
* **Transaction Clarity:** Display the key details of any transaction clearly to the user *before* sending it to the wallet for signing. The wallet should also display this information, but providing context in the dApp is crucial.
* **Input Validation:** Sanitize and validate any user input used in transaction construction to prevent injection attacks or malformed requests.
* **State Management:** Securely manage the connection state within your dApp. Verify `isConnected()` before attempting Context API calls if needed.
* **Avoid Storing Sensitive Data:** Never ask for or store user private keys or seed phrases in your dApp. All signing happens within the wallet.

## Mobile Considerations

* **Connection Initiation:** The method for initiating a connection might differ slightly on mobile (e.g., via deeplinking or a dedicated browser within the mobile wallet app) compared to browser extensions. Check mobile wallet documentation.
* **User Experience:** Ensure your dApp's UI is responsive and works well on mobile screens when interacting with the wallet interface.

## Testing Recommendations

* **Multiple Wallets:** Test each connector implementation and platform you support. Test native ErgoPay/ErgoAuth integrations separately from injected browser connectors.
* **Testnet:** Thoroughly test all connection flows, data fetching, and transaction signing/submission scenarios on the Ergo Testnet before deploying to Mainnet.
* **Edge Cases:** Test user cancellation flows (rejecting connection, rejecting signing), network errors, insufficient funds, and handling of empty/new wallets.
* **Wallet State Changes:** Test how your dApp handles the user switching accounts or disconnecting the wallet while the dApp is active.

## Troubleshooting Common Issues

* **`ergoConnector` Undefined:** Wallet extension is not installed, not enabled, or not injecting the connector object correctly. Prompt user to install/enable.
* **Connection Rejected:** User explicitly denied the connection request in the wallet prompt. Handle gracefully.
* **`sign_tx` Errors:**
  * User rejected the signature: Catch the specific error thrown by the wallet.
  * Insufficient funds: Wallet might pre-check and reject. Ensure input selection logic is correct.
  * Malformed transaction: Double-check the structure of the `unsignedTx` object against EIP-12 specs.
* **`submit_tx` Errors:** Network issues, node errors (transaction invalid), or wallet unable to connect to its node. Provide feedback to the user; they might need to check their wallet's network connection.
* **Incorrect Data (`get_used_addresses`, `get_balance`):** Check wallet/backend synchronization, zero-confirmation settings, and units. Do not pass pagination arguments to Nautilus `v1.3.6`.

## Other Relevant EIPs

* **[EIP-0001: UTXO-Set Scanning Wallet API](https://github.com/ergoplatform/eips/blob/master/eip-0001.md):** Describes registering scans with the reference node wallet to track application-specific boxes.
* **[EIP-0003: Deterministic Wallet Standard (BIP32/BIP44)](https://github.com/ergoplatform/eips/blob/master/eip-0003.md):** Defines derivation paths for hierarchical deterministic (HD) wallets, including public-key export/import conventions for wallet interoperability.
* [EIP-0004 (Assets)](https://github.com/ergoplatform/eips/blob/master/eip-0004.md), [EIP-0020 (ErgoPay)](https://github.com/ergoplatform/eips/blob/master/eip-0020.md), and [EIP-0021 (Genuine Token Verification)](https://github.com/ergoplatform/eips/blob/master/eip-0021.md) cover related integration concerns.

## Example Implementations

Use maintained wallet and SDK repositories as implementation references, and verify against the full EIP before copying behavior:

* [Nautilus Wallet](https://github.com/nautls/nautilus-wallet)
* [Fleet SDK](https://github.com/fleet-sdk/fleet)
* [EIP-0012 pull request and discussion](https://github.com/ergoplatform/eips/pull/23)

---

By understanding and correctly implementing these standards, particularly EIP-0012, dApps can provide a smoother, more secure, and reliable interaction experience across different Ergo wallets.
