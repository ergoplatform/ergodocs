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
  - repo: Emryk-LLC/rigel-mining-toolbox
    branch: main
    paths:
      - README.md
source_of_truth:
  - https://github.com/Emryk-LLC/rigel-mining-toolbox
---

# Software

| Coins | Miners | nvidia | AMD | Intel | Dev Fee |
|-------|--------|--------|-----|-------|---------|
| ERG   | [lolminer](https://github.com/Lolliedieb/lolMiner-releases) | ✓ | ✓ | ✓ | 1.5 % |
| ERG   | [Nanominer](https://github.com/nanopool/nanominer/releases) | ✓ | ✓ |  | 2.5 % or [5 %](https://help.nanopool.org/article/218-pool-information) |
| ERG   | [SRB Miner](https://github.com/doktor83/SRBMiner-Multi/releases) | ✓ | ✓ |  | 2 % |
| ERG   | [NB Miner](https://github.com/NebuTech/NBMiner) | ✓ |  |  | 2 % |
| ERG   | [Team Red Miner](https://github.com/todxx/teamredminer/releases) |  | ✓ |  | 2 % |
| ERG   | [Trex Miner](https://github.com/trexminer/T-Rex/releases) |  | ✓ |  | 2 % |
| ERG+KAS | BzMiner | ✓ |  |  |  |
| ERG+KAS | Gminer | ✓ |  |  |  |
| ERG+KAS | [SRB Miner](https://github.com/doktor83/SRBMiner-Multi/releases) |  | ✓ |  | 2 % |
| ERG | [Rigel](https://github.com/rigelminer/rigel) | ✓ |  |  | Check upstream |

### Source Code Miners

- [AMD miner](https://github.com/mhssamadani/Autolykos2_AMD_Miner)
- [Nvidia miner](https://github.com/mhssamadani/Autolykos2_NV_Miner)

### Other Miners

- [CUDA-based GPU miner for Ergo](https://github.com/ergoplatform/Autolykos-GPU-miner) for NVidia cards
- [OpenCL miner for ERGO](https://github.com/mhssamadani/ergoAMDminer) for AMD cards

### Toolboxes and Setup Helpers

- [Rigel Mining Toolbox](https://github.com/Emryk-LLC/rigel-mining-toolbox): Fedora Toolbox environment for mining ERG with Rigel on Aurora-DX Linux and Nvidia GPUs. Review the repository before use because it packages a miner binary and host-specific setup assumptions.
