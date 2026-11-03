# Network Port Scanner (Reconnaissance Tool)

A lightweight TCP port scanning utility written in Python. It utilizes raw socket programming to probe target IP addresses, handle connection timeouts, and map out active network services.

## Features
- **Socket Programming**: Implements low-level TCP connection attempts via IPv4 sockets.
- **Error Handling**: Gracefully handles timeouts, network interrupts, and unresolved hostnames.
- **Zero Dependencies**: Relies entirely on Python's built-in standard libraries (`socket`, `sys`, `datetime`).

## How to Run in Your Browser
1. Open this repository and press the **`.` (period)** key to launch **GitHub Codespaces**.
2. Run the script directly in the terminal (no installation required):
   ```bash
   python port_scanner.py
