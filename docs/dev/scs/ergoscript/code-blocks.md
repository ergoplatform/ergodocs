
# Code-blocks

Multiple lines must be put inside a code-block enclosed in braces as in:

    {
       val out = OUTPUTS(0)
       val in = INPUTS(0)
       in.value == out.value
    }  

Note that arrays in Scala are accessed using round parentheses, not square brackets like in Java or Python. 
Thus, `OUTPUTS(0)` refers to the first element of the `OUTPUTS` array. As in Scala, the last line of a block is the returned value of that block. In the above example, the value returned is the boolean predicate
`in.value == out.value`.  

The above script, [corresponding to the address](https://wallet.plutomonkey.com/p2s/?source=eyAgCiAgdmFsIG91dCA9IE9VVFBVVFMoMCkKICB2YWwgaW4gPSBJTlBVVFMoMCkKICBpbi52YWx1ZSA9PSBvdXQudmFsdWUKfQ==)  `2EUTBShk4TbLWJNwGpkVYh8dAPqbrfvb3p`, 
allows anyone to spend the corresponding box provided that the first input and first output of the transaction have the same value. 

Observe that we used the `val` keyword to define intermediate variables. As in Scala, a `val` defines an immutable object. Therefore, the following snippet is invalid:

     ...
     val out = OUTPUTS(0)        // define an immutable value and set it to the first output.  
     out = OUTPUTS(1)            // cannot reassign a val (will give error)
     ...

Unlike Scala, ErgoScript does not support the `var` keyword, and thus everything is immutable. 


See below how to use lambda syntax to emulate mutable variables.

Multiple blocks can be joined as in: 

    {
      INPUTS(0).id == SELF.id
    } || {
      INPUTS(0).value == 100000 
    }  