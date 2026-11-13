# LANL Comprehensive Multi-Source Cyber-Security Events Dataset

## Overview
Released by the Advanced Research in Cyber Systems group at Los Alamos National Laboratory (LANL), this dataset covers 58 consecutive days of enterprise activity containing 1.64 billion events across 17,684 hosts and 12,425 users.

- **Source**: Los Alamos National Laboratory (LANL)
- **URL**: https://csr.lanl.gov/data/cyber1/
- **Format**: Tab-separated text files (compressed `.txt.gz`)
- **Total Size**: ~12 GB compressed / >100 GB uncompressed

## Tables Included
1. `auth.txt.gz`: Windows authentication records (Logon, Logoff, Kerberos, NTLM).
2. `proc.txt.gz`: Process start and stop events on endpoints.
3. `dns.txt.gz`: Internal DNS lookup requests and resolutions.
4. `flows.txt.gz`: Router NetFlow connection summaries.
5. `redteam.txt.gz`: Verified adversary red-team events (compromised user-computer pairs with timestamps).

## Project Role: Multi-Source Telemetry Correlation
- **Triage & Investigation Agents**: Cross-modal correlation testing (linking authentication anomalies to process launches and network connections).
- **Compromise Window Estimation**: Calculating temporal validity ($V$) in RTS by tracking the red-team compromise timestamp relative to backup schedules.

## Download Instructions
Visit the LANL CSR portal at https://csr.lanl.gov/data/cyber1/, agree to terms, and download selected tables into this directory.

