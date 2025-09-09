# hash_checker_multi.py
import hashlib

# Load known bad hashes
bad_hashes = open("bad-hashes.txt").read().splitlines()

file = input("Enter file path: ")

# Read file in binary
with open(file, "rb") as f:
    data = f.read()

# Generate hashes
md5 = hashlib.md5(data).hexdigest()
sha1 = hashlib.sha1(data).hexdigest()
sha256 = hashlib.sha256(data).hexdigest()

print(f"MD5:    {md5}")
print(f"SHA1:   {sha1}")
print(f"SHA256: {sha256}")

# Check against bad list
if md5 in bad_hashes:
    print("[!] ALERT: Malicious file detected! (MD5 match)")
elif sha1 in bad_hashes:
    print("[!] ALERT: Malicious file detected! (SHA1 match)")
elif sha256 in bad_hashes:
    print("[!] ALERT: Malicious file detected! (SHA256 match)")
else:
    print("[+] File is clean")
