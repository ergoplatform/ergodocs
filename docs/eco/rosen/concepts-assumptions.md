# RosenBridge Concepts & Assumptions

RosenBridge uses a two-layer, Ergo-centric architecture that enables secure cross-chain transfers without deploying smart contracts on external chains. Consensus and auditability live on Ergo, while external chains only require a multisig or threshold-signature wallet controlled by Guards.

## Two-Layer Architecture

- Layer 1: Watchers
  - Monitor connected chains for deposit/withdrawal intents and report events to Ergo.
  - Verify observed events and work toward consensus on-chain (via “event boxes” on Ergo).
  - Anyone can run a watcher. Watchers do not hold spend keys.

- Layer 2: Guards
  - Verify approved events independently and sign the resulting transaction (for Ergo or the external chain).
  - Hold keys to a multisig/threshold wallet on each connected chain.
  - A predefined set of entities serve as Guards and can change over time.

See also:
- [Watcher](watcher.md)
- [Rosen Guards](rosen-guard.md)

## Core Assumptions

- Multisig/Threshold Wallets
  - For a given external chain (chainX), Guards control a shared wallet via m-of-n multisig or threshold signatures.
  - Bridge safety holds as long as fewer than m Guards are corrupted.
  - Background reading: [Multisig](multisig.md), [Threshold Signatures](threshold.md).

- Independent Guard Validation
  - Watchers may malfunction or behave adversarially. The bridge remains sound because Guards re-validate events independently before signing.

- Confirmations and Finality
  - Watchers require multiple confirmations on the source chain before proposing an event.
  - Watcher consensus on Ergo takes a few blocks.
  - Guards also require sufficient confirmations when validating events.
  - This prioritizes security and robustness over speed to avoid forks, double-spends, and race conditions.

- Ergo-Centric Auditability
  - Most bridge logic is encoded and recorded on Ergo.
  - Eliminates the need for heterogeneous smart contracts on multiple chains and simplifies auditing.

- Metadata Support
  - Cross-chain transfers must carry sufficient message/metadata to identify destination addresses and parameters on the target chain.

- Scalability by Role Separation
  - Watchers actively scan chains and propose events; Guards only verify approved events and sign.
  - Adding watchers increases coverage and liveness without increasing Guard computation.

- Adding New Chains
  - Create a Guard-controlled wallet (multisig/threshold) on the new chain.
  - Implement and deploy the corresponding Watcher(s).
  - Configure Rosen parameters (confirmations, fees, asset maps).
  - No custom on-chain contracts are required on the external network if multisig/threshold capabilities exist.

## Why This Design

- Security: Federated signing with m-of-n (or threshold) minimizes single points of failure.
- Simplicity: Avoids duplicating smart contracts with differing assumptions across chains.
- Transparency: Operations are observable on Ergo, improving auditability.
- Extensibility: New chains can be integrated with minimal coupling, provided they support multisig/threshold signing.

### Architecture at a Glance

```mermaid
flowchart LR
  subgraph ChainX [External Chain (e.g., BTC/ADA/EVM)]
    U[User] -->|Lock tx + metadata| CXMS[Multisig/Threshold Wallet]
  end

  subgraph Ergo
    W1[Watcher]:::watcher
    W2[Watcher]:::watcher
    W3[Watcher]:::watcher
    EB[Event Boxes]
    AEB[Approved Event Box]
    G1[Guard]:::guard
    G2[Guard]:::guard
    G3[Guard]:::guard
    MTX[Signed Tx (mint/burn)]
  end

  classDef watcher fill:#eef,stroke:#336,stroke-width:1px;
  classDef guard fill:#efe,stroke:#363,stroke-width:1px;

  CXMS -->|Confirmations| W1
  CXMS -->|Confirmations| W2
  CXMS -->|Confirmations| W3

  W1 --> EB
  W2 --> EB
  W3 --> EB
  EB -->|consensus| AEB

  AEB --> G1
  AEB --> G2
  AEB --> G3

  G1 --> MTX
  G2 --> MTX
  G3 --> MTX
  MTX -->|Broadcast on Ergo or ChainX| U2[(User Destination)]
```

For an introductory walkthrough, see the overview and user-facing pages:
- Landing: [rosen.md](rosen.md)
- Operations: [Token Transfer Flows](token-transfer-flows.md)
- Fees and housekeeping: [Fees & Dust](fees-and-dust.md)
