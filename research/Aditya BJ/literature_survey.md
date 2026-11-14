# Literature Survey: Resilient Recovery and Intrusion Reconstruction for Cyber Incidents

**Project Title:** Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery  
**Academic Year:** 2026–2027 (Capstone Project Phase-I, Team 221)  
**Author:** Aditya Basavaraj Jambagi (Aditya BJ)  
**Assigned Issue:** [Issue #5 – Research Paper Collection – Aditya BJ](https://github.com/CAPSTONE-221/Incident-Response-and-Resilient-Recovery/issues/5)  
**Repository:** [CAPSTONE-221/Incident-Response-and-Resilient-Recovery](https://github.com/CAPSTONE-221/Incident-Response-and-Resilient-Recovery)  

---

## Abstract

Modern cyber incident response faces a critical failure mode: **contaminated recovery**. Following sophisticated ransomware attacks or stealthy intrusions, automated or human response procedures frequently rely on coarse-grained system rollbacks or newest available backups. If the restored backup was taken *after* initial adversary penetration, malicious implants, persistence mechanisms, and compromised credentials are restored directly into the enterprise production environment. This survey presents an in-depth academic analysis of two foundational research contributions that address complementary dimensions of this challenge:

1. **Paper 1:** *From Backup Restoration to Minimum Viable Factory Recovery: A Systematization of Ransomware Recovery in Manufacturing Systems* by Chun Yin Chiu (published in the *International Journal of Critical Infrastructure Protection*, Vol. 54, 2026, Article 100882). This work establishes that asset rebuilding does not equate to operational recovery and introduces **Minimum Viable Factory Recovery (MVF Recovery)** as a capability-centric, evidence-calibrated objective governed by nine distinct recovery failure modes.
2. **Paper 2:** *ANCORA: Accurate Intrusion Recovery for Web Applications* by Yihao Peng, Biao Ma, Hai Wan, and Xibin Zhao (arXiv v3 preprint, 2 January 2026; accepted to *IEEE Transactions on Dependable and Secure Computing*, DOI: 10.1109/TDSC.2026.3733124). This work develops a surgical, fine-grained intrusion recovery architecture using framework-level delimiter logging, syscall-based provenance tracking, and database spatiotemporal anchoring to isolate malicious requests and selectively replay legitimate concurrent operations.

Together, these works provide vital theoretical framing and low-level recovery mechanisms. We critically evaluate their problem statements, methodologies, findings, and architectural boundaries, demonstrating how our proposed 7-agent Trust-Conditioned Recovery Planning (TCRP) framework builds upon their strengths to resolve their open limitations.

---

## 1. Introduction and Problem Context

### 1.1 The Contaminated Recovery Dilemma
Enterprises experiencing cyber incidents—specifically ransomware outbreaks and multi-stage advanced persistent threats (APTs)—face an existential operational tradeoff:
* **The Rapid Recovery Imperative:** Downtime in industrial manufacturing, critical infrastructure, and high-concurrency web services carries catastrophic financial and safety consequences. Incident responders are heavily incentivized to restore systems from backups as quickly as possible.
* **The Contamination Trap:** The modern dwell time of sophisticated threat actors often extends for days, weeks, or months before destructive payloads are detonated. Consequently, recent automated snapshots, incremental backups, and volume shadow copies frequently capture persistent webshells, privilege escalation hooks, or infected Active Directory registries. Reverting to these restore points inevitably triggers reinfection cycles.

### 1.2 Limitations of Conventional Recovery Paradigms
Current industry approaches fall into two flawed extremes:
1. **Coarse-Grained Snapshot Rollback:** Reverting entire virtual machines or database clusters to arbitrary pre-incident points indiscriminately destroys legitimate user transactions, pending orders, and valid operational states created between the snapshot and the attack disclosure.
2. **Asset-Centric Rebuilding:** IT response teams measure recovery progress purely by the count of operational servers or restored databases without verifying interdependent workflow viability, identity provenance, or operational technology (OT) safety constraints.

To overcome these structural flaws, modern cyber incident response requires **trust-aware autonomous decision making** capable of evaluating recovery point integrity, reconstructing cross-system provenance, and executing capability-centric restoration workflows.

---

## 2. In-Depth Analysis: Paper 1 (Minimum Viable Factory Recovery)

### 2.1 Metadata & Academic Context
* **Title:** *From Backup Restoration to Minimum Viable Factory Recovery: A Systematization of Ransomware Recovery in Manufacturing Systems*
* **Author:** Chun Yin Chiu (King's College London, Department of Informatics)
* **Publication:** *International Journal of Critical Infrastructure Protection* (Elsevier), Volume 54, Article 100882, August 2026.
* **DOI:** [10.1016/j.ijcip.2026.100882](https://doi.org/10.1016/j.ijcip.2026.100882)
* **Academic Nature:** PRISMA-guided Multivocal Review / Systematization of Knowledge (SoK). It is **not** an empirical software tool or autonomous implementation, but an evidence-calibrated conceptual and analytical framework.

### 2.2 Core Problem Addressed
Chiu investigates why industrial manufacturing systems fail to resume production after ransomware attacks even when all encrypted servers and databases have been technically restored from backups. In cyber-physical manufacturing systems (CPMS), production capability depends on tightly coupled interdependencies spanning Information Technology (IT), Operational Technology (OT), Manufacturing Execution Systems (MES), Enterprise Resource Planning (ERP), quality assurance inspection, and external supply chains. Restoring isolated virtual machines fails because the underlying dependency graph, credential trust, and process safety remain corrupted.

### 2.3 Research Methodology
The study conducts a rigorous **PRISMA-guided multivocal review** covering 797 retained academic and grey-literature records (342 core academic records, 427 background records, and 28 primary incident/regulatory filings including Norsk Hydro, Toyota/Kojima, Dole, and Clorox). The methodology employs:
* Strict source-quality rubrics calibrating allowable claim strengths (direct support vs. inferred support).
* Full-text evidence anchoring for all high-impact claims.
* Deduplicated corpus reconciliation across ScienceDirect, IEEE Xplore, ACM DL, Scopus, and PubMed.

### 2.4 Taxonomy of Nine Recovery Failure Modes
The paper's primary contribution is a taxonomy of nine source-supported recovery failure modes organized into four core problem classes:

| Class | Failure Mode ID | Failure Mode Title | Underlying Mechanism |
|---|---|---|---|
| **Dependency Failures** | **FM01** | Dependency Blindness | Treating interdependent systems as isolated assets; restoring MES without verifying identity, historian, or supplier data availability. |
| **Trust & Verification** | **FM02** | Backup Over-Trust | Assuming backups are clean based purely on recency or cryptographic hashes without verifying absence of attacker persistence. |
| | **FM03** | Identity Trust Collapse | Restoring servers into an Active Directory environment where privileged accounts, tokens, and domain trusts remain compromised. |
| | **FM04** | No Proof-of-Recovery | Lack of an auditable forensic evidence bundle demonstrating that restored configurations are clean and safe for restart. |
| **Reintegration Failures** | **FM05** | Unsafe OT Reconnection | Reconnecting IT networks to physical industrial controllers (PLCs, HMIs) before process setpoints and logic configurations are verified. |
| | **FM06** | Segmentation Assumption Failure | Relying on theoretical air-gaps or network diagrams that have been bypassed by maintenance gateways, IIoT, or dual-homed hosts. |
| **Operational Capability** | **FM07** | Capability Mismatch | Restored servers fail to produce valid, releasable physical goods due to broken inspection or packaging dependencies. |
| | **FM08** | Degraded Mode Unmanaged | Operating factories on manual workarounds without explicit safety limits, quality audit trails, or rollback triggers. |
| | **FM09** | Supplier Dependency Failure | Internal factory systems are restored, but operations stall due to external logistics, supply, or shared platform outages. |

### 2.5 The Minimum Viable Factory Recovery (MVF) Construct
Chiu defines **Minimum Viable Factory Recovery (MVF Recovery)** as:
> *"The smallest operationally acceptable, trusted, and meaningful production capability that can be resumed under current dependency, evidence, identity, data, network, OT, quality-release, and supplier constraints."*

Rather than pursuing an unconstrained "all-or-nothing" recovery, MVF models recovery as a multi-stage optimization problem satisfying six simultaneous operational criteria:
$$\text{Production Mission} = f(\text{Dependencies}, \text{Clean State Evidence}, \text{Identity Clean-Room}, \text{OT Gating}, \text{Quality Constraints}, \text{Supply Feasibility})$$

### 2.6 Key Findings and Operational Lifecycle
The paper derives an evidence-informed 8-stage recovery lifecycle:
1. *Mission Impact Assessment*
2. *Dependency Modelling*
3. *Clean-State Selection*
4. *MVF Planning*
5. *Validation and Simulation*
6. *Proof-of-Recovery Compilation*
7. *Staged Reintegration*
8. *Monitored Production Resumption*

### 2.7 Limitations and Critical Assessment
* **No Automated Tooling:** The paper deliberately frames MVF as an analytical decision-support construct. It does not provide an automated recovery orchestration engine, CLI tool, or executable software artifact.
* **Empirical Validation Gap:** The taxonomy and lifecycle are derived from literature synthesis and post-incident disclosures; they require independent empirical validation in live testbeds.
* **Single-Author Coding:** Although calibrated with structured consistency checks, the systematic review did not incorporate multi-rater inter-coder reliability metrics.

---

## 3. In-Depth Analysis: Paper 2 (ANCORA Intrusion Recovery)

### 3.1 Metadata & Academic Context
* **Title:** *ANCORA: Accurate Intrusion Recovery for Web Applications*
* **Authors:** Yihao Peng, Biao Ma, Hai Wan, and Xibin Zhao (Tsinghua University, Beijing, China)
* **Publication Track:** Accepted for publication in *IEEE Transactions on Dependable and Secure Computing* (IEEE TDSC), DOI: [10.1109/TDSC.2026.3733124](https://doi.org/10.1109/TDSC.2026.3733124).
* **Document Version Analyzed:** arXiv preprint v3, dated 2 January 2026 (arXiv:2510.07806v3 [cs.CR]).
* **Artifact Availability:** Open-source prototype released at [https://github.com/ma-b21/Ancora](https://github.com/ma-b21/Ancora).

### 3.2 Core Problem Addressed
In modern high-concurrency web applications, executing surgical intrusion recovery requires attributing every file and database mutation to the specific HTTP request that caused it. However, high-throughput web architectures introduce severe attribution obstacles:
1. **The Database Correlation Challenge:** Web applications employ connection pooling where multiple independent HTTP requests reuse persistent database TCP connections. Simultaneously, database engines handle I/O asynchronously across worker threads, creating an ambiguous many-to-many interleaved event stream.
2. **The File Correlation Challenge:** Exploits involving Remote Code Execution (RCE) or arbitrary file upload frequently spawn out-of-band descendant processes (e.g., `/bin/sh`, `curl`, `base64`) that write webshells to unpredictable file paths, bypassing application-level frameworks entirely.
3. **Black-Box Failure:** Previous state-of-the-art approaches like SANARE (TDSC 2023) rely on machine learning over event time-windows; under high concurrency (>50 connections), inter-request crosstalk degrades their recovery accuracy to below 30%.

### 3.3 System Architecture and Technical Innovations
ANCORA achieves precise intrusion recovery without invasive runtime modification through three integrated stages:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ANCORA THREE-STAGE WORKFLOW                     │
│                                                                        │
│  [ Malicious Request ]                                                 │
│           │                                                            │
│  ┌────────▼─────────────────────────────────────────────────────────┐  │
│  │ STAGE 1: Request Partition                                       │  │
│  │ Framework-level Delimiter Logging + Sysdig Event Stream Tracing  │  │
│  └────────┬─────────────────────────────────────────────────────────┘  │
│           │ Isolates Dedicated Syscall Sequence                        │
│           ├───────────────────────────────────┐                        │
│  ┌────────▼───────────────────────┐  ┌────────▼─────────────────────┐  │
│  │ STAGE 2: File System Recovery  │  │ STAGE 3: Database Recovery   │  │
│  │ • Syscall Provenance Graph     │  │ • Spatiotemporal Anchoring   │  │
│  │   (fork/clone/openat/write)    │  │   (4-tuple + Time Window)    │  │
│  │ • Differentiated Rewind/Replay │  │ • Pinpoint Worker TID & Logs │  │
│  │   - Baseline for System Dirs   │  │ • Snapshot Rollback + Filter │  │
│  │   - Write-Log Replay for Data  │  │   + Chronological Replay     │  │
│  └────────┬───────────────────────┘  └────────┬─────────────────────┘  │
│           │                                   │                        │
│           └─────────────────┬─────────────────┘                        │
│                             ▼                                          │
│                 [ Clean System State ]                                 │
└────────────────────────────────────────────────────────────────────────┘
```

#### A. Deterministic Request Partitioning
Lightweight, application-agnostic delimiters containing a unique request UUID are injected at web framework boundaries (via Python monkey-patching, Node.js `async_hooks`, or Java Agents). The log parser processes Sysdig audit logs to isolate the exact syscall sequence of the malicious request without application rewrites.

#### B. Provenance-Based File Tracking
Instead of passively monitoring static directories, ANCORA constructs an active causal provenance graph from process creation syscalls (`clone`, `fork`, `execve`). It recursively traces descendant processes, exposing webshell writes across any directory on disk. For data directories, a kernel module captures write payloads to enable granular replay; for system directories, it rolls back to immutable container or VM baselines.

#### C. Database Spatiotemporal Anchoring
To overcome connection pooling, ANCORA identifies a deterministic mathematical invariant:
* A web request borrows a connection exclusively for the duration of its query sequence $[T_{\text{start}}, T_{\text{end}}]$.
* The database assigns that specific TCP 4-tuple (`SrcIP:SrcPort -> DstIP:DstPort`) to an exclusive worker thread ID (TID).
By combining the network 4-tuple with the active time window, ANCORA pins down the exact worker thread in database audit logs, extracting only the malicious SQL/NoSQL statements while preserving concurrent legitimate transactions.

### 3.4 Experimental Findings and Reported Results
ANCORA was evaluated across 10 diverse web applications (Django, FastAPI, pgAdmin, Joomla, CMS Made Simple, Gitlist, Solr, OFBiz, Mongo-Express, GeoServer) covering 4 languages (Python, PHP, Java, Node.js), 3 database engines (MySQL, PostgreSQL, MongoDB), and 20 real-world CVE vulnerabilities under concurrency loads up to 150 Locust users:
* **Attribution Accuracy:** Achieved **99.9% F1-score** across all concurrency levels, whereas baseline SANARE collapsed from 74.37% at concurrency 1 to 24.18% at concurrency 150.
* **Malicious Operation Matching:** Achieved **1.000 F1-score** across 17 real-world RCE attack scenarios, whereas SANARE scored 0.000 due to inability to track forked subprocesses.
* **Runtime Overhead:** Manageable overhead with average response latency increase of 3.5%–4.9% (up to 19.8% in worst-case I/O-heavy CMSMS) and throughput decrease of 3.0%–6.3% (max 17.8%).
* **Recovery Throughput:** Sustained recovery speeds of **110.7 database operations/sec** and **27.2 files/sec**.

### 3.5 Critical Limitations
* **Database Proxy Incompatibility:** Spatiotemporal anchoring breaks if connection pooling proxies (e.g., ProxySQL) or advanced multi-threaded multiplexing decouple the one-to-one TCP connection-to-thread mapping.
* **External State Irreversibility:** External web service interactions (e.g., payment gateway APIs, external cloud webhooks) are captured as network syscalls but cannot be automatically rolled back; they require manual compensatory transactions.
* **Middleware State Blindness:** Volatile in-memory state stores such as Redis caches and Kafka message queues are outside ANCORA's recovery boundary.

---

## 4. Deep Comparative Synthesis

The following structured matrix compares both research works across critical technical dimensions:

| Dimension | Paper 1: Minimum Viable Factory Recovery (Chiu 2026) | Paper 2: ANCORA Intrusion Recovery (Peng et al. 2026) |
|---|---|---|
| **Author & Institution** | Chun Yin Chiu, King's College London | Yihao Peng, Biao Ma, Hai Wan, Xibin Zhao, Tsinghua University |
| **Publication Venue** | *Int. Journal of Critical Infrastructure Protection*, Vol. 54 | arXiv v3 preprint (Accepted to *IEEE TDSC*) |
| **System Classification** | PRISMA-guided Multivocal Review / SoK Framework | Empirical System Architecture & Experimental Prototype |
| **Target Infrastructure** | Industrial Manufacturing & Coupled IT/OT Networks | High-Concurrency Web Applications (Linux, Containerized) |
| **Core Recovery Philosophy** | Capability-centric, dependency-aware constrained restart | Surgical "Rewind & Selective Replay" of internal state |
| **State Scope** | Cyber-physical: MES, ERP, PLCs, safety, identity, suppliers | Digital state: Linux filesystem, relational & NoSQL databases |
| **Primary Mechanism** | Multi-criteria dependency graph & proof-of-recovery bundle | Syscall provenance graphs & database spatiotemporal anchoring |
| **Handling of Concurrency** | Focuses on multi-stakeholder and supply-chain concurrency | Solves multi-client TCP connection pooling and async worker TIDs |
| **Handling of Identity** | Formally models Identity Trust Collapse (FM03) clean-rooms | Assumes trusted administrative boundary (TCB) |
| **Handling of Backups** | Warns against Backup Over-Trust (FM02); mandates evidence | Relies on standard periodic snapshots + incremental rsync |
| **Reported Performance** | Qualitative operational metrics, lifecycle benchmarking blueprint | 99.9% accuracy; max 19.8% latency overhead; 110.7 ops/s recovery |
| **Open Source Artifact** | Systematic review audit registers and search protocols | Full source code available on GitHub (`ma-b21/Ancora`) |

---

## 5. Direct Contribution to Capstone Architecture

Our Capstone project, **Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery**, directly integrates and advances the insights from both papers.

```
┌───────────────────────────────────────────────────────────────────────────┐
│                    CAPSTONE 7-AGENT INTEGRATION MAPPING                   │
├────────────────────────────────┬──────────────────────────────────────────┤
│ Capstone Agent / Construct     │ Theoretical & Technical Grounding        │
├────────────────────────────────┼──────────────────────────────────────────┤
│ 1. Triage Agent                │ ANCORA Stage 1 (Delimiter log isolation) │
│ 2. Investigation Agent         │ ANCORA Stage 2 (Syscall provenance DAGs) │
│ 3. Trust Agent (RTS Engine)    │ Chiu FM02 (Backup Over-Trust prevention) │
│ 4. Response Planner            │ Chiu FM05/FM06 (OT/Network containment)  │
│ 5. Recovery Planner (TCRP)     │ Chiu MVF (Topological dependency DAGs)   │
│ 6. Execution Agent             │ ANCORA Rewind & Replay + Human Gate      │
│ 7. Validation Agent            │ Chiu FM04 (Proof-of-Recovery evidence)   │
└────────────────────────────────┴──────────────────────────────────────────┘
```

### 5.1 Formulation of the Recovery Trust Score (RTS)
Chiu's paper establishes that assuming backups are clean based on recency alone leads directly to **FM02 (Untrusted Restore Point & Backup Over-Trust)**. To mathematically eliminate this failure mode, our **Trust Agent** computes the Recovery Trust Score (RTS):
$$\text{BaseTrust} = w_1 \cdot I + w_2 \cdot V + w_3 \cdot T + w_4 \cdot F$$
$$\text{RTS} = \text{BaseTrust} \times (1 - R)$$

* **$I$ (Integrity):** Cryptographic hash and filesystem consistency checks.
* **$V$ (Temporal Validity):** Ensures the recovery point predates the adversary's initial compromise timestamp as reconstructed by the Investigation Agent.
* **$T$ (Threat-Free Confidence):** Scans against our curated IOC threat intelligence dataset (Issue #16).
* **$F$ (Forensic Provenance):** Directly implements Chiu's requirement for an auditable evidence chain.
* **$R$ (Reinfection Risk):** Multiplicative penalty gate reflecting credential compromise (Chiu's **FM03 Identity Trust Collapse**) or compromised backup servers.

### 5.2 Beyond Single-Host Rewind: Dependency-Aware Recovery Planning
While ANCORA provides surgical rewind and replay for a single web and database tier, modern enterprise recovery involves multi-tier services. If a database is restored before the Active Directory identity provider is online, authentication fails.

Our **Recovery Planner** adopts Chiu's Minimum Viable Factory paradigm by executing **Trust-Conditioned Recovery Planning (TCRP)** over a topological service dependency DAG (`service_dependency_dag.json`):
$$\text{SVC\_AUTH\_AD} \longrightarrow \text{SVC\_CORE\_DB} \longrightarrow \text{SVC\_BACKEND\_API} \longrightarrow \text{SVC\_WEB\_FRONTEND}$$

### 5.3 Proof-of-Recovery and Validation Gate
ANCORA does not provide formal post-recovery health validation. In our architecture, the **Validation Agent** implements Chiu's **Stage 6 (Proof-of-Recovery)** and **FM04** prevention by conducting automated memory integrity checks (using Volatility/CIC-MalMem models) and verifying that restored processes do not initiate connections to blacklisted threat intelligence C2 nodes before authorizing traffic restoration.

---

## 6. References (IEEE Style)

[1] C. Y. Chiu, "From backup restoration to Minimum Viable Factory Recovery: A systematization of ransomware recovery in manufacturing systems," *International Journal of Critical Infrastructure Protection*, vol. 54, art. no. 100882, Aug. 2026, doi: 10.1016/j.ijcip.2026.100882.

[2] Y. Peng, B. Ma, H. Wan, and X. Zhao, "ANCORA: Accurate Intrusion Recovery for Web Applications," *arXiv preprint arXiv:2510.07806v3*, Jan. 2026. [Online]. Available: https://arxiv.org/abs/2510.07806 (Accepted for publication in *IEEE Transactions on Dependable and Secure Computing*, doi: 10.1109/TDSC.2026.3733124).

[3] D. R. Matos, M. L. Pardal, and M. Correia, "SANARE: Pluggable intrusion recovery for web applications," *IEEE Transactions on Dependable and Secure Computing*, vol. 20, no. 1, pp. 590–605, Jan.–Feb. 2023, doi: 10.1109/TDSC.2021.3138856.

[4] A. Staves, T. Anderson, A. Balderstone, B. Green, A. Gouglidis, and D. Hutchison, "A cyber incident response and recovery framework to support operators of industrial control systems," *International Journal of Critical Infrastructure Protection*, vol. 37, art. no. 100505, Jun. 2022, doi: 10.1016/j.ijcip.2022.100505.

[5] J. Dafoe, N. Chen, B. Chen, and Z. Wang, "Enabling per-file data recovery from ransomware attacks via file system forensics and flash translation layer data extraction," *Cybersecurity*, vol. 7, art. no. 75, Dec. 2024, doi: 10.1186/s42400-024-00287-9.

[6] R. Chandra, T. Kim, M. Shah, N. Narula, and N. Zeldovich, "Intrusion recovery for database-backed web applications," in *Proc. 23rd ACM Symp. Operating Systems Principles (SOSP)*, Cascais, Portugal, 2011, pp. 101–114.

[7] National Institute of Standards and Technology, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*, NIST Special Publication 800-61 Rev. 3, 2025.

[8] Cybersecurity and Infrastructure Security Agency, *#StopRansomware Guide*, CISA, Multi-State Information Sharing and Analysis Center (MS-ISAC), 2023. [Online]. Available: https://www.cisa.gov/stopransomware/ransomware-guide.
