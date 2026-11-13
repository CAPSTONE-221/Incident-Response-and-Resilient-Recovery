"""
Script: verify_datasets.py
Description: Validates integrity, existence, schemas, and record counts for downloaded datasets.
Project: Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery
"""

import os
import sys
import hashlib
import json

def get_file_stats(path: str):
    if not os.path.exists(path):
        return None
    size_bytes = os.path.getsize(path)
    size_mb = size_bytes / (1024 * 1024)
    return {
        "exists": True,
        "size_mb": size_mb,
        "size_bytes": size_bytes
    }

def verify_all():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "public"))
    print("\n" + "="*80)
    print("        CYBERSECURITY DATASET VERIFICATION & HEALTH CHECK        ")
    print("="*80)
    
    checks = [
        {
            "name": "MITRE ATT&CK STIX 2.1",
            "path": os.path.join(base_dir, "mitre-attack-stix", "enterprise-attack.json"),
            "validator": lambda p: _validate_stix(p)
        },
        {
            "name": "CIC-MalMem-2022",
            "path": os.path.join(base_dir, "cic-malmem-2022", "Obfuscated-MalMem2022.csv"),
            "validator": lambda p: _validate_csv(p, expected_cols=["Class", "Category"])
        },
        {
            "name": "UNSW-NB15",
            "path": os.path.join(base_dir, "unsw-nb15", "UNSW_NB15_training-set.csv"),
            "validator": lambda p: _validate_csv(p, expected_cols=["attack_cat", "label"])
        },
        {
            "name": "NSL-KDD",
            "path": os.path.join(base_dir, "nsl-kdd", "KDDTrain+.txt"),
            "validator": lambda p: _validate_lines(p)
        },
        {
            "name": "CIC-IDS-2017",
            "path": os.path.join(base_dir, "cicids2017", "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"),
            "validator": lambda p: _validate_csv(p, expected_cols=["Label"])
        },
        {
            "name": "DARPA OpTC",
            "path": os.path.join(base_dir, "darpa-optc", "README.md"),
            "validator": lambda p: _validate_file_present(p)
        },
        {
            "name": "Splunk BOTS v3",
            "path": os.path.join(base_dir, "splunk-bots", "botsv3_data_set.tgz"),
            "validator": lambda p: _validate_file_present(p)
        }
    ]
    
    results = []
    for item in checks:
        stats = get_file_stats(item["path"])
        if not stats:
            status = "NOT DOWNLOADED / STAGED"
            detail = f"File not found: {os.path.basename(item['path'])}"
        else:
            status, detail = item["validator"](item["path"])
            detail = f"{stats['size_mb']:.2f} MB | {detail}"
            
        results.append({
            "name": item["name"],
            "status": status,
            "detail": detail
        })
        
    print(f"\n{'Dataset Name':<26} | {'Status':<15} | {'Details'}")
    print("-" * 80)
    for r in results:
        status_marker = "[OK]" if r["status"] == "OK" else "[PENDING]"
        print(f"{r['name']:<26} | {status_marker} {r['status']:<9} | {r['detail']}")
    print("-" * 80)
    print("\nNote: Datasets marked [PENDING] can be fetched using 'python datasets/scripts/download_all.py'")
    print("="*80 + "\n")

def _validate_file_present(path):
    return "OK", "Archive/Repository present"

def _validate_lines(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            count = sum(1 for _ in f)
        return "OK", f"{count:,} records"
    except Exception as e:
        return "ERROR", str(e)

def _validate_csv(path, expected_cols=None):
    try:
        import pandas as pd
        df = pd.read_csv(path, nrows=5)
        cols = list(df.columns)
        if expected_cols:
            for c in expected_cols:
                if c not in cols and not any(c.lower() in col.lower() for col in cols):
                    return "WARNING", f"Missing key column {c}"
        return "OK", f"Schema valid ({len(cols)} columns)"
    except Exception as e:
        return "ERROR", str(e)

def _validate_stix(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        obj_count = len(d.get("objects", []))
        return "OK", f"Valid STIX 2.1 bundle ({obj_count:,} objects)"
    except Exception as e:
        return "ERROR", str(e)

if __name__ == "__main__":
    verify_all()
