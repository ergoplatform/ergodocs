# Babel Fees Plugin Documentation

The Babel Fees Plugin is a specialized extension for the Fleet SDK designed to simplify the process of using Babel Fees within Ergo transactions. Babel Fees is a mechanism that allows users to pay transaction fees with tokens instead of ERG, particularly beneficial for those with limited or no ERG balances. The plugin automates the complex process of token-to-ERG conversion necessary for utilizing Babel Fees. It integrates seamlessly into the Fleet SDK’s transaction framework, enabling developers to build sophisticated transactions that don't require users to have a native ERG balance for transaction fee payments. 

## What are Babel Fees?

At its core, [Babel Fees](babel-fees.md) is an Ergo protocol feature that enables users to pay transaction fees using a variety of tokens, rather than being restricted to using ERG. This is done by leveraging smart contracts which act as liquidity sources (called “Babel Boxes”) for token-to-ERG swaps. These contracts are set up by others who wish to provide this liquidity to users.

Babel Fees offer key benefits:

- **Accessibility**: Allows users with limited or no ERG to interact with the Ergo network.
- **Flexibility**: Users can choose which tokens they want to use for paying fees.
- **Onboarding**: Makes it easier for new users to join the ecosystem.

---

## Key Features

- **Transaction Extension**

    - Provides a BabelSwapPlugin that seamlessly integrates with Fleet SDK's TransactionBuilder
    - Modifies transaction inputs and outputs to incorporate Babel Fee logic

- **Babel Box Validation**

    - Offers utilities to validate the structure and parameters of Babel Boxes
    - Ensures compliance with the Babel Fees protocol

- **Contract Script Generation**

    - Includes functions for building and verifying Babel Fee contract scripts (ErgoTree)

- **Developer-Friendly**

    - Supports ESM and CommonJS modules
    - Tree-shakeable design for smaller bundle sizes
---

## Installation

To install the plugin, use the following commands in your project:

```bash
npm install @fleet-sdk/babel-fees-plugin
```

The core Fleet SDK is also required:
```bash
npm install @fleet-sdk/core
```

**System Requirements**: Node.js version 18 or newer.

---

## Usage Example: Add Babel Fees to a Transaction

This example demonstrates how to pay for transaction fees using tokens with BabelSwapPlugin.


```typescript
import { TransactionBuilder } from '@fleet-sdk/core';
import { BabelSwapPlugin } from '@fleet-sdk/babel-fees-plugin';

const tx = new TransactionBuilder(1000000) // Replace with current block height
  .from(inputs) // Provide input boxes for the transaction
  .extend(
    BabelSwapPlugin(babelBox, {
      tokenId: "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
      amount: "50" // The plugin converts this token amount into ERG to cover fees
    })
  )
  .payMinFee() // Ensure the transaction includes the required network fee
  .sendChangeTo("9hY16vzHmmfyVBwKeFGHvb2bMFsG94A1u7To1QWtUokACyFVENQ") // Define the address for leftover funds after fee conversion
  .build();

console.log(tx);
```

Explanation:

- The code initializes a `TransactionBuilder` with the current block height.
- `from(inputs)` includes input boxes for the transaction.
- `extend(BabelSwapPlugin(...))` adds the BabelSwapPlugin to the transaction. The plugin takes a Babel Box, token ID, and the token amount to convert for ERG fees.
- `payMinFee()` ensures the inclusion of minimum required network fees.
- `sendChangeTo(...)` defines the address for remaining funds after fee conversion.
- `build()` finalizes the transaction object.

This example showcases how to use Babel Fees with the plugin without any direct ERG input from the user for transaction fees.

---

## **API Reference**

**Plugins**

1.  **`BabelSwapPlugin(babelBox: Box<Amount>, token: { tokenId: string, amount: string }): TransactionExtension`**

    *   **Description**: Extends the transaction to incorporate Babel Fees by converting the provided token into ERG needed for fees.
    *   **Parameters**:
        *   `babelBox`: A valid Babel Box containing tokens and ERG for conversion.
        *   `token`: An object containing:
            *   `tokenId`: The ID of the token to be used for fee conversion.
            *   `amount`: The amount of tokens to use for the fee payment.
    *   **Usage**:
        ```typescript
        BabelSwapPlugin(babelBox, {
          tokenId: "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
          amount: "50"
        });
        ```

## **Utility Functions**

1.  **`getTokenPrice(babelBox: Box<Amount>): bigint`**

    *   **Description**: Calculates and returns the price of a single token unit in nanoERG based on a specific Babel Box.
    *   **Example**:
        ```typescript
        const price = getTokenPrice(babelBox);
        console.log(`Price per token: ${price}`);
        ```

