Our next example of a multi-stage contract is the Rock-Paper-Scissors game, often used as an introductory example for smart contracts. The game is played between two players, Alice and Bob. Each player chooses a secret move independently, and the game outcome is decided after both secrets are revealed.

Let `a`, `b` ∈ Z<sub>3</sub> be the secret choices of Alice and Bob, respectively, where (0, 1, 2) represent (rock, paper, scissors). If `a = b`, the game is a draw. Otherwise, if `a - b mod 3 = 1`, Alice wins; if `a - b mod 3 = 2`, Bob wins. A key challenge is that the first party to reveal their secret is disadvantaged, as the other party could then adaptively choose their move to guarantee a win. In the physical world, simultaneous revelation prevents this. In the virtual world of blockchains, however, simultaneity cannot be strictly enforced. This potential attack must be handled using cryptographic commitments. The first party (Alice) initially reveals only a commitment to her secret, not the secret itself.

The modified game using commitments proceeds as follows:

1.  **Commitment Phase**: Alice chooses her secret move `a` and a secret random value `s`. She computes a commitment `c = H(a || s)` (where `H` is a hash function like Blake2b256) and publishes `c` (e.g., by locking funds in a contract containing `c`).
2.  **Reveal Phase (Bob)**: Bob chooses and reveals his move `b`. At this point, Alice knows the outcome based on `a` and `b`, but Bob doesn't know `a`.
3.  **Reveal Phase (Alice)**: Alice reveals her original move `a` and the secret `s`. Anyone can now verify that `c = H(a || s)`, confirming Alice didn't change her move after seeing Bob's. The winner is then determined based on `a` and `b`.

This protocol works assuming Alice behaves honestly and reveals `a` and `s` regardless of the outcome. However, a malicious Alice might refuse to reveal her commitment if she knows she lost. Smart contracts must handle such edge cases, as they cannot be easily fixed after deployment. In this example, we must penalize Alice (e.g., by forfeiting her stake) if she fails to reveal her commitment within a specified timeframe (deadline).

The complete game is implemented in ErgoScript using a two-stage protocol:

1.  **Stage 1 (Start Game)**: Alice creates a "start-game" box. This box locks her stake and contains her commitment `c`. The script guarding this box defines the rules for the next stage.
2.  **Stage 2 (End Game)**: Bob spends the start-game box by revealing his move `b` and contributing his stake. This transaction creates one or two "end-game" boxes. These boxes contain the combined stake and are spendable only according to the game's outcome rules (including Alice revealing `a` and `s`, handling draws, wins, losses, and timeouts).

To initiate the game, Alice decides on the stake amount `x` (in nanoErgs), chooses her move `a` and secret `s`, computes the commitment `c = H(a || s)`, and locks `x` nanoErgs along with `c` in the start-game box, protected by the following script (`startGameScript`):

```scala
OUTPUTS.forall(
    {(out:Box) =>
        val b = out.R4[Byte].get
        val bobDeadline = out.R6[Int].get
        bobDeadline >= HEIGHT+30 && out.value >= SELF.value &&
        (b == 0 || b == 1 || b == 2) &&
        out.propositionBytes == outScript
    }
) && OUTPUTS.size == 2 && OUTPUTS(0).R7[SigmaProp].get == alice &&
OUTPUTS(0).R4[Byte].get == OUTPUTS(1).R4[Byte].get // same b
```

The above code requires that the spending transaction create exactly two outputs, one paying to each player in the event of a draw or both paying to the winner otherwise. In particular, the code requires that (1) register R7 of the first output must contain Alice’s public key (for use in the draw scenario), (2) register R4 of each output must contain Bob’s choice, and (3) each output must contain at least x tokens protected by outScript, which is given below:

```scala
val s = getVar[Coll[Byte]](0).get // Alice’s secret byte string s
val a = getVar[Byte](1).get // Alice’s secret choice a
val b = SELF.R4[Byte].get // Bob’s public choice b
val bob = SELF.R5[SigmaProp].get // Bob’s public key
val bobDeadline = SELF.R6[Int].get // after this, Bob wins by default
val drawPubKey = SELF.R7[SigmaProp].get
val valid_a = (a == 0 || a == 1 || a == 2)
val validCommitment = blake2b256(s ++ Coll(a)) == c
val validAliceChoice = valid_a && validAliceChoice
val aliceWins = (a - b) == 1 || (a - b) == -2
val receiver = if (a == b) drawPubKey else (if (aliceWins) alice else bob)
(bob && HEIGHT > bobDeadline) || (receiver && validAliceChoice)
```

The above code protects the two end-game boxes that Bob generates. The condition `(bob && HEIGHT > bobDeadline)` guarantees that Bob automatically wins if Alice does not open her commitment before a certain deadline. Note that Bob has to ensure that R7 of the second output contains his public key. Additionally, he must ensure that R5 of both outputs contains his public key (see below). We do not encode these conditions because if Bob does not follow the protocol, he will automatically lose.
