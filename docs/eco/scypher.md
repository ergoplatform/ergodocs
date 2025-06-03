# SCypher: Blockchain-Hosted BIP39 Seed Cipher

**Project for [ErgoHack 10: AI on the Ergo Blockchain](ergohack.md)**

### 1. Introduction

SCypher is a groundbreaking decentralized tool designed for BIP39 seed phrase encryption. Its core innovation lies in leveraging the Ergo blockchain for immutable and censorship-resistant software distribution. The entire application is stored as encoded fragments across multiple Ergo tokens, creating a truly trustless and autonomous system for critical cryptocurrency security utility.

### 2. Key Innovations

SCypher introduces several novel approaches to software distribution and security:

* **Blockchain-Native Software Hosting:** The complete SCypher application is hosted directly on the Ergo blockchain. It is fragmented and encoded across various Ergo tokens, eliminating reliance on centralized servers or repositories for distribution.
* **Dual Access Methods:** Users can retrieve and reconstruct the SCypher application through two primary methods:
    * A Command Line Interface (CLI) download via `curl`, offering a robust and simple access point.
    * A web interface that automatically reconstructs the application in the browser for ease of use.
* **XOR Encryption:** Utilizes a cryptographically sound XOR-based cipher for encrypting BIP39 seed phrases, ensuring their integrity and validity are maintained.
* **Autonomous Distribution:** The system is self-contained and operates without requiring any central authority or servers for its distribution, embodying decentralized principles.

### 3. Technical Implementation

SCypher's architecture is built for security, resilience, and accessibility:

* **Core Logic:** The primary encryption and reconstruction logic is implemented as a robust Bash script with comprehensive security features.
* **Web Interface:** A user-friendly web interface provides browser-based access, integrating with the Nautilus wallet using the Fleet SDK. This facilitates functionalities like donation transactions directly from the DApp.
* **Storage Optimization:** Data is Base64 encoded and distributed across multiple Ergo tokens, optimizing blockchain storage.
* **File Decompression:** For web browser compatibility, the reconstruction process now utilizes `.gz` format decompression, ensuring reliable file delivery.

### 4. Alignment with ErgoHack X Theme

SCypher perfectly aligns with the theme of "AI on the Ergo Blockchain" by demonstrating an autonomous, trustless software distribution model using Ergo's token system as fundamental infrastructure. This eliminates dependence on centralized repositories while providing a practical and crucial utility for cryptocurrency security. Notably, the project was developed entirely with AI assistance, showcasing the accessibility of blockchain development through AI tooling.

### 5. Current Status & Progress (ErgoHack 10)

During ErgoHack 10, the SCypher project achieved significant milestones:

* The core Bash script, "SCypher v2.0," is fully functional and considered release-ready.
* The web interface has been developed and successfully integrated with the blockchain.
* The Nautilus wallet connection and donation transaction flow are fully operational and have been demonstrated.
* The blockchain download functionality works completely through the web browser, allowing the application file to be reconstructed directly from Ergo.
* Comprehensive documentation (including an AI-made guide for Nautilus integration) and a presentation video have been released.

### 6. Links

* **Live Web Demo:** [https://scypher.vercel.app/](https://scypher.vercel.app/)
* **GitHub Repository (Core Logic):** [https://github.com/moon-miner/bash-BIP39-seed-cypher](https://github.com/moon-miner/bash-BIP39-seed-cypher)
* **GitHub Repository (Web Interface):** [https://github.com/moon-miner/SCypher-web](https://github.com/moon-miner/SCypher-web)
* **Nautilus Donation Guide (Technical Document):** [https://github.com/moon-miner/SCypher-web/blob/main/technical-documents/Donation%20Implementation%20with%20Nautilus%20Wallet%20on%20Ergo.md](https://github.com/moon-miner/SCypher-web/blob/main/technical-documents/Donation%20Implementation%20with%20Nautilus%20Wallet%20on%20Ergo.md)

### 7. Contribution

SCypher is an open-source project welcoming contributions from developers passionate about decentralized security and innovative blockchain applications. Please refer to the GitHub repositories for details on how to contribute.