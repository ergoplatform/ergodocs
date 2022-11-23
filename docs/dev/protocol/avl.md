# AVL Trees

Ergo has native support for AVL trees, an efficient authenticated data structure which allows proving various properties of the data without needing to know the entire set.

This enables
Verification on low-end hardware
Mining on commodity hardware


## Single Operation Proof Size
![Single Operation Proof Size](../../assets/img/avl/single_op_proof.png)

## Multiple Operations Proof Size
For tree N=10^6 and batch B=10^3, compressed proof size is ~400 bytes, plain ~765 bytes.

![](../../assets/img/avl/multiple_op_proof.png)

## Comparison to prior work.

## Validation Time
![](../../assets/img/avl/validation_time.png)