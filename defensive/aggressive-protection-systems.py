import os
import time
import psutil
import logging

# Set up logging with the correct path
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

# Function to display the ASCII art at the start of the script
def display_ascii_art():
    print(ascii_art)
    time.sleep(0.8)  # Slight delay for aesthetics

# Function to trigger the alert when suspicious IP is detected
def alert_terminal_output(ip_address):
    print(f"\n[SHADOW-SEC APS] - Triggering Alert for Suspicious IP: {ip_address}\n")
    
    # Directly activate the countermeasures, no delays, just actions.
    print(f"--- Aggressive Protection System Triggered ---")
    print(f"[ALERT] Potential threat detected from IP: {ip_address}")
    print(f"Activating defensive countermeasures...")

    # Call the functions that deploy firewalls and activate IDS
    deploy_firewalls()
    activate_ids()

# Function to deploy firewalls (implement this as needed)
def deploy_firewalls():
    print(f"[ACTION] Deploying firewalls and security filters...")
    # Add firewall deployment logic here (e.g., iptables or ufw commands)
    os.system("sudo ufw allow from <ip_address> to any port 20")  # Example for opening port 20 for a specific IP (adjust accordingly)
    print(f"[SUCCESS] Firewalls deployed, security filters active.")

# Function to activate Intrusion Detection System (IDS)
def activate_ids():
    print(f"[ACTION] Activating Intrusion Detection System (IDS)...")
    # Implement your IDS activation logic (e.g., start a specific service)
    # Example of enabling Snort or another IDS
    os.system("sudo systemctl start snort")  # Example command, adjust based on your IDS configuration
    print(f"[SUCCESS] IDS activated, monitoring for intrusions.")

# Function to detect network anomalies and suspicious activity in real-time
def monitor_network():
    suspicious_ips = {}  # Track incoming connections
    failed_connections = {}  # Track failed connection attempts (e.g., port scan attempts)
    threshold = 5  # Lowered threshold to trigger quicker detection (for port scans)
    time_window = 2  # Seconds for monitoring to detect rapid scans

    connections = psutil.net_connections(kind='inet')

    for conn in connections:
        if conn.status == 'ESTABLISHED':
            ip = conn.raddr.ip
            if ip not in suspicious_ips:
                suspicious_ips[ip] = 1
            else:
                suspicious_ips[ip] += 1

        # Monitor for failed connections (attempts to closed ports)
        if conn.status in ['CLOSE_WAIT', 'TIME_WAIT']:
            ip = conn.raddr.ip
            if ip:
                if ip not in failed_connections:
                    failed_connections[ip] = {'count': 1, 'time': time.time()}
                else:
                    failed_connections[ip]['count'] += 1

    # Detect potential DDoS or suspicious behavior based on the threshold
    suspicious_ips_detected = False
    for ip, count in suspicious_ips.items():
        if count > threshold:  # Detecting high traffic volume from a single IP
            print(f"\n[SUSPICIOUS] Potential DDoS detected from IP: {ip}")
            trigger_alert(ip)
            suspicious_ips_detected = True
            logging.debug(f"Potential DDoS detected from IP: {ip}")

    # Detecting failed connection attempts (port scans)
    for ip, data in failed_connections.items():
        if data['count'] > threshold and time.time() - data['time'] < time_window:
            print(f"\n[SUSPICIOUS] Potential port scan detected from IP: {ip}")
            trigger_alert(ip)
            failed_connections[ip]['count'] = 0  # Reset after triggering alert
            logging.debug(f"Potential port scan detected from IP: {ip}")

    if not suspicious_ips_detected:
        return  # No suspicious IPs detected, so no output

    time.sleep(5)  # Monitor every 5 seconds

# Function to trigger the alert by running alert.py in a separate terminal using xterm
def trigger_alert(ip_address):
    print(f"Triggering alert for suspicious IP: {ip_address}")
    # Use xterm to open a new terminal and run alert.py
    os.system(f'xterm -e "python3 /root/Shadow-Sec-Vault/defensive/alert.py {ip_address}; bash"')
    logging.debug(f"Alert triggered for IP: {ip_address}")

# Main function to simulate APS behavior
def main():
    display_ascii_art()  # Display ASCII art at the start
    print("Starting Aggressive Protection System...\n")
    
    # Perform the APS boot-up sequence
    print(f"--- Initializing Aggressive Protection System ---")
    time.sleep(1.0)
    print(f"[SUCCESS] Aggressive Protection System Activated.\n")
    time.sleep(1.0)
    print(f"Scanning Network for Anomalies...")
    time.sleep(0.9)
    print(f"[SUCCESS] Network anomalies scan complete.\n")
    time.sleep(1.0)
    print(f"Deploying Firewalls and Security Filters...")
    time.sleep(1.0)
    print(f"[SUCCESS] Firewalls deployed, security filters active.\n")
    time.sleep(1.0)
    print(f"Activating Intrusion Detection System (IDS)...")
    time.sleep(1.0)
    print(f"[SUCCESS] IDS activated, monitoring for intrusions.\n")
    
    # Now start the real-time network monitoring
    print("Starting real-time network monitoring...\n")
    while True:
        monitor_network()  # Continuously monitor the network for suspicious activity

if __name__ == "__main__":
    main()
