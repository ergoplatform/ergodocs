# Sigma 6.0 Documentation

## Overview

**Sigma 6.0** introduces a major upgrade to the **Ergo protocol** with several key features aimed at improving the expressiveness and flexibility of scripts. This release proposes a soft-fork and includes several backward-compatible changes to enhance functionality while ensuring seamless integration with previous versions.

### Key Information

* **Author:** kushti
* **Status:** [Proposed](https://github.com/ergoplatform/eips/blob/027e8cb92881b25a5842d6e0a0278093c39334dd/eip-0050.md)
* **Created:** 25-Nov-2024
* **Implemented in:** Ergo Protocol Reference Client 6.0.0
* **License:** CC0
* **Forking Type:** Soft-fork (requires all miners to update)

## Motivation

Since the **mainnet launch** of Ergo in July 2019, the **ErgoTree** scripting language has remained largely unchanged. The only significant modification since the launch was the shift from **AOT** to **JIT costing** in the **5.0** soft-fork. Over the past five years, developers have identified numerous ways to improve the script language, addressing issues and introducing new features to increase efficiency.

Many of these improvements were initially planned during the testnets of 2018-2019 but were not included in the mainnet until now. The primary goal of this proposal is to address feedback from developers, fix known issues, and expand the protocol’s capabilities with new features such as **serialization**, **unsigned 256-bit integers**, and enhanced **context management**.

## Main Changes

### 1. **UnsignedBigInt Type**

* Introduces a new **UnsignedBigInt** type for cryptographic applications. It supports unsigned 256-bit integers, suitable for modular arithmetic and cryptographic operations.

### 2. **Serialization and Deserialization Support**

* Adds support for **serialization and deserialization** of existing types, including composite types such as collections (e.g., `Coll[Option[Header]]`).
* Methods like `Global.some[T]()`, `Global.none[T]`, and serialization for higher-order functions (e.g., **SFunc**) are now supported.

### 3. **PoW Methods**

* New methods for **proof-of-work** (PoW) validation, including:

  * `header.checkPow`: To check the validity of **Autolykos2** PoW.
  * Methods for checking PoW on custom variants of Autolykos2.

### 4. **Extended Numeric Methods**

* New methods for **numeric types** (`Byte`, `Short`, `Int`, `Long`), such as:

  * `.toBytes`, `.toBits`, `.shiftLeft`, `.shiftRight`, and bitwise operations (`bitwiseOr`, `bitwiseAnd`, `bitwiseXor`).

### 5. **Context Variable Access**

* Support for reading context variables from another input, enhancing the ability to obtain **state transitions** from companion inputs.

### 6. **Collection and Other Enhancements**

* Enhanced **collection methods** including:

  * `.get`, `reverse`, `distinct`, `startsWith`, `endsWith`.
* Additional numeric and data-related improvements to the protocol.

### 7. **Voteable Parameters**

* New **voteable parameter** to allow for the number of sub-blocks per block. This enables future **sub-block implementation**.

### 8. **Parameter Proposal and Soft-Forks**

* This release proposes relaxed **voteable parameters** validation to support future **soft-forks** or even **velvet-forks** to introduce new parameters in the protocol.

## Corresponding Issues and Pull Requests

Several issues and pull requests have been linked to the changes proposed in **Sigma 6.0**:

| **Feature**                                  | **Issue**                                                                     | **Pull Request**                                                                 |
| -------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| PoW Validation for Autolykos2                | [#958](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/958) | [PR #965](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/965)   |
| Conversion from Long-encoded nBits to BigInt | [#675](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/675) | [PR #962](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/962)   |
| UnsignedBigInt Type for cryptography         | [#554](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/554) | [PR #997](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/997)   |
| Serialization of SFunc Type                  | [#847](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/847) | [PR #1020](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/1020) |

For a full list of issues and pull requests, refer to the [SigmaState Issues](https://github.com/ScorexFoundation/sigmastate-interpreter/issues).

## Activation

The changes introduced in **Sigma 6.0** are activated via a **soft-fork**. For compatibility, some **script deserialization validation rules** will be updated to new IDs. These changes ensure that existing clients can validate scripts with old features while skipping those utilizing new features.

Notably, validation rule changes include **#1007**, **#1008**, and **#1011**, which were implemented in [PR #1029](https://github.com/ergoplatform/sigmastate-interpreter/pull/1029).

## Appendix 1: Future Enhancements and Open Issues

Some features and enhancements are still under investigation or planned for future versions:

* **Boolean to Byte conversion** (issue: [#931](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/931)).
* **ErgoTree exponentiation** (issue: [#731](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/731)).
* **Revise semantics of AvlTree.insert** (issue: [#908](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/908)).

## Appendix 2: How to Add a New Method

Sigma 6.0 adds many new methods to various types. Here’s how to add a new method to an existing type:

### Implementation Steps

1. Checkout a new branch based on the `v6.0.0` branch.
2. Identify the appropriate type (e.g., `SBigInt`) to add the method (e.g., `nbits`).
3. Add the method to the type and update the `getMethods()` function in the corresponding class (e.g., `SBigIntMethods`).
4. Implement the method in **SigmaDsl.scala**.
5. Add method evaluation to the **ErgoTreeEvaluator** interface and the **CErgoTreeEvaluator** instantiation.
6. Update reflection-related descriptions in **ReflectionData**.
7. Add pattern matching in **GraphBuilding.scala** to support the method in **ErgoScript**.
8. Update **SigmaDslUnit.scala** / **SigmaDslImpl.scala** for compiler support.

### Testing

1. **Compilation Tests:** Add tests in `TestingInterpreterSpecification`.
2. **Roundtrip Tests:** Add tests in `MethodCallSerializerSpecification`.
3. **Evaluation Tests:** Add evaluation tests, e.g., for the `nbits` method.

For detailed instructions on adding new methods, refer to the relevant code and documentation in the repository.

## Conclusion

Sigma 6.0 is a significant step forward in the development of the **Ergo protocol**, adding numerous enhancements to the scripting language, improving cryptographic support, and enabling more flexible parameter voting. This upgrade provides developers with the tools to build more powerful and efficient applications on the Ergo platform while maintaining compatibility with existing systems through a soft-fork approach.
