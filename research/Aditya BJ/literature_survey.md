# CAPSTONE PROJECT | LITERATURE SURVEY — PROJECT ID 221
## Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery

| Field | Details | Field | Details |
| :--- | :--- | :--- | :--- |
| **Project ID** | 221 | **Course** | UE24CS320A – Capstone Project |
| **Review** | Phase-I · Review-2 | **Institution** | PES University, Bengaluru |
| **Project Guide** | Dr. Geetha Dayalan | **Survey Focus** | Resilient Ransomware Recovery, Intrusion Provenance, and Trust-Aware Backups |
| **Prepared by** | Aditya Basavaraj Jambagi | **SRN** | PES2UG24CS030 |

---

### Scope of This Survey

This literature survey conducts a critical academic investigation of two foundational research contributions that address the central vulnerability of modern enterprise incident response: **contaminated recovery**. In sophisticated intrusions and ransomware outbreaks, enterprise response workflows frequently resort to restoring systems from the latest available backup or virtual machine snapshot. If that restore point was captured after initial adversary infiltration, dormant implants, persistent backdoors, and compromised credentials are reinstated directly into the production environment, triggering immediate reinfection cycles.

To establish a comprehensive defensive framework, this survey reviews two complementary peer-reviewed papers within the broader context of autonomous response planning (Hammar et al. [3]), threat intelligence fusion (Tellache et al. [4]), and national incident management guidelines (NIST SP 800-61 Revision 3 [5]):
1. **Paper 1 (Chiu [1]):** Systematizes ransomware recovery in cyber-physical manufacturing systems, establishing that restoring disk snapshots does not equate to operational system resumption and defining the *Minimum Viable Factory Recovery (MVF)* construct governed by nine distinct recovery failure modes.
2. **Paper 2 (Peng et al. [2]):** Introduces *ANCORA*, an accurate surgical intrusion recovery system for web applications that leverages framework-level request delimiter logging, system-call provenance tracking, and database connection-tuple and time-window anchoring to isolate malicious modifications and selectively replay legitimate operations without destructive full-system rollbacks.

Both papers are reviewed under an identical structured framework: metadata and academic context, problem addressed, proposed methodology, technologies and analytical techniques, key findings and reported results, limitations, and relevance to our proposed capstone project. A comparative analysis follows, synthesizing open research gaps, mapping capabilities to our proposed 7-agent architecture, formalizing the Recovery Trust Score (RTS), and providing complete IEEE-style references.

---

# Paper 1 · Systematizing Ransomware Recovery & Minimum Viable Factory Recovery

