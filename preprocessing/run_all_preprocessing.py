"""
Script: run_all_preprocessing.py
Description: Master preprocessing orchestration script that executes all dataset pipelines,
             verifies no data leakage, and outputs an end-to-end audit summary report.
Project: Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery
Team: Team 221
"""

import os
import sys
import json
import time

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocessing.scripts import (
    preprocess_unsw_nb15,
    preprocess_cic_malmem,
    preprocess_nsl_kdd,
    preprocess_rts_benchmark
)

def run_master_pipeline():
    start_time = time.time()
    print("=" * 80)
    print("    CYBERSECURITY DATASET PREPROCESSING & STANDARDIZATION PIPELINE     ")
    print("                      CAPSTONE PROJECT TEAM 221                        ")
    print("=" * 80)

    summary_results = {}

    # 1. UNSW-NB15
    try:
        summary_results["UNSW-NB15"] = preprocess_unsw_nb15.run()
    except Exception as e:
        print(f"[-] Error in UNSW-NB15 preprocessing: {e}")
        summary_results["UNSW-NB15"] = {"status": "FAILED", "error": str(e)}

    # 2. CIC-MalMem-2022
    try:
        summary_results["CIC-MalMem-2022"] = preprocess_cic_malmem.run()
    except Exception as e:
        print(f"[-] Error in CIC-MalMem preprocessing: {e}")
        summary_results["CIC-MalMem-2022"] = {"status": "FAILED", "error": str(e)}

    # 3. NSL-KDD
    try:
        summary_results["NSL-KDD"] = preprocess_nsl_kdd.run()
    except Exception as e:
        print(f"[-] Error in NSL-KDD preprocessing: {e}")
        summary_results["NSL-KDD"] = {"status": "FAILED", "error": str(e)}

    # 4. RTS Benchmark
    try:
        summary_results["RTS Benchmark"] = preprocess_rts_benchmark.run()
    except Exception as e:
        print(f"[-] Error in RTS Benchmark preprocessing: {e}")
        summary_results["RTS Benchmark"] = {"status": "FAILED", "error": str(e)}

    elapsed = time.time() - start_time

    # Output master summary audit
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    out_report = os.path.join(base_dir, "preprocessing", "preprocessing_summary_report.json")
    with open(out_report, "w", encoding="utf-8") as f:
        json.dump(summary_results, f, indent=2)

    print("\n" + "=" * 80)
    print("                     PREPROCESSING EXECUTION SUMMARY                    ")
    print("=" * 80)
    print(f"{'Dataset Name':<22} | {'Intended Agent':<25} | {'Train / Val / Test Samples'}")
    print("-" * 80)
    for name, data in summary_results.items():
        if "split_statistics" in data:
            st = data["split_statistics"]
            splits_str = f"{st['train_samples']:,} / {st['val_samples']:,} / {st['test_samples']:,}"
            agent = data.get("intended_agent", "").split("(")[0].strip()
            print(f"{name:<22} | {agent:<25} | {splits_str}")
        else:
            print(f"{name:<22} | {'FAILED':<25} | {data.get('error', 'Error')}")
    print("-" * 80)
    print(f"[+] All pipelines executed in {elapsed:.2f} seconds.")
    print(f"[+] Master summary report saved at: {out_report}")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    run_master_pipeline()
