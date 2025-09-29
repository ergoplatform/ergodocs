---
tags:
  - rsERG
  - Liquidity Pool
  - LP
  - PancakeSwap
  - Aster
  - BNB Chain
  - Rosen Bridge
  - Bridging
  - DeFi
  - Perpetuals
  - Tutorial
  - Guide
---

# Guide: Bridge rsERG to BNB Chain and create a position on Aster

This tutorial takes you from zero to a live position. You will bridge ERG to BNB Chain with Rosen, verify rsERG on BNB Chain, then create either spot liquidity on PancakeSwap or a leveraged trade on Aster.

/// details | Comprehensive Video Guide
    {type: info, open: true}
For a step by step guide on setting up and using Nautilus, watch the [comprehensive video tutorial](https://www.youtube.com/watch?v=hMwtwlUpnRQ).
///

---

## What Aster is and what Astar is not

Aster is a decentralized exchange on BNB Chain that supports both regular token swaps and high-leverage perpetual futures trading. It aggregates liquidity across exchanges on BNB Chain to offer better trading rate

(Ast*a*r is a completely separate Layer-1 blockchain (a Polkadot parachain) and is unrelated to Aster DEX.)


---

## Useful Links for Aster

- **DEX App:** [Aster DEX](https://www.asterdex.com)
- **Documentation:** [Aster Docs](https://docs.asterdex.com)
- **BNB Chain Directory:** [Aster on DappBay](https://dappbay.bnbchain.org/detail/aster)

---

## Step 1: Prerequisites

1.  **Install a BNB Chain-compatible wallet:** MetaMask or Rabby (browser wallets) work well.
2.  **Add BNB Chain to your wallet:** Use [Chainlist](https://chainlist.org/) for a one-click network add, or add it manually (Chain ID `56`, RPC `https://bsc-dataseed.binance.org`, etc.).
3.  **Fund the wallet with a little BNB:** You'll need BNB for gas fees on BNB Smart Chain. A few dollars' worth of BNB is sufficient for several transactions.
4.  **Prepare ERG in an Ergo wallet:** Use the Nautilus wallet (on Ergo) holding the ERG you want to bridge.
5.  **Open the Rosen Bridge app:** Have the Rosen interface ready in a browser tab.
6.  **Rosen Bridge dApp:** [app.rosen.tech](https://app.rosen.tech)
7.  **Rosen project site:** [rosen.tech](https://rosen.tech)

!!! tip
    It's advisable to use one consistent BNB Chain address for all your actions (receiving the bridge, trading, liquidity, etc.). This makes it easier to track funds and manage token approvals from one place.

---

## Step 2: Bridge ERG to BNB Chain with Rosen

1.  **Open Rosen Bridge:** Go to the [Rosen Bridge app](https://app.rosen.tech).
2.  **Select Source and Target:** Set the source chain to **Ergo** and the target chain to **BNB Chain**.
3.  **Enter Destination Address:** Paste your BNB Chain wallet address (from MetaMask/Rabby) as the destination. Double-check that it's the correct BSC address.
4.  **Select Asset and Amount:** Choose **ERG** as the token to bridge, and enter the amount of ERG you want to send.
5.  **Review Fees:** Rosen will display the bridge fee and network fees. Review these before confirming.
6.  **Confirm and Submit:** Proceed with the bridge. You will need to approve the transaction in your Nautilus wallet - it will create and sign an Ergo transaction to lock your ERG in the bridge.
7.  **Track the Status:** Stay on the Rosen page; in the "Events" or status section of the app you can monitor your bridge transaction progress. It will show when the transfer is completed.

!!! note "Notes"
    - If Rosen shows an "insufficient ERG" error despite having enough ERG, use Nautilus's **Wallet Optimization** feature to consolidate small UTXOs. This can clear the error.
    - Bridging is not instant. Transfers typically complete in about **1-2 hours**, but this can vary with network conditions. Be patient and monitor the status.
    - Keep your Nautilus wallet open until you see the Ergo transaction submitted. The bridge transaction must be signed and broadcast from your wallet.

---

## Step 3: Verify rsERG on BNB Chain before Trading

Once the bridge is done, you will receive rsERG tokens on BNB Chain. It's crucial to verify you have the correct rsERG token contract and are interacting with a legitimate liquidity pool.

### Where to Look:

* **GeckoTerminal:** Use the [GeckoTerminal search for "rsERG" on BSC](https://www.geckoterminal.com/bsc/search?q=rsERG). This can show existing pools and the token contract address.
* **PancakeSwap Info:** The [PancakeSwap analytics site](https://pancakeswap.finance/info) (or the PancakeSwap interface itself) can show token details if you search for rsERG.
* **BscScan Token Tracker:** Use the [BscScan Token Approval Checker](https://bscscan.com/tokenapprovalchecker) to see and manage token approvals later (more on this in Step 6).

### What to Check:

1.  **Find the rsERG Pool:** In GeckoTerminal or PancakeSwap's info, locate the liquidity pool for rsERG (e.g. `rsERG/WBNB` or `rsERG/USDT`). Confirm the pool is on BNB Chain (the interface should clearly indicate BSC network).
2.  **Confirm the Token Contract:** On the pool page, note the rsERG token address. Make sure it matches the official rsERG contract on BNB Chain. For reference, the legit rsERG BEP-20 token address is `0xe0E8...78E46`. You can cross-verify this on an explorer like BscScan.
3.  **Follow the Trade Link:** From the analytics page, use the link to open PancakeSwap with the rsERG pair pre-loaded (Gecko Terminal provides a "Trade" button that will route you to PancakeSwap with the token address pre-filled).
4.  **Double-Check in PancakeSwap:** When PancakeSwap opens, it might warn that rsERG is not a common token. Expand the token details to compare the contract address with the one you verified. Only proceed if they match exactly.
5.  **Import Token in Wallet:** After confirming the contract, you may add rsERG as a custom token in your MetaMask/Rabby wallet for easy reference. Use the verified contract address when importing.

!!! warning "Risk Note"
    Liquidity for rsERG on BNB Chain is currently small (only a few thousand dollars in pools). This means large swaps can incur significant **price impact (slippage)**. It's wise to start with a small test trade to see the execution price, and avoid swapping an amount that would drastically move the market price.

---

## Step 4: Connect Your Wallet to Aster

1.  **Open Aster DEX App:** Visit [Aster DEX](https://www.asterdex.com) in your browser. (If using a wallet's built-in browser or mobile, navigate to the app through there.)
2.  **Connect Wallet:** Click "Connect" (often at the top-right) and choose your wallet. Aster supports MetaMask and Binance Wallet extensions, or WalletConnect for mobile wallets.
3.  **Select Network:** If prompted, ensure **BNB Chain** is selected as the network within Aster. The DEX is multi-chain, so it may ask which chain you want to use - choose BNB Smart Chain.
4.  **Sign the Request:** Your wallet will ask you to sign a connection message (this is not a transaction, just proof of ownership). Approve the signature to log in to Aster.
5.  **Permissions:** Aster might request certain permissions. It's generally just the basic wallet access and message signing - review the details and approve. (If any unexpected permission is asked, be cautious.)

At this point, you should see your wallet address connected on Aster, and you can access the trading interface. For more background on Aster's trading modes, fees, and features (like Simple vs. Pro mode, or 1001x leverage), refer to the [Aster Docs](https://docs.asterdex.com) for a detailed product guide.

---

## Step 5: Choose Your Path - Liquidity or Perpetuals

At this stage, you have rsERG on BNB Chain and your wallet is connected to Aster. You can now either provide liquidity on PancakeSwap (to earn fees from swaps) or trade on Aster with leverage. Below are Path A and Path B instructions for each approach.

### Path A: Provide Spot Liquidity on PancakeSwap

Providing liquidity means you supply two tokens (rsERG and another token like BNB or USDT) to PancakeSwap's pool, earning a share of trading fees. **Ensure you understand impermanent loss and the volatility of ERG before providing liquidity**.

1.  **Find the Pool on GeckoTerminal:** Using the rsERG search results on [GeckoTerminal](https://www.geckoterminal.com/bsc/search?q=rsERG), choose the pool you want (for example, `rsERG/WBNB` or `rsERG/USDT`). Click its "Trade" button, which will open PancakeSwap with that pair.
2.  **Connect Wallet on PancakeSwap:** Once PancakeSwap opens, connect your MetaMask/Rabby wallet (ensure it's on BNB Chain network).
3.  **Approve Tokens:** If this is your first time using rsERG (or the paired token) on PancakeSwap, you must approve each token for the liquidity contract. When prompted, allow PancakeSwap to spend your rsERG tokens (and the other token, e.g. WBNB). It's recommended to set a low approval limit initially (perhaps just the amount you plan to add) rather than unlimited, as a safety measure. You can always approve more later.
4.  **Enter Liquidity Amounts:** Specify how much rsERG and the other token to deposit. PancakeSwap V3 uses concentrated liquidity, so you'll also need to set a **price range** for your liquidity position. For example, you might provide liquidity only when ERG is between \$0.5 and \$1.0 (the interface will guide this with a slider or inputs). If you're unsure, you can use the default full range or a wide range, but note that a very wide range is similar to V2 liquidity and a narrow range is higher risk/reward.
5.  **Review Position Details:** The interface will show your pool share, the fees tier (e.g. 1% or 0.25%), and the amounts of each token. Double-check that the numbers look correct and that you are comfortable with the chosen price range and pool fee tier.
6.  **Add Liquidity (Confirm):** Click "Add" or "Supply" and confirm the transaction in your wallet. You will have to approve the transaction which will deposit both tokens into the pool. Once confirmed and mined, you'll receive LP tokens representing your share.
7.  **(Optional) Add LP Token to Wallet:** PancakeSwap might show a prompt to add the LP token to your wallet. This isn't strictly necessary (and LP tokens on PancakeSwap V3 might not appear as a single token in MetaMask since positions are represented as NFTs in V3). You can always track your liquidity position via the PancakeSwap Liquidity page.

!!! success "Good Practices"
    - Start with a small position to familiarize yourself with how V3 liquidity works. You can add more later once you're confident.
    - Check the pool's depth and recent volume before deciding your deposit size. A pool with only ~$3,000 liquidity (as in rsERG/WBNB) means your addition or removal can significantly affect pool composition and price. Also, low volume means fee earnings might be low.
    - Monitor impermanent loss: If ERG's price moves a lot relative to the paired asset, the value of your LP position will fluctuate. Be prepared to adjust or remove liquidity if needed.

### Path B: Trade Perpetuals on Aster (Leveraged Trading)

If you prefer to trade price direction with leverage, Aster provides perpetual futures. You can go long (bet on price going up) or short (bet on price going down) with up to 1001x leverage on some markets.

!!! danger "High Risk"
    This is advanced and risky; use leverage with caution.

Before trading, you need to deposit collateral into Aster as margin for your trades (Aster uses a deposited balance for trading, rather than directly using tokens from your wallet). Typically, you will use a stablecoin like USDT as collateral on Aster.

1.  **Deposit Funds to Aster:** In the Aster app, click on "Deposit" (you should see this in the interface once your wallet is connected). Choose the network (BNB Chain) and token you want to deposit as margin, for example USDT. Enter the amount (ensure you leave a bit of BNB for gas) and confirm. Your wallet will ask you to approve and then send the tokens to Aster's smart contract. After a minute or two, the deposited amount will show up in your Aster account balance.
2.  **Select a Market:** Navigate to the Trade/Perpetuals section of Aster. Browse the available markets (e.g., ERG/USDT if available, or major coins if you plan to trade something else). Choose the trading pair or asset you want to trade. Aster might have both crypto and stock perpetuals; ensure you select the correct one.
3.  **Choose Long or Short:** Decide your position direction. **Long** means you profit if the price goes up; **Short** means you profit if the price goes down. On Aster's interface, you'll typically see "Buy/Long" and "Sell/Short" buttons.
4.  **Set Leverage and Order Details:** Choose your leverage level and input how much of your collateral to use for the position (position size). For example, 5x leverage with \$100 USDT will let you open a \$500 position. Be very cautious with high leverage - even a 10% adverse move can liquidate a 10x leveraged position.
5.  **Optional - Set Stop Loss/Take Profit:** It's good practice to set a stop-loss order (an automatic close if the price goes too far against you) and a take-profit target. Aster's order ticket allows adding these conditions. For instance, you might set a stop loss at 10% loss and take profit at 20% gain, or any strategy you prefer.
6.  **Submit the Order:** Double-check your order details (market or limit order type, leverage, etc.) then confirm Buy Long or Sell Short. Approve the transaction in your wallet (this will cost a small BNB gas fee). Your position will be opened, and you'll see it in the Aster interface's positions panel.
7.  **Monitor the Position:** Once open, your position's unrealized PnL (profit and loss) will update in real time. Aster will also show funding rate payments (periodic fees paid between longs and shorts) if applicable. You can close the position anytime by submitting a closing order (or reduce it partially). Make sure to have some BNB for the closing transaction fee as well.

!!! warning "Risk Primer: Trading with Leverage"
    Trading with leverage carries significant risks. Prices can move quickly, and if the market goes against your position, you can be **liquidated** (losing most of your margin). Pay attention to the funding rate on Aster, as it can add costs or income depending on market imbalance over time. Always trade with a plan - define your max loss, use stop-loss orders, and consider using lower leverage especially in volatile markets. It's highly recommended to read [Aster's documentation](https://docs.asterdex.com) on fees, margin, and liquidation so you fully understand the mechanics before using large amounts or high leverage.

---

## Step 6: Manage Your Positions and Safety Checks

Whether you provided liquidity or opened a trade, you should actively manage your assets and permissions:

1.  **Track Your LP Position:** If you added liquidity on PancakeSwap, you can view your position under PancakeSwap's **Liquidity** page. It will show your current pool share, value, and unclaimed fees. You can also remove liquidity from there when you choose. In your wallet, the LP tokens (for V2 pools) or position NFT (for V3) might be visible - do not send or trade this token/NFT, it represents your liquidity. Use the interface to withdraw.
2.  **Track Your Perp Position:** If trading on Aster, keep an eye on the **Positions** or **Portfolio** section on Aster DEX. It will show your open positions, PnL, and margin usage. Make note of your margin ratio - if it drops too low (due to losses), you're at risk of liquidation and may need to add margin or reduce exposure.
3.  **Keep BNB for Fees:** Always maintain a small BNB balance in your wallet. You will need BNB to pay for transactions like closing positions, removing liquidity, claiming any rewards, and even revoking token approvals. Running out of BNB at a critical moment could leave you unable to react quickly.
4.  **Revoke Unneeded Approvals:** Periodically visit the [BscScan Token Approval Checker](https://bscscan.com/tokenapprovalchecker) tool to review which dApps have spending approvals on your tokens. After you're done with providing liquidity or if you no longer plan to use a particular token, you might want to revoke the approval to reduce risk. For example, if you approved an infinite spend of rsERG or USDT for a platform, you can use this tool to revoke that permission when it's no longer needed. (You'll have to pay a small gas fee for each revocation, and only revoke when you have no active need for that contract to save time and fees.)

---

## Troubleshooting Common Issues

**Problem:** Rosen Bridge UI shows "insufficient ERG for fees," preventing bridging.  
**Cause:** Your ERG might be fragmented into many small inputs, and the bridge can't gather enough in one transaction for fees.  
**Fix:** Open Nautilus and run **Wallet Optimization** (found in settings) to consolidate your small boxes/UTXOs. After optimization, try the bridge again - the error should resolve if you indeed had enough total ERG.

**Problem:** Your bridge transaction on BNB Chain is stuck in "pending" for a long time.  
**Cause:** Possibly network congestion or low gas.  
**Fix:** In MetaMask, go to your activity and find the pending transaction (the one that claims the bridged rsERG). Use the "Speed Up" option to resubmit it with a higher gas price. Alternatively, if the transaction is not propagating, you might need to cancel and resend. Ensure your network is set to BNB Chain (to avoid confusion with Ethereum transactions).

**Problem:** After bridging, the rsERG token doesn't show up in your MetaMask asset list.  
**Cause:** MetaMask doesn't automatically know custom tokens.  
**Fix:** Manually import the token. Go to BscScan, find the rsERG token contract, and copy the address. In MetaMask, click "Import Token" and paste the address (MetaMask should then auto-fill "RSERG" if it's the correct address). After adding, your balance will display. (You can also import via the PancakeSwap interface when you're prompted to import the token before trading.)

**Problem:** A swap on PancakeSwap shows an unexpectedly high price impact or you get a warning about insufficient liquidity.  
**Cause:** rsERG liquidity is low, so even moderate trade sizes can move the price or exceed available pool depth.  
**Fix:** Reduce the swap amount and try splitting your trade into smaller chunks. For example, instead of swapping all at once, do it in a few transactions, allowing the market to adjust. Also verify you selected the most liquid pair (e.g., perhaps the USDT pair has more liquidity than the WBNB pair, depending on the pools). Always review the minimum received amount and price impact percentage that PancakeSwap displays before confirming a swap.

---

## Quick Reference Links

* **Aster DEX App:** [https://www.asterdex.com](https://www.asterdex.com)
* **Aster Documentation:** [https://docs.asterdex.com](https://docs.asterdex.com)
* **Aster on BNB Chain DappBay:** [https://dappbay.bnbchain.org/detail/aster](https://dappbay.bnbchain.org/detail/aster)
* **GeckoTerminal search for rsERG (BSC):** [https://www.geckoterminal.com/bsc/search?q=rsERG](https://www.geckoterminal.com/bsc/search?q=rsERG)
* **PancakeSwap Info/Analytics:** [https://pancakeswap.finance/info](https://pancakeswap.finance/info)
* **Rosen Bridge dApp:** [https://app.rosen.tech](https://app.rosen.tech)
* **Rosen Project Site:** [https://rosen.tech](https://rosen.tech)
* **BscScan Token Approval Checker:** [https://bscscan.com/tokenapprovalchecker](https://bscscan.com/tokenapprovalchecker)