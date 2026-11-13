# Cybersecurity Datasets Guide for Team 221

> **Project Title:** Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery  
> **Course:** UE24CS320A – Capstone Project Phase-I (Team ID: 221)  
> **Target Problem:** Autonomous threat containment and resilient recovery from ransomware and multi-stage attacks without falling victim to **contaminated recovery** (restoring infected backups).

---

## 📖 Welcome Team! What is this Folder?

Hey everyone! This directory contains the **curated cybersecurity datasets** and **simulation files** needed to build, train, and test our Capstone system. 

When presenting to our project guide or external reviewers, every team member must be able to answer:
1. *What datasets are in our repository?*
2. *Why did we choose each one instead of generic toy data?*
3. *Which specific AI Agent in our system consumes which dataset?*

This document explains everything in clear, simple terms.

---

## 🧠 The Core Idea of Our Project in 60 Seconds

Traditional cybersecurity systems (like SOAR playbooks) try to detect attacks, but when an attacker compromises the system and deploys ransomware, **admins panic and restore the newest backup**.

💥 **The Problem (Contaminated Recovery):**  
If the attacker breached the network at 10:00 PM, and a scheduled backup ran at 4:00 AM, that backup **already contains the attacker's backdoor**. Restoring it immediately reinfects the enterprise!

🛡️ **Our Solution (Trust-Conditioned Recovery Planning - TCRP):**  
We introduce an autonomous 7-agent AI team that calculates a **Recovery Trust Score (RTS)** for each candidate backup:
$$\text{BaseTrust} = w_1 I + w_2 V + w_3 T + w_4 F$$
$$\text{RTS} = \text{BaseTrust} \times (1 - R)$$

- **$I$ (Integrity):** Hashes and filesystem checks match.
- **$V$ (Temporal Validity):** Backup was taken *before* the attacker's initial breach window.
- **$T$ (Threat-Free Confidence):** Scans show zero malware or ransomware implants.
- **$F$ (Forensic/Provenance):** Backup logs and audit chains confirm it wasn't tampered with.
- **$R$ (Reinfection Risk):** Multiplicative gate — if the backup host or admin credentials were breached, $(1 - R)$ penalizes the trust score to prevent autonomous restoration!

---

## 🗺️ Visual Architecture: Which Agent Uses Which Dataset?

```
[ Incoming Telemetry / SIEM ]
       │
       ├──► simulated_ransomware_telemetry.csv  ── (High-entropy file alerts)
       ├──► Friday-WorkingHours-Afternoon-DDos.csv ── (Network traffic anomaly)
       ▼
 1. TRIAGE AGENT
       │  Datasets: UNSW-NB15 + NSL-KDD
       │  Job: Classifies attack type (Ransomware/DoS/Exploit) and priority in < 1s
       ▼
 2. INVESTIGATION AGENT
       │  Datasets: enterprise-attack.json (STIX 2.1) + LANL/DARPA OpTC
       │  Job: Reconstructs the attack timeline to find the exact breach window
       ▼
 3. TRUST AGENT (RTS Calculator)
       │  Datasets: synthetic_rts_benchmark.csv + CIC-MalMem-2022
       │  Job: Calculates RTS for each backup candidate; flags poisoned backups
       ▼
 4. RESPONSE PLANNER
       │  Datasets: enterprise-attack.json (course-of-action mitigations)
       │  Job: Generates containment actions (isolate subnets, kill C2 sockets)
       ▼
 5. RECOVERY PLANNER
       │  Datasets: service_dependency_dag.json + synthetic_rts_benchmark.csv
       │  Job: Plans restoration in safe topological order (AD -> DB -> Web)
       ▼
 6. EXECUTION AGENT (Policy Gate)
       │  Datasets: service_dependency_dag.json (Tier-1 Policy Rules)
       │  Job: Executes containment autonomously; requires human sign-off for critical DB
       ▼
 7. VALIDATION AGENT
          Datasets: Obfuscated-MalMem2022.csv + Canary Entropy Metrics
          Job: Scans RAM and files post-restore to certify zero residual malware
```

---

## 📂 Master Inventory of Local Datasets

All the following files are present locally in this folder:

