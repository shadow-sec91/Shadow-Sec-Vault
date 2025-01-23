import os
import subprocess

# ASCII Art Header
ascii_art = r"""
  ____  _               _                   ____
 / ___|| |__   __ _  __| | _____      __   / ___|  ___  ___
 \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / /___\___ \ / _ \/ __|
  ___) | | | | (_| | (_| | (_) \ V  V /_____|__) |  __/ (__
 |____/|_| |_|\__,_|\__,_|\___/ \_/\_/     |____/ \___|\___|
"""
print(ascii_art)

# Tool Categories and Tools
tool_categories = {
    "Recon": [
        "nmap", "theHarvester", "shodan", "dnsrecon", "sublist3r", "Amass",
        "Gobuster", "DirBuster", "masscan", "metagoofil", "sn1per", "knockpy", 
        "eyed3", "prtdbg", "wafw00f", "dradis", "mfoc", "crowbar", "recon-ng",
        "dnsmap", "asnlookup", "dnsenum", "ipv6-toolkit", "mitmproxy", "tor",
        "dirsearch", "dnschef", "enum4linux", "p0f", "dmitry", "smtp-user-enum",
        "whatweb", "wpscan", "foca", "masscan", "subdomainizer", "amass", 
        "subfinder", "hackertarget", "metagoofil", "nikto", "cewl", "httprint",
        "urlcrazy", "dnsmap", "netdiscover", "wifite", "pywifi", "bettercap",
        "socat"
    ],
    "Exploitation": [
        "metasploit-framework", "sqlmap", "hydra", "john the ripper", "hashcat",
        "nikto", "medusa", "aircrack-ng", "metasploit", "ettercap", "armitage", 
        "reverse_tcp_shell", "msfvenom", "exploitdb", "beef", "netsploit", "webshells", 
        "scriptkiddie", "dslr", "crackmapexec", "evilgrade", "mimikatz", "empire", 
        "cain", "cracks", "shellter", "beef", "setoolkit", "msfvenom", "webshells", 
        "websploit", "exploitpack", "responder", "safe3", "metasploit_psexec", "volshell", 
        "gophish", "websploit", "social_engineer_toolkit", "intrusion_desk", "wapiti", 
        "canarytokens", "dns_exfiltration", "webshell", "zaproxy", "wireshark", 
        "cewl", "se-toolkit", "nikto", "searchsploit"
    ],
    "Post-Exploitation": [
        "mimikatz", "empire", "pth_toolkit", "post-exploitation_scripts", "responder", 
        "crackmapexec", "metasploit", "mimikatz", "pass-the-hash", "kerberos", "psexec", 
        "red_team_tools", "linpeas", "winpeas", "privcheck", "asleap", "smbexec", 
        "gpp-decrypt", "evil-winrm", "metasploit-post-exploitation", "coboltstrike", 
        "gopher", "necromancer", "rainbowcrack", "powercat", "privesc-check", "sharpview", 
        "bloodhound", "rosalind", "powersploit", "pppd", "nginx-shell", "stunnel", "netcat", 
        "socat", "relaysploit", "multi-post-exploitation", "bruteforce-winpass", "htb-tools", 
        "responder", "hashes", "hashid", "hashes", "samdump2", "kismet", "social-engineering-toolkit", 
        "userrecon", "mssql-query"
    ],
    "Networking": [
        "wireshark", "aircrack-ng", "netcat", "bettercap", "tcpdump", "netdiscover", 
        "ping", "socat", "ncat", "sslscan", "hping3", "ikeview", "ssldump", "zmap", "tcpflow", 
        "tcpreplay", "nmap", "tls-scan", "masscan", "arping", "dnsspoof", "netstat", 
        "traceroute", "sslstrip", "apache-bench", "sslscan", "tcpreplay", "privtest", "ikeview", 
        "tcptraceroute", "tshark", "tcpdump", "packetfence", "iperf3", "wireguard", "iputils", 
        "vpncloud", "ngrep", "lft", "scapy", "pyshark", "nslookup", "forensics", "p0f", "commix", 
        "socat", "xrdp", "testssl.sh", "tcpdump", "openssl", "ipcalc", "ncat", "nprobe"
    ],
    "Web Development/Testing": [
        "burp-suite", "zaproxy", "nikto", "wpscan", "metasploit", "sqlmap", "gobuster", 
        "dirmap", "gobuster", "feroxbuster", "nikto", "wapiti", "xsser", "fuzzer", 
        "paramspider", "cherrypy", "buster", "tcpspike", "nmap", "shodan", "ffox", "phpmyadmin", 
        "joomla", "wordpress", "drupal", "marionette", "burp-collaborator", "capturer", "trufflehog", 
        "exploitdb", "jsfuzz", "xsfuzz", "turbofuzzer", "cookie-cutter", "decaweb", "jsfuzz", 
        "recon-ng", "tools-burpsuite", "ngrok", "metahash", "hter", "searchsploit", "webfuzzer", 
        "hashcat", "social-engineer", "custom-scripts"
    ],
    "Custom": [
        "shadowsec-scanner", "shadowsec-tool", "test-c2", "automated-malware-analysis", 
        "botnet", "exploit-scanner", "internal-tools", "honeypot", "file-exfiltration", 
        "malware-payloads", "scripts-developer", "misp", "dark-net-scanner", "vpn-scanner", 
        "dos-and-ddos", "malware-execution", "rat-control", "ransomware", "shellcodes", 
        "payloads", "keylogger", "system-cleaner", "fuzzing_tools", "automatic_exfiltration", 
        "shadowscanner", "backdoor-payload", "ssh-backdoor", "application-exploit"
    ]
}

