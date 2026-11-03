Simple TCP Port Scanner (Network Reconnaissance Tool)
-----------------------------------------------------
Scans specified TCP ports on a target host to identify open services
using Python's built-in socket library.
"""

import socket
import sys
from datetime import datetime

def scan_ports(target_host, ports):
    print("-" * 50)
    print(f"[*] Scanning target: {target_host}")
    print(f"[*] Time started: {str(datetime.now())}")
    print("-" * 50)

    open_ports = []

    try:
        for port in ports:
            # Create a socket object (IPv4, TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0) # 1 second timeout
            
            # Attempt connection (connect_ex returns 0 if successful)
            result = s.connect_ex((target_host, port))
            if result == 0:
                print(f"[+] Port {port}: OPEN")
                open_ports.append(port)
            s.close()
                
    except KeyboardInterrupt:
        print("\n[!] Exiting script...")
        sys.exit()
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\n[!] Could not connect to server.")
        sys.exit()

    print("-" * 50)
    print(f"[+] Scan completed. Open ports found: {open_ports if open_ports else 'None'}")
    print("-" * 50)

if __name__ == "__main__":
    # Default target: localhost (127.0.0.1) for safe local testing
    target = "127.0.0.1"
    
    # Common network and web services ports to check
    common_ports = [21, 22, 80, 443, 3306, 8080]
    
    scan_ports(target, common_ports)
