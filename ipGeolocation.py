import requests
from ipChecker import checkIPType
from saveResults import save_geolocation_results
from history import view_geolocation_history


def get_geolocation_data(ip):
    """Get geolocation data for a given IP address."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        geo_data = response.json()

        # Extract latitude and longitude from the loc field (it is comma-separated)
        loc = geo_data.get('loc', '')
        if loc:
            lat, lon = loc.split(',')

        return {
            'ip': geo_data.get('ip'),
            'city': geo_data.get('city'),
            'region': geo_data.get('region'),
            'country': geo_data.get('country'),
            'lat': lat,
            'lon': lon,
            'isp': geo_data.get('org')
        }
    except Exception as e:
        print(f"Error getting geolocation data: {e}")
        return None


def ip_geolocator():
    # Ask if the user wants to view geolocation search history
    history_option = input("Do you want to view your geolocation search history? (yes/no): ").strip().lower()
    if history_option == "yes":
        view_geolocation_history()
        return  # Exit the program after viewing history

    # Ask if the user wants to input multiple IPs
    multiple_ips_option = input("\nDo you want to check multiple IP addresses? (yes/no): ").strip().lower()
    if multiple_ips_option == "yes":
        ip_addresses = input("Enter the IP addresses separated by commas: ").strip().split(',')
    else:
        # If only one IP address is needed
        ip_addresses = [input("Enter an IP address: ").strip()]

    # Process each IP address
    for ip in ip_addresses:
        ip_type = input(f"Enter IP type (4 for IPv4 / 6 for IPv6) for IP {ip}: ").strip()

        if checkIPType(ip_type, ip):
            print(f"IP address {ip} is valid!")

            # Get geolocation data
            geo_data = get_geolocation_data(ip)

            if geo_data:
                # Display the geolocation information
                print("\nGeolocation Information:")
                print(f"IP: {geo_data['ip']}")
                print(f"Country: {geo_data['country']}")
                print(f"Region: {geo_data['region']}")
                print(f"City: {geo_data['city']}")
                print(f"ISP: {geo_data['isp']}")
                print(f"Latitude: {geo_data['lat']}")
                print(f"Longitude: {geo_data['lon']}")
                print(f"Google Maps Link: https://www.google.com/maps?q={geo_data['lat']},{geo_data['lon']}")

                # Save results
                save_option = input("\nDo you want to save the geolocation results? (yes/no): ").strip().lower()
                if save_option == "yes":
                    save_geolocation_results(geo_data)

            else:
                print(f"Could not retrieve geolocation data for IP {ip}.")
        else:
            print(f"Invalid IP address: {ip}. Please check the IP address and try again.")


if __name__ == "__main__":
    ip_geolocator()
