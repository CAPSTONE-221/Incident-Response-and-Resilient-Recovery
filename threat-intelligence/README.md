# Curated Threat Intelligence IOC Dataset

**Project:** Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery  
**Team ID:** 221 (Capstone Project Phase-I)  
**Author:** Aditya Basavaraj Jambagi (Aditya BJ)  
**Assigned Issue:** [Issue #16 – Collect and Organize Threat Intelligence Sources](https://github.com/CAPSTONE-221/Incident-Response-and-Resilient-Recovery/issues/16)  
**Dataset Location:** `threat-intelligence/` (Repository Root)

---

## 1. Motivation & Relevance to Capstone Framework

In our proposed **Trust-Aware Agentic AI** architecture, resilient recovery relies on making informed, evidence-grounded decisions rather than blind rollbacks. Unsafe recovery occurs when incident responders unknowingly restore backups that already harbor persistent backdoors, droppers, or active Command & Control (C2) configurations.

This dataset provides the essential telemetry and Indicators of Compromise (IOCs) needed by our multi-agent framework:

1. **Triage Agent:** Correlates incoming network logs, DNS lookups, and firewall events against known malicious IPs and domains in sub-second triage passes.
2. **Investigation Agent:** Leverages domain and URL threat types to trace the attacker's initial access vector, reconstruct lateral movement chains, and assess adversary footprint.
3. **Trust Agent (RTS Calculator):** Evaluates candidate recovery point safety. Specifically, the Threat-Free Confidence metric ($T$) is calculated by scanning file hash states across recovery points against the malicious file hashes (SHA-256 and MD5) present in this dataset.
4. **Validation Agent:** Employs post-restore verification rules to ensure that newly provisioned systems do not initiate outbound connections to blacklisted C2 IP addresses.

---

## 2. Dataset Structure and Inventory

The dataset is organized consistently across both structured tabular (CSV) and semi-structured (JSON) representations, governed by a strict JSON schema:

| File Name | Format | Description |
|---|---|---|
| [`iocs.csv`](iocs.csv) | CSV (UTF-8) | Clean, normalized tabular dataset with standard headers. |
| [`iocs.json`](iocs.json) | JSON (UTF-8) | Complete dataset including audit metadata, source distributions, and record arrays. |
| [`schema.json`](schema.json) | JSON Schema | Draft-07 compliant formal data definition and validation schema. |
| [`sources.md`](sources.md) | Markdown | Attribution records, upstream licensing terms, and access endpoints. |
| [`README.md`](README.md) | Markdown | Comprehensive dataset documentation, methodology, and usage guide. |

---

## 3. Indicator Distribution Summary

* **Total Validated Unique Indicators:** 805 records
* **Deduplication Rate:** 36 duplicate entries safely removed
* **Format Regex Pass Rate:** 100%

### Breakdown by Indicator Type
* **Malicious URLs (`url`):** 311 (defanged `hxxp://` and `[.]`)
* **Malicious Domains (`domain`):** 220 (defanged `[.]`)
* **Malicious IPv4 Addresses (`ipv4`):** 155 (strictly validated quad-dotted format)
* **Cryptographic Hashes (SHA-256):** 100 (64-character hexadecimal)
* **Cryptographic Hashes (MD5):** 19 (32-character hexadecimal)

### Breakdown by Threat Intelligence Source
* **TweetFeed (Security Researcher Feeds):** 725 indicators
* **AlienVault OTX (IP Reputation Feed):** 80 indicators

---

## 4. Schema & Field Definitions

Each record conforms to the following standardized fields:

1. `indicator`: The actual IoC value. Domains and URLs are stored in defanged format (e.g., `example[.]com`, `hxxp://bad[.]site`) to prevent accidental clicks.
2. `indicator_type`: The category of the indicator (`ipv4`, `domain`, `url`, `sha256`, `md5`).
3. `source_name`: The authoritative intelligence provider or feed name.
4. `source_url`: Link to the upstream source repository or feed homepage.
5. `source_record_id`: Upstream tracking ID, tweet ID, or report reference if provided.
6. `first_seen`: Timestamp when the indicator was first identified by the threat feed.
7. `last_seen`: Timestamp when activity was last verified (left empty if omitted by source).
8. `collection_timestamp_utc`: Standardized ISO 8601 UTC timestamp of ingestion.
9. `confidence`: Provider-assigned confidence score or reliability classification.
10. `threat_type`: Categorization of threat activity (e.g., `phishing`, `malware_distribution`, `botnet_c2`, `scanning_host`).
11. `malware_family`: Associated threat actor or malware strain (e.g., `AgentTesla`, `RedLine`, `LockBit`, `CobaltStrike`).
12. `tags`: Additional classification metadata, port numbers, or researcher hashtags.
13. `description`: Human-readable summary providing forensic context and analysis details.

---

## 5. Defensive Safety and Ethical Compliance

This repository enforces strict defensive cyber safety principles:
* **No Live Attack Tools:** No exploit payloads, droppers, or active malware samples are included or downloaded.
* **Passive Defanging:** All indicators that could trigger automated link resolution in web browsers or markdown viewers are defanged with square brackets.
* **Privacy & Attribution:** No personal identifying information (PII) or confidential credentials are contained in the dataset. All upstream community researchers are credited in accordance with OSINT standards.

---

## 6. How to Reproduce and Verify

To verify file validity and reproduce the dataset collection pipeline:

```powershell
# Verify parsing of both JSON and CSV files
python -c "
import json, csv
with open('iocs.json', encoding='utf-8') as f:
    j = json.load(f)
with open('iocs.csv', encoding='utf-8') as f:
    c = list(csv.DictReader(f))
assert len(j['indicators']) == len(c), 'Record count mismatch!'
print(f'Verification passed: {len(c)} matching records.')
"
```
