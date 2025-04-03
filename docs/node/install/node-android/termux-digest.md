---
tags:
  - Android
  - Node
  - Mobile
  - Termux
  - Installation
  - Guide
  - Digest Mode
---

# Android Node: Direct Termux Setup (Digest Mode)

This guide details the recommended method for running an Ergo node on Android using Termux directly. This approach is best suited for the resource-efficient `stateType="digest"` mode.

**Prerequisites:**

*   Android device meeting the [requirements](node-android.md#device-requirements).
*   Termux installed from F-Droid (see [main Android guide](node-android.md#direct-termux-setup-digest-mode)).

**Steps:**

1.  **Update Termux Packages:**
    *   Open Termux and run:
        ```bash
        pkg update && pkg upgrade -y
        ```
    *   Answer default prompts if asked.
2.  **Install Dependencies:**
    *   Install Java (OpenJDK 17 recommended) and `wget`:
        ```bash
        pkg install openjdk-17 wget -y
        ```
3.  **Download Ergo Node JAR:**
    *   For `stateType="digest"`, the standard Ergo node JAR (without `-rocksdb` suffix) is usually sufficient.
    *   Use `wget` to download the latest release:
        ```bash
        # Get the URL for the latest standard JAR
        LATEST_JAR_URL=$(wget -qO- "https://api.github.com/repos/ergoplatform/ergo/releases/latest" | grep -o 'https://github.com/ergoplatform/ergo/releases/download/.*ergo-[0-9.]*\.jar' | head -n 1)

        # Download it
        echo "Downloading latest Ergo node JAR from: $LATEST_JAR_URL"
        wget -q --show-progress "$LATEST_JAR_URL" -O ergo.jar
        ```
    *   *(Verify the downloaded URL or manually find the correct URL on the [Ergo Releases](https://github.com/ergoplatform/ergo/releases) page if the script fails).*
4.  **Create Configuration File (`ergo.conf`):**
    *   Create the file using `nano`:
        ```bash
        nano ergo.conf
        ```
    *   Paste the following configuration, suitable for mobile digest mode:
        ```conf
        ergo {
          node {
            stateType = "digest"
            blocksToKeep = 1440 // Keep ~1 day of full blocks (~500MB-1GB), adjust if needed
            mining = false

            # Enable faster bootstrapping (both recommended for flexibility)
            nipopow.nipopowBootstrap = true
            utxoBootstrap = true

            # Optional: Adjust NiPoPoW parameters if using nipopowBootstrap
            # nipopow.p2pNipopows = 2
          }
        }

        scorex {
          restApi {
            # Set your desired API key hash (generate one if needed)
            # Example hash for password "hello":
            apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
          }
          network {
            # Optional: Add known reliable peers if discovery is slow
            # knownPeers = ["ip:port", "ip:port"]
          }
        }
        ```
    *   **Explanation:**
        *   `stateType = "digest"`: Enables the lightweight digest mode.
        *   `blocksToKeep = 1440`: Keeps roughly the last day's worth of full blocks. Adjust based on storage/needs. Lower values save space but limit historical data access via API.
        *   `nipopow.nipopowBootstrap = true` & `utxoBootstrap = true`: Enable fast synchronization methods. The node will use the best available option from peers.
    *   Save the file: Press `CTRL + O`, then `Enter`.
    *   Exit nano: Press `CTRL + X`.
5.  **Launch the Node:**
    *   Run the node, allocating memory with `-Xmx`. Start with 1GB or 1.5GB:
        ```bash
        java -Xmx1536M -jar ergo.jar --mainnet -c ergo.conf
        ```
    *   *(Adjust `-Xmx1536M` (1.5GB) based on your device. If it crashes, try `-Xmx1G` or increase if you have more RAM available, e.g., `-Xmx2G`).*
6.  **Monitor Synchronization:**
    *   Open a web browser on your Android device and go to `http://127.0.0.1:9053/panel`.
    *   Initial sync (especially the UTXO snapshot download if `utxoBootstrap` is used) can take time and may not show detailed progress in logs. Monitor network activity or storage usage. Once synced, the panel will update.

Refer back to the [main Android guide](node-android.md#direct-termux-setup-digest-mode) for general tips, disk space clarification, and troubleshooting.
