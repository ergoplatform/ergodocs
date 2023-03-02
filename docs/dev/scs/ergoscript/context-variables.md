# Context Variables

More interesting ErgoScript programs contain predicates defined on context, such as:

    HEIGHT < 4000000            // address 2fp75qcgMrTNR2vuLhiJYQt
    
This uses the context variable `HEIGHT`, representing the height of the block in which the transaction gets mined. 
A box with this address is "anyone-can-spend" if the blockchain height is less than 4000000 and "no-one-can-spend" otherwise. 
There are other context variables such as `OUTPUTS, INPUTS, minerPubKey`. See the [documentation](https://github.com/ScorexFoundation/sigmastate-interpreter/blob/develop/docs/LangSpec.md) for details.
