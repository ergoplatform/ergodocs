---
tags:
  - Mempool
  - Visualization
  - Indexing
  - ErgoHack
owner: docs
last_reviewed: 2026-05-30
source_repos:
  - repo: 2ndtlmining/Ergomempool
    branch: main
    paths:
      - README.md
  - repo: SavonarolaLabs/memepool
    branch: main
    paths:
      - package.json
      - src/routes
  - repo: cannonQ/ergo-mempool-watcher
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://ergomempool.com/
  - https://github.com/2ndtlmining/Ergomempool
  - https://github.com/SavonarolaLabs/memepool
  - https://github.com/cannonQ/ergo-mempool-watcher
---

# Ergomempool Visualizer

**Project for [ErgoHack 10: AI on the Ergo Blockchain](https://www.google.com/search?q=ergohack.md)**

### 1\. Introduction

The Ergomempool Visualizer is an open-source application designed to provide a real-time, dynamic visualization of the Ergo mempool. Inspired by similar Bitcoin visualizers, this project aims to offer a clear and intuitive understanding of unconfirmed transactions and recent block activity on the Ergo blockchain. It serves as a valuable tool for anyone interested in monitoring network traffic and blockchain dynamics.

The current public README describes the app as a real-time mempool monitor with multiple visualization modes, transaction-origin detection, wallet highlighting, and platform activity tracking across DEXs, bridges, privacy tools, stablecoin apps, mining pools, exchanges, and other Ergo services.

### 2\. Key Features

The visualizer provides comprehensive insights into the Ergo network:

* **Real-time Block Information:**
  * Displays the last 4 blocks from the Ergo blockchain.
  * Shows essential details including block height, size, and total miner reward (Block reward + Fees).
  * Includes miner identification with logos.
  * Features an animation of mined blocks.
* **Mempool Transaction Monitoring:**
  * Fetches and displays unconfirmed transactions from the Ergo network.
  * Visualizes transactions with their ID, Value, and Size.
  * Transactions are color-coded based on value and size.
  * Highlights transactions based on a connected wallet.
  * Includes the ability to send test and donations.
  * Features a visual representation of transaction packing within a block, presented in a hexagon shape to match the Ergo logo.

### 3\. Technical Details

* **Development Language:** Python webapp making use of Flask.
* **Frontend:** Uses Javascript for animations and to utilize Ergo tooling.
* **Deployment:** Dockerised, making it easier to deploy on Flux. The application is hosted on decentralized infrastructure.
* **AI Assistance:** Developed with the help of three different AI models:
  * Local Ollama with Qwen2.5-Coder14b and Devstral24b.
  * Free ClaudeAI.
* **Wallet Integration:** Makes use of the ErgoDappConnector for wallet integration.
* **Visualization Modes:** The source describes transaction-packing grid, hexagon packing, ball-physics, and grid/table views.
* **Platform Detection:** The app attempts to identify transactions from known Ergo platforms such as ErgoDEX, Spectrum/ErgoDex infrastructure, Rosen Bridge, ErgoMixer, SigmaFi, DuckPools, mining pools, exchanges, Auction House, and Ergo Raffle.

### 4\. Current Status & Progress (ErgoHack 10)

The Ergomempool Visualizer has reached its Minimum Viable Product (MVP) stage and is live for public access. Key progress during ErgoHack 10 includes:

* Successful deployment of a live version of the website.
* Implementation of total block reward calculation (Subsidy + Block fee).
* Integration of Nautilus wallet connection and the ability to highlight user's transactions.
* Development of block animation and mempool block formatting.
* Addition of cosmetic updates, including a logo and improved miner logo backgrounds.
* Implementation of donation and test transaction functionalities within the visualizer.
* Ongoing work on visualizing transaction packing within a block.

### 5\. Lessons Learned

* Leveraging existing Ergo tooling in Java and Typescript might simplify development.
* AI has significantly improved, aiding non-developers in building basic applications.
* The Ergo developer community's job sharing makes it relatively easy to get started.

### 6\. Links

* **Live Website:** [https://ergomempool.com/](https://ergomempool.com/)
* **GitHub Repository:** [https://github.com/2ndtlmining/Ergomempool](https://github.com/2ndtlmining/Ergomempool)
* **ErgoHack Presentation:** [https://ergomempool.com/static/ergohack10-presentation.html](https://ergomempool.com/static/ergohack10-presentation.html)
* **Video Overview:** [https://youtu.be/4wfHir5Steo](https://youtu.be/4wfHir5Steo)

### 6.1 Other Mempool Experiments

[SavonarolaLabs/memepool](https://github.com/SavonarolaLabs/memepool) is a small TypeScript mempool visualization experiment. It is separate from Ergomempool, but useful as another public reference for live mempool UI work on Ergo.

[ergo-mempool-watcher](https://github.com/cannonQ/ergo-mempool-watcher) is an investigative TypeScript tool for local-node mempool analysis. It records mempool transactions and mined blocks to Supabase, then analyzes inclusion rate, dwell time, stuck transactions, and pool-selection behavior.

### 7\. Contribution

As an open-source project, the Ergomempool Visualizer welcomes community contributions. Developers interested in Python, blockchain data visualization, and the Ergo ecosystem are encouraged to explore the GitHub repository.
