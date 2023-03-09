Our next example of a multi-stage contract is the Rock-Paper-Scissors game, often used to introduce Ethereum [11]. The game is played between two players, Alice and Bob. Each player chooses a secret independently, and the game is decided after the secrets are revealed.
Let a, b ∈ Z3 be the secrets of Alice and Bob, respectively, with the understanding that (0, 1, 2) represent (rock, paper, scissors). If a = b, then the game is a draw; otherwise, if a − b ∈ {1, −2}, then Alice wins, else Bob wins. The first party to reveal the secret is disadvantaged since the other party can adaptively choose and win. In the real world, both parties reveal their secrets simultaneously to prevent this. In the virtual world, however, this cannot be enforced. Hence this attack must be handled using cryptographic commitments, where the first party, Alice, does not initially reveal her secret but rather only a commitment to that secret.

The modified game using commitments is as follows:

- Alice commits to her secret a by inputting her commitment c = Comm(a).
- Bob inputs his public value b. At this stage, Alice knows if she won or lost.
- Alice opens her commitment and reveals a, after which the winner is decided.

This works fine, assuming that Alice is well-behaved, i.e., she always opens her commitment irrespective of whether she won or lost. In the real world, however, we must also consider the possibility that Alice never opens her commitment. Border cases such as these make smart contracts quite tricky because adding “bug fixes” to them is impossible once deployed. In this example, we must penalize Alice (with a loss) if she does not open her commitment within some stipulated time.

The complete game is coded in ErgoScript in two stages. In the first stage, Alice creates a start-game box that encodes her game rules. In the second stage, Bob spends the start-game box and creates two end-game boxes spendable by the winner. These new boxes indicate that the game has ended.
To start the game, Alice decides a game amount x (of Ergo’s primary token), which each player must contribute. She then selects a secret s and computes a commitment c = H(a||s) to a. Finally, she locks up x tokens and her commitment c inside the start-game box protected by the following script:"

```java
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

```java
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
