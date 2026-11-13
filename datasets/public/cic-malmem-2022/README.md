# CIC-MalMem-2022: Obfuscated Malware Memory Forensics Dataset

## Overview
CIC-MalMem-2022 was developed by the Canadian Institute for Cybersecurity (CIC) at the University of New Brunswick to detect obfuscated malware in volatile memory (RAM) that bypasses static disk detection.

- **Source**: University of New Brunswick (UNB) / CIC
- **URL**: https://www.unb.ca/cic/datasets/malmem-2022.html
- **Kaggle Mirror**: `dhoogla/cic-malmem-2022`
- **Format**: CSV / Parquet
- **Size**: ~50 MB CSV
- **Total Records**: 58,596 rows (perfectly balanced: 29,298 Benign, 29,298 Malicious)

## Malware Classes and Families Covered
1. **Ransomware** (Critical for Project Scope):
   - `Conti`, `MAZE`, `Pysa`, `Ako`, `Shade`
2. **Spyware**:
   - `180Solutions`, `Coolwebsearch`, `Gator`, `Transponder`, `TIBS`
3. **Trojan Horses**:
   - `Zeus`, `Emotet`, `Refroso`, `Scar`, `Reconyc`

## Key Forensic Memory Features (Extracted via VolMemLyzer)
- `pslist.nproc`, `pslist.nppid`, `pslist.avg_threads`: Process count and hierarchy
- `dlllist.ndlls`, `dlllist.avg_dlls_per_proc`: Loaded dynamic link libraries
- `handles.nhandles`, `handles.nport`, `handles.nfile`: Open handles, sockets, files
- `ldrmodules.not_in_load`, `ldrmodules.not_in_init`: Unlinked modules (stealth injection)
- `malfind.ninjections`, `malfind.commitCharge`: Injected code sections and memory permissions
- `svcscan.nservices`: Background Windows services running

## Project Role: Trust Agent & RTS Formulation
This dataset provides direct empirical input for the **Recovery Trust Score (RTS)**:
- **$T$ (Threat-Free Confidence)**: Evaluating whether an in-memory snapshot or restored state exhibits active ransomware indicators.
- **$R$ (Reinfection Risk)**: High injection counts or suspicious hidden handles immediately increase $R$, gating recovery points from autonomous execution.
- **Validation Agent**: Post-recovery verification that systems brought online are free of residual memory implants.

## Download Instructions
```bash
python datasets/scripts/download_all.py --dataset cic-malmem-2022
# Or download directly from Kaggle:
kaggle datasets download -d dhoogla/cic-malmem-2022 -p datasets/public/cic-malmem-2022/ --unzip
```

