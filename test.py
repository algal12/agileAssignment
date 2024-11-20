import re


def is_valid_ipv6(ip):
    ipv6_pattern = re.compile(r"""
        ^                                     # Start of string
        (([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}          # Full address (8 hextets)
        |(([0-9a-fA-F]{1,4}:){1,7}:)                    # Leading segments, compressed end
        |(:([0-9a-fA-F]{1,4}:){1,7})                    # Trailing segments, compressed start
        |(([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4})    # Mixed segments with one empty
        |(([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2})
        |(([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3})
        |(([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4})
        |(([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5})
        |([0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6}))
        |(::([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})    # Fully compressed
        |(::))                                          # Double colon only
        $                                     # End of string
    """, re.VERBOSE)

    # Debugging
    if not ip:
        print("Empty input.")
        return False

    # Match the input against the pattern
    match = ipv6_pattern.match(ip)
    if match:
        print(f"'{ip}' is a valid IPv6 address.")
    else:
        print(f"'{ip}' is NOT a valid IPv6 address.")

    return bool(match)


# Test Case
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Expected True
