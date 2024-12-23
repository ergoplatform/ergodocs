# Getting Started with Off-the-Grid Ergo Trading Bot

This guide provides a thorough walkthrough for setting up and operating the **[Off-the-Grid Ergo Trading Bot](https://github.com/Telefragged/off-the-grid)** decentralized grid trading bot on the Ergo blockchain.

/// details | Video Guide
    {type: info, open: true}
Alternatively, a video walkthrough from MarcTheShark can be found here: [Ergo Grid Trading Bot Setup](https://www.youtube.com/watch?v=LsRb8_G9rzE)
///

---

## Prerequisites

Before proceeding, ensure the following:

1. **Knowledge and Tools:**

    - Basic understanding of the Ergo blockchain and grid trading strategies.
    - Familiarity with Rust programming language and CLI tools.

2. **Environment Setup:**

    - Installed [Rust](https://rustup.rs/) and Cargo (Rust's package manager).
    - Configured Ergo node and wallet. Follow [Ergo Node Setup](https://docs.ergoplatform.com/node/install/) and [Wallet Guide](https://docs.ergoplatform.com/node/wallet/).

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

2. **Set Up Wallet:**

    Follow the Ergo wallet setup guide. Ensure the wallet is initialized and synchronized.

3. **Generate Scans Configuration:**

    Run the following command to generate `scan_config.json`:

    ```bash
    off-the-grid scans create-config
    ```

    To include all existing boxes, add `--rescan` to the command.

---

### 3. Fetch Token Information (Optional)

For better usability, update the token list:

```bash
off-the-grid tokens update
```

This fetches token details from Spectrum's API and saves them locally.

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

---

### 7. Optimize and Analyze

1. **Performance Monitoring:**

    Check logs to identify issues or opportunities for improvement:

    ```bash
    off-the-grid logs tail
    ```

2. **Experiment with Parameters:**

    Test various configurations to find optimal settings for market conditions.

3. **Integrate Analytics:**

    Use tools like Spectrum to track market trends and evaluate the bot's performance.

---

## Best Practices

- **Security:** Safeguard your API keys and wallet credentials.

- **Caution:** Avoid over-investing in untested strategies or assets.

- **Stay Updated:** Keep the bot, tokens, and configs up-to-date with regular updates.

For additional assistance, consult the repository's documentation or contact the community.

