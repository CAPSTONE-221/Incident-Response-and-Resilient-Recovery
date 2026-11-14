# Research Summary

> **Working document.** The entries below are structured research notes based on the source list assembled for the project. They are not a substitute for reading the full text. Verify exact methods, datasets, metrics, and limitations in each original publication before using them as definitive claims.

## 1. IRCopilot: Automated Incident Response with Large Language Models

- **Authors:** Xihuan Lin et al. (verify complete author list in the paper)
- **Year/source:** 2025, arXiv preprint
- **URL:** https://arxiv.org/abs/2505.20945
- **Problem:** Applying large language models to automate or assist incident-response workflows.
- **Approach noted in the project source list:** Collaborative LLM-based components for response reasoning and action.
- **Relevance:** Provides a baseline for agentic incident response and motivates a system that constrains proposed actions using independently evaluated evidence and policies.
- **Limitations/gaps to verify in full text:** Whether it validates backup/recovery-point integrity; whether execution is independently authorised; whether service dependencies are modelled during recovery; how hallucination and unsafe actions are measured.

## 2. Incident Response Planning Using a Lightweight Large Language Model with Reduced Hallucination

- **Authors:** Kim Hammar, Tansu Alpcan, Emil C. Lupu
- **Year/source:** 2026, NDSS publication; an earlier 2025 arXiv version exists.
- **URL:** https://www.ndss-symposium.org/ndss-paper/incident-response-planning-using-a-lightweight-large-language-model-with-reduced-hallucination/
- **Problem:** Improving LLM-generated incident-response plans while reducing hallucinations.
- **Approach noted in the source:** Lightweight model adaptation, retrieval, and lookahead planning. Verify exact experimental design in the final paper.
- **Relevance:** Informs planning quality and the use of retrieved threat intelligence.
- **Limitations/gaps to verify:** Whether reduced hallucination is paired with deterministic execution authorisation; whether recovery points are independently scored for trust; whether restoration dependencies are explicitly modelled.

## 3. In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach

- **Authors:** Yiran Gao, Kim Hammar, Tao Li
- **Year/source:** 2026, arXiv
- **URL:** https://arxiv.org/abs/2602.13156
- **Problem:** End-to-end autonomous response to network incidents.
- **Approach noted in the source:** LLM agent functions spanning perception, reasoning, planning, and action.
- **Relevance:** Helps frame the agent workflow and the interface between detection, planning, and action.
- **Limitations/gaps to verify:** Applicability to post-compromise recovery; backup contamination assessment; trust-ranked recovery-point selection; dependency-aware restoration and post-recovery validation.

## 4. From Backup Restoration to Minimum Viable Factory Recovery: A Systematization of Ransomware Recovery in Manufacturing Systems

- **Author:** Chun Yin Chiu
- **Year/source:** 2026, *International Journal of Critical Infrastructure Protection* (verify final issue metadata).
- **URL:** https://www.sciencedirect.com/science/article/pii/S1874548226000545
- **DOI:** https://doi.org/10.1016/j.ijcip.2026.100882
- **Problem:** Understanding ransomware recovery in manufacturing systems beyond restoring backups.
- **Approach noted in the source:** Systematisation of recovery concerns in manufacturing and critical infrastructure.
- **Relevance:** Strongly relevant to dependency-aware recovery, backup trust, identity compromise, and safe return to operation.
- **Limitations/gaps to verify:** Whether the work proposes an implemented quantitative trust score, an automated agentic planner, or an experimentally evaluated policy gate.

## 5. Time-Scale Reconfiguration for Ransomware Mitigation by Delaying Encryption Progress

- **Authors:** Kosuke Higuchi and Ryotaro Kobayashi
- **Year/source:** 2026, IEEE Access (verify final bibliographic metadata).
- **DOI:** https://doi.org/10.1109/ACCESS.2026.3692203
- **Problem:** Reducing ransomware damage by delaying encryption progress relative to backup operations.
- **Approach noted in the source:** System-level scheduling and resource-control mechanisms; verify the precise use of eBPF and other mechanisms in the paper.
- **Relevance:** Supports the importance of backup protection and timing during ransomware incidents.
- **Limitations/gaps to verify:** Whether the work addresses post-incident recovery-point trust, evidence fusion, recovery ordering, or safe restoration.

