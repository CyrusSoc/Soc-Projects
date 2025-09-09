# Malicious Hash Detector

## Overview
This project simulates a **basic malware detection system** using file integrity verification.  
It checks file hashes (MD5, SHA1, SHA256) against a list of **known malicious hashes**.

## Features
- Supports **MD5, SHA1, and SHA256** hashing
- Compares file hash against a malicious hash database
- Alerts if file is malicious, otherwise reports safe

## Project Files
- `bad-hashes.txt` → Contains hashes of malicious files
- `malicious-files/` → Contains 6 sample malicious text files
- `safe-files/` → Contains 2 safe text files
- `hash_checker_multi.py` → Main script to check file hashes

## Usage
1. Clone the repo:
   ```bash
   git clone <your_repo_link>
   cd hash-checker-project
   ```

2. Run the Python script:
   ```bash
   python3 hash_checker_multi.py
   ```

3. Enter the file path when prompted:
   ```
   Enter file path: malicious-files/malicious1.txt
   ```

4. Output:
   ```
   MD5:    <hash>
   SHA1:   <hash>
   SHA256: <hash>

   [!] ALERT: Malicious file detected! (SHA1 match)
   ```

## SOC Relevance
- Demonstrates knowledge of **file integrity monitoring (FIM)**
- Basic understanding of how SOC teams detect **Indicators of Compromise (IOCs)**
- Practice with **hashing algorithms** in Python
