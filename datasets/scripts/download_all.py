"""
Script: download_all.py
Description: Master utility for downloading, tracking, and staging cybersecurity datasets.
Project: Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery
Team: Team 221
"""

import os
import sys
import argparse
import subprocess
import urllib.request
import json

DATASETS_CONFIG = {
    "mitre-attack-stix": {
        "name": "MITRE ATT&CK Enterprise STIX 2.1",
        "category": "Threat Intelligence",
        "target_dir": "datasets/public/mitre-attack-stix",
        "type": "direct_url",
        "url": "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json",
        "filename": "enterprise-attack.json"
    },
    "cic-malmem-2022": {
        "name": "CIC-MalMem-2022 (Obfuscated Malware Memory Forensics)",
        "category": "Malware & Ransomware",
        "target_dir": "datasets/public/cic-malmem-2022",
        "type": "kaggle",
        "kaggle_ref": "dhoogla/cic-malmem-2022"
    },
    "nsl-kdd": {
        "name": "NSL-KDD Benchmark Dataset",
        "category": "Intrusion Detection",
        "target_dir": "datasets/public/nsl-kdd",
        "type": "kaggle",
        "kaggle_ref": "hassan06/nslkdd"
    },
    "unsw-nb15": {
        "name": "UNSW-NB15 Intrusion Detection Dataset",
        "category": "Intrusion Detection",
        "target_dir": "datasets/public/unsw-nb15",
        "type": "kaggle",
        "kaggle_ref": "mrwellsdavid/unsw-nb15"
    },
    "cicids2017": {
        "name": "CIC-IDS-2017 Network Intrusion Detection",
        "category": "Intrusion Detection",
        "target_dir": "datasets/public/cicids2017",
        "type": "kaggle",
        "kaggle_ref": "cicdataset/cicids2017"
    },
    "cse-cic-ids2018": {
        "name": "CSE-CIC-IDS-2018 (AWS Open Data)",
        "category": "Intrusion Detection",
        "target_dir": "datasets/public/cse-cic-ids2018",
        "type": "aws_s3",
        "s3_uri": "s3://cse-cic-ids2018/"
    },
    "ctu13": {
        "name": "CTU-13 Botnet Dataset",
        "category": "Botnet & APT",
        "target_dir": "datasets/public/ctu13",
        "type": "kaggle",
        "kaggle_ref": "dhooge/ctu-13"
    },
    "ember": {
        "name": "EMBER 2018 v2 Malware PE Features",
        "category": "Malware",
        "target_dir": "datasets/public/ember",
        "type": "direct_url",
        "url": "https://ember.elastic.co/ember_dataset_2018_2.tar.bz2",
        "filename": "ember_dataset_2018_2.tar.bz2"
    },
    "darpa-optc": {
        "name": "DARPA OpTC Transparent Computing APT Telemetry",
        "category": "APT & Provenance",
        "target_dir": "datasets/public/darpa-optc",
        "type": "git_clone",
        "repo_url": "https://github.com/FiveDirections/OpTC-data.git"
    },
    "lanl-cyber": {
        "name": "LANL Multi-Source Cyber-Security Events Dataset",
        "category": "Enterprise Security Logs",
        "target_dir": "datasets/public/lanl-cyber",
        "type": "manual_or_csr",
        "portal_url": "https://csr.lanl.gov/data/cyber1/"
    },
    "otrf-security-datasets": {
        "name": "OTRF Security Datasets (Mordor ATT&CK telemetry)",
        "category": "Attack Simulation",
        "target_dir": "datasets/public/otrf-security-datasets",
        "type": "git_clone",
        "repo_url": "https://github.com/OTRF/Security-Datasets.git"
    },
    "splunk-bots": {
        "name": "Splunk Boss of the SOC (BOTSv3)",
        "category": "Enterprise Security Logs",
        "target_dir": "datasets/public/splunk-bots",
        "type": "direct_url",
        "url": "https://botsdataset.s3.amazonaws.com/botsv3/botsv3_data_set.tgz",
        "filename": "botsv3_data_set.tgz"
    }
}

def report_progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    if total_size > 0:
        percent = min(100.0, (downloaded / total_size) * 100)
        sys.stdout.write(f"\r    Downloading: {downloaded / (1024*1024):.2f} MB / {total_size / (1024*1024):.2f} MB ({percent:.1f}%)")
    else:
        sys.stdout.write(f"\r    Downloading: {downloaded / (1024*1024):.2f} MB")
    sys.stdout.flush()

