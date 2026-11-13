# Cybersecurity Datasets for Trust-Aware Agentic AI

## Project: Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery (Team 221)

This directory contains the cybersecurity datasets collected, documented, and organized for developing and testing the proposed AI-driven Cyber Threat Intelligence and Automated Incident Response system.

> [!IMPORTANT]
> Large dataset files (CSVs, PCAPs, JSON logs) are **NOT** stored in this repository. This directory contains download scripts, documentation, and metadata only. Actual datasets should be downloaded locally using the provided scripts.

---

## Directory Structure

```
datasets/
├── README.md                          # This file — master documentation
├── DATASET_CATALOG.md                 # Detailed catalog of all datasets
├── public/                            # Download scripts & metadata for public datasets
│   ├── download_all.py                # Master download script
│   ├── cicids2017/                    # CIC-IDS-2017 dataset
│   │   └── README.md
│   ├── cicids2018/                    # CSE-CIC-IDS-2018 dataset
│   │   └── README.md
│   ├── unsw-nb15/                     # UNSW-NB15 dataset
│   │   └── README.md
│   ├── nsl-kdd/                       # NSL-KDD dataset
│   │   └── README.md
│   ├── ctu13/                         # CTU-13 Botnet dataset
│   │   └── README.md
│   ├── darpa-optc/                    # DARPA OpTC APT dataset
│   │   └── README.md
│   ├── lanl-cyber/                    # LANL Security Events dataset
│   │   └── README.md
│   ├── cic-malmem-2022/               # CIC-MalMem-2022 Malware Memory dataset
│   │   └── README.md
│   ├── ember/                         # EMBER Malware dataset
│   │   └── README.md
│   ├── mitre-attack-stix/             # MITRE ATT&CK STIX data
│   │   └── README.md
│   ├── otrf-security-datasets/        # OTRF/Mordor Security Datasets
│   │   └── README.md
│   ├── splunk-bots/                   # Splunk Boss of the SOC datasets
│   │   └── README.md
│   └── cic-ddos2019/                  # CIC-DDoS-2019 dataset
│       └── README.md
├── lab-generated/                     # Datasets to be generated in lab VMs
│   ├── README.md                      # Lab dataset generation guide
│   ├── ransomware-simulation/         # Ransomware attack simulation data
│   ├── backup-trust-validation/       # Recovery point trust scoring data
│   └── multi-stage-attack/            # Multi-stage APT simulation data
└── scripts/
    ├── download_all.py                # Master download script
    ├── verify_datasets.py             # Dataset integrity verification
    └── requirements.txt               # Python dependencies
```

---

## Dataset Categories & Project Mapping

| Category | Datasets | Project Module / Agent |
|----------|----------|----------------------|
| **Network Traffic & IDS** | CICIDS2017, CICIDS2018, UNSW-NB15, NSL-KDD, CIC-DDoS2019 | Triage Agent, Investigation Agent |
| **Botnet & APT Detection** | CTU-13, DARPA OpTC | Investigation Agent, Response Planner |
| **Malware & Ransomware** | EMBER, CIC-MalMem-2022 | Triage Agent, Trust Agent |
| **Enterprise Security Logs** | LANL Cyber, Splunk BOTS | Investigation Agent, Triage Agent |
| **Threat Intelligence** | MITRE ATT&CK STIX, MITRE D3FEND, MITRE CAR | CTI Agent, Response Planner, Recovery Planner |
| **Attack Simulation** | OTRF Security Datasets, Atomic Red Team | Validation Agent, Execution Agent |
| **Lab-Generated** | Ransomware Simulation, Backup Trust, Multi-Stage APT | Trust Agent, Recovery Planner, Validation Agent |

---

## Quick Start

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Download all public datasets
python scripts/download_all.py

# Verify dataset integrity
python scripts/verify_datasets.py
```

---

## References

- Canadian Institute for Cybersecurity (CIC): https://www.unb.ca/cic/datasets/
- MITRE ATT&CK: https://attack.mitre.org/
- MITRE D3FEND: https://d3fend.mitre.org/
- Stratosphere Laboratory: https://www.stratosphereips.org/datasets-overview
- LANL Cyber Security Research: https://csr.lanl.gov/data/
- OTRF Security Datasets: https://github.com/OTRF/Security-Datasets
- Splunk BOTS: https://github.com/splunk/botsv3

---

*Closes [#14](https://github.com/CAPSTONE-221/Incident-Response-and-Resilient-Recovery/issues/14)*

