---
tags:
  - Mining Software
  - Mining
  - GPU
  - AMD
  - Nvidia
  - Intel
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: cyberia-to/erga
    branch: main
    paths:
      - README.md
  - repo: Emryk-LLC/rigel-mining-toolbox
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/cyberia-to/erga
  - https://github.com/Emryk-LLC/rigel-mining-toolbox
---

# Software

| Coins | Miners | nvidia | AMD | Intel | Dev Fee |
|-------|--------|--------|-----|-------|---------|
| ERG | [lolminer](https://github.com/Lolliedieb/lolMiner-releases) | | | | 1.5 % |
| ERG | [Nanominer](https://github.com/nanopool/nanominer/releases) | | | | 2.5 % or [5 %](https://help.nanopool.org/hc/en-us/categories/4896043358365-Ergo-ERG-pool) |
| ERG | [SRB Miner](https://github.com/doktor83/SRBMiner-Multi/releases) | | | | 2 % |
| ERG | [NB Miner](https://github.com/NebuTech/NBMiner) | | | | 2 % |
| ERG | [Team Red Miner](https://github.com/todxx/teamredminer/releases) | | | | 2 % |
| ERG | [Trex Miner](https://github.com/trexminer/T-Rex/releases) | | | | 2 % |
| ERG+KAS | BzMiner | | | | |
| ERG+KAS | Gminer | | | | |
| ERG+KAS | [SRB Miner](https://github.com/doktor83/SRBMiner-Multi/releases) | | | | 2 % |
| ERG | [Rigel](https://github.com/rigelminer/rigel) | | | | Check upstream |

### Source Code Miners

- [AMD miner](https://github.com/mhssamadani/Autolykos2_AMD_Miner)
- [Nvidia miner](https://github.com/mhssamadani/Autolykos2_NV_Miner)

### Other Miners

- [erga](https://github.com/cyberia-to/erga): community Autolykos v2 pool miner for Apple Silicon, with a desktop app and command-line interface. Upstream specifies macOS 14+ and at least 16 GB of unified memory, and notes that builds are not notarized. Back up the recovery phrase if using its generated wallet. Hardware support and accepted pool shares do not guarantee profitability; check the current memory requirement as the mining table grows.
- [CUDA-based GPU miner for Ergo](https://github.com/ergoplatform/Autolykos-GPU-miner) for NVidia cards
- [OpenCL miner for ERGO](https://github.com/mhssamadani/ergoAMDminer) for AMD cards

### Toolboxes and Setup Helpers

- [Rigel Mining Toolbox](https://github.com/Emryk-LLC/rigel-mining-toolbox): Fedora Toolbox environment for mining ERG with Rigel on Aurora-DX Linux and Nvidia GPUs. Review the repository before use because it packages a miner binary and host-specific setup assumptions.
