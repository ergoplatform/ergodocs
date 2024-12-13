# Babel Fees Implementation Guide

## Overview

This guide provides detailed instructions for implementing Babel fees in your Ergo applications. The implementation example demonstrates how to enable users to pay transaction fees using tokens instead of ERG, which is particularly useful for new users who may not have ERG in their wallets.

## Prerequisites

1. Node.js and npm (tested with Node v20.10.0)
2. Fleet SDK core and babel-fees plugin
3. Webpack for building
4. A minted token to use for Babel fees
5. A Nautilus wallet
6. Ubuntu 22.04 LTS (for server setup)

## Implementation Steps

### 1. Token Preparation

First, mint the token you wish to use for Babel Fees:
1. Create your token (e.g., "lightning tokens" with 1,000,000 supply)
2. Note the Asset ID (e.g., `272a4aeba6d1596ee0405b13fa223074077fd31f2d519fcd2f7b1656596db029`)
3. Note the bank wallet address (e.g., `9hqbqkUfC4nmi1fVNcj8B3iEYh9HUnsLazcsRHwjoZJpZbmrCiq`)

### 2. Create Babel Fee Box

Use TokenJay.app to create a Babel Box providing liquidity:
1. Visit [Tokenjay](https://tokenjay.app/)
2. Click "Open App"
3. Navigate to "Purchase Tokens" → "Babel Fee Liquidity"
4. Connect your ErgoPay wallet
5. Create new babel fee box
6. Set your exchange rate (e.g., 0.0001 ERG per 1 token)
7. Set liquidity amount (e.g., 10,000 tokens & 100 ERG)

### 3. Server Setup

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade

# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash

# Restart terminal or reboot
nvm install v20.10.0
nvm install-latest-npm

# Install nginx
sudo apt-get install nginx

# Create project directory
cd /var/www/html
mkdir fleetsdk
cd fleetsdk/

# Install dependencies
npm install @fleet-sdk/core
npm install --save-dev webpack webpack-cli ts-loader html-webpack-plugin typescript
npm install @fleet-sdk/babel-fees-plugin
```

### 4. Configuration Files

Create webpack configuration (`webpack.config.js`):
```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: './src/index.ts',
    devtool: 'inline-source-map',
    module: {
        rules: [
        {
            test: /\.tsx?$/,
            use: 'ts-loader',
            exclude: /node_modules/,
        },
        ],
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.js'],
    },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: 'index.html'
        })
    ]
};
```

Create TypeScript configuration (`tsconfig.json`):
```json
{
    "compilerOptions": {
        "outDir": "./dist/",
        "sourceMap": true,
        "noImplicitAny": true,
        "module": "es6",
        "target": "es5",
        "jsx": "react",
        "allowJs": true
    },
    "include": [
        "./src/**/*"
    ]
}
```

### 5. Implementation Code

Create the main implementation file (`src/index.ts`):

```typescript
import { OutputBuilder, TransactionBuilder } from '@fleet-sdk/core';
import { BabelSwapPlugin } from '@fleet-sdk/babel-fees-plugin'; 

// Configuration - Replace with your values
const AssetID = "272a4aeba6d1596ee0405b13fa223074077fd31f2d519fcd2f7b1656596db029";
const BabelBoxBankAddr = "9hqbqkUfC4nmi1fVNcj8B3iEYh9HUnsLazcsRHwjoZJpZbmrCiq";
const ergoTree = `100604000e20${AssetID}0400040005000500d803d601e30004d602e4c6a70408d603e4c6a7050595e67201d804d604b2a5e4720100d605b2db63087204730000d606db6308a7d60799c1a7c17204d1968302019683050193c27204c2a7938c720501730193e4c672040408720293e4c672040505720393e4c67204060ec5a796830201929c998c7205029591b1720673028cb272067303000273047203720792720773057202`;

// Fetch Babel Box from API
const fetchBabelBox = async () => {
    try {
        const response = await fetch(`https://api.ergoplatform.com/api/v1/boxes/unspent/byErgoTree/${ergoTree}`);
        const json = await response.json();
        const babelBox = json.items[0];

        const additionalRegisters = { 
            R4: babelBox.additionalRegisters.R4?.serializedValue,
            R5: babelBox.additionalRegisters.R5?.serializedValue,
            R6: babelBox.additionalRegisters.R6?.serializedValue,
            R7: babelBox.additionalRegisters.R7?.serializedValue,
            R8: babelBox.additionalRegisters.R8?.serializedValue,
            R9: babelBox.additionalRegisters.R9?.serializedValue 
        }; 
        
        return { ...babelBox, additionalRegisters };
    } catch (error) {
        console.error('Failed to fetch Babel Box:', error);
        return null;
    }
}

