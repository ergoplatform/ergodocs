
# Sigma 6.0 Documentation Summary

Below is a summary of the key information from the **Sigma 6.0 EIP (Ergo Improvement Proposal)**, which details a significant upgrade to the Ergo protocol. The full technical proposal can be found here:
[EIP-0050: Sigma 6.0 on GitHub](https://github.com/ergoplatform/eips/blob/6102112617fff96fe88013858c307c2cf363babf/eip-0050.md)

## Overview

**Sigma 6.0** introduces a major upgrade to the **Ergo protocol** with several key features aimed at improving the expressiveness and flexibility of scripts. This release proposes a soft-fork (much like the SegWit update in Bitcoin, where existing nodes validate scripts with old features and skip scripts with new features) and includes several backward-compatible changes to enhance functionality while ensuring seamless integration with previous versions.

### Key Information from the EIP

* **Author:** kushti
* **Status:** Proposed
* **Created (in EIP):** 25-Nov-2024
* **Implemented in:** Ergo Protocol Reference Client 6.0.0
* **Last edited (EIP):** 27-May-2024 (as per the version linked)
* **License:** CC0
* **Forking Type:** Soft-fork (requires all miners to update)

## Motivation

Since the **mainnet launch** of Ergo in July 2019, the **ErgoTree** scripting language has remained largely unchanged. The only significant modification since the launch was the shift from **AOT** to **JIT costing** in the **5.0** soft-fork, along with minimal changes. Over the past five years, developers have identified numerous ways to improve the expressiveness of scripts and efficiently implement things that currently require non-trivial workarounds. Some issues were also found (though none critical). Additionally, some features planned during the Ergo testnets (2018-19) were not included in the mainnet until now.

The primary goal of this proposal is to address feedback from developers, fix known issues (including the now-resolved semantics of `AvlTree.insert`), and expand the protocol’s capabilities. This includes introducing new features such as **serialization**, **unsigned 256-bit integers**, enhanced **context management**, and relaxing voteable parameter validation for future updates. It also proposes a new voteable blockchain parameter: the **average number of sub-blocks per block**, to support upcoming sub-block implementations.

## Main Changes Proposed

### 1. **UnsignedBigInt Type**

* Introduces a new **UnsignedBigInt** type, an unsigned 256-bit integer tailored for cryptographic applications, supporting modular arithmetic operations and more.

### 2. **Serialization and Deserialization Support**

* Adds support for **serialization and deserialization** in scripts for all existing types, including composite types like `Coll[Option[Header]]`.
* Supports serialization/deserialization for instances of `Option` and `Header` types, allowing them to be stored in registers or context extension variables (with usage notes below).
* Introduces constructors for `Option` instances (`Global.some[T]()`, `Global.none[T]`) and serialization/deserialization for the `SFunc` type (supporting higher-order functions).

### 3. **PoW and nBits Conversion**

* New methods for **proof-of-work** (PoW) validation:
  * `header.checkPow`: To check the validity of an Ergo header's Autolykos2 PoW.
  * Methods for checking PoW for custom variants of the Autolykos2 algorithm on arbitrary messages.
* Support for conversion from nBits-encoded numbers to BigInt and back, enabling efficient difficulty checking for Ergo (and Bitcoin) headers.

### 4. **Extended Numeric Methods**

* Enhanced methods for numeric types (`Byte`, `Short`, `Int`, `Long`), including:
  * `.toBytes`, `.toBits`, `.shiftLeft`, `.shiftRight`, and bitwise operations (`bitwiseOr`, `bitwiseAnd`, `bitwiseXor`).

### 5. **Context Variable Access**

* Allows reading context variables from another input, useful for obtaining state transition information for a companion input.

### 6. **Collection Enhancements**

* More collection methods, such as:
  * `.get` (to optionally get an element if a collection contains it), `reverse`, `startsWith`, `endsWith`.

### 7. **Voteable Parameters and Forks**

* Possibility to propose voting for parameters not known to the protocol client, allowing new voteable parameters to be introduced via soft-forks or even velvet-forks.
* Introduction of a new voteable parameter: the **average number of sub-blocks per block**, for future sub-block implementation. This is achieved by disabling soft-forkable rule #215 via miner voting.

## Corresponding Issues and Pull Requests

Sigma 6.0 incorporates numerous fixes and features detailed in specific issues and pull requests. Key changes highlighted in the EIP include:

| **Selected Feature/Fix** | **Issue(s)** | **Pull Request(s)** |
| :--------------------------------------- | :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PoW Validation for Autolykos2            | [#958](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/958)  | [PR #965](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/965) (custom message), [PR #968](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/968) (Header.checkPow) |
| nBits to BigInt Conversion               | [#675](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/675)  | [PR #962](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/962)                                                                                                  |
| UnsignedBigInt Type                      | [#554](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/554)  | [PR #997](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/997)                                                                                                  |
| Serialization of SFunc Type              | [#847](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/847)  | [PR #1020](https://github.com/ScorexFoundation/sigmastate-interpreter/pull/1020)                                                                                                 |
| Fix Semantics of AvlTree.insert          | [#908](https://github.com/ScorexFoundation/sigmastate-interpreter/issues/908)  | [PR #1038](https://github.com/ergoplatform/sigmastate-interpreter/pull/1038)                                                                                                    |

This is a selection of the developments. For a comprehensive list of all addressed issues, features, fixes (such as for `BigInt` downcasting, `Option.getOrElse` laziness, `ErgoTree` size serialization, `Box.getReg` implementation, collection equality improvements, etc.), and their corresponding pull requests, please refer to the "Corresponding Issues and Pull Requests" section of the official Sigma 6.0 EIP linked above.

## Activation

The changes introduced in **Sigma 6.0** are activated via a **soft-fork**. To ensure backward compatibility, some script deserialization validation rules (specifically #1007, #1008, and #1011) are replaced with identical ones under different IDs. These changes, implemented in [PR #1029](https://github.com/ergoplatform/sigmastate-interpreter/pull/1029), allow existing clients to validate scripts with old features while correctly skipping (or handling) those utilizing new Sigma 6.0 features post-activation.

## Notes on Usage (from EIP)

* Methods added in Sigma 6.0 and the new `UnsignedBigInt` type can only be used within an ErgoTree with version >= 3.
* Values of types `Option[]`, `Header`, and `UnsignedBigInt` cannot be directly put into registers or context extension variables. This is to avoid versioning issues with 5.0 clients. To work around this limitation, you can serialize the typed value to bytes and then call `Global.deserialize` within a script to obtain an instance of these types.
* An example of higher-order lambdas supported since this EIP's implementation can be found [here](https://github.com/ergoplatform/sigmastate-interpreter/blob/b754e143cf38ed86d95698ede744a470dfa053d6/sigmastate/src/test/scala/special/sigma/SigmaDslSpecification.scala#L10040).

## Conclusion

Sigma 6.0 represents a significant evolution for the **Ergo protocol**. It enhances the ErgoTree scripting language with powerful new capabilities, improves cryptographic support, offers more flexible governance through voteable parameters, and addresses various issues. This upgrade equips developers with better tools to build sophisticated and efficient decentralized applications on the Ergo platform, all while maintaining network stability and compatibility through a soft-fork mechanism.
