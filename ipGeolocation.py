from ipChecker import checkIPType #ip validation
import requests #for API calls

def validate_ip(ip_type, ip):
    return checkIPType(ip_type, ip)

def get_geolocation(ip):
    try:
        #call API
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data.get("status") == "success":
            return {
                "ip": ip,
                "country": data.get("country", "unknown"), #unknown for unavailable data from API's response
                "region": data.get("region", "unknown"),
                "city": data.get("city", "unknown"),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "isp": data.get("isp", "unknown"),
            }
        else:
            return {"error": data.get("message", "Unknown Error")}
    except Exception as e:
        return {"error": e}


def generate_map_link(lat, lon):
    return f"https://www.google.com/maps?q={lat},{lon}"


def main():
    print("Welcome to IP Geolocation tool")
    print("Enter the ip addresses you want to locate (seperate with commmas): ")
    ips = input().strip()


    while True:
        ip_type = input("Please enter your IP type (4 for IPv4, 6 for IPv6): ").strip()
        if ip_type in ["4", "6"]:
            break
        else:
            print("Please enter a valid ip type.")

    ip = input ("Enter the IP address to locate: ").strip()

    if not validate_ip(ip_type, ip):
        print("Invalid IP address. Please restart and try again.")
        return

    print("IP address validated. Fetching geolocation data...")
    geo_data = get_geolocation(ip)

    if "error" in geo_data:
        print(f"Error fetching geolocation data: {geo_data['error']}")
    else:
        # geolocation details
        print("Geolocation Details:")
        print(f"  IP Address: {geo_data['ip']}")
        print(f"  Country: {geo_data['country']}")
        print(f"  Region: {geo_data['region']}")
        print(f"  City: {geo_data['city']}")
        print(f"  ISP: {geo_data['isp']}")
        print(f"  Latitude: {geo_data['lat']}")
        print(f"  Longitude: {geo_data['lon']}")

        # Google Maps link
        map_link = generate_map_link(geo_data['lat'], geo_data['lon'])
        print(f"Google Maps Link: {map_link}")

# run the script
if __name__ == "__main__":
    main()

