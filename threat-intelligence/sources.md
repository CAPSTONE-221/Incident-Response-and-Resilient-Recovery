# Threat Intelligence Sources and Attribution

**Project:** Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery  
**Team ID:** 221 (UE24CS320A Capstone Project Phase-I)  
**Author:** Aditya Basavaraj Jambagi (Aditya BJ)  
**GitHub Issue:** [Issue #16 – Collect and Organize Threat Intelligence Sources](https://github.com/CAPSTONE-221/Incident-Response-and-Resilient-Recovery/issues/16)  
**Collection Date:** November 2026 (UTC)

---

## 1. Executive Overview

This document provides transparent attribution, licensing details, collection methodology, and access parameters for the open-source threat intelligence (OSINT) indicators ingested into this dataset.

All indicators were obtained from publicly accessible, legally permitted feeds and research aggregators without violating access controls or terms of service. No proprietary, leaked, or credential-gated feeds were used without explicit permission.

---

## 2. Ingested Sources Catalog

### 2.1. AlienVault Open Threat Exchange (OTX) / IP Reputation Feed
* **Provider:** AT&T Cybersecurity / AlienVault
* **Feed Endpoint:** `https://reputation.alienvault.com/reputation.data`
* **Portal URL:** [https://otx.alienvault.com/](https://otx.alienvault.com/)
* **Indicator Types Collected:** Malicious IPv4 addresses (`ipv4`)
* **Collection Protocol:** Automated HTTP GET over TLS using anonymous academic research user-agent.
* **Provided Metadata:** IP Address, Risk Score (1–10), Reliability Score (1–10), Malicious Activity Category (e.g., Scanning Host, Spamming, Malicious Host), Country Code, City.
* **Usage & Licensing:** AlienVault terms allow public security research and non-commercial defensive correlation.
* **Role in Capstone:** Enables the **Triage Agent** and **Investigation Agent** to cross-reference incoming security log source IPs against active malicious scanners and brute-force actors.

---

### 2.2. TweetFeed (Live Infosec Community Threat Tracker)
* **Maintainer / Creator:** Daniel López ([@0xDanielLopez](https://x.com/0xDanielLopez))
* **Feed Endpoint:** `https://raw.githubusercontent.com/0xDanielLopez/TweetFeed/master/week.csv`
* **Portal URL:** [https://tweetfeed.live/](https://tweetfeed.live/)
* **Indicator Types Collected:** 
  - Malicious Domains (`domain`)
  - Malicious URLs (`url`)
  - Cryptographic File Hashes (`sha256`, `md5`)
  - Command & Control IPs (`ipv4`)
* **Collection Protocol:** Direct ingestion of the weekly verified community aggregation stream.
* **Attributed Researchers:** Community infosec analysts sharing real-time IoCs (e.g., `@TKemmerling`, `@masaomi346`, `@ThreatInsight`, `@siri_urz`).
* **Provided Metadata:** Observation timestamp, Reporting handle, IoC classification, Target IoC value, Malware/Threat tags (e.g., `#phishing`, `#malware`, `#AgentTesla`, `#RedLine`, `#LockBit`), Original tweet verification URL.
* **Usage & Licensing:** Open Source / Community Attribution.
* **Role in Capstone:** Provides high-recency indicators to simulate the **Investigation Agent's** automated IoC expansion and assists the **Trust Agent** in evaluating file hash integrity against active malware campaigns.

---

### 2.3. Feodo Tracker & abuse.ch Community Feeds
* **Provider:** abuse.ch (Bern University of Applied Sciences / Cyber Defense project)
* **Endpoints Evaluated:**
  - `https://feodotracker.abuse.ch/downloads/ipblocklist.txt` (Botnet C2 IP Blocklist)
  - `https://sslbl.abuse.ch/blacklist/sslblacklist.csv` (Malicious SSL Certificate SHA-1 fingerprints)
* **Indicator Types:** Botnet C2 IPv4 addresses, Malicious SSL/TLS certificate SHA-1 hashes.
* **Usage Terms:** Free for defensive cybersecurity usage and academic research.
* **Role in Capstone:** Used to flag Command-and-Control channels during lateral movement and persistent connection identification.

---

### 2.4. Internet Cyber Health Index (ICHI) [Macro Context]
* **Portal URL:** [https://ichi.global](https://ichi.global)
* **Description:** As noted in Issue #16 discussion, ICHI provides a composite 0–100 cyber health score derived from CISA KEV, EPSS exploitation rates, and global active C2 density.
* **Usage Distinction:** While individual IoCs in `iocs.csv` / `iocs.json` represent micro-level indicators ("Is this hash malicious?"), ICHI serves as an environmental baseline metric ("Is global exploitation activity currently elevated?").

---

## 3. Data Safety and Defanging Policy

To prevent inadvertent weaponization, automated browsing, or accidental URL execution:
1. **Domains:** All dots (`.`) are defanged with square brackets, e.g., `malicious-domain[.]com`.
2. **URLs:** Protocols and dots are replaced with harmless representations, e.g., `hxxp://` and `[.]`.
3. **Execution Safety:** Under no circumstances are live binaries downloaded or malicious infrastructure connected to. This dataset operates purely on passive metadata.

---

## 4. Verification and Reproducibility

Any team member can reproduce and verify this dataset by running the reproducible collection script:
```powershell
python threat-intelligence/collect_threat_intel.py
```
This guarantees complete end-to-end auditability and compliance with project engineering guidelines.
