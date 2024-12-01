import socket
from datetime import datetime
import threading




def scan_udp_port(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.sendto(b"Ping", (ip, port))  # Sending a basic UDP packet
        try:
            data, addr = sock.recvfrom(1024)  # Waiting for a response
            results["open"].append(port)
        except socket.timeout:
            results["filtered"].append(port)
    except Exception:
        results["closed"].append(port)


def scan_udp_ports(ip, ports):
    print(f"Starting UDP scan on {ip} for ports: {ports}")
    start_time = datetime.now()
    results = {"open": [], "closed": [], "filtered": []}

    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_udp_port, args=(ip, port, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = datetime.now()
    print(f"UDP Scan completed in {end_time - start_time}")
    display_results(results)


def display_results(results):
    print("\nUDP Scan Results:")
    print(f"Open Ports: {results['open']}")
    print(f"Closed Ports: {results['closed']}")
    print(f"Filtered Ports: {results['filtered']}")


