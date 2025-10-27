
# FAQs: Rosen Bridge Operations and Features

### What is the bridge fee structure?

Initially, it's the greater of $10 or 0.5% of the transaction value, plus network fees, adjustable by the guard set. The fee is collected in the transferred token on Ergo. Network fees vary: static for Ergo and Cardano, dynamic for EVM-based networks.

### Is there a maximum amount for a single transaction on Rosen Bridge?

No fixed maximum, but large transfers may take longer, from hours to 1-2 days, due to manual guard intervention for fund transfers from cold to hot wallets.

### How is ADA managed within the system for transactions to Cardano?

Network fees in the transaction token on Ergo are sent to a dedicated address for covering network fees on different chains. Currently, the Rosen team manually manages this, with plans for future automation.

### How can a project add new token options to the bridge?

Projects pay a listing fee to the Rosen Fund, with potential discounts for open-source projects. This involves minting wrapped tokens and updating the token map. Fees are distributed to watchers and guards.

### What are the next chains to be added following ADA?

The roadmap includes BTC, BSC (EVM-chains), and Dogecoin in the midterm. Code refactoring aims to facilitate adding new chains, with initial chains being the most challenging.

### What is the size and composition of the team?

The team includes 8 developers, with some frontend and UI tasks outsourced. Additionally, 2-3 developers have worked part-time over the past year, supported by several advisors.

For more information, please see the [Team](rosen-team.md) section.

### How long do transfers take?

Typical transfers complete in about 1–2 hours. Timing depends on:
- Source chain confirmation requirements (e.g., Bitcoin can take longer).
- Watcher consensus on Ergo and Guard validation/signatures.
- Network congestion and large-value cold ➜ hot wallet movements.

If your event appears delayed beyond expectations, see “My event looks stuck — what should I check?” below.

### How many confirmations are required?

Confirmation thresholds are chain-specific and conservatively chosen to avoid reorgs:
- Watchers wait for a minimum number of confirmations on the source chain before proposing an event.
- Guards independently validate and may require additional confirmations for finality.
Thresholds are parameterized and may evolve; the Rosen UI tracks and enforces current requirements.

### How do I track my bridge event?

- Use the Rosen Events page: https://app.rosen.tech/events
- Monitor your source chain transaction on a reputable explorer.
- Events typically progress through stages: detected → approved → signed → broadcast → confirmed.

### My event looks stuck — what should I check?

- Ensure the source transaction is confirmed with enough confirmations.
- Verify you used the correct destination address.
- Check the Events page for status updates or errors.
- Consider network congestion (e.g., high gas or pending mempool).
- If significantly delayed beyond usual windows, contact support through official channels (Telegram/Discord).

### Are there minimums or maximums?

- No fixed maximum; very large transfers can require coordination and may take longer (hours to 1–2 days).
- Practical minimums are enforced by fees and dust thresholds on Ergo; small transfers may be uneconomical.
- The Rosen UI prevents attempts that do not meet current operational thresholds.

### What fees do I pay and when?

- Bridge fee: greater of $10 or 0.5% of the transfer value, plus network fees. Adjustable by the guard set.
- Network fees: depend on source/target chains (static on Ergo/Cardano, dynamic on EVMs).
- Fees are shown up-front in the Rosen UI prior to confirmation. See also [Fees & Dust](fees-and-dust.md).

### How do I verify token contracts and avoid scams?

- Always use the official Rosen assets list: https://app.rosen.tech/assets
- Cross-check on reputable explorers (e.g., Etherscan, BscScan, CardanoScan).
- Avoid contracts shared via chats/DMs; use verified links from docs and the Rosen app.

### What happens during chain reorgs?

- Watchers wait for conservative confirmations; reorgs that occur before thresholds can reset the event.
- Guards validate against finalized states and only sign once safe; this improves security at the cost of latency.

### Do I need KYC to use Rosen?

- No. Rosen is an Ergo-centric bridge with a federated Guard set; normal usage does not require KYC.

### How are fees and rewards distributed?

- Fees are distributed between Watchers and Guards for successful events.
- A portion of RSN emissions rewards participants during bootstrapping.
- See [Tokenomics](rosen-tokenomics.md) for the fee split and emission details.

### Where can I learn the security and operational details?

- Design and assumptions: [concepts-assumptions.md](concepts-assumptions.md)
- Security posture and threats: [security-model.md](security-model.md)
- End-to-end flows: [token-transfer-flows.md](token-transfer-flows.md)
- Operational dust handling: [fees-and-dust.md](fees-and-dust.md)
