
# Templatized ErgoTree

One issue with embedding constants directly in contracts is that it prevents effective optimization through caching. To address this, each constant in the body of an ErgoTree can be replaced with an indexed placeholder node (`ConstantPlaceholder`, OpCode 63). Each placeholder has an index referring to the constant in a separate constants collection associated with the ErgoTree. This transformation is part of the compilation process and is performed ahead of time, meaning each ErgoTree will have an array containing all the constants extracted from its body. Each placeholder refers to a constant by its index in this array.

Therefore, the format of the serialized ErgoTree contains:

- The bytes representing a collection of segregated constants.
- The bytes representing the script expression with placeholders instead of constants.


This separation means that we can use the script expression bytes (the template without constants) as a key in a cache. After the constants are segregated, what remains is the template. Hence, instead of applying evaluation steps 1-2 (reduction and cost estimation) from section D.2.1 to constant-full scripts, we can apply them to these constant-less templates. Before applying the final steps 3-5 (signature verification), we need to bind the placeholders with the actual values taken from the constants collection and then evaluate both the cost graph and the ErgoTree.
