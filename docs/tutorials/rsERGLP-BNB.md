---
tags:
  - rsERG
  - Liquidity Pool
  - LP
  - PancakeSwap
  - BNB Chain
  - Rosen Bridge
  - Bridging
  - DeFi
  - Tutorial
  - Guide
---

# Guide: How to Use rsERG on BNB Chain with PancakeSwap

This tutorial takes you from zero to providing liquidity. You will bridge ERG to BNB Chain with Rosen, verify rsERG on BNB Chain, and then create a spot liquidity position on PancakeSwap.

---

## Step 1: Prerequisites

1.  **Install a BNB Chain-compatible wallet:** Install [MetaMask](https://metamask.io/en-GB) or any wallet supporting BSC (e.g., Enkrypt from MyEtherWallet).
2.  **Add BNB Chain to your wallet:** In Metamask you can go to Settings -> Networks -> BNB, or use [Chainlist](https://chainlist.org/) for a one-click network add, or add it manually (Chain ID `56`, RPC `https://bsc-dataseed.binance.org`, etc.). 
3.  **Fund the wallet with BNB:** You'll need BNB for gas fees on BNB Smart Chain. A few dollars' worth is sufficient for several transactions.
4.  **Prepare ERG in an Ergo wallet:** Use a wallet like Nautilus holding the ERG you want to bridge.
5.  **Obtain USDT (BSC-USD):** You will need a stablecoin like USDT on the BNB Chain to pair with your rsERG in the liquidity pool. You can acquire this on a centralized exchange and withdraw to your BNB wallet, or swap for it on PancakeSwap using BNB.

!!! tip
    It's advisable to use one consistent BNB Chain address for all your actions (receiving the bridge, trading, liquidity, etc.). This makes it easier to track funds and manage token approvals from one place.

---

## Step 2: Bridge ERG to BNB Chain with Rosen

1.  **Open Rosen Bridge:** Go to the [Rosen Bridge dApp](https://app.rosen.tech/).
2.  **Select Source and Target:** Set the source chain to **Ergo** and the target chain to **BNB Chain**.
3.  **Enter Destination Address:** Paste your BNB Chain wallet address (from MetaMask) as the destination. Double-check that it's the correct BSC address.
4.  **Select Asset and Amount:** Choose **ERG** as the token to bridge, and enter the amount you want to send.
5.  **Review Fees:** Rosen will display the bridge fee and network fees. Review these before confirming.
6.  **Confirm and Submit:** Proceed with the bridge. You will need to approve the transaction in your Ergo wallet (e.g., Nautilus) - it will create and sign an Ergo transaction to lock your ERG in the bridge.
7.  **Track the Status:** Stay on the Rosen page; in the "Events" or status section of the app you can monitor your bridge transaction progress. It will show when the transfer is completed.

!!! note "Notes"
    - If Rosen shows an "insufficient ERG" error despite having enough ERG, use Nautilus's **Wallet Optimization** feature to consolidate small UTXOs. This can clear the error.
    - Bridging is not instant. Transfers typically complete in about **1-2 hours**, but this can vary with network conditions. Be patient and monitor the status.
    - Keep your Ergo wallet open until you see the Ergo transaction submitted.

---

## Step 3: Verify and Import rsERG on BNB Chain

Once the bridge is complete, you will receive rsERG tokens on BNB Chain. Before you can use them on PancakeSwap, you need to make them visible in your wallet and in the exchange interface.

1.  **Go to PancakeSwap:** Open [PancakeSwap](https://pancakeswap.finance/).
2.  **Import the rsERG Token:**
    - Navigate to the "Swap" feature.
    - Click on the token selection dropdown (usually showing 'BNB' by default).
    - Paste the official rsERG token contract address for BNB Chain: `0xe0E8a04242f35b95DC64b07E0eAe23A8e43A78e4`.
    - PancakeSwap will find the token. Click "Import" and accept the warning. You should now see rsERG in the swap options and your balance if the bridge was successful.
3.  **Add Token to Wallet:** It's also a good idea to add rsERG as a custom token in your MetaMask wallet for easy tracking. Use the same contract address (`0xe0E8a04242f35b95DC64b07E0eAe23A8e43A78e4`) when importing.

!!! warning "Risk Note"
    Liquidity for rsERG on BNB Chain can be low. This means large swaps can incur significant **price impact (slippage)**. When providing liquidity, be aware of the current token prices and the pool's depth.

---

## Step 4: Provide Liquidity on PancakeSwap

Providing liquidity means you supply two tokens (in this case, rsERG and USDT) to PancakeSwap's pool, earning a share of trading fees in return. **Ensure you understand impermanent loss and the volatility of ERG before providing liquidity**.

1.  **Navigate to the Liquidity Pool:** Go directly to the [rsERG/USDT pool on PancakeSwap](https://pancakeswap.finance/liquidity/pool/bsc/0x609fC7345C5F98ef610650CBa921A52A0ceA9291).
2.  **Connect Your Wallet:** Click "Connect Wallet" on PancakeSwap and select your wallet (e.g., MetaMask). Ensure it's connected to the BNB Chain network.
3.  **Add Liquidity:** Press the "Add Liquidity" button.
4.  **Approve Tokens:** If this is your first time using rsERG or USDT on PancakeSwap, you must approve each token. You'll be prompted to allow PancakeSwap to spend your tokens. It's a good security practice to set a specific approval limit rather than unlimited.
5.  **Enter Liquidity Amounts:**
    - Specify how much rsERG or USDT you want to deposit. The interface will automatically calculate the required amount of the other token based on the current pool ratio.
    - It's possible to use only one asset if the price is outside the active range, but typically you will need both.
6.  **Set Price Range (PancakeSwap V3):**
    - PancakeSwap V3 uses concentrated liquidity. You must set a **price range** for your position. Your liquidity will only earn fees when the trading price is within this range.
    - A narrow range offers higher potential fees but carries a higher risk of the price moving outside your range (at which point you stop earning fees) and experiencing more significant impermanent loss. A wider range is safer but less capital-efficient.
7.  **Review and Confirm:** The interface will show your position details. Double-check everything, then click "Add" and confirm the transaction in your wallet. Once confirmed, you'll receive an NFT representing your liquidity position.

!!! success "Good Practices"
    - Start with a small position to familiarize yourself with how V3 liquidity works.
    - Check the pool's depth and recent volume. A pool with low liquidity means your addition or removal can significantly affect the price. Low volume also means fee earnings might be low.
    - Monitor impermanent loss: If ERG's price moves a lot relative to USDT, the value of your LP position will fluctuate. Be prepared to adjust or remove liquidity if needed.

---

## Step 5: Manage Your Position and Safety Checks

1.  **Track Your LP Position:** View your position under PancakeSwap's **Liquidity** page. It will show your current pool share, value, and unclaimed fees. You can manage your position (add more, remove, or claim fees) from here. The position is represented by an NFT in your wallet; do not transfer this NFT unless you intend to transfer ownership of your liquidity.
2.  **Keep BNB for Fees:** Always maintain a small BNB balance in your wallet for transaction fees (closing positions, removing liquidity, claiming rewards, revoking approvals).
3.  **Revoke Unneeded Approvals:** Periodically visit the [BscScan Token Approval Checker](https://bscscan.com/tokenapprovalchecker) to review which dApps have spending permissions on your tokens. If you no longer plan to provide liquidity, you can revoke the approvals for rsERG and USDT from the PancakeSwap contract to enhance security.

---

## Troubleshooting Common Issues

**Problem:** Rosen Bridge UI shows "insufficient ERG for fees," preventing bridging.  
**Cause:** Your ERG might be fragmented into many small inputs (UTXOs).  
**Fix:** Open Nautilus and run **Wallet Optimization** to consolidate your UTXOs. After optimization, try the bridge again.

**Problem:** Your bridge transaction on BNB Chain is stuck in "pending".  
**Cause:** Network congestion or low gas fee.  
**Fix:** In MetaMask, find the pending transaction and use the "Speed Up" option to resubmit it with a higher gas price.

**Problem:** After bridging, the rsERG token doesn't show up in your MetaMask asset list.  
**Cause:** MetaMask doesn't automatically add custom tokens.  
**Fix:** Manually import the token in MetaMask using the contract address: `0xe0E8a04242f35b95DC64b07E0eAe23A8e43A78e4`.

**Problem:** A swap on PancakeSwap shows an unexpectedly high price impact.  
**Cause:** rsERG liquidity is low.  
**Fix:** Reduce the swap amount and consider splitting your trade into smaller chunks. Always review the price impact percentage before confirming a swap.

---

## Quick Reference Links

* **PancakeSwap:** [https://pancakeswap.finance/](https://pancakeswap.finance/)
* **rsERG/USDT Liquidity Pool:** [https://pancakeswap.finance/liquidity/pool/bsc/0x609fC7345C5F98ef610650CBa921A52A0ceA9291](https://pancakeswap.finance/liquidity/pool/bsc/0x609fC7345C5F98ef610650CBa921A52A0ceA9291)
* **rsERG on DexTools:** [https://www.dextools.io/app/en/bnb/pair-explorer/0x609fc7345c5f98ef610650cba921a52a0cea9291](https://www.dextools.io/app/en/bnb/pair-explorer/0x609fc7345c5f98ef610650cba921a52a0cea9291)
* **Rosen Bridge dApp:** [https://app.rosen.tech](https://app.rosen.tech)
* **BscScan Token Approval Checker:** [https://bscscan.com/tokenapprovalchecker](https://bscscan.com/tokenapprovalchecker)
