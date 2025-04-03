---
tags:
  - Debugging
  - ErgoScript
  - On-Chain
  - debug()
  - Transaction Failure
  - Node Logs
---

# On-Chain Debugging Mechanisms (Limited)

Direct, interactive debugging of ErgoScript during its execution on the live blockchain is generally not possible due to the deterministic and constrained nature of the environment. However, there are limited mechanisms that can provide some insight, primarily focused on logging and analyzing failures.

## `debug()` Function (Experimental)

*   **Concept:** An experimental `debug()` function may be available in recent versions of the ErgoTree interpreter. Its purpose is to allow script writers to output specific information during script evaluation.
*   **Status & Availability:** This feature's availability and exact behavior depend on the interpreter version used by the nodes. **Always check the relevant `sigmastate-interpreter` release notes and Issue [#1035](https://github.com/ergoplatform/sigmastate-interpreter/issues/1035) for the current status.**
*   **Output:** The output from `debug()` is typically expected to appear in the logs of the validating node that processes the transaction containing the script. This usually requires the node to be configured with a specific log level (e.g., `DEBUG`) to capture this information.
*   **Usage:** *(Specific syntax and output format details should be added here once the feature is stable and officially documented).*
*   **Caution:**
    *   Using `debug()` adds computational cost to script execution.
    *   Excessive use can significantly increase node log verbosity.
    *   It is primarily intended for **development and testing phases**, not for widespread use in production contracts deployed on mainnet. Relying on it for core contract logic is discouraged.

## Transaction Failure Analysis

When a transaction attempting to spend a contract-protected box fails validation by a node, the node often logs information about the reason for failure.

*   **Finding Errors:** Check the logs of the node that rejected the transaction (either your own node or potentially an explorer's backend node if using their API for submission). Look for `ERROR` or `WARN` level messages related to transaction validation or script execution around the time the transaction was submitted.
*   **Common Errors:** Logs might indicate:
    *   `Script evaluation failed`: The script returned `false`.
    *   `Assertion failed`: A specific `sigmaProp` condition evaluated to false.
    *   `Cost limit exceeded`: The script execution was too complex.
    *   Type mismatches or other interpreter errors.
*   **Limitations:** While helpful, these logs often don't pinpoint the exact line number within the ErgoScript source. They indicate *that* the script failed, but debugging *why* usually requires correlating the error with off-chain testing and logic review.

These on-chain mechanisms offer limited visibility compared to traditional debugging but can provide valuable clues when troubleshooting transaction failures. They should be used in conjunction with robust [off-chain testing and simulation](debugging.md#core-principles-best-practices).
