# This will be the main interface for Port Scanning. All the functionality will be placed in other classes, this is just an intermediate between them. This will also server as an IP checker.

print("Welcome to Port Scanner. Please select if you're using an IPv4 or IPv6 address ( Type 4 for IPv4, type 6 for IPv6 )")
IP_type = input() # Will only accept 4 or 6

match IP_type:
    case "4": # Run checks to make sure it's a right kind of IP address before going to the next step
        pass
    case "6": # Same thing as above, but for IPv6
        pass
    case _: # Default case; If they don't input 4 or 6 just close the program
        print("You have given wrong input. Closing program.")


        # testing for ability to push
