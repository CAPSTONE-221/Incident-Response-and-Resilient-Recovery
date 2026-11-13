# Splunk Boss of the SOC (BOTS) Datasets

## Overview
Splunk Boss of the SOC (BOTS) datasets are realistic SIEM datasets created for CTF competitions. They simulate modern enterprise infrastructures featuring hybrid on-premise and multi-cloud environments (AWS, Azure) under active attack.

- **Source**: Splunk Inc.
- **Versions**: BOTSv1, BOTSv2, BOTSv3
- **Repository**: https://github.com/splunk/botsv3
- **Direct S3 Download**: `https://botsdataset.s3.amazonaws.com/botsv3/botsv3_data_set.tgz` (~320 MB)
- **Format**: Pre-indexed Splunk Application bundles (`.tgz`), JSON, CSV exports

## Data Sources Inside BOTS
- Windows Event Logs (Security, System, Application)
- Sysmon telemetry (Process, Network, Registry, ImageLoad)
- Suricata / Snort IDS alerts
- Apache / IIS Web server access logs
- CloudTrail & VPC Flow Logs (AWS)
- Endpoint detection data (Osquery)

## Project Role: SIEM Ingestion & Triage
- **Triage Agent**: Parsing raw SIEM events, eliminating false positives, and prioritizing high-fidelity incidents.
- **Realistic SOC Alert Streams**: Testing agent performance against the exact alert format security operation centers encounter in production.

## Download Instructions
```bash
python datasets/scripts/download_all.py --dataset splunk-bots
```
