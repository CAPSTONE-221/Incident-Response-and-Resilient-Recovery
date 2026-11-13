"""
Script: fetch_mitre_stix.py
Description: Downloads and validates the official MITRE Enterprise ATT&CK STIX 2.1 JSON bundle.
Project: Trust-Aware Agentic AI for Autonomous Cyber Incident Response and Resilient Recovery
"""

import os
import sys
import json
import urllib.request

STIX_URL = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json"
TARGET_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "public", "mitre-attack-stix"))
TARGET_FILE = os.path.join(TARGET_DIR, "enterprise-attack.json")

def download_file(url: str, dest_path: str):
    print(f"[*] Downloading MITRE ATT&CK STIX 2.1 from: {url}")
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    def report_hook(block_num, block_size, total_size):
        downloaded = block_num * block_size
        if total_size > 0:
            percent = min(100.0, (downloaded / total_size) * 100)
            sys.stdout.write(f"\r    Progress: {downloaded / (1024*1024):.2f} MB / {total_size / (1024*1024):.2f} MB ({percent:.1f}%)")
        else:
            sys.stdout.write(f"\r    Downloaded: {downloaded / (1024*1024):.2f} MB")
        sys.stdout.flush()

    urllib.request.urlretrieve(url, dest_path, reporthook=report_hook)
    print("\n[+] Download completed successfully.")

def validate_stix(file_path: str):
    print(f"[*] Validating STIX bundle structure: {file_path}")
    if not os.path.exists(file_path):
        print(f"[-] Error: File not found at {file_path}")
        return False
        
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    print(f"[+] File Size: {file_size_mb:.2f} MB")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    bundle_type = data.get("type")
    objects = data.get("objects", [])
    
    print(f"[+] STIX Object Type: {bundle_type}")
    print(f"[+] Total STIX Objects: {len(objects)}")
    
    type_counts = {}
    for obj in objects:
        t = obj.get("type", "unknown")
        type_counts[t] = type_counts.get(t, 0) + 1
        
    print("[+] Key MITRE ATT&CK Object Distribution:")
    for key in ["attack-pattern", "course-of-action", "malware", "tool", "intrusion-set", "relationship"]:
        if key in type_counts:
            print(f"    - {key}: {type_counts[key]}")
            
    return True

if __name__ == "__main__":
    download_file(STIX_URL, TARGET_FILE)
    validate_stix(TARGET_FILE)