## 6. Do You Play It by the Books? A Study on Incident Response Playbooks and Influencing Factors

- **Authors:** Daniel Schlette, Philip Empl, Marco Caselli, Thomas Schreck, Günther Pernul
- **Year/source:** 2024, IEEE Symposium on Security and Privacy.
- **DOI:** https://doi.org/10.1109/SP54263.2024.00060
- **URL:** https://ieeexplore.ieee.org/abstract/document/10646756
- **Problem:** Understanding incident-response playbooks and the factors that influence their use.
- **Approach noted in the source:** Empirical study of playbooks and practitioner perspectives; verify sample sizes and methodology in the paper.
- **Relevance:** Helps motivate structured, auditable response procedures.
- **Limitations/gaps to verify:** Whether playbooks adapt dynamically to evidence, quantify recovery trust, or validate recovery-point safety.

## 7. Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence

- **Authors:** Verify against the IEEE publisher record before final citation.
- **Year/source:** 2025, IEEE GLOBECOM.
- **DOI:** https://doi.org/10.1109/GLOBECOM59602.2025.11432623
- **URL:** https://ieeexplore.ieee.org/abstract/document/11432623
- **Problem:** Using cyber threat intelligence to improve LLM-supported incident response.
- **Approach noted in the source:** CTI retrieval and LLM-supported response generation; verify architecture and evaluation in the full paper.
- **Relevance:** Connects threat-intelligence evidence with response planning.
- **Limitations/gaps to verify:** Whether CTI is connected to recovery-point trust, integrity validation, dependency-aware restoration, and policy-controlled execution.

## 8. CIPHER-A: An Adaptive Agentic AI Framework for Counterfactual Validation and Adversarial Lookahead in Automated Incident Response

- **Authors:** Verify against the Springer publisher record.
- **Year/source:** 2026, Springer publication.
- **DOI:** https://doi.org/10.1007/s44163-026-02058-6
- **URL:** https://link.springer.com/article/10.1007/s44163-026-02058-6
- **Problem/approach:** The title and publisher record indicate agentic incident response with counterfactual validation and adversarial lookahead. Read the full paper before describing its implementation or results.
- **Relevance:** Potentially informs action validation and adversarial planning.
- **Limitations/gaps to verify:** Whether it assesses backup trust, recovery-point integrity, and dependency-aware restoration.

## 9. A Trustworthiness Assessment for Software Based on Multi-Source Evidence Fusion

- **Authors:** Verify against the publisher record.
- **Year/source:** 2026 publication record; verify issue year and article metadata.
- **DOI:** https://doi.org/10.1016/j.ress.2025.111842
- **URL:** https://www.sciencedirect.com/science/article/pii/S0951832025010427
- **Problem/approach:** Trustworthiness assessment using evidence from multiple sources. Confirm the specific evidence-fusion method and evaluation in the full text.
- **Relevance:** May inform the design of a Recovery Trust Score that combines independent evidence sources.
- **Limitations/gaps to verify:** Domain transfer from software trustworthiness to backup/recovery-point trust; operational integration with an incident-response agent; policy enforcement and recovery validation.

## Standards and non-paper sources

### NIST SP 800-184 — Guide for Cybersecurity Event Recovery
- 2016. https://www.nist.gov/publications/guide-cybersecurity-event-recovery
- Provides guidance relevant to planning, prioritising, and managing cybersecurity event recovery.

### NIST SP 800-61 Rev. 3
- 2025. https://csrc.nist.gov/pubs/sp/800/61/r3/final
- Provides incident-response recommendations aligned with the Cybersecurity Framework 2.0.

### MITRE ATT&CK
- https://attack.mitre.org/
- A knowledge base for describing adversary tactics and techniques; not a recovery trust-scoring standard.

### OASIS STIX 2.1 and TAXII 2.1
- STIX: https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html
- TAXII: https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1.html
- Specifications for representing and exchanging cyber threat intelligence.

### Sophos State of Ransomware 2024
- https://www.sophos.com/en-us/blog/the-state-of-ransomware-2024
- Industry report; verify any statistics against the report itself before quoting.
