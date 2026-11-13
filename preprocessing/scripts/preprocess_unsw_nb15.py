"""
Script: preprocess_unsw_nb15.py
Description: Full preprocessing pipeline for the UNSW-NB15 dataset (used by the Triage Agent).
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
from preprocessing.pipelines.feature_selector import FeatureSelector
from preprocessing.pipelines.imbalance_handler import ClassImbalanceHandler
from preprocessing.pipelines.data_splitter import DataSplitter

def run():
    print("\n" + "=" * 75)
    print("      PROCESSING UNSW-NB15 DATASET (FOR TRIAGE AGENT)      ")
    print("=" * 75)

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    train_src = os.path.join(base_dir, "datasets", "public", "unsw-nb15", "UNSW_NB15_training-set.csv")
    test_src = os.path.join(base_dir, "datasets", "public", "unsw-nb15", "UNSW_NB15_testing-set.csv")
    out_dir = os.path.join(base_dir, "datasets", "processed", "unsw_nb15")
    artifacts_dir = os.path.join(base_dir, "preprocessing", "artifacts")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(artifacts_dir, exist_ok=True)

    print(f"[*] Loading raw sources:\n    - {train_src}\n    - {test_src}")
    df_train_raw = pd.read_csv(train_src)
    df_test_raw = pd.read_csv(test_src)
    df_full = pd.concat([df_train_raw, df_test_raw], ignore_index=True)
    print(f"[+] Loaded {len(df_full):,} total records with {df_full.shape[1]} features.")

    # 1. Clean data
    print("[*] Step 1: Cleaning missing values, infinite entries, and non-predictive IDs...")
    cleaner = DataCleaner(drop_columns=["id"])
    df_clean = cleaner.fit_transform(df_full)

    # Standardize attack_cat labels
    df_clean["attack_cat"] = df_clean["attack_cat"].fillna("Normal").astype(str).str.strip()
    df_clean["attack_cat"] = df_clean["attack_cat"].replace({
        "Backdoors": "Backdoor",
        "": "Normal",
        "nan": "Normal"
    })

    # Standardize service '-' to 'none'
    if "service" in df_clean.columns:
        df_clean["service"] = df_clean["service"].replace({"-": "none"})

    # 2. Stratified train/val/test split
    print("[*] Step 2: Stratified Train (70%) / Validation (15%) / Test (15%) splitting...")
    splitter = DataSplitter(train_ratio=0.70, val_ratio=0.15, test_ratio=0.15, random_seed=42)
    train_df, val_df, test_df = splitter.split(df_clean, stratify_col="attack_cat")
    split_stats = splitter.get_split_stats(train_df, val_df, test_df)
    print(f"    - Train set: {split_stats['train_samples']:,} samples ({split_stats['train_percent']}%)")
    print(f"    - Val set:   {split_stats['val_samples']:,} samples ({split_stats['val_percent']}%)")
    print(f"    - Test set:  {split_stats['test_samples']:,} samples ({split_stats['test_percent']}%)")

    # 3. Analyze class distribution and calculate balanced class weights
    print("[*] Step 3: Analyzing class imbalance and computing cost-sensitive weights...")
    imbalance_binary = ClassImbalanceHandler(target_column="label").fit(train_df["label"])
    imbalance_multi = ClassImbalanceHandler(target_column="attack_cat").fit(train_df["attack_cat"])

    # 4. Feature Selection (Low-variance & redundant collinear features on train only)
    print("[*] Step 4: Filtering zero-variance and collinear features (fitted on train)...")
    selector = FeatureSelector(
        variance_threshold=0.0001,
        correlation_threshold=0.98,
        exclude_columns=["label", "attack_cat"]
    )
    train_selected = selector.fit_transform(train_df)
    val_selected = selector.transform(val_df)
    test_selected = selector.transform(test_df)
    if selector.dropped_variance_cols_:
        print(f"    - Dropped low-variance columns: {selector.dropped_variance_cols_}")
    if selector.dropped_correlation_cols_:
        print(f"    - Dropped collinear columns: {selector.dropped_correlation_cols_}")

    # 5. Categorical Encoding & Numerical Scaling (Fit on Train only!)
    print("[*] Step 5: Encoding categoricals and RobustScaling numerical flows (Train-fit only)...")
    cat_cols = [c for c in ["proto", "service", "state"] if c in train_selected.columns]
    transformer = FeatureTransformer(
        scaler_type="RobustScaler",
        categorical_columns=cat_cols,
        target_columns=["label", "attack_cat"],
        artifacts_dir=artifacts_dir
    )
    train_proc = transformer.fit_transform(train_selected)
    val_proc = transformer.transform(val_selected)
    test_proc = transformer.transform(test_selected)
    saved_artifacts = transformer.save_artifacts("unsw_nb15")

    # 6. Save Processed Datasets
    print("[*] Step 6: Saving standardized splits to disk...")
    train_out = os.path.join(out_dir, "train.csv")
    val_out = os.path.join(out_dir, "val.csv")
    test_out = os.path.join(out_dir, "test.csv")
    train_proc.to_csv(train_out, index=False)
    val_proc.to_csv(val_out, index=False)
    test_proc.to_csv(test_out, index=False)

    metadata = {
        "dataset_name": "UNSW-NB15 (Processed)",
        "intended_agent": "Triage Agent (Incident Classification & Severity)",
        "features_count": train_proc.shape[1],
        "feature_names": list(train_proc.columns),
        "split_statistics": split_stats,
        "class_imbalance_binary": imbalance_binary.get_summary(),
        "class_imbalance_multiclass": imbalance_multi.get_summary(),
        "artifacts": saved_artifacts
    }
    with open(os.path.join(out_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"[+] UNSW-NB15 preprocessing complete! Outputs saved in: {out_dir}")
    return metadata

if __name__ == "__main__":
    run()
