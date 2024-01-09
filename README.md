# PyPortScan / Port Scanner

PyPortScan / Port Scanner is an efficient, asynchronous port scanning tool written in Python. It's designed to quickly identify open ports on a target host, providing insights for network analysis and security auditing.

## Features

- **Asynchronous Scanning**: Utilizes Python's `asyncio` for fast, non-blocking network I/O.
- **Multiple Scan Types**: Supports various scanning methods including TCP, UDP, and SYN.
- **Flexible Output Formats**: Allows output in different formats like console display, file, or database.
- **Command-Line Interface**: Easy-to-use CLI for quick scans and results.
- **Customizable Port Range**: Scan a range of ports as specified by the user.
- **Robust Error Handling**: Gracefully handles network errors and interruptions.

## Usage

To use AsyncPortScanner, run the following command in your terminal:

```bash
python port_scanner.py -H <target_host> -p <port1,port2,...> [--scan-type <TCP/UDP/SYN>] [--output-format <console/file/db>]
```

### Command-Line Arguments

- `-H` or `--host`: Specify the target host IP address or domain name.
- `-p` or `--ports`: List of target ports to scan, separated by commas.
- `--scan-type`: Optional. Specify the scan type (TCP, UDP, SYN). Default is TCP.
- `--output-format`: Optional. Specify the output format (console, file, database). Default is console.

## Installation

No special installation is required. However, you must install Python 3.7 or higher on your system.

### Installing Python

- For Windows, macOS, and Linux distributions: Visit [Python's official website](https://www.python.org/downloads/) and download the installer for Python 3.7+.

## Requirements

- Python 3.7+
- Internet connection for scanning remote hosts

## Disclaimer

Port scanning can be perceived as intrusive by network administrators. This tool is intended for educational purposes and security assessments with permission. Always ensure you have the right to scan the target network. Unauthorized scanning can lead to legal actions.
