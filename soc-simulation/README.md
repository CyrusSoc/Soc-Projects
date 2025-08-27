
# 🛡️ SOC Simulation: Kali → Raspberry Pi → Splunk

## 📌 Project Overview
This project simulates a **Security Operations Center (SOC)** workflow:
- **Kali Linux** (Attacker)
- **Raspberry Pi** (Victim + rsyslog forwarder)
- **Ubuntu with Splunk Enterprise** (SIEM)

Attacks are launched **from Kali → Raspberry Pi**. Raspberry writes to `/var/log/auth.log` and `/var/log/syslog`, then forwards logs to **Splunk** on Ubuntu for detection and alerting.

---

## ⚙️ Architecture
```
Kali (Attacker)  --->  Raspberry Pi (Victim + rsyslog)  --->  Ubuntu Splunk (SIEM)
```

---

## 🚀 Step 1: Configure Raspberry Pi (rsyslog → Splunk)
Edit `/etc/rsyslog.conf` on Raspberry Pi and add (replace the IP):
```conf
*.*   @<ubuntu-splunk-ip>:1514
```
Restart rsyslog:
```bash
sudo systemctl restart rsyslog
```
Optional checks:
```bash
logger "Test log from RaspberryPi"
tail -n 50 /var/log/syslog
```

---

## 🛠 Step 2: Configure Splunk (Ubuntu) to Receive Syslog
From the Ubuntu Splunk server:
```bash
sudo /opt/splunk/bin/splunk add udp 1514 -sourcetype syslog
sudo /opt/splunk/bin/splunk restart
```
Now Splunk will index incoming syslog over UDP 1514.

---

## ⚔️ Step 3: Generate Security Events (Kali → Raspberry Pi)

### 3.1 SSH Brute Force
```bash
hydra -l pi -P /usr/share/wordlists/rockyou.txt ssh://<raspberry-ip>
```

### 3.2 Port Scan
```bash
nmap -A <raspberry-ip>
```

### 3.3 Simple Failed SSH Login
```bash
ssh wronguser@<raspberry-ip>
```

These actions generate events in Raspberry’s system logs.

---

## 🔍 Step 4: Search & Detect in Splunk

### 4.1 All Raspberry logs
```spl
index=* sourcetype=syslog host=<raspberry-hostname>
```

### 4.2 SSH Brute Force Detection
```spl
index=* sourcetype=syslog host=<raspberry-hostname> "Failed password"
| stats count by src, user
| where count > 5
```

### 4.3 Nmap Port Scan Indicator
```spl
index=* sourcetype=syslog host=<raspberry-hostname> "nmap"
| stats count by src
```

---

## 🧰 Files in This Repo
- `configs/raspberry_rsyslog.conf` → Example rsyslog forwarding config
- `attacks/ssh_bruteforce.txt` → Hydra commands
- `attacks/port_scan.txt` → Nmap commands
- `splunk_queries/brute_force_detection.spl` → Brute-force detector
- `splunk_queries/port_scan_detection.spl` → Nmap detection

---

## ✅ Outcome
- End-to-end log pipeline (Raspberry → Splunk) working
- Realistic adversary simulation (Kali)
- Detections built in Splunk (SPL queries)
- Portfolio-ready project for SOC/Blue Team roles
