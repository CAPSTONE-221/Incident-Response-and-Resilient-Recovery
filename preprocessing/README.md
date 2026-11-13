# Cybersecurity Dataset Preprocessing & Standardization Pipeline

> **Issue Reference:** Closes [#15](https://github.com/CAPSTONE-221/Incident-Response-and-Resilient-Recovery/issues/15)  
> **Project Title:** Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery  
> **Team ID:** 221

---

## 📌 Executive Summary

This directory implements the production-grade **data cleaning, feature engineering, standardization, and class imbalance mitigation pipeline** for Team 221's cybersecurity datasets.

Raw network flow logs, memory dumps, and simulated telemetry cannot be directly fed into neural networks or gradient-boosted decision trees. They contain:
- Non-predictive identifiers (`id`, arbitrary session numbers)
- Infinite values (`inf` in packet rates where duration $\approx 0$)
- Extreme outliers in flow duration and byte counts
- Severe class imbalance (millions of benign flows vs. rare exploit/ransomware samples)
- Data leakage risks if scalers or encoders are fitted across entire datasets

Our modular pipeline transforms these raw sources into **standardized, leak-free, reproducible training, validation, and testing splits** with persisted transformer artifacts.

---

## 🏗️ Preprocessing Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 PREPROCESSING PIPELINE ARCHITECTURE                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

   Raw Sources (datasets/public/ & datasets/lab-generated/)
   ├── UNSW-NB15 (Train + Test: 257,673 rows)
   ├── CIC-MalMem-2022 (58,596 rows)
   ├── NSL-KDD (148,517 rows)
   └── Synthetic RTS Benchmark (500 recovery points)
                            │
                            ▼
 ┌───────────────────────────────────────────────────────┐
 │ Step 1: Data Cleaning (DataCleaner)                   │
 │  - Remove non-predictive IDs                          │
 │  - Replace ±inf with NaN; impute median (mode for cat)│
 │  - Deduplicate training records                       │
 └──────────────────────────┬────────────────────────────┘
                            │
                            ▼
 ┌───────────────────────────────────────────────────────┐
 │ Step 2: Stratified Splitting (DataSplitter)           │
 │  - 70% Train, 15% Validation, 15% Test                │
 │  - Preserves multi-class & binary target proportions  │
 │  - Zero index overlap (Mathematical Leakage Check)    │
 └──────────────────────────┬────────────────────────────┘
                            │
                            ▼
 ┌───────────────────────────────────────────────────────┐
 │ Step 3: Feature Selection (FeatureSelector)           │
 │  - Low-variance filter (VarianceThreshold >= 0.0001)  │
 │  - Pairwise collinearity filter (corr <= 0.98)        │
 │  - Fitted strictly on Train; applied to Val & Test    │
 └──────────────────────────┬────────────────────────────┘
                            │
                            ▼
 ┌───────────────────────────────────────────────────────┐
 │ Step 4: Encoding & Scaling (FeatureTransformer)       │
 │  - RobustScaler (for high-variance network flows)     │
 │  - StandardScaler (for memory forensics & benchmarks) │
 │  - Unknown-category handling for test robustness      │
 │  - Persist fitted transformers as .joblib artifacts   │
 └──────────────────────────┬────────────────────────────┘
                            │
                            ▼
 ┌───────────────────────────────────────────────────────┐
 │ Step 5: Class Imbalance Mitigation (ImbalanceHandler) │
 │  - Compute cost-sensitive balanced class weights      │
 │  - Inverse-frequency formulation: w_j = n / (k * n_j) │
 └──────────────────────────┬────────────────────────────┘
                            │
                            ▼
   Output Artifacts (datasets/processed/ & preprocessing/artifacts/)
   ├── train.csv, val.csv, test.csv
   ├── metadata.json (Auditing, feature schema, class weights)
   └── *.joblib (Serialised Scalers & Encoders for runtime agents)
```

---

## 📂 Directory Layout

```
preprocessing/
├── README.md                      # This master guide
├── preprocessing_summary_report.json # Comprehensive execution audit
├── configs/
│   └── preprocessing_config.yaml  # Centralized hyperparameter configuration
├── pipelines/                     # Reusable modular pipeline classes
│   ├── __init__.py
│   ├── cleaner.py                 # Null/inf removal, deduplication, ID dropping
│   ├── data_splitter.py           # Stratified train/val/test splitting
│   ├── feature_selector.py        # VarianceThreshold & collinearity filter
│   ├── encoder_scaler.py          # Encoders, Scalers & artifact persistence
│   └── imbalance_handler.py       # Balanced class weight formulation
├── artifacts/                     # Persisted transformers for inference
│   ├── unsw_nb15_RobustScaler.joblib
│   ├── unsw_nb15_encoders.joblib
│   ├── cic_malmem_StandardScaler.joblib
│   ├── cic_malmem_encoders.joblib
│   ├── nsl_kdd_StandardScaler.joblib
│   └── nsl_kdd_encoders.joblib
├── scripts/                       # Per-dataset preprocessing runners
│   ├── preprocess_unsw_nb15.py
│   ├── preprocess_cic_malmem.py
│   ├── preprocess_nsl_kdd.py
│   └── preprocess_rts_benchmark.py
└── run_all_preprocessing.py       # Master orchestration script
```

---

## 📊 Preprocessing Execution & Validation Matrix

Running `python preprocessing/run_all_preprocessing.py` produces the following validated splits across all four core datasets:

| Dataset | Intended Agent | Total Rows | Train (70%) | Val (15%) | Test (15%) | Features Kept | Dropped Features |
|---|---|---|---|---|---|---|---|
| **UNSW-NB15** | **Triage Agent** | 162,745 (deduped) | **113,921** | **24,412** | **24,412** | 41 | `id`, `sloss`, `dloss`, `ct_ftp_cmd` |
| **CIC-MalMem-2022** | **Trust & Validation Agents** | 58,047 (deduped) | **40,632** | **8,707** | **8,708** | 41 | 6 zero-variance + 12 collinear columns |
| **NSL-KDD** | **Triage Agent (Baseline)** | 147,888 (deduped) | **103,521** | **22,183** | **22,184** | 40 | `difficulty`, `label`, constant flags |
| **RTS Benchmark** | **Trust Agent & TCRP Engine** | 500 | **350** | **75** | **75** | 14 | None (all core attributes verified) |

---

## 🔍 In-Depth Dataset Transformations

### 1. UNSW-NB15 (For Triage Agent)
- **Problem:** Contains non-predictive sequential `id`s, high-variance byte/packet rates spanning 6 orders of magnitude, and '-' characters in the `service` column.
- **Transformations:**
  1. Dropped `id`.
  2. Replaced `service: "-"` with `"none"`.
  3. Standardized attack categories (mapped `"Backdoors"` to `"Backdoor"`, empty values to `"Normal"`).
  4. Dropped collinear features (`sloss`, `dloss`, `ct_ftp_cmd` with $r > 0.98$).
  5. Applied `RobustScaler` on continuous flow metrics (uses interquartile range to remain immune to extreme DDoS packet bursts).
  6. Stratified on 10 attack classes: `Normal`, `Generic`, `Exploits`, `Fuzzers`, `DoS`, `Reconnaissance`, `Analysis`, `Backdoor`, `Shellcode`, `Worms`.

### 2. CIC-MalMem-2022 (For Trust & Validation Agents)
- **Problem:** Raw categories contain composite names (e.g. `Ransomware-Conti-1`, `Spyware-Gator-2`). Several kernel memory structures have zero variance in the sandbox environment.
- **Transformations:**
  1. Extracted `malware_type` (`Ransomware`, `Spyware`, `Trojan`, `Benign`) and `malware_family` (`Conti`, `MAZE`, `Pysa`, `Ako`, `Shade`, `Zeus`, etc.).
  2. Encoded binary target: `is_malware` ($0$ for Benign, $1$ for Malware).
  3. Filtered 6 zero-variance memory features:
     - `pslist.nprocs64bit`, `handles.nport`, `ldrmodules.not_in_load_avg`, `ldrmodules.not_in_mem_avg`, `psxview.not_in_eprocess_pool_false_avg`, `svcscan.interactive_process_services`.
  4. Filtered 12 collinear memory structures ($r > 0.98$).
  5. Scaled kernel metrics with `StandardScaler`.

### 3. NSL-KDD (Baseline Benchmark)
- **Problem:** Headerless raw text files with 41 unstructured fields and over 38 sub-attack labels.
- **Transformations:**
  1. Assigned official KDD column headers.
  2. Mapped 38 specific attacks to the 5 canonical academic classes:
     - `normal`, `dos`, `probe`, `r2l`, `u2r`.
  3. Encoded protocol types (`tcp`, `udp`, `icmp`), service ports, and TCP flags (`SF`, `S0`, `REJ`, etc.).
  4. Stratified on `attack_class`.

### 4. Recovery Trust Score (RTS) Benchmark (For TCRP Engine)
- **Mathematical Compliance Check:**
  Every record was verified against our formal equation:
  $$\text{BaseTrust} = 0.30 I + 0.30 V + 0.25 T + 0.15 F$$
  $$\text{RTS} = \text{BaseTrust} \times (1 - R)$$
  *Result:* Max divergence across all 500 samples was $0.000112$ (within floating-point rounding precision).
- **Ordinal Encoding of Trust States:**
  - `UNTRUSTED` $\to 0$ (Hard rejection / $RTS < 0.40$)
  - `UNCERTAIN` $\to 1$ (Sandbox test / $0.40 \le RTS < 0.75$)
  - `TRUSTED` $\to 2$ (Autonomous restore eligible / $RTS \ge 0.75$)

---

## ⚖️ Class Imbalance Mitigation

Cybersecurity datasets exhibit severe class imbalance (normal traffic drastically outnumbers attacks). To resolve this without synthetic data distortion on validation/test sets:

1. **Inverse-Frequency Balanced Class Weights:**
   $$w_j = \frac{n}{k \cdot n_j}$$
   Where $n$ is total training samples, $k$ is number of classes, and $n_j$ is samples in class $j$.
2. **Computed and Saved:**
   The exact weights are stored in each dataset's `metadata.json`:
   - UNSW-NB15 binary: `Normal: 0.902`, `Attack: 1.121`
   - UNSW-NB15 multi-class: Rare classes like `Worms` receive high penalty weights ($w \approx 42.1$), preventing models from ignoring stealthy threats.
   - CIC-MalMem: Balanced 50/50 weights ($w = 1.0$).

---

## 🛡️ Data Leakage Prevention Guarantee

To guarantee strict academic and scientific validity:
1. **Fit on Train Only:** `RobustScaler`, `StandardScaler`, `LabelEncoder`, and `VarianceThreshold` are strictly fitted on `train_df`. Validation and Test sets are transformed using the pre-fitted parameters.
2. **Index Disjointness:** Automated assertion guarantees:
   $$\text{Train}_{\text{indices}} \cap \text{Val}_{\text{indices}} = \emptyset, \quad \text{Train}_{\text{indices}} \cap \text{Test}_{\text{indices}} = \emptyset, \quad \text{Val}_{\text{indices}} \cap \text{Test}_{\text{indices}} = \emptyset$$
3. **Artifact Persistence:** Fitted objects are serialized to `.joblib` in `preprocessing/artifacts/` so the live inference agents in Phase 3 load the exact training transformation parameters.

---

## 🚀 How to Run the Pipeline

To re-run or verify all preprocessing steps locally:

```powershell
# Navigate to project repository
cd d:\Capstone-221\Incident-Response-and-Resilient-Recovery

# Execute master pipeline
python preprocessing/run_all_preprocessing.py
```

Outputs will be populated in:
- `datasets/processed/unsw_nb15/`
- `datasets/processed/cic_malmem/`
- `datasets/processed/nsl_kdd/`
- `datasets/processed/rts_benchmark/`
- `preprocessing/artifacts/`
- `preprocessing/preprocessing_summary_report.json`
