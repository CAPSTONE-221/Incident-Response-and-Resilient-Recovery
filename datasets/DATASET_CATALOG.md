# Dataset Catalog — Detailed Documentation

## Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery

> This document provides a comprehensive evaluation of each dataset including source, description, features, size, format, relevance, and suitability for the project.

---

## Table of Contents

1. [Network Traffic & Intrusion Detection Datasets](#1-network-traffic--intrusion-detection-datasets)
   - 1.1 [CIC-IDS-2017](#11-cic-ids-2017)
   - 1.2 [CSE-CIC-IDS-2018](#12-cse-cic-ids-2018)
   - 1.3 [UNSW-NB15](#13-unsw-nb15)
   - 1.4 [NSL-KDD](#14-nsl-kdd)
   - 1.5 [CIC-DDoS-2019](#15-cic-ddos-2019)
2. [Botnet & APT Datasets](#2-botnet--apt-datasets)
   - 2.1 [CTU-13](#21-ctu-13-botnet-dataset)
   - 2.2 [DARPA OpTC](#22-darpa-optc-transparent-computing)
3. [Malware & Ransomware Datasets](#3-malware--ransomware-datasets)
   - 3.1 [EMBER 2018](#31-ember-2018)
   - 3.2 [CIC-MalMem-2022](#32-cic-malmem-2022)
4. [Enterprise Security Logs](#4-enterprise-security-logs)
   - 4.1 [LANL Comprehensive Cyber Security Events](#41-lanl-comprehensive-cyber-security-events)
   - 4.2 [Splunk Boss of the SOC (BOTS)](#42-splunk-boss-of-the-soc-bots)
5. [Threat Intelligence & ATT&CK Datasets](#5-threat-intelligence--attck-datasets)
   - 5.1 [MITRE ATT&CK STIX Data](#51-mitre-attck-stix-data)
   - 5.2 [MITRE D3FEND](#52-mitre-d3fend)
   - 5.3 [MITRE Cyber Analytics Repository (CAR)](#53-mitre-cyber-analytics-repository-car)
6. [Attack Simulation Datasets](#6-attack-simulation-datasets)
   - 6.1 [OTRF Security Datasets (Mordor)](#61-otrf-security-datasets-mordor)
   - 6.2 [Atomic Red Team](#62-atomic-red-team)
7. [Lab-Generated Datasets](#7-lab-generated-datasets-to-be-created)
   - 7.1 [Ransomware Simulation Dataset](#71-ransomware-simulation-dataset)
   - 7.2 [Backup/Recovery Trust Validation Dataset](#72-backuprecovery-trust-validation-dataset)
   - 7.3 [Multi-Stage APT Simulation Dataset](#73-multi-stage-apt-simulation-dataset)
8. [Dataset Comparison Matrix](#8-dataset-comparison-matrix)
9. [Dataset-to-Agent Mapping](#9-dataset-to-agent-mapping)

---

## 1. Network Traffic & Intrusion Detection Datasets

### 1.1 CIC-IDS-2017

| Attribute | Details |
|-----------|---------|
| **Full Name** | Canadian Institute for Cybersecurity Intrusion Detection System 2017 |
| **Source** | University of New Brunswick (UNB), Canadian Institute for Cybersecurity |
| **URL** | https://www.unb.ca/cic/datasets/ids-2017.html |
| **Mirror** | Kaggle: `Network Intrusion dataset CIC-IDS-2017` |
| **Year** | 2017 |
| **Size** | ~50 GB (PCAPs), ~1.5 GB (CSV) |
| **Format** | PCAP (raw), CSV (preprocessed with CICFlowMeter) |
| **License** | Open / Academic Research |
| **Records** | ~2.8 million flow records |

**Description:**
Generated over 5 days (Monday–Friday) of network traffic simulation containing both benign and attack traffic. The dataset was created using CICFlowMeter, which extracts over 80 network flow features. Attacks were profiled using the B-Profile system to simulate realistic human behavior.

**Attack Types Covered:**
- Monday: Benign (normal activity only)
- Tuesday: Brute Force (FTP, SSH)
- Wednesday: DoS (Slowloris, Slowhttptest, Hulk, GoldenEye), Heartbleed
- Thursday: Web Attacks (Brute Force, XSS, SQL Injection), Infiltration
- Friday: Botnet, Port Scan, DDoS

**Key Features (80+ features):**
- Flow ID, Source IP, Source Port, Destination IP, Destination Port, Protocol
- Flow Duration, Total Fwd/Bwd Packets, Packet Length (Min, Max, Mean, Std)
- Flow Bytes/s, Flow Packets/s, Flow IAT (Mean, Std, Max, Min)
- Fwd/Bwd Header Length, Fwd/Bwd Packets/s
- Flags (FIN, SYN, RST, PSH, ACK, URG, CWE, ECE)
- Active/Idle Time, Subflow metrics
- **Label** (BENIGN or specific attack type)

**Relevance to Project:**
- **Triage Agent**: Train attack classification models to categorize incoming alerts by type and severity
- **Investigation Agent**: Correlate network flow features with known attack patterns
- Provides labeled multi-class classification data for the incident triage pipeline

**Quality Assessment:** ⭐⭐⭐⭐ (High quality, well-labeled, widely cited, some class imbalance)

---

### 1.2 CSE-CIC-IDS-2018

| Attribute | Details |
|-----------|---------|
| **Full Name** | Communications Security Establishment – CIC IDS 2018 |
| **Source** | CIC + Communications Security Establishment (CSE), Canada |
| **URL** | https://www.unb.ca/cic/datasets/ids-2018.html |
| **Download** | AWS Open Data: `aws s3 ls --no-sign-request s3://cse-cic-ids2018/` |
| **Mirror** | Kaggle: `IDS 2018 Intrusion CSVs` |
| **Year** | 2018 |
| **Size** | ~400 GB (full), ~6.5 GB (CSV preprocessed) |
| **Format** | PCAP, CSV |
| **License** | Open / Academic Research |
| **Records** | ~16 million flow records |

**Description:**
An expanded successor to CICIDS2017 with a larger infrastructure (50 machines for attack traffic, 420 machines + 30 servers for victim organization). Contains 10 days of network traffic with 7 different attack scenarios. More realistic and larger-scale than its predecessor.

**Attack Types Covered:**
- Brute-Force (Web, SSH, FTP)
- Heartbleed
- Botnet
- DoS (Hulk, Slowloris, SlowHTTPTest, GoldenEye)
- DDoS (LOIC-HTTP, LOIC-UDP, HOIC)
- Web Attacks (SQL Injection, XSS, Brute Force)
- Infiltration (Dropbox Download, Cool Disk)

**Relevance to Project:**
- **Triage Agent**: Larger training set for more robust attack detection models
- **Investigation Agent**: Multi-day attack sequences allow correlation analysis
- Scale matches enterprise environments better than CICIDS2017

**Quality Assessment:** ⭐⭐⭐⭐⭐ (Best-in-class IDS dataset, massive scale, diverse attacks)

---

### 1.3 UNSW-NB15

| Attribute | Details |
|-----------|---------|
| **Full Name** | University of New South Wales Network-Based 2015 |
| **Source** | Australian Centre for Cyber Security (ACCS), UNSW Canberra |
| **URL** | https://research.unsw.edu.au/projects/unsw-nb15-dataset |
| **Download** | Kaggle: `UNSW-NB15` |
| **Year** | 2015 |
| **Size** | ~2 GB (CSV), ~100 GB (PCAP) |
| **Format** | CSV, PCAP |
| **License** | Open / Academic Research |
| **Records** | ~2.54 million records (175,341 training / 82,332 testing in benchmark split) |
| **Features** | 49 features |

**Description:**
Created using the IXIA PerfectStorm tool in the Cyber Range Lab at UNSW Canberra. Contains a hybrid of real modern normal activities and synthetic contemporary attack behaviours from the CVE database.

**Attack Types (9 families):**
Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode, Worms

**Key Features (49):**
- Flow features (duration, protocol, service, state)
- Basic features (source/dest bytes, source/dest TTL)
- Content features (source/dest TCP window, HTTP transactions)
- Time features (jitter, start/last time)
- Generated features (ct_srv_src, ct_dst_ltm, ct_src_dport_ltm)
- Binary label and attack category label

**Relevance to Project:**
- **Triage Agent**: Complementary to CICIDS for attack classification (different attack families)
- **Investigation Agent**: Modern attack patterns including exploits and backdoors
- 9-class multi-classification aligns with incident severity determination

**Quality Assessment:** ⭐⭐⭐⭐ (Modern attacks, well-structured features, slightly older)

---

### 1.4 NSL-KDD

| Attribute | Details |
|-----------|---------|
| **Full Name** | NSL-KDD (Improved KDD Cup 1999) |
| **Source** | University of New Brunswick |
| **URL** | https://www.unb.ca/cic/datasets/nsl.html |
| **Download** | Kaggle: `NSL-KDD Dataset` |
| **Year** | 2009 (improved from 1999) |
| **Size** | ~25 MB |
| **Format** | CSV, ARFF |
| **License** | Open / Academic Research |
| **Records** | 125,973 (training) / 22,544 (testing) |
| **Features** | 41 features + label |

**Description:**
An improved version of KDD Cup 1999 that removes redundant records to prevent bias toward frequent patterns. Includes 4 attack categories: DoS, Probe, R2L (Remote-to-Local), U2R (User-to-Root).

**Relevance to Project:**
- **Baseline benchmarking**: Well-established benchmark for comparing model performance
- Lightweight dataset suitable for initial model prototyping and algorithm validation
- Useful for establishing baseline detection accuracy before testing on larger datasets

**Quality Assessment:** ⭐⭐⭐ (Classic benchmark, aging traffic patterns, good for baseline comparison)

---

### 1.5 CIC-DDoS-2019

| Attribute | Details |
|-----------|---------|
| **Full Name** | CIC DDoS Evaluation Dataset 2019 |
| **Source** | Canadian Institute for Cybersecurity |
| **URL** | https://www.unb.ca/cic/datasets/ddos-2019.html |
| **Year** | 2019 |
| **Size** | ~30 GB (CSV) |
| **Format** | CSV, PCAP |
| **License** | Open / Academic Research |

**Description:**
Focused specifically on DDoS attacks with both reflection-based and exploitation-based attack vectors. Contains 12 types of DDoS attacks.

**Attack Types:**
- Reflection-based: MSSQL, SSDP, DNS, LDAP, NetBIOS, SNMP, NTP, UDP, TFTP
- Exploitation-based: SYN, UDP-Lag, WebDDoS

**Relevance to Project:**
- **Triage Agent**: Specialized DDoS detection and classification
- **Response Planner**: DDoS-specific containment strategies

**Quality Assessment:** ⭐⭐⭐⭐ (Comprehensive DDoS coverage, modern attacks)

---

## 2. Botnet & APT Datasets

### 2.1 CTU-13 Botnet Dataset

| Attribute | Details |
|-----------|---------|
| **Full Name** | CTU-13: A Labeled Dataset with Botnet, Normal, and Background Traffic |
| **Source** | Stratosphere Laboratory, Czech Technical University (CTU), Prague |
| **URL** | https://www.stratosphereips.org/datasets-ctu13 |
| **Download** | Kaggle: `CTU-13 Dataset` |
| **Year** | 2011–2014 |
| **Size** | ~60 GB (full PCAPs), ~2 GB (Binetflow files) |
| **Format** | PCAP, Binetflow (CSV-like), Argus |
| **License** | Open / Academic Research |
| **Scenarios** | 13 distinct capture scenarios |

**Description:**
Contains real botnet traffic mixed with normal and background traffic, captured in 13 different scenarios. Each scenario involves a specific malware sample (e.g., Neris, Rbot, Virut, NSIS, Sogou, Murlo, Menti) running on a real host while normal and background traffic was also present.

**Botnet Families:**
| Scenario | Malware | Duration | Packets | Flows |
|----------|---------|----------|---------|-------|
| 1 | Neris | 6.15h | 71M | 2.8M |
| 2 | Neris | 4.21h | 71M | 1.8M |
| 3 | Rbot | 66.85h | 167M | 4.7M |
| 4 | Rbot | 4.21h | 62M | 1.1M |
| 5 | Virut | 11.63h | 4.5M | 129K |
| 6 | Menti | 2.18h | 38M | 558K |
| 7 | Sogou | 0.38h | 7.4M | 114K |
| 8 | Murlo | 19.5h | 155M | 2.9M |
| 9 | Neris | 5.18h | 115M | 2.0M |
| 10 | Rbot | 4.75h | 90M | 1.3M |
| 11 | Rbot | 0.26h | 6.3M | 107K |
| 12 | NSIS | 1.21h | 13M | 325K |
| 13 | Virut | 16.36h | 50M | 1.9M |

**Labels:** Background, Normal, Botnet (with detailed sub-labels)

**Relevance to Project:**
- **Investigation Agent**: Botnet C2 communication patterns for attack-chain reconstruction
- **Triage Agent**: Botnet vs normal traffic classification
- Referenced directly in CIPHER-A research paper (used for network blocking consequence study)

**Quality Assessment:** ⭐⭐⭐⭐ (Real botnet traffic, well-labeled, good for C2 detection)

---

### 2.2 DARPA OpTC (Transparent Computing)

| Attribute | Details |
|-----------|---------|
| **Full Name** | DARPA Operationally Transparent Cyber (OpTC) Dataset |
| **Source** | DARPA / Five Directions |
| **URL** | https://github.com/FiveDirections/OpTC-data |
| **Year** | 2019–2020 |
| **Size** | ~1 TB (compressed JSON telemetry) |
| **Format** | JSON (CDM — Common Data Model) |
| **License** | Open / Government Research |

**Description:**
Multi-day, multi-host controlled APT simulation across 500+ enterprise Windows 10 hosts. Contains host-level telemetry (process creation, file operations, network connections, registry modifications) with injected red-team APT activities over benign background noise. Part of the DARPA Transparent Computing program designed for provenance graph analysis.

**Data Streams:**
- Endpoint telemetry (process, file, network, registry events)
- Benign background traffic (realistic enterprise workload)
- Red-team APT injection (ground-truth attack labels)

**Key CDM Event Types:**
- `EVENT_OPEN`, `EVENT_CLOSE`, `EVENT_READ`, `EVENT_WRITE`
- `EVENT_EXECUTE`, `EVENT_CREATE_OBJECT`, `EVENT_MODIFY_FILE_ATTRIBUTES`
- `EVENT_CONNECT`, `EVENT_ACCEPT`, `EVENT_RECVFROM`, `EVENT_SENDTO`

**Relevance to Project:**
- **Investigation Agent**: Attack-chain reconstruction from host provenance graphs
- **Trust Agent**: Asset compromise timeline from host telemetry
- **Response Planner**: Multi-host blast radius assessment
- **Critical**: Directly referenced in CIPHER-A paper (Kizhakel & Pande, 2026) used by Dhruva's research

**Quality Assessment:** ⭐⭐⭐⭐⭐ (Gold-standard APT dataset, realistic enterprise scale, ground-truth labels)

---

## 3. Malware & Ransomware Datasets

### 3.1 EMBER 2018

| Attribute | Details |
|-----------|---------|
| **Full Name** | Elastic Malware Benchmark for Empowering Researchers 2018 |
| **Source** | Endgame / Elastic |
| **URL** | https://github.com/elastic/ember |
| **Download** | `https://ember.elastic.co/ember_dataset_2018_2.tar.bz2` |
| **Year** | 2018 |
| **Size** | ~4 GB (compressed) |
| **Format** | JSON (feature vectors), Python pickle |
| **License** | Open / Academic Research |
| **Records** | 1.1 million PE file samples (600K training, 200K test, 300K unlabeled) |
| **Features** | 2,351 features extracted from PE headers |

**Description:**
Contains extracted features from 1.1 million Windows Portable Executable (PE) files. Features are derived from PE headers, imports, exports, sections, and byte histograms. Designed for training static malware detection models without requiring raw binaries.

**Feature Categories:**
- Byte histogram (256 features)
- Byte-entropy histogram (256 features)
- String information (104 features)
- General file info (10 features)
- PE header info (62 features)
- Section info (255 features)
- Import info (1,280 features)
- Export info (128 features)

**Labels:** Malicious (1), Benign (0), Unlabeled (-1)

**Relevance to Project:**
- **Triage Agent**: Malware detection models for file-level threat classification
- **Trust Agent**: Determining if files/executables on recovery points are clean
- Supports the Threat-Free Confidence (T) variable in the Recovery Trust Score formula

**Quality Assessment:** ⭐⭐⭐⭐⭐ (Industry-standard malware benchmark, large scale, reproducible)

---

### 3.2 CIC-MalMem-2022

| Attribute | Details |
|-----------|---------|
| **Full Name** | CIC Malware Memory Analysis 2022 |
| **Source** | Canadian Institute for Cybersecurity |
| **URL** | https://www.unb.ca/cic/datasets/malmem-2022.html |
| **Download** | Kaggle: `CIC-MalMem-2022` |
| **Year** | 2022 |
| **Size** | ~50 MB (CSV) |
| **Format** | CSV |
| **License** | Open / Academic Research |
| **Records** | 58,596 (balanced: 50% malicious, 50% benign) |

**Description:**
Memory forensics dataset for detecting obfuscated malware. Malware samples were executed in sandboxed Windows 10 VMs, and memory dumps were captured and analyzed using VolMemLyzer (Volatility framework on Kali Linux) to extract kernel-level and process-level features.

**Malware Categories & Families:**
| Category | Families |
|----------|---------|
| **Ransomware** | Conti, MAZE, Pysa, Ako, Shade |
| **Spyware** | 180Solutions, Coolwebsearch, Gator, Transponder, TIBS |
| **Trojan** | Zeus, Emotet, Refroso, Scar, Reconyc |

**Key Memory Features:**
- Process-level: VAD (Virtual Address Descriptor), handles, DLLs, threads
- Kernel-level: SSDT hooks, driver objects, callbacks
- Injection artifacts: code injection indicators, suspicious memory regions

**Relevance to Project:**
- **Trust Agent**: Critical for Recovery Trust Score — validates if a system/backup is malware-free
- **Validation Agent**: Post-recovery verification that restored systems are clean
- Directly supports the Threat-Free Confidence (T) and Reinfection Risk (R) variables in the RTS formula
- **Ransomware families** (Conti, MAZE) directly relevant to the primary evaluation scenario

**Quality Assessment:** ⭐⭐⭐⭐⭐ (Perfect for ransomware detection, memory-level features, balanced classes, modern malware families)

---

## 4. Enterprise Security Logs

### 4.1 LANL Comprehensive Cyber Security Events

| Attribute | Details |
|-----------|---------|
| **Full Name** | Comprehensive Multi-Source Cyber-Security Events Dataset |
| **Source** | Los Alamos National Laboratory (LANL) |
| **URL** | https://csr.lanl.gov/data/cyber1/ |
| **Year** | 2015 |
| **Size** | ~12 GB (compressed) |
| **Format** | CSV/TXT (tab-separated) |
| **License** | Open / Academic Research |
| **Duration** | 58 consecutive days |
| **Scale** | 1.64 billion events, 12,425 users, 17,684 computers, 62,974 processes |

**Description:**
One of the most comprehensive enterprise security datasets ever publicly released. Collected from LANL's internal corporate network over 58 consecutive days. All entities are de-identified but consistently anonymized across data streams.

**Data Streams:**
| File | Description | Approx. Events |
|------|-------------|----------------|
| `auth.txt` | Windows authentication events (logins, logoffs, Active Directory) | 1.05 billion |
| `proc.txt` | Process start/stop events on Windows endpoints | 426 million |
| `dns.txt` | DNS query logs from internal DNS servers | 40 million |
| `flows.txt` | Network flow data from enterprise routers | 129 million |
| `redteam.txt` | Ground-truth red-team attack events | 749 events |

**Schema Examples:**
- `auth.txt`: `time, source_user@domain, dest_user@domain, source_computer, dest_computer, auth_type, logon_type, auth_orientation, success/failure`
- `flows.txt`: `time, duration, source_computer, source_port, dest_computer, dest_port, protocol, packet_count, byte_count`
- `redteam.txt`: `time, source_user@domain, source_computer, dest_computer`

**Relevance to Project:**
- **Investigation Agent**: Cross-correlate authentication, process, network, and DNS events for attack-chain reconstruction
- **Trust Agent**: Authentication anomalies indicate asset compromise → affects RTS
- **Triage Agent**: Lateral movement detection from auth events
- Red-team ground truth enables supervised training for attack detection
- Multi-source correlation is exactly what the proposed framework's telemetry correlation engine requires

**Quality Assessment:** ⭐⭐⭐⭐⭐ (Largest real-world enterprise dataset, multi-source, ground-truth red-team labels, 58-day window)

---

### 4.2 Splunk Boss of the SOC (BOTS)

| Attribute | Details |
|-----------|---------|
| **Full Name** | Splunk Boss of the SOC Datasets (v1, v2, v3) |
| **Source** | Splunk Inc. |
| **URLs** | v1: https://github.com/splunk/botsv1 |
|  | v2: https://github.com/splunk/botsv2 |
|  | v3: https://github.com/splunk/botsv3 |
| **Year** | 2017–2020 |
| **Size** | v2: ~16.4 GB (full), ~3.2 GB (attack-only); v3: ~320 MB |
| **Format** | Splunk pre-indexed data (SPL) |
| **License** | Open / CC BY-SA 4.0 |

**Description:**
Real-world-like SIEM log datasets created for Splunk's Boss of the SOC cybersecurity competitions. Contains multi-source log data from simulated enterprise environments with injected attack scenarios.

**BOTS v2 Data Sources:**
- Windows Event Logs (Sysmon, Security, System)
- Suricata IDS alerts
- Apache/IIS web logs
- DNS logs
- Osquery results
- Stream network captures
- AWS CloudTrail and VPC flow logs
- Fortinet firewall logs

**BOTS v3 Scenarios:**
- Cloud security (AWS, Azure)
- APT investigations
- Data exfiltration
- Ransomware

**Relevance to Project:**
- **Triage Agent**: Multi-source SIEM alert processing and prioritization
- **Investigation Agent**: Cross-source log correlation (endpoint + network + cloud)
- **Response Planner**: Realistic enterprise log context for response planning
- Simulates the actual SIEM environment the proposed framework would operate in

**Quality Assessment:** ⭐⭐⭐⭐ (Realistic SIEM data, multi-source, requires Splunk for native format)

---

## 5. Threat Intelligence & ATT&CK Datasets

### 5.1 MITRE ATT&CK STIX Data

| Attribute | Details |
|-----------|---------|
| **Full Name** | MITRE ATT&CK Framework — STIX 2.1 Data |
| **Source** | MITRE Corporation |
| **URL** | https://github.com/mitre-attack/attack-stix-data |
| **API** | TAXII 2.1 Server: `https://cti-taxii.mitre.org/` |
| **Year** | Continuously updated (latest: v16, Oct 2024) |
| **Format** | JSON (STIX 2.1) |
| **License** | Apache 2.0 |

**Description:**
The complete MITRE ATT&CK knowledge base in machine-readable STIX 2.1 format. Contains detailed descriptions of adversary tactics, techniques, and procedures (TTPs), threat groups, software, mitigations, and data sources.

**STIX Object Types:**
- `attack-pattern`: ATT&CK Techniques and Sub-techniques (~800+)
- `intrusion-set`: Threat Groups (~140+)
- `malware`: Known malware families (~600+)
- `tool`: Adversary tools (~80+)
- `course-of-action`: Mitigations (~40+)
- `x-mitre-tactic`: ATT&CK Tactics (14)
- `x-mitre-data-source`: Data sources for detection
- `relationship`: Maps techniques to groups, software, mitigations

**Relevance to Project:**
- **CTI Agent**: Core threat intelligence knowledge base for grounding LLM responses
- **Investigation Agent**: Map observed indicators to ATT&CK techniques for attack-chain reconstruction
- **Response Planner**: Look up recommended mitigations for identified techniques
- **Recovery Planner**: Understand adversary objectives to assess blast radius
- Referenced in ALL research papers surveyed (Hammar et al., Tellache et al., Kizhakel & Pande)

**Quality Assessment:** ⭐⭐⭐⭐⭐ (Industry-standard, continuously maintained, machine-readable, comprehensive)

---

### 5.2 MITRE D3FEND

| Attribute | Details |
|-----------|---------|
| **Full Name** | MITRE D3FEND — A Knowledge Graph of Cybersecurity Countermeasures |
| **Source** | MITRE Corporation |
| **URL** | https://d3fend.mitre.org/ |
| **GitHub** | https://github.com/d3fend/d3fend-ontology |
| **Format** | OWL (Ontology), JSON-LD |
| **License** | Open |

**Description:**
Complementary to ATT&CK, D3FEND provides a knowledge graph of defensive techniques and countermeasures. Maps defensive capabilities to the offensive techniques they counter.

**Taxonomy:**
- Harden, Detect, Isolate, Deceive, Evict categories
- Maps to ATT&CK techniques via `counters` relationships

**Relevance to Project:**
- **Response Planner**: Automated selection of appropriate defensive countermeasures
- **Recovery Planner**: Identifies recovery-specific defensive techniques
- Referenced in the NDSS 2026 paper (Hammar et al.) for recovery stage taxonomy

**Quality Assessment:** ⭐⭐⭐⭐ (Authoritative, structured, complements ATT&CK)

---

### 5.3 MITRE Cyber Analytics Repository (CAR)

| Attribute | Details |
|-----------|---------|
| **Full Name** | MITRE Cyber Analytics Repository |
| **Source** | MITRE Corporation |
| **URL** | https://car.mitre.org/ |
| **GitHub** | https://github.com/mitre-attack/car |
| **Format** | YAML, JSON |
| **License** | Apache 2.0 |

**Description:**
A knowledge base of analytics (detection rules) developed by MITRE based on the ATT&CK adversary model. Each analytic includes pseudocode, implementations (Splunk, EQL, Sigma), data model references, and coverage mapping to ATT&CK techniques.

**Relevance to Project:**
- **Triage Agent**: Pre-built detection rules for alert generation
- **Investigation Agent**: Analytics for identifying specific attack techniques from telemetry

**Quality Assessment:** ⭐⭐⭐⭐ (Ready-to-use detection logic, ATT&CK-mapped)

---

## 6. Attack Simulation Datasets

### 6.1 OTRF Security Datasets (Mordor)

| Attribute | Details |
|-----------|---------|
| **Full Name** | Open Threat Research Forge (OTRF) Security Datasets (formerly Mordor) |
| **Source** | Open Threat Research Forge |
| **URL** | https://github.com/OTRF/Security-Datasets |
| **Playbook** | https://github.com/OTRF/ThreatHunter-Playbook |
| **Year** | 2019–present |
| **Format** | JSON (pre-recorded security events) |
| **License** | Open Source |

**Description:**
Pre-recorded security events generated by simulating adversarial techniques in controlled environments. Each dataset is categorized by MITRE ATT&CK tactics and techniques and contains Windows Event Logs, Sysmon logs, and other security telemetry produced during attack simulation.

**Organized By:**
- ATT&CK Tactics (Initial Access, Execution, Persistence, Privilege Escalation, etc.)
- ATT&CK Techniques (specific technique IDs)
- Platform (Windows, Linux, macOS)

**Relevance to Project:**
- **Investigation Agent**: Pre-labeled attack telemetry for training detection models
- **Triage Agent**: ATT&CK-mapped security events for classification
- **Validation Agent**: Ground-truth events for validating detection capabilities
- Pairs with Threat Hunter Playbook for detection engineering

**Quality Assessment:** ⭐⭐⭐⭐ (ATT&CK-mapped, ready-to-use, growing collection)

---

### 6.2 Atomic Red Team

| Attribute | Details |
|-----------|---------|
| **Full Name** | Atomic Red Team by Red Canary |
| **Source** | Red Canary |
| **URL** | https://github.com/redcanaryco/atomic-red-team |
| **Year** | 2017–present |
| **Format** | YAML (test definitions), PowerShell/Bash (execution scripts) |
| **License** | MIT |

**Description:**
Library of small, portable, standalone tests mapped directly to MITRE ATT&CK techniques. Each "atomic" test simulates a specific malicious action. Can be used with MITRE CALDERA for automated adversary emulation.

**Relevance to Project:**
- **Lab Dataset Generation**: Execute atomic tests in lab VMs to generate ground-truth attack data
- **Validation Agent**: Test detection capabilities against known techniques
- Enables creation of lab-generated datasets (Section 7)

**Quality Assessment:** ⭐⭐⭐⭐⭐ (Comprehensive ATT&CK coverage, executable, maintained by Red Canary)

---

## 7. Lab-Generated Datasets (To Be Created)

> [!IMPORTANT]
> These datasets must be generated in controlled lab environments using team members' VMs. They address the unique aspects of the project that no public dataset covers — specifically **recovery point trust assessment** and **backup integrity validation**.

### 7.1 Ransomware Simulation Dataset

| Attribute | Details |
|-----------|---------|
| **Purpose** | Primary evaluation dataset for Trust-Conditioned Recovery Planning (TCRP) |
| **Environment** | Windows 10/11 VMs (VirtualBox/VMware), Kali Linux attacker VM |
| **Tools** | MITRE CALDERA, Atomic Red Team, custom ransomware simulation scripts |

**Data to Capture:**
1. **Pre-Attack Telemetry** (baseline):
   - Normal process events (Sysmon logs)
   - Network flows (normal traffic)
   - File system state snapshots
   - Authentication events
   - Scheduled backups with integrity hashes

2. **Attack Phase Telemetry**:
   - Ransomware deployment and execution (simulated — NOT real ransomware)
   - File encryption events
   - Lateral movement attempts
   - C2 communication
   - Privilege escalation attempts

3. **Recovery Phase Data**:
   - Multiple backup snapshots (some pre-compromise, some post-compromise)
   - Backup metadata (timestamp, hash, size, location)
   - Recovery attempt logs
   - Post-restoration system state

**Generated Labels:**
- Backup timestamp relative to compromise window
- Backup integrity status (clean / contaminated / uncertain)
- Recovery success/failure
- Recovery Trust Score ground truth

**Relevance to Project:**
- **Trust Agent**: Training data for Recovery Trust Score (RTS) calculation
- **Recovery Planner**: Clean vs. contaminated recovery-point selection evaluation
- **Validation Agent**: Post-recovery verification testing
- **This is the PRIMARY evaluation dataset** for the core TCRP mechanism

---

### 7.2 Backup/Recovery Trust Validation Dataset

| Attribute | Details |
|-----------|---------|
| **Purpose** | Training and evaluation data for the Recovery Trust Score formula |
| **Environment** | Windows Server VMs with backup infrastructure |

**Data to Generate:**
For each backup/recovery point, record:
- **I (Integrity)**: File hashes before/after, signature verification results, filesystem consistency check results, restore verification test pass/fail
- **V (Temporal Validity)**: Backup timestamp, estimated compromise start time, backup predates/postdates compromise
- **T (Threat-Free Confidence)**: IOC scan results, malware scan results, encryption indicators
- **F (Forensic/Provenance)**: Backup chain of custody, independent log corroboration, backup host trust status
- **R (Reinfection Risk)**: Backup server compromise status, malicious file indicators, exposed credential presence, compromised dependency status

**Ground Truth Labels:**
- TRUSTED / UNCERTAIN / UNTRUSTED (per problem statement Section 9)
- Human expert assessment of recovery point safety
- Known compromise status (injected)

---

### 7.3 Multi-Stage APT Simulation Dataset

| Attribute | Details |
|-----------|---------|
| **Purpose** | Multi-stage attack scenarios for blast radius assessment |
| **Environment** | Multi-VM network with domain controller, file server, web server, database server |

**Attack Scenarios to Simulate:**
1. **Initial Access** → **Lateral Movement** → **Data Exfiltration**
2. **Phishing** → **Privilege Escalation** → **Ransomware Deployment**
3. **Supply Chain Compromise** → **Persistence** → **Credential Theft**

**Data to Capture:**
- Asset dependency graph (which services depend on which)
- Compromise timeline across multiple hosts
- Service impact assessment (which services went down/were degraded)
- Recovery dependency ordering (which services must be restored first)

---

## 8. Dataset Comparison Matrix

| Dataset | Size | Attack Types | Labels | Year | Format | Ease of Use | Relevance |
|---------|------|-------------|--------|------|--------|-------------|-----------|
| CIC-IDS-2017 | 1.5 GB | 14 | ✅ Multi-class | 2017 | CSV | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| CSE-CIC-IDS-2018 | 6.5 GB | 14+ | ✅ Multi-class | 2018 | CSV | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| UNSW-NB15 | 2 GB | 9 | ✅ Multi-class | 2015 | CSV | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| NSL-KDD | 25 MB | 4 | ✅ Multi-class | 2009 | CSV | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| CIC-DDoS-2019 | 30 GB | 12 | ✅ Multi-class | 2019 | CSV | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| CTU-13 | 2 GB | 7 botnets | ✅ 3-class | 2014 | Binetflow | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| DARPA OpTC | 1 TB | APT | ✅ Binary | 2020 | JSON | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| EMBER 2018 | 4 GB | Malware | ✅ Binary | 2018 | JSON | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| CIC-MalMem-2022 | 50 MB | 3 families | ✅ Multi-class | 2022 | CSV | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| LANL Cyber | 12 GB | Red team | ✅ Binary | 2015 | TXT | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Splunk BOTS | 16 GB | Multi-type | Partial | 2020 | SPL | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| ATT&CK STIX | ~50 MB | Knowledge Base | N/A | 2024+ | JSON | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| OTRF/Mordor | ~5 GB | ATT&CK mapped | ✅ | 2024+ | JSON | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 9. Dataset-to-Agent Mapping

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        FRAMEWORK ARCHITECTURE                          │
│                                                                         │
│  ┌─────────────┐    Datasets: CICIDS2017/2018, UNSW-NB15, NSL-KDD     │
│  │ Triage Agent │◄── CIC-DDoS-2019, EMBER, CIC-MalMem-2022            │
│  │              │    MITRE CAR (detection rules)                        │
│  └──────┬───────┘                                                       │
│         │                                                               │
│  ┌──────▼───────────┐  Datasets: LANL Cyber, DARPA OpTC, CTU-13       │
│  │Investigation Agent│◄── Splunk BOTS, OTRF/Mordor                     │
│  │                   │    ATT&CK STIX (technique mapping)              │
│  └──────┬────────────┘                                                  │
│         │                                                               │
│  ┌──────▼──────┐    Datasets: Lab-Generated (Backup Trust)             │
│  │ Trust Agent  │◄── CIC-MalMem-2022 (malware-free validation)         │
│  │              │    EMBER (file integrity checking)                    │
│  │              │    Lab-Generated (RTS ground truth)                   │
│  └──────┬───────┘                                                       │
│         │                                                               │
│  ┌──────▼──────────┐  Datasets: ATT&CK STIX (mitigations)             │
│  │ Response Planner │◄── D3FEND (countermeasures)                      │
│  │                  │    DARPA OpTC (blast radius)                      │
│  └──────┬───────────┘                                                   │
│         │                                                               │
│  ┌──────▼──────────┐  Datasets: Lab-Generated (Recovery Trust)         │
│  │ Recovery Planner │◄── Lab-Generated (dependency graphs)             │
│  │                  │    D3FEND (recovery techniques)                   │
│  └──────┬───────────┘                                                   │
│         │                                                               │
│  ┌──────▼───────────┐  Datasets: Atomic Red Team (validation tests)    │
│  │ Validation Agent  │◄── Lab-Generated (post-recovery state)          │
│  │                   │    CIC-MalMem-2022 (clean state verification)   │
│  └───────────────────┘                                                  │
└──────────────────────────────────────────────────────────────────────────┘
```

---

*Document prepared for Capstone Project 221 — Phase I, Issue #14: Dataset Collection*
*Last updated: November 2026*

