# Functional Programming

Our next examples demonstrate the functional features of ErgoScript. Suppose we want to allow a box to be spent if all the following 
conditions hold:

1. Spender knows the discrete log of the above EC point `0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352`.
2. All input boxes must be protected by the same ErgoScript program.

The following program encodes these conditions:

    {
       val z = decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS"))
       def sameAsMe(box:Box) = box.propositionBytes == SELF.propositionBytes
       
       proveDlog(z) && INPUTS.forall(sameAsMe)       
    }

The [address corresponding to the above program](https://wallet.plutomonkey.com/p2s/?source=ICAgIHsKICAgICAgIHZhbCB6ID0gZGVjb2RlUG9pbnQoZnJvbUJhc2U2NCgiQWxDR090WktoNjZLTCtnOEd2R29RRHkxUDFQa2h0aFJIYTJLQkloK1d5TlMiKSkKICAgICAgIGRlZiBzYW1lQXNNZShib3g6Qm94KSA9IGJveC5wcm9wb3NpdGlvbkJ5dGVzID09IFNFTEYucHJvcG9zaXRpb25CeXRlcwogICAgICAgcHJvdmVEbG9nKHopICYmIElOUFVUUy5mb3JhbGwoc2FtZUFzTWUpCiAgICB9Cg==) is `3PwBHASpxaJa5i3vmLtUTvEqjbJWcpqnyuX9hSmUbaK2HAmoDLHmYSMm4up5pCRytSStEhsHnzTfpHzvCRZ`
 
One may think that the lack of the `var` keyword may seem restrictive as it enforces everything to be immutable.
For instance, to compute the sum of all the inputs, one might want to store the accumulated value in a `var` and iterate 
over all the inputs, updating the `var` at each iteration.

The following code shows how to compute the sum of all inputs in ErgoScript. Assume that the additional condition
is that the box can only be spent if the sum of all inputs is greater than 1 Erg (or 1000000000 nanoErgs).

    {
       val z = decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS"))
       def sameAsMe(box:Box) = box.propositionBytes == SELF.propositionBytes
       val sum = INPUTS.fold(0L, { (accum:Long, box: Box) => accum + box.value }) 
       
       proveDlog(z) && INPUTS.forall(sameAsMe) && sum > 1000000000       
    }


This [corresponds to the address](https://wallet.plutomonkey.com/p2s/?source=ICAgIHsKICAgICAgIHZhbCB6ID0gZGVjb2RlUG9pbnQoZnJvbUJhc2U2NCgiQWxDR090WktoNjZLTCtnOEd2R29RRHkxUDFQa2h0aFJIYTJLQkloK1d5TlMiKSkKICAgICAgIGRlZiBzYW1lQXNNZShib3g6Qm94KSA9IGJveC5wcm9wb3NpdGlvbkJ5dGVzID09IFNFTEYucHJvcG9zaXRpb25CeXRlcwogICAgICAgdmFsIHN1bSA9IElOUFVUUy5mb2xkKDBMLCB7IChhY2N1bTpMb25nLCBib3g6IEJveCkgPT4gYWNjdW0gKyBib3gudmFsdWUgfSkgCiAgICAgICAKICAgICAgIHByb3ZlRGxvZyh6KSAmJiBJTlBVVFMuZm9yYWxsKHNhbWVBc01lKSAmJiBzdW0gPiAxMDAwMDAwMDAwICAgICAgIAogICAgfQo=)
`49AkSSPuVSQHk17C4JLxhqxH7yL5NMWxdEsELp6MNzYeJZvF7iKk3Jgi4fh96o7RJeaU8JSVPvZ5EhCgboQy9d68QreWaYcVxSUcsd8UCamHPsv9kHzqhe4tAM5D7ZmF` 

