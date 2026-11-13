# NSL-KDD Benchmark Dataset

## Overview
NSL-KDD is a refined version of the classic KDD Cup 99 dataset, developed to address duplicate and redundant records that skewed machine learning evaluation. It provides standard train and test splits with varying difficulty levels.

- **Source**: University of New Brunswick (UNB)
- **URL**: https://www.unb.ca/cic/datasets/nsl.html
- **Format**: CSV / ARFF
- **Records**: 125,973 (KDDTrain+) / 22,544 (KDDTest+)
- **Features**: 41 network traffic features + attack label + difficulty level
- **Size**: ~25 MB

## Attack Classes
1. **DoS** (Denial of Service): neptune, smurf, pod, teardrop, back, etc.
2. **Probe** (Surveillance/Probing): ipsweep, portsweep, nmap, satan, etc.
3. **R2L** (Remote to Local): unauthorized access from remote machine (guess_passwd, ftp_write, imap, etc.)
4. **U2R** (User to Root): local privilege escalation (buffer_overflow, loadmodule, rootkit, perl).

## Project Role
- **Prototyping Baseline**: Fast lightweight training of initial triage algorithms.
- **Benchmarking**: Verifying classifier pipelines against historical literature baselines.

## Download Instructions
```bash
python datasets/scripts/download_all.py --dataset nsl-kdd
```
