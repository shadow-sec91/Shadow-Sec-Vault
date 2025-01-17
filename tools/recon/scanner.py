import subprocess
import requests
import ftplib
import socket
import nmap

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


# Functions
def quick_common_ports_scan(target):
    common_ports = [22, 23, 25, 80, 443, 3389]
    nm = nmap.PortScanner()
    print(f"[+] Quickly scanning common ports on {target}...")
    try:
        nm.scan(target, arguments='-sT -p ' + ','.join(map(str, common_ports)) + ' -sV')
        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()})")
            print(f"State: {nm[host].state()}")
            for port in common_ports:
                if port in nm[host]['tcp']:
                    print(f"Port {port}: {nm[host]['tcp'][port]['state']}, Service: {nm[host]['tcp'][port].get('name', 'Unknown')}, Version: {nm[host]['tcp'][port].get('version', 'Unknown')}")
    except Exception as e:
        print(f"[!] Error during common ports scan: {e}")

def grab_http_headers(target):
    print(f"[+] Grabbing HTTP headers from {target}...")
    try:
        response = requests.head(f"http://{target}", timeout=5)
        print("[+] HTTP Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(f"[!] Error grabbing HTTP headers: {e}")

def ping_host(target):
    print(f"[+] Pinging {target}...")
    try:
        result = subprocess.run(["ping", "-c", "1", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"[+] Host {target} is reachable.")
        else:
            print(f"[!] Host {target} is not reachable.")
    except Exception as e:
        print(f"[!] Error during ping: {e}")

def dns_lookup(target):
    print(f"[+] Performing DNS lookup for {target}...")
    try:
        ip_addresses = socket.gethostbyname_ex(target)[2]
        print("[+] Resolved IP addresses:")
        for ip in ip_addresses:
            print(f"- {ip}")
    except Exception as e:
        print(f"[!] Error performing DNS lookup: {e}")

def check_default_ftp_credentials(target):
    print(f"[+] Checking for default FTP credentials on {target}...")
    try:
        ftp = ftplib.FTP(target, timeout=5)
        ftp.login("anonymous", "anonymous")
        print("[+] Default FTP credentials work!")
        ftp.quit()
    except Exception as e:
        print(f"[!] Default FTP credentials failed: {e}")

def check_default_ssh_credentials(target):
    print(f"[+] Checking for default SSH credentials on {target}...")
    # Placeholder for SSH credentials checking logic
    print("[+] Default SSH credentials test completed. (This is a placeholder)")

# Run All Function
def run_all(target):
    print("[+] Running all functions on the target...\n")
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
        print("[1] Ping host")
        print("[2] DNS lookup")
        print("[3] Quick scan common ports")
        print("[4] Grab HTTP headers")
        print("[5] Check default FTP credentials")
        print("[6] Check default SSH credentials")
        print("[7] Run all")
        print("[8] Exit")
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
            print("Exiting...")
            break
        else:
            print("[!] Invalid choice.")
        
        # Ask if user wants to continue or exit
        continue_choice = input("\nDo you want to continue? (y/n): ")
        if continue_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
