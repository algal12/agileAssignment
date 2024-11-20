import re
def checkIPType(ip_type, ip):
    match ip_type:
        case "4":  # Check IPv4
            return checkIPv4Address(ip)
        case "6":  # Check IPv6
            return checkIPv6Address(ip)
        case _:  # Default case
            print("Wrong input: wrong type of IP address")
            return False

def checkIPv4Address(ip):
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

def checkIPv6Address(ip):
    # Regex for the general IPv6 format (including the IPv4-mapped part)
    ipv6_pattern = re.compile(r"""
        ^                                     # Start of string
        (                                     # Begin group for IPv6 patterns
            (([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})          # Full address (8 hextets)
            |(([0-9a-fA-F]{1,4}:){1,7}:)                    # Leading segments, compressed end
            |(:([0-9a-fA-F]{1,4}:){1,7})                    # Trailing segments, compressed start
            |(([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4})    # Mixed segments with one empty
            |(([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2})
            |(([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3})
            |(([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4})
            |(([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5})
            |([0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6}))
            |(::([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})    # Fully compressed
            |(::)                                           # Double colon only
            |(::ffff:(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)  # IPv4-mapped: start
                \.                                          # Dot
                (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)      # Second octet
                \.                                          # Dot
                (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)      # Third octet
                \.                                          # Dot
                (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)      # Fourth octet
            )                                               # IPv4-mapped: end
        )$                                                  # End of string
    """, re.VERBOSE)

    # Match the input against the pattern
    match = ipv6_pattern.match(ip)

    if match:
        # Check for IPv4-mapped IPv6 format (::ffff:<IPv4>)
        if '::ffff:' in ip:
            ipv4_part = ip.split('::ffff:')[1]  # Extract the IPv4 part
            if checkIPv4Address(ipv4_part):  # Use your existing IPv4 validation
                return True
            else:
                return False

        # If not an IPv4-mapped IPv6, it's a valid standard IPv6
        return True
    else:
        return False