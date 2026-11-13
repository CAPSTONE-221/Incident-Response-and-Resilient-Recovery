"""
Script: generate_synthetic_rts_eval.py
Description: Generates a benchmark dataset of candidate recovery points for evaluating the
             Recovery Trust Score (RTS) and Trust-Conditioned Recovery Planning (TCRP).
Formula:
    BaseTrust = w1*I + w2*V + w3*T + w4*F
    RTS = BaseTrust * (1 - R)
    States:
        - TRUSTED:   RTS >= tau_high and no hard violation
        - UNCERTAIN: tau_low <= RTS < tau_high or evidence incomplete
        - UNTRUSTED: RTS < tau_low or hard violation
"""

import os
import random
import pandas as pd
import numpy as np

def generate_recovery_points(num_samples: int = 500, random_seed: int = 42) -> pd.DataFrame:
    random.seed(random_seed)
    np.random.seed(random_seed)
    
    # Weights for BaseTrust
    w1, w2, w3, w4 = 0.30, 0.30, 0.25, 0.15  # sum = 1.0
    tau_high = 0.75
    tau_low = 0.40
    
    records = []
    
    scenarios = ["clean_pre_compromise", "post_compromise_poisoned", "tampered_integrity", 
                 "compromised_backup_server", "uncertain_forensics", "safe_recent_incremental"]
    
    for i in range(1, num_samples + 1):
        rp_id = f"RP-{i:04d}"
        scenario = random.choices(
            scenarios, 
            weights=[0.35, 0.25, 0.15, 0.10, 0.10, 0.05], 
            k=1
        )[0]
        
        # Hard violation flag (e.g. confirmed malware in snapshot or compromised backup root)
        hard_violation = False
        
        if scenario == "clean_pre_compromise":
            # Backup occurred well before attack: high I, high V, high T, high F, low R
            I = np.clip(np.random.normal(0.95, 0.03), 0.85, 1.0)
            V = np.clip(np.random.normal(0.95, 0.04), 0.85, 1.0)
            T = np.clip(np.random.normal(0.98, 0.02), 0.90, 1.0)
            F = np.clip(np.random.normal(0.92, 0.05), 0.80, 1.0)
            R = np.clip(np.random.normal(0.05, 0.03), 0.0, 0.15)
            compromise_window_delta_hours = -random.randint(12, 168)  # 12 hours to 7 days before
            
        elif scenario == "post_compromise_poisoned":
            # Backup made after initial breach: I may be intact, but V and T are low, R is high
            I = np.clip(np.random.normal(0.90, 0.05), 0.70, 1.0)
            V = np.clip(np.random.normal(0.20, 0.10), 0.0, 0.35)
            T = np.clip(np.random.normal(0.25, 0.12), 0.0, 0.45)
            F = np.clip(np.random.normal(0.60, 0.15), 0.30, 0.85)
            R = np.clip(np.random.normal(0.75, 0.10), 0.50, 0.99)
            compromise_window_delta_hours = random.randint(1, 72)     # 1 to 72 hours after compromise
            if random.random() < 0.30:
                hard_violation = True  # Confirmed ransomware binary in restore tree
                
        elif scenario == "tampered_integrity":
            # Corrupted image, failed hash, or bad restore test
            I = np.clip(np.random.normal(0.25, 0.10), 0.0, 0.40)
            V = np.clip(np.random.normal(0.70, 0.20), 0.30, 1.0)
            T = np.clip(np.random.normal(0.70, 0.15), 0.40, 0.90)
            F = np.clip(np.random.normal(0.35, 0.12), 0.10, 0.55)
            R = np.clip(np.random.normal(0.40, 0.15), 0.15, 0.70)
            compromise_window_delta_hours = -random.randint(1, 48)
            if random.random() < 0.40:
                hard_violation = True  # Cryptographic hash verification failed
                
        elif scenario == "compromised_backup_server":
            # Backup host itself was accessed by adversary (high R, multiplicative risk penalty)
            I = np.clip(np.random.normal(0.85, 0.08), 0.65, 0.95)
            V = np.clip(np.random.normal(0.80, 0.10), 0.60, 0.95)
            T = np.clip(np.random.normal(0.40, 0.15), 0.10, 0.65)
            F = np.clip(np.random.normal(0.30, 0.10), 0.05, 0.50)
            R = np.clip(np.random.normal(0.88, 0.06), 0.75, 1.0)
            compromise_window_delta_hours = -random.randint(2, 24)
            hard_violation = True  # Compromised host overrides score
            
        elif scenario == "uncertain_forensics":
            # Missing logs, telemetry gaps, incomplete provenance
            I = np.clip(np.random.normal(0.85, 0.05), 0.75, 0.95)
            V = np.clip(np.random.normal(0.55, 0.10), 0.40, 0.70)
            T = np.clip(np.random.normal(0.60, 0.10), 0.45, 0.75)
            F = np.clip(np.random.normal(0.20, 0.08), 0.05, 0.35)
            R = np.clip(np.random.normal(0.30, 0.10), 0.15, 0.50)
            compromise_window_delta_hours = -random.randint(1, 20)
            
        else: # safe_recent_incremental
            I = np.clip(np.random.normal(0.98, 0.02), 0.92, 1.0)
            V = np.clip(np.random.normal(0.90, 0.03), 0.85, 0.98)
            T = np.clip(np.random.normal(0.95, 0.03), 0.90, 1.0)
            F = np.clip(np.random.normal(0.95, 0.03), 0.88, 1.0)
            R = np.clip(np.random.normal(0.03, 0.02), 0.0, 0.08)
            compromise_window_delta_hours = -random.randint(4, 36)

        base_trust = w1 * I + w2 * V + w3 * T + w4 * F
        rts = base_trust * (1.0 - R)
        
        # Policy determination
        if hard_violation or rts < tau_low:
            trust_state = "UNTRUSTED"
            recommendation = "EXCLUDE_FROM_RECOVERY"
            actual_clean_ground_truth = 0
        elif rts >= tau_high and not hard_violation:
            trust_state = "TRUSTED"
            recommendation = "ELIGIBLE_AUTONOMOUS_RESTORE"
            actual_clean_ground_truth = 1
        else:
            trust_state = "UNCERTAIN"
            recommendation = "REQUIRE_HUMAN_APPROVAL_AND_ISOLATION_TEST"
            actual_clean_ground_truth = 1 if scenario in ["clean_pre_compromise", "safe_recent_incremental"] else 0

        records.append({
            "recovery_point_id": rp_id,
            "scenario": scenario,
            "integrity_confidence_I": round(float(I), 4),
            "temporal_validity_V": round(float(V), 4),
            "threat_free_confidence_T": round(float(T), 4),
            "forensic_provenance_F": round(float(F), 4),
            "reinfection_risk_R": round(float(R), 4),
            "base_trust": round(float(base_trust), 4),
            "recovery_trust_score_RTS": round(float(rts), 4),
            "hard_security_violation": hard_violation,
            "trust_state": trust_state,
            "policy_recommendation": recommendation,
            "hours_relative_to_breach": compromise_window_delta_hours,
            "ground_truth_is_clean": actual_clean_ground_truth
        })

    df = pd.DataFrame(records)
    return df

if __name__ == "__main__":
    out_dir = os.path.dirname(__file__)
    out_csv = os.path.join(out_dir, "synthetic_rts_benchmark.csv")
    df = generate_recovery_points(num_samples=500)
    df.to_csv(out_csv, index=False)
    
    print("\n[+] Successfully generated Recovery Trust Score benchmark dataset:")
    print(f"    Path:    {out_csv}")
    print(f"    Samples: {len(df)}")
    print("\n[+] Distribution of Trust States:")
    print(df["trust_state"].value_counts())
    print("\n[+] Sample Records:")
    print(df[["recovery_point_id", "scenario", "recovery_trust_score_RTS", "trust_state", "policy_recommendation"]].head(6).to_string(index=False))
