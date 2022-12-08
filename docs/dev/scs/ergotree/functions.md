# ErgoTree Functions

> This page is a WIP. Please see [ErgoTree.pdf](https://storage.googleapis.com/ergo-cms-media/docs/ErgoTree.pdf) for full details.


| Code | Mnemonic | Description | Description |
|---|---|---|---|
115 | ConstantPlaceholder |  Int    => T | Create special ErgoTree node which can be replaced by constant with given id. 
116 | SubstConstants | Coll[Byte], Coll[Int], Coll[T]    => Coll[Byte] | ... 
122 | LongToByteArray | Long    => Coll[Byte] | Converts Long value to big-endian bytes representation. 
123 | ByteArrayToBigInt | Coll[Byte]    => BigInt | Convert big-endian bytes representation (Coll[Byte]) to BigInt value. 
124 | ByteArrayToLong | Coll[Byte]    => Long | Convert big-endian bytes representation (Coll[Byte]) to Long value. 
125 | Downcast |   (T    => R) | Cast this numeric value to a smaller type (e.g. Long to Int). Throws exception if overflow. 
126 | Upcast |  (T    => R) | Cast this numeric value to a bigger type (e.g. Int to Long) 
140 | SelectField | (T, Byte    => R) | Select tuple field by its 1-based index. E.g. input._1 is transformed to SelectField(input, 1 
143 | LT | T, T    => Boolean | Returns true is the left operand is less then the right operand, false otherwise. 
144 | LE | T, T    => Boolean | Returns true is the left operand is less then or equal to the right operand, false otherwise. 
145 | GT | T, T    => Boolean | Returns true is the left operand is greater then the right operand, false otherwise. 
146 | GE | T, T    => Boolean | Returns true is the left operand is greater then or equal to the right operand, false otherwise. 
147 | EQ | T, T    => Boolean | Compare equality of left and right arguments 
148 | NEQ | T, T    => Boolean | Compare inequality of left and right arguments 
149 | If | Boolean, T, T    => T | Compute condition, if true then compute trueBranch else compute falseBranch 
150 | AND | Coll[Boolean]    => Boolean | Returns true if \emph{all the elements in collection are true. 
151 | OR | Coll[Boolean]    => Boolean | Returns true if \emph{any the elements in collection are true. 
152 | AtLeast | Int, Coll[SigmaProp]    => SigmaProp | ... 
153 | Minus | T, T    => T | Returns a result of subtracting second numeric operand from the first. 
154 | Plus | T, T    => T | Returns a sum of two numeric operands 
155 | Xor | Coll[Byte], Coll[Byte]    => Coll[Byte] | Byte-wise XOR of two collections of bytes 
156 | Multiply | T, T    => T | Returns a multiplication of two numeric operands 
157 | Division | T, T    => T | Integer division of the first operand by the second operand. 
158 | Modulo | T, T    => T | Reminder from division of the first operand by the second operand. 
161 | Min | T, T    => T | Minimum value of two operands. 
162 | Max | T, T    => T | Maximum value of two operands. 
182 | CreateAvlTree |   (Byte, Coll[Byte], Int, Option[Int]    => AvlTree | Construct a new authenticated dictionary with given parameters and tree root digest. 
183 | TreeLookup |   (AvlTree, Coll[Byte], Coll[Byte]    => Option[Coll[Byte]] |  
203 | CalcBlake2b256 |   (Coll[Byte]    => Coll[Byte] | Calculate Blake2b hash from input bytes. 
204 | CalcSha256 |   (Coll[Byte]    => Coll[Byte] | Calculate Sha256 hash from input bytes. 
205 | CreateProveDlog | GroupElement    => SigmaProp | ErgoTree operation to create a new SigmaProp value representing public key of discrete logarithm signature protocol.
206 | CreateProveDHTuple | GroupElement, GroupElement, GroupElement, GroupElement => SigmaProp |  ErgoTree operation to create a new SigmaProp value representing public key of Diffie Hellman signature protocol. Common input: (g,h,u,v)
209 | BoolToSigmaProp |  (Boolean    => SigmaProp) | ... 
212 | DeserializeContext |   (Byte    => T) | ... 
213 | DeserializeRegister |   (Byte, Option[T]    => T | ... 
218 | Apply |(T) => R, T    => R | Apply the function to the arguments.  
227 | GetVar |   (Byte    => Option[T]) | Get context variable with given varId and type. 
234 | SigmaAnd |   (Coll[SigmaProp]    => SigmaProp) | Returns sigma proposition which is proven when \emph{all the elements in collection are proven. 
235 | SigmaOr |   (Coll[SigmaProp]    => SigmaProp) | Returns sigma proposition which is proven when \emph{any of the elements in collection is proven. 
236 | BinOr |   (Boolean, Boolean)    => Boolean | Logical OR of two operands 
237 | BinAnd |   (Boolean, Boolean)    => Boolean | Logical AND of two operands 
238 | DecodePoint| Coll[Byte]    => GroupElement | Convert Coll[Byte] to GroupElement using GroupElementSerializer
239 | LogicalNot | Boolean    => Boolean | Logical NOT operation. Returns true if input is falseand falseif input is true. 
240 | Negation |   (T    => T) | Negates numeric value x by returning -x. 
241 | BitInversion |   (T    => T) | Invert every bit of the numeric value. 
242 | BitOr |   (T, T)    => T | Bitwise OR of two numeric operands. 
243 | BitAnd |   (T, T)    => T | Bitwise AND of two numeric operands. 
244 | BinXor |   (Boolean, Boolean    => Boolean) | Logical XOR of two operands 
245 | BitXor |   (T, T)    => T | Bitwise XOR of two numeric operands. 
246 | BitShiftRight |   (T, T)    => T | Right shift of bits. 
247 | BitShiftLeft |   (T, T)    => T | Left shift of bits. 
248 | BitShiftRightZeroed |  (T, T)    => T | Right shift of bits. 
255 | XorOf |   (Coll[Boolean]    => Boolean) | Similar to allOf, but performing logical XOR operation between all conditions instead of ||