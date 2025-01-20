def save_scan_results(results, scan_type, ip, filename="scan_results.txt", history_file="scan_history.txt"):
    """
    Save the full scan results (open, closed, filtered) and services to a text file,
    and append a summary to the history file.
    :param results: The scan results dictionary containing "open", "closed", and "filtered" ports.
    :param scan_type: Type of scan (TCP, UDP, etc.)
    :param filename: Name of the file to save the detailed results to (default is "scan_results.txt").
    :param history_file: Name of the file to save the history to (default is "scan_history.txt").
    """
    try:
        # Save detailed results to the main results file
        with open(filename, "w") as file:
            file.write(ip)
            file.write(f" Port Scan Results ({scan_type} scan)\n")
            file.write("=" * 50 + "\n")

            # For open ports
            file.write("Open Ports:\n")
            if results.get("open"):
                for port in results["open"]:
                    file.write(f"Port {port}: Open \n")
            else:
                file.write("No open ports found.\n")

            file.write("=" * 50 + "\n")
        print(f"Results saved to {filename}")

        # Save summary to the history file
        with open(history_file, "a") as history:


            history.write(f"{ip} \n")
            history.write("Summary:\n")
            history.write(f"Open Ports: {', '.join(map(str, results.get('open', []))) or 'None'}\n")
            history.write("=" * 50 + "\n\n")
        print(f"Summary appended to {history_file}")

    except Exception as e:
        print(f"Error saving results: {e}")



def save_geolocation_results(geo_data, filename="geolocation_results.txt", history_file="geolocation_history.txt"):
    """Save the geolocation results to a text file and append to history.
    :param geo_data: The geolocation results dictionary containing "latitude", "longitude", etc.
    :param filename: Name of the file to save the latest results to (default is "geolocation_results.txt").
    :param history_file: Name of the file to save the geolocation history (default is "geolocation_history.txt").
    """
    try:
        # Create the Google Maps link
        google_maps_link = f"https://www.google.com/maps?q={geo_data['lat']},{geo_data['lon']}"

        # Save the latest results (overwrite)
        with open(filename, "w") as file:
            file.write("=" * 50 + "\n")
            file.write(f"Geolocation Results for IP: {geo_data['ip']}\n")
            file.write(f"Country: {geo_data['country']}\n")
            file.write(f"Region: {geo_data['region']}\n")
            file.write(f"City: {geo_data['city']}\n")
            file.write(f"ISP: {geo_data['isp']}\n")
            file.write(f"Latitude: {geo_data['lat']}\n")
            file.write(f"Longitude: {geo_data['lon']}\n")
            file.write(f"Google Maps Link: {google_maps_link}\n")
            file.write("=" * 50 + "\n")
        print(f"Results saved to {filename}")

        # Append results to the history file
        with open(history_file, "a") as history:
            history.write("=" * 50 + "\n")
            history.write(f"Geolocation Results for IP: {geo_data['ip']}\n")
            history.write(f"Country: {geo_data['country']}\n")
            history.write(f"Region: {geo_data['region']}\n")
            history.write(f"City: {geo_data['city']}\n")
            history.write(f"ISP: {geo_data['isp']}\n")
            history.write(f"Latitude: {geo_data['lat']}\n")
            history.write(f"Longitude: {geo_data['lon']}\n")
            history.write(f"Google Maps Link: {google_maps_link}\n")
            history.write("=" * 50 + "\n")
        print(f"Results appended to {history_file}")
    except Exception as e:
        print(f"Error saving results: {e}")


def save_geolocation_history(geo_data, history_file="geolocation_history.txt"):
    google_maps_link = f"https://www.google.com/maps?q={geo_data['lat']},{geo_data['lon']}"
    try:
        with open(history_file, "a") as history:
            history.write("=" * 50 + "\n")
            history.write(f"Geolocation Results for IP: {geo_data['ip']}\n")
            history.write(f"Country: {geo_data['country']}\n")
            history.write(f"Region: {geo_data['region']}\n")
            history.write(f"City: {geo_data['city']}\n")
            history.write(f"ISP: {geo_data['isp']}\n")
            history.write(f"Latitude: {geo_data['lat']}\n")
            history.write(f"Longitude: {geo_data['lon']}\n")
            history.write(f"Google Maps Link: {google_maps_link}\n")
            history.write("=" * 50 + "\n")
        print(f"Results appended to {history_file}")
    except Exception as e:
        print(f"Error saving results: {e}")

def save_scan_history(results, scan_type, ip, history_file="scan_history.txt"):
    try:
        with open(history_file, "a") as history:

            history.write(f"{ip} \n")
            history.write("Summary:\n")
            history.write(f"Open Ports: {', '.join(map(str, results.get('open', []))) or 'None'}\n")
            history.write("=" * 50 + "\n\n")
        print(f"Summary appended to {history_file}")

    except Exception as e:
        print(f"Error saving results: {e}")