import socket
from datetime import datetime
import threading
from serviceFinder import getServicesTCP

# Function to scan a single port
def scan_port(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for the connection
        result = sock.connect_ex((ip, port))
        if result == 0:
            results["open"].append(port)
        elif result == socket.timeout:
            results["filtered"].append(port)
        else:
            results["closed"].append(port)
        getServicesTCP(port)
        sock.close()
    except Exception as e:
        results["filtered"].append(port)

# Function to scan a list of ports
def scan_ports(ip, ports):
    print(f"Starting scan on {ip} for ports: {ports}")
    start_time = datetime.now()
    results = {"open": [], "closed": [], "filtered": []}

    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(ip, port, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = datetime.now()
    print(f"Scan completed in {end_time - start_time}")
    display_results(results)

# Display scan results
def display_results(results):
    print("\nScan Results:")
    print(f"Open Ports: {results['open']}")
    print(f"Closed Ports: {results['closed']}")
    print(f"Filtered Ports: {results['filtered']}")

# Get ports based on user choice
def get_ports():
    print("\nPort Selection Options:")
    print("1. Single Port")
    print("2. Multiple Specific Ports (comma-separated)")
    print("3. Port Range")
    print("4. All Ports (1-65535)")
    choice = input("Choose an option: ")

    if choice == "1":
        port = int(input("Enter the port number: "))
        return [port]
    elif choice == "2":
        ports = input("Enter the port numbers (comma-separated): ")
        return [int(port.strip()) for port in ports.split(",")]
    elif choice == "3":
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        return list(range(start_port, end_port + 1))
    elif choice == "4":
        print("Scanning all ports (1-65535)...")
        return list(range(1, 65536))
    else:
        print("Invalid choice. Exiting.")
        exit()




