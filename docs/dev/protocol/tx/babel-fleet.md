# Babel Fees Plugin Documentation 


The **Babel Fees Plugin** is a Fleet SDK extension that allows transaction fees to be paid using tokens instead of ERG. This is particularly valuable for onboarding users with empty wallets by enabling token-to-ERG swaps for transaction fees. The plugin includes utility functions for contract creation, validation, and management, along with seamless integration into Fleet SDK's transaction framework.

---

### Key Features

1. **Token-Based Fee Payment**:

    - Enables users to pay fees with tokens.
    - Automates token-to-ERG swaps.

2. **Validation Utilities**:

    - Validate Babel Boxes and contracts to ensure proper functionality.

3. **Customizable Contracts**:

    - Developers can define token prices and liquidity for Babel Boxes.

4. **Optimized for Modern Development**:

    - Supports both ESM and CommonJS modules.
    - Tree-shaking enabled for optimal bundle size.

---

### Installation

Install the Babel Fees Plugin via npm:

```bash
npm install @fleet-sdk/babel-fees-plugin
```

Ensure compatibility with Fleet SDK Core:

```bash
npm install @fleet-sdk/core
```

The plugin requires **Node.js ≥ 18**.

---

### Usage Example

#### Add Babel Fees to a Transaction

```typescript
import { TransactionBuilder } from '@fleet-sdk/core';
import { BabelSwapPlugin } from '@fleet-sdk/babel-fees-plugin';

const tx = new TransactionBuilder(1000000) // Replace with current block height
  .from(inputs) // Transaction inputs
  .extend(
    BabelSwapPlugin(babelBox, {
      tokenId: "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
      amount: "50" // Amount of tokens to swap
    })
  )
  .payMinFee()
  .sendChangeTo("9hY16vzHmmfyVBwKeFGHvb2bMFsG94A1u7To1QWtUokACyFVENQ") // Change address
  .build();

console.log(tx);
```

---

### API Reference

#### Plugins

1. **`BabelSwapPlugin`**

    - **Description**: Adds Babel Fee logic to transactions for token-to-ERG conversions.
    - **Parameters**:
        - `babelBox`: A valid Babel Fee box providing token liquidity.
        - `token`: Specifies the token and amount to swap for ERG.
    - **Usage**:
        ```typescript
        BabelSwapPlugin(babelBox, {
        tokenId: "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
        amount: "50"
        });
        ```

#### Utility Functions

1. **`getTokenPrice(babelBox: Box<Amount>): bigint`**

        - Retrieves the price of a token unit in Nanoergs from a Babel Box.
        - **Example**:
            ```typescript
            const price = getTokenPrice(babelBox);
            console.log(`Price per token: ${price}`);
            ```

2. **`buildBabelContract(tokenId: string): string`**

     - Constructs a Babel Fee ErgoTree for a specified token ID.

3. **`isValidBabelBox(box: Box<Amount>): boolean`**

      - Checks if a given box is a valid Babel Fee box.

4. **`extractTokenIdFromBabelContract(ergoTree: string): string`**

      - Extracts the token ID from a Babel Fee ErgoTree.

5. **`isBabelContractForTokenId(ergoTree: string, tokenId: string): boolean`**

     - Validates that a Babel Fee contract matches a given token ID.

---

### Box Discovery and Identification



The hexadecimal representation of the Babel Fees contract is:
```
100604000e20{tokenId}0400040005000500d803d601e30004d602e4c6a70408d603e4c6a7050595e67201d804d604b2a5e4720100d605b2db63087204730000d606db6308a7d60799c1a7c17204d1968302019683050193c27204c2a7938c720501730193e4c672040408720293e4c672040505720393e4c67204060ec5a796830201929c998c7205029591b1720673028cb272067303000273047203720792720773057202
```
Replace `{tokenId}` with the specific token ID and use this as a parameter in the API endpoint: `https://api.ergoplatform.com/api/v1/boxes/unspent/byErgoTree/{ErgoTree}`


```typescript
const fetchBabelBox = async (ergoTree: string) => {
  try {
    const response = await fetch(`https://api.ergoplatform.com/api/v1/boxes/unspent/byErgoTree/${ergoTree}`);
    const json = await response.json();
    return json.items[0]; // Returns the first Babel Box
  } catch (error) {
    console.error("Error fetching Babel Box:", error);
    return null;
  }
};
```


### Tutorials

[this guide](http://147.182.244.219/ergobabelfees.html) provides a tutorial on how mint a token, create your babel box, and self-sign on a web application with Babel Fees.

---

### Development Insights

#### Key Updates from `CHANGELOG.md`

- **Validation Enhancements**:

    - Type validation for Babel Box fields (`R4`, `R5`) introduced in version `0.1.16`.

- **Module Export Fixes**:

     - Improved ESM and CommonJS export compatibility in version `0.1.10`.

#### Package Metadata

- **Version**: `0.1.18`
- **Dependencies**:
- 
    - `@fleet-sdk/core`
    - `@fleet-sdk/common`
    - `@fleet-sdk/serializer`
  
- **Environment**:

    - Requires Node.js 18 or above.

---

### Testing and Validation

#### Unit Testing Example

```typescript
describe("BabelSwapPlugin Tests", () => {
  it("should integrate Babel Fee inputs and outputs", () => {
    const babelBox = { /* Mock Babel Box */ };
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
