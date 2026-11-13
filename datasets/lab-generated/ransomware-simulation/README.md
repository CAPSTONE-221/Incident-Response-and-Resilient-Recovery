# Controlled Ransomware Simulation Dataset

## Overview
To evaluate our agentic incident response and resilient recovery system under the primary evaluation scenario (ransomware attack), we conduct safe, controlled adversary simulations inside isolated virtual machine environments.

> [!CAUTION]
> Never execute real ransomware binaries in uncontained environments. All simulations in this project use controlled benign simulation scripts or authorized adversary emulation frameworks (such as MITRE CALDERA and Atomic Red Team).

## Simulation Objectives
1. **Trigger Multi-Modal Telemetry**:
   - High-rate file modifications with high entropy (Sysmon Event ID 11 / Zeek File Extraction)
   - Process creation and injection patterns (Sysmon Event ID 1, 8, 10)
   - Volume Shadow Copy deletion attempts (`vssadmin delete shadows /all /quiet`)
   - Network beaconing / C2 callbacks (Sysmon Event ID 3)
2. **Generate Multiple Recovery Point Snapshots**:
   - Snapshot $T_0$: Baseline clean system (24h before breach)
   - Snapshot $T_1$: Baseline clean system (2h before breach)
   - Snapshot $T_2$: Attacker footholds established (dormant webshell / persistence script)
   - Snapshot $T_3$: Active lateral movement & credential dumping
   - Snapshot $T_4$: Post-encryption impacted system

## Telemetry Captured
- Endpoint Windows Event Logs (`.evtx` and exported `.json`)
- Sysmon Process & Network Telemetry
- Memory Forensics Dumps (`.raw` memory dumps processed via Volatility)
- Backup Repository Audit Logs & Hash Tables

## Simulation Script
A safe lab simulation script is provided in `simulate_ransomware_activity.py` which encrypts only dummy canary files inside a dedicated sandbox directory while recording detailed forensic timestamps.

