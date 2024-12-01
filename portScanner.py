from ipChecker import checkIPType
from portTCPScanner import get_ports, scan_ports, return_open_ports
from portUDPScanner import scan_udp_ports
from serviceFinder import display_services, find_services
from saveResults import save_scan_results  # Import the save function
from history import save_scan_to_history, display_scan_history  # Import the history functions

print("Welcome to Port Scanner. Please select if you'd like to view previous scan history or start a new scan.")
print("1. View scan history")
print("2. Start a new scan")

choice = input("Please choose an option (1 or 2): ").strip()

if choice == "1":
    # Display scan history and exit the program
    display_scan_history()
    print("\nExiting the program.")
    exit()  # Exit the program after displaying history

elif choice == "2":
    print("Please select if you're using an IPv4 or IPv6 address (Type 4 for IPv4, type 6 for IPv6)")
    IP_type = input().strip()  # Will only accept 4 or 6

    if IP_type != "4" and IP_type != "6":
        print("Invalid IP type. Please try again.")
    else:
        print("Please enter IP address.")
        IP_address = input().strip()
        if checkIPType(IP_type, IP_address):  # Now the function returns the actual result
            print("IP Address validated.")
            print("Please input whether you want a TCP, UDP or TCP/UDP scan.")
            scan_type = input()
            if scan_type.upper() == "TCP":
                ports = get_ports()
                results = scan_ports(IP_address, ports)
                open_ports = return_open_ports(results)
                tcp_services = find_services(open_ports, "tcp")
                results["services"] = tcp_services  # Store services info in results dictionary
                display_services(tcp_services, "tcp")

                # Ask if the user wants to save the results
                save_choice = input("Do you want to save the scan results to a text file? (y/n): ").strip().lower()
                if save_choice == "y":
                    save_scan_results(results, "TCP")

                # Save to history
                save_scan_to_history(IP_address, "TCP")

            elif scan_type.upper() == "UDP":
                ports = get_ports()
                results = scan_udp_ports(IP_address, ports)
                open_ports = return_open_ports(results)
                udp_services = find_services(open_ports, "udp")
                results["services"] = udp_services  # Store services info in results dictionary
                display_services(udp_services, "udp")

                # Ask if the user wants to save the results
                save_choice = input("Do you want to save the scan results to a text file? (y/n): ").strip().lower()
                if save_choice == "y":
                    save_scan_results(results, "UDP")

                # Save to history
                save_scan_to_history(IP_address, "UDP")

            elif scan_type.upper() == "TCP/UDP":
                print("going for TCP/UDP")
                # Add your implementation here for TCP/UDP scanning.
            else:
                print("Incorrect Port Scan type.")
        else:
            print("IP address entered is invalid.")
else:
    print("Invalid choice. Exiting.")
    exit()  # Exit the program if an invalid option was chosen
