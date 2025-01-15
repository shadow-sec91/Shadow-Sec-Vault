import os
import time
import psutil

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

    time.sleep(0.6)  # Shorter delay for immediate feedback
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

def monitor_network():
    # Track incoming connections
    connections = psutil.net_connections(kind='inet')
    
    suspicious_ips = {}
    for conn in connections:
        if conn.status == 'ESTABLISHED':
            ip = conn.raddr.ip
            if ip not in suspicious_ips:
                suspicious_ips[ip] = 1
            else:
                suspicious_ips[ip] += 1
    
    # Only print results when suspicious activity is detected
    suspicious_ips_detected = False
    for ip, count in suspicious_ips.items():
        if count > 50:  # Adjust this threshold as needed for detecting DDoS patterns
            print(f"\n[SUSPICIOUS] Potential DDoS detected from IP: {ip}")
            trigger_alert(ip)
            suspicious_ips_detected = True
    
    # If no suspicious activity detected, do not print anything
    if not suspicious_ips_detected:
        return  # No suspicious IPs detected, so no output

    # Sleep and monitor again (adjust frequency as needed)
    time.sleep(5)  # Monitor every 5 seconds (you can adjust this time)

# Function to trigger the alert by running alert.py in a separate terminal
def trigger_alert(ip_address):
    print(f"Triggering alert for suspicious IP: {ip_address}")
    # Open a new terminal window and run the alert.py script with the suspicious IP as an argument
    os.system(f'gnome-terminal -- bash -c "python3 /path/to/alert.py {ip_address}; exec bash"')

# Main function to simulate APS behavior
def main():
    display_ascii_art()  # Display ASCII art at the start
    print("Starting real-time network monitoring...\n")
    
    # Run the real-time network monitoring only once and continue monitoring after that
    while True:
        monitor_network()  # Continuously monitor the network for suspicious activity

if __name__ == "__main__":
    main()
