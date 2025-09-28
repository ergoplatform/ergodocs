---
tags:
  - Android
  - Node
  - Mobile
  - Termux
  - Installation
  - Guide
  - RocksDB
  - Digest Mode
  - proot
---
# Running an Ergo Node on Android

Running an Ergo node directly on an Android device is possible and allows users without desktop access to participate more fully in the network, potentially using their own node for mobile wallets or dApps.

This guide provides an overview of the methods available using the [Termux](https://termux.dev/) terminal emulator.

## Overview of Methods

There are two primary approaches, depending on your needs and technical comfort level:

1.  **[Direct Termux Setup (Digest Mode)](termux-digest.md):**
    *   **Recommended for most users.**
    *   Runs the node directly within Termux.
    *   Best suited for the resource-efficient `stateType="digest"` mode.
    *   Simpler setup process.

2.  **[Arch Linux via proot (RocksDB/UTXO Mode)](proot-rocksdb.md):**
    *   **Advanced method.**
    *   Required if you need to run `stateType="utxo"` (which uses RocksDB) or encounter specific database compatibility issues (e.g., LevelDB failures on `aarch64`).
    *   Involves running an Arch Linux environment within Termux to provide `glibc` compatibility for RocksDB.
    *   More complex setup and higher resource usage.

/// details | One-Click App Attempt
    {type: tip, open: false}
[ErgoNodeAndroid](https://github.com/rustinmyeye/ErgoNodeAndroid) is a community project attempting a one-click Ergo node app for Android, based on Termux scripts. It typically sets up a stateless/digest node. You may explore this as an alternative to manual setup.
///

## Device Requirements

Meeting these requirements is crucial for a stable experience:

*   **OS:** Android version 7.0 or higher.
*   **Storage:**
    *   **Digest Mode:** ~5-10GB free space recommended initially. Actual usage after sync might settle around ~3GB, but bootstrapping can require more temporarily.
    *   **UTXO Mode (via proot):** Significantly more, potentially 30GB+ depending on pruning (`blocksToKeep`). Archival mode (`blocksToKeep=-1`) is likely impractical on mobile storage.
*   **RAM:** Minimum 1-2GB available *specifically for Termux/Java*. More RAM (e.g., 4GB+) provides a smoother experience, especially during sync. You will need to use the `-Xmx` Java flag to allocate memory appropriately.

## General Tips and Tricks (Apply to Both Methods)

*   **Keyboard:** Consider installing a different keyboard app (like Hacker's Keyboard from F-Droid) if your default keyboard doesn't work well in Termux.
*   **Background Operation:** Install `tmux` (`pkg install tmux` in Termux, or `pacman -S tmux` in the Arch environment) to run the node in a background session that persists even if you close the Termux app window.
*   **Port Forwarding:** If you want your node to be reachable by external peers, configure port forwarding for TCP port 9030 on your home router to your Android device's local IP address.
*   **Wallet Connection:** If using the Ergo Wallet App on the same device, you can often change its node setting to `http://127.0.0.1:9053` to connect to your local node.
*   **Troubleshooting:** If the node fails to start, check common issues:
    *   Correct Java version installed and selected (`java --version`).
    *   Sufficient memory allocated via `-Xmx`. Try adjusting the value.
    *   Correct Ergo node JAR file used (Standard vs. RocksDB variant, depending on the method and `stateType`).
    *   Syntax errors in your `ergo.conf` file.
    *   Insufficient free storage space on the device.
    *   Permissions issues within Termux or the proot environment.

## Disk Space Clarification

*   **Digest Mode:** Typically settles around **~3GB** after sync with bootstrapping and moderate `blocksToKeep`.
*   **UTXO Mode:** Requires significantly more storage (tens of GBs) due to storing the UTXO set state.

Choose the method that best suits your needs and technical capabilities by following the links above for detailed steps.
