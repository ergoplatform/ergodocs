---
tags:
  - Android
  - Node
  - Mobile
  - Termux
  - Installation
  - Guide
  - RocksDB
  - UTXO Mode
  - proot
  - Arch Linux
  - glibc
---

# Android Node: Arch Linux via proot (RocksDB/UTXO Mode)

This guide details the more advanced method for running an Ergo node on Android using an Arch Linux environment within Termux via `proot`. This method is necessary if you need to run the node with `stateType="utxo"` (which uses RocksDB for state storage) or if you encounter database issues (e.g., LevelDB failures) with the direct Termux setup.

**Why is this needed?**

*   The Ergo node uses database engines (LevelDB by default, RocksDB as an option, especially for `stateType="utxo"`) to store blockchain state.
*   The Java bindings for RocksDB often rely on the standard GNU C Library (`glibc`).
*   Android/Termux typically use a different C library (`musl libc` via Bionic).
*   Running the RocksDB-enabled node JAR directly in Termux can lead to incompatibility errors.
*   `proot-distro` allows running a Linux distribution (like Arch Linux, which uses `glibc`) within Termux, providing the necessary environment for RocksDB.

**Disclaimer:** This is a more complex setup than the [direct Termux method](termux-digest.md) and adds overhead. It's primarily required for specific use cases needing RocksDB/UTXO mode. For most mobile users, the direct Termux setup with `stateType="digest"` is recommended.

**Prerequisites:**

*   Android device meeting the [requirements](node-android.md#device-requirements) (Note: UTXO mode requires significantly more storage than digest mode).
*   Termux installed from F-Droid.

**Steps:**

1.  **Install `proot-distro` in Termux:**
    *   Open Termux and run:
        ```bash
        pkg update && pkg upgrade -y
        pkg install proot-distro -y
        ```
2.  **Install Arch Linux via `proot-distro`:**
    ```bash
    proot-distro install archlinux
    ```
    *   This will download the Arch Linux root filesystem.
3.  **Login to Arch Linux Environment:**
    *   Each time you want to run the node using this method, you first need to log into the Arch environment:
        ```bash
        proot-distro login archlinux
        ```
    *   Your terminal prompt should change, indicating you are now inside Arch Linux within Termux.
4.  **Inside Arch Linux: Install Dependencies (First Time Only):**
    *   Update package lists:
        ```bash
        pacman -Syu --noconfirm
        ```
    *   Install Java (OpenJDK 17 recommended), `wget`, and `nano`:
        ```bash
        pacman -S jdk-openjdk wget nano --noconfirm
        ```
5.  **Inside Arch Linux: Download RocksDB Ergo Node JAR:**
    *   You **must** download the JAR variant specifically built with RocksDB support. Find the correct `.jar` file (often named `ergo-<version>-rocksdb.jar`) on the [Ergo Releases](https://github.com/ergoplatform/ergo/releases) page.
    *   Get the download URL for the specific RocksDB JAR you need.
    *   Use `wget` to download it *within the Arch environment*:
        ```bash
        # Example (replace URL with the actual RocksDB JAR URL):
        ROCKSDB_JAR_URL="https://github.com/ergoplatform/ergo/releases/download/vX.Y.Z/ergo-X.Y.Z-rocksdb.jar"
        echo "Downloading RocksDB Ergo node JAR from: $ROCKSDB_JAR_URL"
        wget -q --show-progress "$ROCKSDB_JAR_URL" -O ergo-rocksdb.jar
        ```
6.  **Inside Arch Linux: Create Configuration File (`ergo.conf`):**
    *   Create the file using `nano`:
        ```bash
        nano ergo.conf
        ```
    *   Paste a configuration suitable for `stateType="utxo"` with pruning (adjust `blocksToKeep` based on your storage capacity):
        ```conf
        ergo {
          node {
            stateType = "utxo" // Use UTXO state with RocksDB
            // Keep ~1 week of blocks (~3-5GB?), adjust based on storage
            // WARNING: -1 (archival) is likely impractical on mobile storage
            blocksToKeep = 10080 
            mining = false

            # Enable faster bootstrapping (both recommended)
            nipopow.nipopowBootstrap = true
            utxoBootstrap = true
          }
        }

        scorex {
          restApi {
            apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf" // Example, change this
          }
          network {
            # Optional: Add known reliable peers
            # knownPeers = ["ip:port", "ip:port"]
          }
        }
        ```
    *   Save (`CTRL+O`, `Enter`) and Exit (`CTRL+X`).
7.  **Inside Arch Linux: Launch the Node:**
    *   Run the RocksDB JAR, allocating sufficient memory (UTXO mode generally needs more than digest mode):
        ```bash
        java -Xmx2G -jar ergo-rocksdb.jar --mainnet -c ergo.conf
        ```
    *   *(Adjust `-Xmx2G` based on your device's available RAM. You might need more or less).*
8.  **Monitor Synchronization:**
    *   Open a web browser on your Android device and go to `http://127.0.0.1:9053/panel`.
    *   Synchronization, especially the initial UTXO snapshot download, will take time and consume significant storage.

**Exiting:** To stop the node, press `CTRL + C` in the Arch Linux terminal. To exit the Arch Linux environment back to the main Termux shell, type `exit`.

Refer back to the [main Android guide](node-android.md) for general tips, disk space clarification, and troubleshooting. Remember this method adds complexity and resource overhead compared to the direct Termux approach.
