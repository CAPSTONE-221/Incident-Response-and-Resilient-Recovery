# EMBER: Elastic Malware Benchmark for Empowering Researchers

## Overview
EMBER 2018 is an open dataset containing features extracted from 1.1 million Windows Portable Executable (PE) files. It serves as an academic benchmark for static machine learning malware classification without distributing malicious binaries.

- **Source**: Elastic / Endgame
- **Repository**: https://github.com/elastic/ember
- **Direct Download**: `https://ember.elastic.co/ember_dataset_2018_2.tar.bz2` (~4 GB)
- **Format**: JSON-lines feature vectors
- **Samples**: 1,100,000 PEs (600,000 training, 200,000 test, 300,000 unlabeled)
- **Features**: 2,351 extracted static features per executable

## Feature Groups
1. General file information (size, virtual size, entropy, debug flags)
2. Header information (machine type, timestamp, subsystem)
3. Section characteristics (entropy, physical/virtual sizes)
4. Imported and exported functions (DLL linkage analysis)
5. Byte histograms & byte-entropy histograms

## Project Role: File Integrity & Backup Scanning
- **Trust Agent**: Evaluates the Threat-Free Confidence ($T$) of executables, DLLs, and scripts located inside backup restore points.
- **Verification of Stored Binaries**: Rapid static feature inference to flag poisoned binaries inside system images before approval.

## Download Instructions
```bash
python datasets/scripts/download_all.py --dataset ember
```