// Main Babel Fees transaction function
const BabelFees = async () => {
    try {
        const connected = await ergoConnector.nautilus.connect();
        if (connected) {
            const defaultAddress = await ergo.get_change_address();
            const height = await ergo.get_current_height();
            const babelBox = await fetchBabelBox();

            if (!babelBox) {
                console.log("No suitable Babel Box found.");
                return;
            }

            const unsignedTx = new TransactionBuilder(height)
                .from(await ergo.get_utxos())
                .extend(BabelSwapPlugin(babelBox, {
                    tokenId: AssetID,
                    amount: "50"
                }))
                .to(
                    new OutputBuilder(
                        '1000000',
                        defaultAddress
                    ).addTokens({
                        tokenId: AssetID,
                        amount: "50"
                    })
                )
                .sendChangeTo(BabelBoxBankAddr)
                .payMinFee()
                .build()
                .toEIP12Object();

            const signedTx = await ergo.sign_tx(unsignedTx);
            const txId = await ergo.submit_tx(signedTx);

            if (txId) {
                console.log("Transaction ID:", txId);
            }
        }
    } catch (error) {
        console.error("Transaction Error:", error);
    }
};

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    const PayWithBabelFees = document.getElementById('BabelFees');
    if (PayWithBabelFees) {
        PayWithBabelFees.addEventListener('click', BabelFees);
    }
});
```

### 6. Create HTML Interface

Create `babelfees.html`:
```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ergo BabelFees</title>
    <script defer src="http://YOUR-DOMAIN-OR-IP/fleetsdk/dist/bundle.js"></script>
</head>
<body>
    <div style="padding: 15px;">
        <div>
            <button id="BabelFees">Self Sign with Babel Fees</button>
        </div>
    </div>
</body>
</html>
```

### 7. Build and Deploy

Compile the TypeScript code:
```bash
cd /var/www/html/fleetsdk
npx webpack
```

## Testing

To test your implementation:

1. Create a new Nautilus wallet (0 assets initially)
2. Transfer appropriate amount of tokens to the new wallet
3. Wait for transaction settlement
4. Connect to your test page using the wallet
5. Attempt self-signing with Babel fees

## Important Security Notes

1. Change Address Handling:
   - Current implementation sends change to `BabelBoxBankAddr`
   - Using `defaultAddress` is cleaner but requires security evaluation
   - Consider potential liquidity draining attacks

2. Transaction Monitoring:
   - Implement proper error handling
   - Monitor transaction status
   - Handle concurrent spending attempts

## Reference Implementations
* [Nautilus Wallet implementation](https://github.com/capt-nemo429/nautilus-wallet/pull/82)
* [AppKit implementation](https://github.com/ergoplatform/ergo-appkit/pull/204)
* [Fleet SDK Babel fees plugin](https://fleet-sdk.github.io/docs/plugins/babel-fees)

## Additional Resources
- [EIP-0031 Specification](https://github.com/ergoplatform/eips/blob/master/eip-0031.md)
- [Fleet SDK Documentation](https://fleet-sdk.github.io/docs/plugins/babel-fees)
- [Ergo Platform API Documentation](https://api.ergoplatform.com/api/v1/docs/)




## Wallet Implementation Considerations

### Box Discovery and Identification
The hexadecimal representation of the Babel Fees contract is:
```
100604000e20{tokenId}0400040005000500d803d601e30004d602e4c6a70408d603e4c6a7050595e67201d804d604b2a5e4720100d605b2db63087204730000d606db6308a7d60799c1a7c17204d1968302019683050193c27204c2a7938c720501730193e4c672040408720293e4c672040505720393e4c67204060ec5a796830201929c998c7205029591b1720673028cb272067303000273047203720792720773057202
```
Replace `{tokenId}` with the specific token ID and use this as a parameter in the API endpoint: `https://api.ergoplatform.com/api/v1/boxes/unspent/byErgoTree/{ErgoTree}`

### Implementation Requirements

1. **Fee Calculation and Display**

      - Calculate required Babel fee amount
      - Show clear exchange rates
      - Provide fee comparisons
      - Display transaction status updates

2. **Transaction Management**

      - Monitor mempool for concurrent spending
      - Implement chained transaction support
      - Handle transaction failures gracefully
      - Support multiple users spending same box

3. **Security Considerations**

      - Validate all Babel fee box parameters
      - Implement proper change address handling
      - Consider potential liquidity draining attacks


### Development Tools
- Fleet SDK plugin: `@fleet-sdk/babel-fees-plugin`
- API integration endpoints
- Smart contract templates

