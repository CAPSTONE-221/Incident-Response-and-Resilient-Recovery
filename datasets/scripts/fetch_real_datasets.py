"""
Script: fetch_real_datasets.py
Description: Directly downloads core cybersecurity datasets into their respective local directories.
"""

import os
import sys
import ssl
import urllib.request

# Allow standard HTTPS downloads without SSL cert errors on Windows
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATASETS_TO_DOWNLOAD = [
    {
        "name": "NSL-KDD Training Set",
        "url": "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain%2B.txt",
        "dest": os.path.join(BASE_DIR, "public", "nsl-kdd", "KDDTrain+.txt")
    },
    {
        "name": "NSL-KDD Testing Set",
        "url": "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTest%2B.txt",
        "dest": os.path.join(BASE_DIR, "public", "nsl-kdd", "KDDTest+.txt")
    },
    {
        "name": "UNSW-NB15 Training Set",
        "url": "https://huggingface.co/datasets/Mouwiya/UNSW-NB15/resolve/main/UNSW_NB15_training-set.csv",
        "dest": os.path.join(BASE_DIR, "public", "unsw-nb15", "UNSW_NB15_training-set.csv")
    },
    {
        "name": "UNSW-NB15 Testing Set",
        "url": "https://huggingface.co/datasets/Mouwiya/UNSW-NB15/resolve/main/UNSW_NB15_testing-set.csv",
        "dest": os.path.join(BASE_DIR, "public", "unsw-nb15", "UNSW_NB15_testing-set.csv")
    },
    {
        "name": "CIC-MalMem-2022 (Obfuscated Malware Memory)",
        "url": "https://raw.githubusercontent.com/atilimkoca/malware-classification/master/Obfuscated-MalMem2022.csv",
        "dest": os.path.join(BASE_DIR, "public", "cic-malmem-2022", "Obfuscated-MalMem2022.csv")
    },
    {
        "name": "CIC-IDS-2017 (DDoS Friday Sample Flow CSV)",
        "url": "https://huggingface.co/datasets/bencorn/CICIDS2017/resolve/main/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
        "dest": os.path.join(BASE_DIR, "public", "cicids2017", "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")
    }
]

def download_item(item):
    name = item["name"]
    url = item["url"]
    dest = item["dest"]
    
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest):
        sz_mb = os.path.getsize(dest) / (1024 * 1024)
        print(f"[!] {name} already exists ({sz_mb:.2f} MB). Skipping.")
        return
        
    print(f"\n[*] Downloading {name}...")
    print(f"    URL: {url}")
    print(f"    Destination: {dest}")
    
    def hook(count, block_size, total_size):
        dl = count * block_size
        if total_size > 0:
            p = min(100.0, (dl / total_size) * 100)
            sys.stdout.write(f"\r    Progress: {dl/(1024*1024):.2f} MB / {total_size/(1024*1024):.2f} MB ({p:.1f}%)")
        else:
            sys.stdout.write(f"\r    Downloaded: {dl/(1024*1024):.2f} MB")
        sys.stdout.flush()

    opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
    urllib.request.install_opener(opener)
    
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with opener.open(req) as resp, open(dest, "wb") as out_file:
        total = int(resp.headers.get("content-length", 0))
        downloaded = 0
        chunk_size = 1024 * 1024 # 1 MB
        while True:
            chunk = resp.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)
            downloaded += len(chunk)
            if total > 0:
                p = min(100.0, (downloaded / total) * 100)
                sys.stdout.write(f"\r    Progress: {downloaded/(1024*1024):.2f} MB / {total/(1024*1024):.2f} MB ({p:.1f}%)")
            else:
                sys.stdout.write(f"\r    Downloaded: {downloaded/(1024*1024):.2f} MB")
            sys.stdout.flush()
            
    print(f"\n[+] Successfully saved {name} ({os.path.getsize(dest)/(1024*1024):.2f} MB)")

if __name__ == "__main__":
    print("=" * 70)
    print("      DOWNLOADING REAL CYBERSECURITY DATASET FILES LOCALLY       ")
    print("=" * 70)
    for it in DATASETS_TO_DOWNLOAD:
        try:
            download_item(it)
        except Exception as e:
            print(f"\n[-] Error downloading {it['name']}: {e}")
            
    print("\n" + "=" * 70)
    print("[+] All available dataset downloads finished!")
    print("=" * 70)
