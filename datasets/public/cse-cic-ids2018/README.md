# CSE-CIC-IDS-2018 Intrusion Dataset (AWS Open Data)

## Overview
CSE-CIC-IDS-2018 is an enterprise-scale network intrusion dataset developed jointly by the Communications Security Establishment (CSE) and the Canadian Institute for Cybersecurity (CIC). It features a 500-node network infrastructure (420 workstations + 30 servers across 5 departments, plus 50 attack machines).

- **Source**: Communications Security Establishment & UNB CIC
- **Hosted on**: AWS Open Data Registry (`s3://cse-cic-ids2018/`)
- **Total Records**: ~16 million flow records across 10 days
- **Total Size**: ~400 GB (raw PCAP & system logs), ~6.5 GB (Processed Traffic Data for ML CSVs)

## Attacks Captured
- Brute Force (Web, SSH, FTP)
- Denial of Service (Hulk, GoldenEye, Slowloris, SlowHTTPTest)
- Distributed Denial of Service (LOIC-HTTP, LOIC-UDP, HOIC)
- Web Application Attacks (SQL Injection, Cross-Site Scripting, Brute-Force)
- Infiltration & Lateral Movement (Dropbox Download, Cool Disk)
- Botnet Execution (Ares Botnet)

## Project Role
- **Triage & Investigation Agents**: Training robust deep learning and tree-based ensembles (e.g., LightGBM / XGBoost) on multi-day attack sequences.
- **Enterprise-Scale Baseline**: Provides realistic noise-to-attack ratios for assessing false-positive alert rates in enterprise SOC simulations.

## Download Instructions (AWS CLI - No Account Required)
```bash
# List files in the open bucket:
aws s3 ls --no-sign-request s3://cse-cic-ids2018/

# Download processed CSV files for machine learning:
aws s3 cp --no-sign-request "s3://cse-cic-ids2018/Processed Traffic Data for ML Algorithms/" ./datasets/public/cse-cic-ids2018/ --recursive
```

