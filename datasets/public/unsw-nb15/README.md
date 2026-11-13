# UNSW-NB15 Intrusion Detection Dataset

## Overview
Created by the Cyber Range Lab of the Australian Centre for Cyber Security (ACCS) at UNSW Canberra using the IXIA PerfectStorm tool. It models modern realistic synthetic attack behaviors and contemporary benign traffic.

- **Source**: ACCS, UNSW Canberra
- **URL**: https://research.unsw.edu.au/projects/unsw-nb15-dataset
- **Format**: CSV (49 features extracted via Argus/Bro-IDS) and PCAP
- **Total Records**: 2,540,044 records (Benchmark subset: 175,341 train / 82,332 test)
- **Size**: ~2 GB CSV

## Attack Categories (9 Families)
1. **Fuzzers**: Discovering security loopholes by inputting massive random data.
2. **Analysis**: Port scans, spam, and HTML file intrusions.
3. **Backdoors**: Stealth administrative access channels.
4. **DoS**: Denying legitimate users access to services.
5. **Exploits**: Known vulnerability exploitation.
6. **Generic**: Cryptographic collision and generic algorithmic attacks.
7. **Reconnaissance**: Network topology mapping and host discovery.
8. **Shellcode**: Small executable code used as payload in software exploitation.
9. **Worms**: Self-replicating malware over network services.

## Project Role
- **Triage Agent**: Multi-class classification to categorize attack families and calculate attack severity index.
- **Investigation Agent**: Correlating protocol states, TTL variations, and transaction flows with MITRE ATT&CK techniques.

## Download Instructions
```bash
python datasets/scripts/download_all.py --dataset unsw-nb15
```
