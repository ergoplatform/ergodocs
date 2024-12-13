# Babel Fees Plugin Documentation

The **Babel Fees Plugin** is a Fleet SDK extension that lets users pay transaction fees with tokens instead of ERG. This approach proves useful for users who start with empty wallets. It facilitates token-to-ERG swaps for fee payments. The plugin includes functions that create Babel Fee contracts, validate Babel Boxes, and manage contract states. It plugs into Fleet SDK's transaction framework, which makes it possible to build complex transactions that do not require a native ERG balance for fee payment.

---

### Key Features

1. **Token-Based Fee Payment**:

    - Enables users to pay fees with tokens.
    - Automates token-to-ERG swaps.

2. **Validation Utilities**:

    - Validate Babel Boxes and their associated contracts.
    - Check contract parameters and fields to ensure correct configurations.

3. **Customizable Contracts**:

    - Developers define token prices and liquidity for Babel Boxes.
    - Contracts adjust their parameters based on a specific token ID.

4. **Optimized for Modern Development**:

    - Supports both ESM and CommonJS modules.
    - Offers tree-shaking for reduced bundle size.

---

### Installation

Install the Babel Fees Plugin with npm:

```bash
npm install @fleet-sdk/babel-fees-plugin
```

The Babel Fees Plugin requires Fleet SDK Core:

```bash
npm install @fleet-sdk/core
```

This plugin requires Node.js 18 or newer.

---

### Usage Example

#### Add Babel Fees to a Transaction

The code below constructs a transaction that pays its fees with tokens instead of ERG. It sets the current blockchain height, adds inputs, integrates Babel fee logic, requests minimum fees, assigns a change address, and builds the final transaction object. After the build step completes, the transaction object includes instructions that convert a defined amount of tokens into the necessary ERG fees.

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

This snippet demonstrates a transaction builder in action. The `BabelSwapPlugin` function takes a Babel Box and configuration parameters for token-to-ERG conversion. The plugin then attaches fee-paying logic to the transaction. When the transaction finalizes, the included Babel Box and token parameters ensure that any required ERG fees are sourced from the specified tokens.

---

### API Reference

#### Plugins

1. **`BabelSwapPlugin`**

    - **Description**: Integrates Babel fee functionality into a transaction, converting tokens into ERG to meet fee requirements.
    - **Parameters**:

          - `babelBox`: A valid Babel Fee box. A Babel Box contains tokens and ERG that a contract uses to set a token price.
          - `token`: An object that specifies the token ID and the token amount used to generate the necessary ERG fees.

    - **Usage**:

          ```typescript
          BabelSwapPlugin(babelBox, {
            tokenId: "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
            amount: "50"
          });
          ```

    This plugin modifies a transaction so that the transaction no longer requires a direct ERG payment for fees. It uses the Babel Box as a liquidity source to convert specified tokens into enough ERG to cover the fee.

#### Utility Functions

1. **`getTokenPrice(babelBox: Box<Amount>): bigint`**

     Returns the price of a single token unit in nanoERG. Developers use this function to understand how many nanoERG one token unit represents.

     **Example**:

     ```typescript
     const price = getTokenPrice(babelBox);
     console.log(`Price per token: ${price}`);
     ```

     This code retrieves the token price from the Babel Box and logs it. Developers then know the rate at which tokens convert into ERG.

2. **`buildBabelContract(tokenId: string): string`**

     Returns a Babel Fee ErgoTree for a given token ID. This function constructs the contract script that defines how tokens and ERG interact inside a Babel Box. Developers use this when they want to generate a Babel Box contract for a specific token.

3. **`isValidBabelBox(box: Box<Amount>): boolean`**

     Returns a boolean that indicates whether a given box qualifies as a Babel Fee box. Developers use this to confirm that a discovered box meets all criteria for acting as a Babel Box.

4. **`extractTokenIdFromBabelContract(ergoTree: string): string`**

     Extracts the token ID from a Babel Fee contract. Developers use this to confirm which token the Babel Box manages.

