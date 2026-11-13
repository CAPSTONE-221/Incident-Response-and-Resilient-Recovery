"""
Script: simulate_ransomware_activity.py
Description: Safe, controlled simulation of ransomware-like file mutation for generating
             forensic telemetry and recovery point evaluation data in a local VM sandbox.
Safety: Operates ONLY inside a temporary designated sandbox folder. Does NOT touch system files.
"""

import os
import sys
import time
import math
import hashlib
from datetime import datetime

def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    entropy = 0.0
    for x in range(256):
        p_x = float(data.count(bytes([x]))) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log2(p_x)
    return entropy

def run_simulation(target_sandbox: str, num_files: int = 20):
    os.makedirs(target_sandbox, exist_ok=True)
    telemetry_log = []
    
    print(f"[*] Initializing Controlled Ransomware Simulation in: {target_sandbox}")
    print("[*] Creating benign dummy files...")
    
    file_paths = []
    for i in range(num_files):
        p = os.path.join(target_sandbox, f"document_{i+1:02d}.txt")
        benign_content = f"Sensitive customer record #{i*1039}. Benign corporate data.\n" * 50
        with open(p, "w", encoding="utf-8") as f:
            f.write(benign_content)
        file_paths.append(p)
        
    print(f"[+] Created {len(file_paths)} benign documents.")
    
    # Simulate attacker delay / dwell time
    time.sleep(1)
    
    print("[*] Simulating fast encryption phase (mutating bytes, increasing entropy, appending .locked extension)...")
    for p in file_paths:
        t_start = datetime.utcnow().isoformat()
        with open(p, "rb") as f:
            raw = f.read()
        pre_hash = hashlib.sha256(raw).hexdigest()
        pre_entropy = calculate_entropy(raw)
        
        # Controlled pseudo-encryption (XOR with key)
        key = b"\xAA\xBB\xCC\xDD"
        encrypted = bytes([b ^ key[idx % len(key)] for idx, b in enumerate(raw)])
        post_entropy = calculate_entropy(encrypted)
        
        new_path = p + ".locked"
        with open(new_path, "wb") as f:
            f.write(encrypted)
        os.remove(p)
        
        post_hash = hashlib.sha256(encrypted).hexdigest()
        t_end = datetime.utcnow().isoformat()
        
        telemetry_log.append({
            "timestamp": t_end,
            "event_type": "FILE_MUTATION_HIGH_ENTROPY",
            "original_file": os.path.basename(p),
            "renamed_file": os.path.basename(new_path),
            "pre_sha256": pre_hash,
            "post_sha256": post_hash,
            "pre_entropy": round(pre_entropy, 4),
            "post_entropy": round(post_entropy, 4),
            "suspicious_entropy_delta": round(post_entropy - pre_entropy, 4)
        })
        
    print(f"[+] Simulation complete. {len(telemetry_log)} file encryption events logged.")
    return telemetry_log

if __name__ == "__main__":
    sandbox = os.path.join(os.path.dirname(__file__), "sandbox_test")
    logs = run_simulation(sandbox, num_files=10)
    print("\n[+] Sample Generated Telemetry:")
    for log in logs[:3]:
        print(f"    - [{log['timestamp']}] {log['original_file']} -> {log['renamed_file']} (Entropy: {log['pre_entropy']} -> {log['post_entropy']})")
    print(f"\n[i] Cleaning up sandbox directory: {sandbox}")
    import shutil
    shutil.rmtree(sandbox, ignore_errors=True)

