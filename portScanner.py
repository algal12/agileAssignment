# This will be the main interface for Port Scanning. All the functionality will be placed in other classes, this is just an intermediate between them. This will also server as an IP checker.
from ipChecker import checkIPType

print("Welcome to Port Scanner. Please select if you're using an IPv4 or IPv6 address (Type 4 for IPv4, type 6 for IPv6)")
IP_type = input().strip()  # Will only accept 4 or 6
print("Please enter IP address.")
IP_address = input().strip()


if IP_type != "4" and IP_type != "6":
    print("Invalid IP type. Please try again.") # reminder to add a break here when we loop this, so it breaks the loop and it doesn't check for the IP address.
if checkIPType(IP_type, IP_address):  # Now the function returns the actual result
    print("Correct IP address")
else:
    print("Wrong IP address")





