def save_scan_results(results, scan_type, filename="scan_results.txt"):
    """
    Save the full scan results (open, closed, filtered) and services to a text file.
    :param results: The scan results dictionary containing "open", "closed", and "filtered" ports.
    :param scan_type: Type of scan (TCP, UDP, etc.)
    :param filename: Name of the file to save the results to (default is "scan_results.txt").
    """
    try:
        with open(filename, "w") as file:
            file.write(f"Port Scan Results ({scan_type} scan)\n")
            file.write("=" * 50 + "\n")

            # For open ports
            file.write("Open Ports:\n")
            if results.get("open"):
                for port in results["open"]:
                    service = results.get("services", {}).get(port, "Unknown")
                    file.write(f"Port {port}: Open, Service: {service}\n")
            else:
                file.write("No open ports found.\n")

            # For closed ports
            file.write("\nClosed Ports:\n")
            if results.get("closed"):
                for port in results["closed"]:
                    file.write(f"Port {port}: Closed\n")
            else:
                file.write("No closed ports found.\n")

            # For filtered ports
            file.write("\nFiltered Ports:\n")
            if results.get("filtered"):
                for port in results["filtered"]:
                    file.write(f"Port {port}: Filtered\n")
            else:
                file.write("No filtered ports found.\n")

            file.write("=" * 50 + "\n")
            print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")

from ipGeolocation import generate_map_link
def save_geolocation_results(geo_data, filename="geolocation_results.txt"):
    """Save the geolocation results to a text file.
    :param geo_data: The geolocation results dictionary containing "latitude", "longitude", and "accuracy" ports.
    :param filename: Name of the file to save the results to (default is "geolocation_results.txt")."""
    try:
        with open(filename, "w") as file:
            file.write("=" * 50 + "\n")
            file.write(f"Geolocation Results for IP: {geo_data['ip']}\n")
            file.write(f"Country: {geo_data['country']}\n")
            file.write("Region: {geo_data['region']}\n")
            file.write(f"City: {geo_data['city']}\n")
            file.write(f"ISP: {geo_data['isp']}\n")
            file.write(f"Latitude: {geo_data['lat']}\n")
            file.write(f"Longitude: {geo_data['lon']}\n")
            file.write(f"Google Maps Link: {generate_map_link(geo_data['lat'], geo_data['lon'])}\n")
            file.write("=" * 50 + "\n")
            print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")