2.  **`buildBabelContract(tokenId: string): string`**

    *   **Description**: Generates the ErgoTree (contract script) for a Babel Box using a specified token ID.
    *   **Usage**:
         ```typescript
          const contract = buildBabelContract(tokenId);
         ```

3.  **`isValidBabelBox(box: Box<Amount>): boolean`**

    *   **Description**: Determines if a given box is a valid Babel Box.
    *   **Usage**:
        ```typescript
        const isValid = isValidBabelBox(myBox);
        if (isValid) {
            console.log('This is a valid babel box');
        }
        ```

4.  **`extractTokenIdFromBabelContract(ergoTree: string): string`**

    *   **Description**: Extracts the token ID from a Babel Fee contract script (ErgoTree).
    *   **Usage**:
        ```typescript
        const tokenId = extractTokenIdFromBabelContract(ergoTree);
        ```

5.  **`isBabelContractForTokenId(ergoTree: string, tokenId: string): boolean`**

    *   **Description**: Validates if an ErgoTree matches the Babel Fee contract for a specific token ID.
    *   **Usage**:
        ```typescript
        const isForToken = isBabelContractForTokenId(ergoTree, tokenId);
        ```
---

## Box Discovery and Identification

A Babel Box is a container that holds a specified token and associated ERG. This combination allows the plugin to determine the conversion rate between tokens and ERG. The plugin references the Babel Box when it performs token-to-ERG conversions.

The hexadecimal representation of the Babel Fees contract:
```
100604000e20{tokenId}0400040005000500d803d601e30004d602e4c6a70408d603e4c6a7050595e67201d804d604b2a5e4720100d605b2db63087204730000d606db6308a7d60799c1a7c17204d1968302019683050193c27204c2a7938c720501730193e4c672040408720293e4c672040505720393e4c67204060ec5a796830201929c998c7205029591b1720673028cb272067303000273047203720792720773057202
```

Replace `{tokenId}` with the target token ID. Use the resulting ErgoTree to discover Babel Boxes through the Ergo platform API:

`https://api.ergoplatform.com/api/v1/boxes/unspent/byErgoTree/{ErgoTree}`

**Example of Fetching a Babel Box:**

```typescript
const fetchBabelBox = async (ergoTree: string) => {
  try {
    const response = await fetch(`https://api.ergoplatform.com/api/v1/boxes/unspent/byErgoTree/${ergoTree}`);
    const json = await response.json();
    return json.items[0]; // Returns the first Babel Box found
  } catch (error) {
    console.error("Error fetching Babel Box:", error);
    return null;
  }
};
```

This snippet uses the Ergo API to locate and return a Babel Box. Developers supply an ErgoTree string, and the function queries the blockchain to find a box that matches. The returned Babel Box can then serve as the liquidity source for token-to-ERG conversions in transactions.

---

## Step-by-Step


For a detailed guide on how to mint a token, set up a Babel Box, and utilize the plugin within a web application, refer to [this guide](http://147.182.244.219/ergobabelfees.html).


---

## Development Insights

### Key Updates from `CHANGELOG.md`

- **Validation Enhancements**:

    - Introduced type validation for Babel Box fields (`R4`, `R5`) in version `0.1.16`. This ensures that boxes meet strict requirements.

- **Module Export Fixes**:

     - Adjusted the ESM and CommonJS exports in version `0.1.10` to prevent issues with package imports.

### Package Metadata

- **Version**: `0.1.18`
- **Dependencies**:

    - `@fleet-sdk/core`  
    - `@fleet-sdk/common`  
    - `@fleet-sdk/serializer`  
      
- **Environment**:

    - Requires Node.js 18 or newer.

---

## Reference Implementations

* [Implementing Ergo Babel Fees with Fleet-SDK - May 17, 2024](http://147.182.244.219/ergobabelfees.html)
* [Nautilus Wallet implementation](https://github.com/capt-nemo429/nautilus-wallet/pull/82)
* [AppKit implementation](https://github.com/ergoplatform/ergo-appkit/pull/204)
* [Fleet SDK Babel fees plugin](https://fleet-sdk.github.io/docs/plugins/babel-fees)

## Additional Resources

- **Fleet SDK Documentation**: [Fleet SDK Babel Fees Plugin](https://fleet-sdk.github.io/docs/plugins/babel-fees)
- **Ergo Platform API**: [Ergo API Documentation](https://api.ergoplatform.com/api/v1/docs/)
- **EIP-0031 Specification**: [Ergo Babel Fees EIP](https://github.com/ergoplatform/eips/blob/master/eip-0031.md)
