---
owner: docs
last_reviewed: '2026-05-31'
ia_status: directory
source_repos:
  - repo: Telefragged/off-the-grid
    branch: master
    paths:
      - README.md
      - node_config.json
      - matcher_config.json
      - cli/src/commands
source_of_truth:
  - https://github.com/Telefragged/off-the-grid
---

# Getting Started with Off-the-Grid Ergo Trading Bot

This guide covers setup and operation for the **[Off-the-Grid Ergo Trading Bot](https://github.com/Telefragged/off-the-grid)**. Off-the-Grid is a Rust CLI and matcher for decentralized grid trading on Ergo.

/// details | Video Guide
    {type: info, open: true}
Alternatively, a video walkthrough from MarcTheShark can be found here: [Ergo Grid Trading Bot Setup](https://www.youtube.com/watch?v=LsRb8_G9rzE)
///

---

## Operator Model

| Role | What it does | Funds needed |
| --- | --- | --- |
| Grid owner | Creates, lists, inspects, and redeems grid orders. | Funds committed to the grid order. |
| Matcher operator | Watches grid orders and matches them against Spectrum AMM liquidity. | Reward address only; the reward address does not need to be tied to the node wallet. |

The matcher competes with other matchers. If another matcher spends the same grid-order input first, your submitted transaction can fail or never confirm.

## Prerequisites

Before proceeding, ensure the following:

1. **Knowledge and Tools:**
    - Basic understanding of the Ergo blockchain and grid trading strategies.
    - Familiarity with Rust programming language and CLI tools.

2. **Environment Setup:**
    - Installed [Rust](https://rustup.rs/) and Cargo (Rust's package manager).
    - Configured Ergo node and wallet. Follow [Ergo Node Setup](https://docs.ergoplatform.com/node/install/) and [Wallet Guide](https://docs.ergoplatform.com/node/wallet/).
    - Node wallet initialized even for matcher use; node scans need wallet support.

3. **Nix Installation (Optional):**
    - For easier building and execution, install [Nix](https://nixos.org/).

---

## Overview of Off-the-Grid

**Off-the-Grid** enables decentralized, automated grid trading on the Ergo blockchain, providing features such as:

- Secure contract-based trading ensuring order safety.
- Off-chain bots for order tracking and execution.
- Compatibility with Spectrum AMM for liquidity matching.

**Limitations:**

- Contracts are not audited—exercise caution with significant assets.
- Profits are not guaranteed, and risks depend on market conditions.
- The token list is fetched from Spectrum pools through the explorer API by default.
- Grid orders currently trade ERG/token pairs and accumulate profits as ERG.

---

## Step-by-Step Guide

### 1. Clone and Build the Repository

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Telefragged/off-the-grid.git
    cd off-the-grid
    ```

2. **Build with Cargo or Nix:**
    - **With Nix:** (Recommended for simplicity)

        ```bash
        nix build
        ```

        The executable is placed in `./result/bin/off-the-grid`.

    - **With Cargo:**

        ```bash
        cargo build --release
        ```

        The executable is in `./target/release/off-the-grid`.

---

### 2. Node Setup

1. **Node Configuration:**

    Update the `node_config.json` file with:

    - `api_url`: Your Ergo node's API URL (e.g., `http://127.0.0.1:9053`).
    - `api_key`: API key from your Ergo node.

    Example:

    ```json
    {
        "api_url": "http://127.0.0.1:9053",
        "api_key": "your-wallet-api-key"
    }
    ```

    Keep the node API key private. Do not expose a wallet-enabled node API to the public internet.

2. **Set Up Wallet:**

    Follow the Ergo wallet setup guide. Ensure the wallet is initialized and synchronized.

3. **Generate Scans Configuration:**

    Run the following command to generate `scan_config.json`:

    ```bash
    off-the-grid scans create-config
    ```

    To include all existing boxes, add `--rescan` to the command.

    ```bash
    off-the-grid scans create-config --rescan
    ```

---

### 3. Fetch Token Information (Optional)

For better usability, update the token list:

```bash
off-the-grid tokens update
```

This fetches token details from the current set of Spectrum pools and saves them locally. Rerun it as more tokens become available on Spectrum.

---

### 4. Create Grid Orders

1. **Define a Grid Order:**

    Use the `grid create` command to specify trading parameters:

    ```bash
    off-the-grid grid create -t <token_name> -v <total_value> -o <num_orders> -r <high>-<low> -i <grid_id>
    ```

    - `<token_name>`: Name of the token to trade.
    - `<total_value>`: Total Ergo value for the grid.
    - `<num_orders>`: Number of grid orders.
    - `<high>` and `<low>`: Price range for the grid.
    - `<grid_id>`: Unique identifier for the grid.

    **Example:**

    ```bash
    off-the-grid grid create -t COMET -v 10 -o 50 -r 50000-100000 -i comet
    ```

2. **Confirm Transaction:**

    After generating the grid order, review and confirm using on-screen prompts.

---

### 5. Manage and Monitor Grids

1. **List Active Grids:**

    ```bash
    off-the-grid grid list
    ```

    This command displays all active grids with details like bid/ask prices and profit.

2. **View Grid Details:**

    ```bash
    off-the-grid grid details -i <grid_id>
    ```

    Replace `<grid_id>` with the grid's unique identifier.

3. **Redeem Grid Orders:**

    Close or redeem grid orders with:

    ```bash
    off-the-grid grid redeem -i <grid_id>
    ```

---

### 6. Run the Matching Bot

1. **Configure Matcher:**

    Set up the reward address in `matcher_config.json`:

    ```json
    {
        "reward_address": "your_reward_address"
    }
    ```

    Alternatively, use an environment variable:

    ```bash
    export MATCHER_REWARD_ADDRESS="your_reward_address"
    ```

2. **Start the Matcher:**

    ```bash
    off-the-grid matcher
    ```

    The bot logs successful transactions and errors. Multiple matchers may compete for transactions, so occasional failures are expected.

3. **Tune Polling Interval:**

    `matcher_config.json` also supports an `interval` value. The repository example uses:

    ```json
    {
        "reward_address": "",
        "interval": 10.0
    }
    ```

    Shorter intervals may react faster but can increase node/API load.

---

### 7. Optimize and Analyze

1. **Performance Monitoring:**

    Watch terminal output for submitted transaction IDs and errors. A submitted transaction is not guaranteed to confirm.

2. **Experiment with Parameters:**

    Test various configurations to find optimal settings for market conditions.

3. **Integrate Analytics:**

    Use tools like Spectrum to track market trends and evaluate the bot's performance.

---

## Best Practices

- **Security:** Safeguard node API keys and wallet credentials.
- **Caution:** Avoid over-investing in unaudited contracts or untested strategies.
- **Updates:** Pull repository updates, rebuild, rerun `tokens update`, and review sample config changes.
- **Node health:** Keep the node synced before creating grids or running the matcher.
- **Competition:** Treat failed submissions as normal when another matcher spends the same input first.

For additional assistance, consult the repository's documentation or contact the community.
