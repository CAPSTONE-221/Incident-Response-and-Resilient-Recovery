"""
Script: preprocess_nsl_kdd.py
Description: Full preprocessing pipeline for NSL-KDD benchmark (used as baseline for Triage Agent).
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

NSL_KDD_COLUMNS = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
    "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
    "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "difficulty"
]

ATTACK_5_CLASS_MAP = {
    # Normal
    "normal": "normal",
    # DoS
    "neptune": "dos", "back": "dos", "land": "dos", "pod": "dos", "smurf": "dos",
    "teardrop": "dos", "mailbomb": "dos", "apache2": "dos", "processtable": "dos",
    "udpstorm": "dos",
    # Probe
    "ipsweep": "probe", "nmap": "probe", "portsweep": "probe", "satan": "probe",
    "mscan": "probe", "saint": "probe",
    # R2L
    "ftp_write": "r2l", "guess_passwd": "r2l", "imap": "r2l", "multihop": "r2l",
    "phf": "r2l", "spy": "r2l", "warezclient": "r2l", "warezmaster": "r2l",
    "sendmail": "r2l", "named": "r2l", "snmpgetattack": "r2l", "snmpguess": "r2l",
    "xlock": "r2l", "xsnoop": "r2l", "worm": "r2l",
    # U2R
    "buffer_overflow": "u2r", "loadmodule": "u2r", "perl": "u2r", "rootkit": "u2r",
    "httptunnel": "u2r", "ps": "u2r", "sqlattack": "u2r", "xterm": "u2r"
}

def run():
    print("\n" + "=" * 75)
    print("      PROCESSING NSL-KDD DATASET (BASELINE BENCHMARK)       ")
    print("=" * 75)

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    train_src = os.path.join(base_dir, "datasets", "public", "nsl-kdd", "KDDTrain+.txt")
    test_src = os.path.join(base_dir, "datasets", "public", "nsl-kdd", "KDDTest+.txt")
    out_dir = os.path.join(base_dir, "datasets", "processed", "nsl_kdd")
    artifacts_dir = os.path.join(base_dir, "preprocessing", "artifacts")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(artifacts_dir, exist_ok=True)

    print(f"[*] Loading raw NSL-KDD train and test sources...")
    df_train_raw = pd.read_csv(train_src, names=NSL_KDD_COLUMNS)
    df_test_raw = pd.read_csv(test_src, names=NSL_KDD_COLUMNS)
    df_full = pd.concat([df_train_raw, df_test_raw], ignore_index=True)
    print(f"[+] Loaded {len(df_full):,} total records.")

    # 1. Map to 5 high-level classes & binary label
    print("[*] Step 1: Mapping attack types to 5 canonical categories (normal, dos, probe, r2l, u2r)...")
    df_clean = df_full.copy()
    df_clean["attack_class"] = df_clean["label"].str.lower().map(ATTACK_5_CLASS_MAP).fillna("other")
    df_clean["is_attack"] = (df_clean["attack_class"] != "normal").astype(int)

    # 2. Clean data
    cleaner = DataCleaner(drop_columns=["difficulty", "label"])
    df_clean = cleaner.fit_transform(df_clean)

    # 3. Stratified split
    print("[*] Step 2: Stratified Train (70%) / Validation (15%) / Test (15%) splitting...")
    splitter = DataSplitter(train_ratio=0.70, val_ratio=0.15, test_ratio=0.15, random_seed=42)
    train_df, val_df, test_df = splitter.split(df_clean, stratify_col="attack_class")
    split_stats = splitter.get_split_stats(train_df, val_df, test_df)

    # 4. Class Imbalance
    imbalance_binary = ClassImbalanceHandler(target_column="is_attack").fit(train_df["is_attack"])
    imbalance_multi = ClassImbalanceHandler(target_column="attack_class").fit(train_df["attack_class"])

    # 5. Feature selection
    print("[*] Step 3: Filtering constant and redundant features...")
    selector = FeatureSelector(
        variance_threshold=0.0001,
        correlation_threshold=0.98,
        exclude_columns=["is_attack", "attack_class"]
    )
    train_selected = selector.fit_transform(train_df)
    val_selected = selector.transform(val_df)
    test_selected = selector.transform(test_df)

    # 6. Scaling & Encoding
    print("[*] Step 4: StandardScaling numeric fields and encoding protocols/flags...")
    cat_cols = ["protocol_type", "service", "flag"]
    transformer = FeatureTransformer(
        scaler_type="StandardScaler",
        categorical_columns=cat_cols,
        target_columns=["is_attack", "attack_class"],
        artifacts_dir=artifacts_dir
    )
    train_proc = transformer.fit_transform(train_selected)
    val_proc = transformer.transform(val_selected)
    test_proc = transformer.transform(test_selected)
    saved_artifacts = transformer.save_artifacts("nsl_kdd")

    # 7. Save to disk
    train_proc.to_csv(os.path.join(out_dir, "train.csv"), index=False)
    val_proc.to_csv(os.path.join(out_dir, "val.csv"), index=False)
    test_proc.to_csv(os.path.join(out_dir, "test.csv"), index=False)

    metadata = {
        "dataset_name": "NSL-KDD (Processed)",
        "intended_agent": "Triage Agent (Fast Baseline Benchmark)",
        "features_count": train_proc.shape[1],
        "split_statistics": split_stats,
        "class_imbalance_binary": imbalance_binary.get_summary(),
        "class_imbalance_5class": imbalance_multi.get_summary(),
        "artifacts": saved_artifacts
    }
    with open(os.path.join(out_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"[+] NSL-KDD preprocessing complete! Outputs saved in: {out_dir}")
    return metadata

if __name__ == "__main__":
    run()