# Menu Function
def main_menu():
    print("\nWelcome to the Decentralised Shadow-Sec Vault!")
    print("Would you like to install all recommended tools? (y/n)")
    choice = input("Choose an option: ").strip().lower()
    if choice == "y":
        install_all_tools()
    elif choice == "n":
        menu_options()
    else:
        print("[!] Invalid choice. Please try again.")
        main_menu()

def menu_options():
    print("\nMain Menu:")
    print("1. List Tools")
    print("2. Add Tool (Admin Only)")
    print("3. Install Tool")
    print("4. Install All Tools")
    print("5. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        list_tools()
    elif choice == "2":
        add_tool()
    elif choice == "3":
        install_tool()
    elif choice == "4":
        install_all_tools()
    elif choice == "5":
        confirm_exit()
    else:
        print("[!] Invalid choice. Please try again.")
        menu_options()

# List Tools with Selection
def list_tools():
    """List all tools and allow selection for execution or installation."""
    tool_mapping = {}  # Map tool numbers to tools
    print("\nTool Categories and Tools:")
    
    # Display all categories and tools with numbers
    index = 1
    for category, tools in tool_categories.items():
        print(f"\n[{category.upper()}]")
        for tool in tools:
            print(f"  {index}. {tool}")
            tool_mapping[str(index)] = tool
            index += 1
    
    # Allow user to select a tool
    try:
        choice = input("\nEnter the number of the tool to execute or install: ").strip()
        if choice in tool_mapping:
            selected_tool = tool_mapping[choice]
            print(f"\n[INFO] You selected: {selected_tool}")
            
            # Check if the tool is installed
            if check_tool_installed(selected_tool):
                print(f"{selected_tool} is already installed.")
            else:
                print(f"{selected_tool} is not installed. Proceeding with installation.")
                install_tool(selected_tool)
        else:
            print("[!] Invalid selection.")
            list_tools()
    except Exception as e:
        print(f"[!] Error: {e}")

# Install a specific tool
def install_tool(tool_name):
    """Install a tool from a specific category."""
    print(f"\n[INFO] Installing {tool_name}...")
    try:
        subprocess.run(["sudo", "apt", "install", "-y", tool_name], check=True)
        print(f"{tool_name} installation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to install {tool_name}: {e}")

# Install all tools
def install_all_tools():
    """Install all tools from all categories."""
    print("\n[INFO] Installing all tools...")
    for category, tools in tool_categories.items():
        for tool in tools:
            install_tool(tool)
    
# Tool Check
def check_tool_installed(tool_name):
    """Check if a tool is already installed."""
    try:
        subprocess.run(["which", tool_name], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

# Exit Confirmation
def confirm_exit():
    """Exit confirmation."""
    choice = input("\nAre you sure you want to exit? (y/n): ").strip().lower()
    if choice == "y":
        print("\nGoodbye.")
        exit()
    elif choice == "n":
        menu_options()
    else:
        print("[!] Invalid choice. Please try again.")
        confirm_exit()

# Start the main menu
main_menu()






