def download_dataset(dataset_key: str, repo_root: str):
    if dataset_key not in DATASETS_CONFIG:
        print(f"[-] Unknown dataset: {dataset_key}. Available: {list(DATASETS_CONFIG.keys())}")
        return False
        
    cfg = DATASETS_CONFIG[dataset_key]
    dest_dir = os.path.join(repo_root, cfg["target_dir"])
    os.makedirs(dest_dir, exist_ok=True)
    
    print(f"\n==================================================================")
    print(f"Dataset:  {cfg['name']}")
    print(f"Category: {cfg['category']}")
    print(f"Target:   {dest_dir}")
    print(f"Type:     {cfg['type']}")
    print(f"==================================================================")
    
    dtype = cfg["type"]
    
    if dtype == "direct_url":
        target_file = os.path.join(dest_dir, cfg["filename"])
        if os.path.exists(target_file):
            print(f"[!] Target file already exists: {target_file} (Size: {os.path.getsize(target_file)/(1024*1024):.2f} MB)")
            return True
        print(f"[*] Downloading from: {cfg['url']}")
        urllib.request.urlretrieve(cfg["url"], target_file, reporthook=report_progress)
        print(f"\n[+] Successfully saved to {target_file}")
        return True
        
    elif dtype == "kaggle":
        ref = cfg["kaggle_ref"]
        print(f"[*] Kaggle dataset reference: {ref}")
        print(f"[*] Attempting download using Kaggle CLI: kaggle datasets download -d {ref} -p \"{dest_dir}\" --unzip")
        try:
            res = subprocess.run(["kaggle", "datasets", "download", "-d", ref, "-p", dest_dir, "--unzip"], capture_output=True, text=True)
            if res.returncode == 0:
                print(f"[+] Kaggle download succeeded:\n{res.stdout}")
                return True
            else:
                print(f"[!] Kaggle CLI note: {res.stderr.strip() or res.stdout.strip()}")
                print(f"[i] To download manually from Kaggle web UI:")
                print(f"    https://www.kaggle.com/datasets/{ref}")
                print(f"    Place extracted files into: {dest_dir}")
                return False
        except FileNotFoundError:
            print("[!] Kaggle CLI tool is not installed or not in PATH.")
            print(f"[i] Run: pip install kaggle, set ~/.kaggle/kaggle.json, or download manually from:")
            print(f"    https://www.kaggle.com/datasets/{ref}")
            return False
            
    elif dtype == "git_clone":
        repo_url = cfg["repo_url"]
        print(f"[*] Repository URL: {repo_url}")
        print(f"[*] Checking if already cloned...")
        if os.path.exists(os.path.join(dest_dir, ".git")):
            print(f"[+] Git repository already present at {dest_dir}")
            return True
        print(f"[*] Running shallow clone into {dest_dir}...")
        try:
            res = subprocess.run(["git", "clone", "--depth", "1", repo_url, dest_dir], capture_output=True, text=True)
            if res.returncode == 0:
                print(f"[+] Git clone completed.")
                return True
            else:
                print(f"[-] Git clone error: {res.stderr}")
                return False
        except Exception as e:
            print(f"[-] Clone failed: {e}")
            return False
            
    elif dtype == "aws_s3":
        print(f"[*] AWS S3 Open Data: {cfg['s3_uri']}")
        print(f"[i] To download specific files without sign-in, run:")
        print(f"    aws s3 ls --no-sign-request {cfg['s3_uri']}")
        print(f"    aws s3 cp --no-sign-request \"{cfg['s3_uri']}Processed Traffic Data for ML Algorithms/\" \"{dest_dir}\" --recursive")
        return True
        
    elif dtype == "manual_or_csr":
        print(f"[*] Dedicated research portal download required:")
        print(f"    Portal: {cfg['portal_url']}")
        print(f"    Follow terms and download tables (auth.txt.gz, proc.txt.gz, flows.txt.gz, redteam.txt.gz)")
        print(f"    Place into: {dest_dir}")
        return True

def list_datasets():
    print(f"\n{'Key':<25} | {'Category':<22} | {'Dataset Name'}")
    print("-" * 75)
    for k, v in DATASETS_CONFIG.items():
        print(f"{k:<25} | {v['category']:<22} | {v['name']}")
    print("-" * 75)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cybersecurity Datasets Downloader")
    parser.add_argument("--list", action="store_true", help="List all cataloged datasets")
    parser.add_argument("--dataset", type=str, help="Specify dataset key to download (or 'all')")
    args = parser.parse_args()
    
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    if args.list:
        list_datasets()
    elif args.dataset:
        if args.dataset == "all":
            for k in DATASETS_CONFIG:
                download_dataset(k, repo_root)
        else:
            download_dataset(args.dataset, repo_root)
    else:
        list_datasets()
        print("\nUsage example:")
        print("  python datasets/scripts/download_all.py --dataset mitre-attack-stix")
        print("  python datasets/scripts/download_all.py --dataset all")
