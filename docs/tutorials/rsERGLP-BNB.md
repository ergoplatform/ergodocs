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

## What Aster is and what Astar is not

Aster is a decentralized exchange on BNB Chain. The app supports spot swaps and perpetuals with leverage.  
Astar is a separate Layer One in the Polkadot family. It is a different network and a different product.

Links for Aster  
* App: [Aster DEX](https://www.asterdex.com)  
* Docs: [Aster Docs](https://docs.asterdex.com)  
* BNB directory entry: [Aster on DappBay](https://dappbay.bnbchain.org/detail/aster)

---

## Step 1: Prerequisites

1. Install a wallet that works with BNB Chain. MetaMask or Rabby both work well.  
2. Add BNB Chain to your wallet. Chainlist can help with a one click add.  
   * Chainlist: [Chainlist BNB Chain](https://chainlist.org/chain/56)  
3. Fund a little BNB for gas. A few dollars usually covers several actions.  
4. Hold ERG in a Nautilus wallet for the bridge step.  
5. Open Rosen in a browser tab.  
   * Rosen Bridge: [Rosen Bridge](https://app.rosen.tech)  
   * Rosen overview: [Rosen site](https://rosen.tech)

Tip  
Keep one address for BNB Chain actions. Consistent use improves tracking and approval management.

---

## Step 2: Bridge ERG to BNB Chain with Rosen

1. Open [Rosen Bridge](https://app.rosen.tech).  
2. Set source chain to Ergo.  
3. Set target chain to BNB Chain.  
4. Paste your BNB Chain address from MetaMask or Rabby.  
5. Select ERG and enter the amount.  
6. Review the bridge fee and the network fee.  
7. Confirm and submit.  
8. Track status on the same page in the events section.

Notes that matter  
* Wallet optimization in Nautilus can clear an insufficient ERG message.  
* Completion often lands in one to two hours. Network load can change this.  
* Keep your Nautilus open until you see a submitted transaction.

---

## Step 3: Verify rsERG on BNB Chain before you trade

You need a correct token and a real pool.

Where to look  
* rsERG search on BSC: [GeckoTerminal search](https://www.geckoterminal.com/bsc/search?q=rsERG)  
* PancakeSwap info hub: [PancakeSwap Info](https://pancakeswap.finance/info)  
* Token approvals checker: [BscScan Token Approval Checker](https://bscscan.com/tokenapprovalchecker)

What to check  
1. Open the rsERG pool page on GeckoTerminal.  
2. Confirm the pair and the network label.  
3. Follow the trade link from the pool page to PancakeSwap.  
4. Compare the token address that the DEX loads against the explorer.  
5. Import the token in your wallet only after you confirm the address.

Risk note  
rsERG liquidity on BNB Chain can be small. Large orders can move price quickly. Start with a test swap and confirm expected execution.

---

## Step 4: Connect to Aster

1. Open [Aster DEX](https://www.asterdex.com).  
2. Click Connect and choose your wallet.  
3. Confirm network reads BNB Chain.  
4. If the app prompts for permissions, read them and approve only what you need.

Need more context about modes and fees  
* Read the product guide in the docs: [Aster Docs](https://docs.asterdex.com)

---

## Step 5: Choose your path

You can earn swap fees with spot liquidity or trade direction with leverage.

### Path A: Provide spot liquidity on PancakeSwap

1. From the rsERG search page, open the pool you want and click the trade button.  
   * Search entry point: [GeckoTerminal search](https://www.geckoterminal.com/bsc/search?q=rsERG)  
2. Connect your wallet on BNB Chain.  
3. Approve rsERG when the DEX asks for permission. Approve WBNB if the position also needs it.  
4. Enter deposit amounts. Concentrated liquidity can ask for a price range.  
5. Review price range and expected share.  
6. Confirm the add liquidity transaction in your wallet.  
7. Add the LP token to your wallet if the interface suggests it.

Good habits  
* Use a small approval limit for your first attempt. You can raise it later.  
* Check the pool depth and the recent volume before you size the position.

### Path B: Trade perpetuals on Aster

1. In the Aster app, open Trade or Perpetuals.  
2. Select the market that fits your plan.  
3. Choose Long for upside or Short for downside.  
4. Set leverage and position size.  
5. Place a stop loss and a take profit in the ticket.  
6. Submit the order and sign in your wallet.  
7. Watch the position panel for funding and PnL changes.

Risk primer  
Funding can change your PnL over time. Liquidation can occur if price moves against your margin. Read the fees and risk notes in the docs before you use leverage.  
* Docs entry: [Aster Docs](https://docs.asterdex.com)

---

## Step 6: Manage and review

1. Track your LP position in the DEX interface and in your wallet.  
2. Track your perp position and funding in the Aster position panel.  
3. Keep some BNB aside for exits and for approval revocations.  
4. Use the approvals checker to prune old permissions.  
   * Approvals tool: [BscScan Token Approval Checker](https://bscscan.com/tokenapprovalchecker)

---

## Troubleshooting

Problem  
Rosen displays insufficient ERG for fees  
Fix  
Open Nautilus and run Wallet Optimization. Consolidate small boxes and retry the bridge.

Problem  
Transaction on BNB Chain sits pending  
Fix  
Open your wallet activity. Use speed up with a slightly higher gas price. Confirm network reads BNB Chain.

Problem  
Token fails to appear in the wallet asset list  
Fix  
Open the pool page. Copy the token address from the explorer link. Import the address into your wallet.

Problem  
Unexpected price impact on a swap  
Fix  
Check live liquidity and recent volume on the pool page. Reduce size. Consider more splits across time.

---

## Quick link list

* Aster DEX: [https://www.asterdex.com](https://www.asterdex.com)  
* Aster Docs: [https://docs.asterdex.com](https://docs.asterdex.com)  
* Aster on DappBay: [https://dappbay.bnbchain.org/detail/aster](https://dappbay.bnbchain.org/detail/aster)  
* GeckoTerminal rsERG search: [https://www.geckoterminal.com/bsc/search?q=rsERG](https://www.geckoterminal.com/bsc/search?q=rsERG)  
* PancakeSwap Info: [https://pancakeswap.finance/info](https://pancakeswap.finance/info)  
* Rosen Bridge: [https://app.rosen.tech](https://app.rosen.tech)  
* Rosen site: [https://rosen.tech](https://rosen.tech)  
* BscScan Token Approval Checker: [https://bscscan.com/tokenapprovalchecker](https://bscscan.com/tokenapprovalchecker)
