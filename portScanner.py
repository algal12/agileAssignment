# This will be the main interface for Port Scanning. All the functionality will be placed in other classes, this is just an intermediate between them. This will also server as an IP checker.
def checkIPType(ip_type, ip):
    match ip_type:
        case "4":  # Check if there's letters, and numbers in the IP are greater than 0, lesser than 255, and 4 numbers total
            # Split by dots and check the number of parts
            parts = ip.split(".")
            if len(parts) != 4:
                return False

            for part in parts:
                # Check if each part is a digit and within the valid range
                if not part.isdigit() or not 0 <= int(part) <= 255:
                    return False
                # Check for leading zeros
                if part != "0" and part.startswith("0"):
                    return False

            return True
        case "6":  # Same thing as above, but for IPv6
            print("6 selected")
        case _:  # Default case; If they don't input 4 or 6 just close the program
            print("Wrong input: wrong type of IP address")

print("Welcome to Port Scanner. Please select if you're using an IPv4 or IPv6 address ( Type 4 for IPv4, type 6 for IPv6 )")
IP_type = input() # Will only accept 4 or 6
print("Please enter IP address.")
IP_address = input()
if(checkIPType(IP_type, IP_address)):
    print("Correct IP address")
else:
    print("Wrong")




