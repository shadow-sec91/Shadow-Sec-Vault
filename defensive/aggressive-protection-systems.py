import os
import time
import psutil
import logging

# Set up logging
logging.basicConfig(filename='/root/Shadow-Sec-Vault/logs/aps.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

# ASCII Art for Shadow-Sec (Aesthetics)
ascii_art = """
███████ ██   ██  █████  ██████   ██████  ██     ██       ███████ ███████  ██████ 
██      ██   ██ ██   ██ ██   ██ ██    ██ ██     ██       ██      ██      ██      
███████ ███████ ███████ ██   ██ ██    ██ ██  █  ██ █████ ███████ █████   ██      
     ██ ██   ██ ██   ██ ██   ██ ██    ██ ██ ███ ██            ██ ██      ██      
███████ ██   ██ ██   ██ ██████   ██████   ███ ███        ███████ ███████  ██████ 
                                                                                 
                                                                                 
                             █████  ██████  ███████                              
                            ██   ██ ██   ██ ██                                   
                            ███████ ██████  ███████                              
                            ██   ██ ██           ██                              
                            ██   ██ ██      ███████                              
"""

# Function to display the ASCII art
def display_ascii_art():
    print(ascii_art)
    time.sleep(0.8)

# Function to trigger the alert for suspicious IPs
def trigger_alert(ip_address):
    print(f"Triggering alert for suspicious IP: {ip_address}")
    os.system(f'xterm -e "python3 /root/Shadow-Sec-Vault/defensive/alert.py {ip_address}; bash"')
    logging.debug(f"Alert triggered for IP: {ip_address}")

# Function to deploy firewalls
def deploy_firewalls():
    if os.system("which ufw") == 0:
        print(f"[ACTION] Deploying firewalls...")
        os.system("sudo ufw enable")
        print(f"[SUCCESS] Firewalls deployed.")
    else:
        print(f"[WARNING] UFW not found. Skipping firewall deployment.")

# Function to monitor network traffic
def monitor_network():
    suspicious_ips = {}  # Track IPs with high traffic
    packet_count = {}    # Count packets per port
    alert_threshold = 1000  # Packets per second threshold
    time_window = 1      # Monitoring interval in seconds

    # Capture live network traffic
    connections = psutil.net_connections(kind='inet')

    for conn in connections:
        ip = conn.raddr.ip if conn.raddr else None
        port = conn.raddr.port if conn.raddr else None

        if ip and port:
            # Track packet counts for each port
            if port not in packet_count:
                packet_count[port] = 1
            else:
                packet_count[port] += 1

            # Track suspicious IPs
            if ip not in suspicious_ips:
                suspicious_ips[ip] = 1
            else:
                suspicious_ips[ip] += 1

    # Detect high packet rates per port
    for port, count in packet_count.items():
        if count > alert_threshold:
            print(f"\n[SUSPICIOUS] High traffic detected on port {port} ({count} packets/s)")
            logging.debug(f"High traffic detected on port {port}: {count} packets/s")

    # Detect potential DDoS or port scans
    for ip, count in suspicious_ips.items():
        if count > alert_threshold:
            print(f"\n[SUSPICIOUS] Potential DDoS detected from IP: {ip}")
            trigger_alert(ip)
            logging.debug(f"Potential DDoS detected from IP: {ip}")
    
    time.sleep(time_window)

# Main function
def main():
    display_ascii_art()
    print("Starting Aggressive Protection System...\n")
    
    print(f"--- Initializing Aggressive Protection System ---")
    time.sleep(1)
    print(f"[SUCCESS] Aggressive Protection System Activated.\n")
    time.sleep(1)
    print(f"Deploying Firewalls and Security Filters...")
    deploy_firewalls()
    print(f"\nStarting real-time network monitoring...\n")

    # Continuous monitoring
    while True:
        monitor_network()

if __name__ == "__main__":
    main()
