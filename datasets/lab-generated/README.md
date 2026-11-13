# Lab-Generated Datasets: Specifications & Generation Guide

## Why Lab-Generated Datasets Are Necessary
While public datasets (such as CICIDS, UNSW-NB15, and DARPA OpTC) provide exceptional network flows and host intrusion telemetry, **none of them provide recovery-specific evidence**. Specifically, no public benchmark captures:
1. **Candidate recovery points with varying compromise timestamps**
2. **Backup snapshot integrity metrics ($I$), temporal validity ($V$), threat confidence ($T$), provenance records ($F$), and reinfection risk ($R$)**
3. **Contaminated vs. clean backup states**
4. **Service dependency graphs with cascading restoration sequences**

Therefore, our team will generate targeted datasets using virtual machines (VMs) running on our laptops.

---

## 1. Laptop VM Lab Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                          LOCAL LAB NETWORK (Host-Only / NAT)           │
│                                                                        │
│   ┌────────────────────────┐             ┌─────────────────────────┐  │
│   │   Attacker VM (Kali)   │             │   SIEM / Telemetry VM   │  │
│   │   IP: 192.168.56.10    │             │   (Elasticsearch/Kibana)│  │
│   │   - CALDERA C2 Server  │             │   IP: 192.168.56.20     │  │
│   │   - Atomic Red Team    │             │   - Logstash / Fleet    │  │
│   │   - Attack scripts     │             │   - Centralized Storage │  │
│   └───────────┬────────────┘             └────────────▲────────────┘  │
│               │ (Simulated attack traffic)            │ (Telemetry)   │
│               ▼                                       │               │
│   ┌────────────────────────┐             ┌────────────┴────────────┐  │
│   │  Victim 1: App Server  │             │  Victim 2: DB / File    │  │
│   │  (Ubuntu 22.04 LTS)    │             │  (Windows 10/11 VM)     │  │
│   │  IP: 192.168.56.30     │             │  IP: 192.168.56.40      │  │
│   │  - Web App, APIs       │             │  - Sysmon + Winlogbeat  │  │
│   │  - Zeek / Auditd       │             │  - Backup Target Client │  │
│   └───────────┬────────────┘             └────────────┬────────────┘  │
│               │ (Scheduled Snapshots)                 │               │
│               └───────────────────┬───────────────────┘               │
│                                   ▼                                   │
│                     ┌───────────────────────────┐                     │
│                     │   Backup Server (Isolated)│                     │
│                     │   IP: 192.168.56.50       │                     │
│                     │   - ZFS/Btrfs snapshots   │                     │
│                     │   - Cryptographic hashes  │                     │
│                     │   - Provenance chain logs │                     │
│                     └───────────────────────────┘                     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. VM Requirements & Allocation per Laptop

Each team member can host 1–2 lightweight VMs using **VirtualBox** or **VMware Workstation Player**:
- **Member 1 (Adarsh)**: Windows 10 Endpoint VM (Sysmon, File Server, Ransomware target)
- **Member 2 (Dhruva)**: SIEM & Ingestion VM (Elasticsearch/Logstash/Kibana or lightweight OpenSearch)
- **Member 3 (Abhirama)**: Attacker VM (Kali Linux with MITRE CALDERA / Atomic Red Team runner)
- **Member 4**: Linux Application Server & Backup Storage Target (Ubuntu Server with Docker & ZFS/rsync)

---

## 3. Subdirectories & Schemas

| Directory | Purpose | Artifacts Produced |
|-----------|---------|-------------------|
| `ransomware-simulation/` | Controlled ransomware execution & file mutation | Sysmon Event ID 11 (FileCreate), Event 1 (ProcessCreate), entropy logs |
| `backup-trust-validation/` | Recovery Point dataset with ground truth RTS | CSV table of recovery points with $I, V, T, F, R$ attributes and safety labels |
| `multi-stage-attack/` | End-to-end APT kill-chain across multiple hosts | Incident graphs, service dependency DAGs, blast radius metrics |

---

## 4. Synthetic Evaluation Data
To enable agent training and mathematical formula validation immediately (before all VM runs are finalized), we also provide a benchmark generator script:
```bash
python datasets/lab-generated/backup-trust-validation/generate_synthetic_rts_eval.py
```
This produces 500 validated candidate recovery points modeling clean, poisoned, and uncertain backup scenarios.

