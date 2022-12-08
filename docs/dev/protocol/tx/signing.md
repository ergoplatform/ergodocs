# Signing A Transaction

To spend a box, a spending transaction `tx` has as an input; one needs to use `bytesToSign(tx)` (note that different inputs can be signed in parallel; however, the coins being spent are to be specified before signing), as well as the current state of the blockchain, or `context`. The signer also can extend the context by putting values there.

By having this data, a signer (or a prover) of an input first reduces the guarding proposition for the input box by evaluating it using the context. Possible results of the reduction are:

-   abort if the estimated upper-bound evaluation cost (and verification) is too high.
-   true means that the box is spendable by anyone
-   false means that the box is not spendable at all (at least according to the current context)
-   expression still containing predicates over the context. That means more than context is needed to evaluate some predicates over it. Prover can look into its own not yet revealed secrets to extend context. If the secrets are found, the prover the expression further and does the next step if there is nothing more to evaluate. Otherwise, the prover aborts.
-   expression containing only expressions over secret information provable via `\Sigma`-protocols. This is the most common case, and we will explain it further.

We have possible complex expressions, like `dlog(x_1) \lor (dlog(x2) /\ dlog(x3))`, where `dlog(x)` means "prove me knowledge of a secret `w`, such as for a known group with generator `g`, `g^w = x`, via a non-interactive form of the Schnorr protocol". Internally, this expression is represented as a tree (TODO). This proof is to be proven and then serialized into a binary spending proof (which could be included in a transaction) as follows:

**Proving steps for a tree:**


1. bottom-up: mark every node, real or simulated, according to the following rule. DLogNode -- if you know the secret, then real, else simulated. `\lor`: if at least one child is real, then real; else simulated. `\land`: if at least one child simulated, then simulated; else real. 

> Note that all descendants of a simulated node will be later simulated, even if marked as real. This is what the next step will do.

Root should end up real according to this rule -- else you will not be able to carry out the proof.

1. **top-down:** mark every child of a simulated node \"simulated.\" If two or more children of a real `\lor` are real, mark all but one simulated.
2. **top-down:** compute a challenge for every simulated child of every `\lor` and `\land`, according to the following rules. If `\lor`, then every simulated child gets a fresh random challenge. If `\land` (which means `\land` itself is simulated, and all its children are), then every child gets the same challenge as the `\land`.
3. **bottom-up:** For every simulated leaf, simulate a response and a commitment (i.e., second and first prover message) according to the Schnorr simulator. For every real leaf, compute the commitment (i.e., first prover message) according to the Schnorr protocol. For every `\lor`/`\land` node, let the commitment be the union (as a set) of commitments below it.
4. Compute the Schnorr challenge as the hash of the commitment of the root (plus other inputs -- probably the tree being proven and the message).
5. **top-down:** compute the challenge for every real child of every real `\lor` and `\land`, as follows. If `\lor`, then the challenge for the one real child of `\lor` is equal to the XOR of the challenge of `\lor` and the challenges for all the simulated children of `\lor`. If `\land`, then the challenge for every real child of `\land` is equal to the challenge of the `\land`.

> Note that simulated `\land` and `\lor` have only simulated descendants, so there is no need to recurse down from them.

Now, how to get a flat binary string containing `(e, z)` pairs (challenge and prover's response for a leaf sub-protocol) from the tree:
