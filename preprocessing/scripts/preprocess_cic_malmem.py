"""
Script: preprocess_cic_malmem.py
Description: Full preprocessing pipeline for CIC-MalMem-2022 (used by Trust Agent & Validation Agent).
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
    print("   PROCESSING CIC-MALMEM-2022 DATASET (FOR TRUST & VALIDATION AGENTS)   ")
    print("=" * 75)

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    src_csv = os.path.join(base_dir, "datasets", "public", "cic-malmem-2022", "Obfuscated-MalMem2022.csv")
    out_dir = os.path.join(base_dir, "datasets", "processed", "cic_malmem")
    artifacts_dir = os.path.join(base_dir, "preprocessing", "artifacts")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(artifacts_dir, exist_ok=True)

    print(f"[*] Loading raw dataset from: {src_csv}")
    df_raw = pd.read_csv(src_csv)
    print(f"[+] Loaded {len(df_raw):,} records with {df_raw.shape[1]} features.")

    # 1. Feature Engineering: Extract malware_type and malware_family from 'Category'
    print("[*] Step 1: Parsing malware type and family taxonomy from Category...")
    df_clean = df_raw.copy()
    
    def parse_category(cat: str):
        if not isinstance(cat, str) or cat.lower() == "benign":
            return "Benign", "Benign"
        parts = cat.split("-")
        m_type = parts[0] if len(parts) > 0 else "Unknown"
        m_family = parts[1] if len(parts) > 1 else m_type
        return m_type, m_family

    parsed = df_clean["Category"].apply(parse_category)
    df_clean["malware_type"] = [p[0] for p in parsed]
    df_clean["malware_family"] = [p[1] for p in parsed]

    # Binary label: 0 for Benign, 1 for Malware
    df_clean["is_malware"] = (df_clean["Class"].str.lower() != "benign").astype(int)

    # 2. Clean missing/inf/duplicate data
    print("[*] Step 2: Cleaning missing/infinite values...")
    cleaner = DataCleaner(drop_columns=["Class", "Category"])
    df_clean = cleaner.fit_transform(df_clean)

    # 3. Stratified Train (70%) / Validation (15%) / Test (15%)
    print("[*] Step 3: Stratified Train/Val/Test split on malware_type...")
    splitter = DataSplitter(train_ratio=0.70, val_ratio=0.15, test_ratio=0.15, random_seed=42)
    train_df, val_df, test_df = splitter.split(df_clean, stratify_col="malware_type")
    split_stats = splitter.get_split_stats(train_df, val_df, test_df)
    print(f"    - Train set: {split_stats['train_samples']:,} samples ({split_stats['train_percent']}%)")
    print(f"    - Val set:   {split_stats['val_samples']:,} samples ({split_stats['val_percent']}%)")
    print(f"    - Test set:  {split_stats['test_samples']:,} samples ({split_stats['test_percent']}%)")

    # 4. Class Imbalance Analysis
    print("[*] Step 4: Computing class weights for malware families and types...")
    imbalance_binary = ClassImbalanceHandler(target_column="is_malware").fit(train_df["is_malware"])
    imbalance_type = ClassImbalanceHandler(target_column="malware_type").fit(train_df["malware_type"])

    # 5. Feature Selection (Drop zero/low-variance kernel features on train only)
    print("[*] Step 5: Filtering zero-variance memory features...")
    selector = FeatureSelector(
        variance_threshold=0.0001,
        correlation_threshold=0.98,
        exclude_columns=["is_malware", "malware_type", "malware_family"]
    )
    train_selected = selector.fit_transform(train_df)
    val_selected = selector.transform(val_df)
    test_selected = selector.transform(test_df)
    if selector.dropped_variance_cols_:
        print(f"    - Dropped zero-variance columns: {selector.dropped_variance_cols_}")
    if selector.dropped_correlation_cols_:
        print(f"    - Dropped collinear columns: {selector.dropped_correlation_cols_}")

    # 6. Scaling & Encoding
    print("[*] Step 6: StandardScaling memory features and encoding targets...")
    transformer = FeatureTransformer(
        scaler_type="StandardScaler",
        categorical_columns=[],
        target_columns=["is_malware", "malware_type", "malware_family"],
        artifacts_dir=artifacts_dir
    )
    train_proc = transformer.fit_transform(train_selected)
    val_proc = transformer.transform(val_selected)
    test_proc = transformer.transform(test_selected)
    saved_artifacts = transformer.save_artifacts("cic_malmem")

    # 7. Save outputs
    print("[*] Step 7: Saving standardized splits and metadata...")
    train_proc.to_csv(os.path.join(out_dir, "train.csv"), index=False)
    val_proc.to_csv(os.path.join(out_dir, "val.csv"), index=False)
    test_proc.to_csv(os.path.join(out_dir, "test.csv"), index=False)

    metadata = {
        "dataset_name": "CIC-MalMem-2022 (Processed)",
        "intended_agent": "Trust Agent (RTS Threat-Free Confidence T) & Validation Agent",
        "features_count": train_proc.shape[1],
        "feature_names": list(train_proc.columns),
        "split_statistics": split_stats,
        "class_imbalance_binary": imbalance_binary.get_summary(),
        "class_imbalance_malware_type": imbalance_type.get_summary(),
        "artifacts": saved_artifacts
    }
    with open(os.path.join(out_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"[+] CIC-MalMem-2022 preprocessing complete! Outputs saved in: {out_dir}")
    return metadata

if __name__ == "__main__":
    run()
