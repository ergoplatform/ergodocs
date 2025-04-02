---
tags:
  - mobile
  - android
  - ios
  - build
  - scala
  - jvm
  - jdk
  - sdk
  - r8
  - desugaring
  - constraints
  - troubleshooting
---

# Mobile Build Constraints for Scala/JVM Components

Developing mobile applications (Android/iOS) that incorporate Scala or other JVM-based libraries (like AppKit or core Ergo components) involves navigating a complex set of build constraints and potential compatibility issues. This page outlines some key areas developers should be aware of, based on community discussions.

## Key Constraint Areas

### 1. Scala Version Compatibility

*   **Scala 2 vs. Scala 3:** Ergo's core libraries have migrated to Scala 3. Ensure your build tools (SBT, Gradle) and dependencies are compatible with the Scala version used by the Ergo libraries you depend on.
*   **Binary Compatibility:** Be mindful of potential binary incompatibilities between different Scala minor versions, especially across major releases (2.x vs. 3.x).

### 2. JDK Version Requirements

*   **Compilation:** The JDK version used to compile your Scala code and dependencies matters. Ergo components often require JDK 11 or higher.
*   **Android Compatibility:** Android projects have specific JDK compatibility requirements that might differ from your desktop development environment. Ensure the JDK used by your Android build process (e.g., via Android Studio's settings or Gradle configuration) is compatible with both Android and the required JDK level for your Scala dependencies.

### 3. Android SDK Levels & API Compatibility

*   **`minSdkVersion`:** The minimum Android API level your app targets can restrict which Java APIs and language features are available directly.
*   **Desugaring:** To use newer Java language features (from JDK 8+) on older Android versions, Android's build process uses "desugaring". This transforms bytecode to be compatible with older Android runtimes. Desugaring needs to be enabled and configured correctly in your `build.gradle` file.
    *   **Reference:** [Android Java 8+ API Desugaring](https://developer.android.com/studio/write/java8-support#library-desugaring)
*   **Scala Standard Library:** The Scala standard library itself might use Java APIs that require desugaring for compatibility with your `minSdkVersion`.

### 4. Code Shrinking & Obfuscation (R8/ProGuard)

*   **R8:** Android's default code shrinker and obfuscator (replacing ProGuard). R8 removes unused code and renames classes/methods to reduce app size.
*   **Configuration (`proguard-rules.pro`):** R8 requires careful configuration, especially when dealing with reflection, serialization, or JNI (Java Native Interface) used by Scala or dependent libraries. You often need to add `-keep` rules in `proguard-rules.pro` to prevent R8 from removing or renaming essential classes or methods that are accessed indirectly (e.g., via reflection). Incorrect configuration can lead to runtime crashes (`ClassNotFoundException`, `NoSuchMethodError`).
*   **Scala Reflection:** Scala's reflection capabilities can be particularly sensitive to R8 optimization. Extensive `-keep` rules might be necessary if your code or dependencies rely heavily on reflection.

### 5. iOS Build Limitations (JVM on iOS)

*   **No Native JVM:** iOS does not have a native Java Virtual Machine. Running Scala/JVM code directly on iOS typically requires cross-compilation or specific frameworks:
    *   **Scala Native:** Compiles Scala code to native binaries using LLVM. Compatibility with all JVM libraries is not guaranteed.
    *   **Multi-OS Engine (Deprecated):** Previously allowed running JVM bytecode on iOS, but is no longer actively maintained.
    *   **Gluon SubstrateVM (GraalVM):** Can compile Java/Scala applications into native iOS binaries.
    *   **Kotlin Multiplatform Mobile (KMM):** While focused on Kotlin, it provides mechanisms for sharing code (potentially including Scala via JVM interop) between Android and iOS, often compiling to native code for iOS.
*   **Sigma-Rust Bindings:** For core Ergo cryptographic operations, using the [iOS bindings provided by `sigma-rust`](sigma-rust.md) is often the most practical approach for iOS development, avoiding the complexities of running a full JVM environment.

## General Recommendations & Resources

*   **Start Simple:** Begin with a minimal setup and gradually add dependencies to isolate compatibility issues.
*   **Check Dependency Requirements:** Carefully review the documentation for the specific Ergo libraries (AppKit, sigma-rust bindings, etc.) regarding their required Scala, JDK, and Android SDK versions.
*   **Consult Build Logs:** Pay close attention to warnings and errors during the Gradle build process, especially those related to desugaring, R8, or dependency conflicts.
*   **Scala on Android Tutorial:** While potentially slightly dated depending on the specific library versions you use, the official Scala documentation provides background: [Scala on Android Tutorial](https://docs.scala-lang.org/tutorials/scala-on-android.html)
*   **Community Support:** Mobile development with Scala/JVM can be complex. Seek help in Ergo developer community channels, providing details about your build configuration (Gradle files, SBT versions, library versions) and any error messages encountered.

Navigating these constraints requires careful configuration and testing. Understanding the interplay between Scala versions, JDK features, Android build tools (Gradle, R8, Desugaring), and platform limitations (especially for iOS) is key to successfully building mobile Ergo applications using JVM-based components.
