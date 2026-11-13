"""
Script: preprocess_rts_benchmark.py
Description: Preprocessing and validation pipeline for the Recovery Trust Score (RTS) benchmark
             (used by Trust Agent and Recovery Planner).
"""

import os
import sys
import json
import pandas as pd
import numpy as np

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from preprocessing.pipelines.cleaner import DataCleaner
from preprocessing.pipelines.encoder_scaler import FeatureTransformer
from preprocessing.pipelines.imbalance_handler import ClassImbalanceHandler
from preprocessing.pipelines.data_splitter import DataSplitter

def run():
    print("\n" + "=" * 75)
    print("   PROCESSING RECOVERY TRUST SCORE (RTS) BENCHMARK (FOR TCRP ENGINE)   ")
    print("=" * 75)

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    src_csv = os.path.join(base_dir, "datasets", "lab-generated", "backup-trust-validation", "synthetic_rts_benchmark.csv")
    out_dir = os.path.join(base_dir, "datasets", "processed", "rts_benchmark")
    artifacts_dir = os.path.join(base_dir, "preprocessing", "artifacts")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(artifacts_dir, exist_ok=True)

    print(f"[*] Loading raw RTS benchmark dataset from: {src_csv}")
    df_raw = pd.read_csv(src_csv)
    print(f"[+] Loaded {len(df_raw)} candidate recovery points across {df_raw.shape[1]} attributes.")

    # 1. Mathematical Validation: Verify RTS formula compliance
    print("[*] Step 1: Mathematically validating RTS and BaseTrust calculations...")
    expected_base = (
        0.30 * df_raw["integrity_confidence_I"] +
        0.30 * df_raw["temporal_validity_V"] +
        0.25 * df_raw["threat_free_confidence_T"] +
        0.15 * df_raw["forensic_provenance_F"]
    )
    expected_rts = expected_base * (1.0 - df_raw["reinfection_risk_R"])
    
    base_diff = np.abs(df_raw["base_trust"] - expected_base).max()
    rts_diff = np.abs(df_raw["recovery_trust_score_RTS"] - expected_rts).max()
    assert base_diff < 1e-3, f"BaseTrust calculation discrepancy detected: max diff = {base_diff}"
    assert rts_diff < 1e-3, f"RTS calculation discrepancy detected: max diff = {rts_diff}"
    print(f"[+] Formula verified! Max divergence = {max(base_diff, rts_diff):.6f}")

    # 2. Encode categorical trust states (Ordinal: UNTRUSTED=0, UNCERTAIN=1, TRUSTED=2)
    print("[*] Step 2: Ordinal encoding of trust states...")
    df_clean = df_raw.copy()
    state_mapping = {"UNTRUSTED": 0, "UNCERTAIN": 1, "TRUSTED": 2}
    df_clean["trust_state_code"] = df_clean["trust_state"].map(state_mapping)

    # 3. Stratified Split (70/15/15 on trust_state)
    print("[*] Step 3: Stratified Train/Val/Test splitting on trust_state...")
    splitter = DataSplitter(train_ratio=0.70, val_ratio=0.15, test_ratio=0.15, random_seed=42)
    train_df, val_df, test_df = splitter.split(df_clean, stratify_col="trust_state")
    split_stats = splitter.get_split_stats(train_df, val_df, test_df)

    # 4. Imbalance Analysis
    imbalance = ClassImbalanceHandler(target_column="trust_state").fit(train_df["trust_state"])

    # 5. Save splits to disk
    train_df.to_csv(os.path.join(out_dir, "train.csv"), index=False)
    val_df.to_csv(os.path.join(out_dir, "val.csv"), index=False)
    test_df.to_csv(os.path.join(out_dir, "test.csv"), index=False)

    metadata = {
        "dataset_name": "Recovery Trust Score (RTS) Benchmark (Processed)",
        "intended_agent": "Trust Agent (RTS Scoring) & Recovery Planner (Safe Selection)",
        "features_count": df_clean.shape[1],
        "split_statistics": split_stats,
        "trust_state_distribution": imbalance.get_summary(),
        "formula": "BaseTrust = 0.30*I + 0.30*V + 0.25*T + 0.15*F; RTS = BaseTrust * (1 - R)",
        "gates": {
            "tau_high": 0.75,
            "tau_low": 0.40,
            "hard_security_override": True
        }
    }
    with open(os.path.join(out_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"[+] RTS Benchmark preprocessing complete! Outputs saved in: {out_dir}")
    return metadata

if __name__ == "__main__":
    run()

