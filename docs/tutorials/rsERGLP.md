# Comprehensive Guide: Participating in rsERG/ETH Liquidity Pools

This guide walks you through the process of participating in rsERG/ETH liquidity pools. It covers essential precautions, the bridging process, and how to provide liquidity on Uniswap step by step. 


---

## Table of Contents
1. [Important Notes](#important-notes)
2. [Preparing for the Bridge](#preparing-for-the-bridge)
3. [Bridging Assets Using Rosen](#bridging-assets-using-rosen)
4. [Adding rsERG to MetaMask](#adding-rserg-to-metamask)
5. [Step-by-Step: Providing Liquidity on Uniswap](#step-by-step-providing-liquidity-on-uniswap)
6. [Additional Tips and Notes](#additional-tips-and-notes)

---

## Important Notes

### ERGO Token Contract Address

- **ERGO Token Contract**: `0x6C060Ba738af39A09F3b45ac6487dFC9Ebb885f6`
- Always verify the token contract address on the [Rosen asset list](https://app.rosen.tech/assets) or on [Etherscan](https://etherscan.io/address/0x6C060Ba738af39A09F3b45ac6487dFC9Ebb885f6). Avoid using addresses shared via DMs or chats, as there are scams, especially on EVM chains.


### Liquidity Pools (LPs)
Liquidity pools are versatile financial tools used by both small investors and large entities. By providing liquidity, you can:

- **Earn Swap Fees**: LP providers share the swap fees paid by traders.
- **Hedge Risk**: By pooling multiple assets, you can reduce losses in volatile markets.

LPs are relatively safe, especially when using verified decentralized exchanges (DEXs) with high liquidity. However, it’s essential to do your own research (DYOR) to understand the risks involved.

---

## Preparing for the Bridge

Before bridging ERG to ETH, ensure you have an Ethereum wallet with enough ETH for gas fees. Recommended wallets include MetaMask and Rabby Wallet, both of which support hardware wallets for added security.

---

## Bridging Assets Using Rosen

To bridge ERG through Rosen, follow these steps:

1. **Access Rosen Bridge**: Visit the [Rosen Bridge application](https://app.rosen.tech/).
2. **Select Source and Target Chains**: Choose 'Ergo' as the source and 'Ethereum' as the target.
3. **Enter Destination Address**: Fill in the Ethereum destination address where you want to receive the assets.
4. **Select Token and Amount**: Choose 'ERG' as the token and specify the amount you wish to bridge.
5. **Review Fees**: The Rosen UI will display both the transaction fee and the bridge fee before you proceed.

By following these steps, you can efficiently bridge your assets using Rosen Bridge.

- **Consolidate Your Wallet**: If you encounter an "insufficient ERG" message but have funds, consolidate your wallet using Nautilus > Wallet Optimization.
-  **Transaction Timing**: Transfers typically take around 2 hours, but delays can occur.
- **Monitor Transaction Status**: Track your transaction progress on the [Rosen events page](https://app.rosen.tech/events).




---

## Adding rsERG to MetaMask

After bridging the rsERG token, you may need to manually add rsERG to your MetaMask to view your assets. Here’s how to do it:

### Step 1: Open MetaMask
- In your MetaMask wallet, click on **"Assets"**.

### Step 2: Add Token
- Scroll down and click on **"Import Tokens"**.

### Step 3: Add Custom Token
- Paste the rsERG contract address (`0x6C060Ba738af39A09F3b45ac6487dFC9Ebb885f6`) into the **Token Contract Address** field.


### Step 4: Confirm
- Click **"Add Custom Token"** and your rsERG tokens will now be visible in your MetaMask wallet.

---

## Step-by-Step: Providing Liquidity on Uniswap

Follow these steps to provide liquidity in the rsERG/ETH pool on Uniswap:

### Step 0: Enable Smart Transactions in MetaMask
1. **MetaMask Advanced Settings**: Enable the "Smart Transactions" feature to ensure that if a transaction fails or gas fees exceed the market rate, the transaction will be reverted at no cost. This may take about 2 minutes to process.

### Step 1: Open Uniswap
- Access Uniswap via [this link](https://app.uniswap.org/) or by visiting it through a reliable source like DefiLlama (navigate to Chains > Ethereum > Uniswap).



### Step 2: Connect Your Wallet

- Connect Your Wallet

![Opening Uniswap](2.jpg)

- Select your ETH address that holds rsERG tokens.

![Connecting Wallet](3.jpg)

### Step 3: Confirm Permission
- Once connected, confirm that Uniswap has permission to access your wallet.

![Confirming Permission](4.jpg)

### Step 4: Access the Pool Section
- Navigate to the “Pool” tab and click on “+ New Position.”

![Access Pool](5.jpg)

### Step 5: Choose the ETH/rsERG Pair
- Enter ETH in the left field and copy-paste the rsERG contract address (`0x6C060Ba738af39A09F3b45ac6487dFC9Ebb885f6`) on the right side.

![Choosing ETH/rsERG Pair](7.jpg)

### Step 6: Select the Fee Tier
- The rsERG/ETH pair has a 1% fee pool, which is usually selected by default.

![Selecting Fee Tier](8.jpg)

### Step 7: Enter the Deposit Amount
- Input the amount of ETH or rsERG you want to provide. The system will automatically calculate the corresponding amount of the other asset (50/50 ratio).

![Entering Deposit Amount](9.jpg)

### Step 8: Preview and Confirm the Transaction
- If you have enough assets, click “Preview” to review the transaction details. Then click “Add” to initiate the liquidity transaction.

![Previewing Transaction](10.jpg)

### Step 9: Approving rsERG Interaction with Uniswap
- Uniswap will require your approval to interact with your rsERG tokens.
    - **Infinite Approval Option**: You can set this approval to an infinite amount, meaning you won’t need to approve every time you interact with the contract. This can be revoked later via Etherscan if necessary.
    - **Exact Amount Option**: Alternatively, you can set the approval to the exact amount of rsERG you plan to use, but this may become inconvenient in the future as you would need to sign the interaction transaction every time.

### Step 10: Confirm the Transaction in MetaMask

- MetaMask will open, showing the gas fees and transaction details. Double-check everything, then confirm the transaction if everything looks correct.

### Step 11: Sign Two Transactions
- **Transaction 1**: Approve Uniswap to interact with your rsERG tokens.
- **Transaction 2**: Send the assets to the liquidity pool.

![Confirming Transaction](12.jpg)

Congratulations! You’ve successfully added assets to the rsERG/ETH liquidity pool.

---

## Additional Tips and Notes

- **Track Your LP Tokens**: After adding liquidity, Uniswap may prompt you to add rsERG and LP tokens to your token list. Do this so that they appear in your wallet's assets tab.
- **Gas Fee Considerations**: ETH gas fees are based on current network load, not the transaction amount. Therefore, providing larger amounts may reduce overall fees as a percentage of the transaction.

To check your liquidity pool positions, visit the "Pool" tab on Uniswap.

---

This guide equips you with the knowledge to participate in rsERG/ETH liquidity pools effectively. Make sure to stay informed about ongoing risks, always verify contract addresses (such as on [Etherscan](https://etherscan.io/address/0x6C060Ba738af39A09F3b45ac6487dFC9Ebb885f6)), and use trusted platforms for your transactions.

*Credit for this guide goes to Vadim on Telegram.*