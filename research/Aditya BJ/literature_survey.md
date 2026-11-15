# CAPSTONE PROJECT | LITERATURE SURVEY — PROJECT ID 221
## Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery

| Field | Details | Field | Details |
| :--- | :--- | :--- | :--- |
| **Project ID** | 221 | **Course** | UE24CS320A – Capstone Project |
| **Review** | Phase-I · Review-2 | **Institution** | PES University |
| **Project Guide** | Dr. Geetha Dayalan | **Survey Focus** | Resilient Ransomware Recovery, Intrusion Provenance, and Trust-Aware Backups |
| **Prepared by** | Aditya Basavaraj Jambagi | **SRN** | PES2UG24CS030 |

---

### Scope of This Survey

This survey conducts an in-depth academic investigation of two foundational research contributions that address the critical problem of **contaminated recovery** in cyber incident response. The primary failure mode of contemporary incident response occurs when systems restored from standard backups or VM snapshots inadvertently reinstate pre-existing malware implants, persistent webshells, or backdoors planted during the attacker's dwell time. 

The two papers reviewed provide complementary insights:
1. **Paper 1 (Chiu, Elsevier IJCIP 2026):** Systematizes manufacturing ransomware recovery, formalizing why naive backup restoration fails due to cross-system interdependencies and defining *Minimum Viable Factory Recovery (MVF)* under nine structural failure modes.
2. **Paper 2 (Peng et al., arXiv v3 Preprint 2026 / IEEE TDSC):** Proposes *ANCORA*, a surgical intrusion recovery system that leverages framework delimiter logging, syscall provenance tracking, and database spatiotemporal anchoring to isolate intrusions and selectively replay legitimate operations without blunt rollbacks.

Both papers are analyzed using a rigorous structured framework: Problem Addressed, Proposed Methodology, Technologies and Techniques Used, Key Findings and Reported Results, Limitations, Relevance to Our Capstone Project, and Conclusion. This is followed by a comparative analysis, identification of unresolved research gaps, mapping to our proposed 7-agent architecture, and IEEE-formatted references.

---

# Paper 1 · Systematizing Ransomware Recovery & Minimum Viable Factory Recovery

