# Transaction Signing Process

To initiate a transaction, a spending transaction $tx$ is required as an input. This can be achieved by using $bytesToSign(tx)$. It's important to note that multiple inputs can be signed simultaneously, but the coins to be spent must be specified prior to signing. The current state of the blockchain, or $context$, is also required. The signer has the ability to extend the context by adding values.

With this data, the signer (or prover) of an input begins by reducing the guarding proposition for the input box. This is done by evaluating it using the context. The possible outcomes of this reduction are as follows:

-   The process is aborted if the estimated upper-bound evaluation cost (and verification) is too high.
-   If the result is true, it means that the box can be spent by anyone.
-   If the result is false, it means that the box cannot be spent at all (according to the current context).
-   If the expression still contains predicates over the context, it means more than context is needed to evaluate some predicates over it. The prover can look into its own not yet revealed secrets to extend context. If the secrets are found, the prover evaluates the expression further and proceeds to the next step if there is nothing more to evaluate. Otherwise, the prover aborts.
-   If the expression contains only expressions over secret information provable via $\Sigma$-protocols, this is the most common case, and we will explain it further.

Complex expressions, such as $dlog(x_1) \lor (dlog(x2) /\ dlog(x3))$, where $dlog(x)$ means "prove me knowledge of a secret $w$, such as for a known group with generator $g$, $g^w = x$, via a non-interactive form of the Schnorr protocol", may be encountered. Internally, this expression is represented as a tree (TODO). This proof is to be proven and then serialized into a binary spending proof (which could be included in a transaction) as follows:

**Steps for Proving a Tree:**


1. **Bottom-up:** Each node, whether real or simulated, is marked according to the following rule. DLogNode -- if the secret is known, then it's real, else it's simulated. $\lor$: if at least one child is real, then it's real; else it's simulated. $\land$: if at least one child is simulated, then it's simulated; else it's real. 
    - Note: All descendants of a simulated node will be simulated later, even if they were initially marked as real.
    - The root should end up being real according to this rule -- otherwise, the proof cannot be carried out.

2. **Top-down:** Every child of a simulated node is marked as *simulated*. If two or more children of a real $\lor$ are real, all but one are marked as simulated.
3. **Top-down:** A challenge is computed for every simulated child of every $\lor$ and $\land$, according to the following rules. If $\lor$, then every simulated child gets a fresh random challenge. If $\land$ (which means $\land$ itself is simulated, and all its children are), then every child gets the same challenge as the $\land$.
4. **Bottom-up:** For every simulated leaf, a response and a commitment (i.e., second and first prover message) are simulated according to the Schnorr simulator. For every real leaf, the commitment (i.e., first prover message) is computed according to the Schnorr protocol. For every $\lor$/$\land$ node, the commitment is the union (as a set) of commitments below it.
    - The Schnorr challenge is computed as the hash of the commitment of the root (plus other inputs -- probably the tree being proven and the message).
6. **Top-down:** The challenge for every real child of every real $\lor$ and $\land$ is computed as follows. If $\lor$, then the challenge for the one real child of $\lor$ is equal to the XOR of the challenge of $\lor$ and the challenges for all the simulated children of $\lor$. If $\land$, then the challenge for every real child of $\land$ is equal to the challenge of the $\land$.

    - **Note:** Simulated $\land$ and $\lor$ only have simulated descendants, so there is no need to recurse down from them.

Finally, to obtain a flat binary string containing $(e, z)$ pairs (challenge and prover's response for a leaf sub-protocol) from the tree, follow these steps: (TODO)

<!---TODO: -->