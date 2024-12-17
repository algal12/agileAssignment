from datetime import datetime

def save_scan_to_history(IP_address, scan_type):
    """
    Save the scan details to the history file.
    :param IP_address: The IP address that was scanned.
    :param scan_type: The type of scan (TCP, UDP, TCP/UDP).
    """
    try:
        with open("scan_history.txt", "a") as history_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_file.write(f"{timestamp} | IP: {IP_address} | Scan Type: {scan_type}\n")
    except Exception as e:
        print(f"Error saving scan to history: {e}")

def display_scan_history():
    """
    Display the contents of the scan history file.
    """
    try:
        with open("scan_history.txt", "r") as history_file:
            history = history_file.readlines()
            if history:
                print("\nScan History:")
                for entry in history:
                    print(entry.strip())
            else:
                print("No scan history available.")
    except FileNotFoundError:
        print("No scan history found. You haven't performed any scans yet.")
    except Exception as e:
        print(f"Error reading scan history: {e}")

def view_geolocation_history(filename="geolocation_results.txt"):
    """View the history of IP geolocation searches."""
    try:
        with open(filename, "r") as file:
            history = file.read()
            if history:
                print("Geolocation History:\n")
                print(history)
            else:
                print("No history found.")
    except Exception as e:
        print(f"Error reading history: {e}")
