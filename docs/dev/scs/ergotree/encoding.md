# Understanding ErgoTree Encoding

ErgoTree encoding is a binary formatting system designed for the storage, transfer, and cross-platform operation of ErgoTree contracts. This format is advantageous due to its proficiency in the serialization and deserialization of ErgoTree contracts.

## Variable Length Quantity (VLQ) Encoding

The ErgoTree encoding applies Variable Length Quantity (VLQ) encoding for integer representation. VLQ encoding is an effective scheme that accommodates integer representation using a variable number of bytes.

In the following Scala code, we define a method `putULong`, which accepts a single long value and encodes it using VLQ encoding. The encoding process entails iteratively analyzing the input value and writing the encoded bytes to a buffer array.

During the encoding procedure, the method first verifies if the value can be represented using a single byte by applying a bitwise AND operation with `~0x7FL` (bitwise NOT 0x7F) and checking if the result equals zero. If so, the value is cast to a byte and stored in the buffer array. If not, the value undergoes a bitwise AND operation with `0x7F`, is then cast to a byte, and finally bitwise ORed with `0x80`. The resulting byte is stored in the buffer array, and the value is right-shifted by 7 bits (unsigned shift). This procedure repeats until the entire value is encoded.

```scala
// Defining a public method putULong that accepts a single long value as input
public final void putULong(long value) {
    // An infinite loop will continue until a return statement is executed
    while (true) {
        // If the bitwise AND operation between the value and 0x7FL (bitwise NOT operation) equals zero
        if ((value & ~0x7FL) == 0) {
            // When the above condition is satisfied, cast the value to a byte and store it in 
            // the buffer array at the current position
            buffer[position++] = (byte) value;
            // Terminate the method
            return;
        } else {
            // If the above condition is not satisfied, perform a bitwise AND operation on the value with 0x7F,
            // cast the resultant integer to a byte, and perform a bitwise OR operation with 0x80.
            // Store the resulting byte value in the buffer array at the current position
            buffer[position++] = (byte) (((int) value & 0x7F) | 0x80);
            // Shift the value 7 bits to the right
            value >>>= 7;
        }
    }
}
```

## ZigZag Encoding

To efficiently encode signed 64-bit integers using variable-length encoding, ErgoTree employs ZigZag encoding. This method converts signed integers into unsigned integers suitable for efficient VLQ/varint encoding. Without ZigZag encoding, negative values would require sign-extension to 64 bits for standard varint encoding, invariably consuming 10 bytes in the buffer.

Parameter **n** is a signed 64-bit integer. The following Java method demonstrates ZigZag encoding. Note that while the result represents an unsigned value conceptually, Java returns it as a standard signed `long`.

```scala
public static long encodeZigZag64(final long n) {
    // This code shifts the long integer 'n' one bit to the left and performs a bitwise XOR operation 
    // with 'n' shifted arithmetically 63 bits to the right. This arithmetic shift ensures the sign bit 
    // is extended to the leftmost position.
    return (n << 1) ^ (n >> 63);
}
```
