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
---

# Wallet Interaction Standards (EIPs) for dApp Developers

Ergo Improvement Proposals (EIPs) define standards for interaction between dApps and wallets, ensuring a consistent and secure experience for users and developers. This page highlights key EIPs and expected behaviors relevant to dApp development, focusing primarily on EIP-0012 (dApp Connector).

*(Note: This page is not a substitute for the full EIP specifications. Refer to the official [Ergo EIPs repository](https://github.com/ergoplatform/eips) for complete details. This aims to clarify common implementation points based on developer feedback.)*

## Supported Wallets (EIP-0012)

Currently, the primary wallets implementing the EIP-0012 dApp Connector standard are:

*   **[Nautilus Wallet](nautilus.md)** (Browser Extension)
*   **Ergo Mobile Wallet (Android/iOS)**

**Note:** Yoroi Wallet's Ergo support is deprecated. Developers and users should utilize Nautilus or the official Ergo Mobile Wallet for dApp interactions. See the main [Wallets page](../wallets.md) for more options.

## EIP-0012: dApp Connector Overview

EIP-0012 defines a standard JavaScript interface injected into the dApp's web context by the wallet (usually as `window.ergoConnector.ergo` or just `window.ergo` after connection). It separates functions into two main categories:

*   **Connection API:** Functions for establishing and managing the connection between the dApp and the wallet (e.g., `connect`, `disconnect`, `check`, `isConnected`). These are typically accessed via `ergoConnector`.
*   **Context API:** Functions available *after* a connection is established, allowing the dApp to interact with the wallet's context (e.g., get addresses, balances, request signing). These are accessed via the `ergo` object obtained after successful connection.

### Typical Connection Flow (Conceptual JS)

```javascript
async function connectWallet() {
  // Check if the connector object exists (wallet extension installed)
  if (typeof ergoConnector === 'undefined' || !ergoConnector.ergo) {
    console.error("Ergo Wallet Connector not found. Please install Nautilus or use a compatible wallet.");
    // Optionally prompt user to install
    return null;
  }

  try {
    // Check if already connected
    const isConnected = await ergoConnector.ergo.isConnected();
    if (isConnected) {
      console.log("Wallet already connected.");
      return ergo; // Return the existing context API object
    }

    // Request read access (prompts user in wallet)
    const granted = await ergoConnector.ergo.connect(); 
    
    if (!granted) {
      console.log("Wallet connection request denied by user.");
      return null;
    } else {
      console.log("Wallet connected successfully!");
      // 'ergo' object (Context API) is now available globally or via ergoConnector.ergo
      // You might want to store this 'ergo' object reference in your dApp's state
      return ergo; 
    }
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

*   **`ergoConnector.ergo.connect()`:** Initiates the connection request. Returns `true` if access granted, `false` otherwise.
*   **`ergoConnector.ergo.disconnect()`:** Disconnects the dApp (if supported by the wallet).
*   **`ergoConnector.ergo.isConnected()`:** Checks if the dApp currently has read access without prompting the user.

### Context API Functions (`ergo.*`) & Expected Behavior

*(Available only after `connect()` returns `true`)*

*   **`ergo.get_used_addresses(paging?)`:**
    *   **Purpose:** Returns addresses involved in past transactions. Crucial for discovering user funds.
    *   **Return (Empty Wallet):** **MUST return `[]` (empty array)** if no addresses have been used. Do not rely on error codes for this case, although older wallets might have thrown errors.
    *   **Pagination:** Supports `{ page: number, limit: number }` argument. Handle paginated results if expecting many addresses.
    *   **Error Handling:** Catch potential errors (e.g., user session expired, wallet internal error).
*   **`ergo.get_unused_addresses()`:**
    *   **Purpose:** Returns addresses generated but not yet seen on-chain. Useful for providing fresh deposit addresses.
    *   **Error Handling:** Catch potential errors.
*   **`ergo.get_balance(token_id?)`:**
    *   **Purpose:** Returns confirmed and unconfirmed balance for ERG (if `token_id` omitted) or a specific token.
    *   **Error Handling:** Catch potential errors.
*   **`ergo.sign_tx(unsignedTx)`:**
    *   **Purpose:** Sends an *unsigned* transaction (built according to EIP-12 structure) to the wallet for the user to review and sign.
    *   **Return:** Returns the *signed* transaction if approved by the user.
    *   **Error Handling:** Crucial to handle user rejection (often throws a specific error code/message), insufficient funds errors from the wallet's pre-check, or malformed transaction errors.
*   **`ergo.submit_tx(signedTx)`:**
    *   **Purpose:** Sends a *signed* transaction to the wallet for submission to the network via the wallet's connected node.
    *   **Return:** Returns the transaction ID upon successful submission.
    *   **Error Handling:** Handle network errors, node rejection errors (e.g., double spends, invalid transaction), or wallet internal errors. Note that successful submission doesn't guarantee inclusion in a block.

*(Refer to the full EIP-0012 specification for exact function signatures, parameter/return types, and detailed error codes.)*

## Security Best Practices

*   **Request Minimal Permissions:** Only request read access initially (`connect`). Don't request signing permissions upfront if not immediately needed.
*   **User Intent:** Ensure all signing requests (`sign_tx`) clearly correspond to an explicit user action within your dApp. Don't trigger signing requests unexpectedly.
*   **Transaction Clarity:** Display the key details of any transaction clearly to the user *before* sending it to the wallet for signing. The wallet should also display this information, but providing context in the dApp is crucial.
*   **Input Validation:** Sanitize and validate any user input used in transaction construction to prevent injection attacks or malformed requests.
*   **State Management:** Securely manage the connection state within your dApp. Verify `isConnected()` before attempting Context API calls if needed.
*   **Avoid Storing Sensitive Data:** Never ask for or store user private keys or seed phrases in your dApp. All signing happens within the wallet.

## Mobile Considerations

*   **Connection Initiation:** The method for initiating a connection might differ slightly on mobile (e.g., via deeplinking or a dedicated browser within the mobile wallet app) compared to browser extensions. Check mobile wallet documentation.
*   **User Experience:** Ensure your dApp's UI is responsive and works well on mobile screens when interacting with the wallet interface.

## Testing Recommendations

*   **Multiple Wallets:** Test your dApp integration with all supported wallets (Nautilus, Ergo Mobile Wallet) on different platforms (desktop, mobile).
*   **Testnet:** Thoroughly test all connection flows, data fetching, and transaction signing/submission scenarios on the Ergo Testnet before deploying to Mainnet.
*   **Edge Cases:** Test user cancellation flows (rejecting connection, rejecting signing), network errors, insufficient funds, and handling of empty/new wallets.
*   **Wallet State Changes:** Test how your dApp handles the user switching accounts or disconnecting the wallet while the dApp is active.

## Troubleshooting Common Issues

*   **`ergoConnector` Undefined:** Wallet extension is not installed, not enabled, or not injecting the connector object correctly. Prompt user to install/enable.
*   **Connection Rejected:** User explicitly denied the connection request in the wallet prompt. Handle gracefully.
*   **`sign_tx` Errors:**
    *   User rejected the signature: Catch the specific error thrown by the wallet.
    *   Insufficient funds: Wallet might pre-check and reject. Ensure input selection logic is correct.
    *   Malformed transaction: Double-check the structure of the `unsignedTx` object against EIP-12 specs.
*   **`submit_tx` Errors:** Network issues, node errors (transaction invalid), or wallet unable to connect to its node. Provide feedback to the user; they might need to check their wallet's network connection.
*   **Incorrect Data (`get_used_addresses`, `get_balance`):** Ensure the wallet is fully synced. Check for pagination issues with `get_used_addresses`.

## Other Relevant EIPs

*   **[EIP-0001: Ergo Address Allocation and Encoding](https://github.com/ergoplatform/eips/blob/master/eip-0001.md):** Defines the standard address formats (P2PK, P2S).
*   **[EIP-0003: Deterministic Wallet Standard (BIP32/BIP44)](https://github.com/ergoplatform/eips/blob/master/eip-0003.md):** Defines derivation paths for hierarchical deterministic (HD) wallets.
*   *(Others like EIP-0004 (Assets), EIP-0020 (ErgoPay), EIP-0027 (Asset Linking) may also be relevant depending on dApp functionality).*

## Example Implementations

*   *(Placeholder: Link to well-known open-source dApps or libraries demonstrating good EIP-0012 integration, e.g., Spectrum UI, Nautilus examples, Fleet examples, if available).*

---

By understanding and correctly implementing these standards, particularly EIP-0012, dApps can provide a smoother, more secure, and reliable interaction experience across different Ergo wallets.
