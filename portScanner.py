# This will be the main interface for Port Scanning. All the functionality will be placed in other classes, this is just an intermediate between them. This will also server as an IP checker.
from ipChecker import checkIPType
from portTCPScanner import get_ports, scan_ports
from portUDPScanner import scan_udp_ports

print("Welcome to Port Scanner. Please select if you're using an IPv4 or IPv6 address (Type 4 for IPv4, type 6 for IPv6)")
IP_type = input().strip()  # Will only accept 4 or 6
if IP_type != "4" and IP_type != "6":
    print("Invalid IP type. Please try again.") # reminder to add a break here when we loop this, so it breaks the loop and it doesn't check for the IP address (if we loop it).
else:
    print("Please enter IP address.")
    IP_address = input().strip()
    if checkIPType(IP_type, IP_address):  # Now the function returns the actual result
        print("IP Address validated.")
        print("Please input whether you want a TCP, UDP or TCP/UDP scan.")
        scan_type = input()
        if scan_type.upper() == "TCP":
            ports = get_ports()
            scan_ports(IP_address, ports)
        elif scan_type.upper() == "UDP":
            ports = get_ports()
            scan_udp_ports(IP_address, ports)
        elif scan_type.upper() == "TCP/UDP":
            print("going for TCP/UDP")
        else:
            print("Incorrect Port Scan type.")
    else:
        print("IP address entered is invalid.")