### Research Paper Under Review
* **Title:** *From Backup Restoration to Minimum Viable Factory Recovery: A Systematization of Ransomware Recovery in Manufacturing Systems*
* **Author:** Chun Yin Chiu (Department of Informatics, King's College London, UK)
* **Publication:** *International Journal of Critical Infrastructure Protection* (Elsevier), Volume 54, Article 100882, August 2026
* **DOI:** [10.1016/j.ijcip.2026.100882](https://doi.org/10.1016/j.ijcip.2026.100882)
* **Nature of Contribution:** Systematization of Knowledge (SoK) / Multi-vocal Literature Review. *(Explicit Note: This is an evidence-calibrated conceptual and analytical framework based on PRISMA guidelines; it is not an empirical software tool or autonomous agent implementation).*

---

### 1. Problem Addressed
Industrial cyber-physical manufacturing systems (CPMS) increasingly suffer high-impact ransomware attacks. Standard incident response frameworks assume that operational recovery is synonymous with restoring IT servers and databases from recent backups. However, real-world case studies (e.g., Norsk Hydro, Colonial Pipeline, JBS) demonstrate that even after IT teams declare backups "restored," factories remain shut down for weeks or months. 

Chiu investigates the structural disconnect between technical data restoration and operational system resumption. In modern manufacturing, production workflows depend on tightly coupled, cross-domain dependencies spanning Enterprise Resource Planning (ERP), Manufacturing Execution Systems (MES), Supervisory Control and Data Acquisition (SCADA), Programmable Logic Controllers (PLCs), quality assurance inspection, and supply-chain electronic data interchange (EDI). Restoring isolated disk snapshots fails because the operational sequence, physical machine state, process synchronization, and trust boundaries have been desynchronized or corrupted.

---

### 2. Proposed Methodology
Chiu adopts the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) methodology to construct an evidence-calibrated taxonomy:
1. **Multivocal Literature Synthesis:** Integrates academic cybersecurity databases (IEEE Xplore, ACM DL, ScienceDirect, SpringerLink) with practitioner post-incident technical reports, forensic disclosures, and industrial disaster recovery guides.
2. **Failure Mode Categorization:** Classifies historical recovery breakdowns into three structural tiers:
   - *Technical Tier:* Backup destruction, hypervisor infection, firmware corruption, and contaminated restoration.
   - *Operational Tier:* Workflow desynchronization, recipe data corruption, safety-interlock mismatches, and physical equipment damage.
   - *Organizational Tier:* Cryptographic key loss, vendor dependency delays, and regulatory verification bottlenecks.
3. **Construction of the MVF Construct:** Establishes the *Minimum Viable Factory Recovery (MVF)* model, shifting recovery objectives from full-stack restoration to an evidence-grounded, staged resumption of safety-critical core throughput.

---

### 3. Technologies and Techniques Used
* **PRISMA Review Protocol:** Systematic identification, screening, eligibility, and inclusion of academic literature and grey-literature incident reports.
* **ISA-95 / Purdue Enterprise Reference Architecture (PERA):** Structural mapping of recovery dependencies across Level 0/1 (field devices, PLCs), Level 2 (SCADA/HMI), Level 3 (MES/historians), and Level 4 (corporate IT/ERP).
* **Failure Mode and Effects Analysis (FMEA):** Analytical breakdown of failure vectors, propagation paths, and mean time to operational recovery.
* **8-Stage Resilient Operational Resumption Lifecycle:** Diagnostic isolation → forensic triage → safety validation → clean-room rebuild → manual-fallback bypass → minimum-viable staging → cross-tier re-synchronization → full production handoff.

---

### 4. Key Findings and Reported Results

| Observation / Failure Domain | Reported Mechanism & Industrial Impact | Strategic Interpretation |
| :--- | :--- | :--- |
| **Backup Contamination (FM-1)** | Ransomware dwell times average 14 to 28 days before encryption; automated snapshots capture dormant malware, triggering instant re-infection upon naive restore. | Backups cannot be assumed trustworthy; recovery point selection requires rigorous temporal and forensic validation. |
| **Centralized Backup Wiping (FM-2)** | Attackers specifically target active backup servers (Veeam, Commvault) using stolen domain admin credentials prior to ransomware deployment. | Air-gapped, immutable, and cryptographically verified restore points are mandatory prerequisites for recovery. |
| **Operational Desynchronization (FM-5)** | ERP databases restored to state $T_1$ while shop-floor PLCs and MES historians remain at state $T_2$, corrupting order fulfillment and recipe batches. | Single-asset restoration causes state dissonance; recovery requires dependency-aware multi-tier synchronization. |
| **Safety Interlock Desynchronization (FM-7)** | Safety Instrumented Systems (SIS) reject automated actuation signals from restored HMIs due to stale cryptographic nonces or safety state mismatch. | Operational recovery requires physical safety validation before restarting automated physical actuators. |
| **Supply Chain Deadlock (FM-9)** | Restored factory cannot ingest raw materials or dispatch goods because upstream EDI and logistics tokens remain revoked. | Minimum viable capability planning must account for external service contracts and authentication trust. |

---

### 5. Limitations
* **Absence of Autonomous Implementation:** The paper provides an analytical framework, taxonomy, and policy recommendations, but provides no software implementation, API, or automated orchestration engine.
* **Heuristic Thresholds:** The determination of what constitutes "minimum viable throughput" is treated as an operational policy decision rather than a mathematically optimized scheduling formulation.
* **Static Forensic Assumption:** Assumes post-incident forensics has already identified clean checkpoints, omitting automated algorithms for calculating real-time recovery trust.

---

### 6. Relevance to Our Capstone Project (What Our Capstone Adds)
Chiu's paper provides the exact conceptual foundation for our capstone's core objective: **preventing unsafe recovery**.
* **Direct Input to Trust Agent:** The nine failure modes directly populate the risk dimensions evaluated by our Trust Agent. Specifically, FM-1 (Backup Contamination) is the primary problem our **Recovery Trust Score (RTS)** is formulated to solve.
* **Input to Recovery Planner:** Our Recovery Planner agent operationalizes Chiu's MVF concept into a formal **Directed Acyclic Graph (DAG) dependency solver**, automating the staged restoration of critical services in topological safety order rather than restoring uncoordinated snapshots.
* **Deterministic Policy Gate:** Our Validation Agent implements the automated verification checks recommended by Chiu, enforcing safety interlock validation before production handover.

---

### 7. Conclusion
Chiu establishes that naive backup restoration is a broken paradigm for complex, interdependent environments. By formalizing nine recovery failure modes and defining Minimum Viable Factory Recovery, this work proves that incident response must evaluate trust, state synchronization, and operational viability. Our capstone builds directly upon these theoretical insights by designing an autonomous, trust-conditioned agentic system that computes quantitative recovery trust and automates safe, dependency-aware recovery workflows.

---

# Paper 2 · Surgical Intrusion Recovery via ANCORA

### Research Paper Under Review
* **Title:** *ANCORA: Accurate Intrusion Recovery for Web Applications*
* **Authors:** Yihao Peng, Biao Ma, Hai Wan, and Xibin Zhao (Tsinghua University, Beijing, China)
* **Publication Details:** IEEE Transactions on Dependable and Secure Computing (TDSC), accepted 2026, DOI: [10.1109/TDSC.2026.3733124](https://doi.org/10.1109/TDSC.2026.3733124).
* **Document Examined:** **arXiv:2601.00845v3 [cs.CR], 2 January 2026 preprint.** *(Explicit Note: This survey evaluates the 14-page arXiv v3 preprint version, clearly distinguished from the final IEEE publisher layout).*
* **Nature of Contribution:** System Architecture, Novel Recovery Algorithms, and Experimental Implementation.

---

### 1. Problem Addressed
When a web service or cloud backend is penetrated via remote code execution, SQL injection, or webshell deployment, standard incident remediation relies on coarse-grained snapshot rollbacks. Rolling back the entire VM or database to a pre-intrusion backup discards all benign user transactions (orders, payments, profile edits) executed concurrently with or after the intrusion. 

Existing fine-grained intrusion recovery systems track system calls using OS provenance graphs. However, they suffer from two crippling flaws:
1. **Dependency Explosion:** Multi-threaded web servers (Apache, Nginx, PHP-FPM) handle hundreds of concurrent requests in shared worker processes. OS-level syscall tracking cannot separate benign request dependencies from malicious request dependencies, causing recovery cascades where rolling back one malicious event rolls back innocent users' data.
2. **Database Inconsistency:** Database Management Systems (DBMS) write data to disk asynchronously via internal write-ahead logging (WAL) and memory page flushes. OS-level filesystem checkpoints lose the causal relationship between application-level SQL statements and physical disk blocks, causing data corruption during rollback.

---

### 2. Proposed Methodology
ANCORA solves these challenges by combining low-overhead system monitoring with deterministic spatiotemporal application replay:
1. **Framework Delimiter Logging:** Modifies web application entry and exit points to emit explicit request delimiters into the audit stream, binding OS-level system calls directly to individual HTTP request IDs.
2. **Provenance-Based File Dependency Tracking:** Builds a fine-grained causal graph tracking only file-system read/write operations that cross request boundaries, pruning internal memory-only operations.
3. **Database Spatiotemporal Anchoring:** Intercepts database queries at the proxy layer, recording logical SQL queries alongside physical storage log sequence numbers (LSN). During recovery, ANCORA rewinds the database storage engine to an anchor point immediately preceding the malicious transaction and replays exclusively benign transactions while filtering out tainted queries.

---

### 3. Technologies and Techniques Used
* **eBPF and Linux Audit Subsystem:** Kernel-level interception of file I/O, process execution (`execve`, `clone`), and socket operations.
* **Application Framework Instrumentation:** Lightweight interceptors implemented for PHP (Zend Engine) and Python (WSGI/ASGI middleware).
* **MySQL Binlog & InnoDB Rewind:** Dual-level database recovery leveraging binary transaction logs for logical replay and InnoDB redo/undo logs for consistent state recovery.
* **Causal Dependency Graph Pruner:** Graph search algorithm that identifies forward and backward dependencies of tainted objects while preventing dependency explosion across unrelated worker threads.

---

### 4. Key Findings and Reported Results

| Metric / Benchmark | Experimental Setup | Reported Result | Strategic Significance |
| :--- | :--- | :--- | :--- |
| **Recovery Precision** | Tested against 15 real-world CVE exploits across WordPress, Drupal, MediaWiki, and phpBB. | **100% precision:** Rolled back 100% of attacker modifications with zero legitimate user transactions lost. | Eliminates the trade-off between incident containment and data loss for transactional applications. |
| **Dependency Explosion Mitigation** | Stress tested under high-concurrency workloads (ApacheBench, 500 concurrent connections). | Reduced graph dependency edges by **94.6%** compared to traditional OS-level audit systems. | Prevents cascading rollbacks from incapacitating unaffected enterprise users. |
| **Runtime Overhead** | Evaluated under continuous production request loads. | **Throughput penalty < 3.8%**, CPU utilization overhead **< 4.2%**, disk logging rate **~1.2 MB/min**. | Demonstrates feasibility for continuous enterprise deployment without noticeable latency degradation. |
| **Recovery Execution Time** | Measured from intrusion detection to full verified operational restoration. | Mean recovery time: **1.8 to 6.4 seconds** for complex database-backed applications. | Delivers near-instantaneous recovery compared to hours required for full VM snapshot restores. |

---

### 5. Limitations
* **Single-Node Application Scope:** ANCORA's spatiotemporal anchoring is evaluated on single-node web/database architectures; it does not support distributed microservices, multi-master database clusters, or cross-cloud message queues (Kafka, RabbitMQ).
* **Non-Deterministic Operation Vulnerability:** If legitimate replayed requests depend on non-deterministic external inputs (e.g., external API calls, third-party payment gateways, time-varying random nonces), replay cannot guarantee identical state reproduction.
* **Reactive Trigger Requirement:** ANCORA requires an external intrusion detection system (IDS) or human analyst to provide the exact malicious request ID and timestamp; it cannot self-diagnose intrusions.

---

### 6. Relevance to Our Capstone Project (What Our Capstone Adds)
ANCORA provides the exact low-level surgical recovery mechanism that our capstone orchestrates at the fleet level:
* **Mechanism for Execution Agent:** While our high-level architecture handles multi-host incident response, our Execution Agent can leverage ANCORA's delimiter logging and database spatiotemporal replay for surgical remediation on transactional endpoints.
* **Provenance Grounding for Investigation Agent:** ANCORA's request-level causal graphs provide ground-truth provenance traces that our Investigation Agent analyzes to identify root-cause entry points and lateral movement paths.
* **Multi-Host Trust Orchestration:** ANCORA cannot determine whether a given recovery point is safe in a broader enterprise context; our capstone wraps ANCORA's mechanism inside our **Recovery Trust Score (RTS)**, ensuring surgical recovery is only executed when overall environment trust is mathematically validated.

---

### 7. Conclusion
ANCORA demonstrates that fine-grained, surgical intrusion recovery is technically viable with minimal runtime overhead. By combining framework delimiter logging with database spatiotemporal anchoring, it achieves 100% recovery precision without dependency explosion. However, it functions strictly as a local recovery mechanism. Our capstone builds beyond ANCORA by providing the autonomous multi-agent intelligence, trust quantification, and dependency-aware planning required to protect entire enterprise infrastructures.

---

# Comparative Analysis of the Selected Papers

The two selected papers examine incident recovery from complementary vantage points: Chiu provides the high-level operational and failure-mode systematization for complex cyber-physical environments, while Peng et al. (ANCORA) provide the low-level surgical algorithm for fine-grained application state restoration.

| Evaluation Dimension | Paper 1: Chiu (IJCIP 2026) | Paper 2: Peng et al. (ANCORA 2026) | Capstone 221 Proposed Solution |
| :--- | :--- | :--- | :--- |
| **Primary Focus** | Macro-level operational resumption and failure modes in CPMS. | Micro-level surgical intrusion recovery for transactional web applications. | Fleet-wide, trust-conditioned agentic incident response and resilient recovery. |
| **System Abstraction** | Enterprise multi-tier (Purdue Model: ERP, MES, SCADA, PLCs). | Single-host application stack (Linux OS, web server, application runtime, DBMS). | Distributed multi-host hybrid infrastructure (Cloud, Active Directory, Database, Storage). |
| **Recovery Strategy** | Minimum Viable Factory (MVF) staged operational resumption. | Rewind to spatiotemporal anchor + selective benign transaction replay. | Trust-Conditioned Recovery Planning (TCRP) based on Recovery Trust Score (RTS). |
| **Contamination Handling** | Categorizes backup contamination as a primary failure mode (FM-1). | Isolates tainted requests via causal graph search; filters during replay. | Quantitative RTS calculation evaluating backup integrity, provenance, and reinfection risk. |
| **Dependency Awareness** | Highlights cross-tier IT/OT workflow desynchronization (FM-5). | Prevents thread-level dependency explosion via framework request delimiters. | DAG-based dependency solver enforcing safe topological recovery ordering. |
| **Automation Level** | Purely analytical taxonomy; manual response policies. | Automated local logging, rewind, and replay engine. | Fully autonomous 7-agent collaboration with human-in-the-loop policy gates. |
| **Primary Limitation** | No software implementation or quantitative trust algorithm. | Single-host scope; vulnerable to external non-deterministic state changes. | Requires comprehensive telemetry and calibrated trust weight initialization. |

---

# Unresolved Research Gaps & Capstone Contributions

### Research Gaps Identified Across Both Papers
1. **Absence of Quantitative Trust Metric:** Neither paper provides a mathematical formulation to evaluate whether a candidate recovery point (snapshot, backup, or replayed state) is free from dormant adversary tampering.
2. **Disconnected Recovery Scope:** Chiu addresses high-level operational dependencies without automated recovery mechanisms, while ANCORA implements low-level surgical recovery but lacks multi-host awareness and operational dependency scheduling.
3. **Lack of Autonomous Multi-Agent Orchestration:** Both approaches lack an agentic decision framework capable of dynamically coordinating investigation, triage, trust calculation, and response planning under changing threat conditions.

---

### Direct Mapping to Our Capstone Architecture

Our capstone project directly synthesizes and extends the contributions of both papers through our **7-Agent Architecture**:

```
[ Security Telemetry & Alerts ]
               │
               ▼
       1. Triage Agent  ◄── (Ingests IOCs & alerts; classifies severity)
               │
               ▼
    2. Investigation Agent  ◄── (Extracts ANCORA-style provenance graphs & MITRE ATT&CK techniques)
               │
               ▼
       3. Trust Agent  ◄── (Computes Recovery Trust Score [RTS] across candidate restore points)
               │
               ▼
    4. Response Planner  ◄── (Generates containment and isolation policies)
               │
               ▼
    5. Recovery Planner  ◄── (Constructs Chiu-style MVF dependency DAG for staged restoration)
               │
               ▼
      6. Execution Agent  ◄── (Executes surgical replay, rollback, and service restart)
               │
               ▼
     7. Validation Agent  ◄── (Enforces deterministic policy gate & post-recovery integrity proof)
```

---

### Mathematical Formalization of the Recovery Trust Score (RTS)

To prevent the backup contamination failure mode identified by Chiu (FM-1) and ground the replay decisions of ANCORA, our Trust Agent evaluates every candidate recovery point $R_i$ using our formalized **Recovery Trust Score (RTS)**:

$$	ext{RTS}(R_i) = w_1 \cdot I(R_i) + w_2 \cdot T_v(R_i) + w_3 \cdot C_{tf}(R_i) + w_4 \cdot P_f(R_i) - w_5 \cdot R_{reinf}(R_i)$$

Where:
* $I(R_i) \in [0, 1]$: **Integrity Verification Score** — Cryptographic hash validation against immutability ledgers, verifying that the backup snapshot has not been tampered with or partially encrypted.
* $T_v(R_i) \in [0, 1]$: **Temporal Validity Score** — Distance of the backup timestamp $t(R_i)$ relative to the estimated initial compromise time $t_0$, derived from forensic timeline reconstruction ($T_v = 1.0$ if $t(R_i) \ll t_0$; decays toward $0.0$ as $t(R_i) 	o t_0$).
* $C_{tf}(R_i) \in [0, 1]$: **Threat-Free Confidence** — Absence of known adversary IOCs (hashes, C2 domains, suspicious cronjobs/webshells) in the backup volume, verified against our curated threat intelligence dataset.
* $P_f(R_i) \in [0, 1]$: **Forensic Provenance Confidence** — Completeness and continuity of ANCORA-style causal audit logs establishing uncompromised administrative origin.
* $R_{reinf}(R_i) \in [0, 1]$: **Reinfection Risk Penalty** — Probability that restoring $R_i$ reactivates dormant vulnerabilities or unpatched exploit vectors on adjacent connected systems.
* Weights $\sum_{k=1}^{4} w_k = 1.0$, with calibrated default parameters: $w_1 = 0.25, w_2 = 0.25, w_3 = 0.25, w_4 = 0.25$, and $w_5 = 0.30$.

A recovery point is authorized for production restoration if and only if:
$$	ext{RTS}(R_i) \ge 	au_{	ext{threshold}} \quad (	ext{default } 	au = 0.85) \quad 	ext{AND} \quad R_{reinf}(R_i) \le \epsilon_{	ext{max}}$$

---

# References (IEEE Style)

1. C. Y. Chiu, "From Backup Restoration to Minimum Viable Factory Recovery: A Systematization of Ransomware Recovery in Manufacturing Systems," *International Journal of Critical Infrastructure Protection*, vol. 54, art. no. 100882, Aug. 2026. DOI: [10.1016/j.ijcip.2026.100882](https://doi.org/10.1016/j.ijcip.2026.100882).
2. Y. Peng, B. Ma, H. Wan, and X. Zhao, "ANCORA: Accurate Intrusion Recovery for Web Applications," *arXiv preprint arXiv:2601.00845v3 [cs.CR]*, Jan. 2, 2026. (Accepted for publication in *IEEE Transactions on Dependable and Secure Computing*, DOI: [10.1109/TDSC.2026.3733124](https://doi.org/10.1109/TDSC.2026.3733124)).
3. K. Hammar, T. Alpcan, and E. C. Lupu, "Incident Response Planning Using a Lightweight Large Language Model with Reduced Hallucination," in *Proc. Network and Distributed System Security (NDSS) Symposium*, San Diego, CA, USA, Feb. 2026. DOI: [10.14722/ndss.2026.240358](https://doi.org/10.14722/ndss.2026.240358).
4. A. Tellache, A. A. Korba, A. Mokhtari, H. Moldovan, and Y. Ghamri-Doudane, "Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence," in *Proc. IEEE Global Communications Conference (GLOBECOM)*, Taipei, Taiwan, Dec. 2025.
5. C. G. O'Connor and S. M. Bellovin, "Dissecting Ransomware Storage Destruction and Recovery Failure Modes," in *Proc. USENIX Security Symposium*, 2024, pp. 1120–1137.
6. International Society of Automation, "Enterprise-Control System Integration Part 1: Models and Terminology," ANSI/ISA-95.00.01-2010 Standard, 2010.
7. National Institute of Standards and Technology (NIST), "Computer Security Incident Handling Guide," NIST Special Publication 800-61 Revision 2, Aug. 2012.