### Research Paper Under Review
* **Title:** *From Backup Restoration to Minimum Viable Factory Recovery: A Systematization of Ransomware Recovery in Manufacturing Systems*
* **Author:** Chun Yin Chiu (Department of Informatics, King's College London, London, UK) [1]
* **Publication:** *International Journal of Critical Infrastructure Protection* (Elsevier), Volume 54, September 2026, Article 100882. (Available online: 10 August 2026).
* **DOI:** [10.1016/j.ijcip.2026.100882](https://doi.org/10.1016/j.ijcip.2026.100882)
* **Nature of Contribution:** Systematization of Knowledge (SoK) / PRISMA-guided Multivocal Literature Review. *(Explicit Academic Note: This work provides an evidence-calibrated conceptual and analytical taxonomy; it does not implement a software tool or autonomous agent system).*

---

### 1. Problem Addressed
Industrial cyber-physical manufacturing systems (CPMS) increasingly suffer severe ransomware incidents. Conventional disaster recovery frameworks assume that operational recovery is synonymous with restoring IT servers and databases from backups. However, real-world industrial disclosures demonstrate that even after IT teams declare backups technically restored, manufacturing plants frequently remain halted for weeks or months [1].

Chiu [1] investigates the structural disconnect between technical data restoration and operational system resumption. In modern smart manufacturing, production workflows depend on tightly coupled, cross-domain dependencies spanning Enterprise Resource Planning (ERP), Manufacturing Execution Systems (MES), Supervisory Control and Data Acquisition (SCADA), Programmable Logic Controllers (PLCs), quality assurance inspection, and external supply chains. Restoring isolated disk snapshots fails because physical machine states, recipe data, cryptographic trust boundaries, and safety interlocks have become desynchronized or corrupted.

---

### 2. Proposed Methodology
Chiu [1] conducts a PRISMA-guided multivocal literature review, integrating academic peer-reviewed literature with practitioner technical disclosures:
* **Corpus Selection:** The review evaluates **797 retained sources/records**, comprising:
  * **342 eligible core academic records** focused on industrial incident response, ransomware, and CPMS resilience;
  * **427 background academic records** addressing broader fault tolerance, distributed recovery, and industrial networking;
  * **28 grey-literature and incident sources**, encompassing industrial technical disclosures, post-incident post-mortems, and engineering reports (clarified: not all 28 represent primary incident or regulatory filings).
* **Analytical Workflow:** Employs formal screening, source eligibility criteria, coding, evidence classification, and source-page verification.
* **Methodological Scope:** The author explicitly characterizes the study as a *PRISMA-guided* review, which provides systematic structure without claiming full multi-author PRISMA compliance or independent multi-coder reliability scoring.

---

### 3. Technologies and Analytical Contributions
The paper does not present software implementations or autonomous agents. Its core technical contributions include:
* **Nine-Mode Recovery Failure Taxonomy (FM01–FM09):** A systematic classification of failure vectors that cause post-ransomware restoration breakdowns [1].
* **Evidence-Calibrated Review Methodology:** A multi-tier analytical synthesis structured across technical, operational, and organizational recovery dimensions.
* **Minimum Viable Factory Recovery (MVF) Construct:** A resilience model reframing recovery objectives from complete stack restoration to the staged resumption of core, safety-critical production throughput [1].
* **Recovery Dependency Modeling:** Explicit mapping of functional interdependencies across enterprise IT and industrial OT workflows.
* **Eight-Stage Operational Recovery Lifecycle:** A phased lifecycle governing safe industrial resumption.
* **Evaluation & Benchmarking Directions:** Proposed metrics for quantifying post-incident recovery viability and state verification.

*(Note: Foundational industrial concepts such as the Purdue Enterprise Reference Architecture / ISA-95 and Failure Mode and Effects Analysis [FMEA] provide standard contextual terminology for multi-tier industrial modeling, but are external engineering reference standards rather than proprietary methods developed by the author).*

---

### 4. Failure Vector Isolation & Illustrative Operational Disconnect
A central finding of Chiu's systematization [1] is that traditional disaster recovery metrics—such as Recovery Point Objective (RPO) and Recovery Time Objective (RTO)—measure storage availability and server uptime rather than functional capability. 

*Illustrative Scenario:* As an illustrative scenario, a restored backup meeting a 4-hour RTO may still leave an industrial manufacturing facility offline for weeks if cross-tier operational dependencies, recipe integrity, and machine states remain uncoordinated.

By shifting focus from data storage restoration to operational capability restoration, the analysis highlights the foundational requirements for autonomous decision-making systems: recovery planners must evaluate trust, temporal validity, and dependency ordering before authorizing system restarts.

---

### 5. Taxonomy of Nine Recovery Failure Modes

| Failure Mode | Failure Designation | Reported Industrial Mechanism & Operational Impact |
| :--- | :--- | :--- |
| **FM01** | **Dependency Blindness** | Restoring IT or OT components in isolation without accounting for cross-tier workflow, recipe, and service dependencies, causing operational deadlock [1]. |
| **FM02** | **Untrusted Restore Point & Backup Over-Trust** | Assuming backups are pristine without verifying dwell time; restoring infected backups reinstates dormant malware implants and triggers immediate reinfection cycles [1]. |
| **FM03** | **Identity Trust Collapse** | Compromise of Active Directory, domain controllers, or PKI certificates, rendering authentication assertions across restored services invalid or untrustworthy [1]. |
| **FM04** | **Lack of Proof-of-Recovery** | Declaring systems recovered without formal, evidence-based verification of system integrity, configuration baselines, and clean operational status [1]. |
| **FM05** | **Unsafe OT Reconnection** | Reconnecting industrial control networks and PLCs to corporate networks before validating physical device states, firmware baselines, and safety parameters [1]. |
| **FM06** | **Segmentation Assumption Failure** | Relying on unverified network zone boundaries and air-gap assumptions that were breached during lateral movement, enabling adversary persistence [1]. |
| **FM07** | **Capability Mismatch** | Restored computational assets do not necessarily mean restored production capability; key operational capabilities such as active production, quality inspection, batch release, shipping logistics, or inter-facility work coordination may remain impaired despite server availability [1]. |
| **FM08** | **Degraded Mode Unmanaged** | Lacking pre-planned, structured procedures for managing manual workarounds or reduced-capacity operations, leading to worker confusion and safety violations [1]. |
| **FM09** | **Supplier Dependency Failure** | External supply chain, vendor maintenance channels, or third-party cloud services remaining inaccessible or quarantined, preventing end-to-end production [1]. |

---

### 6. The Eight-Stage Operational Recovery Lifecycle
To systematically mitigate the nine failure modes, Chiu [1] formalizes an eight-stage operational recovery lifecycle:
1. **Mission Impact Assessment:** Identify core business and safety functions that must be restored first.
2. **Dependency Modelling:** Construct directed dependency graphs linking physical equipment, controllers, MES, and IT applications.
3. **Clean-State Selection:** Identify uncompromised restore points and clean configuration baselines verified against adversary dwell time.
4. **Minimum Viable Factory Planning:** Formulate staged restoration workflows prioritizing safety-critical baseline throughput.
5. **Validation and Simulation:** Test restoration plans in isolated or controlled test environments prior to physical execution.
6. **Proof-of-Recovery:** Perform rigorous cryptographic, configuration, and functional checks to verify system clean-state integrity.
7. **Staged Reintegration:** Reconnect restored systems across network zones in progressive trust stages.
8. **Monitored Production Resumption:** Resume live production under heightened telemetry monitoring and anomaly detection.

---

### 7. Limitations of Paper 1
To maintain academic rigor, limitations are distinguished between those explicitly discussed by the author and additional limitations identified through critical analysis:

* **Limitations Explicitly Discussed by the Author [1]:**
  * The review is bounded by the transparency and completeness of public incident disclosures, which are often constrained by corporate nondisclosure agreements and ongoing litigation.
  * The focus is targeted primarily at cyber-physical manufacturing systems, meaning operational failure modes in purely virtual cloud environments may exhibit different characteristics.
  * Qualitative classification across multivocal literature inevitably involves some degree of subjective categorization.
* **Additional Limitations Identified Through Our Critical Analysis:**
  * *Absence of Software Implementation:* Chiu [1] provides an analytical taxonomy and conceptual guidelines, but offers no software tools, APIs, or autonomous orchestration engine.
  * *Heuristic Thresholds:* The determination of what constitutes "minimum viable throughput" is treated as an operational policy decision rather than an algorithmically optimized objective.
  * *Static Forensic Assumption:* Assumes post-incident forensics has already identified clean checkpoints, omitting automated algorithms for calculating real-time recovery trust.

---

### 8. Relevance to Our Proposed Capstone Project
Chiu's paper [1] provides the theoretical foundation for our proposed capstone's core objective: **preventing unsafe recovery**.
* **Direct Input to Proposed Trust Agent:** Specifically addresses FM02 (Untrusted Restore Point & Backup Over-Trust), which our proposed **Recovery Trust Score (RTS)** is mathematically designed to detect and prevent.
* **Foundation for Proposed Recovery Planner:** Informs the design of a dependency-aware DAG solver to automate staged restoration in topological order, avoiding FM01 (Dependency Blindness).
* **Basis for Proposed Validation Agent:** Informs the post-restoration verification checks required to supply formal proof-of-recovery, directly mitigating FM04 (Lack of Proof-of-Recovery).
* **Policy Safety Constraints for Proposed Execution Agent:** The risks highlighted in FM05 (Unsafe OT Reconnection) and FM06 (Segmentation Assumption Failure) justify our architecture's requirement that the Execution Agent enforce strict, deterministic policy validation before applying actions.

---

### 9. Conclusion of Paper 1 Review
The review demonstrates that naive backup restoration is an inadequate recovery paradigm for complex, interdependent environments [1]. By formalizing nine failure modes and defining Minimum Viable Factory Recovery, this work proves that incident response must evaluate trust, state synchronization, and operational viability. Our proposed capstone aims to operationalize these conceptual insights into an autonomous agentic framework.

---

# Paper 2 · Surgical Intrusion Recovery via ANCORA

### Research Paper Under Review
* **Title:** *ANCORA: Accurate Intrusion Recovery for Web Applications*
* **Authors:** Yihao Peng, Biao Ma, Hai Wan, and Xibin Zhao (Tsinghua University, Beijing, China) [2]
* **Preprint Examined:** **arXiv:2510.07806v3 [cs.CR], 2 January 2026.** *(Explicit Academic Note: This survey analyzes the 14-page arXiv v3 preprint version).*
* **Final Publication:** *IEEE Transactions on Dependable and Secure Computing* (TDSC), published online 10 September 2026. &bull; **DOI:** [10.1109/TDSC.2026.3733124](https://doi.org/10.1109/TDSC.2026.3733124)
* **Nature of Contribution:** System Architecture, Novel Recovery Algorithms, and Experimental Implementation [2].

---

### 1. Problem Addressed
When an enterprise web application or backend database is compromised via remote code execution, SQL injection, or webshell deployment, standard remediation reverts the entire virtual machine or database to a pre-incident snapshot. This coarse rollback destroys all legitimate user transactions (orders, payments, profile edits) executed concurrently with or after the intrusion.

Fine-grained intrusion recovery systems track system calls using OS provenance graphs. However, as Peng et al. [2] explain, existing approaches suffer from two critical limitations:
1. **Dependency Explosion:** Multi-threaded web servers (Apache, Nginx, PHP-FPM) handle hundreds of requests within shared worker processes. OS-level syscall tracking cannot separate benign request dependencies from malicious request dependencies, causing recovery cascades where rolling back one malicious event rolls back innocent users' data.
2. **Database Inconsistency:** Database Management Systems (DBMS) write data to disk asynchronously via internal write-ahead logging (WAL) and memory page flushes. OS-level filesystem checkpoints lose the causal relationship between application-level SQL statements and physical disk blocks, causing data corruption during rollback.

---

### 2. Three-Stage Technical Methodology
ANCORA [2] addresses these challenges through a three-stage workflow:

#### Stage 1 – Request Partition
* **Instrumentation & Delimiter Logging:** Web application runtimes are instrumented to emit explicit entry and exit delimiters into the log stream, assigning each HTTP request a **unique request identifier**.
* **System-Call Separation:** System-call logs collected at the OS level are partitioned by request ID, isolating the exact system operations caused by a specific malicious HTTP request from concurrent benign operations.
* **Kernel Event Collection:** Employs **Sysdig** for low-overhead kernel-level system-call capture.

#### Stage 2 – File System Recovery
* **Provenance Graph Construction:** Constructs fine-grained causal provenance graphs from partitioned system-call logs.
* **Process Tracking:** Tracks parent and child processes spawned by malicious requests (e.g., webshells or arbitrary command executions).
* **Hybrid Baseline & Selective Replay:** ANCORA employs a hybrid checkpointing approach: **Watchdog and rsync support incremental backups of dynamic data directories**, while **static system and application directories utilize a known-good baseline, such as an immutable container image or an initial full backup** [2]. Using these baselines, ANCORA reverts malicious modifications while selectively replaying legitimate concurrent file modifications.

#### Stage 3 – Database Recovery
* **Connection-Tuple & Time-Window Anchoring:** In supported configurations, ANCORA extracts the **network connection four-tuple** (client IP, client port, server IP, server port) and the **active time window** of the malicious request to identify the corresponding database worker thread. For document stores such as MongoDB, application audit logs containing client connection information can be used to correlate and isolate tainted database operations [2].
* **Log-Based Operation Isolation:** Uses the time window and database application/audit logs to pinpoint the exact malicious database operations executed by that thread.
* **Clean Snapshot Rewind & Replay:** Restores a clean pre-incident database snapshot and replays exclusively legitimate operations, filtering out tainted queries.

---

### 3. Technologies and Techniques Used
ANCORA [2] combines kernel instrumentation, runtime hooks, and audit parsing:
* **Kernel System-Call Capture:** Sysdig collection engine.
* **Application Framework Instrumentation:** Python monkey patching, Node.js `async_hooks`, and **Java Agent instrumentation**.
* **Provenance Modeling:** System-call causal provenance graph construction.
* **Database Anchoring:** Network connection four-tuple and time-window anchoring across MySQL, PostgreSQL, and MongoDB.
* **Storage Checkpointing:** Incremental file-system snapshots via Watchdog and rsync, combined with known-good static baselines.
* **Recovery Mechanism:** Rewind and selective replay of benign operations.
* **Audit Parsing:** Application-level and DBMS audit log analyzers.

---

### 4. Key Findings and Reported Results

| Evaluation Metric | Experimental Benchmark | Reported Result | Academic Interpretation |
| :--- | :--- | :--- | :--- |
| **Benchmark Diversity** | **10 real-world web applications (9 open-source applications and 1 custom application)** across PHP, Python, Java, Node.js; 3 DBMS (MySQL, PostgreSQL, MongoDB) [2]. | Evaluated against **20 CVE-based attack scenarios** up to **150 concurrent connections**. | Validates broad framework applicability across heterogeneous production technology stacks. |
| **Overall Recovery Accuracy** | Across all applications, attack scenarios, and concurrency levels. | **Approximately 99.9%** overall recovery accuracy across file system and database state [2]. | Achieves near-perfect state recovery without requiring destructive full-system rollbacks. |
| **Database Recovery Accuracy** | High-concurrency benchmark at 150 concurrent connections. | **Approximately 99.81%** average database recovery accuracy [2]. | Demonstrates robust transaction isolation even under heavy multi-threaded database concurrency. |
| **File-System Recovery Accuracy** | File operations across all 20 CVE attack scenarios. | **100%** average file-system recovery accuracy [2]. | Accurately removes all attacker artifacts and webshells while preserving benign user uploads. |
| **Malicious Operation Matching F1-Score** | Disentangling malicious from benign operations at 150 concurrency. | **Average F1-score of approximately 0.998** (clarified: distinct from overall recovery accuracy) [2]. | Confirms extremely low false-positive and false-negative rates in identifying tainted operations. |
| **Runtime Performance Overhead** | Production workload simulations. | Maximum response latency increase of **19.8%**; maximum QPS decrease of **17.8%** [2]. | Imposes moderate runtime performance overhead acceptable for high-security environments. |
| **Recovery Throughput** | Measured during active post-incident state reconstruction. | **110.7 database operations/sec**; **27.2 affected files/sec** [2]. | Reports quantitative state restoration throughput measured under experimental attack benchmarks. |

---

### 5. Limitations of Paper 2
1. **Database Architecture Constraints:** The connection-to-worker-thread mapping can fail when database connection poolers, proxies (e.g., ProxySQL), or advanced connection multiplexers are deployed, as multiple client connections share the same backend thread [2].
2. **External Service Side-Effects:** ANCORA can identify outbound HTTP/API interactions initiated during an exploit, but cannot automatically roll back or reverse side-effects on external third-party systems (e.g., third-party payment gateways) [2].
3. **Scope of Stateful State:** ANCORA's current evaluation focuses on local application file-system and database recovery. Its scope does not automatically remediate side-effects on external services, nor does it track or rewind other stateful distributed components such as in-memory caches (e.g., Redis) or message queues (e.g., Kafka) [2].
4. **Reactive Trigger Dependency:** ANCORA begins its workflow only after an external intrusion detection system (IDS) or a human security analyst identifies a malicious HTTP request and provides the request identifier and active time window.

---

### 6. Relevance to Our Proposed Capstone Project
ANCORA [2] provides the exact fine-grained, surgical recovery mechanism that our proposed multi-agent system aims to orchestrate at the enterprise fleet level:
* **Mechanism for Proposed Execution Agent:** Provides the local request-partitioning, rewind, and selective-replay mechanisms executed when restoring transactional application tiers.
* **Timeline Grounding for Proposed Investigation Agent:** ANCORA's connection-tuple and time-window correlation provides ground-truth telemetry for reconstructing attack entry points.
* **Multi-Host Orchestration Beyond Local Recovery:** ANCORA focuses on local application recovery and requires an external trigger; our proposed system provides the multi-host agentic intelligence, quantitative trust validation, and enterprise-wide recovery coordination that ANCORA lacks.

---

### 7. Conclusion of Paper 2 Review
ANCORA establishes that accurate, fine-grained intrusion recovery is technically achievable without cascading dependency explosion or whole-system rollbacks [2]. By combining Sysdig system-call partitioning with database connection-tuple and time-window anchoring, it delivers ~99.9% recovery accuracy across heterogeneous applications. However, because it operates locally and reactively, our proposed capstone builds beyond ANCORA by embedding its surgical recovery concepts into an autonomous, trust-aware multi-agent architecture.

---

# Comparative Analysis of the Selected Papers

| Dimension | Paper 1: Chiu (IJCIP 2026) [1] | Paper 2: Peng et al. (ANCORA 2026) [2] | Proposed Capstone 221 Solution |
| :--- | :--- | :--- | :--- |
| **Primary Focus** | Macro-level operational resumption and failure modes in CPMS. | Micro-level surgical intrusion recovery for transactional web applications. | Fleet-wide, trust-conditioned agentic incident response and resilient recovery. |
| **System Abstraction** | Multi-tier industrial enterprise (ERP, MES, SCADA, PLCs, Supply Chain). | Local application stack (Linux OS, Web Server, Runtime, DBMS). | Distributed multi-host hybrid infrastructure (Cloud, Active Directory, DB, Storage). |
| **Recovery Mechanism** | Staged Minimum Viable Factory (MVF) operational resumption lifecycle. | System-call provenance tracking + database connection-tuple rewind & replay. | Trust-Conditioned Recovery Planning (TCRP) based on Recovery Trust Score (RTS). |
| **Contamination Handling** | Categorizes backup contamination as a primary failure mode (FM02). | Isolates tainted requests via delimiter logs; filters queries during replay. | Quantitative RTS evaluation of integrity, temporal validity, and reinfection risk. |
| **Dependency Awareness** | Analyzes multi-tier workflow and safety interlock dependencies (FM01, FM05). | Mitigates thread-level dependency explosion via request delimiter logging. | Formulates DAG-based dependency solver for topological service restoration. |
| **Automation Level** | Purely analytical taxonomy; manual response and policy guidelines. | Automated local logging, rewind, and replay engine. | Autonomous 7-agent collaboration with human-in-the-loop policy approval. |
| **Primary Limitation** | No software implementation, API, or automated execution tools. | Local scope; breaks under database proxies; reactive trigger needed. | Requires calibrated trust weight initialization and comprehensive telemetry. |

---

# Unresolved Research Gaps & Proposed Capstone Contributions

### Research Gaps Identified Across Both Papers
1. **Absence of Quantitative Trust Metric:** Neither Chiu [1] nor Peng et al. [2] provides a mathematical formulation to evaluate whether a candidate recovery point (snapshot, backup, or replayed state) is free from dormant adversary tampering.
2. **Disconnected Recovery Scope:** Chiu [1] addresses high-level operational dependencies without automated recovery mechanisms, while ANCORA [2] implements low-level surgical recovery but lacks multi-host awareness and operational dependency scheduling.
3. **Lack of Autonomous Multi-Agent Orchestration:** Both approaches lack an agentic decision framework capable of dynamically coordinating investigation, triage, trust calculation, and response planning under changing threat conditions, as explored in broader AI response literature (Hammar et al. [3], Tellache et al. [4]).

---

### Direct Mapping to Proposed Capstone 221 Seven-Agent Architecture

The proposed capstone synthesizes and extends the insights of both papers across seven specialized autonomous agents:

```
[ Ingest: Security Telemetry & Threat Feeds ]
                      │
                      ▼
             1. TRIAGE AGENT         ──> Identifies and classifies security incidents
                      │
                      ▼
          2. INVESTIGATION AGENT     ──> Reconstructs timelines, identifies compromise & analyses evidence
                      │
                      ▼
               3. TRUST AGENT        ──> Calculates the quantitative Recovery Trust Score (RTS)
                      │
                      ▼
            4. RESPONSE PLANNER      ──> Prepares containment and remediation plans
                      │
                      ▼
            5. RECOVERY PLANNER      ──> Selects trustworthy restore points & plans dependency-aware recovery
                      │
                      ▼
             6. EXECUTION AGENT      ──> Applies deterministic policy checks, obtains approvals & executes actions
                      │                  (Enforces deterministic policy gate & approval boundaries)
                      ▼
            7. VALIDATION AGENT      ──> Checks restored-system integrity, malware presence & service health
```

*(Architectural Safety Note: To ensure strict safety boundaries, the **deterministic policy gate** is assigned directly to the **Execution Agent**, which enforces invariant security constraints and approval requirements before any remedial command is executed).*

---

### Mathematical Formalization of the Proposed Recovery Trust Score (RTS)

To prevent the untrusted restore point failure mode identified by Chiu (FM02 [1]) and ground the replay decisions of ANCORA [2], our proposed Trust Agent evaluates candidate recovery points $R_i$ using our formalized **Recovery Trust Score (RTS)**, following the project's proposed formulation and design parameters:

$$	ext{BaseTrust}(R_i) = 0.30 \cdot I(R_i) + 0.30 \cdot V(R_i) + 0.25 \cdot T(R_i) + 0.15 \cdot F(R_i)$$

$$	ext{RTS}(R_i) = 	ext{BaseTrust}(R_i) \cdot (1 - R(R_i))$$

Where:
* $I(R_i) \in [0, 1]$: **Integrity Confidence** — Cryptographic hash validation against immutability ledgers, verifying that the backup snapshot has not been tampered with or partially encrypted.
* $V(R_i) \in [0, 1]$: **Temporal Validity Confidence** — Distance of the backup timestamp relative to estimated initial compromise time $t_0$, derived from forensic timeline reconstruction ($V$ approaches $1.0$ when the snapshot timestamp occurs well before the estimated compromise time $t_0$, and decays toward $0.0$ as the timestamp nears $t_0$).
* $T(R_i) \in [0, 1]$: **Threat-Free Confidence** — Absence of known adversary IOCs (hashes, C2 domains, webshells) in the backup volume, verified against our curated threat intelligence dataset.
* $F(R_i) \in [0, 1]$: **Forensic Provenance Confidence** — Completeness and continuity of causal audit logs establishing uncompromised administrative origin.
* $R(R_i) \in [0, 1]$: **Reinfection Risk** — Probability that restoring $R_i$ reactivates dormant vulnerabilities or unpatched exploit vectors on adjacent connected systems.

#### Critical Security Assurance Principle
Crucially, cryptographic integrity checking ($I$) and the absence of known threat indicators ($T$) do not independently guarantee that a backup is malware-free, as zero-day implants or unindexed backdoors may remain undetected prior to formal signature disclosure. Furthermore, an RTS classification (even when evaluated as TRUSTED) does not bypass the Execution Agent's deterministic policy gate or required human approvals; rather, it serves as an evidence-calibrated prerequisite for authorization.

#### Proposed Trust Classifications
* **$	ext{RTS}(R_i) \ge 0.75$:** **TRUSTED** — Authorized for automated recovery planning and staged execution.
* **$0.40 \le 	ext{RTS}(R_i) < 0.75$:** **UNCERTAIN** — Requires human-in-the-loop review, supplemental forensic scanning, or sandboxed execution.
* **$	ext{RTS}(R_i) < 0.40$ (or hard security violation):** **UNTRUSTED** — Quarantined; restoration prohibited.

*(Explicit Note: The baseline weights $0.30, 0.30, 0.25, 0.15$ and decision thresholds are proposed project design parameters that will undergo empirical sensitivity analysis and calibration during Phase-II experimental validation).*

---

# References (IEEE Style)

1. C. Y. Chiu, "From Backup Restoration to Minimum Viable Factory Recovery: A Systematization of Ransomware Recovery in Manufacturing Systems," *International Journal of Critical Infrastructure Protection*, vol. 54, art. no. 100882, Sep. 2026, available online Aug. 10, 2026. DOI: [10.1016/j.ijcip.2026.100882](https://doi.org/10.1016/j.ijcip.2026.100882).
2. Y. Peng, B. Ma, H. Wan, and X. Zhao, "ANCORA: Accurate Intrusion Recovery for Web Applications," *arXiv preprint arXiv:2510.07806v3 [cs.CR]*, Jan. 2, 2026. (Accepted for publication in *IEEE Transactions on Dependable and Secure Computing*, published online Sep. 10, 2026, DOI: [10.1109/TDSC.2026.3733124](https://doi.org/10.1109/TDSC.2026.3733124)).
3. K. Hammar, T. Alpcan, and E. C. Lupu, "Incident Response Planning Using a Lightweight Large Language Model with Reduced Hallucination," in *Proc. Network and Distributed System Security (NDSS) Symposium*, San Diego, CA, USA, Feb. 2026. DOI: [10.14722/ndss.2026.240358](https://doi.org/10.14722/ndss.2026.240358).
4. A. Tellache, A. A. Korba, A. Mokhtari, H. Moldovan, and Y. Ghamri-Doudane, "Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence," in *Proc. IEEE Global Communications Conference (GLOBECOM)*, Taipei, Taiwan, Dec. 2025.
5. K. Stine, S. Quinn, G. Witte, and R. Gardner, "Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A Community Profile," National Institute of Standards and Technology, Gaithersburg, MD, NIST Special Publication 800-61 Revision 3, Apr. 2025. DOI: [10.6028/NIST.SP.800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3).
