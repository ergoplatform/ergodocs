# Arbit Documentation

[Arbit](https://github.com/ConnecMent/arbit) is a simple and intuitive arbitrage platform designed for decentralized trading on the Ergo and Cardano blockchains. It aims to simplify the arbitrage process, enabling users to identify and execute profitable swaps with minimal setup.

/// details | WIP
    {type: warning, open: true}
This project is a work in progress and is not yet ready for production use.
///


---

## Overview

**What is Arbit?**

Arbit streamlines the process of arbitrage trading by providing a clean and simple interface. The platform identifies opportunities where a user can buy and sell tokens across different decentralized exchanges to make a profit.

- **Supported Tokens:** ERG, ADA, and RSN.
- **Supported Exchanges:** Ergo Dex and Splash.
- **Core Features:**

    - Predefined arbitrage strategies (called "Arbits").
    - Focus on simplicity and usability.
    - Execution of swaps with just a few clicks.

**What is an Arbit?**

An Arbit is a series of swaps that generate profit. For example:

1. Sell 100 X tokens on Exchange A for $100.
2. Buy 105 Y tokens on Exchange B for the same $100.
3. Profit from the additional 5 Y tokens.

---

## Key Features

### Simplicity and Usability

- Designed for users with basic blockchain knowledge.
- Clear interface with no distractions or unnecessary complexity.
- Profitability of swaps displayed prominently.

### Fixed Arbitrage Strategies

- Supports predefined arbitrage paths, such as:

    - ERG ↔ ADA
    - RSN ↔ ADA

- Profit calculations are based on fixed USD values ($50 and $100).

---

## How It Works

1. **Arbitrage Strategy Execution:**

    - Predefined paths calculate profitability based on current market conditions.
    - Fixed token values ($50 and $100) are used for calculations to avoid complexity.

2. **Supported Providers:**

    - **Ergo Dex:** Facilitates ERG and ADA swaps.
    - **Splash:** Enables swapping of RSN and ADA tokens.

3. **Profit Calculation:**

    - Example for a $50 swap:
        - Sell $50 worth of rsADA on Ergo Dex for ERG.
        - Swap ERG for ADA on Splash.
        - Compare the ADA received with the initial $50 equivalent.

---

## Deployment

### Local Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/ConnecMent/arbit.git
    cd arbit
    ```

2. **Set Up Environment Variables:**

    Create a `.env` file in the root directory with the following variables:

    - `SPLASH_API_URL`: API URL for Splash exchange.
    - `ERGO_EXPLORER_API_URL`: API URL for Ergo Explorer.

    Example:

    ```env
    SPLASH_API_URL=https://api.splash.exchange
    ERGO_EXPLORER_API_URL=https://api.ergoplatform.com
    ```

3. **Run the Development Server:**

    Install dependencies and start the development server:

    ```bash
    pnpm install
    pnpm run dev
    ```

    The application will be available at `http://localhost:3000`.

---

## Arbitrage Strategies

The following strategies are implemented in Arbit:

### ERG ↔ ADA Arbitrage

- Leverages Ergo Dex and Splash to identify profitable swaps between ERG and ADA.
- Calculations consider both direct and reverse swap paths for maximum opportunities.

### RSN ↔ ADA Arbitrage

- Utilizes Ergo Dex and Splash for swaps between RSN and ADA tokens.
- Similar profit calculation methods as the ERG ↔ ADA strategy.

---

## Technical Details

### Core Arbitrage Logic

The core logic for arbitrage is implemented in `src/arbitrategy.ts`. It defines a set of predefined strategies for swapping between supported tokens and providers.

### Provider Integrations

- **Ergo Dex (`src/providers/ergodex.ts`):**

    - Interacts with the Ergo Dex SDK for swapping tokens.
    - Supports `x2y` and `y2x` operations.

- **Splash (`src/providers/splash.ts`):**

  - Uses the Splash API to fetch order book data.
  - Supports bid/ask matching for liquidity and price calculations.

---

## Usage Guide

1. **Prepare Tokens:**

    - Ensure you have supported tokens (ERG, ADA, RSN) on Ergo and Cardano chains.
    - Use [Rosen Bridge](https://app.rosen.tech) to bridge assets if necessary.

2. **Visit the App:**

    - Open the application and review the displayed arbitrage opportunities.

3. **Execute a Swap:**

    - If a profitable Arbit is available, execute the swap by following the on-screen instructions.

---

## Contributing

The project is maintained by [ConnecMent](https://github.com/ConnecMent). Contributions are welcome via pull requests.

**Team:**

- Mentors: [@mkermani144](https://github.com/mkermani144), [@fatemeh-ra](https://github.com/fatemeh-ra)
- Mentee: [@SeyedMojtaba1](https://github.com/SeyedMojtaba1)

Special thanks to [@zargarzadehm](https://github.com/zargarzadehm) for Ergo Dex SDK insights.

