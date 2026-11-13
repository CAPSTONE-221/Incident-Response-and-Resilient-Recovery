# MITRE ATT&CK Enterprise STIX 2.1 Dataset

## Overview
This directory contains the machine-readable STIX 2.1 bundle for the MITRE ATT&CK Enterprise Matrix. It serves as the primary cyber threat intelligence (CTI) grounding database for the multi-agent system.

- **Source**: MITRE Corporation
- **Format**: JSON (STIX 2.1 standard)
- **File**: `enterprise-attack.json` (~52.7 MB)
- **Total Objects**: 26,699 STIX objects

## Key STIX Object Counts
- `attack-pattern` (Techniques & Sub-techniques): 867
- `course-of-action` (Mitigations & Responses): 268
- `malware` (Malware Families): 750
- `tool` (Attacker Tools): 95
- `intrusion-set` (Threat Actor / APT Groups): 193
- `relationship` (Mappings between TTPs, groups, mitigations): 21,822

## Role in the Project
1. **CTI Agent**: Queries techniques and adversary threat profiles based on extracted IOCs and alerts.
2. **Investigation Agent**: Maps raw telemetry events to ATT&CK Technique IDs to build attack chains.
3. **Response Planner Agent**: Queries `course-of-action` objects to recommend defensible containment actions.
4. **Attacker Simulation / Lookahead**: Used by the lookahead validation module to predict next likely adversary moves based on ATT&CK relationship graphs.

## Verification
Run:
```bash
python datasets/scripts/fetch_mitre_stix.py
```
