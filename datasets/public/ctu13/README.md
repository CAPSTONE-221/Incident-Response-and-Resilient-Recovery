# CTU-13 Botnet Network Dataset

## Overview
Captured by the Stratosphere Laboratory at Czech Technical University in Prague, CTU-13 consists of 13 distinct scenarios of real botnet malware executed in a controlled lab network alongside legitimate user background traffic.

- **Source**: Stratosphere IPS / Czech Technical University
- **URL**: https://www.stratosphereips.org/datasets-ctu13
- **Format**: Binetflow (Argus bidirectional flow files) and PCAP
- **Size**: ~2 GB (flows), ~60 GB (PCAP)
- **Scenarios**: 13 captured botnet attacks (Neris, Rbot, Virut, Menti, Sogou, Murlo, NSIS)

## Project Role
- **Investigation Agent**: Identifying Command-and-Control (C2) communication channels and periodic beaconing behavior.
- **Response Planner**: Designing automated network quarantine rules (e.g., DNS sinkholing vs. firewall IP block) to neutralize botnet communication.
- **Literature Baseline**: Directly referenced in the CIPHER-A research paper (Discover AI 2026) for evaluating network blocking side-effects.

## Download Instructions
```bash
python datasets/scripts/download_all.py --dataset ctu13
```