5. **`isBabelContractForTokenId(ergoTree: string, tokenId: string): boolean`**

     Checks whether a Babel Fee contract matches a given token ID. This helps validate that the contract in use corresponds to the intended token.

---

### Box Discovery and Identification

A Babel Box is a container that holds a specified token and associated ERG. This combination allows the plugin to determine the conversion rate between tokens and ERG. The plugin references the Babel Box when it performs token-to-ERG conversions.

The hexadecimal representation of the Babel Fees contract:
```
100604000e20{tokenId}0400040005000500d803d601e30004d602e4c6a70408d603e4c6a7050595e67201d804d604b2a5e4720100d605b2db63087204730000d606db6308a7d60799c1a7c17204d1968302019683050193c27204c2a7938c720501730193e4c672040408720293e4c672040505720393e4c67204060ec5a796830201929c998c7205029591b1720673028cb272067303000273047203720792720773057202
```

Replace `{tokenId}` with the target token ID. Use the resulting ErgoTree to discover Babel Boxes through the Ergo platform API:

`https://api.ergoplatform.com/api/v1/boxes/unspent/byErgoTree/{ErgoTree}`

**Example Box Fetching:**

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

### Step-by-Step

Read [this guide](http://147.182.244.219/ergobabelfees.html) for details on minting a token, creating a Babel Box, and using a web application to self-sign transactions with Babel Fees involved. The guide walks through each stage, which includes preparing a token, generating a Babel Box contract, and integrating the BabelSwapPlugin within a Fleet SDK transaction.

---

### Development Insights

#### Key Updates from `CHANGELOG.md`

- **Validation Enhancements**:

    - Introduced type validation for Babel Box fields (`R4`, `R5`) in version `0.1.16`. This ensures that boxes meet strict requirements.

- **Module Export Fixes**:

     - Adjusted the ESM and CommonJS exports in version `0.1.10` to prevent issues with package imports.

#### Package Metadata

- **Version**: `0.1.18`
- **Dependencies**:

    - `@fleet-sdk/core`  
    - `@fleet-sdk/common`  
    - `@fleet-sdk/serializer`  
      
- **Environment**:

    - Requires Node.js 18 or newer.

---

### Testing and Validation

#### Unit Testing Example

The unit test below verifies that the `BabelSwapPlugin` integrates Babel fee logic into a transaction. It sets a mock Babel Box, builds a transaction that uses the plugin, and checks whether the resulting transaction includes the Babel Box as a source of fee liquidity.

```typescript
describe("BabelSwapPlugin Tests", () => {
  it("should integrate Babel Fee inputs and outputs", () => {
    const babelBox = { /* Mock Babel Box with required fields */ };
    const tx = new TransactionBuilder(1000000)
      .from(inputs)
      .extend(BabelSwapPlugin(babelBox, {
        tokenId: "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
        amount: "50"
      }))
      .build();

    expect(tx.inputs).toContain(babelBox);
  });
});
```

This test confirms the presence of the Babel Box in the transaction inputs. If it passes, developers know that the plugin logic runs correctly and that the transaction is now prepared for token-based fee payments.

---

### Reference Implementations

* [Implementing Ergo Babel Fees with Fleet-SDK - May 17, 2024](http://147.182.244.219/ergobabelfees.html)
* [Nautilus Wallet implementation](https://github.com/capt-nemo429/nautilus-wallet/pull/82)
* [AppKit implementation](https://github.com/ergoplatform/ergo-appkit/pull/204)
* [Fleet SDK Babel fees plugin](https://fleet-sdk.github.io/docs/plugins/babel-fees)

### Additional Resources

- **Fleet SDK Documentation**: [Fleet SDK Babel Fees Plugin](https://fleet-sdk.github.io/docs/plugins/babel-fees)
- **Ergo Platform API**: [Ergo API Documentation](https://api.ergoplatform.com/api/v1/docs/)
- **EIP-0031 Specification**: [Ergo Babel Fees EIP](https://github.com/ergoplatform/eips/blob/master/eip-0031.md)
