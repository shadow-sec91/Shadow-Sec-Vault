import os
import subprocess
import requests
import ftplib
import socket
import nmap
import logging

# Configure Logging
logging.basicConfig(
    filename='/root/Shadow-Sec-Vault/logs/scanner.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def show_banner():
    ascii_art = r"""
 $$$$$$\  $$\                       $$\                                 $$$$$$\                                                        
$$  __$$\ $$ |                      $$ |                               $$  __$$\                                                       
$$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$$ | $$$$$$\  $$\  $$\  $$\        $$ /  \__| $$$$$$\   $$$$$$$\                                   
\$$$$$$\  $$  __$$\  \____$$\ $$  __$$ |$$  __$$\ $$ | $$ | $$ |$$$$$$\$$$$$$\  $$  __$$\ $$  _____|                                  
 \____$$\ $$ |  $$ | $$$$$$$ |$$ /  $$ |$$ /  $$ |$$ | $$ | $$ |\______|\____$$\ $$$$$$$$ |$$ /                                        
$$\   $$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |       $$\   $$ |$$   ____|$$ |                                        
\$$$$$$  |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$  |\$$$$$\$$$$  |       \$$$$$$  |\$$$$$$$\ \$$$$$$$\                                   
 \______/ \__|  \__| \_______| \_______| \______/  \_____\____/         \______/  \_______| \_______|                                  
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
                                                                   $$$$$$\                                                             
                                                                  $$  __$$\                                                            
                                                                  $$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
                                                                  \$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
                                                                   \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
                                                                  $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
                                                                  \$$$$$$  |\$$$$$$$\$$$$$$$ |$$ |  $$ |$$ |  $$ |\$$$$$$$\ $$ |      
                                                                   \______/  \_______|\_______|\__|  \__|\__|  \__| \_______|\__|
    """
    print(ascii_art)

def log_and_print(message):
    print(message)
    logging.info(message)

# Functions
def quick_common_ports_scan(target):
    common_ports = [22, 23, 25, 80, 443, 3389]
    nm = nmap.PortScanner()
    log_and_print(f"[+] Quickly scanning common ports on {target}...")
    try:
        nm.scan(target, arguments='-sT -p ' + ','.join(map(str, common_ports)) + ' -sV')
        for host in nm.all_hosts():
            log_and_print(f"Host: {host} ({nm[host].hostname()})")
            log_and_print(f"State: {nm[host].state()}")
            for port in common_ports:
                if port in nm[host]['tcp']:
                    log_and_print(f"Port {port}: {nm[host]['tcp'][port]['state']}, Service: {nm[host]['tcp'][port].get('name', 'Unknown')}, Version: {nm[host]['tcp'][port].get('version', 'Unknown')}")
    except Exception as e:
        log_and_print(f"[!] Error during common ports scan: {e}")

def grab_http_headers(target):
    log_and_print(f"[+] Grabbing HTTP headers from {target}...")
    try:
        response = requests.head(f"http://{target}", timeout=5)
        log_and_print("[+] HTTP Headers:")
        for header, value in response.headers.items():
            log_and_print(f"{header}: {value}")
    except Exception as e:
        log_and_print(f"[!] Error grabbing HTTP headers: {e}")

def ping_host(target):
    log_and_print(f"[+] Pinging {target}...")
    try:
        result = subprocess.run(["ping", "-c", "1", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            log_and_print(f"[+] Host {target} is reachable.")
        else:
            log_and_print(f"[!] Host {target} is not reachable.")
    except Exception as e:
        log_and_print(f"[!] Error during ping: {e}")

def dns_lookup(target):
    log_and_print(f"[+] Performing DNS lookup for {target}...")
    try:
        ip_addresses = socket.gethostbyname_ex(target)[2]
        log_and_print("[+] Resolved IP addresses:")
        for ip in ip_addresses:
            log_and_print(f"- {ip}")
    except Exception as e:
        log_and_print(f"[!] Error performing DNS lookup: {e}")

def check_default_ftp_credentials(target):
    log_and_print(f"[+] Checking for default FTP credentials on {target}...")
    try:
        ftp = ftplib.FTP(target, timeout=5)
        ftp.login("anonymous", "anonymous")
        log_and_print("[+] Default FTP credentials work!")
        ftp.quit()
    except Exception as e:
        log_and_print(f"[!] Default FTP credentials failed: {e}")

def check_default_ssh_credentials(target):
    log_and_print(f"[+] Checking for default SSH credentials on {target}...")
    log_and_print("[+] Default SSH credentials test completed. (This is a placeholder)")

# Run All Function
def run_all(target):
    log_and_print("[+] Running all functions on the target...\n")
    ping_host(target)
    dns_lookup(target)
    quick_common_ports_scan(target)
    grab_http_headers(target)
    check_default_ftp_credentials(target)
    check_default_ssh_credentials(target)

# Main script
def main():
    while True:
        show_banner()
        target = input("Enter the target: ")
        log_and_print("[1] Ping host")
        log_and_print("[2] DNS lookup")
        log_and_print("[3] Quick scan common ports")
        log_and_print("[4] Grab HTTP headers")
        log_and_print("[5] Check default FTP credentials")
        log_and_print("[6] Check default SSH credentials")
        log_and_print("[7] Run all")
        log_and_print("[8] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            ping_host(target)
        elif choice == '2':
            dns_lookup(target)
        elif choice == '3':
            quick_common_ports_scan(target)
        elif choice == '4':
            grab_http_headers(target)
        elif choice == '5':
            check_default_ftp_credentials(target)
        elif choice == '6':
            check_default_ssh_credentials(target)
        elif choice == '7':
            run_all(target)
        elif choice == '8':
            log_and_print("Exiting...")
            break
        else:
            log_and_print("[!] Invalid choice.")
        
        # Ask if user wants to continue or exit
        continue_choice = input("\nDo you want to continue? (y/n): ")
        if continue_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
