---
tags:
  - Node
  - Installation
  - Build
  - Source Code
  - SBT
  - Development
  - Release Candidate
---

# Building the Ergo Node from Source

While downloading the pre-compiled JAR from the [Ergo GitHub releases page](https://github.com/ergoplatform/ergo/releases/) is recommended for most users, you might need to build the node from source if you:

*   Need a specific version not available as a pre-compiled JAR (e.g., a specific development commit or Release Candidate).
*   Want to contribute to Ergo node development.
*   Prefer compiling the software yourself.

## Prerequisites

*   **Git:** [Install Git](https://git-scm.com/downloads) if you don't have it.
*   **Java Development Kit (JDK):** A compatible JDK is required (typically JDK 9 or higher). Check the specific version recommendations in the main [Ergo repository README](https://github.com/ergoplatform/ergo#requirements). OpenJDK is recommended.
*   **SBT (Scala Build Tool):** [Install SBT](https://www.scala-sbt.org/download.html).

## Build Steps

1.  **Clone Repository:**
    ```bash
    git clone https://github.com/ergoplatform/ergo.git
    ```
2.  **Navigate to Directory:**
    ```bash
    cd ergo
    ```
3.  **Checkout Specific Version (Optional):**
    *   To build the absolute latest development code (potentially unstable), stay on the default branch (`master`).
    *   To build a specific release or release candidate (RC), check out the corresponding tag using `git checkout <tag_name>`. Find tags on the [releases page](https://github.com/ergoplatform/ergo/releases/).
        ```bash
        # Example for a specific release
        git checkout v5.0.10 
        
        # Example for a Release Candidate
        git checkout v6.0.0-RC2 
        ```
4.  **Handle SNAPSHOT Dependencies (If Applicable):**
    *   Some development versions, especially **Release Candidates**, may depend on unreleased `SNAPSHOT` versions of libraries (like `sigmastate-interpreter`). If the next step fails due to missing SNAPSHOT dependencies, you **must** build and publish these dependencies locally first.
    *   **See the dedicated guide: [Handling SNAPSHOT Dependencies](snapshot-dependencies.md)**
5.  **Compile the JAR:**
    *   Run the SBT `assembly` task. This compiles the code and packages the node and all its dependencies into a single executable JAR file.
        ```bash
        sbt assembly
        ```
    *   The resulting JAR file will be located in the `target/scala-*/` directory within the `ergo` project folder (e.g., `target/scala-2.13/ergo-*.jar`). The exact name will include the version number.
6.  **Locate the JAR:** Find the generated `ergo-*.jar` file in the `target/scala-*/` directory. You can now move this JAR file to your desired node installation folder (e.g., the `ergo` folder created in the [Manual Setup guide](manual.md)).

## Alternative: Docker Build

You can also build and run the node using Docker. See the [Docker setup guide](docker.md) for instructions.

After successfully building the JAR, proceed with [Setting Up Your Node](manual.md#setting-up-your-node) as described in the main manual installation guide.
