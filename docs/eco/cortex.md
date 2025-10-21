# Cortex: Advanced AI-Optimized GPU Miner for Ergo

**Project for [ErgoHack 10: AI on the Ergo Blockchain](ergohack.md)**

### 1. Introduction

Cortex is an advanced, fully open-source GPU miner developed for the Ergo blockchain. Building upon the foundation of established open-source miners and community Stratum pool servers, Cortex integrates cutting-edge AI-driven optimizations to enhance mining efficiency, hardware utilization, and overall system openness. This project aims to leverage AI across all phases, from initial design and resource allocation to code auditing and performance tuning, pushing the boundaries of decentralized mining.

### 2. Key Innovations & AI Integration

Cortex distinguishes itself through its deep integration of Artificial Intelligence at multiple levels:

* **AI in Design & Optimization:** AI is employed from the initial design phase to streamline resource optimization and refine the core architecture.
* **Performance Optimization:** AI analyzes real-time mining statistics (hashrate, power consumption, GPU temperature) to suggest or automatically tune GPU settings for optimal efficiency.
* **Health Monitoring:** AI detects hardware issues or performance degradation early by learning from log patterns and GPU behavior, proactively preventing downtime.
* **Dynamic Nonce Partitioning:** Utilizes Machine Learning to intelligently divide mining work, preventing redundant guesses and adapting in real-time to mining pool responses to improve valid share submission.

### 3. Features & Functionality

Cortex provides a comprehensive set of tools for Ergo miners:

* **CLI CUDA Miner:** Initial setup for NVIDIA GPUs, supporting solo mining directly to an Ergo node (primarily testnet for demo purposes due to single GPU setup).
* **Node Manager Backend:** Handles the download, configuration, launch, and shutdown of both mainnet and testnet Ergo nodes via a simple web application.
* **REST APIs:** Exposes live logs, allows version selection, and provides CLI toggling for mainnet/testnet configurations.
* **Frontend (NodeManager):** A user-friendly web-based dashboard UI for controlling node deployment and miner operations, offering live log previews, configuration editing, and quick access to node APIs.
* **GPU Monitoring & Overclocking:** Provides capabilities for monitoring GPU performance (e.g., when idle or under full load) and basic overclocking controls.
* **AI Training Data Pipeline:** Includes a FastAPI server that parses GPU and nonce data into an SQL database, preparing it for AI model training.
* **Stratum & Pool Integration:** Supports connection to mining pools like Sigs mining pool, with ongoing development for full stratum handshake (subscribe and authorize) and job processing.

### 4. Technical Details

Cortex is built primarily with Python, utilizing frameworks like FastAPI for its data processing backend. It relies on a full Ergo Node instance for mining operations and interacts with GPU hardware through tools like `nvidia-smi` (with ongoing efforts to overcome its limitations for advanced control).

### 5. Current Status & Progress (ErgoHack 10)

During ErgoHack 10, Cortex achieved significant milestones:

* Successfully integrated backend node and miner deployment into the UI.
* Fully functional GPU monitoring under various loads.
* Created a FastAPI server for parsing GPU and nonce data to SQL for AI training.
* Built out the UI interface for the miner.
* Successfully connected to the Sigs mining pool and is actively working on stratum handshake and job processing.
* Node deployment for both mainnet and testnet is fully functional.

### 6. Getting Started

As an open-source project, Cortex's development is publicly accessible. For instructions on setting up and running Cortex, please refer to the project's GitHub repository.

### 7. Links

* **GitHub Repository:** [https://github.com/Cortex-Miner/Cortex](https://github.com/Cortex-Miner/Cortex)

### 8. Contribution

Cortex is an open-source project welcoming contributions from developers interested in AI, blockchain mining, and the Ergo ecosystem. Please refer to the GitHub repository for contribution guidelines and open issues.
