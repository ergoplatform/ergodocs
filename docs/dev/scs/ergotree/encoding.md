# ErgoTree Encoding

## VLQ encoding

```scala
// Define a public method putULong that takes a single long value as input
public final void putULong(long value) {
    // Run an infinite loop until it returns
    while (true) {
        // Check if the bitwise and operation between the value and 0x7FL, bitwise not 
        // operation, is equal to zero
        if ((value & ~0x7FL) == 0) {
            // If the above condition is true, cast the value to a byte and put it in 
            // the buffer array at the current position
            buffer[position++] = (byte) value;
            // Return from the method
            return;
        } else {
            // If the above condition is false, bitwise and the value with 0x7F, cast 
            // the resulting integer to a byte and bitwise or it with 0x80. Then put 
            // this byte value in the buffer array at the current position
            buffer[position++] = (byte) (((int) value & 0x7F) | 0x80);
            // Right shift the value by 7 bits
            value >>>= 7;
        }
    }
}

```

## ZigZag encoding

Encode a ZigZag-encoded 64-bit value. ZigZag encodes signed integers into values that can be efficiently encoded with **varint**. (Otherwise, negative values must be sign-extended to 64 bits to be **varint** encoded, thus always taking 10 bytes in the buffer.

Parameter **n** is a signed 64-bit integer. This Java method returns an unsigned 64-bit integer stored in a signed int because Java has no explicit unsigned support.

```scala
public static long encodeZigZag64(final long n) {
    // Shifts the long integer n one bit to the left and
    // performs a bitwise XOR operation with n shifted arithmetically 63 bits to the right.
    // The arithmetic shift ensures that the sign bit is extended to the leftmost position.
    return (n << 1) ^ (n >> 63);
}
```


