# DARPA Operationally Transparent Cyber (OpTC) Dataset

## Overview
The DARPA OpTC dataset is an enterprise-scale endpoint and network telemetry dataset collected during the DARPA Transparent Computing program. It spans multi-day APT operations injected across more than 500 Windows 10 endpoints.

- **Source**: DARPA / Five Directions Inc.
- **Repository**: https://github.com/FiveDirections/OpTC-data
- **Format**: JSON (Common Data Model - CDM schema)
- **Size**: ~1 TB uncompressed / multi-GB compressed subsets
- **Hosts**: 500+ enterprise Windows 10 workstations + servers

## Telemetry Streams
- Process operations: creation, termination, memory injection, DLL loading
- File operations: open, read, write, rename, attribute modification, delete
- Network connections: socket creation, connect, accept, send, receive
- Registry activity: key creation, value write, deletion

## Project Role: Core Architectural Reference
1. **Investigation Agent**: Provenance graph reconstruction — tracing back an alert to its initial intrusion root cause.
2. **Blast Radius Analysis**: Identifying all endpoints, accounts, and services touched by the adversary.
3. **Literature Grounding**: Primary APT evaluation dataset utilized by CIPHER-A (Kizhakel & Pande, Discover Artificial Intelligence 2026), one of Team 221's foundational papers.

## Access & Cloning Instructions
```bash
python datasets/scripts/download_all.py --dataset darpa-optc
# Or clone telemetry schema and tools:
git clone --depth 1 https://github.com/FiveDirections/OpTC-data.git datasets/public/darpa-optc/
```
