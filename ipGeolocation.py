from ipChecker import checkIPType

def validate_ip(ip_type, ip):
    return checkIPType(ip_type, ip)

def generate_map_link(lat, lon):
    return f"https://www.google.com/maps?q={lat},{lon}"


ip = input("Enter ip address: ")
ip_type = "4"

if not validate_ip(ip_type, ip):
    print("Invalid ip address.")
else:
    ...

## ???? 🤫🧏‍♀️


