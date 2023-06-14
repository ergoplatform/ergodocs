
# Templatized ErgoTree

One issue with embedded constants in contracts is it prevents effective optimization through caching. Each constant in the body of ErgoTree can be replaced with an indexed placeholder node (see 63 ConstantPlaceholder). Each placeholder has an index of the constant in the constants collection of ErgoTree. This transformation is part of the compilation and is performed ahead of time, meaning each ErgoTree will have an array of all the constants extracted from its body. Each placeholder refers to the constant by the constant’s index in the array.

Therefore, the format of the serialized ErgoTree contains:

- The bytes of a collection with segregated constants.
- The bytes of script expression with placeholders.


This separation means that we can use the script expression bytes as a key in the cache. After the constants are segregated, what remains is the template. Hence, instead of applying steps 1-2 from section D.2.1 to constant-full scripts, we can apply them to constant-less templates. Before applying steps 3 - 5, we need to bind placeholders with actual values taken from the constants collection and then evaluate both the cost graph and ErgoTree.