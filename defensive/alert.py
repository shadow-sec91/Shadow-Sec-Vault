import os
import time
import subprocess

# ASCII Art for Shadow-Sec (Aesthetics)
ascii_art = """
█████  ██      ███████ ██████  ████████     
██   ██ ██      ██      ██   ██    ██       
███████ ██      █████   ██████     ██       
██   ██ ██      ██      ██   ██    ██       
██   ██ ███████ ███████ ██   ██    ██    ██ 
"""

# Function to display the ASCII art at the start of the script
def display_ascii_art():
    print(ascii_art)
    time.sleep(0.8)  # Slight delay for aesthetics

# Function to trigger the alert and display suspicious activity
def trigger_alert(ip_address):
    print(f"\nALERT: Potential DDoS attack detected! Suspicious IP: {ip_address}")
    alert_sound()  # Trigger the alert sound
    alert_terminal_output(ip_address)  # Trigger terminal output for APS
def alert_sound():
    try:
        subprocess.run(["aplay", "/home/neo/Downloads/alert.wav"], stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Alert sound not found. Ensure you have a sound package installed.")



def alert_terminal_output(ip_address):
    print(f"\n[SHADOW-SEC APS] - Triggering Alert for Suspicious IP: {ip_address}\n")
    print(f"--- Initializing System Defense Protocols ---")
    time.sleep(1.0)
    print(f"System protocols initialized...\n")
    
    time.sleep(1.0)  # Slight delay before the next action
    print(f"Scanning Network for Anomalies...")
    time.sleep(0.9)
    print(f"[SUCCESS] Network anomalies scan complete.\n")
    
    time.sleep(1.1)  # Longer delay to simulate more in-depth scanning
    print(f"Analyzing Incoming Traffic Patterns...")
    time.sleep(0.8)
    print(f"Incoming traffic analyzed.\n")
    
    time.sleep(1.0)
    print(f"Deploying Firewalls and Security Filters...")
    time.sleep(1.0)
    print(f"[SUCCESS] Firewalls deployed, security filters active.\n")
    
    time.sleep(0.9)
    print(f"Establishing Real-Time Threat Detection...")
    time.sleep(1.7)
    print(f"Threat detection system active.\n")
    
    time.sleep(2.1)  # Longer delay for realistic threat detection
    print(f"Activating Intrusion Detection System (IDS)...")
    time.sleep(0.9)
    print(f"IDS activated, monitoring for intrusions.\n")
    
    time.sleep(1.0)
    print(f"Verifying Firewall Configuration...")
    time.sleep(3.0)
    print(f"Firewall configuration verified.\n")
    
    time.sleep(1.9)
    print(f"Traffic Encryption Enabled: Securing Channels...")
    time.sleep(1.0)
    print(f"Traffic encryption enabled.\n")
    
    time.sleep(2.1)
    print(f"Deploying Advanced Persistent Threat (APT) Detection...")
    time.sleep(0.9)
    print(f"APT detection systems deployed.\n")
    
    time.sleep(2.0)
    print(f"Verifying Target IP Address...")
    time.sleep(5.1)
    print(f"Target IP verified.\n")
    
    time.sleep(0.8)
    print(f"Isolating Malicious IP from Network...")
    time.sleep(0.9)
    print(f"SUCCESS Suspicious IP isolated from network.\n")
    
    time.sleep(1.0)
    print(f"Performing Geolocation Analysis for Suspicious IP...")
    time.sleep(4.8)
    print(f"Geolocation analysis complete.\n")
    
    time.sleep(0.9)
    print(f"Initiating Threat Intelligence Collection...")
    time.sleep(2.0)
    print(f"Threat intelligence collection active.\n")
    
    time.sleep(0.7)
    print(f"Deploying Mitigation Measures...")
    time.sleep(1.1)
    print(f"[SUCCESS] Mitigation measures deployed.\n")
    
    time.sleep(1.0)
    print(f"Recalculating Attack Vectors...")
    time.sleep(0.8)
    print(f"Attack vectors recalculated.\n")
    
    time.sleep(0.9)
    print(f"Analyzing Potential Exploits in Traffic...")
    time.sleep(1.2)
    print(f"Potential exploits analyzed.\n")
    
    time.sleep(0.8)
    print(f"Remote Backups Activated...")
    time.sleep(6.0)
    print(f"Remote backups secured.\n")
    
    time.sleep(2.7)
    print(f"Network Traffic Analysis: Potential DDoS Attack Detected...")
    time.sleep(0.9)
    print(f"DDoS attack detected and flagged.\n")
    
    time.sleep(0.8)
    print(f"Blocking Malicious Traffic: {ip_address}")
    time.sleep(1.0)
    print(f"Malicious traffic blocked.\n")
    
    time.sleep(0.9)
    print(f"Enhanced Threat Detection Mode: Engaged")
    time.sleep(1.7)
    print(f"Threat detection mode enabled.\n")
    
    time.sleep(1.1)
    print(f"Activating Traffic Redirection Protocol...")
    time.sleep(0.8)
    print(f"Traffic redirection protocols active.\n")
    
    time.sleep(1.2)
    print(f"Deploying Zero-Day Exploit Mitigation...")
    time.sleep(0.9)
    print(f"Zero-day exploit mitigation deployed.\n")
    
    time.sleep(0.8)
    print(f"Conducting Heuristic Network Scan...")
    time.sleep(1.1)
    print(f"Heuristic network scan complete.\n")
    
    time.sleep(1.0)
    print(f"Cross-referencing with Threat Database...")
    time.sleep(7.7)
    print(f"Cross-referencing complete.\n")
    
    time.sleep(0.8)
    print(f"Automated Threat Intelligence Feed: Updating...")
    time.sleep(2.0)
    print(f"Threat intelligence feed updated.\n")
    
    time.sleep(1.0)
    print(f"Engaging Defensive Data Sanitization...")
    time.sleep(1.2)
    print(f"Data sanitization complete.\n")
    
    time.sleep(1.1)
    print(f"Security Log Monitoring: Threat Activity Detected...")
    time.sleep(2.9)
    print(f"Threat activity logged.\n")
    
    time.sleep(1.0)
    print(f"Dynamic Intrusion Blocking Activating...")
    time.sleep(3.4)
    print(f"Dynamic intrusion blocking engaged.\n")
    
    time.sleep(1.2)
    print(f"Securing Outbound Connections...")
    time.sleep(2.8)
    print(f"Outbound connections secured.\n")
    
    time.sleep(0.9)
    print(f"Engaging Advanced Malware Detection...")
    time.sleep(3.2)
    print(f"Advanced malware detection active.\n")
    
    time.sleep(1.1)
    print(f"Real-time Vulnerability Scan Running...")
    time.sleep(5.9)
    print(f"Vulnerability scan complete.\n")
    
    time.sleep(0.8)
    print(f"Threat Landscape Monitoring: Active")
    time.sleep(0.9)
    print(f"Threat landscape monitoring active.\n")
    
    time.sleep(1.0)
    print(f"Blocking Unauthorized Protocols...")
    time.sleep(4.2)
    print(f"Unauthorized protocols blocked.\n")
    
    time.sleep(1.0)
    print(f"System Integrity Check in Progress...")
    time.sleep(1.0)
    print(f"System integrity verified.. all system secured\n")
    
    time.sleep(1.1)
    print(f"Routing Traffic Through Secured Channels...")
    time.sleep(0.9)
    print(f"Traffic routing secured.\n")
    
    time.sleep(1.0)
    print(f"Isolating Affected Systems from Network...")
    time.sleep(2.1)
    print(f"Affected systems isolated.\n")
    
    time.sleep(0.9)
    print(f"Automated Traffic Filtering Activating...")
    time.sleep(1.0)
    print(f"Traffic filtering active.\n")
    
    time.sleep(1.2)
    print(f"Deploying Multi-layered Defense Strategies...")
    time.sleep(3.1)
    print(f"Multi-layered defenses deployed.\n")
    
    time.sleep(1.1)
    print(f"System Analysis Complete: No Threats Detected\n")
    time.sleep(1.2)
    print(f"APS system is clear.\n")

# Function to block suspicious IP addresses
def block_ip(ip_address):
    print(f"Blocking IP: {ip_address}")
    # Uncomment the line below if running as root to block the IP using iptables
    os.system(f"iptables -A INPUT -s {ip_address} -j DROP")

# Function to detect suspicious activity based on IP address
def detect_suspicious_activity(ip_address):
    # For simplicity, we trigger an alert if the IP ends with ".100"
    if ip_address.endswith(".100"):
        trigger_alert(ip_address)
        block_ip(ip_address)
    else:
        print(f"Checked {ip_address}, no suspicious activity detected.")

# Function to exit APS
def exit_aps():
    print("\nAll systems and network traffic secured. Exiting APS...\n")
    time.sleep(1.2)
    print("Goodbye, the APS system is now inactive.\n")
    exit(0)

# Main function to run the script
if __name__ == "__main__":
    # Display the ASCII art at the start
    display_ascii_art()

    # Simulate checking an IP address for suspicious activity
    suspicious_ip = "192.168.1.100"  # Example suspicious IP address
    detect_suspicious_activity(suspicious_ip)

    # Exit APS
    exit_aps()