| Directory Path | File Name | Size | Records / Objects | Assigned Agent |
|---|---|---|---|---|
| `public/mitre-attack-stix/` | **`enterprise-attack.json`** | 52.72 MB | 26,699 STIX objects | CTI, Investigation, Response |
| `public/cic-malmem-2022/` | **`Obfuscated-MalMem2022.csv`** | 18.04 MB | 58,596 memory dumps | Trust Agent, Validation Agent |
| `public/unsw-nb15/` | **`UNSW_NB15_training-set.csv`**<br>**`UNSW_NB15_testing-set.csv`** | 30.80 MB<br>14.67 MB | 175,341 train<br>82,332 test | Triage Agent |
| `public/nsl-kdd/` | **`KDDTrain+.txt`**<br>**`KDDTest+.txt`** | 18.22 MB<br>3.28 MB | 125,973 train<br>22,544 test | Triage Agent (Baseline) |
| `public/cicids2017/` | **`Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`** | 73.55 MB | 225,745 flows | Triage & Investigation |
| `lab-generated/backup-trust-validation/` | **`synthetic_rts_benchmark.csv`** | 60 KB | 500 recovery points | Trust Agent & Recovery Planner |
| `lab-generated/ransomware-simulation/` | **`simulated_ransomware_telemetry.csv`** | 25 KB | 100 canary events | Triage & Validation Agent |
| `lab-generated/multi-stage-attack/` | **`service_dependency_dag.json`** | 3 KB | 4-tier service graph | Recovery & Execution Agents |

---

## 🔍 Deep-Dive: Why Each Dataset is Here & What it Does

### 1. `public/mitre-attack-stix/enterprise-attack.json`
- **What it is:** The official MITRE ATT&CK Enterprise Matrix in STIX 2.1 JSON format.
- **Why we need it:** AI agents cannot hallucinate incident response steps. This dataset grounds our agents in 867 standardized adversary techniques (`T1486 Data Encrypted for Impact`, `T1078 Valid Accounts`) and 268 verified mitigations (`course-of-action`).
- **Which agent uses it:** 
  - **CTI Agent:** Translates raw IOCs into known attacker behaviors.
  - **Investigation Agent:** Chains together attack steps into a timeline.
  - **Response Planner:** Looks up recommended mitigations to contain the threat.

---

### 2. `public/cic-malmem-2022/Obfuscated-MalMem2022.csv`
- **What it is:** A volatile memory (RAM) forensics dataset created by the Canadian Institute for Cybersecurity (UNB). Contains memory dumps of real ransomware families (**Conti, MAZE, Pysa, Ako, Shade**) alongside benign system processes.
- **Why we need it:** Modern ransomware decrypts itself and injects code into memory (`malfind`, `ldrmodules`). Traditional antivirus scanning disk files will miss it.
- **Which agent uses it:** 
  - **Trust Agent:** Evaluates Threat-Free Confidence ($T$) by verifying if backup snapshots contain memory injection artifacts.
  - **Validation Agent:** Once a server is restored from backup, the validation agent tests its RAM to verify that no dormant rootkits or injected threads remain active before bringing it back online.

---

### 3. `public/unsw-nb15/` (`UNSW_NB15_training-set.csv` & `testing-set.csv`)
- **What it is:** Modern network traffic dataset from the Australian Centre for Cyber Security, featuring 9 modern attack families (Exploits, Fuzzers, Backdoors, DoS, Reconnaissance, Shellcode, Worms).
- **Why we need it:** In real life, ransomware doesn't appear in isolation. Attackers first scan networks (`Reconnaissance`), exploit a vulnerability (`Exploit`), and drop a payload (`Backdoor`).
- **Which agent uses it:** 
  - **Triage Agent:** Trains machine learning classifiers (Random Forest / LightGBM) to classify incoming alerts by type and severity in under a second.

---

### 4. `public/nsl-kdd/` (`KDDTrain+.txt` & `KDDTest+.txt`)
- **What it is:** Refined benchmark dataset with 125,973 training records and 22,544 testing records across 4 attack classes: DoS, Probe, R2L (Remote to Local), and U2R (User to Root).
- **Why we need it:** Standard benchmark in academic literature. We use it to establish our baseline classification accuracy and verify our preprocessing pipeline.
- **Which agent uses it:** 
  - **Triage Agent:** Serves as a lightweight baseline for rapid model comparison.

---

