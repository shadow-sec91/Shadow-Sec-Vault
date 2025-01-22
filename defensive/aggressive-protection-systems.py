import os
import time
import psutil
import logging
import requests
import subprocess
import sys
import netifaces
from scapy.all import sniff, IP, TCP, ICMP

# Set up logging
logging.basicConfig(filename='/root/Shadow-Sec-Vault/logs/aps.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Required packages
required_packages = [
    "scapy",
    "requests",
    "psutil",
    "netifaces",
    "macchanger"
]

# ASCII Art for Shadow-Sec
ascii_art = """
 .oooooo..o oooo                        .o8                                      .oooooo..o                     
d8P'    `Y8 `888                       "888                                     d8P'    `Y8                     
Y88bo.       888 .oo.    .oooo.    .oooo888   .ooooo.  oooo oooo    ooo         Y88bo.       .ooooo.   .ooooo.  
 `"Y8888o.   888P"Y88b  `P  )88b  d88' `888  d88' `88b  `88. `88.  .8'           `"Y8888o.  d88' `88b d88' `"Y8 
     `"Y88b  888   888   .oP"888  888   888  888   888   `88..]88..8'   8888888      `"Y88b 888ooo888 888       
oo     .d8P  888   888  d8(  888  888   888  888   888    `888'`888'            oo     .d8P 888    .o 888   .o8 
8""88888P'  o888o o888o `Y888""8o `Y8bod88P" `Y8bod8P'     `8'  `8'             8""88888P'  `Y8bod8P' `Y8bod8P' 
                                                                                                                
                                                                                                                
                                                                                                                
                                    .o.       ooooooooo.    .oooooo..o                                          
                                   .888.      `888   `Y88. d8P'    `Y8                                          
                                  .8"888.      888   .d88' Y88bo.                                               
                                 .8' `888.     888ooo88P'   `"Y8888o.                                           
                                .88ooo8888.    888              `"Y88b                                          
                               .8'     `888.   888         oo     .d8P                                          
                              o88o     o8888o o888o        8""88888P'                                           
"""

def display_ascii_art():
    print(ascii_art)
    time.sleep(0.8)

def check_and_install_packages():
    """Check for required Python packages and install if missing."""
    print("[INFO] Checking required packages...")
    missing_packages = []
    
    for pkg in required_packages:
        try:
            __import__(pkg)
        except ImportError:
            missing_packages.append(pkg)

    if missing_packages:
        print(f"[WARNING] Missing packages detected: {', '.join(missing_packages)}")
        choice = input("[ACTION] Do you want to install the missing packages? (y/n): ").strip().lower()
        if choice == 'y':
            for pkg in missing_packages:
                print(f"[INSTALLING] Installing {pkg}...")
                subprocess.run([sys.executable, "-m", "pip", "install", pkg, "--break-system-packages"])
            print("[SUCCESS] All missing packages have been installed.")
        else:
            print("[ERROR] Missing packages cannot be installed automatically. Exiting...")
            sys.exit(1)
    else:
        print("[SUCCESS] All required packages are installed.")

def deploy_firewalls():
    """Deploy and enable firewalls using UFW."""
    if os.system("which ufw > /dev/null 2>&1") == 0:  # Check if UFW is installed
        print(f"[ACTION] Deploying firewalls...")
        os.system("sudo ufw enable")
        print(f"[SUCCESS] Firewalls deployed.")
        logging.debug("[INFO] Firewalls deployed successfully.")
    else:
        print(f"[WARNING] UFW not found. Skipping firewall deployment.")
        logging.debug("[WARNING] UFW not found.")

def list_network_interfaces():
    """List all available physical network interfaces."""
    interfaces = netifaces.interfaces()
    active_interfaces = [
        iface for iface in interfaces
        if netifaces.AF_INET in netifaces.ifaddresses(iface) and iface != "lo"
    ]
    print("[INFO] Available network interfaces:")
    for idx, iface in enumerate(active_interfaces, start=1):
        print(f"  {idx}. {iface}")
    return active_interfaces

def select_network_interface():
    """Allow user to select an interface directly or auto-detect."""
    active_interfaces = list_network_interfaces()
    if not active_interfaces:
        print("[ERROR] No active network interfaces detected.")
        sys.exit(1)

    print("[ACTION] Select an interface by entering its number or type 'a' to auto-detect:")
    while True:
        choice = input("Enter choice: ").strip().lower()

        # Auto-detect option
        if choice == 'a':
            print(f"[INFO] Automatically selecting {active_interfaces[0]}")
            return active_interfaces[0]

        # Direct number selection
        try:
            iface_num = int(choice)
            if 1 <= iface_num <= len(active_interfaces):
                print(f"[INFO] You selected {active_interfaces[iface_num - 1]}")
                return active_interfaces[iface_num - 1]
            else:
                print(f"[ERROR] Invalid selection. Please choose a number between 1 and {len(active_interfaces)}.")
        except ValueError:
            print("[ERROR] Invalid input. Please enter a number or 'a' for auto-detect.")

def validate_interface(interface):
    """Validate that the network interface is up and operational."""
    result = subprocess.run(["ip", "link", "show", interface], stdout=subprocess.PIPE)
    if "state UP" in result.stdout.decode():
        print(f"[INFO] Interface {interface} is up and operational.")
        logging.info(f"Interface {interface} is up and operational.")
    else:
        print(f"[ERROR] Interface {interface} is down. Aborting operation.")
        logging.error(f"Interface {interface} is down.")
        sys.exit(1)

def change_mac_address(interface):
    """Change MAC address of the specified interface."""
    print(f"[INFO] Changing MAC address for {interface}...")
    try:
        os.system(f"sudo ifconfig {interface} down")
        result = subprocess.run(
            ["sudo", "macchanger", "-r", interface],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        os.system(f"sudo ifconfig {interface} up")
        if "Current MAC" in result.stdout and "Permanent MAC" in result.stdout:
            print(result.stdout)
            confirm_mac_change(interface)
        else:
            print(f"[ERROR] Could not change MAC: {result.stderr.strip()}")
            logging.debug(f"MAC change failed for {interface}: {result.stderr.strip()}")
    except Exception as e:
        print(f"[ERROR] Failed to change MAC address for {interface}: {e}")
        logging.debug(f"Failed to change MAC address for {interface}: {e}")

def confirm_mac_change(interface):
    """Confirm MAC address change."""
    result = subprocess.run(["ifconfig", interface], stdout=subprocess.PIPE)
    output = result.stdout.decode()
    if "ether" in output:
        mac_address = output.split("ether")[1].strip().split(" ")[0]
        print(f"[SUCCESS] New MAC address for {interface}: {mac_address}")
        logging.debug(f"MAC address changed: {mac_address}")
    else:
        print(f"[ERROR] Failed to retrieve MAC address for {interface}.")
        logging.debug(f"Failed to retrieve MAC address for {interface}.")

def change_ip_address(interface):
    """Change IP address using DHCP."""
    print(f"[INFO] Changing IP address for {interface}...")
    os.system(f"sudo ifconfig {interface} up")
    os.system(f"sudo dhclient -r {interface}")
    os.system(f"sudo dhclient {interface}")
    confirm_ip_change(interface)

def confirm_ip_change(interface):
    """Confirm IP address change."""
    result = subprocess.run(["ip", "addr", "show", interface], stdout=subprocess.PIPE)
    ip_address = [line.split()[1] for line in result.stdout.decode().splitlines() if "inet " in line]
    if ip_address:
        print(f"[SUCCESS] New IP address for {interface}: {ip_address[0]}")
        logging.debug(f"IP address changed: {ip_address[0]}")
    else:
        print(f"[ERROR] Failed to change IP address for {interface}.")
        logging.debug(f"Failed to change IP address for {interface}.")

def detect_nmap(packet):
    """Detect potential Nmap scans and trigger alert."""
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        if tcp_layer.flags == "S":  # SYN flag detection
            src_ip = packet[IP].src
            dest_port = tcp_layer.dport
            print(f"[ALERT] Nmap scan detected from IP: {src_ip} targeting port: {dest_port}")
            logging.debug(f"Nmap scan detected from IP: {src_ip} targeting port: {dest_port}")
            trigger_alert(src_ip)

def trigger_alert(ip_address):
    """Trigger the alert system."""
    print(f"[ACTION] Triggering alert for suspicious IP: {ip_address}")
    logging.info(f"Alert triggered for suspicious IP: {ip_address}")
    os.system(f'python3 /root/Shadow-Sec-Vault/defensive/alert.py {ip_address}')

def monitor_traffic():
    """Monitor network traffic and detect suspicious activity."""
    print("[INFO] Monitoring traffic for all protocols...")
    try:
        sniff(prn=detect_nmap, filter="tcp[tcpflags] & tcp-syn != 0", store=0)
    except KeyboardInterrupt:
        print("\n[INFO] Stopping network monitoring...")
        logging.debug("[INFO] Network monitoring stopped.")
        sys.exit(0)

def main():
    display_ascii_art()
    print("Starting Aggressive Protection System...\n")

    print("[INFO] Checking system readiness...")
    check_and_install_packages()

    print(f"--- Initializing Aggressive Protection System ---")
    time.sleep(1)
    print(f"[SUCCESS] Aggressive Protection System Activated.\n")
    time.sleep(1)
    print(f"Deploying Firewalls and Security Filters...")
    deploy_firewalls()

    # Dynamic interface selection
    interface = select_network_interface()
    change_mac_address(interface)
    change_ip_address(interface)
    validate_interface(interface)

    # Start continuous network monitoring
    print("\n[INFO] Starting real-time network monitoring...")
    monitor_traffic()

if __name__ == "__main__":
    main()
