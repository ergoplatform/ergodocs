# Mathematical Fun with ErgoScript


Just for fun, I decided to see how hard it would be to create a "bounty" protected by some mathematical problem.  I was inspired by today's [announcement](https://aperiodical.com/2019/09/42-is-the-answer-to-the-question-what-is-80538738812075974%c2%b3-80435758145817515%c2%b3-12602123297335631%c2%b3/) that 42 can be written as the sum of three cubes:

> 42 = (−80538738812075974)^3 + 80435758145817515^3 + 12602123297335631^3

I created the following trivial contract:

    {
      val a = getVar[BigInt](1).get
      val b = getVar[BigInt](2).get
      val c = getVar[BigInt](3).get

      a * a * a + b * b * b + c * c * c == 42
    }

I converted this to a P2S address using a [simple P2S web tool](https://wallet.plutomonkey.com/p2s/?source=ewogIHZhbCBhID0gZ2V0VmFyW0JpZ0ludF0oMSkuZ2V0CiAgdmFsIGIgPSBnZXRWYXJbQmlnSW50XSgyKS5nZXQKICB2YWwgYyA9IGdldFZhcltCaWdJbnRdKDMpLmdldAoKICBhICogYSAqIGEgKyBiICogYiAqIGIgKyBjICogYyAqIGMgPT0gNDIKfQ==) that I'm working on, which gave me this P2S address:

> [YUgUAFeNudkkLfjWcnXfg6HphUDaWdaR88yTQHeP6oozcvvwbM74SRZPW1R3WrqYmyp5vM4PhC2SuTfMA](https://explorer.ergoplatform.com/en/addresses/YUgUAFeNudkkLfjWcnXfg6HphUDaWdaR88yTQHeP6oozcvvwbM74SRZPW1R3WrqYmyp5vM4PhC2SuTfMA)

I sent 42 ERG to this address ready for testing.

Now, in order to claim the "bounty", I created an unsigned transaction with the three values above included in the `extension` field under `spendingProof`.  No signature was necessary, of course, just the correct values that solve the puzzle. I successfully claimed the bounty and sent it on to the [crowdfunding CLI project](https://www.ergoforum.org/t/simple-crowdfunding/70)!

Notes:

* It would be good to have better documentation for ErgoScript; in particular, I was confused about BigInt and whether it represented 256-bit integers as noted [here](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/9169e8f594f61942862383425c4837bfb42680ab/docs/LangSpec.md), or arbitrary-precision integers due to the use of `java.math.BigInteger` internally -- it has now been confirmed to represent 256-bit integers.
* It would have been nice to test the script properly somehow in a standalone manner e.g. write test cases for it. I know that this is possible in Scala but maybe a tutorial on this would be good (or even better for non-Scala developers - some way to more easily work with ErgoScript outside of Scala?)
* The explorer doesn't currently show extension data, so I was a bit disappointed you couldn't really see the solution to the puzzle in the explorer very well.

Any feedback is welcome!

Taken from: [Mathematical Fun with ErgoScript](https://www.ergoforum.org/t/mathematical-fun-with-ergoscript/76)
