import argparse
import asyncio
import signal
from typing import List, Tuple, Optional

class StorageManager:
    """
    Handles the storage of scan results in various formats.
    """
    def __init__(self, format: str):
        self.format = format

    def save(self, results: List[Tuple[int, bool, Optional[str]]]) -> None:
        # Implement saving logic for different formats (console, file, db, etc.)
        pass

class PortScanner:
    """
    Performs port scanning on a given target host.
    """
    def __init__(self, tgt_host: str, tgt_ports: List[int], scan_type: str):
        self.tgt_host = tgt_host
        self.tgt_ports = tgt_ports
        self.scan_type = scan_type
        self.timeout = 1  # Default timeout for scanning

    async def scan_port(self, port: int) -> Tuple[int, bool, Optional[str]]:
        """
        Scans a single port on the target host.
        """
        try:
            conn = asyncio.open_connection(self.tgt_host, port)
            await asyncio.wait_for(conn, timeout=self.timeout)
            return (port, True, None)  # Port open
        except asyncio.TimeoutError:
            return (port, False, "Timeout")  # Timeout, port likely closed
        except Exception as e:
            return (port, False, str(e))  # Other exceptions

    async def perform_scan(self) -> List[Tuple[int, bool, Optional[str]]]:
        """
        Performs the port scan on all specified ports.
        """
        tasks = [self.scan_port(port) for port in self.tgt_ports]
        results = await asyncio.gather(*tasks)
        return results

def parse_arguments() -> argparse.Namespace:
    """
    Parses command line arguments.
    """
    parser = argparse.ArgumentParser(description="Asynchronous Port Scanner")
    parser.add_argument("-H", "--host", required=True, help="Target host")
    parser.add_argument("-p", "--ports", required=True, help="Target ports (comma-separated)")
    parser.add_argument("--scan-type", default="TCP", help="Type of scan (TCP/UDP/SYN)")
    parser.add_argument("--output-format", default="console", help="Output format (console/file/db)")
    return parser.parse_args()

async def main() -> None:
    """
    Main function to execute the port scanner.
    """
    args = parse_arguments()
    scanner = PortScanner(args.host, args.ports.split(','), args.scan_type)
    storage_manager = StorageManager(args.output_format)

    try:
        results = await scanner.perform_scan()
        open_ports = sum(1 for _, status, _ in results if status)
        print(f"Total open ports: {open_ports}")
        storage_manager.save(results)
    except asyncio.CancelledError:
        print("Scan cancelled.")

if __name__ == "__main__":
    asyncio.run(main())

# Handle Ctrl+C gracefully
signal.signal(signal.SIGINT, signal.default_int_handler)
