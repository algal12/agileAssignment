# Import functions from your existing TCP and UDP scanners
from portTCPScanner import scan_port, scan_ports  # Import both TCP functions
from portUDPScanner import scan_udp_port, scan_udp_ports  # Import both UDP functions

def combined_scan(ip, ports, scan_type="both"):
    """
    Perform TCP, UDP, or both scans on the given IP and ports.
    :param ip: Target IP address.
    :param ports: List of ports to scan.
    :param scan_type: Type of scan ("tcp", "udp", or "both").
    :return: Dictionary with TCP and/or UDP results.
    """
    results = {"TCP": None, "UDP": None}

    # Check if we're scanning only TCP or both
    if scan_type in ["both", "tcp"]:
        # If only one port is given, use scan_port, otherwise use scan_ports
        if len(ports) == 1:
            print(f"\nStarting TCP scan for single port {ports[0]} on {ip}...")
            results["TCP"] = scan_port(ip, ports[0], {"open": [], "closed": [], "filtered": []})
        else:
            print(f"\nStarting TCP scan for multiple ports {ports} on {ip}...")
            results["TCP"] = scan_ports(ip, ports)

    # Check if we're scanning only UDP or both
    if scan_type in ["both", "udp"]:
        # If only one port is given, use scan_udp_port, otherwise use scan_udp_ports
        if len(ports) == 1:
            print(f"\nStarting UDP scan for single port {ports[0]} on {ip}...")
            results["UDP"] = scan_udp_port(ip, ports[0], {"open": [], "closed": [], "filtered": []})
        else:
            print(f"\nStarting UDP scan for multiple ports {ports} on {ip}...")
            results["UDP"] = scan_udp_ports(ip, ports)

    return results
