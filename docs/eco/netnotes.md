# NetNotes

NetNotes is a cross-platform reactive application framework and cryptocurrency management suite. It integrates blockchain networks like Ergo and centralized exchanges such as KuCoin through a modular, messaging-driven architecture.

NetNotes enables secure wallet management, node and explorer control, transaction transparency, and direct API integrations through built-in applications. It includes an encrypted local database for secure data storage without requiring external services.

---

## About NetNotes

* **Reactive Messaging System**
  All blockchain functionality is wrapped in a message-driven architecture. Wallet actions, node operations, explorer queries, and transactions are processed through structured messages. Users can review and approve every message before signing, ensuring full control over blockchain interactions.

* **Encrypted Local Database**
  NetNotes includes a built-in encrypted database for managing wallets, transactions, contact lists, and custom data. No external database configuration is needed.

* **Built-In Applications**
  NetNotes supports internal applications that bring external data directly into the system. Available integrations include:

  * Spectrum Finance for token price data
  * KuCoin API for market charts and trading data

  Planned integrations:

  * Rosen Bridge API
  * Ergo Mixer API

* **Direct Message Review Before Signing**
  Before any transaction is signed, the corresponding message is displayed for user verification. This prevents unauthorized or hidden operations.

---

## Features

* Reactive event-driven architecture
* Encrypted local database for contacts and transactions
* Transparent message review before signing
* Linux and Windows support
* Integration with ErgoDEX and Spectrum Finance
* Centralized exchange market data from KuCoin
* Built-in application system for API integrations
* AES-encrypted wallet data storage
* Application launcher with update management and integrity verification

---

## Developer Integration

NetNotes provides a foundation for building custom applications directly within its environment. Developers can extend the system using its internal messaging framework and encrypted database to create additional tools and interfaces.

### Key Integration Points

* **Messaging Interface**
  Applications communicate through the message bus. Messages can trigger wallet actions, interact with blockchain explorers, or query market data.

* **Custom API Applications**
  Developers can create apps that integrate external APIs into the NetNotes environment. Data fetched through APIs can be stored securely using the encrypted database and displayed through the application interface.

* **Secure Data Handling**
  All data storage is handled through the encrypted local database, reducing the need to manage separate storage layers.

* **Signing Workflows**
  Applications can prepare blockchain transactions by assembling message payloads. NetNotes will handle transaction signing after the user approves the prepared message.

### Example Use Cases

* Build an app that fetches and visualizes historical token prices
* Create a transaction monitoring tool for a set of Ergo addresses
* Integrate a new decentralized protocol by consuming its API

If you are interested in building on NetNotes, explore the [NetNotes Engine Repository](https://github.com/networkspore/netnotes-engine) to understand its messaging architecture and backend services.

---

## Repositories

* [NetNotes Engine (Core Messaging and Blockchain Logic)](https://github.com/networkspore/netnotes-engine)
* [NetNotes Linux Client](https://github.com/networkspore/Netnotes-Linux)
* [NetNotes Cross-Platform Client + Launcher](https://github.com/networkspore/Netnotes)