### 5. `public/cicids2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`
- **What it is:** Full network flow dataset extracted with CICFlowMeter (79 features) representing high-volume attack traffic (DDoS / LOIC) mixed with benign office activity.
- **Why we need it:** Attackers frequently launch DDoS or burst network traffic to distract SOC operators while deploying ransomware in the background.
- **Which agent uses it:** 
  - **Triage & Investigation Agents:** Tests the system's ability to filter out background noise and handle burst traffic conditions.

---

### 6. `lab-generated/backup-trust-validation/synthetic_rts_benchmark.csv`
- **What it is:** A ground-truth benchmark dataset of 500 candidate recovery points across 6 realistic operational failure modes:
  1. `clean_pre_compromise`: Safe backups taken before the breach ($V \approx 0.95$).
  2. `post_compromise_poisoned`: Backups taken after initial access ($V \approx 0.20, R \approx 0.75$).
  3. `tampered_integrity`: Corrupted backup images with broken SHA-256 hashes ($I \approx 0.25$).
  4. `compromised_backup_server`: Backup host itself breached by adversary ($R \approx 0.88$, hard violation!).
  5. `uncertain_forensics`: Missing audit logs ($F \approx 0.20$).
  6. `safe_recent_incremental`: Clean incremental snapshots ($RTS \ge 0.90$).
- **Why we need it:** **No public dataset in the world contains recovery trust scores.** This is our capstone project's primary novel contribution. We generated this dataset using the exact mathematical formula defined in our problem statement.
- **Which agent uses it:** 
  - **Trust Agent:** Evaluates and calibrates weights $w_1, w_2, w_3, w_4$.
  - **Recovery Planner:** Evaluates candidate selection accuracy and contaminated-recovery prevention rate.

---

### 7. `lab-generated/ransomware-simulation/simulated_ransomware_telemetry.csv`
- **What it is:** 100 canary file-encryption events simulating the exact filesystem telemetry produced when ransomware executes.
- **Why we need it:** Captures key metrics:
  - `event_id: 11` (Sysmon FileCreate/FileModify)
  - `pre_entropy` vs. `post_entropy` (jump from normal text ~3.5 to high-entropy encrypted ciphertext ~7.95)
  - `renamed_filename` (`.locked` extension)
- **Which agent uses it:** 
  - **Triage Agent:** Detects mass file modification with high entropy.
  - **Validation Agent:** Post-recovery verification that file entropy has stabilized back to normal.

---

### 8. `lab-generated/multi-stage-attack/service_dependency_dag.json`
- **What it is:** A JSON schema modeling a realistic 4-tier enterprise infrastructure:
  $$\text{SVC\_AUTH\_AD} \longrightarrow \text{SVC\_CORE\_DB} \longrightarrow \text{SVC\_BACKEND\_API} \longrightarrow \text{SVC\_WEB\_FRONTEND}$$
- **Why we need it:** In real enterprise recovery, you cannot simply restore machines randomly. If you turn on the web app before the database is online, transactions crash. If you restore without active directory authentication, credentials fail.
- **Which agent uses it:** 
  - **Recovery Planner:** Solves the topological ordering to restore services in safe sequence.
  - **Execution Agent:** Enforces human policy gates (`requires_human_approval_to_restore: true` on Tier-1 database).

---

## 🛠️ How to Verify and Use These Files

### 1. Verify Everything is Working
Run our automated verification script:
```powershell
python datasets/scripts/verify_datasets.py
```
You will see `[OK]` status across all datasets with exact record counts and column validations.

### 2. Download Other Advanced Datasets (Optional)
If you want to pull additional datasets (like Splunk BOTS or clone DARPA OpTC):
```powershell
python datasets/scripts/download_all.py --list
python datasets/scripts/download_all.py --dataset splunk-bots
```

### 3. Generate More Lab Data
To create a larger RTS evaluation benchmark (e.g., 2,000 samples):
```powershell
python datasets/lab-generated/backup-trust-validation/generate_synthetic_rts_eval.py
```

To run a safe local canary encryption simulation:
```powershell
python datasets/lab-generated/ransomware-simulation/simulate_ransomware_activity.py
```

---

## 🤝 Project Contribution & Issue Reference
- **GitHub Issue:** Closes [#14](https://github.com/CAPSTONE-221/Incident-Response-and-Resilient-Recovery/issues/14) (*Dataset Collection & Evaluation*)
- **Next Phase (Issue #15):** Data Preprocessing, Feature Normalization, and Pipeline Construction.
